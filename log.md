default 21:53:57.154509-0500 StorageManagementService <STMOpaqueExtension:0x7fdec9812200 <EXConcreteExtension: 0x7fdec9815e40> {id = com.apple.STMExtension.Applications}> finished processing (
    "<NSExtensionItem: 0x7fdec7f0b8f0> - userInfo: {\n    \"_KIND_\" = COMMAND;\n    \"\\U2022COMMAND\" = \"RESOURCE_SHOW\";\n}",
    "<NSExtensionItem: 0x7fdec8f247e0> - userInfo: {\n    \"_APP_SIZE_\" = 200192000;\n    \"_BUNDLE_ID_\" = \"com.nexy.assistant\";\n    \"_CATEGORY_\" = iOS;\n    \"_CREATED_\" = \"2025-11-14 14:44:37 +0000\";\n    \"_DELETABLE_\" = 1;\n    \"_DELETABLE_SIZE_\" = 200192000;\n    \"_ICON_CONSTRUCTOR_\" = {length = 306, bytes = 0x62706c69 73743030 d4010203 04050607 ... 00000000 000000f5 };\n    \"_KIND_\" = RESOURCE;\n    \"_MODIFIED_\" = \"2025-11-17 02:53:13 +0000\";\n    \"_NAME_\" = Nexy;\n    \"_OPENED_\" = \"2025-11-17 02:53:13 +0000\";\n    \"_REVEALABLE_\" = 1;\n    \"_URL_\" = \"file:///Applications/Nexy.app/\";\n    \"_VERSION_\" = \"1.0.0\";\n}"
): result count 1, error (null)
default 21:53:58.048840-0500 CategoriesService Performing iTunes lookup on behalf of com.apple.dmd: (
    "com.nexy.assistant"
)
default 21:53:58.252078-0500 CategoriesService Performing iTunes lookup on behalf of com.apple.dmd: (
    "com.nexy.assistant"
)
default 21:53:58.345566-0500 dmd Requested application com.nexy.assistant has policy OK, associated categories:DH1009 associated sites:(null) equivalent bundle identifiers:com.nexy.assistant
default 21:53:59.749223-0500 lsd com.nexy.assistant/Unknown Persona:5:5:1:1:Building bundle record for app
default 21:53:59.749459-0500 lsd com.nexy.assistant/Unknown Persona:5:5:2:1:Built bundle record for app
default 21:53:59.854703-0500 lsd com.nexy.assistant/Unknown Persona:5:4:2:1:_LSServerRegisterItemInfo result = 0
error 21:53:59.860877-0500 CoreServicesUIAgent LAUNCH:Application cannot be launched because its unsupported bit is set, com.nexy.assistant node=<FSNode 0x600002e6c6c0> { isDir = y, path = <private> } status=-10661
default 21:53:59.861399-0500 dmd Received xpc stream event (distributed notification matching) with name: com.apple.LaunchServices.applicationRegistered user info: {
    CFBundleDisplayName = Nexy;
    bundleIDs =     (
        "com.nexy.assistant"
    );
    isPlaceholder = 0;
}