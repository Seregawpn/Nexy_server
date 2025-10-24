 default	14:02:46.882658-0400	lsd	com.nexy.assistant/Unknown Persona:5:5:1:1:Building bundle record for app
default	14:02:46.882817-0400	lsd	com.nexy.assistant/Unknown Persona:5:5:2:1:Built bundle record for app
default	14:02:46.884512-0400	lsd	com.nexy.assistant/Unknown Persona:5:4:2:1:_LSServerRegisterItemInfo result = 0
default	14:02:46.890877-0400	runningboardd	Launch request for app<application.com.nexy.assistant.17524881.17524887(501)>[0] is using uid 501 (divined from auid 501 euid 501)
default	14:02:46.890959-0400	runningboardd	Acquiring assertion targeting app<application.com.nexy.assistant.17524881.17524887(501)> from originator [osservice<com.apple.coreservices.uiagent(501)>:590] with description <RBSAssertionDescriptor| "LS launch com.nexy.assistant" ID:398-590-42751 target:app<application.com.nexy.assistant.17524881.17524887(501)> attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"LaunchRoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	14:02:46.891031-0400	runningboardd	Assertion 398-590-42751 (target:app<application.com.nexy.assistant.17524881.17524887(501)>) will be created as active
default	14:02:46.890177-0400	dmd	Received xpc stream event (distributed notification matching) with name: com.apple.LaunchServices.applicationRegistered user info: {
    CFBundleDisplayName = Nexy;
    bundleIDs =     (
        "com.nexy.assistant"
    );
    isPlaceholder = 0;
}
default	14:02:46.895307-0400	runningboardd	Checking PreventLaunch: global:0 exPath:/Applications/Nexy.app/Contents/MacOS/Nexy predicates:(null) allow:(null)
default	14:02:46.895338-0400	runningboardd	Creating and launching job for: app<application.com.nexy.assistant.17524881.17524887(501)>
default	14:02:46.895351-0400	runningboardd	_mutateContextIfNeeded called for com.nexy.assistant
default	14:02:46.895411-0400	runningboardd	app<application.com.nexy.assistant.17524881.17524887(501)>: -[RBPersonaManager personaForIdentity:context:personaUID:personaUniqueString:] required 0.000954 ms (wallclock); resolved to {4294967295, (null)}
default	14:02:46.922288-0400	runningboardd	[app<application.com.nexy.assistant.17524881.17524887(501)>:31544] is not RunningBoard jetsam managed.
default	14:02:46.922303-0400	runningboardd	[app<application.com.nexy.assistant.17524881.17524887(501)>:31544] This process will not be managed.
default	14:02:46.922314-0400	runningboardd	Now tracking process: [app<application.com.nexy.assistant.17524881.17524887(501)>:31544]
default	14:02:46.922461-0400	runningboardd	Calculated state for app<application.com.nexy.assistant.17524881.17524887(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	14:02:46.923089-0400	gamepolicyd	Hit the server for a process handle cb8cfaf00007b38 that resolved to: [app<application.com.nexy.assistant.17524881.17524887(501)>:31544]
default	14:02:46.923124-0400	gamepolicyd	Received state update for 31544 (app<application.com.nexy.assistant.17524881.17524887(501)>, running-active-NotVisible
default	14:02:46.927308-0400	runningboardd	Using default underlying assertion for app: [app<application.com.nexy.assistant.17524881.17524887(501)>:31544]
default	14:02:46.927376-0400	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.17524881.17524887(501)>:31544] from originator [app<application.com.nexy.assistant.17524881.17524887(501)>:31544] with description <RBSAssertionDescriptor| "RB Underlying Assertion" ID:398-398-42752 target:31544 attributes:[
	<RBSDomainAttribute| domain:"com.apple.underlying" name:"defaultUnderlyingAppAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	14:02:46.927493-0400	runningboardd	Assertion 398-398-42752 (target:[app<application.com.nexy.assistant.17524881.17524887(501)>:31544]) will be created as active
default	14:02:46.927684-0400	runningboardd	[app<application.com.nexy.assistant.17524881.17524887(501)>:31544] Ignoring jetsam update because this process is not memory-managed
default	14:02:46.927699-0400	runningboardd	[app<application.com.nexy.assistant.17524881.17524887(501)>:31544] Ignoring suspend because this process is not lifecycle managed
default	14:02:46.927719-0400	runningboardd	[app<application.com.nexy.assistant.17524881.17524887(501)>:31544] Set darwin role to: UserInteractive
default	14:02:46.927736-0400	runningboardd	[app<application.com.nexy.assistant.17524881.17524887(501)>:31544] Ignoring GPU update because this process is not GPU managed
default	14:02:46.927769-0400	runningboardd	[app<application.com.nexy.assistant.17524881.17524887(501)>:31544] Ignoring memory limit update because this process is not memory-managed
default	14:02:46.927809-0400	runningboardd	[app<application.com.nexy.assistant.17524881.17524887(501)>:31544] reported to RB as running
default	14:02:46.929085-0400	runningboardd	[app<application.com.nexy.assistant.17524881.17524887(501)>:31544] Ignoring jetsam update because this process is not memory-managed
default	14:02:46.929126-0400	runningboardd	[app<application.com.nexy.assistant.17524881.17524887(501)>:31544] Ignoring suspend because this process is not lifecycle managed
default	14:02:46.929188-0400	runningboardd	[app<application.com.nexy.assistant.17524881.17524887(501)>:31544] Ignoring GPU update because this process is not GPU managed
default	14:02:46.929275-0400	runningboardd	[app<application.com.nexy.assistant.17524881.17524887(501)>:31544] Ignoring memory limit update because this process is not memory-managed
default	14:02:46.929323-0400	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.17524881.17524887(501)>:31544] from originator [osservice<com.apple.coreservices.launchservicesd>:363] with description <RBSAssertionDescriptor| "uielement:31544" ID:398-363-42753 target:31544 attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"RoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	14:02:46.929419-0400	runningboardd	Assertion 398-363-42753 (target:[app<application.com.nexy.assistant.17524881.17524887(501)>:31544]) will be created as active
default	14:02:46.929442-0400	runningboardd	Successfully acquired underlying assertion for [app<application.com.nexy.assistant.17524881.17524887(501)>:31544]
default	14:02:46.930221-0400	loginwindow	-[Application updateInformation] | Got App URL: file:///Applications/Nexy.app/
default	14:02:46.929367-0400	CoreServicesUIAgent	LAUNCH: 0x0-0x3a93a9 com.nexy.assistant starting stopped process.
default	14:02:46.935266-0400	runningboardd	Calculated state for app<application.com.nexy.assistant.17524881.17524887(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	14:02:46.935595-0400	runningboardd	Invalidating assertion 398-590-42751 (target:app<application.com.nexy.assistant.17524881.17524887(501)>) from originator [osservice<com.apple.coreservices.uiagent(501)>:590]
default	14:02:46.935672-0400	runningboardd	[app<application.com.nexy.assistant.17524881.17524887(501)>:31544] Ignoring jetsam update because this process is not memory-managed
default	14:02:46.935686-0400	runningboardd	[app<application.com.nexy.assistant.17524881.17524887(501)>:31544] Ignoring suspend because this process is not lifecycle managed
default	14:02:46.935693-0400	runningboardd	[app<application.com.nexy.assistant.17524881.17524887(501)>:31544] Ignoring GPU update because this process is not GPU managed
default	14:02:46.935810-0400	runningboardd	[app<application.com.nexy.assistant.17524881.17524887(501)>:31544] Ignoring memory limit update because this process is not memory-managed
default	14:02:46.936253-0400	gamepolicyd	Received state update for 31544 (app<application.com.nexy.assistant.17524881.17524887(501)>, running-active-NotVisible
default	14:02:46.936738-0400	loginwindow	-[ApplicationManager checkInAppContext:eventData:] | ApplicationManager: Checked in app : Nexy
default	14:02:46.940624-0400	runningboardd	Calculated state for app<application.com.nexy.assistant.17524881.17524887(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	14:02:47.036720-0400	runningboardd	[app<application.com.nexy.assistant.17524881.17524887(501)>:31544] Ignoring jetsam update because this process is not memory-managed
default	14:02:47.036741-0400	runningboardd	[app<application.com.nexy.assistant.17524881.17524887(501)>:31544] Ignoring suspend because this process is not lifecycle managed
default	14:02:47.036761-0400	runningboardd	[app<application.com.nexy.assistant.17524881.17524887(501)>:31544] Ignoring GPU update because this process is not GPU managed
default	14:02:47.036798-0400	gamepolicyd	Received state update for 31544 (app<application.com.nexy.assistant.17524881.17524887(501)>, running-active-NotVisible
default	14:02:47.036794-0400	runningboardd	[app<application.com.nexy.assistant.17524881.17524887(501)>:31544] Ignoring memory limit update because this process is not memory-managed
default	14:02:47.059833-0400	syspolicyd	GK evaluateScanResult: 3, PST: (path: a2cffff67b96be6e), (team: 5NKLL2CLB9), (id: com.nexy.assistant), (bundle_id: (null)), 0, 0, 1, 0, 9, 4, 1
default	14:02:47.061707-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=511.23, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=31544, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.syspolicyd, pid=511, auid=0, euid=0, binary_path=/usr/libexec/syspolicyd}, },
default	14:02:47.071070-0400	tccd	AUTHREQ_SUBJECT: msgID=511.23, subject=com.nexy.assistant,
default	14:02:47.071829-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d116700 at /Applications/Nexy.app
default	14:02:47.450941-0400	Nexy	[0x103592ba0] activating connection: mach=true listener=false peer=false name=com.apple.cfprefsd.daemon
default	14:02:47.451023-0400	Nexy	[0x103592ce0] activating connection: mach=true listener=false peer=false name=com.apple.cfprefsd.agent
error	14:02:47.594639-0400	Nexy	dlsym cannot find symbol NSMakeRect in CFBundle 0xb8f7880e0 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	14:02:47.594882-0400	Nexy	dlsym cannot find symbol NSMakePoint in CFBundle 0xb8f7880e0 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	14:02:47.595098-0400	Nexy	dlsym cannot find symbol NSMakeSize in CFBundle 0xb8f7880e0 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	14:02:47.595305-0400	Nexy	dlsym cannot find symbol NSMakeRange in CFBundle 0xb8f7880e0 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
default	14:02:47.687206-0400	Nexy	Registered notify signal com.apple.caulk.alloc.rtdump (0)
default	14:02:47.691217-0400	Nexy	System_Input_Processing_Notification_Handler.mm:456   System_Input_Processing_Notification_Handler::is_vi_available(): Voice isolation DSP is available for client with bundle id com.nexy.assistant (AVFoundation is available, application is not in client deny list, application is not FaceTime variant)
default	14:02:47.692594-0400	Nexy	[0x1035937a0] activating connection: mach=true listener=false peer=false name=com.apple.cmio.registerassistantservice.system-extensions
fault	14:02:47.695715-0400	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.17524881.17524887 AUID=501> and <type=Application identifier=application.com.nexy.assistant.17524881.17524887>
default	14:02:47.699857-0400	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOInitializeListenersForBundleID: for <private> -> <private>
default	14:02:47.701581-0400	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> vpio_preferenceChangedListener: new value ((null)) for key AUVoiceIOClients/com-nexy-assistant/AUVoiceIOChatFlavor, translatedBundleID com.nexy.assistant, bundleIDs {(
    "com.nexy.assistant"
)}
default	14:02:47.701785-0400	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> vpio_preferenceChangedListener: new value ((null)) for key AUVoiceIOClients/com-nexy-assistant/AUVoiceIOIsAutoChatFlavorEnabled, translatedBundleID com.nexy.assistant, bundleIDs {(
    "com.nexy.assistant"
)}
default	14:02:47.701936-0400	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetSupportedChatFlavorsForBundleID: <private>-><private> get supported chat flavors: <private>
default	14:02:47.701946-0400	Nexy	            HALSystem.cpp:134    Enabling HAL Voice Isolation support
default	14:02:47.701978-0400	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetHiddenChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	14:02:47.702148-0400	Nexy	[0xb8f938000] activating connection: mach=true listener=false peer=false name=com.apple.tccd
default	14:02:47.702666-0400	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOHiddenChatFlavors newValue: (
    1
)
default	14:02:47.702727-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=31544.1, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=31544, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	14:02:47.709074-0400	tccd	AUTHREQ_SUBJECT: msgID=31544.1, subject=com.nexy.assistant,
default	14:02:47.709693-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc5f149200 at /Applications/Nexy.app
default	14:02:47.720309-0400	Nexy	[0xb8f938000] invalidated after the last release of the connection object
default	14:02:47.720355-0400	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetSupportedChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	14:02:47.722640-0400	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOSupportedChatFlavors newValue: (
)
default	14:02:47.725004-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=401.1248, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=31544, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	14:02:47.725754-0400	tccd	AUTHREQ_SUBJECT: msgID=401.1248, subject=com.nexy.assistant,
default	14:02:47.726267-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc5f149200 at /Applications/Nexy.app
error	14:02:47.737128-0400	tccd	Request message contains a target_token to accessing_process (TCCDProcess: identifier=com.nexy.assistant, pid=31544, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy) but TCCDProcess: identifier=com.apple.audio.coreaudiod, pid=401, auid=202, euid=202, binary_path=/usr/sbin/coreaudiod is not a TCC manager for service: kTCCServiceScreenCapture.
default	14:02:47.737983-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=401.1250, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=31544, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	14:02:47.738652-0400	tccd	AUTHREQ_SUBJECT: msgID=401.1250, subject=com.nexy.assistant,
default	14:02:47.739150-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc5f149200 at /Applications/Nexy.app
default	14:02:47.751493-0400	Nexy	  HALPlugInManagement.cpp:440    HALPlugInManagement::RegisterPlugIns: skipping in-process plug-ins
error	14:02:47.751509-0400	Nexy	AddInstanceForFactory: No factory registered for id <CFUUID 0xb8eba0140> F8BB1C28-BAE8-11D6-9C31-00039315CD46
default	14:02:47.766084-0400	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetPreferredChatFlavorForBundleID: <private>-><private> get value: 0
default	14:02:49.997096-0400	Nexy	[0xb8f938000] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
error	14:02:49.997744-0400	tccd	TCCDProcess: identifier=com.nexy.assistant, pid=31544, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy attempted to call TCCAccessRequest for kTCCServiceAccessibility without the recommended com.apple.private.tcc.manager.check-by-audit-token entitlement
default	14:02:49.997915-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=31544.2, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=31544, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.nexy.assistant, pid=31544, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	14:02:49.999428-0400	tccd	AUTHREQ_SUBJECT: msgID=31544.2, subject=com.nexy.assistant,
default	14:02:50.000124-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d116700 at /Applications/Nexy.app
default	14:02:50.011686-0400	Nexy	[0xb8f938000] invalidated after the last release of the connection object
default	14:02:50.012550-0400	Nexy	[0xb8f938000] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
error	14:02:50.012914-0400	tccd	TCCDProcess: identifier=com.nexy.assistant, pid=31544, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy attempted to call TCCAccessRequest for kTCCServiceAccessibility without the recommended com.apple.private.tcc.manager.check-by-audit-token entitlement
default	14:02:50.013067-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=31544.3, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=31544, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.nexy.assistant, pid=31544, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	14:02:50.013870-0400	tccd	AUTHREQ_SUBJECT: msgID=31544.3, subject=com.nexy.assistant,
default	14:02:50.014456-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d116700 at /Applications/Nexy.app
default	14:02:50.025321-0400	Nexy	[0xb8f938000] invalidated after the last release of the connection object
default	14:02:50.025394-0400	Nexy	[0xb8f938000] activating connection: mach=true listener=false peer=false name=com.apple.distributed_notifications@Uv3
default	14:02:50.025522-0400	Nexy	[0xb8f938140] activating connection: mach=true listener=false peer=false name=com.apple.universalaccessAuthWarn
default	14:02:50.025603-0400	Nexy	[0xb8f938140] invalidated after the last release of the connection object
default	14:02:50.025939-0400	Nexy	[0xb8f938280] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	14:02:50.026432-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=31544.4, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=31544, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	14:02:50.027437-0400	tccd	AUTHREQ_SUBJECT: msgID=31544.4, subject=com.nexy.assistant,
default	14:02:50.028121-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d116700 at /Applications/Nexy.app
default	14:02:50.040807-0400	tccd	Notifying for access  kTCCServiceListenEvent for target PID[31544], responsiblePID[31544], responsiblePath: /Applications/Nexy.app to UID: 501
default	14:02:50.041049-0400	Nexy	[0xb8f938280] invalidated after the last release of the connection object
default	14:02:50.041397-0400	Nexy	server port 0x00008c13, session port 0x00009a0f
default	14:02:50.042326-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=393.2088, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=31544, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=393, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	14:02:50.042356-0400	tccd	requestor: TCCDProcess: identifier=com.apple.WindowServer, pid=393, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=31544, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	14:02:50.043195-0400	tccd	AUTHREQ_SUBJECT: msgID=393.2088, subject=com.nexy.assistant,
default	14:02:50.043828-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d1db600 at /Applications/Nexy.app
default	14:02:50.072798-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d116700 at /Applications/Nexy.app
default	14:02:50.080754-0400	kernel	SK[6]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 894EF5C8-0FBA-4372-B4F6-5C78A504CDD1 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.56798,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0xd6d41b46 tp_proto=0x06"
default	14:02:50.080884-0400	kernel	tcp connect outgoing: [<IPv4-redacted>:56798<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 610233 t_state: SYN_SENT process: Nexy:31544 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x9002dda3
default	14:02:50.088929-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117900 at /Applications/Nexy.app
default	14:02:50.092920-0400	tccd	Publishing <TCCDEvent: type=Modify, service=kTCCServiceAccessibility, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 0 subscribers: {
}
default	14:02:50.098584-0400	kernel	tcp connected: [<IPv4-redacted>:56798<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 610233 t_state: ESTABLISHED process: Nexy:31544 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x9002dda3
default	14:02:50.098978-0400	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:56798<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 610233 t_state: FIN_WAIT_1 process: Nexy:31544 Duration: 0.018 sec Conn_Time: 0.018 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 18.000 ms rttvar: 9.000 ms base rtt: 18 ms so_error: 0 svc/tc: 0 flow: 0x9002dda3
default	14:02:50.098989-0400	kernel	tcp_connection_summary [<IPv4-redacted>:56798<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 610233 t_state: FIN_WAIT_1 process: Nexy:31544 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	14:02:50.126729-0400	Nexy	[0xb8f938280] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioComponentRegistrar
default	14:02:50.138036-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d116700 at /Applications/Nexy.app
default	14:02:50.140204-0400	Nexy	                AUHAL.cpp:420   AUHAL: (0xb8f8bf840) Selecting device 71 from constructor
default	14:02:50.140217-0400	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0xb8f8bf840)
default	14:02:50.140225-0400	Nexy	                AUHAL.cpp:676   SelectDevice: (0xb8f8bf840) not already running
default	14:02:50.140230-0400	Nexy	                AUHAL.cpp:752   SelectDevice: (0xb8f8bf840) nothing to teardown
default	14:02:50.140244-0400	Nexy	                AUHAL.cpp:757   SelectDevice: (0xb8f8bf840) connecting device 71
default	14:02:50.140386-0400	Nexy	                AUHAL.cpp:3413  IsDeviceUsable: (0xb8f8bf840) Device ID: 71 (Input:No | Output:Yes): true
default	14:02:50.140499-0400	Nexy	                AUHAL.cpp:769   SelectDevice: (0xb8f8bf840) created ioproc 0xa for device 71
default	14:02:50.140607-0400	Nexy	                AUHAL.cpp:858   SelectDevice: (0xb8f8bf840) adding 7 device listeners to device 71
default	14:02:50.140790-0400	Nexy	                AUHAL.cpp:858   SelectDevice: (0xb8f8bf840) adding 0 device delegate listeners to device 71
default	14:02:50.140799-0400	Nexy	                AUHAL.cpp:1581  UpdateStreamFormats: -> (0xb8f8bf840)
default	14:02:50.140880-0400	Nexy	                AUHAL.cpp:1677  UpdateStreamFormats: 
  output stream 0 [0x48]:  2 ch,  48000 Hz, Float32, interleaved
default	14:02:50.140889-0400	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 1 output streams; not all mono
default	14:02:50.140896-0400	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	14:02:50.140902-0400	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 0 input streams; not all mono
default	14:02:50.140909-0400	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	14:02:50.141012-0400	Nexy	                AUHAL.cpp:1771  UpdateStreamFormats: AUHAL(0xb8f8bf840) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	14:02:50.141024-0400	Nexy	                AUHAL.cpp:1777  UpdateStreamFormats: AUHAL(0xb8f8bf840) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	14:02:50.141030-0400	Nexy	                AUHAL.cpp:1787  UpdateStreamFormats: <-
default	14:02:50.141035-0400	Nexy	                AUHAL.cpp:895   SelectDevice: (0xb8f8bf840) removing 0 device listeners from device 0
default	14:02:50.141038-0400	Nexy	                AUHAL.cpp:895   SelectDevice: (0xb8f8bf840) removing 0 device delegate listeners from device 0
default	14:02:50.141043-0400	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0xb8f8bf840)
default	14:02:50.141060-0400	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Output stream enables: Stream 0 is DISABLED
default	14:02:50.141150-0400	Nexy	                AUHAL.cpp:2298  SetProperty: (0xb8f8bf840) caller requesting device change from 71 to 78
default	14:02:50.141160-0400	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0xb8f8bf840)
default	14:02:50.141166-0400	Nexy	                AUHAL.cpp:676   SelectDevice: (0xb8f8bf840) not already running
default	14:02:50.141171-0400	Nexy	                AUHAL.cpp:682   SelectDevice: (0xb8f8bf840) disconnecting device 71
default	14:02:50.141175-0400	Nexy	                AUHAL.cpp:746   SelectDevice: (0xb8f8bf840) destroying ioproc 0xa for device 71
default	14:02:50.141226-0400	Nexy	  AVAudioSession_MacOS.mm:1021  initForMacOS
default	14:02:50.141774-0400	Nexy	[0xb8f938500] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioSession
default	14:02:50.142492-0400	audiomxd	  ServerSessionManager.mm:315   { "action":"create_session", "session":{"ID":"0x1ef03f","name":"Nexy(31544)"}, "details":{"PID":31544,"session_type":"Primary"} }
default	14:02:50.142569-0400	audiomxd	AudioApplicationInfoImpl.mm:250   Setting initial isRecording state: 0 for newly-created AudioApp
	app: {"name":"[implicit] Nexy","pid":31544}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1ef03f, sessionType: 'prim', isRecording: false }, 
]
default	14:02:50.143141-0400	audiomxd	  ServerSessionManager.mm:1317  Start process monitoring, pid = 31544, name = Nexy
default	14:02:50.143383-0400	Nexy	    SessionCore_Create.mm:99    Created session 0xb8f7aaa20 with ID: 0x1ef03f
default	14:02:50.143887-0400	Nexy	[0xb8f938640] activating connection: mach=true listener=false peer=false name=com.apple.audioanalyticsd
default	14:02:50.143994-0400	Nexy	No persisted cache on this platform.
error	14:02:50.144262-0400	Nexy	Reporter disconnected. { function=sendMessage, reporterID=135480448385025 }
default	14:02:50.144275-0400	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped Unknown {BuiltInSpeakerDevice, 0xa}
default	14:02:50.144326-0400	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	14:02:50.144424-0400	Nexy	                AUHAL.cpp:757   SelectDevice: (0xb8f8bf840) connecting device 78
default	14:02:50.144510-0400	Nexy	                AUHAL.cpp:3413  IsDeviceUsable: (0xb8f8bf840) Device ID: 78 (Input:Yes | Output:No): true
default	14:02:50.145926-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=401.1251, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=31544, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	14:02:50.146977-0400	tccd	AUTHREQ_SUBJECT: msgID=401.1251, subject=com.nexy.assistant,
default	14:02:50.147680-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc5f149200 at /Applications/Nexy.app
default	14:02:50.153146-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117900 at /Applications/Nexy.app
default	14:02:50.157866-0400	tccd	Publishing <TCCDEvent: type=Modify, service=kTCCServiceListenEvent, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 0 subscribers: {
}
default	14:02:50.163275-0400	tccd	AUTHREQ_PROMPTING: msgID=401.1251, service=kTCCServiceMicrophone, subject=Sub:{com.nexy.assistant}Resp:{TCCDProcess: identifier=com.nexy.assistant, pid=31544, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy},
default	14:02:51.392848-0400	tccd	Publishing <TCCDEvent: type=Create, service=kTCCServiceMicrophone, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 3 subscribers: {
    471 = "<TCCDEventSubscriber: token=471, state=Passed, csid=com.apple.chronod>";
    37 = "<TCCDEventSubscriber: token=37, state=Initial, csid=(null)>";
    476 = "<TCCDEventSubscriber: token=476, state=Passed, csid=com.apple.photolibraryd>";
}
default	14:02:51.393620-0400	chronod	[appAuth:com.nexy.assistant] tcc authorization(s) changed
default	14:02:51.393625-0400	Nexy	                AUHAL.cpp:769   SelectDevice: (0xb8f8bf840) created ioproc 0xa for device 78
default	14:02:51.393842-0400	Nexy	                AUHAL.cpp:858   SelectDevice: (0xb8f8bf840) adding 7 device listeners to device 78
default	14:02:51.394155-0400	Nexy	                AUHAL.cpp:858   SelectDevice: (0xb8f8bf840) adding 0 device delegate listeners to device 78
default	14:02:51.394170-0400	Nexy	                AUHAL.cpp:1581  UpdateStreamFormats: -> (0xb8f8bf840)
default	14:02:51.394186-0400	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 0 output streams; not all mono
default	14:02:51.394215-0400	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Output render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	14:02:51.394440-0400	Nexy	                AUHAL.cpp:1677  UpdateStreamFormats: 
  input stream 0 [0x4f]:  1 ch,  48000 Hz, Float32
default	14:02:51.394452-0400	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 1 input streams; all mono
default	14:02:51.394459-0400	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Input render format:  1 ch,  48000 Hz, Float32
default	14:02:51.394596-0400	Nexy	                AUHAL.cpp:1771  UpdateStreamFormats: AUHAL(0xb8f8bf840) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	14:02:51.394620-0400	Nexy	                AUHAL.cpp:1777  UpdateStreamFormats: AUHAL(0xb8f8bf840) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	14:02:51.394629-0400	Nexy	                AUHAL.cpp:1787  UpdateStreamFormats: <-
default	14:02:51.394635-0400	Nexy	                AUHAL.cpp:895   SelectDevice: (0xb8f8bf840) removing 7 device listeners from device 71
default	14:02:51.394865-0400	Nexy	                AUHAL.cpp:895   SelectDevice: (0xb8f8bf840) removing 0 device delegate listeners from device 71
default	14:02:51.394880-0400	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0xb8f8bf840)
default	14:02:51.395447-0400	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	14:02:51.397315-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=401.1252, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=31544, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	14:02:51.398901-0400	tccd	AUTHREQ_SUBJECT: msgID=401.1252, subject=com.nexy.assistant,
default	14:02:51.399951-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc5f149200 at /Applications/Nexy.app
default	14:02:51.415685-0400	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	14:02:51.416985-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=401.1253, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=31544, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	14:02:51.418013-0400	tccd	AUTHREQ_SUBJECT: msgID=401.1253, subject=com.nexy.assistant,
default	14:02:51.418608-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc5f149200 at /Applications/Nexy.app
default	14:02:51.431826-0400	Nexy	Registered notify signal com.apple.caulk.alloc.audiodump (0)
default	14:02:51.433553-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=401.1254, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=31544, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	14:02:51.434506-0400	tccd	AUTHREQ_SUBJECT: msgID=401.1254, subject=com.nexy.assistant,
default	14:02:51.435098-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc5f149200 at /Applications/Nexy.app
default	14:02:51.447293-0400	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetPreferredChatFlavorForBundleID: <private>-><private> get value: 0
default	14:02:51.447784-0400	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetSupportedChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	14:02:51.448333-0400	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.17524881.17524887(501)>:31544] from originator [osservice<com.apple.powerd>:334] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:398-334-42762 target:31544 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	14:02:51.448417-0400	runningboardd	Assertion 398-334-42762 (target:[app<application.com.nexy.assistant.17524881.17524887(501)>:31544]) will be created as active
default	14:02:51.448762-0400	runningboardd	[app<application.com.nexy.assistant.17524881.17524887(501)>:31544] Ignoring jetsam update because this process is not memory-managed
default	14:02:51.448801-0400	runningboardd	[app<application.com.nexy.assistant.17524881.17524887(501)>:31544] Ignoring suspend because this process is not lifecycle managed
default	14:02:51.448839-0400	runningboardd	[app<application.com.nexy.assistant.17524881.17524887(501)>:31544] Ignoring GPU update because this process is not GPU managed
default	14:02:51.448915-0400	runningboardd	[app<application.com.nexy.assistant.17524881.17524887(501)>:31544] Ignoring memory limit update because this process is not memory-managed
default	14:02:51.450525-0400	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOSupportedChatFlavors newValue: (
    0,
    2
)
default	14:02:51.459434-0400	runningboardd	Calculated state for app<application.com.nexy.assistant.17524881.17524887(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	14:02:51.460246-0400	gamepolicyd	Received state update for 31544 (app<application.com.nexy.assistant.17524881.17524887(501)>, running-active-NotVisible
default	14:02:51.473844-0400	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Input {BuiltInMicrophoneDevice, 0xa}
default	14:02:51.474536-0400	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ef03f","name":"Nexy(31544)"}, "details":{"deviceUIDs":[],"implicit_category":"Record","input_running":true,"output_running":false} }
default	14:02:51.474606-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 64, PID = 31544, Name = sid:0x1ef03f, Nexy(31544), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	14:02:51.474652-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 64, PID = 31544, Name = sid:0x1ef03f, Nexy(31544), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	14:02:51.474699-0400	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1ef03f, Nexy(31544), 'prim'', AudioCategory changed to 'Record_WithBluetooth'
default	14:02:51.474729-0400	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:02:51.474760-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 64, PID = 31544, Name = sid:0x1ef03f, Nexy(31544), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	14:02:51.474792-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 64, PID = 31544, Name = sid:0x1ef03f, Nexy(31544), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	14:02:51.474849-0400	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:02:51.474838-0400	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 64, PID = 31544, Name = sid:0x1ef03f, Nexy(31544), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> is going active
default	14:02:51.474900-0400	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:02:51.474842-0400	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:02:51.474852-0400	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1ef03f, Nexy(31544), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 64 starting recording
default	14:02:51.474957-0400	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:02:51.474961-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 64, PID = 31544, Name = sid:0x1ef03f, Nexy(31544), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	14:02:51.474997-0400	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:02:51.475023-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 64, PID = 31544, Name = sid:0x1ef03f, Nexy(31544), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	14:02:51.475052-0400	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1ef03f, Nexy(31544), 'prim'', displayID:'com.nexy.assistant'}
default	14:02:51.475131-0400	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [1, 0]. BT device UIDS: {(
)}
default	14:02:51.475191-0400	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	14:02:51.475138-0400	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	14:02:51.475215-0400	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	14:02:51.475229-0400	audioaccessoryd	AudioStateChanged: Added audio session app com.nexy.assistant NULL -> 200 count 1
default	14:02:51.475092-0400	audiomxd	UpdateAudioState CID 0xD310001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	14:02:51.475236-0400	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
error	14:02:51.475244-0400	audioaccessoryd	Updating local audio category 100 -> 200 app com.nexy.assistant
fault	14:02:51.475366-0400	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.17524881.17524887 AUID=501> and <type=Application identifier=application.com.nexy.assistant.17524881.17524887>
default	14:02:51.475295-0400	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
fault	14:02:51.476826-0400	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.17524881.17524887 AUID=501> and <type=Application identifier=application.com.nexy.assistant.17524881.17524887>
default	14:02:51.487176-0400	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	14:02:51.487247-0400	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	14:02:51.487277-0400	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	14:02:51.487756-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:02:51.487765-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:02:51.487773-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	14:02:51.487780-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:02:51.487809-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	14:02:51.487859-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	14:02:51.488151-0400	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	14:02:51.490475-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:02:51.490489-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:02:51.490499-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	14:02:51.490506-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:02:51.490513-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	14:02:51.490519-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	14:02:51.490600-0400	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	14:02:51.491848-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:02:51.491861-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:02:51.491871-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	14:02:51.491877-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:02:51.491883-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	14:02:51.491902-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	14:02:51.492082-0400	ControlCenter	Navigating to new application [com.nexy.assistant]
default	14:02:52.028539-0400	audioaccessoryd	AudioStateSnapshot: Route:Speaker App com.nexy.assistant, Score 200, Remote -1NumofApp 1
default	14:02:52.458230-0400	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	14:02:52.465836-0400	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {BuiltInMicrophoneDevice, 0xa}
default	14:02:52.466329-0400	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ef03f","name":"Nexy(31544)"}, "details":{"deviceUIDs":[],"implicit_category":"","input_running":false,"output_running":false} }
default	14:02:52.466280-0400	runningboardd	Invalidating assertion 398-334-42762 (target:[app<application.com.nexy.assistant.17524881.17524887(501)>:31544]) from originator [osservice<com.apple.powerd>:334]
default	14:02:52.466542-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 64, PID = 31544, Name = sid:0x1ef03f, Nexy(31544), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	14:02:52.466671-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 64, PID = 31544, Name = sid:0x1ef03f, Nexy(31544), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	14:02:52.466738-0400	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1ef03f, Nexy(31544), 'prim'', displayID:'com.nexy.assistant'}
default	14:02:52.466861-0400	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1ef03f, Nexy(31544), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 64 stopping recording
default	14:02:52.466877-0400	audiomxd	UpdateAudioState CID 0xD310001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	14:02:52.466914-0400	audiomxd	-MXCoreSession- -[MXCoreSession endInterruption:]: Session <ID: 64, PID = 31544, Name = sid:0x1ef03f, Nexy(31544), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> is going inactive
default	14:02:52.466976-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 64, PID = 31544, Name = sid:0x1ef03f, Nexy(31544), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	14:02:52.467103-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 64, PID = 31544, Name = sid:0x1ef03f, Nexy(31544), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	14:02:52.467140-0400	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	14:02:52.467257-0400	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	14:02:52.467299-0400	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	14:02:52.467395-0400	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	14:02:52.467621-0400	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:02:52.467653-0400	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:02:52.467483-0400	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:02:52.467689-0400	audioaccessoryd	AudioStateChanged: Removed audio session app com.nexy.assistant 201 count 0
default	14:02:52.467478-0400	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 0]. BT device UIDS: {(
)}
default	14:02:52.467499-0400	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	14:02:52.469857-0400	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	14:02:52.471694-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:02:52.471709-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:02:52.471724-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	14:02:52.471734-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:02:52.471741-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	14:02:52.471750-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	14:02:52.471860-0400	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	14:02:52.569896-0400	Nexy	                AUHAL.cpp:473   ~AUHAL: (0xb8f8bf840) Selecting device 0 from destructor
default	14:02:52.569917-0400	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0xb8f8bf840)
default	14:02:52.569926-0400	Nexy	                AUHAL.cpp:676   SelectDevice: (0xb8f8bf840) not already running
default	14:02:52.569931-0400	Nexy	                AUHAL.cpp:682   SelectDevice: (0xb8f8bf840) disconnecting device 78
default	14:02:52.569940-0400	Nexy	                AUHAL.cpp:746   SelectDevice: (0xb8f8bf840) destroying ioproc 0xa for device 78
default	14:02:52.569981-0400	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {BuiltInMicrophoneDevice, 0xa}
default	14:02:52.570014-0400	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	14:02:52.570189-0400	Nexy	                AUHAL.cpp:848   SelectDevice: (0xb8f8bf840) nothing to setup
default	14:02:52.570204-0400	Nexy	                AUHAL.cpp:858   SelectDevice: (0xb8f8bf840) adding 0 device listeners to device 0
default	14:02:52.570210-0400	Nexy	                AUHAL.cpp:858   SelectDevice: (0xb8f8bf840) adding 0 device delegate listeners to device 0
default	14:02:52.570218-0400	Nexy	                AUHAL.cpp:895   SelectDevice: (0xb8f8bf840) removing 7 device listeners from device 78
default	14:02:52.570287-0400	runningboardd	[app<application.com.nexy.assistant.17524881.17524887(501)>:31544] Ignoring jetsam update because this process is not memory-managed
default	14:02:52.570303-0400	runningboardd	[app<application.com.nexy.assistant.17524881.17524887(501)>:31544] Ignoring suspend because this process is not lifecycle managed
default	14:02:52.570314-0400	runningboardd	[app<application.com.nexy.assistant.17524881.17524887(501)>:31544] Ignoring GPU update because this process is not GPU managed
default	14:02:52.570336-0400	runningboardd	[app<application.com.nexy.assistant.17524881.17524887(501)>:31544] Ignoring memory limit update because this process is not memory-managed
default	14:02:52.570473-0400	Nexy	                AUHAL.cpp:895   SelectDevice: (0xb8f8bf840) removing 0 device delegate listeners from device 78
default	14:02:52.570488-0400	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0xb8f8bf840)
default	14:02:52.575355-0400	runningboardd	Calculated state for app<application.com.nexy.assistant.17524881.17524887(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	14:02:52.575820-0400	runningboardd	Assertion did invalidate due to timeout: 398-398-42752 (target:[app<application.com.nexy.assistant.17524881.17524887(501)>:31544])
default	14:02:52.576045-0400	gamepolicyd	Received state update for 31544 (app<application.com.nexy.assistant.17524881.17524887(501)>, running-active-NotVisible
default	14:02:52.708355-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=31547.1, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=31544, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.osascript, pid=31547, auid=501, euid=501, binary_path=/usr/bin/osascript}, },
default	14:02:52.709917-0400	tccd	AUTHREQ_SUBJECT: msgID=31547.1, subject=com.nexy.assistant,
default	14:02:52.710545-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117900 at /Applications/Nexy.app
default	14:02:52.724621-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=393.2100, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=31544, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.osascript, pid=31547, auid=501, euid=501, binary_path=/usr/bin/osascript}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=393, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	14:02:52.725600-0400	tccd	AUTHREQ_SUBJECT: msgID=393.2100, subject=com.nexy.assistant,
default	14:02:52.726187-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117900 at /Applications/Nexy.app
default	14:02:52.753289-0400	launchservicesd	CHECKIN:0x0-0x3a93a9 31547 com.nexy.assistant
default	14:02:52.754131-0400	loginwindow	-[Application updateInformation] | Got App URL: file:///Applications/Nexy.app/
default	14:02:52.754255-0400	loginwindow	-[ApplicationManager checkInAppContext:eventData:] | ApplicationManager: Checked in app : Nexy
default	14:02:52.754647-0400	runningboardd	[app<application.com.nexy.assistant.17524881.17524887(501)>:31544] Ignoring jetsam update because this process is not memory-managed
default	14:02:52.754659-0400	runningboardd	[app<application.com.nexy.assistant.17524881.17524887(501)>:31544] Ignoring suspend because this process is not lifecycle managed
default	14:02:52.754693-0400	runningboardd	[app<application.com.nexy.assistant.17524881.17524887(501)>:31544] Ignoring GPU update because this process is not GPU managed
default	14:02:52.754777-0400	runningboardd	[app<application.com.nexy.assistant.17524881.17524887(501)>:31544] Ignoring memory limit update because this process is not memory-managed
default	14:02:52.755795-0400	WindowServer	e84af[CreateApplication]: Process creation: 0x0-0x3a93a9 (Nexy) connectionID: E84AF pid: 31547 in session 0x101
default	14:02:52.759174-0400	runningboardd	Calculated state for app<application.com.nexy.assistant.17524881.17524887(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	14:02:52.759238-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117900 at /Applications/Nexy.app
default	14:02:52.759809-0400	runningboardd	Invalidating assertion 398-363-42753 (target:[app<application.com.nexy.assistant.17524881.17524887(501)>:31544]) from originator [osservice<com.apple.coreservices.launchservicesd>:363]
default	14:02:52.759910-0400	gamepolicyd	Received state update for 31544 (app<application.com.nexy.assistant.17524881.17524887(501)>, running-active-NotVisible
default	14:02:52.767349-0400	loginwindow	-[Application updateInformation] | Got App URL: file:///Applications/Nexy.app/
default	14:02:52.779097-0400	System Events	TCCAccessRequestIndirect: TCCAccessRequestIndirect with pid 29142: target_identity: {
    kTCCCodeIdentityAuditToken = {length = 32, bytes = 0xf5010000 f5010000 14000000 f5010000 ... b7860100 67680300 };
    kTCCCodeIdentityAuthority = kTCCCodeIdentityDesignatedRequirementAuthority;
    kTCCCodeIdentityCSFlags = 536941313;
    kTCCCodeIdentityCanSendToAnyTarget = 0;
    kTCCCodeIdentityDesignatedRequirementData = {length = 160, bytes = 0xfade0c00 000000a0 00000001 00000006 ... 4c32434c 42390000 };
    kTCCCodeIdentityExecutableURL = "file:///Applications/Nexy.app/Contents/MacOS/Nexy";
    kTCCCodeIdentityIdentifier = "com.nexy.assistant";
    kTCCCodeIdentityIdentifierType = 0;
    kTCCCodeIdentityPlatformType = 1;
    kTCCCodeIdentityPromptPolicy = 2;
    kTCCCodeIdentitySDKVersion = 984064;
    kTCCCodeIdentityTeamID = 5NKLL2CLB9;
}
default	14:02:52.794087-0400	tccd	target_executable_path_URL: file:///Applications/Nexy.app/Contents/MacOS/Nexy
default	14:02:52.804941-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc5f149500 at /Applications/Nexy.app
default	14:02:52.817440-0400	tccd	Prompting for access to indirect object System Events by Nexy
default	14:02:52.869268-0400	runningboardd	[app<application.com.nexy.assistant.17524881.17524887(501)>:31544] Ignoring jetsam update because this process is not memory-managed
default	14:02:52.869277-0400	runningboardd	[app<application.com.nexy.assistant.17524881.17524887(501)>:31544] Ignoring suspend because this process is not lifecycle managed
default	14:02:52.869299-0400	runningboardd	[app<application.com.nexy.assistant.17524881.17524887(501)>:31544] Set darwin role to: None
default	14:02:52.869353-0400	runningboardd	[app<application.com.nexy.assistant.17524881.17524887(501)>:31544] Ignoring GPU update because this process is not GPU managed
default	14:02:52.869410-0400	runningboardd	[app<application.com.nexy.assistant.17524881.17524887(501)>:31544] Ignoring memory limit update because this process is not memory-managed
default	14:02:52.873536-0400	runningboardd	Calculated state for app<application.com.nexy.assistant.17524881.17524887(501)>: running-suspended (role: None) (endowments: (null))
default	14:02:52.874031-0400	gamepolicyd	Received state update for 31544 (app<application.com.nexy.assistant.17524881.17524887(501)>, running-suspended-NotVisible
default	14:02:53.631998-0400	loginwindow	-[ApplicationManager handleCASEvent:withData:] | CAS notification for appDeath for com.nexy.assistant with asn: LSASN:{hi=0x0;lo=0x3a93a9} for bundle path: /Applications/Nexy.app with URL: file:///Applications/Nexy.app/
default	14:02:53.632030-0400	loginwindow	-[ApplicationManager(AppDeathHandler) appDeathCleanupHandler:forApp:] | Termination handler for: Nexy : 3838889
default	14:02:53.632117-0400	loginwindow	-[PersistentAppsSupport applicationQuit:] | for app:Nexy, _appTrackingState = 2
default	14:02:53.635472-0400	WindowServer	0[outside of RPC]: Process death: 0x0-0x3a93a9 (Nexy) connectionID: E84AF pid: 31547 in session 0x101
default	14:02:53.635524-0400	WindowServer	<BSCompoundAssertion:0x7fb0154c0> ([FocusManager:257]-deferringPolicyEvaluationSuppression) acquire for reason:process death - 0x0-0x3a93a9 (Nexy) acq:0x7fb26f8e0 count:1
default	14:02:53.635966-0400	WindowServer	0[outside of RPC]: [FocusManager:257] update to deferring policy requested for reason: permitted list updated - 0x0-0x3a93a9 removed - but we are suppressing evaluation for reasons: {(
    "process death - 0x0-0x3a93a9 (Nexy)"
)}
default	14:02:53.636331-0400	WindowServer	0[outside of RPC]: [FocusManager:257] update to deferring policy requested for reason: permitted list updated - 0x1-0x7b3b removed - but we are suppressing evaluation for reasons: {(
    "process death - 0x0-0x3a93a9 (Nexy)"
)}
default	14:02:53.828536-0400	Nexy	                AUHAL.cpp:420   AUHAL: (0xb8f8bf840) Selecting device 71 from constructor
default	14:02:53.828572-0400	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0xb8f8bf840)
default	14:02:53.828609-0400	Nexy	                AUHAL.cpp:676   SelectDevice: (0xb8f8bf840) not already running
default	14:02:53.828617-0400	Nexy	                AUHAL.cpp:752   SelectDevice: (0xb8f8bf840) nothing to teardown
default	14:02:53.828629-0400	Nexy	                AUHAL.cpp:757   SelectDevice: (0xb8f8bf840) connecting device 71
default	14:02:53.828773-0400	Nexy	                AUHAL.cpp:3413  IsDeviceUsable: (0xb8f8bf840) Device ID: 71 (Input:No | Output:Yes): true
default	14:02:53.828903-0400	Nexy	                AUHAL.cpp:769   SelectDevice: (0xb8f8bf840) created ioproc 0xb for device 71
default	14:02:53.829066-0400	Nexy	                AUHAL.cpp:858   SelectDevice: (0xb8f8bf840) adding 7 device listeners to device 71
default	14:02:53.829245-0400	Nexy	                AUHAL.cpp:858   SelectDevice: (0xb8f8bf840) adding 0 device delegate listeners to device 71
default	14:02:53.829252-0400	Nexy	                AUHAL.cpp:1581  UpdateStreamFormats: -> (0xb8f8bf840)
default	14:02:53.829339-0400	Nexy	                AUHAL.cpp:1677  UpdateStreamFormats: 
  output stream 0 [0x48]:  2 ch,  48000 Hz, Float32, interleaved
default	14:02:53.829346-0400	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 1 output streams; not all mono
default	14:02:53.829353-0400	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	14:02:53.829359-0400	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 0 input streams; not all mono
default	14:02:53.829365-0400	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	14:02:53.829468-0400	Nexy	                AUHAL.cpp:1771  UpdateStreamFormats: AUHAL(0xb8f8bf840) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	14:02:53.829498-0400	Nexy	                AUHAL.cpp:1777  UpdateStreamFormats: AUHAL(0xb8f8bf840) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	14:02:53.829504-0400	Nexy	                AUHAL.cpp:1787  UpdateStreamFormats: <-
default	14:02:53.829528-0400	Nexy	                AUHAL.cpp:895   SelectDevice: (0xb8f8bf840) removing 0 device listeners from device 0
default	14:02:53.829534-0400	Nexy	                AUHAL.cpp:895   SelectDevice: (0xb8f8bf840) removing 0 device delegate listeners from device 0
default	14:02:53.829538-0400	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0xb8f8bf840)
default	14:02:53.829576-0400	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Output stream enables: Stream 0 is DISABLED
default	14:02:53.829678-0400	Nexy	                AUHAL.cpp:2298  SetProperty: (0xb8f8bf840) caller requesting device change from 71 to 78
default	14:02:53.829704-0400	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0xb8f8bf840)
default	14:02:53.829737-0400	Nexy	                AUHAL.cpp:676   SelectDevice: (0xb8f8bf840) not already running
default	14:02:53.829761-0400	Nexy	                AUHAL.cpp:682   SelectDevice: (0xb8f8bf840) disconnecting device 71
default	14:02:53.829766-0400	Nexy	                AUHAL.cpp:746   SelectDevice: (0xb8f8bf840) destroying ioproc 0xb for device 71
default	14:02:53.829802-0400	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped Unknown {BuiltInSpeakerDevice, 0xb}
default	14:02:53.829845-0400	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	14:02:53.829926-0400	Nexy	                AUHAL.cpp:757   SelectDevice: (0xb8f8bf840) connecting device 78
default	14:02:53.830029-0400	Nexy	                AUHAL.cpp:3413  IsDeviceUsable: (0xb8f8bf840) Device ID: 78 (Input:Yes | Output:No): true
default	14:02:53.831541-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=401.1255, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=31544, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	14:02:53.832731-0400	tccd	AUTHREQ_SUBJECT: msgID=401.1255, subject=com.nexy.assistant,
default	14:02:53.833477-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc5f149500 at /Applications/Nexy.app
default	14:02:53.846636-0400	Nexy	                AUHAL.cpp:769   SelectDevice: (0xb8f8bf840) created ioproc 0xb for device 78
default	14:02:53.846793-0400	Nexy	                AUHAL.cpp:858   SelectDevice: (0xb8f8bf840) adding 7 device listeners to device 78
default	14:02:53.846995-0400	Nexy	                AUHAL.cpp:858   SelectDevice: (0xb8f8bf840) adding 0 device delegate listeners to device 78
default	14:02:53.847002-0400	Nexy	                AUHAL.cpp:1581  UpdateStreamFormats: -> (0xb8f8bf840)
default	14:02:53.847012-0400	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 0 output streams; not all mono
default	14:02:53.847023-0400	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Output render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	14:02:53.847193-0400	Nexy	                AUHAL.cpp:1677  UpdateStreamFormats: 
  input stream 0 [0x4f]:  1 ch,  48000 Hz, Float32
