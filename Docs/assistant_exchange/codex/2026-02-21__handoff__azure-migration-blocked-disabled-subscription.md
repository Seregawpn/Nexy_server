# Azure Migration Blocked: Disabled Subscription

## Summary
Attempted to execute server migration to new Azure account from local workspace automation scripts.
Provisioning stopped at resource group creation due Azure API rejecting write operations.

## Executed
- Verified Azure login and account context.
- Prepared SSH private/public key pair at `~/.ssh/nexy_key.pem` and `~/.ssh/nexy_key.pem.pub`.
- Ran infrastructure script with explicit env:
  - `AZURE_RESOURCE_GROUP=NexyNewRG`
  - `AZURE_LOCATION=canadacentral`
  - `AZURE_VM_NAME=NexyNew`
  - `AZURE_VM_SIZE=Standard_D2s_v3`
  - `AZURE_ADMIN_USERNAME=azureuser`
  - `AZURE_ADMIN_IP=193.187.150.92/32`
  - `AZURE_SSH_KEY_PATH=/Users/sergiyzasorin/.ssh/nexy_key.pem`

## Blocking Error
Azure returned:
`ReadOnlyDisabledSubscription: The subscription '6ad75f5a-b865-4a45-9319-cc066ac37723' is disabled and therefore marked as read only.`

## Impact
- Cannot create Resource Group / VM / NSG / Public IP.
- Migration cannot proceed until subscription write access is restored.

## Required User Action
- Reactivate billing/subscription in Azure Portal for subscription `6ad75f5a-b865-4a45-9319-cc066ac37723`, or provide another active subscription with write permissions.

## Resume Plan
After reactivation:
1. `az account set --subscription <active-subscription-id>`
2. Re-run `server/scripts/create_azure_infrastructure.sh`
3. Run `server/scripts/setup_server.sh`
4. Run `server/scripts/verify_deployment.sh`
5. Proceed DNS cutover.
