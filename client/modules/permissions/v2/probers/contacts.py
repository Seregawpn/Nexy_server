"""
Permission System V2 - Contacts Prober

Probes Contacts permission using CNContactStore.
"""

from __future__ import annotations

import logging
from typing import Literal

from ..error_matrix import apply_normalization_to_evidence
from ..types import PermissionId, ProbeEvidence, ProbeResult, StepConfig
from .base import BaseProber

logger = logging.getLogger(__name__)


class ContactsProber(BaseProber):
    """Prober for Contacts permission."""
    
    def __init__(self, config: StepConfig):
        super().__init__(config)
        self.permission = PermissionId.CONTACTS
        self._last_result: bool | None = None
    
    async def trigger(self) -> None:
        """
        Trigger Contacts permission via CNContactStore.requestAccess().
        """
        try:
            from Contacts import (  # type: ignore[reportMissingImports, reportAttributeAccessIssue]
                CNContactStore,  # type: ignore[reportAttributeAccessIssue]
                CNEntityTypeContacts,  # type: ignore[reportAttributeAccessIssue]
            )
            
            store = CNContactStore.alloc().init()
            
            # Request access (async callback)
            def completion_handler(granted, error):
                if granted:
                    logger.debug("[CONTACTS_PROBER] Access granted via trigger")
                elif error:
                    logger.debug("[CONTACTS_PROBER] Access denied: %s", error)
            
            store.requestAccessForEntityType_completionHandler_(
                CNEntityTypeContacts,
                completion_handler
            )
            logger.debug("[CONTACTS_PROBER] Triggered contacts permission request")
            
        except ImportError as e:
            logger.warning("[CONTACTS_PROBER] Contacts framework not available: %s", e)
        except Exception as e:
            logger.warning("[CONTACTS_PROBER] Trigger failed: %s", e)
    
    async def probe(self, probe_kind: Literal["light", "heavy"]) -> ProbeResult:
        """Probe contacts capability."""
        ts = self._now()
        
        # Light probe: use cached
        if probe_kind == "light" and self._last_result is not None:
            ok = self._last_result
            domain, code, msg = None, None, None
        else:
            ok, domain, code, msg = await self._capability_contacts()
            self._last_result = ok
        
        ev = ProbeEvidence(
            contacts_fetch_ok=ok,
            error_domain=domain,
            error_code=code,
            error_message=msg,
        )
        ev = apply_normalization_to_evidence(self.permission, ev)
        
        return ProbeResult(
            permission=self.permission,
            timestamp=ts,
            probe_kind=probe_kind,
            evidence=ev
        )
    
    async def _capability_contacts(self) -> tuple[bool | None, str | None, str | None, str | None]:
        """
        Test Contacts capability by checking authorization status.
        Returns (contacts_fetch_ok, domain, code, message).
        """
        try:
            from Contacts import (  # type: ignore[reportMissingImports]
                CNAuthorizationStatusAuthorized,  # type: ignore[reportAttributeAccessIssue]
                CNAuthorizationStatusDenied,  # type: ignore[reportAttributeAccessIssue]
                CNAuthorizationStatusNotDetermined,  # type: ignore[reportAttributeAccessIssue]
                CNContactStore,  # type: ignore[reportAttributeAccessIssue]
                CNEntityTypeContacts,  # type: ignore[reportAttributeAccessIssue]
            )
            
            status = CNContactStore.authorizationStatusForEntityType_(CNEntityTypeContacts)  # type: ignore[reportAttributeAccessIssue]
            
            if status == CNAuthorizationStatusAuthorized:
                logger.debug("[CONTACTS_PROBER] Authorized")
                return True, None, None, None
            elif status == CNAuthorizationStatusDenied:
                logger.debug("[CONTACTS_PROBER] Denied")
                return False, "Contacts", "DENIED", "Contacts access denied"
            elif status == CNAuthorizationStatusNotDetermined:
                logger.debug("[CONTACTS_PROBER] Not determined")
                return None, "Contacts", "NOT_DETERMINED", "Contacts access not yet requested"
            else:
                return None, "Contacts", "UNKNOWN", f"Unknown status: {status}"
                
        except ImportError as e:
            logger.warning("[CONTACTS_PROBER] Contacts framework not available: %s", e)
            return None, "import", None, str(e)
        except Exception as e:
            logger.error("[CONTACTS_PROBER] Contacts test failed: %s", e)
            return None, "Contacts", type(e).__name__, str(e)
    
    def supports_light_probe(self) -> bool:
        return True