default	14:02:53.847203-0400	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 1 input streams; all mono
default	14:02:53.847208-0400	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Input render format:  1 ch,  48000 Hz, Float32
default	14:02:53.847304-0400	Nexy	                AUHAL.cpp:1771  UpdateStreamFormats: AUHAL(0xb8f8bf840) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	14:02:53.847318-0400	Nexy	                AUHAL.cpp:1777  UpdateStreamFormats: AUHAL(0xb8f8bf840) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	14:02:53.847323-0400	Nexy	                AUHAL.cpp:1787  UpdateStreamFormats: <-
default	14:02:53.847336-0400	Nexy	                AUHAL.cpp:895   SelectDevice: (0xb8f8bf840) removing 7 device listeners from device 71
default	14:02:53.847580-0400	Nexy	                AUHAL.cpp:895   SelectDevice: (0xb8f8bf840) removing 0 device delegate listeners from device 71
default	14:02:53.847590-0400	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0xb8f8bf840)
default	14:02:53.847987-0400	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	14:02:53.849303-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=401.1256, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=31544, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	14:02:53.850694-0400	tccd	AUTHREQ_SUBJECT: msgID=401.1256, subject=com.nexy.assistant,
default	14:02:53.851331-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc5f149500 at /Applications/Nexy.app
default	14:02:53.864342-0400	Nexy	       ACv2Workarounds.mm:51    com.nexy.assistant: fix84702776_86723525_86479548_89800354_SinglePacketDesc: false
default	14:02:53.864459-0400	Nexy	       AudioConverter.cpp:1042  Created a new in process converter -> 0xb8d090d50, from  1 ch,  48000 Hz, Float32 to  1 ch,  16000 Hz, Float32
default	14:02:53.864701-0400	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	14:02:53.865972-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=401.1257, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=31544, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	14:02:53.867188-0400	tccd	AUTHREQ_SUBJECT: msgID=401.1257, subject=com.nexy.assistant,
default	14:02:53.868519-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc5f149500 at /Applications/Nexy.app
default	14:02:53.883085-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=401.1258, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=31544, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	14:02:53.884412-0400	tccd	AUTHREQ_SUBJECT: msgID=401.1258, subject=com.nexy.assistant,
default	14:02:53.885567-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc5f149500 at /Applications/Nexy.app
default	14:02:53.899822-0400	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.17524881.17524887(501)>:31544] from originator [osservice<com.apple.powerd>:334] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:398-334-42769 target:31544 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	14:02:53.899971-0400	runningboardd	Assertion 398-334-42769 (target:[app<application.com.nexy.assistant.17524881.17524887(501)>:31544]) will be created as active
default	14:02:53.900352-0400	runningboardd	[app<application.com.nexy.assistant.17524881.17524887(501)>:31544] Ignoring jetsam update because this process is not memory-managed
default	14:02:53.900379-0400	runningboardd	[app<application.com.nexy.assistant.17524881.17524887(501)>:31544] Ignoring suspend because this process is not lifecycle managed
default	14:02:53.900460-0400	runningboardd	[app<application.com.nexy.assistant.17524881.17524887(501)>:31544] Set darwin role to: Background
default	14:02:53.900473-0400	runningboardd	[app<application.com.nexy.assistant.17524881.17524887(501)>:31544] Ignoring GPU update because this process is not GPU managed
default	14:02:53.900543-0400	runningboardd	[app<application.com.nexy.assistant.17524881.17524887(501)>:31544] Ignoring memory limit update because this process is not memory-managed
default	14:02:53.906307-0400	runningboardd	Calculated state for app<application.com.nexy.assistant.17524881.17524887(501)>: running-active (role: Background) (endowments: (null))
default	14:02:53.906970-0400	gamepolicyd	Received state update for 31544 (app<application.com.nexy.assistant.17524881.17524887(501)>, running-active-NotVisible
default	14:02:53.924741-0400	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Input {BuiltInMicrophoneDevice, 0xb}
default	14:02:53.925951-0400	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ef03f","name":"Nexy(31544)"}, "details":{"deviceUIDs":[],"implicit_category":"Record","input_running":true,"output_running":false} }
default	14:02:53.926054-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 64, PID = 31544, Name = sid:0x1ef03f, Nexy(31544), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	14:02:53.926093-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Category/Mode changed -- The score for sid:0x1ef03f, Nexy(31544), 'prim'/com.nexy.assistant was not correct. Old score = 201
default	14:02:53.926132-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 64, PID = 31544, Name = sid:0x1ef03f, Nexy(31544), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	14:02:53.926188-0400	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1ef03f, Nexy(31544), 'prim'', AudioCategory changed to 'Record_WithBluetooth'
default	14:02:53.926235-0400	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:02:53.926249-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 64, PID = 31544, Name = sid:0x1ef03f, Nexy(31544), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	14:02:53.926281-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 64, PID = 31544, Name = sid:0x1ef03f, Nexy(31544), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	14:02:53.926331-0400	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:02:53.926336-0400	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 64, PID = 31544, Name = sid:0x1ef03f, Nexy(31544), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> is going active
default	14:02:53.926351-0400	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1ef03f, Nexy(31544), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 64 starting recording
default	14:02:53.926404-0400	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:02:53.926462-0400	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:02:53.926428-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 64, PID = 31544, Name = sid:0x1ef03f, Nexy(31544), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	14:02:53.926460-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 64, PID = 31544, Name = sid:0x1ef03f, Nexy(31544), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	14:02:53.926502-0400	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:02:53.926490-0400	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1ef03f, Nexy(31544), 'prim'', displayID:'com.nexy.assistant'}
default	14:02:53.926556-0400	audiomxd	UpdateAudioState CID 0xD310001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	14:02:53.926601-0400	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:02:53.926634-0400	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	14:02:53.926668-0400	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	14:02:53.926683-0400	audioaccessoryd	AudioStateChanged: Added audio session app com.nexy.assistant NULL -> 200 count 1
default	14:02:53.926692-0400	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
error	14:02:53.926701-0400	audioaccessoryd	Updating local audio category 100 -> 200 app com.nexy.assistant
default	14:02:53.926729-0400	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	14:02:53.926733-0400	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [1, 0]. BT device UIDS: {(
)}
default	14:02:53.926744-0400	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	14:02:53.933290-0400	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	14:02:53.933386-0400	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	14:02:53.933439-0400	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	14:02:53.934052-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:02:53.934066-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:02:53.934082-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	14:02:53.934091-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:02:53.934109-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	14:02:53.934117-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	14:02:53.934127-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:02:53.934135-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:02:53.934144-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	14:02:53.934149-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:02:53.934165-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	14:02:53.934186-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	14:02:53.934286-0400	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	14:02:53.934969-0400	ControlCenter	Navigating to new application [com.nexy.assistant]
default	14:02:53.935143-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:02:53.935158-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:02:53.935170-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	14:02:53.935178-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:02:53.935185-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	14:02:53.935192-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	14:02:54.714559-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc5f149800 at /Applications/Nexy.app
default	14:02:54.721554-0400	tccd	Publishing <TCCDEvent: type=Create, service=kTCCServiceAppleEvents, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 3 subscribers: {
    471 = "<TCCDEventSubscriber: token=471, state=Passed, csid=com.apple.chronod>";
    37 = "<TCCDEventSubscriber: token=37, state=Initial, csid=(null)>";
    476 = "<TCCDEventSubscriber: token=476, state=Passed, csid=com.apple.photolibraryd>";
}
default	14:02:54.723787-0400	chronod	[appAuth:com.nexy.assistant] tcc authorization(s) changed
default	14:02:55.028542-0400	audioaccessoryd	AudioStateSnapshot: Route:Speaker App com.nexy.assistant, Score 200, Remote -1NumofApp 1
error	14:02:57.599140-0400	Nexy	         HALC_ProxyIOContext.cpp:1623  HALC_ProxyIOContext::IOWorkLoop: skipping cycle due to overload
default	14:02:58.032480-0400	audioaccessoryd	AudioStateSnapshot: Route:Speaker App com.nexy.assistant, Score 200, Remote -1NumofApp 1
error	14:02:58.659976-0400	Nexy	         HALC_ProxyIOContext.cpp:1623  HALC_ProxyIOContext::IOWorkLoop: skipping cycle due to overload
error	14:02:58.668052-0400	Nexy	         HALC_ProxyIOContext.cpp:1623  HALC_ProxyIOContext::IOWorkLoop: skipping cycle due to overload
default	14:02:58.757591-0400	coreaudiod	Sending message. { reporterID=135480448385027, category=IO, type=error, message=["smallest_buffer_frame_size": Optional(4096), "output_device_transport_list": Optional(), "io_buffer_size": Optional(4096), "HostApplicationDisplayID": Optional(com.nexy.assistant), "num_continuous_silent_io_cycles": Optional(0), "input_device_uid_list": Optional(BuiltInMicrophoneDevice), "io_cycle_budget": Optional(85354166), "safety_violation_time_gap": Optional(0), "wg_external_wakeups": Optional(0), "io_cycle": Optional(1), "start_time": Optional(1103623985858), "wg_total_wakeups": Optional(5), "io_page_faults_duration": Optional(0), "time_since_prev_overload": Optional(880748625), "is_recovering": Optional(0), "other_active_clients": Optional([  ]), "cause": Optional(ClientHALIODurationExceededBudget), "output_device_source_list": Optional(), "deadline": Optional(222560), "safety_violation": Optional(0), "io_cycle_usage": Optional(1), "overload_type": Optional(Overload), "cause_set": Optional(4), "num_continuous_nonzero_io_cycles": Optional(0), "anchor_sample_time<…> }
default	14:03:00.934905-0400	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	14:03:00.942030-0400	runningboardd	Invalidating assertion 398-334-42769 (target:[app<application.com.nexy.assistant.17524881.17524887(501)>:31544]) from originator [osservice<com.apple.powerd>:334]
default	14:03:00.942259-0400	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {BuiltInMicrophoneDevice, 0xb}
default	14:03:00.942629-0400	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ef03f","name":"Nexy(31544)"}, "details":{"deviceUIDs":[],"implicit_category":"","input_running":false,"output_running":false} }
default	14:03:00.942786-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 64, PID = 31544, Name = sid:0x1ef03f, Nexy(31544), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	14:03:00.942867-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 64, PID = 31544, Name = sid:0x1ef03f, Nexy(31544), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	14:03:00.942909-0400	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1ef03f, Nexy(31544), 'prim'', displayID:'com.nexy.assistant'}
default	14:03:00.943002-0400	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1ef03f, Nexy(31544), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 64 stopping recording
default	14:03:00.943058-0400	audiomxd	-MXCoreSession- -[MXCoreSession endInterruption:]: Session <ID: 64, PID = 31544, Name = sid:0x1ef03f, Nexy(31544), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> is going inactive
default	14:03:00.943077-0400	audiomxd	UpdateAudioState CID 0xD310001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	14:03:00.943100-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 64, PID = 31544, Name = sid:0x1ef03f, Nexy(31544), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	14:03:00.943160-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 64, PID = 31544, Name = sid:0x1ef03f, Nexy(31544), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	14:03:00.943224-0400	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:03:00.943267-0400	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	14:03:00.943330-0400	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	14:03:00.943355-0400	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:03:00.943380-0400	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	14:03:00.943451-0400	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	14:03:00.943469-0400	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:03:00.943490-0400	audioaccessoryd	AudioStateChanged: Removed audio session app com.nexy.assistant 201 count 0
default	14:03:00.944108-0400	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	14:03:00.944180-0400	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 0]. BT device UIDS: {(
)}
default	14:03:00.944195-0400	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	14:03:00.945601-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:03:00.945619-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:03:00.945636-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	14:03:00.945645-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:03:00.945657-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	14:03:00.945667-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	14:03:00.945825-0400	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	14:03:01.045795-0400	runningboardd	[app<application.com.nexy.assistant.17524881.17524887(501)>:31544] Ignoring jetsam update because this process is not memory-managed
default	14:03:01.045809-0400	runningboardd	[app<application.com.nexy.assistant.17524881.17524887(501)>:31544] Ignoring suspend because this process is not lifecycle managed
default	14:03:01.045862-0400	runningboardd	[app<application.com.nexy.assistant.17524881.17524887(501)>:31544] Set darwin role to: None
default	14:03:01.045876-0400	runningboardd	[app<application.com.nexy.assistant.17524881.17524887(501)>:31544] Ignoring GPU update because this process is not GPU managed
default	14:03:01.045913-0400	runningboardd	[app<application.com.nexy.assistant.17524881.17524887(501)>:31544] Ignoring memory limit update because this process is not memory-managed
default	14:03:01.050244-0400	runningboardd	Calculated state for app<application.com.nexy.assistant.17524881.17524887(501)>: running-suspended (role: None) (endowments: (null))
default	14:03:01.051352-0400	gamepolicyd	Received state update for 31544 (app<application.com.nexy.assistant.17524881.17524887(501)>, running-suspended-NotVisible
default	14:03:01.147684-0400	Nexy	                AUHAL.cpp:473   ~AUHAL: (0xb8f8bf840) Selecting device 0 from destructor
default	14:03:01.147715-0400	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0xb8f8bf840)
default	14:03:01.147795-0400	Nexy	                AUHAL.cpp:676   SelectDevice: (0xb8f8bf840) not already running
default	14:03:01.147809-0400	Nexy	                AUHAL.cpp:682   SelectDevice: (0xb8f8bf840) disconnecting device 78
default	14:03:01.147860-0400	Nexy	                AUHAL.cpp:746   SelectDevice: (0xb8f8bf840) destroying ioproc 0xb for device 78
default	14:03:01.148004-0400	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {BuiltInMicrophoneDevice, 0xb}
default	14:03:01.148113-0400	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	14:03:01.148489-0400	Nexy	                AUHAL.cpp:848   SelectDevice: (0xb8f8bf840) nothing to setup
default	14:03:01.148549-0400	Nexy	                AUHAL.cpp:858   SelectDevice: (0xb8f8bf840) adding 0 device listeners to device 0
default	14:03:01.148560-0400	Nexy	                AUHAL.cpp:858   SelectDevice: (0xb8f8bf840) adding 0 device delegate listeners to device 0
default	14:03:01.148571-0400	Nexy	                AUHAL.cpp:895   SelectDevice: (0xb8f8bf840) removing 7 device listeners from device 78
default	14:03:01.148978-0400	Nexy	                AUHAL.cpp:895   SelectDevice: (0xb8f8bf840) removing 0 device delegate listeners from device 78
default	14:03:01.149002-0400	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0xb8f8bf840)
default	14:03:01.152548-0400	Nexy	[0xb8f938780] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	14:03:01.153784-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=31544.5, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=31544, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	14:03:01.155738-0400	tccd	AUTHREQ_SUBJECT: msgID=31544.5, subject=com.nexy.assistant,
default	14:03:01.156790-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d114000 at /Applications/Nexy.app
default	14:03:01.175304-0400	Nexy	[0xb8f938780] invalidated after the last release of the connection object
default	14:03:01.175730-0400	Nexy	[0xb8f938780] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	14:03:01.176521-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=31544.6, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=31544, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	14:03:01.177961-0400	tccd	AUTHREQ_SUBJECT: msgID=31544.6, subject=com.nexy.assistant,
default	14:03:01.178700-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d114000 at /Applications/Nexy.app
default	14:03:01.192277-0400	tccd	Notifying for access  kTCCServiceScreenCapture for target PID[31544], responsiblePID[31544], responsiblePath: /Applications/Nexy.app to UID: 501
default	14:03:01.192553-0400	Nexy	[0xb8f938780] invalidated after the last release of the connection object
default	14:03:01.242846-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117000 at /Applications/Nexy.app
default	14:03:01.255906-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d114000 at /Applications/Nexy.app
default	14:03:01.259716-0400	tccd	Publishing <TCCDEvent: type=Modify, service=kTCCServiceScreenCapture, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 0 subscribers: {
}
default	14:03:01.774116-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117000 at /Applications/Nexy.app
default	14:03:01.787569-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d114000 at /Applications/Nexy.app
default	14:03:01.796312-0400	tccd	Publishing <TCCDEvent: type=Modify, service=kTCCServiceListenEvent, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 0 subscribers: {
}
default	14:03:08.230948-0400	Nexy	[0xb8f938a00] activating connection: mach=true listener=false peer=false name=com.apple.analyticsd
default	14:03:08.232198-0400	Nexy	Received configuration update from daemon (initial)
default	14:03:08.234446-0400	Nexy	server port 0x00009a0f, session port 0x00009a0f
default	14:03:08.235672-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=393.2138, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=31544, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=393, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	14:03:08.235702-0400	tccd	requestor: TCCDProcess: identifier=com.apple.WindowServer, pid=393, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=31544, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	14:03:08.236386-0400	Nexy	networkd_settings_read_from_file initialized networkd settings by reading plist directly
default	14:03:08.236605-0400	Nexy	networkd_settings_read_from_file initialized networkd settings by reading plist directly
default	14:03:08.237584-0400	tccd	AUTHREQ_SUBJECT: msgID=393.2138, subject=com.nexy.assistant,
default	14:03:08.237750-0400	Nexy	nw_path_libinfo_path_check [BCBDA4DF-36DB-4888-8898-F24C9C786E06 IPv4#8bab8f72:8081 tcp, legacy-socket, attribution: developer]
	libinfo check path: <private>
default	14:03:08.238363-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d116a00 at /Applications/Nexy.app
default	14:03:08.238502-0400	kernel	SK[2]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 51FEB2E8-7F98-4D21-82E6-D779719E88A4 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.56800,dst=<IPv4-redacted>.8081,proto=0x06 mask=0x0000003f,hash=0xa60d842e tp_proto=0x06"
default	14:03:08.238653-0400	kernel	tcp connect outgoing: [<IPv4-redacted>:56800<-><IPv4-redacted>:8081] interface: en0 (skipped: 0)
so_gencnt: 610274 t_state: SYN_SENT process: Nexy:31544 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x8886d784
default	14:03:08.270730-0400	Nexy	[0xb8f938b40] activating connection: mach=true listener=false peer=false name=com.apple.coreservices.launchservicesd
default	14:03:08.273173-0400	Nexy	New connection 0x12538f main
default	14:03:08.273334-0400	Nexy	[0xb8f938c80] activating connection: mach=true listener=false peer=false name=com.apple.pasteboard.1
default	14:03:08.277149-0400	Nexy	[0xb8f938f00] activating connection: mach=true listener=false peer=false name=com.apple.lsd.mapdb
default	14:03:08.299377-0400	kernel	tcp connected: [<IPv4-redacted>:56800<-><IPv4-redacted>:8081] interface: en0 (skipped: 0)
so_gencnt: 610274 t_state: ESTABLISHED process: Nexy:31544 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x8886d784
default	14:03:08.353755-0400	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:56800<-><IPv4-redacted>:8081] interface: en0 (skipped: 0)
so_gencnt: 610274 t_state: FIN_WAIT_1 process: Nexy:31544 Duration: 0.116 sec Conn_Time: 0.061 sec bytes in/out: 1562/245 pkts in/out: 2/2 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 52.000 ms rttvar: 32.750 ms base rtt: 22 ms so_error: 0 svc/tc: 0 flow: 0x8886d784
default	14:03:08.353785-0400	kernel	tcp_connection_summary [<IPv4-redacted>:56800<-><IPv4-redacted>:8081] interface: en0 (skipped: 0)
so_gencnt: 610274 t_state: FIN_WAIT_1 process: Nexy:31544 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	14:03:08.361449-0400	Nexy	void _NSDisableAutomaticTerminationAndLog(NSString *) No windows open yet
default	14:03:08.366421-0400	Nexy	CHECKIN: pid=31544
default	14:03:08.375690-0400	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.17524881.17524887(501)>:31544] from originator [osservice<com.apple.coreservices.launchservicesd>:363] with description <RBSAssertionDescriptor| "uielement:31544" ID:398-363-42897 target:31544 attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"RoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	14:03:08.375833-0400	runningboardd	Assertion 398-363-42897 (target:[app<application.com.nexy.assistant.17524881.17524887(501)>:31544]) will be created as active
default	14:03:08.375780-0400	launchservicesd	CHECKIN:0x0-0x3bc3bc 31544 com.nexy.assistant
default	14:03:08.376302-0400	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.17524881.17524887(501)>:31544] from originator [osservice<com.apple.coreservices.launchservicesd>:363] with description <RBSAssertionDescriptor| "uielement:31544" ID:398-363-42898 target:31544 attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"RoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	14:03:08.376315-0400	runningboardd	[app<application.com.nexy.assistant.17524881.17524887(501)>:31544] Ignoring jetsam update because this process is not memory-managed
default	14:03:08.376384-0400	runningboardd	Assertion 398-363-42898 (target:[app<application.com.nexy.assistant.17524881.17524887(501)>:31544]) will be created as active
default	14:03:08.376396-0400	runningboardd	[app<application.com.nexy.assistant.17524881.17524887(501)>:31544] Ignoring suspend because this process is not lifecycle managed
default	14:03:08.376441-0400	Nexy	CHECKEDIN: pid=31544 asn=0x0-0x3bc3bc foreground=0
default	14:03:08.376461-0400	runningboardd	[app<application.com.nexy.assistant.17524881.17524887(501)>:31544] Set darwin role to: UserInteractive
default	14:03:08.376516-0400	loginwindow	-[Application updateInformation] | Got App URL: file:///Applications/Nexy.app/
default	14:03:08.376481-0400	runningboardd	[app<application.com.nexy.assistant.17524881.17524887(501)>:31544] Ignoring GPU update because this process is not GPU managed
default	14:03:08.376539-0400	runningboardd	[app<application.com.nexy.assistant.17524881.17524887(501)>:31544] Ignoring memory limit update because this process is not memory-managed
default	14:03:08.376720-0400	loginwindow	-[ApplicationManager checkInAppContext:eventData:] | ApplicationManager: Checked in app : Nexy
default	14:03:08.376909-0400	Nexy	[0xb8f939040] activating connection: mach=true listener=false peer=false name=com.apple.lsd.modifydb
default	14:03:08.377409-0400	Nexy	[0xb8f939180] activating connection: mach=false listener=true peer=false name=(anonymous)
default	14:03:08.377418-0400	Nexy	[0xb8f939180] Connection returned listener port: 0xca03
default	14:03:08.377556-0400	Nexy	[0xb8d7fc480] activating connection: mach=false listener=false peer=true name=com.apple.xpc.anonymous.0xb8f939180.peer[363].0xb8d7fc480
default	14:03:08.378631-0400	Nexy	FRONTLOGGING: version 1
default	14:03:08.378669-0400	Nexy	Registered, pid=31544 ASN=0x0,0x3bc3bc
default	14:03:08.378940-0400	WindowServer	12538f[CreateApplication]: Process creation: 0x0-0x3bc3bc (Nexy) connectionID: 12538F pid: 31544 in session 0x101
default	14:03:08.381910-0400	runningboardd	Calculated state for app<application.com.nexy.assistant.17524881.17524887(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	14:03:08.382227-0400	runningboardd	Invalidating assertion 398-363-42897 (target:[app<application.com.nexy.assistant.17524881.17524887(501)>:31544]) from originator [osservice<com.apple.coreservices.launchservicesd>:363]
default	14:03:08.382472-0400	gamepolicyd	Received state update for 31544 (app<application.com.nexy.assistant.17524881.17524887(501)>, running-active-NotVisible
default	14:03:08.383229-0400	Nexy	[0xb8f939180] Connection returned listener port: 0xca03
default	14:03:08.383752-0400	Nexy	BringForward: pid=31544 asn=0x0-0x3bc3bc bringForward=0 foreground=0 uiElement=1 launchedByLS=0 modifiersCount=0 allDisabled=0
default	14:03:08.384221-0400	Nexy	Current system appearance, (HLTB: 1), (SLS: 0)
default	14:03:08.385595-0400	Nexy	Current system appearance, (HLTB: 1), (SLS: 0)
default	14:03:08.386053-0400	Nexy	Post-registration system appearance: (HLTB: 1)
default	14:03:08.412612-0400	lsd	com.nexy.assistant/Unknown Persona:5:5:1:1:Building bundle record for app
default	14:03:08.412771-0400	lsd	com.nexy.assistant/Unknown Persona:5:5:2:1:Built bundle record for app
default	14:03:08.418960-0400	Nexy	FBSWorkspace: endpoint monitoring is disabled.
default	14:03:08.418972-0400	Nexy	FBSWorkspace: default shell endpoint is disabled.
default	14:03:08.419029-0400	Nexy	Initializing connection
default	14:03:08.419076-0400	Nexy	Removing all cached process handles
default	14:03:08.419104-0400	Nexy	Sending handshake request attempt #1 to server
default	14:03:08.419112-0400	Nexy	Creating connection to com.apple.runningboard
default	14:03:08.419121-0400	Nexy	[0xb8f939400] activating connection: mach=true listener=false peer=false name=com.apple.runningboard
default	14:03:08.419648-0400	runningboardd	Setting client for [app<application.com.nexy.assistant.17524881.17524887(501)>:31544] as ready
default	14:03:08.419642-0400	Nexy	[0xb8f939180] Connection returned listener port: 0xca03
default	14:03:08.420382-0400	Nexy	Handshake succeeded
default	14:03:08.420401-0400	Nexy	Identity resolved as app<application.com.nexy.assistant.17524881.17524887(501)>
default	14:03:08.420627-0400	distnoted	register name: com.apple.xctest.FakeForceTouchDevice object: com.nexy.assistant token: 2d00000024 pid: 31544
default	14:03:08.423727-0400	Nexy	[0xb8f939180] Connection returned listener port: 0xca03
default	14:03:08.425206-0400	Nexy	Created a new Process Instance Registry XPC connection (inactive)
default	14:03:08.425224-0400	Nexy	[0xb8f9392c0] activating connection: mach=true listener=false peer=false name=com.apple.linkd.autoShortcut
default	14:03:08.425297-0400	Nexy	Activated connection to com.apple.linkd.autoShortcut (ApplicationService)
default	14:03:08.425345-0400	Nexy	[0xb8f939680] activating connection: mach=false listener=true peer=false name=(anonymous)
default	14:03:08.428129-0400	WindowServer	12538f[SetFrontProcessWithInfo]: [DeferringManager] Updating policy {
    advicePolicy: .frontmost;
    frontmostProcess: 0x0-0x3bc3bc (Nexy) mainConnectionID: 12538F;
} for reason: updated frontmost process
default	14:03:08.428090-0400	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.17524881.17524887(501)>:31544] from originator [osservice<com.apple.coreservices.launchservicesd>:363] with description <RBSAssertionDescriptor| "frontmost:31544" ID:398-363-42899 target:31544 attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"RoleUserInteractiveFocal" sourceEnvironment:"(null)">
	]>
