import builtins
import sys

from modules.permissions.macos.accessibility_handler import AccessibilityHandler


def test_check_accessibility_permission_uses_public_ax_api(monkeypatch):
    """
    Ensure we rely on the public AXIsProcessTrustedWithOptions API and pass prompt=False.
    """
    calls: dict[str, object] = {}

    class DummyNSNumber:
        @staticmethod
        def numberWithBool_(value):
            calls["prompt_value"] = value
            return f"NSNumber({value})"

    class DummyNSDictionary:
        @staticmethod
        def dictionaryWithObject_forKey_(obj, key):
            calls["options_obj"] = obj
            calls["options_key"] = key
            return {"obj": obj, "key": key}

    def ax_mock(options):
        calls["ax_called_with"] = options
        return True

    class DummyQuartz:
        AXIsProcessTrustedWithOptions = staticmethod(ax_mock)
        kAXTrustedCheckOptionPrompt = "kAXTrustedCheckOptionPrompt"

    class DummyFoundation:
        NSDictionary = DummyNSDictionary
        NSNumber = DummyNSNumber

    monkeypatch.setitem(sys.modules, "Quartz", DummyQuartz)
    monkeypatch.setitem(sys.modules, "Foundation", DummyFoundation)

    handler = AccessibilityHandler()
    assert handler.check_accessibility_permission() is True
    assert calls["prompt_value"] is False
    assert calls["options_key"] == DummyQuartz.kAXTrustedCheckOptionPrompt
    assert calls["ax_called_with"] == {
        "obj": "NSNumber(False)",
        "key": DummyQuartz.kAXTrustedCheckOptionPrompt,
    }


def test_check_accessibility_permission_handles_missing_quartz(monkeypatch):
    """
    If Quartz is unavailable, we should return False without raising.
    """
    real_import = builtins.__import__

    def raising_import(name, *args, **kwargs):
        if name in {"Quartz", "Foundation"}:
            raise ImportError("Quartz not available")
        return real_import(name, *args, **kwargs)

    monkeypatch.setattr(builtins, "__import__", raising_import)

    handler = AccessibilityHandler()
    assert handler.check_accessibility_permission() is False
