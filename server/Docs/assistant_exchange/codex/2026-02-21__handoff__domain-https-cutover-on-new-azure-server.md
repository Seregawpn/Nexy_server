# Domain HTTPS Cutover on New Azure Server

## Objective
Replicate previous server access style (HTTPS by hostname, not bare IP) on the new Azure server.

## Implemented
1. Assigned free Azure Public DNS hostname to VM public IP resource:
   - Public IP: `nexy-new-public-ip`
   - FQDN: `nexy-prod-sergiy.canadacentral.cloudapp.azure.com`
   - IP: `20.104.80.82`
2. Updated Nginx server name on VM to domain host.
3. Installed Certbot and issued Let's Encrypt certificate for the domain.
4. Cert deployed to Nginx (`/etc/letsencrypt/live/.../fullchain.pem`, `privkey.pem`).
5. Enabled and validated renewal timer:
   - `certbot.timer` -> enabled/active.
6. Verified external HTTPS:
   - `https://nexy-prod-sergiy.canadacentral.cloudapp.azure.com/health` -> `HTTP/2 200`
   - TLS subject CN matches domain; issuer Let's Encrypt.

## Source of Truth
- Public host: `nexy-prod-sergiy.canadacentral.cloudapp.azure.com`

## Additional Sync
- Replaced active script/docs references from direct IP to domain host in:
  - `Docs/*` (active only)
  - `server/Docs/*` (active only)
  - `server/scripts/*`
  - `azure_infrastructure_info.txt`
- Excluded archives and assistant exchange history.

## Notes
- One earlier certbot run used wrong shell interpolation and produced invalid email/server_name; corrected via direct SSH execution on VM.
- A stale `certbot renew --dry-run` process lock was cleared; final state is healthy.

## Final Verification Snapshot
- `curl -I https://nexy-prod-sergiy.canadacentral.cloudapp.azure.com/health` => `200`
- TLS:
  - `subject=CN=nexy-prod-sergiy.canadacentral.cloudapp.azure.com`
  - `issuer=Let's Encrypt (R13)`
- VM endpoint payload health reports service OK.