default	14:03:08.428220-0400	runningboardd	Assertion 398-363-42899 (target:[app<application.com.nexy.assistant.17524881.17524887(501)>:31544]) will be created as active
default	14:03:08.428246-0400	WindowServer	12538f[SetFrontProcessWithInfo]: [DeferringManager] Deferring events from frontmost process PSN 0x0-0x3bc3bc (Nexy) -> <pid: 31544>
default	14:03:08.428385-0400	WindowServer	new deferring rules for pid:393: [
    [393-1898]; <keyboardFocus; Nexy:0x0-0x3bc3bc>; () -> <pid: 31544>; reason: frontmost PSN --> outbound target,
    [393-1897]; <keyboardFocus; <frontmost>>; () -> <token: Nexy:0x0-0x3bc3bc; pid: 393>; reason: frontmost PSN,
    [393-1896]; <keyboardFocus>; () -> <token: <frontmost>; pid: 393>; reason: Deferring to <frontmost>
]
default	14:03:08.428428-0400	WindowServer	[keyboardFocus 0x7facf2b20] setRules:forPID(393): [
    [393-1898]; <keyboardFocus; Nexy:0x0-0x3bc3bc>; () -> <pid: 31544>; reason: frontmost PSN --> outbound target,
    [393-1897]; <keyboardFocus; <frontmost>>; () -> <token: Nexy:0x0-0x3bc3bc; pid: 393>; reason: frontmost PSN,
    [393-1896]; <keyboardFocus>; () -> <token: <frontmost>; pid: 393>; reason: Deferring to <frontmost>
]
default	14:03:08.428910-0400	runningboardd	[app<application.com.nexy.assistant.17524881.17524887(501)>:31544] Ignoring jetsam update because this process is not memory-managed
default	14:03:08.428956-0400	runningboardd	[app<application.com.nexy.assistant.17524881.17524887(501)>:31544] Ignoring suspend because this process is not lifecycle managed
default	14:03:08.429013-0400	runningboardd	[app<application.com.nexy.assistant.17524881.17524887(501)>:31544] Set darwin role to: UserInteractiveFocal
default	14:03:08.429040-0400	runningboardd	[app<application.com.nexy.assistant.17524881.17524887(501)>:31544] Ignoring GPU update because this process is not GPU managed
default	14:03:08.429116-0400	runningboardd	[app<application.com.nexy.assistant.17524881.17524887(501)>:31544] Ignoring memory limit update because this process is not memory-managed
default	14:03:08.429347-0400	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.17524881.17524887(501)>:31544] from originator [osservice<com.apple.coreservices.launchservicesd>:363] with description <RBSAssertionDescriptor| "notification:31544" ID:398-363-42900 target:31544 attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"LSNotification" sourceEnvironment:"(null)">
	]>
default	14:03:08.429405-0400	runningboardd	Assertion 398-363-42900 (target:[app<application.com.nexy.assistant.17524881.17524887(501)>:31544]) will be created as active
default	14:03:08.430083-0400	WindowServer	chain did update (setDeferringRules) <keyboardFocus; display: null> containsEndOfChain: YES; [
    <token: <frontmost>; pid: 393>,
    <token: Nexy:0x0-0x3bc3bc; pid: 393>,
    <pid: 31544>
]
default	14:03:08.430943-0400	Nexy	[0xb8f939680] Connection returned listener port: 0x10d03
default	14:03:08.431602-0400	Nexy	Registered process with identifier 31544-223327
default	14:03:08.434405-0400	Nexy	[0xb8f939900] activating connection: mach=true listener=false peer=false name=com.apple.usernoted.client
default	14:03:08.438791-0400	runningboardd	Calculated state for app<application.com.nexy.assistant.17524881.17524887(501)>: running-active (role: UserInteractiveFocal) (endowments: <private>)
default	14:03:08.439147-0400	runningboardd	[app<application.com.nexy.assistant.17524881.17524887(501)>:31544] Ignoring jetsam update because this process is not memory-managed
default	14:03:08.439162-0400	runningboardd	[app<application.com.nexy.assistant.17524881.17524887(501)>:31544] Ignoring suspend because this process is not lifecycle managed
default	14:03:08.439178-0400	runningboardd	[app<application.com.nexy.assistant.17524881.17524887(501)>:31544] Ignoring GPU update because this process is not GPU managed
default	14:03:08.439230-0400	runningboardd	[app<application.com.nexy.assistant.17524881.17524887(501)>:31544] Ignoring memory limit update because this process is not memory-managed
default	14:03:08.444675-0400	runningboardd	Calculated state for app<application.com.nexy.assistant.17524881.17524887(501)>: running-active (role: UserInteractiveFocal) (endowments: <private>)
default	14:03:08.447135-0400	usernoted	Connection com.nexy.assistant with path: /Applications/Nexy.app
default	14:03:08.448524-0400	distnoted	register name: com.apple.nsquiet_safe_quit_give_reason object: com.nexy.assistant token: 3100000032 pid: 31544
default	14:03:08.457892-0400	Nexy	NSApp cache appearance:
-NSRequiresAquaSystemAppearance: 0
-appearance: (null)
-effectiveAppearance: <NSCompositeAppearance: 0xb8f795360
 (
    "<NSAquaAppearance: 0xb8f795400>",
    "<NSSystemAppearance: 0xb8f794fa0>"
)>
default	14:03:08.464272-0400	Nexy	[0xb8f939e00] activating connection: mach=true listener=false peer=false name=com.apple.dock.fullscreen
default	14:03:08.464443-0400	Nexy	[0xb8f939f40] activating connection: mach=true listener=false peer=false name=com.apple.fonts
default	14:03:08.466594-0400	Nexy	(<private>) deleteSearchableItemsWithDomainIdentifiers, protectionClass:(null), domainIdentifiers number:1
default	14:03:08.466862-0400	Nexy	sConnectionName: com.apple.spotlight.IndexAgent
default	14:03:08.466890-0400	Nexy	Start service name com.apple.spotlight.IndexAgent
default	14:03:08.466891-0400	Nexy	[C:1] Alloc com.apple.controlcenter.statusitems
default	14:03:08.466927-0400	Nexy	[0xb8f93a080] activating connection: mach=true listener=false peer=false name=com.apple.spotlight.IndexAgent
default	14:03:08.466942-0400	Nexy	[0xb8f93a1c0] activating connection: mach=false listener=false peer=false name=(anonymous)
default	14:03:08.466999-0400	Nexy	FBSWorkspace registering source: <private>
default	14:03:08.467556-0400	suggestd	SGDSpotlightReceiver: deleting 1 domain identifiers (1 after removing overlaps) for com.nexy.assistant: <private>
default	14:03:08.467683-0400	Nexy	FBSWorkspace connected to endpoint : <private>
default	14:03:08.468017-0400	Nexy	<FBSWorkspaceScenesClient:0xb8f795fe0 <private>> attempting immediate handshake from activate
default	14:03:08.468072-0400	Nexy	<FBSWorkspaceScenesClient:0xb8f795fe0 <private>> sent handshake
default	14:03:08.468164-0400	Nexy	Realizing settings extension __NSStatusItemSceneHostSettings__ on FBSSceneSettings
default	14:03:08.468420-0400	ControlCenter	Asked to bootstrap a new process for handle: [app<application.com.nexy.assistant.17524881.17524887(501)>:31544]
default	14:03:08.468446-0400	ControlCenter	Creating process (sync=true) for handle: [app<application.com.nexy.assistant.17524881.17524887(501)>:31544]
default	14:03:08.468508-0400	ControlCenter	[app<application.com.nexy.assistant.17524881.17524887>:31544] Registering event dispatcher at init
default	14:03:08.468569-0400	ControlCenter	Created <FBWorkspace: 0xaf868f7a0; <FBApplicationProcess: 0xaf889aa00; app<application.com.nexy.assistant.17524881.17524887>:31544(v3685F)>>
default	14:03:08.468584-0400	ControlCenter	Bootstrapping app<application.com.nexy.assistant.17524881.17524887> with intent background
default	14:03:08.468816-0400	runningboardd	Launch request for app<application.com.nexy.assistant.17524881.17524887(501)>[0] is using uid 501 (divined from auid 501 euid 501)
default	14:03:08.468743-0400	Nexy	Realizing settings extension __NSStatusItemSceneClientSettings__ on FBSSceneClientSettings
default	14:03:08.468919-0400	runningboardd	Acquiring assertion targeting app<application.com.nexy.assistant.17524881.17524887(501)> from originator [osservice<com.apple.controlcenter(501)>:632] with description <RBSAssertionDescriptor| "FBApplicationProcess" ID:398-632-42901 target:app<application.com.nexy.assistant.17524881.17524887(501)> attributes:[
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableLPRunReason-Suspend" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableRole-NonUI" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableJetsamPriority-Active" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableBootstrapping" sourceEnvironment:"(null)">
	]>
default	14:03:08.469048-0400	runningboardd	Assertion 398-632-42901 (target:app<application.com.nexy.assistant.17524881.17524887(501)>) will be created as active
default	14:03:08.469080-0400	runningboardd	setting abstract target for <RBSAssertionDescriptor| "FBApplicationProcess" ID:398-632-42901 target:app<application.com.nexy.assistant.17524881.17524887(501)> attributes:[
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableLPRunReason-Suspend" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableRole-NonUI" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableJetsamPriority-Active" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableBootstrapping" sourceEnvironment:"(null)">
	]> to [app<application.com.nexy.assistant.17524881.17524887(501)>:31544]
default	14:03:08.470663-0400	Nexy	Realizing settings extension FBSSceneSettingsCore on FBSSceneSettings
default	14:03:08.472137-0400	Nexy	Realizing settings extension FBSSceneClientSettingsCore on FBSSceneClientSettings
default	14:03:08.472835-0400	Nexy	Requesting scene <FBSScene: 0xb8f796300; com.apple.controlcenter:BD5BA3B6-D225-4F6E-B75F-94A9AB64BF69> from com.apple.controlcenter.statusitems
default	14:03:08.473153-0400	Nexy	Request for <FBSScene: 0xb8f796300; com.apple.controlcenter:BD5BA3B6-D225-4F6E-B75F-94A9AB64BF69> complete!
default	14:03:08.473232-0400	Nexy	Realizing settings extension FBSSceneTransitionContextCore on FBSSceneTransitionContext
default	14:03:08.474812-0400	Nexy	Realizing settings extension __NSHostedViewSceneSettings__ on FBSSceneSettings
default	14:03:08.475130-0400	Nexy	Realizing settings extension __NSClientHostedViewSceneSettings__ on FBSSceneClientSettings
default	14:03:08.475366-0400	Nexy	Realizing settings extension __NSStatusItemAuxiliaryViewSceneSettings__ on FBSSceneSettings
default	14:03:08.475400-0400	Nexy	Realizing settings extension __NSClientStatusItemAuxiliaryViewSceneSettings__ on FBSSceneClientSettings
default	14:03:08.475701-0400	Nexy	Requesting scene <FBSScene: 0xb8f7964e0; com.apple.controlcenter:BD5BA3B6-D225-4F6E-B75F-94A9AB64BF69-Aux[1]-NSStatusItemView> from com.apple.controlcenter.statusitems
default	14:03:08.475888-0400	Nexy	Request for <FBSScene: 0xb8f7964e0; com.apple.controlcenter:BD5BA3B6-D225-4F6E-B75F-94A9AB64BF69-Aux[1]-NSStatusItemView> complete!
default	14:03:08.469521-0400	runningboardd	[app<application.com.nexy.assistant.17524881.17524887(501)>:31544] Ignoring jetsam update because this process is not memory-managed
default	14:03:08.475867-0400	runningboardd	[app<application.com.nexy.assistant.17524881.17524887(501)>:31544] Ignoring suspend because this process is not lifecycle managed
default	14:03:08.475915-0400	runningboardd	[app<application.com.nexy.assistant.17524881.17524887(501)>:31544] Ignoring GPU update because this process is not GPU managed
default	14:03:08.477314-0400	runningboardd	[app<application.com.nexy.assistant.17524881.17524887(501)>:31544] Ignoring memory limit update because this process is not memory-managed
default	14:03:08.477691-0400	Nexy	[com.apple.controlcenter:BD5BA3B6-D225-4F6E-B75F-94A9AB64BF69-Aux[1]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
default	14:03:08.477713-0400	Nexy	[com.apple.controlcenter:BD5BA3B6-D225-4F6E-B75F-94A9AB64BF69-Aux[1]-NSStatusItemView] Dropping transition context because the scene is reconnecting
default	14:03:08.481786-0400	runningboardd	[app<application.com.nexy.assistant.17524881.17524887(501)>:31544] Ignoring jetsam update because this process is not memory-managed
default	14:03:08.481797-0400	runningboardd	[app<application.com.nexy.assistant.17524881.17524887(501)>:31544] Ignoring suspend because this process is not lifecycle managed
default	14:03:08.481812-0400	runningboardd	[app<application.com.nexy.assistant.17524881.17524887(501)>:31544] Ignoring GPU update because this process is not GPU managed
default	14:03:08.481875-0400	Nexy	[com.apple.controlcenter:BD5BA3B6-D225-4F6E-B75F-94A9AB64BF69-Aux[1]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
default	14:03:08.481894-0400	Nexy	[com.apple.controlcenter:BD5BA3B6-D225-4F6E-B75F-94A9AB64BF69-Aux[1]-NSStatusItemView] Dropping transition context because the scene is reconnecting
default	14:03:08.481833-0400	runningboardd	[app<application.com.nexy.assistant.17524881.17524887(501)>:31544] Ignoring memory limit update because this process is not memory-managed
default	14:03:08.481977-0400	Nexy	Warning: the app is using `-[NSStatusBarButton setHighlightsBy:]` to set the highlight behavior. Instead, consider removing that setting. That will enable macOS to highlight the status bar button as appropriate for all configurations (e.g., light, dark, and increased contrast modes).
default	14:03:08.482515-0400	Nexy	[com.apple.controlcenter:BD5BA3B6-D225-4F6E-B75F-94A9AB64BF69-Aux[1]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
default	14:03:08.482530-0400	Nexy	[com.apple.controlcenter:BD5BA3B6-D225-4F6E-B75F-94A9AB64BF69-Aux[1]-NSStatusItemView] Dropping transition context because the scene is reconnecting
default	14:03:08.486310-0400	runningboardd	Calculated state for app<application.com.nexy.assistant.17524881.17524887(501)>: running-active (role: UserInteractiveFocal) (endowments: <private>)
default	14:03:08.486716-0400	ControlCenter	Adding: <FBApplicationProcess: 0xaf889aa00; app<application.com.nexy.assistant.17524881.17524887>:31544(v3685F)>
default	14:03:08.489110-0400	ControlCenter	Received state update for 31544 (app<application.com.nexy.assistant.17524881.17524887(501)>, running-active-NotVisible
default	14:03:08.489552-0400	gamepolicyd	Received state update for 31544 (app<application.com.nexy.assistant.17524881.17524887(501)>, running-active-NotVisible
default	14:03:08.493479-0400	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.17524881.17524887(501)>:31544] from originator [osservice<com.apple.controlcenter(501)>:632] with description <RBSAssertionDescriptor| "FBWorkspace (BG-Active[40])" ID:398-632-42904 target:31544 attributes:[
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableLPRunReason-Suspend" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableRole-NonUI" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableJetsamPriority-Active" sourceEnvironment:"(null)">
	]>
default	14:03:08.493577-0400	runningboardd	Assertion 398-632-42904 (target:[app<application.com.nexy.assistant.17524881.17524887(501)>:31544]) will be created as active
default	14:03:08.493654-0400	ControlCenter	[app<application.com.nexy.assistant.17524881.17524887>:31544] Workspace state did change: XX-None[0] --> BG-Active[40] (assertion acquired).
default	14:03:08.493805-0400	runningboardd	[app<application.com.nexy.assistant.17524881.17524887(501)>:31544] Ignoring jetsam update because this process is not memory-managed
default	14:03:08.493817-0400	runningboardd	[app<application.com.nexy.assistant.17524881.17524887(501)>:31544] Ignoring suspend because this process is not lifecycle managed
default	14:03:08.493890-0400	runningboardd	[app<application.com.nexy.assistant.17524881.17524887(501)>:31544] Ignoring GPU update because this process is not GPU managed
default	14:03:08.493988-0400	runningboardd	[app<application.com.nexy.assistant.17524881.17524887(501)>:31544] Ignoring memory limit update because this process is not memory-managed
default	14:03:08.500552-0400	Nexy	SignalReady: pid=31544 asn=0x0-0x3bc3bc
default	14:03:08.500813-0400	Nexy	SIGNAL: pid=31544 asn=0x0x-0x3bc3bc
default	14:03:08.501375-0400	loginwindow	-[Application updateInformation] | Got App URL: file:///Applications/Nexy.app/
default	14:03:08.504983-0400	Nexy	[com.apple.controlcenter:BD5BA3B6-D225-4F6E-B75F-94A9AB64BF69-Aux[1]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
default	14:03:08.508392-0400	Nexy	void _NSEnableAutomaticTerminationAndLog(NSString *) Restoring windows
default	14:03:08.511837-0400	ControlCenter	Starting to track host; (bid:com.nexy.assistant-Item-0-31544)
default	14:03:08.511950-0400	ControlCenter	Created new displayable type DisplayableAppStatusItemType(42F8EAFA, (bid:com.nexy.assistant-Item-0-31544)) for (bid:com.nexy.assistant-Item-0-31544)
default	14:03:08.512387-0400	ControlCenter	Adding displayable items for status items; [(bid:com.nexy.assistant-Item-0-31544)]
default	14:03:08.512505-0400	ControlCenter	Created instance DisplayableId(A8732864) in .menuBar for DisplayableAppStatusItemType(42F8EAFA, (bid:com.nexy.assistant-Item-0-31544)) .menuBar
default	14:03:08.518907-0400	Nexy	[0xb8f93a800] activating connection: mach=false listener=false peer=false name=(anonymous)
default	14:03:08.519449-0400	Nexy	[0xb8f93a940] activating connection: mach=false listener=true peer=false name=(anonymous)
default	14:03:08.519464-0400	Nexy	[0xb8f93a940] Connection returned listener port: 0x1fa03
default	14:03:08.520987-0400	Nexy	[0xb8f938dc0] invalidated after the last release of the connection object
default	14:03:08.521796-0400	Nexy	[C:2] Alloc <private>
default	14:03:08.521831-0400	Nexy	[0xb8f938dc0] activating connection: mach=false listener=false peer=false name=(anonymous)
error	14:03:08.521986-0400	kernel	Sandbox: WindowManager(584) deny(1) mach-task-name others [Nexy(31544)]
default	14:03:08.523504-0400	WindowManager	Connection activated | (31544) Nexy
default	14:03:08.524511-0400	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.17524881.17524887(501)>:31544] from originator [app<application.com.nexy.assistant.17524881.17524887(501)>:31544] with description <RBSAssertionDescriptor| "AudioHAL" ID:398-31544-42905 target:31544 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	14:03:08.524573-0400	runningboardd	Assertion 398-31544-42905 (target:[app<application.com.nexy.assistant.17524881.17524887(501)>:31544]) will be created as active
default	14:03:08.524904-0400	runningboardd	Invalidating assertion 398-31544-42905 (target:[app<application.com.nexy.assistant.17524881.17524887(501)>:31544]) from originator [app<application.com.nexy.assistant.17524881.17524887(501)>:31544]
default	14:03:08.524935-0400	runningboardd	[app<application.com.nexy.assistant.17524881.17524887(501)>:31544] Ignoring jetsam update because this process is not memory-managed
default	14:03:08.524971-0400	runningboardd	[app<application.com.nexy.assistant.17524881.17524887(501)>:31544] Ignoring suspend because this process is not lifecycle managed
default	14:03:08.525029-0400	runningboardd	[app<application.com.nexy.assistant.17524881.17524887(501)>:31544] Ignoring GPU update because this process is not GPU managed
default	14:03:08.525121-0400	ControlCenter	Created ephemaral instance DisplayableId(A8732864) for (bid:com.nexy.assistant-Item-0-31544) with positioning .ephemeral
default	14:03:08.525077-0400	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.17524881.17524887(501)>:31544] from originator [app<application.com.nexy.assistant.17524881.17524887(501)>:31544] with description <RBSAssertionDescriptor| "AudioHAL" ID:398-31544-42906 target:31544 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	14:03:08.525140-0400	runningboardd	Assertion 398-31544-42906 (target:[app<application.com.nexy.assistant.17524881.17524887(501)>:31544]) will be created as active
default	14:03:08.525132-0400	runningboardd	[app<application.com.nexy.assistant.17524881.17524887(501)>:31544] Ignoring memory limit update because this process is not memory-managed
default	14:03:08.537395-0400	Nexy	[com.apple.controlcenter:BD5BA3B6-D225-4F6E-B75F-94A9AB64BF69] Received action(s): NSStatusItemChangeVisibilityAction
default	14:03:08.539789-0400	Nexy	[com.apple.controlcenter:BD5BA3B6-D225-4F6E-B75F-94A9AB64BF69] Observer <NSSceneStatusItem: 0xb8e0be680> handled action(s): <private>
default	14:03:08.540541-0400	Nexy	[com.apple.controlcenter:BD5BA3B6-D225-4F6E-B75F-94A9AB64BF69-Aux[1]-NSStatusItemView] Received action(s) in scene-update: NSSceneFenceAction
default	14:03:08.542674-0400	Nexy	[com.apple.controlcenter:BD5BA3B6-D225-4F6E-B75F-94A9AB64BF69-Aux[1]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
error	14:03:08.543767-0400	Nexy	It's not legal to call -layoutSubtreeIfNeeded on a view which is already being laid out.  If you are implementing the view's -layout method, you can call -[super layout] instead.  Break on void _NSDetectedLayoutRecursion(void) to debug.  This will be logged only once.  This may break in the future.
default	14:03:08.543872-0400	Nexy	[com.apple.controlcenter:BD5BA3B6-D225-4F6E-B75F-94A9AB64BF69-Aux[1]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
default	14:03:08.547765-0400	Nexy	[com.apple.controlcenter:BD5BA3B6-D225-4F6E-B75F-94A9AB64BF69] Sending action(s) in update: NSSceneFenceAction
default	14:03:08.629266-0400	runningboardd	[app<application.com.nexy.assistant.17524881.17524887(501)>:31544] Ignoring jetsam update because this process is not memory-managed
default	14:03:08.629285-0400	runningboardd	[app<application.com.nexy.assistant.17524881.17524887(501)>:31544] Ignoring suspend because this process is not lifecycle managed
default	14:03:08.629295-0400	runningboardd	[app<application.com.nexy.assistant.17524881.17524887(501)>:31544] Ignoring GPU update because this process is not GPU managed
default	14:03:08.629312-0400	runningboardd	[app<application.com.nexy.assistant.17524881.17524887(501)>:31544] Ignoring memory limit update because this process is not memory-managed
default	14:03:08.633558-0400	runningboardd	Calculated state for app<application.com.nexy.assistant.17524881.17524887(501)>: running-active (role: UserInteractiveFocal) (endowments: <private>)
default	14:03:08.634012-0400	ControlCenter	Received state update for 31544 (app<application.com.nexy.assistant.17524881.17524887(501)>, running-active-NotVisible
default	14:03:08.634114-0400	gamepolicyd	Received state update for 31544 (app<application.com.nexy.assistant.17524881.17524887(501)>, running-active-NotVisible
default	14:03:08.639398-0400	Nexy	*warn* MailCS ======%%% _setMailMessageAttributes skip:1
default	14:03:08.643995-0400	Nexy	Start service name com.apple.spotlightknowledged
default	14:03:08.644757-0400	Nexy	[GMS] availability notification token 87
default	14:03:08.681905-0400	kernel	udp connect: [<IPv4-redacted>:54653<-><IPv4-redacted>:50051] interface:  (skipped: 0)
so_gencnt: 610278 so_state: 0x0002 process: Nexy:31544 bytes in/out: 0/0 pkts in/out: 0/0 error: 0 so_error: 0 svc/tc: 0 flow: 0xa5a7e2f2
default	14:03:08.681925-0400	kernel	udp_connection_summary [<IPv4-redacted>:54653<-><IPv4-redacted>:50051] interface:  (skipped: 0)
so_gencnt: 610278 so_state: 0x0002 process: Nexy:31544 Duration: 0.000 sec Conn_Time: 0.000 sec bytes in/out: 0/0 pkts in/out: 0/0 rxnospace pkts/bytes: 0/0 so_error: 0 svc/tc: 0 flow: 0xa5a7e2f2 flowctl: 0us (0x)
default	14:03:08.682459-0400	kernel	SK[9]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 974BC703-CA6F-4E26-9626-13136B196EBE flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.56802,dst=<IPv4-redacted>.50051,proto=0x06 mask=0x0000003f,hash=0xdacc31c2 tp_proto=0x06"
default	14:03:08.682566-0400	kernel	tcp connect outgoing: [<IPv4-redacted>:56802<-><IPv4-redacted>:50051] interface: en0 (skipped: 0)
so_gencnt: 610280 t_state: SYN_SENT process: Nexy:31544 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 22 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xa89f5445
default	14:03:08.694937-0400	Nexy	[com.apple.controlcenter:BD5BA3B6-D225-4F6E-B75F-94A9AB64BF69] Sending action(s) in update: NSSceneFenceAction
default	14:03:08.706056-0400	kernel	tcp connected: [<IPv4-redacted>:56802<-><IPv4-redacted>:50051] interface: en0 (skipped: 0)
so_gencnt: 610280 t_state: ESTABLISHED process: Nexy:31544 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 22 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xa89f5445
default	14:03:08.734678-0400	Nexy	[0xb8f93a6c0] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	14:03:08.735364-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=31544.7, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=31544, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	14:03:08.736489-0400	tccd	AUTHREQ_SUBJECT: msgID=31544.7, subject=com.nexy.assistant,
default	14:03:08.737119-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d116a00 at /Applications/Nexy.app
default	14:03:08.749015-0400	Nexy	[0xb8f93a6c0] invalidated after the last release of the connection object
default	14:03:08.749783-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=393.2139, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=31544, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=393, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	14:03:08.749818-0400	tccd	requestor: TCCDProcess: identifier=com.apple.WindowServer, pid=393, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=31544, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	14:03:08.750684-0400	tccd	AUTHREQ_SUBJECT: msgID=393.2139, subject=com.nexy.assistant,
default	14:03:08.751240-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d116a00 at /Applications/Nexy.app
default	14:03:08.753079-0400	ControlCenter	[app<application.com.nexy.assistant.17524881.17524887>:31544] Workspace state did change: BG-Active[40] --> XX-None[0] (assertion dropped).
default	14:03:08.753164-0400	runningboardd	Invalidating assertion 398-632-42904 (target:[app<application.com.nexy.assistant.17524881.17524887(501)>:31544]) from originator [osservice<com.apple.controlcenter(501)>:632]
default	14:03:08.761447-0400	Nexy	[0xb8f93a6c0] activating connection: mach=false listener=false peer=false name=com.apple.hiservices-xpcservice
default	14:03:08.763602-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=393.2140, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=31544, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=393, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	14:03:08.763629-0400	tccd	requestor: TCCDProcess: identifier=com.apple.WindowServer, pid=393, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=31544, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	14:03:08.764437-0400	tccd	AUTHREQ_SUBJECT: msgID=393.2140, subject=com.nexy.assistant,
default	14:03:08.765002-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d116a00 at /Applications/Nexy.app
default	14:03:08.766109-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=31581.1, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=31544, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.osascript, pid=31581, auid=501, euid=501, binary_path=/usr/bin/osascript}, },
default	14:03:08.767262-0400	tccd	AUTHREQ_SUBJECT: msgID=31581.1, subject=com.nexy.assistant,
default	14:03:08.767798-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117900 at /Applications/Nexy.app
default	14:03:08.781121-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=393.2141, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=31544, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.osascript, pid=31581, auid=501, euid=501, binary_path=/usr/bin/osascript}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=393, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	14:03:08.781250-0400	Nexy	+[IMKClient subclass]: chose IMKClient_Modern
default	14:03:08.781271-0400	Nexy	+[IMKInputSession subclass]: chose IMKInputSession_Modern
default	14:03:08.781932-0400	tccd	AUTHREQ_SUBJECT: msgID=393.2141, subject=com.nexy.assistant,
default	14:03:08.782480-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117900 at /Applications/Nexy.app
default	14:03:08.783376-0400	Nexy	[0xb8f938140] activating connection: mach=true listener=false peer=false name=com.apple.inputmethodkit.getxpcendpoint
default	14:03:08.784504-0400	Nexy	[0xb8f93aa80] activating connection: mach=true listener=false peer=false name=com.apple.inputmethodkit.getxpcendpoint
default	14:03:08.785120-0400	Nexy	[0xb8f93abc0] activating connection: mach=false listener=false peer=false name=(anonymous)
default	14:03:08.785312-0400	Nexy	[0xb8f93ae40] activating connection: mach=false listener=false peer=false name=(anonymous)
default	14:03:08.785617-0400	DictationIM	setting current input controller = com.nexy.assistant
default	14:03:08.786187-0400	Nexy	[0xb8f93ad00] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
error	14:03:08.786783-0400	tccd	TCCDProcess: identifier=com.nexy.assistant, pid=31544, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy attempted to call TCCAccessRequest for kTCCServiceAccessibility without the recommended com.apple.private.tcc.manager.check-by-audit-token entitlement
default	14:03:08.786869-0400	Nexy	[0xb8f93ad00] invalidated after the last release of the connection object
default	14:03:08.791465-0400	Nexy	void _NSDisableAutomaticTerminationAndLog(NSString *) NSAccessibility Request Received
default	14:03:08.794615-0400	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	14:03:08.794663-0400	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant)]
default	14:03:08.794693-0400	ControlCenter	Active activity attributions changed to ["scr:com.nexy.assistant"]
default	14:03:08.795141-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:03:08.795154-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:03:08.795164-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	14:03:08.795170-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:03:08.795176-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	14:03:08.795181-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	14:03:08.795253-0400	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	14:03:08.815982-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117900 at /Applications/Nexy.app
default	14:03:08.830008-0400	System Events	TCCAccessRequestIndirect: TCCAccessRequestIndirect with pid 29142: target_identity: {
    kTCCCodeIdentityAuditToken = {length = 32, bytes = 0xf5010000 f5010000 14000000 f5010000 ... b7860100 cb680300 };
    kTCCCodeIdentityAuthority = kTCCCodeIdentityDesignatedRequirementAuthority;
    kTCCCodeIdentityCSFlags = 536941313;
    kTCCCodeIdentityCanSendToAnyTarget = 0;
    kTCCCodeIdentityDesignatedRequirementData = {length = 160, bytes = 0xfade0c00 000000a0 00000001 00000006 ... 4c32434c 42390000 };
    kTCCCodeIdentityExecutableURL = "file:///Applications/Nexy.app/Contents/MacOS/Nexy";
    kTCCCodeIdentityIdentifier = "com.nexy.assistant";
    kTCCCodeIdentityIdentifierType = 0;
    kTCCCodeIdentityPlatformType = 1;
    kTCCCodeIdentityPromptPolicy = 2;
    kTCCCodeIdentitySDKVersion = 984064;
    kTCCCodeIdentityTeamID = 5NKLL2CLB9;
}
default	14:03:08.839967-0400	tccd	target_executable_path_URL: file:///Applications/Nexy.app/Contents/MacOS/Nexy
default	14:03:08.865868-0400	WindowServer	0[outside of RPC]: [DeferringManager] Updating policy {
    advicePolicy: .frontmost;
    frontmostProcess: 0x0-0x3bc3bc (Nexy) mainConnectionID: 12538F;
} for reason: deferringPolicyEvaluationSuppression
default	14:03:08.865935-0400	WindowServer	0[outside of RPC]: [DeferringManager] Deferring events from frontmost process PSN 0x0-0x3bc3bc (Nexy) -> <pid: 31544>
default	14:03:08.866024-0400	WindowServer	new deferring rules for pid:393: [
    [393-189B]; <keyboardFocus; Nexy:0x0-0x3bc3bc>; () -> <pid: 31544>; reason: frontmost PSN --> outbound target,
    [393-189A]; <keyboardFocus; <frontmost>>; () -> <token: Nexy:0x0-0x3bc3bc; pid: 393>; reason: frontmost PSN,
    [393-1899]; <keyboardFocus>; () -> <token: <frontmost>; pid: 393>; reason: Deferring to <frontmost>
]
default	14:03:08.866058-0400	WindowServer	[keyboardFocus 0x7facf2b20] setRules:forPID(393): [
    [393-189B]; <keyboardFocus; Nexy:0x0-0x3bc3bc>; () -> <pid: 31544>; reason: frontmost PSN --> outbound target,
    [393-189A]; <keyboardFocus; <frontmost>>; () -> <token: Nexy:0x0-0x3bc3bc; pid: 393>; reason: frontmost PSN,
    [393-1899]; <keyboardFocus>; () -> <token: <frontmost>; pid: 393>; reason: Deferring to <frontmost>
]
default	14:03:08.866756-0400	WindowServer	chain did update (setDeferringRules) <keyboardFocus; display: null> containsEndOfChain: YES; [
    <token: <frontmost>; pid: 393>,
    <token: Nexy:0x0-0x3bc3bc; pid: 393>,
    <pid: 31544>
]
default	14:03:08.943849-0400	runningboardd	[app<application.com.nexy.assistant.17524881.17524887(501)>:31544] Ignoring jetsam update because this process is not memory-managed
default	14:03:08.943875-0400	runningboardd	[app<application.com.nexy.assistant.17524881.17524887(501)>:31544] Ignoring suspend because this process is not lifecycle managed
default	14:03:08.943892-0400	runningboardd	[app<application.com.nexy.assistant.17524881.17524887(501)>:31544] Ignoring GPU update because this process is not GPU managed
default	14:03:08.943948-0400	runningboardd	[app<application.com.nexy.assistant.17524881.17524887(501)>:31544] Ignoring memory limit update because this process is not memory-managed
default	14:03:09.018237-0400	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.17524881.17524887(501)>:31544] from originator [osservice<com.apple.WindowServer(88)>:393] with description <RBSAssertionDescriptor| "AppDrawing" ID:398-393-42917 target:31544 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"AppDrawing" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	14:03:09.018306-0400	runningboardd	Assertion 398-393-42917 (target:[app<application.com.nexy.assistant.17524881.17524887(501)>:31544]) will be created as active
default	14:03:09.018627-0400	runningboardd	[app<application.com.nexy.assistant.17524881.17524887(501)>:31544] Ignoring jetsam update because this process is not memory-managed
default	14:03:09.018637-0400	runningboardd	[app<application.com.nexy.assistant.17524881.17524887(501)>:31544] Ignoring suspend because this process is not lifecycle managed
default	14:03:09.018646-0400	runningboardd	[app<application.com.nexy.assistant.17524881.17524887(501)>:31544] Ignoring GPU update because this process is not GPU managed
default	14:03:09.018662-0400	runningboardd	[app<application.com.nexy.assistant.17524881.17524887(501)>:31544] Ignoring memory limit update because this process is not memory-managed
default	14:03:09.023365-0400	runningboardd	Calculated state for app<application.com.nexy.assistant.17524881.17524887(501)>: running-active (role: UserInteractiveFocal) (endowments: <private>)
default	14:03:09.023736-0400	ControlCenter	Received state update for 31544 (app<application.com.nexy.assistant.17524881.17524887(501)>, running-active-NotVisible
default	14:03:09.023827-0400	gamepolicyd	Received state update for 31544 (app<application.com.nexy.assistant.17524881.17524887(501)>, running-active-NotVisible
default	14:03:09.053611-0400	Nexy	                AUHAL.cpp:420   AUHAL: (0xb906de340) Selecting device 71 from constructor
default	14:03:09.053626-0400	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0xb906de340)
default	14:03:09.053632-0400	Nexy	                AUHAL.cpp:676   SelectDevice: (0xb906de340) not already running
default	14:03:09.053638-0400	Nexy	                AUHAL.cpp:752   SelectDevice: (0xb906de340) nothing to teardown
default	14:03:09.053642-0400	Nexy	                AUHAL.cpp:757   SelectDevice: (0xb906de340) connecting device 71
default	14:03:09.053745-0400	Nexy	                AUHAL.cpp:3413  IsDeviceUsable: (0xb906de340) Device ID: 71 (Input:No | Output:Yes): true
default	14:03:09.053862-0400	Nexy	                AUHAL.cpp:769   SelectDevice: (0xb906de340) created ioproc 0xc for device 71
default	14:03:09.054001-0400	Nexy	                AUHAL.cpp:858   SelectDevice: (0xb906de340) adding 7 device listeners to device 71
default	14:03:09.054234-0400	Nexy	                AUHAL.cpp:858   SelectDevice: (0xb906de340) adding 0 device delegate listeners to device 71
default	14:03:09.054243-0400	Nexy	                AUHAL.cpp:1581  UpdateStreamFormats: -> (0xb906de340)
default	14:03:09.054327-0400	Nexy	                AUHAL.cpp:1677  UpdateStreamFormats: 
  output stream 0 [0x48]:  2 ch,  48000 Hz, Float32, interleaved
default	14:03:09.054336-0400	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 1 output streams; not all mono
default	14:03:09.054342-0400	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	14:03:09.054351-0400	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 0 input streams; not all mono
default	14:03:09.054359-0400	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	14:03:09.054478-0400	Nexy	                AUHAL.cpp:1771  UpdateStreamFormats: AUHAL(0xb906de340) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	14:03:09.054488-0400	Nexy	                AUHAL.cpp:1777  UpdateStreamFormats: AUHAL(0xb906de340) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	14:03:09.054495-0400	Nexy	                AUHAL.cpp:1787  UpdateStreamFormats: <-
default	14:03:09.054501-0400	Nexy	                AUHAL.cpp:895   SelectDevice: (0xb906de340) removing 0 device listeners from device 0
default	14:03:09.054507-0400	Nexy	                AUHAL.cpp:895   SelectDevice: (0xb906de340) removing 0 device delegate listeners from device 0
default	14:03:09.054511-0400	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0xb906de340)
default	14:03:09.054522-0400	Nexy	                AUHAL.cpp:2298  SetProperty: (0xb906de340) caller requesting device change from 71 to 71
default	14:03:09.054527-0400	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0xb906de340)
default	14:03:09.054532-0400	Nexy	                AUHAL.cpp:659   SelectDevice: <- (0xb906de340) exiting with nothing to do
default	14:03:09.054987-0400	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	14:03:09.055238-0400	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	14:03:09.056786-0400	Nexy	                AUHAL.cpp:473   ~AUHAL: (0xb906de340) Selecting device 0 from destructor
default	14:03:09.056792-0400	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0xb906de340)
default	14:03:09.056797-0400	Nexy	                AUHAL.cpp:676   SelectDevice: (0xb906de340) not already running
default	14:03:09.056801-0400	Nexy	                AUHAL.cpp:682   SelectDevice: (0xb906de340) disconnecting device 71
default	14:03:09.056806-0400	Nexy	                AUHAL.cpp:746   SelectDevice: (0xb906de340) destroying ioproc 0xc for device 71
default	14:03:09.056835-0400	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Output {BuiltInSpeakerDevice, 0xc}
default	14:03:09.056885-0400	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	14:03:09.056966-0400	Nexy	                AUHAL.cpp:848   SelectDevice: (0xb906de340) nothing to setup
default	14:03:09.056974-0400	Nexy	                AUHAL.cpp:858   SelectDevice: (0xb906de340) adding 0 device listeners to device 0
default	14:03:09.056979-0400	Nexy	                AUHAL.cpp:858   SelectDevice: (0xb906de340) adding 0 device delegate listeners to device 0
default	14:03:09.056983-0400	Nexy	                AUHAL.cpp:895   SelectDevice: (0xb906de340) removing 7 device listeners from device 71
default	14:03:09.057138-0400	Nexy	                AUHAL.cpp:895   SelectDevice: (0xb906de340) removing 0 device delegate listeners from device 71
default	14:03:09.057147-0400	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0xb906de340)
default	14:03:09.057692-0400	Nexy	                AUHAL.cpp:420   AUHAL: (0xb906de340) Selecting device 71 from constructor
default	14:03:09.057699-0400	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0xb906de340)
default	14:03:09.057703-0400	Nexy	                AUHAL.cpp:676   SelectDevice: (0xb906de340) not already running
default	14:03:09.057707-0400	Nexy	                AUHAL.cpp:752   SelectDevice: (0xb906de340) nothing to teardown
default	14:03:09.057710-0400	Nexy	                AUHAL.cpp:757   SelectDevice: (0xb906de340) connecting device 71
default	14:03:09.057770-0400	Nexy	                AUHAL.cpp:3413  IsDeviceUsable: (0xb906de340) Device ID: 71 (Input:No | Output:Yes): true
default	14:03:09.057846-0400	Nexy	                AUHAL.cpp:769   SelectDevice: (0xb906de340) created ioproc 0xd for device 71
default	14:03:09.057945-0400	Nexy	                AUHAL.cpp:858   SelectDevice: (0xb906de340) adding 7 device listeners to device 71
default	14:03:09.058090-0400	Nexy	                AUHAL.cpp:858   SelectDevice: (0xb906de340) adding 0 device delegate listeners to device 71
default	14:03:09.058099-0400	Nexy	                AUHAL.cpp:1581  UpdateStreamFormats: -> (0xb906de340)
default	14:03:09.058161-0400	Nexy	                AUHAL.cpp:1677  UpdateStreamFormats: 
  output stream 0 [0x48]:  2 ch,  48000 Hz, Float32, interleaved
default	14:03:09.058167-0400	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 1 output streams; not all mono
default	14:03:09.058171-0400	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	14:03:09.058177-0400	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 0 input streams; not all mono
default	14:03:09.058185-0400	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	14:03:09.058269-0400	Nexy	                AUHAL.cpp:1771  UpdateStreamFormats: AUHAL(0xb906de340) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	14:03:09.058284-0400	Nexy	                AUHAL.cpp:1777  UpdateStreamFormats: AUHAL(0xb906de340) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	14:03:09.058291-0400	Nexy	                AUHAL.cpp:1787  UpdateStreamFormats: <-
default	14:03:09.058296-0400	Nexy	                AUHAL.cpp:895   SelectDevice: (0xb906de340) removing 0 device listeners from device 0
default	14:03:09.058300-0400	Nexy	                AUHAL.cpp:895   SelectDevice: (0xb906de340) removing 0 device delegate listeners from device 0
default	14:03:09.058305-0400	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0xb906de340)
default	14:03:09.058312-0400	Nexy	                AUHAL.cpp:2298  SetProperty: (0xb906de340) caller requesting device change from 71 to 71
default	14:03:09.058317-0400	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0xb906de340)
default	14:03:09.058321-0400	Nexy	                AUHAL.cpp:659   SelectDevice: <- (0xb906de340) exiting with nothing to do
default	14:03:09.058326-0400	Nexy	AudioHardware-mac-imp.cpp:1299   AudioObjectAddPropertyListener: listener was already added
default	14:03:09.058613-0400	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	14:03:09.058829-0400	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	14:03:09.060884-0400	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.17524881.17524887(501)>:31544] from originator [app<application.com.nexy.assistant.17524881.17524887(501)>:31544] with description <RBSAssertionDescriptor| "AudioHAL" ID:398-31544-42918 target:31544 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	14:03:09.060957-0400	runningboardd	Assertion 398-31544-42918 (target:[app<application.com.nexy.assistant.17524881.17524887(501)>:31544]) will be created as active
default	14:03:09.061295-0400	runningboardd	[app<application.com.nexy.assistant.17524881.17524887(501)>:31544] Ignoring jetsam update because this process is not memory-managed
default	14:03:09.061342-0400	runningboardd	[app<application.com.nexy.assistant.17524881.17524887(501)>:31544] Ignoring suspend because this process is not lifecycle managed
default	14:03:09.061305-0400	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.17524881.17524887(501)>:31544] from originator [osservice<com.apple.powerd>:334] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:398-334-42919 target:31544 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	14:03:09.061398-0400	runningboardd	[app<application.com.nexy.assistant.17524881.17524887(501)>:31544] Ignoring GPU update because this process is not GPU managed
default	14:03:09.061517-0400	runningboardd	[app<application.com.nexy.assistant.17524881.17524887(501)>:31544] Ignoring memory limit update because this process is not memory-managed
default	14:03:09.061522-0400	runningboardd	Assertion 398-334-42919 (target:[app<application.com.nexy.assistant.17524881.17524887(501)>:31544]) will be created as active
default	14:03:09.067164-0400	runningboardd	Calculated state for app<application.com.nexy.assistant.17524881.17524887(501)>: running-active (role: UserInteractiveFocal) (endowments: <private>)
default	14:03:09.067485-0400	runningboardd	[app<application.com.nexy.assistant.17524881.17524887(501)>:31544] Ignoring jetsam update because this process is not memory-managed
default	14:03:09.067495-0400	runningboardd	[app<application.com.nexy.assistant.17524881.17524887(501)>:31544] Ignoring suspend because this process is not lifecycle managed
default	14:03:09.067503-0400	runningboardd	[app<application.com.nexy.assistant.17524881.17524887(501)>:31544] Ignoring GPU update because this process is not GPU managed
default	14:03:09.067519-0400	runningboardd	[app<application.com.nexy.assistant.17524881.17524887(501)>:31544] Ignoring memory limit update because this process is not memory-managed
default	14:03:09.074121-0400	runningboardd	Calculated state for app<application.com.nexy.assistant.17524881.17524887(501)>: running-active (role: UserInteractiveFocal) (endowments: <private>)
default	14:03:09.088366-0400	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {BuiltInSpeakerDevice, 0xd}
default	14:03:09.089071-0400	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ef03f","name":"Nexy(31544)"}, "details":{"deviceUIDs":[],"implicit_category":"MediaPlayback","input_running":false,"output_running":true} }
default	14:03:09.089149-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 64, PID = 31544, Name = sid:0x1ef03f, Nexy(31544), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	14:03:09.089175-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Category/Mode changed -- The score for sid:0x1ef03f, Nexy(31544), 'prim'/com.nexy.assistant was not correct. Old score = 201
default	14:03:09.089204-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 64, PID = 31544, Name = sid:0x1ef03f, Nexy(31544), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	14:03:09.089237-0400	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1ef03f, Nexy(31544), 'prim'', AudioCategory changed to 'MediaPlayback'
default	14:03:09.089257-0400	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:03:09.089283-0400	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 64, PID = 31544, Name = sid:0x1ef03f, Nexy(31544), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO> is going active
default	14:03:09.089314-0400	audiomxd	-MXCoreSession- -[MXCoreSession updateIsPlaying:]: MXCoreSession com.nexy.assistant with category/mode MediaPlayback/Default and coreSessionID = 64 starting playing
default	14:03:09.089378-0400	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:03:09.089411-0400	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:03:09.089405-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 64, PID = 31544, Name = sid:0x1ef03f, Nexy(31544), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	14:03:09.089457-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 64, PID = 31544, Name = sid:0x1ef03f, Nexy(31544), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO>
default	14:03:09.089483-0400	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1ef03f, Nexy(31544), 'prim'', displayID:'com.nexy.assistant'}
default	14:03:09.089504-0400	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Will try to see if we can get the shared route for session = <ID: 64, PID = 31544, Name = sid:0x1ef03f, Nexy(31544), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO>. Old (200) and New (201) scores.
default	14:03:09.089663-0400	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 1]. BT device UIDS: {(
)}
default	14:03:09.089677-0400	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	14:03:09.089603-0400	audiomxd	AudioApplicationInfoImpl.mm:395   Successfully updated session 0x1ef03f to isSessionRecording: 0
	app: {"name":"[implicit] Nexy","pid":31544}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1ef03f, sessionType: 'prim', isRecording: false }, 
]
default	14:03:09.089644-0400	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 201, deviceID = <private>
default	14:03:09.089818-0400	audioaccessoryd	Routing request Wx NULL score 201 flag 0x1 < Hijack > app com.nexy.assistant CID 0xD310001 category Not set
default	14:03:09.089957-0400	audiomxd	UpdateAudioState CID 0xD310001 audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	14:03:09.090019-0400	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 201,
}
default	14:03:09.090043-0400	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	14:03:09.090055-0400	audioaccessoryd	AudioStateChanged: Added audio session app com.nexy.assistant NULL -> 201 count 2
default	14:03:09.090066-0400	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 201
error	14:03:09.090085-0400	audioaccessoryd	Updating local audio category 100 -> 201 app com.nexy.assistant
default	14:03:09.090116-0400	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.nexy.assistant
default	14:03:09.128938-0400	ControlCenter	Received state update for 31544 (app<application.com.nexy.assistant.17524881.17524887(501)>, running-active-NotVisible
default	14:03:09.129170-0400	gamepolicyd	Received state update for 31544 (app<application.com.nexy.assistant.17524881.17524887(501)>, running-active-NotVisible
default	14:03:09.883253-0400	runningboardd	Invalidating assertion 398-363-42899 (target:[app<application.com.nexy.assistant.17524881.17524887(501)>:31544]) from originator [osservice<com.apple.coreservices.launchservicesd>:363]
default	14:03:09.883430-0400	runningboardd	Invalidating assertion 398-363-42900 (target:[app<application.com.nexy.assistant.17524881.17524887(501)>:31544]) from originator [osservice<com.apple.coreservices.launchservicesd>:363]
default	14:03:09.890134-0400	Nexy	void _updateToReflectAutomaticTerminationState(void) Setting _kLSApplicationWouldBeTerminatedByTALKey=1
default	14:03:09.990365-0400	runningboardd	[app<application.com.nexy.assistant.17524881.17524887(501)>:31544] Ignoring jetsam update because this process is not memory-managed
default	14:03:09.990376-0400	runningboardd	[app<application.com.nexy.assistant.17524881.17524887(501)>:31544] Ignoring suspend because this process is not lifecycle managed
default	14:03:09.990413-0400	runningboardd	[app<application.com.nexy.assistant.17524881.17524887(501)>:31544] Set darwin role to: UserInteractive
default	14:03:09.990423-0400	runningboardd	[app<application.com.nexy.assistant.17524881.17524887(501)>:31544] Ignoring GPU update because this process is not GPU managed
default	14:03:09.990442-0400	runningboardd	[app<application.com.nexy.assistant.17524881.17524887(501)>:31544] Ignoring memory limit update because this process is not memory-managed
default	14:03:09.994771-0400	runningboardd	Calculated state for app<application.com.nexy.assistant.17524881.17524887(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	14:03:09.995361-0400	ControlCenter	Received state update for 31544 (app<application.com.nexy.assistant.17524881.17524887(501)>, running-active-NotVisible
default	14:03:09.995662-0400	gamepolicyd	Received state update for 31544 (app<application.com.nexy.assistant.17524881.17524887(501)>, running-active-NotVisible
default	14:03:10.030858-0400	audioaccessoryd	AudioStateSnapshot: Route:Speaker App com.nexy.assistant, Score 201, Remote -1NumofApp 2
default	14:03:10.561709-0400	runningboardd	Invalidating assertion 398-632-42901 (target:app<application.com.nexy.assistant.17524881.17524887(501)>) from originator [osservice<com.apple.controlcenter(501)>:632]
default	14:03:10.664922-0400	runningboardd	Removed last relative-start-date-defining assertion for process app<application.com.nexy.assistant.17524881.17524887(501)>
default	14:03:10.665998-0400	runningboardd	[app<application.com.nexy.assistant.17524881.17524887(501)>:31544] Ignoring jetsam update because this process is not memory-managed
default	14:03:10.666032-0400	runningboardd	[app<application.com.nexy.assistant.17524881.17524887(501)>:31544] Ignoring suspend because this process is not lifecycle managed
default	14:03:10.666058-0400	runningboardd	[app<application.com.nexy.assistant.17524881.17524887(501)>:31544] Ignoring GPU update because this process is not GPU managed
default	14:03:10.666105-0400	runningboardd	[app<application.com.nexy.assistant.17524881.17524887(501)>:31544] Ignoring memory limit update because this process is not memory-managed
default	14:03:10.674314-0400	runningboardd	Calculated state for app<application.com.nexy.assistant.17524881.17524887(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	14:03:10.681830-0400	ControlCenter	Received state update for 31544 (app<application.com.nexy.assistant.17524881.17524887(501)>, running-active-NotVisible
default	14:03:10.682050-0400	gamepolicyd	Received state update for 31544 (app<application.com.nexy.assistant.17524881.17524887(501)>, running-active-NotVisible
default	14:03:11.280322-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d114000 at /Applications/Nexy.app
default	14:03:11.293911-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117900 at /Applications/Nexy.app
default	14:03:11.302902-0400	tccd	Publishing <TCCDEvent: type=Modify, service=kTCCServiceScreenCapture, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 0 subscribers: {
}
default	14:03:11.303122-0400	Nexy	CLEAR:
kTCCServiceScreenCapture
default	14:03:12.960580-0400	audioaccessoryd	AudioStateSnapshot: Route:Speaker App com.nexy.assistant, Score 201, Remote -1NumofApp 2
default	14:03:14.464890-0400	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Output {BuiltInSpeakerDevice, 0xd}
default	14:03:14.465312-0400	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ef03f","name":"Nexy(31544)"}, "details":{"deviceUIDs":[],"implicit_category":"","input_running":false,"output_running":false} }
default	14:03:14.465431-0400	audiomxd	-MXCoreSession- -[MXCoreSession updateIsPlaying:]: MXCoreSession com.nexy.assistant with category/mode MediaPlayback/Default and coreSessionID = 64 stopping playing
default	14:03:14.465507-0400	audiomxd	-MXCoreSession- -[MXCoreSession endInterruption:]: Session <ID: 64, PID = 31544, Name = sid:0x1ef03f, Nexy(31544), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> is going inactive
default	14:03:14.465579-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 64, PID = 31544, Name = sid:0x1ef03f, Nexy(31544), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	14:03:14.465678-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 64, PID = 31544, Name = sid:0x1ef03f, Nexy(31544), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	14:03:14.465996-0400	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 0]. BT device UIDS: {(
)}
default	14:03:14.466022-0400	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:03:14.466020-0400	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	14:03:14.466099-0400	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:03:14.465811-0400	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:03:14.466137-0400	audioaccessoryd	AudioStateChanged: Removed audio session app com.nexy.assistant 201 count 1
default	14:03:14.465884-0400	audiomxd	AudioApplicationInfoImpl.mm:395   Successfully updated session 0x1ef03f to isSessionRecording: 0
	app: {"name":"[implicit] Nexy","pid":31544}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1ef03f, sessionType: 'prim', isRecording: false }, 
]
default	14:03:14.504726-0400	runningboardd	Invalidating assertion 398-31544-42918 (target:[app<application.com.nexy.assistant.17524881.17524887(501)>:31544]) from originator [app<application.com.nexy.assistant.17524881.17524887(501)>:31544]
default	14:03:14.504854-0400	runningboardd	Invalidating assertion 398-334-42919 (target:[app<application.com.nexy.assistant.17524881.17524887(501)>:31544]) from originator [osservice<com.apple.powerd>:334]
default	14:03:14.592803-0400	runningboardd	[app<application.com.nexy.assistant.17524881.17524887(501)>:31544] Ignoring jetsam update because this process is not memory-managed
default	14:03:14.592814-0400	runningboardd	[app<application.com.nexy.assistant.17524881.17524887(501)>:31544] Ignoring suspend because this process is not lifecycle managed
default	14:03:14.592825-0400	runningboardd	[app<application.com.nexy.assistant.17524881.17524887(501)>:31544] Ignoring GPU update because this process is not GPU managed
default	14:03:14.592874-0400	runningboardd	[app<application.com.nexy.assistant.17524881.17524887(501)>:31544] Ignoring memory limit update because this process is not memory-managed
default	14:03:14.622319-0400	Nexy	[com.apple.controlcenter:BD5BA3B6-D225-4F6E-B75F-94A9AB64BF69] Sending action(s) in update: NSSceneFenceAction
default	14:03:14.704607-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=31583.1, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=31544, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.osascript, pid=31583, auid=501, euid=501, binary_path=/usr/bin/osascript}, },
default	14:03:14.706410-0400	tccd	AUTHREQ_SUBJECT: msgID=31583.1, subject=com.nexy.assistant,
default	14:03:14.707104-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117900 at /Applications/Nexy.app
default	14:03:14.722969-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=393.2147, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=31544, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.osascript, pid=31583, auid=501, euid=501, binary_path=/usr/bin/osascript}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=393, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	14:03:14.724065-0400	tccd	AUTHREQ_SUBJECT: msgID=393.2147, subject=com.nexy.assistant,
default	14:03:14.724670-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117900 at /Applications/Nexy.app
default	14:03:14.758223-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117900 at /Applications/Nexy.app
default	14:03:14.777134-0400	System Events	TCCAccessRequestIndirect: TCCAccessRequestIndirect with pid 29142: target_identity: {
    kTCCCodeIdentityAuditToken = {length = 32, bytes = 0xf5010000 f5010000 14000000 f5010000 ... b7860100 d0680300 };
    kTCCCodeIdentityAuthority = kTCCCodeIdentityDesignatedRequirementAuthority;
    kTCCCodeIdentityCSFlags = 536941313;
    kTCCCodeIdentityCanSendToAnyTarget = 0;
    kTCCCodeIdentityDesignatedRequirementData = {length = 160, bytes = 0xfade0c00 000000a0 00000001 00000006 ... 4c32434c 42390000 };
    kTCCCodeIdentityExecutableURL = "file:///Applications/Nexy.app/Contents/MacOS/Nexy";
    kTCCCodeIdentityIdentifier = "com.nexy.assistant";
    kTCCCodeIdentityIdentifierType = 0;
    kTCCCodeIdentityPlatformType = 1;
    kTCCCodeIdentityPromptPolicy = 2;
    kTCCCodeIdentitySDKVersion = 984064;
    kTCCCodeIdentityTeamID = 5NKLL2CLB9;
}
default	14:03:14.790884-0400	tccd	target_executable_path_URL: file:///Applications/Nexy.app/Contents/MacOS/Nexy
default	14:03:15.020462-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=393.2148, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=31544, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=393, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	14:03:15.020493-0400	tccd	requestor: TCCDProcess: identifier=com.apple.WindowServer, pid=393, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=31544, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	14:03:15.022203-0400	tccd	AUTHREQ_SUBJECT: msgID=393.2148, subject=com.nexy.assistant,
default	14:03:15.023092-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117900 at /Applications/Nexy.app
default	14:03:15.674164-0400	WindowServer	12538f[StealKeyFocusReturningID]: [DeferringManager] Updating policy {
    advicePolicy: .keyThief;
    frontmostProcess: 0x0-0x19019 (Finder) mainConnectionID: 7B703;
    keyThiefConnectionID: 12538F;
} for reason: key thief updated 12538f 0x0-0x3bc3bc (Nexy)
default	14:03:15.674256-0400	WindowServer	<BSCompoundAssertion:0x7fb015380> (com.apple.backboard.hid.delivery.localDelivery.preventFlushing) acquire for reason:key thief updated 12538f 0x0-0x3bc3bc (Nexy) <2080> acq:0x7fb26eaa0 count:1
default	14:03:15.728990-0400	Nexy	[com.apple.controlcenter:BD5BA3B6-D225-4F6E-B75F-94A9AB64BF69] Sending action(s) in update: NSSceneFenceAction
default	14:03:15.756159-0400	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.17524881.17524887(501)>:31544] from originator [osservice<com.apple.WindowServer(88)>:393] with description <RBSAssertionDescriptor| "AppVisible" ID:398-393-42928 target:31544 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"AppVisible" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	14:03:15.756273-0400	runningboardd	Assertion 398-393-42928 (target:[app<application.com.nexy.assistant.17524881.17524887(501)>:31544]) will be created as active
default	14:03:15.756639-0400	runningboardd	[app<application.com.nexy.assistant.17524881.17524887(501)>:31544] Ignoring jetsam update because this process is not memory-managed
default	14:03:15.756665-0400	runningboardd	[app<application.com.nexy.assistant.17524881.17524887(501)>:31544] Ignoring suspend because this process is not lifecycle managed
default	14:03:15.756685-0400	runningboardd	[app<application.com.nexy.assistant.17524881.17524887(501)>:31544] Ignoring GPU update because this process is not GPU managed
default	14:03:15.756732-0400	runningboardd	[app<application.com.nexy.assistant.17524881.17524887(501)>:31544] Ignoring memory limit update because this process is not memory-managed
default	14:03:15.761411-0400	runningboardd	Calculated state for app<application.com.nexy.assistant.17524881.17524887(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	14:03:15.762087-0400	ControlCenter	Received state update for 31544 (app<application.com.nexy.assistant.17524881.17524887(501)>, running-active-NotVisible
default	14:03:15.762202-0400	gamepolicyd	Received state update for 31544 (app<application.com.nexy.assistant.17524881.17524887(501)>, running-active-NotVisible
default	14:03:15.778419-0400	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.17524881.17524887(501)>:31544] from originator [osservice<com.apple.WindowServer(88)>:393] with description <RBSAssertionDescriptor| "FUSBProcessWindowState: visible" ID:398-393-42929 target:31544 attributes:[
	<RBSDomainAttribute| domain:"com.apple.fuseboard" name:"Visible" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	14:03:15.778518-0400	runningboardd	Assertion 398-393-42929 (target:[app<application.com.nexy.assistant.17524881.17524887(501)>:31544]) will be created as active
default	14:03:15.779078-0400	runningboardd	[app<application.com.nexy.assistant.17524881.17524887(501)>:31544] Ignoring jetsam update because this process is not memory-managed
default	14:03:15.779089-0400	runningboardd	[app<application.com.nexy.assistant.17524881.17524887(501)>:31544] Ignoring suspend because this process is not lifecycle managed
default	14:03:15.779100-0400	runningboardd	[app<application.com.nexy.assistant.17524881.17524887(501)>:31544] Ignoring GPU update because this process is not GPU managed
default	14:03:15.779119-0400	runningboardd	[app<application.com.nexy.assistant.17524881.17524887(501)>:31544] Ignoring memory limit update because this process is not memory-managed
default	14:03:15.779146-0400	runningboardd	[app<application.com.nexy.assistant.17524881.17524887(501)>:31544] visiblity is yes
default	14:03:15.783703-0400	runningboardd	Calculated state for app<application.com.nexy.assistant.17524881.17524887(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	14:03:15.784266-0400	ControlCenter	Received state update for 31544 (app<application.com.nexy.assistant.17524881.17524887(501)>, running-active-NotVisible
default	14:03:15.784296-0400	gamepolicyd	Received state update for 31544 (app<application.com.nexy.assistant.17524881.17524887(501)>, running-active-NotVisible
default	14:03:16.378117-0400	Nexy	[C:3] Alloc com.apple.backboard.hid-services.xpc
default	14:03:16.378192-0400	Nexy	[0xb8f93b980] activating connection: mach=false listener=false peer=false name=(anonymous)
error	14:03:16.378931-0400	Nexy	Unable to obtain a task name port right for pid 393: (os/kern) failure (0x5)
default	14:03:16.379334-0400	Nexy	BKSHIDEventDeliveryManager - connection activation
default	14:03:16.386352-0400	Nexy	[com.apple.controlcenter:BD5BA3B6-D225-4F6E-B75F-94A9AB64BF69] Sending action(s) in update: NSSceneFenceAction
default	14:03:16.403664-0400	runningboardd	Invalidating assertion 398-393-42928 (target:[app<application.com.nexy.assistant.17524881.17524887(501)>:31544]) from originator [osservice<com.apple.WindowServer(88)>:393]
default	14:03:16.405827-0400	runningboardd	Invalidating assertion 398-393-42929 (target:[app<application.com.nexy.assistant.17524881.17524887(501)>:31544]) from originator [osservice<com.apple.WindowServer(88)>:393]
default	14:03:16.508310-0400	runningboardd	Removed last relative-start-date-defining assertion for process app<application.com.nexy.assistant.17524881.17524887(501)>
default	14:03:16.510153-0400	runningboardd	[app<application.com.nexy.assistant.17524881.17524887(501)>:31544] Ignoring jetsam update because this process is not memory-managed
default	14:03:16.510173-0400	runningboardd	[app<application.com.nexy.assistant.17524881.17524887(501)>:31544] Ignoring suspend because this process is not lifecycle managed
default	14:03:16.510190-0400	runningboardd	[app<application.com.nexy.assistant.17524881.17524887(501)>:31544] Ignoring GPU update because this process is not GPU managed
default	14:03:16.510224-0400	runningboardd	[app<application.com.nexy.assistant.17524881.17524887(501)>:31544] Ignoring memory limit update because this process is not memory-managed
default	14:03:16.510250-0400	runningboardd	[app<application.com.nexy.assistant.17524881.17524887(501)>:31544] visiblity is no
default	14:03:16.518688-0400	runningboardd	Calculated state for app<application.com.nexy.assistant.17524881.17524887(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	14:03:16.519416-0400	ControlCenter	Received state update for 31544 (app<application.com.nexy.assistant.17524881.17524887(501)>, running-active-NotVisible
default	14:03:16.519593-0400	gamepolicyd	Received state update for 31544 (app<application.com.nexy.assistant.17524881.17524887(501)>, running-active-NotVisible
default	14:03:16.896100-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=31584.1, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=31544, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.osascript, pid=31584, auid=501, euid=501, binary_path=/usr/bin/osascript}, },
default	14:03:16.897646-0400	tccd	AUTHREQ_SUBJECT: msgID=31584.1, subject=com.nexy.assistant,
default	14:03:16.898281-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117900 at /Applications/Nexy.app
default	14:03:16.911870-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=393.2153, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=31544, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.osascript, pid=31584, auid=501, euid=501, binary_path=/usr/bin/osascript}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=393, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	14:03:16.912743-0400	tccd	AUTHREQ_SUBJECT: msgID=393.2153, subject=com.nexy.assistant,
default	14:03:16.913305-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117900 at /Applications/Nexy.app
default	14:03:16.941220-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117900 at /Applications/Nexy.app
default	14:03:16.957814-0400	System Events	TCCAccessRequestIndirect: TCCAccessRequestIndirect with pid 29142: target_identity: {
    kTCCCodeIdentityAuditToken = {length = 32, bytes = 0xf5010000 f5010000 14000000 f5010000 ... b7860100 d2680300 };
    kTCCCodeIdentityAuthority = kTCCCodeIdentityDesignatedRequirementAuthority;
    kTCCCodeIdentityCSFlags = 536941313;
    kTCCCodeIdentityCanSendToAnyTarget = 0;
    kTCCCodeIdentityDesignatedRequirementData = {length = 160, bytes = 0xfade0c00 000000a0 00000001 00000006 ... 4c32434c 42390000 };
    kTCCCodeIdentityExecutableURL = "file:///Applications/Nexy.app/Contents/MacOS/Nexy";
    kTCCCodeIdentityIdentifier = "com.nexy.assistant";
    kTCCCodeIdentityIdentifierType = 0;
    kTCCCodeIdentityPlatformType = 1;
    kTCCCodeIdentityPromptPolicy = 2;
    kTCCCodeIdentitySDKVersion = 984064;
    kTCCCodeIdentityTeamID = 5NKLL2CLB9;
}
default	14:03:16.969811-0400	tccd	target_executable_path_URL: file:///Applications/Nexy.app/Contents/MacOS/Nexy
default	14:03:18.865993-0400	ControlCenter	Recent activity attributions changed to ["scr:com.nexy.assistant", "mic:com.nexy.assistant"]
default	14:03:18.867408-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:03:18.867429-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:03:18.867445-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	14:03:18.867459-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:03:18.867469-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	14:03:18.867477-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	14:03:18.867604-0400	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	14:03:19.294017-0400	Nexy	LSExceptions shared instance invalidated for timeout.
default	14:03:19.702416-0400	WindowServer	12538f[StealKeyFocusReturningID]: [DeferringManager] Updating policy {
    advicePolicy: .keyThief;
    frontmostProcess: 0x0-0x19019 (Finder) mainConnectionID: 7B703;
    keyThiefConnectionID: 12538F;
} for reason: key thief updated 12538f 0x0-0x3bc3bc (Nexy)
default	14:03:19.702467-0400	WindowServer	<BSCompoundAssertion:0x7fb015380> (com.apple.backboard.hid.delivery.localDelivery.preventFlushing) acquire for reason:key thief updated 12538f 0x0-0x3bc3bc (Nexy) <2083> acq:0x7fd157120 count:1
default	14:03:19.727749-0400	Nexy	[com.apple.controlcenter:BD5BA3B6-D225-4F6E-B75F-94A9AB64BF69] Sending action(s) in update: NSSceneFenceAction
default	14:03:19.751029-0400	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.17524881.17524887(501)>:31544] from originator [osservice<com.apple.WindowServer(88)>:393] with description <RBSAssertionDescriptor| "AppVisible" ID:398-393-42934 target:31544 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"AppVisible" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	14:03:19.751110-0400	runningboardd	Assertion 398-393-42934 (target:[app<application.com.nexy.assistant.17524881.17524887(501)>:31544]) will be created as active
default	14:03:19.751717-0400	runningboardd	[app<application.com.nexy.assistant.17524881.17524887(501)>:31544] Ignoring jetsam update because this process is not memory-managed
default	14:03:19.751730-0400	runningboardd	[app<application.com.nexy.assistant.17524881.17524887(501)>:31544] Ignoring suspend because this process is not lifecycle managed
default	14:03:19.751741-0400	runningboardd	[app<application.com.nexy.assistant.17524881.17524887(501)>:31544] Ignoring GPU update because this process is not GPU managed
default	14:03:19.751766-0400	runningboardd	[app<application.com.nexy.assistant.17524881.17524887(501)>:31544] Ignoring memory limit update because this process is not memory-managed
default	14:03:19.756855-0400	runningboardd	Calculated state for app<application.com.nexy.assistant.17524881.17524887(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	14:03:19.757425-0400	ControlCenter	Received state update for 31544 (app<application.com.nexy.assistant.17524881.17524887(501)>, running-active-NotVisible
default	14:03:19.757546-0400	gamepolicyd	Received state update for 31544 (app<application.com.nexy.assistant.17524881.17524887(501)>, running-active-NotVisible
default	14:03:19.771892-0400	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.17524881.17524887(501)>:31544] from originator [osservice<com.apple.WindowServer(88)>:393] with description <RBSAssertionDescriptor| "FUSBProcessWindowState: visible" ID:398-393-42935 target:31544 attributes:[
	<RBSDomainAttribute| domain:"com.apple.fuseboard" name:"Visible" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	14:03:19.771970-0400	runningboardd	Assertion 398-393-42935 (target:[app<application.com.nexy.assistant.17524881.17524887(501)>:31544]) will be created as active
default	14:03:19.772350-0400	runningboardd	[app<application.com.nexy.assistant.17524881.17524887(501)>:31544] Ignoring jetsam update because this process is not memory-managed
default	14:03:19.772363-0400	runningboardd	[app<application.com.nexy.assistant.17524881.17524887(501)>:31544] Ignoring suspend because this process is not lifecycle managed
default	14:03:19.772380-0400	runningboardd	[app<application.com.nexy.assistant.17524881.17524887(501)>:31544] Ignoring GPU update because this process is not GPU managed
default	14:03:19.772418-0400	runningboardd	[app<application.com.nexy.assistant.17524881.17524887(501)>:31544] Ignoring memory limit update because this process is not memory-managed
default	14:03:19.772444-0400	runningboardd	[app<application.com.nexy.assistant.17524881.17524887(501)>:31544] visiblity is yes
default	14:03:19.776770-0400	runningboardd	Calculated state for app<application.com.nexy.assistant.17524881.17524887(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	14:03:19.777256-0400	ControlCenter	Received state update for 31544 (app<application.com.nexy.assistant.17524881.17524887(501)>, running-active-NotVisible
default	14:03:19.777317-0400	gamepolicyd	Received state update for 31544 (app<application.com.nexy.assistant.17524881.17524887(501)>, running-active-NotVisible
default	14:03:20.782867-0400	Nexy	terminate:
default	14:03:20.782892-0400	Nexy	void _NSDisableAutomaticTerminationAndLog(NSString *) Terminating
default	14:03:20.782911-0400	Nexy	-[NSApplication _pushPersistentStateTerminationGeneration] sPersistentStateTerminateStackHeight -> 1
default	14:03:20.783040-0400	Nexy	Attempting sudden termination (1st attempt)
default	14:03:20.783057-0400	Nexy	Checking whether app should terminate
default	14:03:20.783118-0400	Nexy	Asking app delegate whether applicationShouldTerminate:
default	14:03:20.783134-0400	Nexy	replyToApplicationShouldTerminate:YES
default	14:03:20.783179-0400	Nexy	App termination approved
default	14:03:20.783190-0400	Nexy	Termination commencing
default	14:03:20.783200-0400	Nexy	Attempting sudden termination (2nd attempt)
default	14:03:20.784893-0400	Nexy	Termination complete. Exiting without sudden termination.
default	14:03:20.785566-0400	Nexy	[0xb8f93b700] activating connection: mach=true listener=false peer=false name=com.apple.powerlog.plxpclogger.xpc
default	14:03:20.785628-0400	Nexy	Entering exit handler.
default	14:03:20.785672-0400	Nexy	Queueing exit procedure onto XPC queue. Any further messages sent will be discarded. activeSendTransactions=0
default	14:03:20.785825-0400	Nexy	Cancelling XPC connection. Any further reply handler invocations will not retry messages
default	14:03:20.785835-0400	Nexy	[0xb8f938a00] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	14:03:20.785851-0400	Nexy	Exiting exit handler.
default	14:03:20.789870-0400	Nexy	XPC connection invalidated (daemon unloaded/disabled)
default	14:03:20.792294-0400	WindowServer	0[outside of RPC]: Process death: 0x0-0x3bc3bc (Nexy) connectionID: 12538F pid: 31544 in session 0x101
default	14:03:20.792387-0400	WindowServer	<BSCompoundAssertion:0x7fb0154c0> ([FocusManager:257]-deferringPolicyEvaluationSuppression) acquire for reason:process death - 0x0-0x3bc3bc (Nexy) acq:0x7fd8f77a0 count:1
default	14:03:20.793270-0400	audiomxd	  ServerSessionManager.mm:472   { "action":"destroy_session", "session":{"ID":"0x1ef03f","name":"Nexy(31544)"}, "details":null }
default	14:03:20.793304-0400	audiomxd	AudioApplicationInfoImpl.mm:690   Successfully removed session 0x1ef03f from AudioApp, recording state unchanged (app: {"name":"[implicit] Nexy","pid":31544})
default	14:03:20.793318-0400	audiomxd	  ServerSessionManager.mm:1081  destroy audio app instance since was created implicitly by session creation and all sessions now gone (audio app: {"name":"[implicit] Nexy","pid":31544})
default	14:03:20.793648-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 64, PID = 31544, Name = sid:0x1ef03f, Nexy(31544), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	14:03:20.793747-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 64, PID = 31544, Name = sid:0x1ef03f, Nexy(31544), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	14:03:20.793802-0400	ControlCenter	[app<application.com.nexy.assistant.17524881.17524887>:31544] Workspace connection invalidated.
default	14:03:20.793833-0400	ControlCenter	[app<application.com.nexy.assistant.17524881.17524887>:31544] Now flagged as pending exit for reason: workspace client connection invalidated
default	14:03:20.794014-0400	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:03:20.794140-0400	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:03:20.794291-0400	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:03:20.794359-0400	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:03:20.795680-0400	WindowServer	0[outside of RPC]: [FocusManager:257] update to deferring policy requested for reason: permitted list updated - 0x0-0x3bc3bc removed - but we are suppressing evaluation for reasons: {(
    "process death - 0x0-0x3bc3bc (Nexy)"
)}
default	14:03:20.794414-0400	WindowManager	Connection invalidated | (31544) Nexy
default	14:03:20.796102-0400	WindowServer	0[outside of RPC]: [FocusManager:257] update to deferring policy requested for reason: permitted list updated - 0x1-0x7b38 removed - but we are suppressing evaluation for reasons: {(
    "process death - 0x0-0x3bc3bc (Nexy)"
)}
default	14:03:20.797343-0400	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:03:20.797501-0400	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:03:20.799195-0400	runningboardd	Invalidating assertion 398-393-42935 (target:[app<application.com.nexy.assistant.17524881.17524887(501)>:31544]) from originator [osservice<com.apple.WindowServer(88)>:393]
default	14:03:20.799309-0400	runningboardd	XPC connection invalidated: [app<application.com.nexy.assistant.17524881.17524887(501)>:31544]
default	14:03:20.799408-0400	runningboardd	Invalidating assertion 398-393-42934 (target:[app<application.com.nexy.assistant.17524881.17524887(501)>:31544]) from originator [osservice<com.apple.WindowServer(88)>:393]
default	14:03:20.812941-0400	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:56802<-><IPv4-redacted>:50051] interface: en0 (skipped: 0)
so_gencnt: 610280 t_state: FIN_WAIT_1 process: Nexy:31544 Duration: 12.131 sec Conn_Time: 0.024 sec bytes in/out: 504382/498 pkts in/out: 43/5 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 9 ACKs delayed: 23 delayed ACKs sent: 0
rtt: 37.812 ms rttvar: 22.750 ms base rtt: 22 ms so_error: 0 svc/tc: 0 flow: 0xa89f5445
default	14:03:20.812962-0400	kernel	tcp_connection_summary [<IPv4-redacted>:56802<-><IPv4-redacted>:50051] interface: en0 (skipped: 0)
so_gencnt: 610280 t_state: FIN_WAIT_1 process: Nexy:31544 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	14:03:20.815792-0400	loginwindow	-[ApplicationManager handleCASEvent:withData:] | CAS notification for appDeath for com.nexy.assistant with asn: LSASN:{hi=0x0;lo=0x3bc3bc} for bundle path: /Applications/Nexy.app with URL: file:///Applications/Nexy.app/
default	14:03:20.815821-0400	loginwindow	-[ApplicationManager(AppDeathHandler) appDeathCleanupHandler:forApp:] | Termination handler for: Nexy : 3916732
default	14:03:20.815926-0400	loginwindow	-[PersistentAppsSupport applicationQuit:] | for app:Nexy, _appTrackingState = 2
default	14:03:20.817472-0400	runningboardd	Invalidating assertion 398-363-42898 (target:[app<application.com.nexy.assistant.17524881.17524887(501)>:31544]) from originator [osservice<com.apple.coreservices.launchservicesd>:363]
default	14:03:20.817631-0400	runningboardd	[app<application.com.nexy.assistant.17524881.17524887(501)>:31544] termination reported by launchd (0, 0, 0)
default	14:03:20.817672-0400	runningboardd	Removing process: [app<application.com.nexy.assistant.17524881.17524887(501)>:31544]
default	14:03:20.817939-0400	runningboardd	Removing launch job for: [app<application.com.nexy.assistant.17524881.17524887(501)>:31544]
default	14:03:20.818165-0400	runningboardd	Removed job for [app<application.com.nexy.assistant.17524881.17524887(501)>:31544]
default	14:03:20.818218-0400	runningboardd	Removing assertions for terminated process: [app<application.com.nexy.assistant.17524881.17524887(501)>:31544]
default	14:03:20.818260-0400	runningboardd	Removed last relative-start-date-defining assertion for process app<application.com.nexy.assistant.17524881.17524887(501)>
default	14:03:20.827723-0400	runningboardd	Calculated state for app<application.com.nexy.assistant.17524881.17524887(501)>: none (role: None) (endowments: (null))
default	14:03:20.828075-0400	runningboardd	Calculated state for app<application.com.nexy.assistant.17524881.17524887(501)>: none (role: None) (endowments: (null))
default	14:03:20.828111-0400	audiomxd	  ServerSessionManager.mm:1322  Monitored process died, pid = 31544, name = Nexy
default	14:03:20.828023-0400	ControlCenter	[app<application.com.nexy.assistant.17524881.17524887>:31544] Process exited: <RBSProcessExitContext| voluntary>.
default	14:03:20.828046-0400	ControlCenter	[app<application.com.nexy.assistant.17524881.17524887>:31544] Setting process task state to: Not Running
default	14:03:20.828105-0400	ControlCenter	[app<application.com.nexy.assistant.17524881.17524887>:31544] Setting process visibility to: Unknown
default	14:03:20.828164-0400	ControlCenter	[app<application.com.nexy.assistant.17524881.17524887>:31544] Invalidating workspace.
default	14:03:20.828056-0400	ControlCenter	Received state update for 31544 (app<application.com.nexy.assistant.17524881.17524887(501)>, none-NotVisible
default	14:03:20.828213-0400	ControlCenter	Removing source registration for processHandle: [app<application.com.nexy.assistant.17524881.17524887(501)>:31544]
default	14:03:20.828469-0400	ControlCenter	Received state update for 31544 (app<application.com.nexy.assistant.17524881.17524887(501)>, none-NotVisible
default	14:03:20.828711-0400	ControlCenter	Removing: <FBApplicationProcess: 0xaf889aa00; app<application.com.nexy.assistant.17524881.17524887>:31544(v3685F)>
default	14:03:20.828767-0400	gamepolicyd	Received state update for 31544 (app<application.com.nexy.assistant.17524881.17524887(501)>, none-NotVisible
default	14:03:20.829041-0400	gamepolicyd	Received state update for 31544 (app<application.com.nexy.assistant.17524881.17524887(501)>, none-NotVisible
default	14:03:20.829236-0400	launchservicesd	Hit the server for a process handle cb8cfaf00007b38 that resolved to: [app<application.com.nexy.assistant.17524881.17524887(501)>:31544]
default	14:03:20.834752-0400	ControlCenter	Stopping tracking for host; (bid:com.nexy.assistant-Item-0-31544)
default	14:03:20.835722-0400	ControlCenter	Removing ephemeral displayable instance DisplayableId(A8732864) from menu bar. No corresponding host (bid:com.nexy.assistant-Item-0-31544)
default	14:03:20.835771-0400	ControlCenter	Removing displayables [DisplayableAppStatusItem(A8732864, (bid:com.nexy.assistant-Item-0-31544))]
default	14:03:20.945466-0400	ControlCenter	Recent activity attributions changed to ["scr:com.nexy.assistant"]
error	14:03:20.996984-0400	runningboardd	RBSStateCapture remove item called for untracked item 398-363-42898 (target:[app<application.com.nexy.assistant.17524881.17524887(501)>:31544])
error	14:03:20.997009-0400	runningboardd	RBSStateCapture remove item called for untracked item 398-393-42934 (target:[app<application.com.nexy.assistant.17524881.17524887(501)>:31544])
error	14:03:20.997025-0400	runningboardd	RBSStateCapture remove item called for untracked item 398-393-42935 (target:[app<application.com.nexy.assistant.17524881.17524887(501)>:31544])
default	14:03:53.633109-0400	loginwindow	-[ApplicationManager(AppDeathHandler) _appQuitTimer:] | _appQuitTimer fired for: ASN: 3838889, name: Nexy with url: file:///Applications/Nexy.app/
default	14:03:53.633363-0400	loginwindow	-[ApplicationManager(AppDeathHandler) _handleLingeringSubordinateProcesses:forApp:] | Last instance of app Nexy at /Applications/Nexy.app, handle lingering spawns.
default	14:03:53.633393-0400	loginwindow	-[ApplicationManager(AppDeathHandler) _handleLingeringSubordinateProcesses:forApp:] | Child applications for Nexy : (
)
default	14:03:53.633415-0400	loginwindow	-[ApplicationManager(AppDeathHandler) _handleLingeringSubordinateProcesses:forApp:] | App Nexy is fully cleaned up.  No user notification is necessary.  Done with handling.
default	14:04:20.817507-0400	loginwindow	-[ApplicationManager(AppDeathHandler) _appQuitTimer:] | _appQuitTimer fired for: ASN: 3916732, name: Nexy with url: file:///Applications/Nexy.app/
default	14:04:20.817708-0400	loginwindow	-[ApplicationManager(AppDeathHandler) _handleLingeringSubordinateProcesses:forApp:] | Last instance of app Nexy at /Applications/Nexy.app, handle lingering spawns.
default	14:04:20.817737-0400	loginwindow	-[ApplicationManager(AppDeathHandler) _handleLingeringSubordinateProcesses:forApp:] | Child applications for Nexy : (
)
default	14:04:20.817955-0400	loginwindow	-[ApplicationManager(AppDeathHandler) _handleLingeringSubordinateProcesses:forApp:] | App Nexy is fully cleaned up.  No user notification is necessary.  Done with handling.
