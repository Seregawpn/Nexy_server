default	14:51:00.174812-0500	lsd	com.nexy.assistant/Unknown Persona:5:5:1:1:Building bundle record for app
default	14:51:00.174962-0500	lsd	com.nexy.assistant/Unknown Persona:5:5:2:1:Built bundle record for app
default	14:51:00.176453-0500	lsd	com.nexy.assistant/Unknown Persona:5:4:2:1:_LSServerRegisterItemInfo result = 0
default	14:51:00.182369-0500	runningboardd	Launch request for app<application.com.nexy.assistant.21074037.21074043(501)>[0] is using uid 501 (divined from auid 501 euid 501)
default	14:51:00.182445-0500	runningboardd	Acquiring assertion targeting app<application.com.nexy.assistant.21074037.21074043(501)> from originator [osservice<com.apple.coreservices.uiagent(501)>:17422] with description <RBSAssertionDescriptor| "LS launch com.nexy.assistant" ID:398-17422-1518708 target:app<application.com.nexy.assistant.21074037.21074043(501)> attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"LaunchRoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	14:51:00.182518-0500	runningboardd	Assertion 398-17422-1518708 (target:app<application.com.nexy.assistant.21074037.21074043(501)>) will be created as active
default	14:51:00.185749-0500	runningboardd	Checking PreventLaunch: global:0 exPath:/Applications/Nexy.app/Contents/MacOS/Nexy predicates:(null) allow:(null)
default	14:51:00.185779-0500	runningboardd	Creating and launching job for: app<application.com.nexy.assistant.21074037.21074043(501)>
default	14:51:00.185790-0500	runningboardd	_mutateContextIfNeeded called for com.nexy.assistant
default	14:51:00.185918-0500	runningboardd	app<application.com.nexy.assistant.21074037.21074043(501)>: -[RBPersonaManager personaForIdentity:context:personaUID:personaUniqueString:] required 0.000000 ms (wallclock); resolved to {4294967295, (null)}
default	14:51:00.184818-0500	dmd	Received xpc stream event (distributed notification matching) with name: com.apple.LaunchServices.applicationRegistered user info: {
    CFBundleDisplayName = Nexy;
    bundleIDs =     (
        "com.nexy.assistant"
    );
    isPlaceholder = 0;
}
default	14:51:00.221148-0500	runningboardd	[app<application.com.nexy.assistant.21074037.21074043(501)>:39688] is not RunningBoard jetsam managed.
default	14:51:00.221162-0500	runningboardd	[app<application.com.nexy.assistant.21074037.21074043(501)>:39688] This process will not be managed.
default	14:51:00.221172-0500	runningboardd	Now tracking process: [app<application.com.nexy.assistant.21074037.21074043(501)>:39688]
default	14:51:00.221332-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.21074037.21074043(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	14:51:00.221880-0500	gamepolicyd	Hit the server for a process handle 8c0137200009b08 that resolved to: [app<application.com.nexy.assistant.21074037.21074043(501)>:39688]
default	14:51:00.221916-0500	gamepolicyd	Received state update for 39688 (app<application.com.nexy.assistant.21074037.21074043(501)>, running-active-NotVisible
default	14:51:00.224320-0500	runningboardd	Using default underlying assertion for app: [app<application.com.nexy.assistant.21074037.21074043(501)>:39688]
default	14:51:00.224386-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.21074037.21074043(501)>:39688] from originator [app<application.com.nexy.assistant.21074037.21074043(501)>:39688] with description <RBSAssertionDescriptor| "RB Underlying Assertion" ID:398-398-1518709 target:39688 attributes:[
	<RBSDomainAttribute| domain:"com.apple.underlying" name:"defaultUnderlyingAppAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	14:51:00.224498-0500	runningboardd	Assertion 398-398-1518709 (target:[app<application.com.nexy.assistant.21074037.21074043(501)>:39688]) will be created as active
default	14:51:00.224673-0500	runningboardd	[app<application.com.nexy.assistant.21074037.21074043(501)>:39688] Ignoring jetsam update because this process is not memory-managed
default	14:51:00.224693-0500	runningboardd	[app<application.com.nexy.assistant.21074037.21074043(501)>:39688] Ignoring suspend because this process is not lifecycle managed
default	14:51:00.224710-0500	runningboardd	[app<application.com.nexy.assistant.21074037.21074043(501)>:39688] Set darwin role to: UserInteractive
default	14:51:00.224725-0500	runningboardd	[app<application.com.nexy.assistant.21074037.21074043(501)>:39688] Ignoring GPU update because this process is not GPU managed
default	14:51:00.224752-0500	runningboardd	[app<application.com.nexy.assistant.21074037.21074043(501)>:39688] Ignoring memory limit update because this process is not memory-managed
default	14:51:00.224785-0500	runningboardd	[app<application.com.nexy.assistant.21074037.21074043(501)>:39688] reported to RB as running
default	14:51:00.226073-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.21074037.21074043(501)>:39688] from originator [osservice<com.apple.coreservices.launchservicesd>:363] with description <RBSAssertionDescriptor| "uielement:39688" ID:398-363-1518710 target:39688 attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"RoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	14:51:00.226216-0500	runningboardd	Assertion 398-363-1518710 (target:[app<application.com.nexy.assistant.21074037.21074043(501)>:39688]) will be created as active
default	14:51:00.226125-0500	CoreServicesUIAgent	LAUNCH: 0x0-0x1a7aa79 com.nexy.assistant starting stopped process.
default	14:51:00.226697-0500	loginwindow	-[Application updateInformation] | Got App URL: file:///Applications/Nexy.app/
default	14:51:00.226871-0500	loginwindow	-[ApplicationManager checkInAppContext:eventData:] | ApplicationManager: Checked in app : Nexy
default	14:51:00.229099-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.21074037.21074043(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	14:51:00.229211-0500	runningboardd	[app<application.com.nexy.assistant.21074037.21074043(501)>:39688] Ignoring jetsam update because this process is not memory-managed
default	14:51:00.229223-0500	runningboardd	[app<application.com.nexy.assistant.21074037.21074043(501)>:39688] Ignoring suspend because this process is not lifecycle managed
default	14:51:00.229233-0500	runningboardd	[app<application.com.nexy.assistant.21074037.21074043(501)>:39688] Ignoring GPU update because this process is not GPU managed
default	14:51:00.229250-0500	runningboardd	[app<application.com.nexy.assistant.21074037.21074043(501)>:39688] Ignoring memory limit update because this process is not memory-managed
default	14:51:00.229315-0500	runningboardd	Successfully acquired underlying assertion for [app<application.com.nexy.assistant.21074037.21074043(501)>:39688]
default	14:51:00.229341-0500	runningboardd	Invalidating assertion 398-17422-1518708 (target:app<application.com.nexy.assistant.21074037.21074043(501)>) from originator [osservice<com.apple.coreservices.uiagent(501)>:17422]
default	14:51:00.229378-0500	runningboardd	[app<application.com.nexy.assistant.21074037.21074043(501)>:39688] Ignoring jetsam update because this process is not memory-managed
default	14:51:00.229391-0500	runningboardd	[app<application.com.nexy.assistant.21074037.21074043(501)>:39688] Ignoring suspend because this process is not lifecycle managed
default	14:51:00.229490-0500	gamepolicyd	Received state update for 39688 (app<application.com.nexy.assistant.21074037.21074043(501)>, running-active-NotVisible
default	14:51:00.229401-0500	runningboardd	[app<application.com.nexy.assistant.21074037.21074043(501)>:39688] Ignoring GPU update because this process is not GPU managed
default	14:51:00.229520-0500	runningboardd	[app<application.com.nexy.assistant.21074037.21074043(501)>:39688] Ignoring memory limit update because this process is not memory-managed
default	14:51:00.232414-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.21074037.21074043(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	14:51:00.332405-0500	runningboardd	[app<application.com.nexy.assistant.21074037.21074043(501)>:39688] Ignoring jetsam update because this process is not memory-managed
default	14:51:00.332420-0500	runningboardd	[app<application.com.nexy.assistant.21074037.21074043(501)>:39688] Ignoring suspend because this process is not lifecycle managed
default	14:51:00.332431-0500	runningboardd	[app<application.com.nexy.assistant.21074037.21074043(501)>:39688] Ignoring GPU update because this process is not GPU managed
default	14:51:00.332468-0500	runningboardd	[app<application.com.nexy.assistant.21074037.21074043(501)>:39688] Ignoring memory limit update because this process is not memory-managed
default	14:51:00.332818-0500	gamepolicyd	Received state update for 39688 (app<application.com.nexy.assistant.21074037.21074043(501)>, running-active-NotVisible
default	14:51:00.336250-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.21074037.21074043(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	14:51:00.336786-0500	gamepolicyd	Received state update for 39688 (app<application.com.nexy.assistant.21074037.21074043(501)>, running-active-NotVisible
default	14:51:00.360603-0500	syspolicyd	GK evaluateScanResult: 3, PST: (path: a2cffff67b96be6e), (team: 5NKLL2CLB9), (id: com.nexy.assistant), (bundle_id: (null)), 0, 0, 1, 0, 9, 4, 1
default	14:51:00.362821-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=511.177, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=39688, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.syspolicyd, pid=511, auid=0, euid=0, binary_path=/usr/libexec/syspolicyd}, },
default	14:51:00.368928-0500	tccd	AUTHREQ_SUBJECT: msgID=511.177, subject=com.nexy.assistant,
default	14:51:00.369613-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d115e00 at /Applications/Nexy.app
default	14:51:00.386008-0500	kernel	Nexy[39688] triggered unnest of range 0x1f6000000->0x1f8000000 of DYLD shared region in VM map 0x8251adb5114c2ac1. While not abnormal for debuggers, this increases system memory footprint until the target exits.
error	14:51:00.843584-0500	Nexy	dlsym cannot find symbol NSMakeRect in CFBundle 0x101b61c60 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	14:51:00.843851-0500	Nexy	dlsym cannot find symbol NSMakePoint in CFBundle 0x101b61c60 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	14:51:00.844070-0500	Nexy	dlsym cannot find symbol NSMakeSize in CFBundle 0x101b61c60 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	14:51:00.844279-0500	Nexy	dlsym cannot find symbol NSMakeRange in CFBundle 0x101b61c60 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
default	14:51:00.845628-0500	Nexy	[0x101b4dc80] activating connection: mach=true listener=false peer=false name=com.apple.coreservices.launchservicesd
default	14:51:00.846426-0500	Nexy	[0x768460000] activating connection: mach=true listener=false peer=false name=com.apple.analyticsd
default	14:51:00.846792-0500	Nexy	[0x768460140] activating connection: mach=true listener=false peer=false name=com.apple.pasteboard.1
default	14:51:00.847243-0500	Nexy	[0x768460280] activating connection: mach=true listener=false peer=false name=com.apple.distributed_notifications@Uv3
default	14:51:00.847953-0500	Nexy	Received configuration update from daemon (initial)
default	14:51:00.849390-0500	Nexy	void _NSDisableAutomaticTerminationAndLog(NSString *) No windows open yet
default	14:51:00.849771-0500	Nexy	[0x7684603c0] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	14:51:00.850516-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=39688.1, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=39688, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	14:51:00.852574-0500	tccd	AUTHREQ_SUBJECT: msgID=39688.1, subject=com.nexy.assistant,
default	14:51:00.853363-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d115e00 at /Applications/Nexy.app
default	14:51:00.867360-0500	Nexy	[0x7684603c0] invalidated after the last release of the connection object
default	14:51:00.868813-0500	Nexy	server port 0x0000360f, session port 0x0000360f
default	14:51:00.869895-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=393.17732, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=39688, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=393, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	14:51:00.869927-0500	tccd	requestor: TCCDProcess: identifier=com.apple.WindowServer, pid=393, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=39688, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	14:51:00.871052-0500	tccd	AUTHREQ_SUBJECT: msgID=393.17732, subject=com.nexy.assistant,
default	14:51:00.871860-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d115e00 at /Applications/Nexy.app
default	14:51:00.888714-0500	Nexy	New connection 0x19b46f main
default	14:51:00.891186-0500	Nexy	CHECKIN: pid=39688
default	14:51:00.897844-0500	launchservicesd	CHECKIN:0x0-0x1a7aa79 39688 com.nexy.assistant
default	14:51:00.898197-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.21074037.21074043(501)>:39688] from originator [osservice<com.apple.coreservices.launchservicesd>:363] with description <RBSAssertionDescriptor| "uielement:39688" ID:398-363-1518711 target:39688 attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"RoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	14:51:00.898355-0500	runningboardd	Assertion 398-363-1518711 (target:[app<application.com.nexy.assistant.21074037.21074043(501)>:39688]) will be created as active
default	14:51:00.898972-0500	runningboardd	Invalidating assertion 398-363-1518710 (target:[app<application.com.nexy.assistant.21074037.21074043(501)>:39688]) from originator [osservice<com.apple.coreservices.launchservicesd>:363]
default	14:51:00.897945-0500	Nexy	CHECKEDIN: pid=39688 asn=0x0-0x1a7aa79 foreground=0
default	14:51:00.898253-0500	Nexy	[0x7684603c0] activating connection: mach=false listener=true peer=false name=(anonymous)
default	14:51:00.899249-0500	loginwindow	-[Application updateInformation] | Got App URL: file:///Applications/Nexy.app/
default	14:51:00.898262-0500	Nexy	[0x7684603c0] Connection returned listener port: 0x4d03
default	14:51:00.899401-0500	loginwindow	-[ApplicationManager checkInAppContext:eventData:] | ApplicationManager: Checked in app : Nexy
default	14:51:00.898498-0500	Nexy	[0x768470300] activating connection: mach=false listener=false peer=true name=com.apple.xpc.anonymous.0x7684603c0.peer[363].0x768470300
default	14:51:00.903929-0500	Nexy	FRONTLOGGING: version 1
default	14:51:00.903937-0500	Nexy	Registered, pid=39688 ASN=0x0,0x1a7aa79
default	14:51:00.904236-0500	WindowServer	19b46f[CreateApplication]: Process creation: 0x0-0x1a7aa79 (Nexy) connectionID: 19B46F pid: 39688 in session 0x101
default	14:51:00.904668-0500	Nexy	[0x768460500] activating connection: mach=true listener=false peer=false name=com.apple.lsd.mapdb
default	14:51:00.905245-0500	Nexy	[0x7684603c0] Connection returned listener port: 0x4d03
default	14:51:00.905667-0500	Nexy	BringForward: pid=39688 asn=0x0-0x1a7aa79 bringForward=0 foreground=0 uiElement=1 launchedByLS=1 modifiersCount=1 allDisabled=0
default	14:51:00.905692-0500	Nexy	BringFrontModifier: pid=39688 asn=0x0-0x1a7aa79 Modifier 0 hideAfter=0 hideOthers=0 dontMakeFrontmost=0 mouseDown=0/0 seed=0/0
default	14:51:00.906341-0500	Nexy	Current system appearance, (HLTB: 1), (SLS: 0)
default	14:51:00.907869-0500	Nexy	No persisted cache on this platform.
default	14:51:00.909302-0500	Nexy	Current system appearance, (HLTB: 1), (SLS: 0)
default	14:51:00.909838-0500	Nexy	Post-registration system appearance: (HLTB: 1)
default	14:51:00.911686-0500	Nexy	FBSWorkspace: endpoint monitoring is disabled.
default	14:51:00.911699-0500	Nexy	FBSWorkspace: default shell endpoint is disabled.
default	14:51:00.911751-0500	Nexy	Initializing connection
default	14:51:00.911796-0500	Nexy	Removing all cached process handles
default	14:51:00.911813-0500	Nexy	Sending handshake request attempt #1 to server
default	14:51:00.911820-0500	Nexy	Creating connection to com.apple.runningboard
default	14:51:00.911828-0500	Nexy	[0x768460640] activating connection: mach=true listener=false peer=false name=com.apple.runningboard
default	14:51:00.912231-0500	Nexy	[0x7684603c0] Connection returned listener port: 0x4d03
default	14:51:00.912352-0500	runningboardd	Setting client for [app<application.com.nexy.assistant.21074037.21074043(501)>:39688] as ready
default	14:51:00.913078-0500	distnoted	register name: com.apple.xctest.FakeForceTouchDevice object: com.nexy.assistant token: 1e0000001d pid: 39688
default	14:51:00.913129-0500	Nexy	Handshake succeeded
default	14:51:00.913147-0500	Nexy	Identity resolved as app<application.com.nexy.assistant.21074037.21074043(501)>
default	14:51:00.920114-0500	Nexy	[0x7684603c0] Connection returned listener port: 0x4d03
default	14:51:00.923754-0500	Nexy	Created a new Process Instance Registry XPC connection (inactive)
default	14:51:00.923778-0500	Nexy	[0x768460780] activating connection: mach=true listener=false peer=false name=com.apple.linkd.autoShortcut
default	14:51:00.923908-0500	Nexy	Activated connection to com.apple.linkd.autoShortcut (ApplicationService)
default	14:51:00.923953-0500	Nexy	[0x768460a00] activating connection: mach=false listener=true peer=false name=(anonymous)
default	14:51:00.926320-0500	Nexy	[0x768460a00] Connection returned listener port: 0x6b03
default	14:51:00.927246-0500	Nexy	Registered process with identifier 39688-2685721
default	14:51:02.189064-0500	Nexy	Registered notify signal com.apple.caulk.alloc.rtdump (0)
default	14:51:02.191930-0500	Nexy	System_Input_Processing_Notification_Handler.mm:456   System_Input_Processing_Notification_Handler::is_vi_available(): Voice isolation DSP is available for client with bundle id com.nexy.assistant (AVFoundation is available, application is not in client deny list, application is not FaceTime variant)
default	14:51:02.195174-0500	Nexy	[0x768460b40] activating connection: mach=true listener=false peer=false name=com.apple.cmio.registerassistantservice.system-extensions
fault	14:51:02.198282-0500	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.21074037.21074043 AUID=501> and <type=Application identifier=application.com.nexy.assistant.21074037.21074043>
default	14:51:02.203365-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOInitializeListenersForBundleID: for <private> -> <private>
default	14:51:02.206453-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> vpio_preferenceChangedListener: new value ((null)) for key AUVoiceIOClients/com-nexy-assistant/AUVoiceIOChatFlavor, translatedBundleID com.nexy.assistant, bundleIDs {(
    "com.nexy.assistant"
)}
default	14:51:02.206614-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> vpio_preferenceChangedListener: new value ((null)) for key AUVoiceIOClients/com-nexy-assistant/AUVoiceIOIsAutoChatFlavorEnabled, translatedBundleID com.nexy.assistant, bundleIDs {(
    "com.nexy.assistant"
)}
default	14:51:02.206768-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetSupportedChatFlavorsForBundleID: <private>-><private> get supported chat flavors: <private>
default	14:51:02.206779-0500	Nexy	            HALSystem.cpp:134    Enabling HAL Voice Isolation support
default	14:51:02.206810-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetHiddenChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	14:51:02.206945-0500	Nexy	[0x768460c80] activating connection: mach=true listener=false peer=false name=com.apple.tccd
default	14:51:02.207350-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOHiddenChatFlavors newValue: (
    1
)
default	14:51:02.208134-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=39688.2, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=39688, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	14:51:02.215442-0500	tccd	AUTHREQ_SUBJECT: msgID=39688.2, subject=com.nexy.assistant,
default	14:51:02.216063-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc37138c00 at /Applications/Nexy.app
default	14:51:02.228169-0500	Nexy	[0x768460c80] invalidated after the last release of the connection object
default	14:51:02.228225-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetSupportedChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	14:51:02.230911-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOSupportedChatFlavors newValue: (
)
default	14:51:02.232026-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.11831, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=39688, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	14:51:02.232949-0500	tccd	AUTHREQ_SUBJECT: msgID=401.11831, subject=com.nexy.assistant,
default	14:51:02.233510-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc37138c00 at /Applications/Nexy.app
error	14:51:02.250488-0500	tccd	Request message contains a target_token to accessing_process (TCCDProcess: identifier=com.nexy.assistant, pid=39688, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy) but TCCDProcess: identifier=com.apple.audio.coreaudiod, pid=401, auid=202, euid=202, binary_path=/usr/sbin/coreaudiod is not a TCC manager for service: kTCCServiceScreenCapture.
default	14:51:02.251368-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.11833, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=39688, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	14:51:02.252475-0500	tccd	AUTHREQ_SUBJECT: msgID=401.11833, subject=com.nexy.assistant,
default	14:51:02.253330-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc37138c00 at /Applications/Nexy.app
default	14:51:02.268105-0500	Nexy	  HALPlugInManagement.cpp:440    HALPlugInManagement::RegisterPlugIns: skipping in-process plug-ins
error	14:51:02.268152-0500	Nexy	AddInstanceForFactory: No factory registered for id <CFUUID 0x768aa2480> F8BB1C28-BAE8-11D6-9C31-00039315CD46
default	14:51:02.287981-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetPreferredChatFlavorForBundleID: <private>-><private> get value: 0
default	14:51:02.562299-0500	Nexy	NotifyToken::RegisterDispatch(user.uid.501.com.apple.LaunchServices.database) fired for session key <private>
default	14:51:04.782870-0500	kernel	SK[7]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 940703BA-F6E9-49A9-8955-85949D0DBB8C flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.58147,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0xbff72696 tp_proto=0x06"
default	14:51:04.782991-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:58147<-><IPv4-redacted>:53] interface: en0 (skipped: 6843)
so_gencnt: 6102088 t_state: SYN_SENT process: Nexy:39688 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xb7059a4c
default	14:51:04.803575-0500	kernel	tcp connected: [<IPv4-redacted>:58147<-><IPv4-redacted>:53] interface: en0 (skipped: 6843)
so_gencnt: 6102088 t_state: ESTABLISHED process: Nexy:39688 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xb7059a4c
default	14:51:04.803884-0500	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:58147<-><IPv4-redacted>:53] interface: en0 (skipped: 6843)
so_gencnt: 6102088 t_state: FIN_WAIT_1 process: Nexy:39688 Duration: 0.021 sec Conn_Time: 0.021 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 21.000 ms rttvar: 10.500 ms base rtt: 21 ms so_error: 0 svc/tc: 0 flow: 0xb7059a4c
default	14:51:04.803894-0500	kernel	tcp_connection_summary [<IPv4-redacted>:58147<-><IPv4-redacted>:53] interface: en0 (skipped: 6843)
so_gencnt: 6102088 t_state: FIN_WAIT_1 process: Nexy:39688 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	14:51:04.831233-0500	Nexy	[0x768460c80] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioComponentRegistrar
default	14:51:04.844377-0500	Nexy	                AUHAL.cpp:420   AUHAL: (0x76a0df140) Selecting device 71 from constructor
default	14:51:04.844388-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0x76a0df140)
default	14:51:04.844393-0500	Nexy	                AUHAL.cpp:676   SelectDevice: (0x76a0df140) not already running
default	14:51:04.844398-0500	Nexy	                AUHAL.cpp:752   SelectDevice: (0x76a0df140) nothing to teardown
default	14:51:04.844402-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0x76a0df140) connecting device 71
default	14:51:04.844492-0500	Nexy	                AUHAL.cpp:3413  IsDeviceUsable: (0x76a0df140) Device ID: 71 (Input:No | Output:Yes): true
default	14:51:04.844824-0500	Nexy	                AUHAL.cpp:769   SelectDevice: (0x76a0df140) created ioproc 0xa for device 71
default	14:51:04.844928-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x76a0df140) adding 7 device listeners to device 71
default	14:51:04.845089-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x76a0df140) adding 0 device delegate listeners to device 71
default	14:51:04.845097-0500	Nexy	                AUHAL.cpp:1581  UpdateStreamFormats: -> (0x76a0df140)
default	14:51:04.845160-0500	Nexy	                AUHAL.cpp:1677  UpdateStreamFormats: 
  output stream 0 [0x48]:  2 ch,  48000 Hz, Float32, interleaved
default	14:51:04.845168-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 1 output streams; not all mono
default	14:51:04.845174-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	14:51:04.845180-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 0 input streams; not all mono
default	14:51:04.845189-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	14:51:04.845274-0500	Nexy	                AUHAL.cpp:1771  UpdateStreamFormats: AUHAL(0x76a0df140) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	14:51:04.845283-0500	Nexy	                AUHAL.cpp:1777  UpdateStreamFormats: AUHAL(0x76a0df140) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	14:51:04.845288-0500	Nexy	                AUHAL.cpp:1787  UpdateStreamFormats: <-
default	14:51:04.845293-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x76a0df140) removing 0 device listeners from device 0
default	14:51:04.845298-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x76a0df140) removing 0 device delegate listeners from device 0
default	14:51:04.845307-0500	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0x76a0df140)
default	14:51:04.845324-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Output stream enables: Stream 0 is DISABLED
default	14:51:04.845422-0500	Nexy	                AUHAL.cpp:2298  SetProperty: (0x76a0df140) caller requesting device change from 71 to 78
default	14:51:04.845431-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0x76a0df140)
default	14:51:04.845437-0500	Nexy	                AUHAL.cpp:676   SelectDevice: (0x76a0df140) not already running
default	14:51:04.845442-0500	Nexy	                AUHAL.cpp:682   SelectDevice: (0x76a0df140) disconnecting device 71
default	14:51:04.845446-0500	Nexy	                AUHAL.cpp:746   SelectDevice: (0x76a0df140) destroying ioproc 0xa for device 71
default	14:51:04.845768-0500	Nexy	  AVAudioSession_MacOS.mm:1021  initForMacOS
default	14:51:04.846839-0500	Nexy	[0x768460f00] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioSession
default	14:51:04.847753-0500	audiomxd	  ServerSessionManager.mm:315   { "action":"create_session", "session":{"ID":"0x1ef2bf","name":"Nexy(39688)"}, "details":{"PID":39688,"session_type":"Primary"} }
default	14:51:04.847836-0500	audiomxd	AudioApplicationInfoImpl.mm:250   Setting initial isRecording state: 0 for newly-created AudioApp
	app: {"name":"[implicit] Nexy","pid":39688}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1ef2bf, sessionType: 'prim', isRecording: false }, 
]
default	14:51:04.848541-0500	audiomxd	  ServerSessionManager.mm:1317  Start process monitoring, pid = 39688, name = Nexy
default	14:51:04.848773-0500	Nexy	    SessionCore_Create.mm:99    Created session 0x768acd280 with ID: 0x1ef2bf
default	14:51:04.849890-0500	Nexy	[0x768461040] activating connection: mach=true listener=false peer=false name=com.apple.audioanalyticsd
error	14:51:04.850308-0500	Nexy	Reporter disconnected. { function=sendMessage, reporterID=170458662043649 }
default	14:51:04.850325-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped Unknown {BuiltInSpeakerDevice, 0xa}
default	14:51:04.850377-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	14:51:04.850481-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0x76a0df140) connecting device 78
default	14:51:04.850570-0500	Nexy	                AUHAL.cpp:3413  IsDeviceUsable: (0x76a0df140) Device ID: 78 (Input:Yes | Output:No): true
default	14:51:04.851983-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.11834, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=39688, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	14:51:04.854032-0500	tccd	AUTHREQ_SUBJECT: msgID=401.11834, subject=com.nexy.assistant,
default	14:51:04.854705-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc37138c00 at /Applications/Nexy.app
default	14:51:04.867402-0500	tccd	AUTHREQ_PROMPTING: msgID=401.11834, service=kTCCServiceMicrophone, subject=Sub:{com.nexy.assistant}Resp:{TCCDProcess: identifier=com.nexy.assistant, pid=39688, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy},
default	14:51:05.189671-0500	runningboardd	Assertion did invalidate due to timeout: 398-398-1518709 (target:[app<application.com.nexy.assistant.21074037.21074043(501)>:39688])
default	14:51:05.390199-0500	runningboardd	[app<application.com.nexy.assistant.21074037.21074043(501)>:39688] Ignoring jetsam update because this process is not memory-managed
default	14:51:05.390216-0500	runningboardd	[app<application.com.nexy.assistant.21074037.21074043(501)>:39688] Ignoring suspend because this process is not lifecycle managed
default	14:51:05.390225-0500	runningboardd	[app<application.com.nexy.assistant.21074037.21074043(501)>:39688] Ignoring GPU update because this process is not GPU managed
default	14:51:05.390244-0500	runningboardd	[app<application.com.nexy.assistant.21074037.21074043(501)>:39688] Ignoring memory limit update because this process is not memory-managed
default	14:51:05.395088-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.21074037.21074043(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	14:51:05.395735-0500	gamepolicyd	Received state update for 39688 (app<application.com.nexy.assistant.21074037.21074043(501)>, running-active-NotVisible
default	14:51:08.586180-0500	tccd	Publishing <TCCDEvent: type=Create, service=kTCCServiceMicrophone, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 3 subscribers: {
    471 = "<TCCDEventSubscriber: token=471, state=Passed, csid=com.apple.chronod>";
    37 = "<TCCDEventSubscriber: token=37, state=Initial, csid=(null)>";
    476 = "<TCCDEventSubscriber: token=476, state=Passed, csid=com.apple.photolibraryd>";
}
default	14:51:08.587306-0500	Nexy	                AUHAL.cpp:769   SelectDevice: (0x76a0df140) created ioproc 0xa for device 78
default	14:51:08.587630-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x76a0df140) adding 7 device listeners to device 78
default	14:51:08.588149-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x76a0df140) adding 0 device delegate listeners to device 78
default	14:51:08.588165-0500	Nexy	                AUHAL.cpp:1581  UpdateStreamFormats: -> (0x76a0df140)
default	14:51:08.588187-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 0 output streams; not all mono
default	14:51:08.588222-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Output render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	14:51:08.588501-0500	Nexy	                AUHAL.cpp:1677  UpdateStreamFormats: 
  input stream 0 [0x4f]:  1 ch,  48000 Hz, Float32
default	14:51:08.588514-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 1 input streams; all mono
default	14:51:08.588521-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Input render format:  1 ch,  48000 Hz, Float32
default	14:51:08.588651-0500	Nexy	                AUHAL.cpp:1771  UpdateStreamFormats: AUHAL(0x76a0df140) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	14:51:08.588686-0500	Nexy	                AUHAL.cpp:1777  UpdateStreamFormats: AUHAL(0x76a0df140) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	14:51:08.588696-0500	Nexy	                AUHAL.cpp:1787  UpdateStreamFormats: <-
default	14:51:08.588713-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x76a0df140) removing 7 device listeners from device 71
default	14:51:08.587841-0500	chronod	[appAuth:com.nexy.assistant] tcc authorization(s) changed
default	14:51:08.588956-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x76a0df140) removing 0 device delegate listeners from device 71
default	14:51:08.588967-0500	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0x76a0df140)
default	14:51:08.589997-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	14:51:08.591871-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.11835, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=39688, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	14:51:08.593262-0500	tccd	AUTHREQ_SUBJECT: msgID=401.11835, subject=com.nexy.assistant,
default	14:51:08.594213-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc37138c00 at /Applications/Nexy.app
default	14:51:08.613430-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	14:51:08.614636-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.11836, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=39688, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	14:51:08.615799-0500	tccd	AUTHREQ_SUBJECT: msgID=401.11836, subject=com.nexy.assistant,
default	14:51:08.617335-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc37138c00 at /Applications/Nexy.app
default	14:51:08.632558-0500	Nexy	Registered notify signal com.apple.caulk.alloc.audiodump (0)
default	14:51:08.634608-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.11837, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=39688, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	14:51:08.635584-0500	tccd	AUTHREQ_SUBJECT: msgID=401.11837, subject=com.nexy.assistant,
default	14:51:08.636168-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc37138c00 at /Applications/Nexy.app
default	14:51:08.651103-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetPreferredChatFlavorForBundleID: <private>-><private> get value: 0
default	14:51:08.651734-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetSupportedChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	14:51:08.656510-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.21074037.21074043(501)>:39688] from originator [osservice<com.apple.powerd>:334] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:398-334-1518718 target:39688 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	14:51:08.656697-0500	runningboardd	Assertion 398-334-1518718 (target:[app<application.com.nexy.assistant.21074037.21074043(501)>:39688]) will be created as active
default	14:51:08.658070-0500	runningboardd	[app<application.com.nexy.assistant.21074037.21074043(501)>:39688] Ignoring jetsam update because this process is not memory-managed
default	14:51:08.658288-0500	runningboardd	[app<application.com.nexy.assistant.21074037.21074043(501)>:39688] Ignoring suspend because this process is not lifecycle managed
default	14:51:08.658402-0500	runningboardd	[app<application.com.nexy.assistant.21074037.21074043(501)>:39688] Ignoring GPU update because this process is not GPU managed
default	14:51:08.658682-0500	runningboardd	[app<application.com.nexy.assistant.21074037.21074043(501)>:39688] Ignoring memory limit update because this process is not memory-managed
default	14:51:08.659050-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOSupportedChatFlavors newValue: (
    0,
    2
)
default	14:51:08.667974-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.21074037.21074043(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	14:51:08.669867-0500	gamepolicyd	Received state update for 39688 (app<application.com.nexy.assistant.21074037.21074043(501)>, running-active-NotVisible
default	14:51:08.679316-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Input {BuiltInMicrophoneDevice, 0xa}
default	14:51:08.681787-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ef2bf","name":"Nexy(39688)"}, "details":{"deviceUIDs":[],"implicit_category":"Record","input_running":true,"output_running":false} }
default	14:51:08.682049-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 704, PID = 39688, Name = sid:0x1ef2bf, Nexy(39688), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	14:51:08.682178-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 704, PID = 39688, Name = sid:0x1ef2bf, Nexy(39688), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	14:51:08.682296-0500	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1ef2bf, Nexy(39688), 'prim'', AudioCategory changed to 'Record_WithBluetooth'
default	14:51:08.682367-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 704, PID = 39688, Name = sid:0x1ef2bf, Nexy(39688), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	14:51:08.682380-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:51:08.682396-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 704, PID = 39688, Name = sid:0x1ef2bf, Nexy(39688), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	14:51:08.682449-0500	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 704, PID = 39688, Name = sid:0x1ef2bf, Nexy(39688), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> is going active
default	14:51:08.682461-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1ef2bf, Nexy(39688), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 704 starting recording
default	14:51:08.682523-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:51:08.682765-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:51:08.682921-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:51:08.682962-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:51:08.682988-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 704, PID = 39688, Name = sid:0x1ef2bf, Nexy(39688), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	14:51:08.683022-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 704, PID = 39688, Name = sid:0x1ef2bf, Nexy(39688), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	14:51:08.683054-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1ef2bf, Nexy(39688), 'prim'', displayID:'com.nexy.assistant'}
default	14:51:08.683125-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:51:08.683129-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	14:51:08.683161-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [1, 0]. BT device UIDS: {(
)}
default	14:51:08.683181-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	14:51:08.683247-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	14:51:08.683291-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	14:51:08.683320-0500	audioaccessoryd	AudioStateChanged: Added audio session app com.nexy.assistant NULL -> 200 count 1
default	14:51:08.683340-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
error	14:51:08.683363-0500	audioaccessoryd	Updating local audio category 100 -> 200 app com.nexy.assistant
default	14:51:08.683428-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
fault	14:51:08.686578-0500	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.21074037.21074043 AUID=501> and <type=Application identifier=application.com.nexy.assistant.21074037.21074043>
fault	14:51:08.688807-0500	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.21074037.21074043 AUID=501> and <type=Application identifier=application.com.nexy.assistant.21074037.21074043>
default	14:51:08.716300-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	14:51:08.716427-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	14:51:08.716484-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	14:51:08.717964-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:51:08.717988-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:51:08.718002-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	14:51:08.718008-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:51:08.718015-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	14:51:08.718024-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	14:51:08.718123-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	14:51:08.719309-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:51:08.719317-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:51:08.719331-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	14:51:08.719341-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:51:08.719347-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	14:51:08.719353-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	14:51:08.719424-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	14:51:08.721946-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:51:08.721961-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:51:08.721973-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	14:51:08.721982-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:51:08.721987-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	14:51:08.721995-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	14:51:08.722722-0500	ControlCenter	Navigating to new application [com.nexy.assistant]
default	14:51:08.798521-0500	audioaccessoryd	AudioStateSnapshot: Route:Speaker App com.nexy.assistant, Score 200, Remote -1NumofApp 1
default	14:51:09.661989-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	14:51:09.670166-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {BuiltInMicrophoneDevice, 0xa}
default	14:51:09.670948-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ef2bf","name":"Nexy(39688)"}, "details":{"deviceUIDs":[],"implicit_category":"","input_running":false,"output_running":false} }
default	14:51:09.670945-0500	runningboardd	Invalidating assertion 398-334-1518718 (target:[app<application.com.nexy.assistant.21074037.21074043(501)>:39688]) from originator [osservice<com.apple.powerd>:334]
default	14:51:09.671188-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 704, PID = 39688, Name = sid:0x1ef2bf, Nexy(39688), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	14:51:09.671293-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 704, PID = 39688, Name = sid:0x1ef2bf, Nexy(39688), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	14:51:09.671359-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1ef2bf, Nexy(39688), 'prim'', displayID:'com.nexy.assistant'}
default	14:51:09.671778-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	14:51:09.671485-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	14:51:09.671870-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	14:51:09.671534-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1ef2bf, Nexy(39688), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 704 stopping recording
default	14:51:09.671910-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	14:51:09.671663-0500	audiomxd	-MXCoreSession- -[MXCoreSession endInterruption:]: Session <ID: 704, PID = 39688, Name = sid:0x1ef2bf, Nexy(39688), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> is going inactive
default	14:51:09.672003-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	14:51:09.671803-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 704, PID = 39688, Name = sid:0x1ef2bf, Nexy(39688), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	14:51:09.671962-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 704, PID = 39688, Name = sid:0x1ef2bf, Nexy(39688), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	14:51:09.672472-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 0]. BT device UIDS: {(
)}
default	14:51:09.672499-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	14:51:09.672418-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:51:09.672629-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:51:09.672678-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:51:09.672703-0500	audioaccessoryd	AudioStateChanged: Removed audio session app com.nexy.assistant 201 count 0
default	14:51:09.686897-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	14:51:09.687972-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:51:09.687989-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:51:09.688005-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	14:51:09.688015-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:51:09.688025-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	14:51:09.688034-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	14:51:09.688175-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	14:51:09.773617-0500	runningboardd	[app<application.com.nexy.assistant.21074037.21074043(501)>:39688] Ignoring jetsam update because this process is not memory-managed
default	14:51:09.773631-0500	runningboardd	[app<application.com.nexy.assistant.21074037.21074043(501)>:39688] Ignoring suspend because this process is not lifecycle managed
default	14:51:09.773641-0500	runningboardd	[app<application.com.nexy.assistant.21074037.21074043(501)>:39688] Ignoring GPU update because this process is not GPU managed
default	14:51:09.773683-0500	runningboardd	[app<application.com.nexy.assistant.21074037.21074043(501)>:39688] Ignoring memory limit update because this process is not memory-managed
default	14:51:09.775075-0500	Nexy	                AUHAL.cpp:473   ~AUHAL: (0x76a0df140) Selecting device 0 from destructor
default	14:51:09.775094-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0x76a0df140)
default	14:51:09.775104-0500	Nexy	                AUHAL.cpp:676   SelectDevice: (0x76a0df140) not already running
default	14:51:09.775109-0500	Nexy	                AUHAL.cpp:682   SelectDevice: (0x76a0df140) disconnecting device 78
default	14:51:09.775115-0500	Nexy	                AUHAL.cpp:746   SelectDevice: (0x76a0df140) destroying ioproc 0xa for device 78
default	14:51:09.775156-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {BuiltInMicrophoneDevice, 0xa}
default	14:51:09.775187-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	14:51:09.775418-0500	Nexy	                AUHAL.cpp:848   SelectDevice: (0x76a0df140) nothing to setup
default	14:51:09.775429-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x76a0df140) adding 0 device listeners to device 0
default	14:51:09.775435-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x76a0df140) adding 0 device delegate listeners to device 0
default	14:51:09.775443-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x76a0df140) removing 7 device listeners from device 78
default	14:51:09.775686-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x76a0df140) removing 0 device delegate listeners from device 78
default	14:51:09.775703-0500	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0x76a0df140)
default	14:51:09.777503-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.21074037.21074043(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	14:51:09.778264-0500	gamepolicyd	Received state update for 39688 (app<application.com.nexy.assistant.21074037.21074043(501)>, running-active-NotVisible
default	14:51:10.041780-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=39695.1, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=39688, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.osascript, pid=39695, auid=501, euid=501, binary_path=/usr/bin/osascript}, },
default	14:51:10.046160-0500	tccd	AUTHREQ_SUBJECT: msgID=39695.1, subject=com.nexy.assistant,
default	14:51:10.048937-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d115e00 at /Applications/Nexy.app
default	14:51:10.065067-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=393.17740, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=39688, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.osascript, pid=39695, auid=501, euid=501, binary_path=/usr/bin/osascript}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=393, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	14:51:10.066163-0500	tccd	AUTHREQ_SUBJECT: msgID=393.17740, subject=com.nexy.assistant,
default	14:51:10.066860-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d115e00 at /Applications/Nexy.app
default	14:51:10.108597-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d115e00 at /Applications/Nexy.app
default	14:51:10.264210-0500	System Events	TCCAccessRequestIndirect: TCCAccessRequestIndirect with pid 39696: target_identity: {
    kTCCCodeIdentityAuditToken = {length = 32, bytes = 0xf5010000 f5010000 14000000 f5010000 ... b7860100 2ffb2800 };
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
default	14:51:10.275298-0500	tccd	target_executable_path_URL: file:///Applications/Nexy.app/Contents/MacOS/Nexy
default	14:51:10.514952-0500	Nexy	[0x768461180] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	14:51:10.515677-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=39688.3, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=39688, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	14:51:10.516882-0500	tccd	AUTHREQ_SUBJECT: msgID=39688.3, subject=com.nexy.assistant,
default	14:51:10.517498-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d115e00 at /Applications/Nexy.app
default	14:51:10.530839-0500	Nexy	[0x768461180] invalidated after the last release of the connection object
default	14:51:10.533941-0500	Nexy	                AUHAL.cpp:420   AUHAL: (0x76a0df140) Selecting device 71 from constructor
default	14:51:10.533951-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0x76a0df140)
default	14:51:10.533957-0500	Nexy	                AUHAL.cpp:676   SelectDevice: (0x76a0df140) not already running
default	14:51:10.533961-0500	Nexy	                AUHAL.cpp:752   SelectDevice: (0x76a0df140) nothing to teardown
default	14:51:10.533965-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0x76a0df140) connecting device 71
default	14:51:10.534073-0500	Nexy	                AUHAL.cpp:3413  IsDeviceUsable: (0x76a0df140) Device ID: 71 (Input:No | Output:Yes): true
default	14:51:10.534226-0500	Nexy	                AUHAL.cpp:769   SelectDevice: (0x76a0df140) created ioproc 0xb for device 71
default	14:51:10.534348-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x76a0df140) adding 7 device listeners to device 71
default	14:51:10.534534-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x76a0df140) adding 0 device delegate listeners to device 71
default	14:51:10.534543-0500	Nexy	                AUHAL.cpp:1581  UpdateStreamFormats: -> (0x76a0df140)
default	14:51:10.534610-0500	Nexy	                AUHAL.cpp:1677  UpdateStreamFormats: 
  output stream 0 [0x48]:  2 ch,  48000 Hz, Float32, interleaved
default	14:51:10.534619-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 1 output streams; not all mono
default	14:51:10.534625-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	14:51:10.534632-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 0 input streams; not all mono
default	14:51:10.534641-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	14:51:10.534729-0500	Nexy	                AUHAL.cpp:1771  UpdateStreamFormats: AUHAL(0x76a0df140) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	14:51:10.534744-0500	Nexy	                AUHAL.cpp:1777  UpdateStreamFormats: AUHAL(0x76a0df140) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	14:51:10.534753-0500	Nexy	                AUHAL.cpp:1787  UpdateStreamFormats: <-
default	14:51:10.534756-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x76a0df140) removing 0 device listeners from device 0
default	14:51:10.534759-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x76a0df140) removing 0 device delegate listeners from device 0
default	14:51:10.534764-0500	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0x76a0df140)
default	14:51:10.534779-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Output stream enables: Stream 0 is DISABLED
default	14:51:10.534852-0500	Nexy	                AUHAL.cpp:2298  SetProperty: (0x76a0df140) caller requesting device change from 71 to 78
default	14:51:10.534859-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0x76a0df140)
default	14:51:10.534863-0500	Nexy	                AUHAL.cpp:676   SelectDevice: (0x76a0df140) not already running
default	14:51:10.534868-0500	Nexy	                AUHAL.cpp:682   SelectDevice: (0x76a0df140) disconnecting device 71
default	14:51:10.534872-0500	Nexy	                AUHAL.cpp:746   SelectDevice: (0x76a0df140) destroying ioproc 0xb for device 71
default	14:51:10.534909-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped Unknown {BuiltInSpeakerDevice, 0xb}
default	14:51:10.534944-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	14:51:10.535018-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0x76a0df140) connecting device 78
default	14:51:10.535094-0500	Nexy	                AUHAL.cpp:3413  IsDeviceUsable: (0x76a0df140) Device ID: 78 (Input:Yes | Output:No): true
default	14:51:10.536314-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.11838, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=39688, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	14:51:10.537353-0500	tccd	AUTHREQ_SUBJECT: msgID=401.11838, subject=com.nexy.assistant,
default	14:51:10.537945-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc37138c00 at /Applications/Nexy.app
default	14:51:10.550621-0500	Nexy	                AUHAL.cpp:769   SelectDevice: (0x76a0df140) created ioproc 0xb for device 78
default	14:51:10.550771-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x76a0df140) adding 7 device listeners to device 78
default	14:51:10.550971-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x76a0df140) adding 0 device delegate listeners to device 78
default	14:51:10.550980-0500	Nexy	                AUHAL.cpp:1581  UpdateStreamFormats: -> (0x76a0df140)
default	14:51:10.550986-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 0 output streams; not all mono
default	14:51:10.550996-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Output render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	14:51:10.551115-0500	Nexy	                AUHAL.cpp:1677  UpdateStreamFormats: 
  input stream 0 [0x4f]:  1 ch,  48000 Hz, Float32
default	14:51:10.551126-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 1 input streams; all mono
default	14:51:10.551132-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Input render format:  1 ch,  48000 Hz, Float32
default	14:51:10.551234-0500	Nexy	                AUHAL.cpp:1771  UpdateStreamFormats: AUHAL(0x76a0df140) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	14:51:10.551249-0500	Nexy	                AUHAL.cpp:1777  UpdateStreamFormats: AUHAL(0x76a0df140) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	14:51:10.551255-0500	Nexy	                AUHAL.cpp:1787  UpdateStreamFormats: <-
default	14:51:10.551259-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x76a0df140) removing 7 device listeners from device 71
default	14:51:10.551426-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x76a0df140) removing 0 device delegate listeners from device 71
default	14:51:10.551438-0500	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0x76a0df140)
default	14:51:10.551858-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	14:51:10.552814-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.11839, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=39688, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	14:51:10.553647-0500	tccd	AUTHREQ_SUBJECT: msgID=401.11839, subject=com.nexy.assistant,
default	14:51:10.554223-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc37138c00 at /Applications/Nexy.app
default	14:51:10.566847-0500	Nexy	       ACv2Workarounds.mm:51    com.nexy.assistant: fix84702776_86723525_86479548_89800354_SinglePacketDesc: false
default	14:51:10.566970-0500	Nexy	       AudioConverter.cpp:1042  Created a new in process converter -> 0x76a371a10, from  1 ch,  48000 Hz, Float32 to  1 ch,  16000 Hz, Float32
default	14:51:10.567193-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	14:51:10.568346-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.11840, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=39688, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	14:51:10.569277-0500	tccd	AUTHREQ_SUBJECT: msgID=401.11840, subject=com.nexy.assistant,
default	14:51:10.569803-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc37138c00 at /Applications/Nexy.app
default	14:51:10.588186-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.11841, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=39688, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	14:51:10.588998-0500	tccd	AUTHREQ_SUBJECT: msgID=401.11841, subject=com.nexy.assistant,
default	14:51:10.589509-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc37138c00 at /Applications/Nexy.app
default	14:51:10.602808-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.21074037.21074043(501)>:39688] from originator [osservice<com.apple.powerd>:334] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:398-334-1518727 target:39688 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	14:51:10.602869-0500	runningboardd	Assertion 398-334-1518727 (target:[app<application.com.nexy.assistant.21074037.21074043(501)>:39688]) will be created as active
default	14:51:10.603130-0500	runningboardd	[app<application.com.nexy.assistant.21074037.21074043(501)>:39688] Ignoring jetsam update because this process is not memory-managed
default	14:51:10.603142-0500	runningboardd	[app<application.com.nexy.assistant.21074037.21074043(501)>:39688] Ignoring suspend because this process is not lifecycle managed
default	14:51:10.603151-0500	runningboardd	[app<application.com.nexy.assistant.21074037.21074043(501)>:39688] Ignoring GPU update because this process is not GPU managed
default	14:51:10.603168-0500	runningboardd	[app<application.com.nexy.assistant.21074037.21074043(501)>:39688] Ignoring memory limit update because this process is not memory-managed
default	14:51:10.606220-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.21074037.21074043(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	14:51:10.606614-0500	gamepolicyd	Received state update for 39688 (app<application.com.nexy.assistant.21074037.21074043(501)>, running-active-NotVisible
default	14:51:10.627171-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Input {BuiltInMicrophoneDevice, 0xb}
default	14:51:10.627963-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ef2bf","name":"Nexy(39688)"}, "details":{"deviceUIDs":[],"implicit_category":"Record","input_running":true,"output_running":false} }
default	14:51:10.628029-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 704, PID = 39688, Name = sid:0x1ef2bf, Nexy(39688), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	14:51:10.628051-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Category/Mode changed -- The score for sid:0x1ef2bf, Nexy(39688), 'prim'/com.nexy.assistant was not correct. Old score = 201
default	14:51:10.628074-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 704, PID = 39688, Name = sid:0x1ef2bf, Nexy(39688), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	14:51:10.628123-0500	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1ef2bf, Nexy(39688), 'prim'', AudioCategory changed to 'Record_WithBluetooth'
default	14:51:10.628151-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:51:10.628165-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 704, PID = 39688, Name = sid:0x1ef2bf, Nexy(39688), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	14:51:10.628192-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 704, PID = 39688, Name = sid:0x1ef2bf, Nexy(39688), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	14:51:10.628240-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:51:10.628240-0500	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 704, PID = 39688, Name = sid:0x1ef2bf, Nexy(39688), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> is going active
default	14:51:10.628274-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:51:10.628285-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1ef2bf, Nexy(39688), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 704 starting recording
default	14:51:10.628313-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:51:10.628345-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:51:10.628357-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 704, PID = 39688, Name = sid:0x1ef2bf, Nexy(39688), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	14:51:10.628386-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 704, PID = 39688, Name = sid:0x1ef2bf, Nexy(39688), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	14:51:10.628427-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:51:10.628407-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1ef2bf, Nexy(39688), 'prim'', displayID:'com.nexy.assistant'}
default	14:51:10.628483-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [1, 0]. BT device UIDS: {(
)}
default	14:51:10.628498-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	14:51:10.628468-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	14:51:10.628547-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	14:51:10.628568-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	14:51:10.628577-0500	audioaccessoryd	AudioStateChanged: Added audio session app com.nexy.assistant NULL -> 200 count 1
default	14:51:10.628586-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
error	14:51:10.628595-0500	audioaccessoryd	Updating local audio category 100 -> 200 app com.nexy.assistant
default	14:51:10.628624-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	14:51:10.640086-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	14:51:10.640141-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	14:51:10.640185-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	14:51:10.640583-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:51:10.640599-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:51:10.640619-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	14:51:10.640628-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:51:10.640635-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	14:51:10.640656-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	14:51:10.640671-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:51:10.640681-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:51:10.640690-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	14:51:10.640722-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:51:10.640810-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	14:51:10.640830-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	14:51:10.640861-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	14:51:10.641443-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:51:10.641460-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:51:10.641470-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	14:51:10.641477-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:51:10.641485-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	14:51:10.641510-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	14:51:10.641535-0500	ControlCenter	Navigating to new application [com.nexy.assistant]
default	14:51:11.798542-0500	audioaccessoryd	AudioStateSnapshot: Route:Speaker App com.nexy.assistant, Score 200, Remote -1NumofApp 1
default	14:51:11.907412-0500	Nexy	LSExceptions shared instance invalidated for timeout.
default	14:51:14.798043-0500	audioaccessoryd	AudioStateSnapshot: Route:Speaker App com.nexy.assistant, Score 200, Remote -1NumofApp 1
default	14:51:17.796802-0500	audioaccessoryd	AudioStateSnapshot: Route:Speaker App com.nexy.assistant, Score 200, Remote -1NumofApp 1
default	14:51:20.796806-0500	audioaccessoryd	AudioStateSnapshot: Route:Speaker App com.nexy.assistant, Score 200, Remote -1NumofApp 1
default	14:51:23.630530-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	14:51:23.638725-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {BuiltInMicrophoneDevice, 0xb}
default	14:51:23.639188-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ef2bf","name":"Nexy(39688)"}, "details":{"deviceUIDs":[],"implicit_category":"","input_running":false,"output_running":false} }
default	14:51:23.639146-0500	runningboardd	Invalidating assertion 398-334-1518727 (target:[app<application.com.nexy.assistant.21074037.21074043(501)>:39688]) from originator [osservice<com.apple.powerd>:334]
default	14:51:23.639420-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 704, PID = 39688, Name = sid:0x1ef2bf, Nexy(39688), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	14:51:23.639522-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 704, PID = 39688, Name = sid:0x1ef2bf, Nexy(39688), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	14:51:23.639590-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1ef2bf, Nexy(39688), 'prim'', displayID:'com.nexy.assistant'}
default	14:51:23.640244-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	14:51:23.640319-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	14:51:23.639839-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1ef2bf, Nexy(39688), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 704 stopping recording
default	14:51:23.640353-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	14:51:23.639892-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	14:51:23.639976-0500	audiomxd	-MXCoreSession- -[MXCoreSession endInterruption:]: Session <ID: 704, PID = 39688, Name = sid:0x1ef2bf, Nexy(39688), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> is going inactive
default	14:51:23.640441-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	14:51:23.640228-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 704, PID = 39688, Name = sid:0x1ef2bf, Nexy(39688), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	14:51:23.641030-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 0]. BT device UIDS: {(
)}
default	14:51:23.641056-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	14:51:23.640431-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 704, PID = 39688, Name = sid:0x1ef2bf, Nexy(39688), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	14:51:23.641388-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:51:23.641452-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:51:23.641480-0500	audioaccessoryd	AudioStateChanged: Removed audio session app com.nexy.assistant 201 count 0
default	14:51:23.641071-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:51:23.660693-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	14:51:23.661727-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:51:23.661755-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:51:23.661778-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	14:51:23.661797-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:51:23.661817-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	14:51:23.661834-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	14:51:23.662328-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	14:51:23.740238-0500	runningboardd	[app<application.com.nexy.assistant.21074037.21074043(501)>:39688] Ignoring jetsam update because this process is not memory-managed
default	14:51:23.740259-0500	runningboardd	[app<application.com.nexy.assistant.21074037.21074043(501)>:39688] Ignoring suspend because this process is not lifecycle managed
default	14:51:23.740286-0500	runningboardd	[app<application.com.nexy.assistant.21074037.21074043(501)>:39688] Ignoring GPU update because this process is not GPU managed
default	14:51:23.740331-0500	runningboardd	[app<application.com.nexy.assistant.21074037.21074043(501)>:39688] Ignoring memory limit update because this process is not memory-managed
default	14:51:23.743230-0500	Nexy	                AUHAL.cpp:473   ~AUHAL: (0x76a0df140) Selecting device 0 from destructor
default	14:51:23.743252-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0x76a0df140)
default	14:51:23.743267-0500	Nexy	                AUHAL.cpp:676   SelectDevice: (0x76a0df140) not already running
default	14:51:23.743278-0500	Nexy	                AUHAL.cpp:682   SelectDevice: (0x76a0df140) disconnecting device 78
default	14:51:23.743293-0500	Nexy	                AUHAL.cpp:746   SelectDevice: (0x76a0df140) destroying ioproc 0xb for device 78
default	14:51:23.743336-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {BuiltInMicrophoneDevice, 0xb}
default	14:51:23.743393-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	14:51:23.743827-0500	Nexy	                AUHAL.cpp:848   SelectDevice: (0x76a0df140) nothing to setup
default	14:51:23.743851-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x76a0df140) adding 0 device listeners to device 0
default	14:51:23.743865-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x76a0df140) adding 0 device delegate listeners to device 0
default	14:51:23.744018-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x76a0df140) removing 7 device listeners from device 78
default	14:51:23.744714-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x76a0df140) removing 0 device delegate listeners from device 78
default	14:51:23.744745-0500	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0x76a0df140)
default	14:51:23.751085-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.21074037.21074043(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	14:51:23.751790-0500	gamepolicyd	Received state update for 39688 (app<application.com.nexy.assistant.21074037.21074043(501)>, running-active-NotVisible
default	14:51:23.763155-0500	Nexy	[0x768461180] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	14:51:23.764312-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=39688.4, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=39688, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	14:51:23.766338-0500	tccd	AUTHREQ_SUBJECT: msgID=39688.4, subject=com.nexy.assistant,
default	14:51:23.767421-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d115e00 at /Applications/Nexy.app
default	14:51:23.785394-0500	tccd	Notifying for access  kTCCServiceListenEvent for target PID[39688], responsiblePID[39688], responsiblePath: /Applications/Nexy.app to UID: 501
default	14:51:23.785768-0500	Nexy	[0x768461180] invalidated after the last release of the connection object
default	14:51:23.881684-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117600 at /Applications/Nexy.app
default	14:51:23.925909-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d115e00 at /Applications/Nexy.app
default	14:51:23.933757-0500	tccd	Publishing <TCCDEvent: type=Modify, service=kTCCServiceListenEvent, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 0 subscribers: {
}
default	14:51:23.951853-0500	nehelper	Received an apps uninstalled notification with bundle IDs (
    "com.nexy.assistant"
)
default	14:51:23.952289-0500	nehelper	Received an apps uninstalled notification with bundle IDs (
    "com.nexy.assistant"
)
default	14:51:24.548151-0500	nehelper	Removing UUIDs for (
    "com.nexy.assistant"
)
default	14:51:24.553685-0500	nehelper	Handling an apps uninstalled notification with bundle IDs (
    "com.nexy.assistant"
)
default	14:51:24.575217-0500	nehelper	com.apple.preferences.networkprivacy-F67B3EA9-90A6-470B-B321-9BBD719C692B: Populating the cache with 1 UUID(s) for com.nexy.assistant
default	14:51:31.277376-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117600 at /Applications/Nexy.app
default	14:51:31.292496-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d114000 at /Applications/Nexy.app
default	14:51:31.301523-0500	tccd	Publishing <TCCDEvent: type=Modify, service=kTCCServiceListenEvent, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 0 subscribers: {
}
default	14:51:36.794878-0500	Nexy	[0x7684612c0] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	14:51:36.796370-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=39688.5, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=39688, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	14:51:36.800103-0500	tccd	AUTHREQ_SUBJECT: msgID=39688.5, subject=com.nexy.assistant,
default	14:51:36.801299-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d114000 at /Applications/Nexy.app
default	14:51:36.820348-0500	tccd	Notifying for access  kTCCServiceScreenCapture for target PID[39688], responsiblePID[39688], responsiblePath: /Applications/Nexy.app to UID: 501
default	14:51:36.820745-0500	Nexy	[0x7684612c0] invalidated after the last release of the connection object
default	14:51:36.874993-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117600 at /Applications/Nexy.app
default	14:51:36.890409-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d114000 at /Applications/Nexy.app
default	14:51:36.894372-0500	tccd	Publishing <TCCDEvent: type=Modify, service=kTCCServiceScreenCapture, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 0 subscribers: {
}
default	14:51:39.979196-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117600 at /Applications/Nexy.app
default	14:51:40.999514-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d114000 at /Applications/Nexy.app
default	14:51:40.008229-0500	tccd	Publishing <TCCDEvent: type=Modify, service=kTCCServiceScreenCapture, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 0 subscribers: {
}
default	14:51:50.356899-0500	audiomxd	  ServerSessionManager.mm:472   { "action":"destroy_session", "session":{"ID":"0x1ef2bf","name":"Nexy(39688)"}, "details":null }
default	14:51:50.356936-0500	audiomxd	AudioApplicationInfoImpl.mm:690   Successfully removed session 0x1ef2bf from AudioApp, recording state unchanged (app: {"name":"[implicit] Nexy","pid":39688})
default	14:51:50.356507-0500	WindowServer	0[outside of RPC]: Process death: 0x0-0x1a7aa79 (Nexy) connectionID: 19B46F pid: 39688 in session 0x101
default	14:51:50.356947-0500	audiomxd	  ServerSessionManager.mm:1081  destroy audio app instance since was created implicitly by session creation and all sessions now gone (audio app: {"name":"[implicit] Nexy","pid":39688})
default	14:51:50.356571-0500	WindowServer	<BSCompoundAssertion:0x7fb0154c0> ([FocusManager:257]-deferringPolicyEvaluationSuppression) acquire for reason:process death - 0x0-0x1a7aa79 (Nexy) acq:0x801b68d60 count:1
default	14:51:50.357301-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 704, PID = 39688, Name = sid:0x1ef2bf, Nexy(39688), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	14:51:50.357431-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 704, PID = 39688, Name = sid:0x1ef2bf, Nexy(39688), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	14:51:50.357578-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:51:50.357743-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:51:50.357832-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:51:50.357892-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:51:50.357916-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:51:50.357903-0500	WindowServer	0[outside of RPC]: [FocusManager:257] update to deferring policy requested for reason: permitted list updated - 0x0-0x1a7aa79 removed - but we are suppressing evaluation for reasons: {(
    "process death - 0x0-0x1a7aa79 (Nexy)"
)}
default	14:51:50.358011-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:51:50.360814-0500	WindowServer	0[outside of RPC]: [FocusManager:257] update to deferring policy requested for reason: permitted list updated - 0x1-0x9b08 removed - but we are suppressing evaluation for reasons: {(
    "process death - 0x0-0x1a7aa79 (Nexy)"
)}
default	14:51:50.369420-0500	runningboardd	XPC connection invalidated: [app<application.com.nexy.assistant.21074037.21074043(501)>:39688]
default	14:51:50.372524-0500	kernel	Nexy[39688] triggered unnest of range 0x1f6000000->0x1f8000000 of DYLD shared region in VM map 0xf06b0b459fa497b9. While not abnormal for debuggers, this increases system memory footprint until the target exits.
default	14:51:50.372539-0500	kernel	Nexy[39688] triggered unnest of range 0x1f8000000->0x1fa000000 of DYLD shared region in VM map 0xf06b0b459fa497b9. While not abnormal for debuggers, this increases system memory footprint until the target exits.
default	14:51:50.434282-0500	Nexy	[0x10545c950] activating connection: mach=true listener=false peer=false name=com.apple.cfprefsd.daemon
default	14:51:50.434359-0500	Nexy	[0x105452d60] activating connection: mach=true listener=false peer=false name=com.apple.cfprefsd.agent
error	14:51:50.566546-0500	Nexy	dlsym cannot find symbol NSMakeRect in CFBundle 0x10545e640 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	14:51:50.566770-0500	Nexy	dlsym cannot find symbol NSMakePoint in CFBundle 0x10545e640 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	14:51:50.566967-0500	Nexy	dlsym cannot find symbol NSMakeSize in CFBundle 0x10545e640 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	14:51:50.567207-0500	Nexy	dlsym cannot find symbol NSMakeRange in CFBundle 0x10545e640 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
default	14:51:50.568440-0500	Nexy	[0x10545ff30] activating connection: mach=true listener=false peer=false name=com.apple.coreservices.launchservicesd
default	14:51:50.569278-0500	Nexy	[0x7be8b4000] activating connection: mach=true listener=false peer=false name=com.apple.analyticsd
default	14:51:50.569674-0500	Nexy	[0x7be8b4140] activating connection: mach=true listener=false peer=false name=com.apple.pasteboard.1
default	14:51:50.570207-0500	Nexy	[0x7be8b4280] activating connection: mach=true listener=false peer=false name=com.apple.distributed_notifications@Uv3
default	14:51:50.572267-0500	Nexy	void _NSDisableAutomaticTerminationAndLog(NSString *) No windows open yet
default	14:51:50.572619-0500	Nexy	[0x7be8b43c0] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	14:51:50.573273-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=39688.1, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=39688, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	14:51:50.576540-0500	tccd	AUTHREQ_SUBJECT: msgID=39688.1, subject=com.nexy.assistant,
default	14:51:50.576905-0500	Nexy	Received configuration update from daemon (initial)
default	14:51:50.577730-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d114000 at /Applications/Nexy.app
default	14:51:50.593049-0500	Nexy	[0x7be8b43c0] invalidated after the last release of the connection object
default	14:51:50.593386-0500	Nexy	server port 0x00003507, session port 0x00003507
default	14:51:50.594480-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=393.17771, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=39688, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=393, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	14:51:50.594511-0500	tccd	requestor: TCCDProcess: identifier=com.apple.WindowServer, pid=393, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=39688, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	14:51:50.595659-0500	tccd	AUTHREQ_SUBJECT: msgID=393.17771, subject=com.nexy.assistant,
default	14:51:50.596513-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d114000 at /Applications/Nexy.app
default	14:51:50.613435-0500	Nexy	New connection 0x19d0d3 main
default	14:51:50.615964-0500	Nexy	CHECKIN: pid=39688
default	14:51:50.622273-0500	launchservicesd	CHECKIN:0x0-0x1a7aa79 39688 com.nexy.assistant
default	14:51:50.622383-0500	Nexy	CHECKEDIN: pid=39688 asn=0x0-0x1a7aa79 foreground=0
default	14:51:50.622652-0500	Nexy	[0x7be8b43c0] activating connection: mach=false listener=true peer=false name=(anonymous)
default	14:51:50.622662-0500	Nexy	[0x7be8b43c0] Connection returned listener port: 0x4703
default	14:51:50.622778-0500	Nexy	[0x7be8d0300] activating connection: mach=false listener=false peer=true name=com.apple.xpc.anonymous.0x7be8b43c0.peer[363].0x7be8d0300
default	14:51:50.623192-0500	loginwindow	-[Application updateInformation] | Got App URL: file:///Applications/Nexy.app/
default	14:51:50.623307-0500	loginwindow	-[ApplicationManager checkInAppContext:eventData:] | ApplicationManager: Checked in app : Nexy
default	14:51:50.623842-0500	Nexy	FRONTLOGGING: version 1
default	14:51:50.623847-0500	Nexy	Registered, pid=39688 ASN=0x0,0x1a7aa79
default	14:51:50.624069-0500	WindowServer	19d0d3[CreateApplication]: Process creation: 0x0-0x1a7aa79 (Nexy) connectionID: 19D0D3 pid: 39688 in session 0x101
default	14:51:50.624345-0500	Nexy	[0x7be8b4500] activating connection: mach=true listener=false peer=false name=com.apple.lsd.mapdb
default	14:51:50.625026-0500	Nexy	[0x7be8b43c0] Connection returned listener port: 0x4703
default	14:51:50.625457-0500	Nexy	BringForward: pid=39688 asn=0x0-0x1a7aa79 bringForward=0 foreground=0 uiElement=1 launchedByLS=1 modifiersCount=1 allDisabled=0
default	14:51:50.625480-0500	Nexy	BringFrontModifier: pid=39688 asn=0x0-0x1a7aa79 Modifier 0 hideAfter=0 hideOthers=0 dontMakeFrontmost=0 mouseDown=0/0 seed=0/0
default	14:51:50.626023-0500	Nexy	Current system appearance, (HLTB: 1), (SLS: 0)
default	14:51:50.628048-0500	Nexy	No persisted cache on this platform.
default	14:51:50.629390-0500	Nexy	Current system appearance, (HLTB: 1), (SLS: 0)
default	14:51:50.630187-0500	Nexy	Post-registration system appearance: (HLTB: 1)
default	14:51:50.631956-0500	Nexy	FBSWorkspace: endpoint monitoring is disabled.
default	14:51:50.631968-0500	Nexy	FBSWorkspace: default shell endpoint is disabled.
default	14:51:50.632016-0500	Nexy	Initializing connection
default	14:51:50.632060-0500	Nexy	Removing all cached process handles
default	14:51:50.632081-0500	Nexy	Sending handshake request attempt #1 to server
default	14:51:50.632090-0500	Nexy	Creating connection to com.apple.runningboard
default	14:51:50.632097-0500	Nexy	[0x7be8b4640] activating connection: mach=true listener=false peer=false name=com.apple.runningboard
default	14:51:50.632426-0500	runningboardd	Setting client for [app<application.com.nexy.assistant.21074037.21074043(501)>:39688] as ready
default	14:51:50.632435-0500	Nexy	[0x7be8b43c0] Connection returned listener port: 0x4703
default	14:51:50.633042-0500	Nexy	Handshake succeeded
default	14:51:50.633060-0500	Nexy	Identity resolved as app<application.com.nexy.assistant.21074037.21074043(501)>
default	14:51:50.633164-0500	distnoted	register name: com.apple.xctest.FakeForceTouchDevice object: com.nexy.assistant token: 1e0000001d pid: 39688
default	14:51:50.635952-0500	Nexy	[0x7be8b43c0] Connection returned listener port: 0x4703
default	14:51:50.639297-0500	Nexy	Created a new Process Instance Registry XPC connection (inactive)
default	14:51:50.639317-0500	Nexy	[0x7be8b4780] activating connection: mach=true listener=false peer=false name=com.apple.linkd.autoShortcut
default	14:51:50.639394-0500	Nexy	Activated connection to com.apple.linkd.autoShortcut (ApplicationService)
default	14:51:50.639436-0500	Nexy	[0x7be8b4a00] activating connection: mach=false listener=true peer=false name=(anonymous)
default	14:51:50.641129-0500	Nexy	[0x7be8b4a00] Connection returned listener port: 0x6803
default	14:51:50.641763-0500	Nexy	Registered process with identifier 39688-2685832
default	14:51:51.805746-0500	Nexy	Registered notify signal com.apple.caulk.alloc.rtdump (0)
default	14:51:51.809211-0500	Nexy	System_Input_Processing_Notification_Handler.mm:456   System_Input_Processing_Notification_Handler::is_vi_available(): Voice isolation DSP is available for client with bundle id com.nexy.assistant (AVFoundation is available, application is not in client deny list, application is not FaceTime variant)
default	14:51:51.810677-0500	Nexy	[0x7be8b4b40] activating connection: mach=true listener=false peer=false name=com.apple.cmio.registerassistantservice.system-extensions
default	14:51:51.812824-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOInitializeListenersForBundleID: for <private> -> <private>
default	14:51:51.814388-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> vpio_preferenceChangedListener: new value ((null)) for key AUVoiceIOClients/com-nexy-assistant/AUVoiceIOChatFlavor, translatedBundleID com.nexy.assistant, bundleIDs {(
    "com.nexy.assistant"
)}
default	14:51:51.814538-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> vpio_preferenceChangedListener: new value ((null)) for key AUVoiceIOClients/com-nexy-assistant/AUVoiceIOIsAutoChatFlavorEnabled, translatedBundleID com.nexy.assistant, bundleIDs {(
    "com.nexy.assistant"
)}
default	14:51:51.814657-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetSupportedChatFlavorsForBundleID: <private>-><private> get supported chat flavors: <private>
default	14:51:51.814668-0500	Nexy	            HALSystem.cpp:134    Enabling HAL Voice Isolation support
default	14:51:51.814698-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetHiddenChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	14:51:51.814834-0500	Nexy	[0x7be8b4c80] activating connection: mach=true listener=false peer=false name=com.apple.tccd
default	14:51:51.815179-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOHiddenChatFlavors newValue: (
    1
)
default	14:51:51.815396-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=39688.2, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=39688, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	14:51:51.821396-0500	tccd	AUTHREQ_SUBJECT: msgID=39688.2, subject=com.nexy.assistant,
default	14:51:51.822171-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc37138c00 at /Applications/Nexy.app
default	14:51:51.834453-0500	Nexy	[0x7be8b4c80] invalidated after the last release of the connection object
default	14:51:51.834584-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetPreferredChatFlavorForBundleID: <private>-><private> get value: 0
default	14:51:51.834621-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetSupportedChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	14:51:51.834922-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOSupportedChatFlavors newValue: (
    0,
    2
)
default	14:51:51.836498-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.11842, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=39688, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	14:51:51.837321-0500	tccd	AUTHREQ_SUBJECT: msgID=401.11842, subject=com.nexy.assistant,
default	14:51:51.837867-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc37138c00 at /Applications/Nexy.app
error	14:51:51.850063-0500	tccd	Request message contains a target_token to accessing_process (TCCDProcess: identifier=com.nexy.assistant, pid=39688, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy) but TCCDProcess: identifier=com.apple.audio.coreaudiod, pid=401, auid=202, euid=202, binary_path=/usr/sbin/coreaudiod is not a TCC manager for service: kTCCServiceScreenCapture.
default	14:51:51.851001-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.11844, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=39688, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	14:51:51.851830-0500	tccd	AUTHREQ_SUBJECT: msgID=401.11844, subject=com.nexy.assistant,
default	14:51:51.852395-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc37138c00 at /Applications/Nexy.app
default	14:51:51.866575-0500	Nexy	  HALPlugInManagement.cpp:440    HALPlugInManagement::RegisterPlugIns: skipping in-process plug-ins
error	14:51:51.866599-0500	Nexy	AddInstanceForFactory: No factory registered for id <CFUUID 0x7beeee300> F8BB1C28-BAE8-11D6-9C31-00039315CD46
default	14:51:51.882781-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetPreferredChatFlavorForBundleID: <private>-><private> get value: 0
default	14:51:53.311582-0500	kernel	SK[6]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid E57063CB-293E-4442-BE6C-2E995F4141A1 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.58165,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0xe0978d53 tp_proto=0x06"
default	14:51:53.311698-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:58165<-><IPv4-redacted>:53] interface: en0 (skipped: 6843)
so_gencnt: 6102366 t_state: SYN_SENT process: Nexy:39688 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xa08fab48
default	14:51:53.329782-0500	kernel	tcp connected: [<IPv4-redacted>:58165<-><IPv4-redacted>:53] interface: en0 (skipped: 6843)
so_gencnt: 6102366 t_state: ESTABLISHED process: Nexy:39688 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xa08fab48
default	14:51:53.330075-0500	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:58165<-><IPv4-redacted>:53] interface: en0 (skipped: 6843)
so_gencnt: 6102366 t_state: FIN_WAIT_1 process: Nexy:39688 Duration: 0.018 sec Conn_Time: 0.018 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 18.000 ms rttvar: 9.000 ms base rtt: 18 ms so_error: 0 svc/tc: 0 flow: 0xa08fab48
default	14:51:53.330085-0500	kernel	tcp_connection_summary [<IPv4-redacted>:58165<-><IPv4-redacted>:53] interface: en0 (skipped: 6843)
so_gencnt: 6102366 t_state: FIN_WAIT_1 process: Nexy:39688 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	14:51:53.345547-0500	Nexy	[0x7be8b4c80] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioComponentRegistrar
default	14:51:53.358176-0500	Nexy	                AUHAL.cpp:420   AUHAL: (0x7bf0a8e40) Selecting device 71 from constructor
default	14:51:53.358186-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0x7bf0a8e40)
default	14:51:53.358191-0500	Nexy	                AUHAL.cpp:676   SelectDevice: (0x7bf0a8e40) not already running
default	14:51:53.358196-0500	Nexy	                AUHAL.cpp:752   SelectDevice: (0x7bf0a8e40) nothing to teardown
default	14:51:53.358200-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0x7bf0a8e40) connecting device 71
default	14:51:53.358289-0500	Nexy	                AUHAL.cpp:3413  IsDeviceUsable: (0x7bf0a8e40) Device ID: 71 (Input:No | Output:Yes): true
default	14:51:53.358397-0500	Nexy	                AUHAL.cpp:769   SelectDevice: (0x7bf0a8e40) created ioproc 0xa for device 71
default	14:51:53.358511-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x7bf0a8e40) adding 7 device listeners to device 71
default	14:51:53.358690-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x7bf0a8e40) adding 0 device delegate listeners to device 71
default	14:51:53.358702-0500	Nexy	                AUHAL.cpp:1581  UpdateStreamFormats: -> (0x7bf0a8e40)
default	14:51:53.358772-0500	Nexy	                AUHAL.cpp:1677  UpdateStreamFormats: 
  output stream 0 [0x48]:  2 ch,  48000 Hz, Float32, interleaved
default	14:51:53.358782-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 1 output streams; not all mono
default	14:51:53.358788-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	14:51:53.358794-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 0 input streams; not all mono
default	14:51:53.358803-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	14:51:53.358889-0500	Nexy	                AUHAL.cpp:1771  UpdateStreamFormats: AUHAL(0x7bf0a8e40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	14:51:53.358896-0500	Nexy	                AUHAL.cpp:1777  UpdateStreamFormats: AUHAL(0x7bf0a8e40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	14:51:53.358900-0500	Nexy	                AUHAL.cpp:1787  UpdateStreamFormats: <-
default	14:51:53.358903-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x7bf0a8e40) removing 0 device listeners from device 0
default	14:51:53.358907-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x7bf0a8e40) removing 0 device delegate listeners from device 0
default	14:51:53.358911-0500	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0x7bf0a8e40)
default	14:51:53.358932-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Output stream enables: Stream 0 is DISABLED
default	14:51:53.359028-0500	Nexy	                AUHAL.cpp:2298  SetProperty: (0x7bf0a8e40) caller requesting device change from 71 to 78
default	14:51:53.359036-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0x7bf0a8e40)
default	14:51:53.359040-0500	Nexy	                AUHAL.cpp:676   SelectDevice: (0x7bf0a8e40) not already running
default	14:51:53.359045-0500	Nexy	                AUHAL.cpp:682   SelectDevice: (0x7bf0a8e40) disconnecting device 71
default	14:51:53.359049-0500	Nexy	                AUHAL.cpp:746   SelectDevice: (0x7bf0a8e40) destroying ioproc 0xa for device 71
default	14:51:53.359108-0500	Nexy	  AVAudioSession_MacOS.mm:1021  initForMacOS
default	14:51:53.359565-0500	Nexy	[0x7be8b4f00] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioSession
default	14:51:53.360505-0500	audiomxd	  ServerSessionManager.mm:315   { "action":"create_session", "session":{"ID":"0x1ef2c0","name":"Nexy(39688)"}, "details":{"PID":39688,"session_type":"Primary"} }
default	14:51:53.360599-0500	audiomxd	AudioApplicationInfoImpl.mm:250   Setting initial isRecording state: 0 for newly-created AudioApp
	app: {"name":"[implicit] Nexy","pid":39688}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1ef2c0, sessionType: 'prim', isRecording: false }, 
]
default	14:51:53.360951-0500	Nexy	    SessionCore_Create.mm:99    Created session 0x7bef09280 with ID: 0x1ef2c0
default	14:51:53.361532-0500	Nexy	[0x7be8b5040] activating connection: mach=true listener=false peer=false name=com.apple.audioanalyticsd
error	14:51:53.361948-0500	Nexy	Reporter disconnected. { function=sendMessage, reporterID=170458662043649 }
default	14:51:53.361963-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped Unknown {BuiltInSpeakerDevice, 0xa}
default	14:51:53.362013-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	14:51:53.362112-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0x7bf0a8e40) connecting device 78
default	14:51:53.362185-0500	Nexy	                AUHAL.cpp:3413  IsDeviceUsable: (0x7bf0a8e40) Device ID: 78 (Input:Yes | Output:No): true
default	14:51:53.363991-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.11845, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=39688, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	14:51:53.365175-0500	tccd	AUTHREQ_SUBJECT: msgID=401.11845, subject=com.nexy.assistant,
default	14:51:53.366024-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc37138c00 at /Applications/Nexy.app
default	14:51:53.379174-0500	Nexy	                AUHAL.cpp:769   SelectDevice: (0x7bf0a8e40) created ioproc 0xa for device 78
default	14:51:53.379291-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x7bf0a8e40) adding 7 device listeners to device 78
default	14:51:53.379483-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x7bf0a8e40) adding 0 device delegate listeners to device 78
default	14:51:53.379494-0500	Nexy	                AUHAL.cpp:1581  UpdateStreamFormats: -> (0x7bf0a8e40)
default	14:51:53.379502-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 0 output streams; not all mono
default	14:51:53.379513-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Output render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	14:51:53.379640-0500	Nexy	                AUHAL.cpp:1677  UpdateStreamFormats: 
  input stream 0 [0x4f]:  1 ch,  48000 Hz, Float32
default	14:51:53.379647-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 1 input streams; all mono
default	14:51:53.379652-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Input render format:  1 ch,  48000 Hz, Float32
default	14:51:53.379761-0500	Nexy	                AUHAL.cpp:1771  UpdateStreamFormats: AUHAL(0x7bf0a8e40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	14:51:53.379776-0500	Nexy	                AUHAL.cpp:1777  UpdateStreamFormats: AUHAL(0x7bf0a8e40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	14:51:53.379782-0500	Nexy	                AUHAL.cpp:1787  UpdateStreamFormats: <-
default	14:51:53.379787-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x7bf0a8e40) removing 7 device listeners from device 71
default	14:51:53.379975-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x7bf0a8e40) removing 0 device delegate listeners from device 71
default	14:51:53.379982-0500	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0x7bf0a8e40)
default	14:51:53.380422-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	14:51:53.381372-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.11846, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=39688, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	14:51:53.382165-0500	tccd	AUTHREQ_SUBJECT: msgID=401.11846, subject=com.nexy.assistant,
default	14:51:53.382699-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc37138c00 at /Applications/Nexy.app
default	14:51:53.394929-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	14:51:53.395834-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.11847, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=39688, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	14:51:53.396578-0500	tccd	AUTHREQ_SUBJECT: msgID=401.11847, subject=com.nexy.assistant,
default	14:51:53.397094-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc37138c00 at /Applications/Nexy.app
default	14:51:53.409368-0500	Nexy	Registered notify signal com.apple.caulk.alloc.audiodump (0)
default	14:51:53.409746-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	14:51:53.410720-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.11848, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=39688, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	14:51:53.411559-0500	tccd	AUTHREQ_SUBJECT: msgID=401.11848, subject=com.nexy.assistant,
default	14:51:53.412111-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc37138c00 at /Applications/Nexy.app
default	14:51:53.424859-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.11849, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=39688, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	14:51:53.425621-0500	tccd	AUTHREQ_SUBJECT: msgID=401.11849, subject=com.nexy.assistant,
default	14:51:53.426147-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc37138c00 at /Applications/Nexy.app
default	14:51:53.439856-0500	runningboardd	ignoring [app<application.com.nexy.assistant.21074037.21074043(501)>:39688] as candidate for concrete target as it is terminating
default	14:51:53.464916-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Input {BuiltInMicrophoneDevice, 0xa}
default	14:51:53.465833-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ef2c0","name":"Nexy(39688)"}, "details":{"deviceUIDs":[],"implicit_category":"Record","input_running":true,"output_running":false} }
default	14:51:53.465919-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 705, PID = 39688, Name = sid:0x1ef2c0, Nexy(39688), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	14:51:53.465969-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 705, PID = 39688, Name = sid:0x1ef2c0, Nexy(39688), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	14:51:53.466031-0500	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1ef2c0, Nexy(39688), 'prim'', AudioCategory changed to 'Record_WithBluetooth'
default	14:51:53.466074-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:51:53.466100-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 705, PID = 39688, Name = sid:0x1ef2c0, Nexy(39688), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	14:51:53.466145-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 705, PID = 39688, Name = sid:0x1ef2c0, Nexy(39688), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	14:51:53.466195-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:51:53.466198-0500	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 705, PID = 39688, Name = sid:0x1ef2c0, Nexy(39688), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> is going active
default	14:51:53.466213-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1ef2c0, Nexy(39688), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 705 starting recording
default	14:51:53.466263-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:51:53.466324-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:51:53.466291-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 705, PID = 39688, Name = sid:0x1ef2c0, Nexy(39688), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	14:51:53.466363-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:51:53.466320-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 705, PID = 39688, Name = sid:0x1ef2c0, Nexy(39688), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	14:51:53.466351-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1ef2c0, Nexy(39688), 'prim'', displayID:'com.nexy.assistant'}
default	14:51:53.466437-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [1, 0]. BT device UIDS: {(
)}
default	14:51:53.466412-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	14:51:53.466479-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:51:53.466449-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	14:51:53.466532-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	14:51:53.466555-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	14:51:53.466564-0500	audioaccessoryd	AudioStateChanged: Added audio session app com.nexy.assistant NULL -> 200 count 1
default	14:51:53.466582-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
error	14:51:53.466590-0500	audioaccessoryd	Updating local audio category 100 -> 200 app com.nexy.assistant
default	14:51:53.466626-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
fault	14:51:53.466890-0500	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.21074037.21074043 AUID=501> and <type=Application identifier=application.com.nexy.assistant.21074037.21074043>
fault	14:51:53.468744-0500	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.21074037.21074043 AUID=501> and <type=Application identifier=application.com.nexy.assistant.21074037.21074043>
default	14:51:53.488871-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	14:51:53.488966-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	14:51:53.489012-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	14:51:53.490436-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:51:53.490447-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:51:53.490461-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	14:51:53.490487-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:51:53.490494-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	14:51:53.490500-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	14:51:53.490602-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	14:51:53.493275-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:51:53.493288-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:51:53.493299-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	14:51:53.493307-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:51:53.493314-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	14:51:53.493319-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	14:51:53.493391-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	14:51:53.494864-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:51:53.494882-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:51:53.494893-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	14:51:53.494900-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:51:53.494918-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	14:51:53.494925-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	14:51:53.495079-0500	ControlCenter	Navigating to new application [com.nexy.assistant]
default	14:51:53.798707-0500	audioaccessoryd	AudioStateSnapshot: Route:Speaker App com.nexy.assistant, Score 200, Remote -1NumofApp 1
default	14:51:54.451998-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	14:51:54.460401-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {BuiltInMicrophoneDevice, 0xa}
default	14:51:54.461117-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ef2c0","name":"Nexy(39688)"}, "details":{"deviceUIDs":[],"implicit_category":"","input_running":false,"output_running":false} }
default	14:51:54.461352-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 705, PID = 39688, Name = sid:0x1ef2c0, Nexy(39688), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	14:51:54.461477-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 705, PID = 39688, Name = sid:0x1ef2c0, Nexy(39688), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	14:51:54.461549-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1ef2c0, Nexy(39688), 'prim'', displayID:'com.nexy.assistant'}
default	14:51:54.461672-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1ef2c0, Nexy(39688), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 705 stopping recording
default	14:51:54.461705-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	14:51:54.461729-0500	audiomxd	-MXCoreSession- -[MXCoreSession endInterruption:]: Session <ID: 705, PID = 39688, Name = sid:0x1ef2c0, Nexy(39688), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> is going inactive
default	14:51:54.461797-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 705, PID = 39688, Name = sid:0x1ef2c0, Nexy(39688), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	14:51:54.461879-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 705, PID = 39688, Name = sid:0x1ef2c0, Nexy(39688), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	14:51:54.461971-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	14:51:54.462058-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	14:51:54.462095-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	14:51:54.462107-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:51:54.462188-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	14:51:54.462295-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:51:54.462136-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 0]. BT device UIDS: {(
)}
default	14:51:54.462352-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:51:54.462163-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	14:51:54.462387-0500	audioaccessoryd	AudioStateChanged: Removed audio session app com.nexy.assistant 201 count 0
default	14:51:54.477243-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	14:51:54.477698-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:51:54.477714-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:51:54.477727-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	14:51:54.477741-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:51:54.477749-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	14:51:54.477755-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	14:51:54.477853-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	14:51:54.564673-0500	Nexy	                AUHAL.cpp:473   ~AUHAL: (0x7bf0a8e40) Selecting device 0 from destructor
default	14:51:54.564706-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0x7bf0a8e40)
default	14:51:54.564722-0500	Nexy	                AUHAL.cpp:676   SelectDevice: (0x7bf0a8e40) not already running
default	14:51:54.564733-0500	Nexy	                AUHAL.cpp:682   SelectDevice: (0x7bf0a8e40) disconnecting device 78
default	14:51:54.564748-0500	Nexy	                AUHAL.cpp:746   SelectDevice: (0x7bf0a8e40) destroying ioproc 0xa for device 78
default	14:51:54.564800-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {BuiltInMicrophoneDevice, 0xa}
default	14:51:54.564847-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	14:51:54.565102-0500	Nexy	                AUHAL.cpp:848   SelectDevice: (0x7bf0a8e40) nothing to setup
default	14:51:54.565123-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x7bf0a8e40) adding 0 device listeners to device 0
default	14:51:54.565134-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x7bf0a8e40) adding 0 device delegate listeners to device 0
default	14:51:54.565145-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x7bf0a8e40) removing 7 device listeners from device 78
default	14:51:54.565578-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x7bf0a8e40) removing 0 device delegate listeners from device 78
default	14:51:54.565608-0500	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0x7bf0a8e40)
default	14:51:54.702984-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=39727.1, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=39688, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.osascript, pid=39727, auid=501, euid=501, binary_path=/usr/bin/osascript}, },
default	14:51:54.704444-0500	tccd	AUTHREQ_SUBJECT: msgID=39727.1, subject=com.nexy.assistant,
default	14:51:54.705055-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d114000 at /Applications/Nexy.app
default	14:51:54.719887-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=393.17772, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=39688, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.osascript, pid=39727, auid=501, euid=501, binary_path=/usr/bin/osascript}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=393, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	14:51:54.720716-0500	tccd	AUTHREQ_SUBJECT: msgID=393.17772, subject=com.nexy.assistant,
default	14:51:54.721270-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d114000 at /Applications/Nexy.app
default	14:51:54.749790-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d114000 at /Applications/Nexy.app
default	14:51:54.769329-0500	System Events	TCCAccessRequestIndirect: TCCAccessRequestIndirect with pid 39696: target_identity: {
    kTCCCodeIdentityAuditToken = {length = 32, bytes = 0xf5010000 f5010000 14000000 f5010000 ... b7860100 90fb2800 };
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
default	14:51:54.781919-0500	tccd	target_executable_path_URL: file:///Applications/Nexy.app/Contents/MacOS/Nexy
default	14:51:56.033030-0500	Nexy	[0x7be8b5400] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
error	14:51:56.033701-0500	tccd	TCCDProcess: identifier=com.nexy.assistant, pid=39688, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy attempted to call TCCAccessRequest for kTCCServiceAccessibility without the recommended com.apple.private.tcc.manager.check-by-audit-token entitlement
default	14:51:56.033879-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=39688.3, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=39688, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.nexy.assistant, pid=39688, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	14:51:56.035418-0500	tccd	AUTHREQ_SUBJECT: msgID=39688.3, subject=com.nexy.assistant,
default	14:51:56.036634-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d114000 at /Applications/Nexy.app
default	14:51:56.049803-0500	Nexy	[0x7be8b5400] invalidated after the last release of the connection object
default	14:51:56.049907-0500	Nexy	[0x7be8b5400] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
error	14:51:56.050276-0500	tccd	TCCDProcess: identifier=com.nexy.assistant, pid=39688, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy attempted to call TCCAccessRequest for kTCCServiceAccessibility without the recommended com.apple.private.tcc.manager.check-by-audit-token entitlement
default	14:51:56.050431-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=39688.4, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=39688, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.nexy.assistant, pid=39688, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	14:51:56.051287-0500	tccd	AUTHREQ_SUBJECT: msgID=39688.4, subject=com.nexy.assistant,
default	14:51:56.051980-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d114000 at /Applications/Nexy.app
default	14:51:56.064552-0500	Nexy	[0x7be8b5400] invalidated after the last release of the connection object
default	14:51:56.064616-0500	Nexy	[0x7be8b5400] activating connection: mach=true listener=false peer=false name=com.apple.universalaccessAuthWarn
default	14:51:56.064708-0500	Nexy	[0x7be8b5400] invalidated after the last release of the connection object
default	14:51:56.070112-0500	Nexy	server port 0x0001540f, session port 0x00003507
default	14:51:56.072555-0500	kernel	SK[7]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 4D0CAB13-1FC9-47E1-A597-60C164627651 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.58166,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0xa3383a18 tp_proto=0x06"
default	14:51:56.072679-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:58166<-><IPv4-redacted>:53] interface: en0 (skipped: 6843)
so_gencnt: 6102368 t_state: SYN_SENT process: Nexy:39688 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 14 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x92631849
default	14:51:56.086338-0500	Nexy	networkd_settings_read_from_file initialized networkd settings by reading plist directly
default	14:51:56.086519-0500	Nexy	networkd_settings_read_from_file initialized networkd settings by reading plist directly
default	14:51:56.087428-0500	Nexy	nw_path_libinfo_path_check [54BE8A8E-A7E4-4BDA-AFB8-002546E62B4A IPv4#46030445:443 tcp, legacy-socket, attribution: developer]
	libinfo check path: <private>
default	14:51:56.088624-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117600 at /Applications/Nexy.app
default	14:51:56.088907-0500	kernel	SK[8]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 59064AAF-4125-4922-9D75-DE7696F4F319 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.58167,dst=<IPv4-redacted>.443,proto=0x06 mask=0x0000003f,hash=0x24063b73 tp_proto=0x06"
default	14:51:56.088989-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:58167<-><IPv4-redacted>:443] interface: en0 (skipped: 6843)
so_gencnt: 6102369 t_state: SYN_SENT process: Nexy:39688 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x81df9cfb
default	14:51:56.090033-0500	kernel	tcp connected: [<IPv4-redacted>:58166<-><IPv4-redacted>:53] interface: en0 (skipped: 6843)
so_gencnt: 6102368 t_state: ESTABLISHED process: Nexy:39688 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 14 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x92631849
default	14:51:56.090393-0500	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:58166<-><IPv4-redacted>:53] interface: en0 (skipped: 6843)
so_gencnt: 6102368 t_state: FIN_WAIT_1 process: Nexy:39688 Duration: 0.018 sec Conn_Time: 0.017 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 17.000 ms rttvar: 8.500 ms base rtt: 14 ms so_error: 0 svc/tc: 0 flow: 0x92631849
default	14:51:56.090403-0500	kernel	tcp_connection_summary [<IPv4-redacted>:58166<-><IPv4-redacted>:53] interface: en0 (skipped: 6843)
so_gencnt: 6102368 t_state: FIN_WAIT_1 process: Nexy:39688 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	14:51:56.090568-0500	kernel	SK[7]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 8607508D-3A0E-4B48-8113-23127716300C flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.58168,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0xf769b3c8 tp_proto=0x06"
default	14:51:56.090584-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:58168<-><IPv4-redacted>:53] interface: en0 (skipped: 6843)
so_gencnt: 6102370 t_state: SYN_SENT process: Nexy:39688 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 14 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xb57f8314
default	14:51:56.104146-0500	kernel	tcp connected: [<IPv4-redacted>:58168<-><IPv4-redacted>:53] interface: en0 (skipped: 6843)
so_gencnt: 6102370 t_state: ESTABLISHED process: Nexy:39688 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 13 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xb57f8314
default	14:51:56.104326-0500	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:58168<-><IPv4-redacted>:53] interface: en0 (skipped: 6843)
so_gencnt: 6102370 t_state: FIN_WAIT_1 process: Nexy:39688 Duration: 0.014 sec Conn_Time: 0.013 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 13.000 ms rttvar: 6.500 ms base rtt: 13 ms so_error: 0 svc/tc: 0 flow: 0xb57f8314
default	14:51:56.104336-0500	kernel	tcp_connection_summary [<IPv4-redacted>:58168<-><IPv4-redacted>:53] interface: en0 (skipped: 6843)
so_gencnt: 6102370 t_state: FIN_WAIT_1 process: Nexy:39688 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	14:51:56.110052-0500	kernel	tcp connected: [<IPv4-redacted>:58167<-><IPv4-redacted>:443] interface: en0 (skipped: 6843)
so_gencnt: 6102369 t_state: ESTABLISHED process: Nexy:39688 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x81df9cfb
default	14:51:56.110620-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d114000 at /Applications/Nexy.app
default	14:51:56.114476-0500	tccd	Publishing <TCCDEvent: type=Modify, service=kTCCServiceAccessibility, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 0 subscribers: {
}
default	14:51:56.199974-0500	Nexy	[0x7be8b5540] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	14:51:56.200664-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=39688.5, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=39688, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	14:51:56.207300-0500	tccd	AUTHREQ_SUBJECT: msgID=39688.5, subject=com.nexy.assistant,
default	14:51:56.207916-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d114000 at /Applications/Nexy.app
default	14:51:56.220554-0500	Nexy	[0x7be8b5540] invalidated after the last release of the connection object
default	14:51:56.398632-0500	Nexy	[0x7be8b57c0] activating connection: mach=true listener=false peer=false name=com.apple.usernoted.client
default	14:51:56.416177-0500	usernoted	Connection com.nexy.assistant with path: /Applications/Nexy.app
default	14:51:56.417037-0500	distnoted	register name: com.apple.nsquiet_safe_quit_give_reason object: com.nexy.assistant token: 2400000020 pid: 39688
default	14:51:56.430146-0500	Nexy	NSApp cache appearance:
-NSRequiresAquaSystemAppearance: 0
-appearance: (null)
-effectiveAppearance: <NSCompositeAppearance: 0x7bf228780
 (
    "<NSAquaAppearance: 0x7bf228640>",
    "<NSSystemAppearance: 0x7bf2286e0>"
)>
default	14:51:56.437164-0500	Nexy	[0x7be8b5cc0] activating connection: mach=true listener=false peer=false name=com.apple.dock.fullscreen
default	14:51:56.437784-0500	Nexy	[0x7be8b5e00] activating connection: mach=true listener=false peer=false name=com.apple.fonts
default	14:51:56.440820-0500	Nexy	(<private>) deleteSearchableItemsWithDomainIdentifiers, protectionClass:(null), domainIdentifiers number:1
default	14:51:56.441126-0500	Nexy	sConnectionName: com.apple.spotlight.IndexAgent
default	14:51:56.441138-0500	Nexy	Start service name com.apple.spotlight.IndexAgent
default	14:51:56.441174-0500	Nexy	[0x7be8b5f40] activating connection: mach=true listener=false peer=false name=com.apple.spotlight.IndexAgent
default	14:51:56.441235-0500	Nexy	[C:1] Alloc com.apple.controlcenter.statusitems
default	14:51:56.441309-0500	Nexy	[0x7be8b6080] activating connection: mach=false listener=false peer=false name=(anonymous)
default	14:51:56.441379-0500	Nexy	FBSWorkspace registering source: <private>
default	14:51:56.442219-0500	suggestd	SGDSpotlightReceiver: deleting 1 domain identifiers (1 after removing overlaps) for com.nexy.assistant: <private>
default	14:51:56.442591-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	14:51:56.443056-0500	Nexy	<FBSWorkspaceScenesClient:0x7bf229f40 <private>> attempting immediate handshake from activate
default	14:51:56.443115-0500	Nexy	<FBSWorkspaceScenesClient:0x7bf229f40 <private>> sent handshake
default	14:51:56.443269-0500	Nexy	Realizing settings extension __NSStatusItemSceneHostSettings__ on FBSSceneSettings
default	14:51:56.447236-0500	Nexy	<FBSWorkspaceScenesClient:0x7bf229f40 <private>> was invalidated
default	14:51:56.447253-0500	Nexy	FBSWorkspace unregistering source: <private>
default	14:51:56.447547-0500	Nexy	Realizing settings extension __NSStatusItemSceneClientSettings__ on FBSSceneClientSettings
default	14:51:56.449089-0500	Nexy	Realizing settings extension FBSSceneSettingsCore on FBSSceneSettings
default	14:51:56.450370-0500	Nexy	Realizing settings extension FBSSceneClientSettingsCore on FBSSceneClientSettings
default	14:51:56.451019-0500	Nexy	Requesting scene <FBSScene: 0x7bf22a1c0; com.apple.controlcenter:0295F1CD-0E98-4ACF-9089-DA67A43885A4> from com.apple.controlcenter.statusitems
error	14:51:56.451231-0500	Nexy	Error creating <FBSScene: 0x7bf22a1c0; com.apple.controlcenter:0295F1CD-0E98-4ACF-9089-DA67A43885A4>: <NSError: 0x7be9f0120; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
default	14:51:56.452692-0500	Nexy	Request for <FBSScene: 0x7bf22a1c0; com.apple.controlcenter:0295F1CD-0E98-4ACF-9089-DA67A43885A4> complete!
default	14:51:56.459088-0500	Nexy	Warning: the app is using `-[NSStatusBarButton setHighlightsBy:]` to set the highlight behavior. Instead, consider removing that setting. That will enable macOS to highlight the status bar button as appropriate for all configurations (e.g., light, dark, and increased contrast modes).
default	14:51:56.473748-0500	Nexy	Registering for test daemon availability notify post.
default	14:51:56.473896-0500	Nexy	notify_get_state check indicated test daemon not ready.
default	14:51:56.473979-0500	Nexy	notify_get_state check indicated test daemon not ready.
default	14:51:56.474073-0500	Nexy	notify_get_state check indicated test daemon not ready.
default	14:51:56.475204-0500	Nexy	[0x7be8b6440] activating connection: mach=true listener=false peer=false name=com.apple.coreservices.appleevents
default	14:51:56.475610-0500	Nexy	[0x7be8b43c0] Connection returned listener port: 0x4703
default	14:51:56.475931-0500	Nexy	SignalReady: pid=39688 asn=0x0-0x1a7aa79
default	14:51:56.476290-0500	Nexy	SIGNAL: pid=39688 asn=0x0x-0x1a7aa79
default	14:51:56.476727-0500	loginwindow	-[Application updateInformation] | Got App URL: file:///Applications/Nexy.app/
default	14:51:56.478506-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d114000 at /Applications/Nexy.app
error	14:51:56.483549-0500	Nexy	scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
default	14:51:56.487950-0500	Nexy	void _NSDisableAutomaticTerminationAndLog(NSString *) Restoring windows
default	14:51:56.487956-0500	Nexy	-[NSApplication _reopenWindowsAsNecessaryIncludingRestorableState:withFullFidelity:completionHandler:] shouldRestoreState=1 hasPersistentStateToRestore=0 shouldStillRestoreStateAfterPrompting=0
default	14:51:56.487970-0500	Nexy	[0x7be8b5540] activating connection: mach=true listener=false peer=false name=com.apple.window_proxies
default	14:51:56.488037-0500	Nexy	[0x7be8b5540] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	14:51:56.488841-0500	Nexy	void _NSEnableAutomaticTerminationAndLog(NSString *) Restoring windows
default	14:51:56.491683-0500	runningboardd	ignoring [app<application.com.nexy.assistant.21074037.21074043(501)>:39688] as candidate for concrete target as it is terminating
default	14:51:56.491720-0500	runningboardd	Acquiring assertion targeting 39688 from originator [app<application.com.nexy.assistant.21074037.21074043(501)>:39688] with description <RBSAssertionDescriptor| "AudioHAL" ID:398-39688-1518817 target:39688 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
error	14:51:56.491962-0500	Nexy	Error acquiring assertion: <Error Domain=RBSAssertionErrorDomain Code=2 "Specified target process 39688 does not exist" UserInfo={NSLocalizedFailureReason=Specified target process 39688 does not exist}>
error	14:51:56.491975-0500	Nexy	          HALRBSAssertionGlue.mm:98    Failed to acquire the AudioHAL RBSAssertion for pid: 39688 with code: 2 - RBSAssertionErrorDomain
default	14:51:56.500490-0500	Nexy	[C:2] Alloc <private>
default	14:51:56.500524-0500	Nexy	[0x7be8b5400] activating connection: mach=false listener=false peer=false name=(anonymous)
error	14:51:56.500698-0500	kernel	Sandbox: WindowManager(584) deny(1) mach-task-name others [Nexy(39688)]
default	14:51:56.502218-0500	WindowManager	Connection activated | (39688) Nexy
default	14:51:56.557374-0500	kernel	udp connect: [<IPv4-redacted>:59466<-><IPv4-redacted>:443] interface:  (skipped: 1081)
so_gencnt: 6102373 so_state: 0x0002 process: Nexy:39688 bytes in/out: 0/0 pkts in/out: 0/0 error: 0 so_error: 0 svc/tc: 0 flow: 0xb03eedca
default	14:51:56.557389-0500	kernel	udp_connection_summary [<IPv4-redacted>:59466<-><IPv4-redacted>:443] interface:  (skipped: 1081)
so_gencnt: 6102373 so_state: 0x0002 process: Nexy:39688 Duration: 0.000 sec Conn_Time: 0.000 sec bytes in/out: 0/0 pkts in/out: 0/0 rxnospace pkts/bytes: 0/0 so_error: 0 svc/tc: 0 flow: 0xb03eedca flowctl: 0us (0x)
default	14:51:56.559493-0500	kernel	SK[6]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 815976B6-6F93-4439-9640-5E57E9B919C9 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.58170,dst=<IPv4-redacted>.443,proto=0x06 mask=0x0000003f,hash=0xf397a45c tp_proto=0x06"
default	14:51:56.559565-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:58170<-><IPv4-redacted>:443] interface: en0 (skipped: 6843)
so_gencnt: 6102375 t_state: SYN_SENT process: Nexy:39688 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 21 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x8e5a5b61
default	14:51:56.585225-0500	kernel	tcp connected: [<IPv4-redacted>:58170<-><IPv4-redacted>:443] interface: en0 (skipped: 6843)
so_gencnt: 6102375 t_state: ESTABLISHED process: Nexy:39688 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 21 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x8e5a5b61
default	14:51:56.610573-0500	Nexy	[0x7be8b5540] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	14:51:56.611155-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=39688.6, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=39688, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	14:51:56.612123-0500	tccd	AUTHREQ_SUBJECT: msgID=39688.6, subject=com.nexy.assistant,
default	14:51:56.612720-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d114000 at /Applications/Nexy.app
default	14:51:56.620189-0500	Nexy	*warn* MailCS ======%%% _setMailMessageAttributes skip:1
default	14:51:56.624164-0500	Nexy	Start service name com.apple.spotlightknowledged
default	14:51:56.624895-0500	Nexy	[GMS] availability notification token 74
default	14:51:56.625881-0500	Nexy	[0x7be8b5540] invalidated after the last release of the connection object
default	14:51:56.627029-0500	Nexy	 [INFO] SLSHWCaptureDesktopProxying:485 request: <private>
default	14:51:56.630271-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=39733.1, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=39688, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.osascript, pid=39733, auid=501, euid=501, binary_path=/usr/bin/osascript}, },
default	14:51:56.630273-0500	Nexy	[0x7be8b5540] activating connection: mach=true listener=false peer=false name=com.apple.replayd
default	14:51:56.630390-0500	Nexy	 [INFO] -[RPDaemonProxy consumeSandboxExtension:processNewConnection:]:568
default	14:51:56.630933-0500	Nexy	 [INFO] -[RPDaemonProxy proxyCoreGraphicsWithMethodType:config:machPort:completionHandler:]:1486
default	14:51:56.637654-0500	tccd	AUTHREQ_SUBJECT: msgID=39733.1, subject=com.nexy.assistant,
default	14:51:56.639022-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d114000 at /Applications/Nexy.app
default	14:51:56.641937-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=31855.4, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=39688, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.replayd, pid=31855, auid=501, euid=501, binary_path=/usr/libexec/replayd}, },
default	14:51:56.641968-0500	tccd	requestor: TCCDProcess: identifier=com.apple.replayd, pid=31855, auid=501, euid=501, binary_path=/usr/libexec/replayd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=39688, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	14:51:56.642973-0500	tccd	AUTHREQ_SUBJECT: msgID=31855.4, subject=com.nexy.assistant,
default	14:51:56.643593-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d114300 at /Applications/Nexy.app
default	14:51:56.653302-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=393.17773, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=39688, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.osascript, pid=39733, auid=501, euid=501, binary_path=/usr/bin/osascript}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=393, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	14:51:56.654259-0500	tccd	AUTHREQ_SUBJECT: msgID=393.17773, subject=com.nexy.assistant,
default	14:51:56.654834-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d114600 at /Applications/Nexy.app
default	14:51:56.671133-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=393.17774, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=39688, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=393, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	14:51:56.671164-0500	tccd	requestor: TCCDProcess: identifier=com.apple.WindowServer, pid=393, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=39688, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	14:51:56.672085-0500	tccd	AUTHREQ_SUBJECT: msgID=393.17774, subject=com.nexy.assistant,
default	14:51:56.672679-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d116700 at /Applications/Nexy.app
default	14:51:56.699250-0500	Nexy	 [INFO] SLSHWCaptureDesktopProxying_block_invoke:506 request: <private>, error: (null), windowInfo: (null)
default	14:51:56.719682-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d116700 at /Applications/Nexy.app
default	14:51:56.722330-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	14:51:56.722385-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant)]
default	14:51:56.722414-0500	ControlCenter	Active activity attributions changed to ["scr:com.nexy.assistant"]
default	14:51:56.726739-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:51:56.726754-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:51:56.726767-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	14:51:56.726773-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:51:56.726783-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	14:51:56.726811-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	14:51:56.727154-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	14:51:56.740559-0500	System Events	TCCAccessRequestIndirect: TCCAccessRequestIndirect with pid 39696: target_identity: {
    kTCCCodeIdentityAuditToken = {length = 32, bytes = 0xf5010000 f5010000 14000000 f5010000 ... b7860100 9cfb2800 };
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
default	14:51:56.752203-0500	tccd	target_executable_path_URL: file:///Applications/Nexy.app/Contents/MacOS/Nexy
default	14:51:57.485259-0500	Nexy	FBSWorkspace registering source: <private>
default	14:51:57.485330-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	14:51:57.485467-0500	Nexy	<FBSWorkspaceScenesClient:0x7c0d34a00 <private>> attempting immediate handshake from activate
default	14:51:57.485537-0500	Nexy	<FBSWorkspaceScenesClient:0x7c0d34a00 <private>> sent handshake
default	14:51:57.486151-0500	Nexy	Requesting scene <FBSScene: 0x7c0d346e0; com.apple.controlcenter:A9B1021A-BDEF-4843-AE5B-7F2FAB947A50> from com.apple.controlcenter.statusitems
default	14:51:57.486804-0500	Nexy	<FBSWorkspaceScenesClient:0x7c0d34a00 <private>> was invalidated
default	14:51:57.486905-0500	Nexy	FBSWorkspace unregistering source: <private>
error	14:51:57.487042-0500	Nexy	Error creating <FBSScene: 0x7c0d346e0; com.apple.controlcenter:A9B1021A-BDEF-4843-AE5B-7F2FAB947A50>: <NSError: 0x7bec07b40; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	14:51:57.487113-0500	Nexy	No scene exists for identity: com.apple.controlcenter:A9B1021A-BDEF-4843-AE5B-7F2FAB947A50
default	14:51:57.488071-0500	Nexy	Request for <FBSScene: 0x7c0d346e0; com.apple.controlcenter:A9B1021A-BDEF-4843-AE5B-7F2FAB947A50> complete!
default	14:51:57.488280-0500	Nexy	Realizing settings extension FBSSceneTransitionContextCore on FBSSceneTransitionContext
default	14:51:57.491725-0500	Nexy	FBSWorkspace registering source: <private>
default	14:51:57.491772-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	14:51:57.491888-0500	Nexy	<FBSWorkspaceScenesClient:0x7c0d34820 <private>> attempting immediate handshake from activate
default	14:51:57.491934-0500	Nexy	<FBSWorkspaceScenesClient:0x7c0d34820 <private>> sent handshake
default	14:51:57.492093-0500	Nexy	Realizing settings extension __NSHostedViewSceneSettings__ on FBSSceneSettings
default	14:51:57.492875-0500	Nexy	Realizing settings extension __NSClientHostedViewSceneSettings__ on FBSSceneClientSettings
default	14:51:57.493145-0500	Nexy	<FBSWorkspaceScenesClient:0x7c0d34820 <private>> was invalidated
default	14:51:57.493177-0500	Nexy	FBSWorkspace unregistering source: <private>
default	14:51:57.493573-0500	Nexy	Realizing settings extension __NSStatusItemAuxiliaryViewSceneSettings__ on FBSSceneSettings
default	14:51:57.493674-0500	Nexy	Realizing settings extension __NSClientStatusItemAuxiliaryViewSceneSettings__ on FBSSceneClientSettings
default	14:51:57.494364-0500	Nexy	Requesting scene <FBSScene: 0x7c0d34780; com.apple.controlcenter:A9B1021A-BDEF-4843-AE5B-7F2FAB947A50-Aux[1]-NSStatusItemView> from com.apple.controlcenter.statusitems
error	14:51:57.494640-0500	Nexy	Error creating <FBSScene: 0x7c0d34780; com.apple.controlcenter:A9B1021A-BDEF-4843-AE5B-7F2FAB947A50-Aux[1]-NSStatusItemView>: <NSError: 0x7bec07a50; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
default	14:51:57.494712-0500	Nexy	Request for <FBSScene: 0x7c0d34780; com.apple.controlcenter:A9B1021A-BDEF-4843-AE5B-7F2FAB947A50-Aux[1]-NSStatusItemView> complete!
error	14:51:57.495198-0500	Nexy	scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	14:51:57.495232-0500	Nexy	[com.apple.controlcenter:A9B1021A-BDEF-4843-AE5B-7F2FAB947A50] No matching scene to invalidate for this identity.
error	14:51:57.495295-0500	Nexy	auxiliary scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	14:51:57.495359-0500	Nexy	Unhandled disconnected scene <private>
error	14:51:57.495493-0500	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
default	14:51:58.496875-0500	Nexy	FBSWorkspace registering source: <private>
default	14:51:58.496934-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	14:51:58.497072-0500	Nexy	<FBSWorkspaceScenesClient:0x7c0d34780 <private>> attempting immediate handshake from activate
default	14:51:58.497127-0500	Nexy	<FBSWorkspaceScenesClient:0x7c0d34780 <private>> sent handshake
default	14:51:58.497611-0500	Nexy	Requesting scene <FBSScene: 0x7c0d346e0; com.apple.controlcenter:655A4E39-D985-4CEB-B975-76140D132942> from com.apple.controlcenter.statusitems
default	14:51:58.498059-0500	Nexy	Request for <FBSScene: 0x7c0d346e0; com.apple.controlcenter:655A4E39-D985-4CEB-B975-76140D132942> complete!
default	14:51:58.498389-0500	Nexy	<FBSWorkspaceScenesClient:0x7c0d34780 <private>> was invalidated
default	14:51:58.498425-0500	Nexy	FBSWorkspace unregistering source: <private>
error	14:51:58.498508-0500	Nexy	Error creating <FBSScene: 0x7c0d346e0; com.apple.controlcenter:655A4E39-D985-4CEB-B975-76140D132942>: <NSError: 0x7bec07120; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	14:51:58.498545-0500	Nexy	No scene exists for identity: com.apple.controlcenter:655A4E39-D985-4CEB-B975-76140D132942
default	14:51:58.498599-0500	Nexy	FBSWorkspace registering source: <private>
default	14:51:58.498621-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	14:51:58.498682-0500	Nexy	<FBSWorkspaceScenesClient:0x7c0d34a00 <private>> attempting immediate handshake from activate
default	14:51:58.498706-0500	Nexy	<FBSWorkspaceScenesClient:0x7c0d34a00 <private>> sent handshake
default	14:51:58.498913-0500	Nexy	Requesting scene <FBSScene: 0x7c0d34820; com.apple.controlcenter:655A4E39-D985-4CEB-B975-76140D132942-Aux[2]-NSStatusItemView> from com.apple.controlcenter.statusitems
default	14:51:58.499264-0500	Nexy	Request for <FBSScene: 0x7c0d34820; com.apple.controlcenter:655A4E39-D985-4CEB-B975-76140D132942-Aux[2]-NSStatusItemView> complete!
default	14:51:58.499332-0500	Nexy	<FBSWorkspaceScenesClient:0x7c0d34a00 <private>> was invalidated
default	14:51:58.499361-0500	Nexy	FBSWorkspace unregistering source: <private>
error	14:51:58.499424-0500	Nexy	Error creating <FBSScene: 0x7c0d34820; com.apple.controlcenter:655A4E39-D985-4CEB-B975-76140D132942-Aux[2]-NSStatusItemView>: <NSError: 0x7bec07870; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	14:51:58.499449-0500	Nexy	No scene exists for identity: com.apple.controlcenter:655A4E39-D985-4CEB-B975-76140D132942-Aux[2]-NSStatusItemView
default	14:51:58.500278-0500	Nexy	[com.apple.controlcenter:655A4E39-D985-4CEB-B975-76140D132942-Aux[2]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
error	14:51:58.500678-0500	Nexy	scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	14:51:58.500703-0500	Nexy	[com.apple.controlcenter:655A4E39-D985-4CEB-B975-76140D132942] No matching scene to invalidate for this identity.
error	14:51:58.500735-0500	Nexy	auxiliary scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	14:51:58.500754-0500	Nexy	[com.apple.controlcenter:655A4E39-D985-4CEB-B975-76140D132942-Aux[2]-NSStatusItemView] No matching scene to invalidate for this identity.
error	14:51:58.501267-0500	Nexy	Unhandled disconnected scene <private>
error	14:51:58.501377-0500	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
error	14:51:58.501468-0500	Nexy	Unhandled disconnected auxiliary scene <private>
error	14:51:58.501518-0500	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
default	14:51:59.502219-0500	Nexy	FBSWorkspace registering source: <private>
default	14:51:59.502278-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	14:51:59.502461-0500	Nexy	<FBSWorkspaceScenesClient:0x7c0d34820 <private>> attempting immediate handshake from activate
default	14:51:59.502520-0500	Nexy	<FBSWorkspaceScenesClient:0x7c0d34820 <private>> sent handshake
default	14:51:59.503019-0500	Nexy	Requesting scene <FBSScene: 0x7c0d346e0; com.apple.controlcenter:B05E2357-4E34-4FBB-A651-6AEA9F0C80C7> from com.apple.controlcenter.statusitems
default	14:51:59.503452-0500	Nexy	Request for <FBSScene: 0x7c0d346e0; com.apple.controlcenter:B05E2357-4E34-4FBB-A651-6AEA9F0C80C7> complete!
default	14:51:59.503911-0500	Nexy	<FBSWorkspaceScenesClient:0x7c0d34820 <private>> was invalidated
default	14:51:59.503967-0500	Nexy	FBSWorkspace unregistering source: <private>
default	14:51:59.504065-0500	Nexy	FBSWorkspace registering source: <private>
default	14:51:59.504101-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	14:51:59.504193-0500	Nexy	<FBSWorkspaceScenesClient:0x7c0d34d20 <private>> attempting immediate handshake from activate
default	14:51:59.504235-0500	Nexy	<FBSWorkspaceScenesClient:0x7c0d34d20 <private>> sent handshake
error	14:51:59.504352-0500	Nexy	Error creating <FBSScene: 0x7c0d346e0; com.apple.controlcenter:B05E2357-4E34-4FBB-A651-6AEA9F0C80C7>: <NSError: 0x7bec07a50; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	14:51:59.504390-0500	Nexy	No scene exists for identity: com.apple.controlcenter:B05E2357-4E34-4FBB-A651-6AEA9F0C80C7
default	14:51:59.504519-0500	Nexy	Requesting scene <FBSScene: 0x7c0d34780; com.apple.controlcenter:B05E2357-4E34-4FBB-A651-6AEA9F0C80C7-Aux[3]-NSStatusItemView> from com.apple.controlcenter.statusitems
default	14:51:59.504856-0500	Nexy	Request for <FBSScene: 0x7c0d34780; com.apple.controlcenter:B05E2357-4E34-4FBB-A651-6AEA9F0C80C7-Aux[3]-NSStatusItemView> complete!
default	14:51:59.505122-0500	Nexy	<FBSWorkspaceScenesClient:0x7c0d34d20 <private>> was invalidated
default	14:51:59.505172-0500	Nexy	FBSWorkspace unregistering source: <private>
error	14:51:59.505278-0500	Nexy	Error creating <FBSScene: 0x7c0d34780; com.apple.controlcenter:B05E2357-4E34-4FBB-A651-6AEA9F0C80C7-Aux[3]-NSStatusItemView>: <NSError: 0x7bec07690; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	14:51:59.505322-0500	Nexy	No scene exists for identity: com.apple.controlcenter:B05E2357-4E34-4FBB-A651-6AEA9F0C80C7-Aux[3]-NSStatusItemView
default	14:51:59.505685-0500	Nexy	[com.apple.controlcenter:B05E2357-4E34-4FBB-A651-6AEA9F0C80C7-Aux[3]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
error	14:51:59.506129-0500	Nexy	scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	14:51:59.506162-0500	Nexy	[com.apple.controlcenter:B05E2357-4E34-4FBB-A651-6AEA9F0C80C7] No matching scene to invalidate for this identity.
error	14:51:59.506218-0500	Nexy	auxiliary scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	14:51:59.506252-0500	Nexy	[com.apple.controlcenter:B05E2357-4E34-4FBB-A651-6AEA9F0C80C7-Aux[3]-NSStatusItemView] No matching scene to invalidate for this identity.
error	14:51:59.506820-0500	Nexy	Unhandled disconnected scene <private>
error	14:51:59.506942-0500	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
error	14:51:59.507050-0500	Nexy	Unhandled disconnected auxiliary scene <private>
error	14:51:59.507128-0500	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
default	14:52:00.507621-0500	Nexy	FBSWorkspace registering source: <private>
default	14:52:00.507667-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	14:52:00.507780-0500	Nexy	<FBSWorkspaceScenesClient:0x7c0d34780 <private>> attempting immediate handshake from activate
default	14:52:00.507822-0500	Nexy	<FBSWorkspaceScenesClient:0x7c0d34780 <private>> sent handshake
default	14:52:00.508193-0500	Nexy	Requesting scene <FBSScene: 0x7c0d346e0; com.apple.controlcenter:EC2154FB-DFCF-4721-94D7-0D9624587FD6> from com.apple.controlcenter.statusitems
default	14:52:00.508528-0500	Nexy	Request for <FBSScene: 0x7c0d346e0; com.apple.controlcenter:EC2154FB-DFCF-4721-94D7-0D9624587FD6> complete!
default	14:52:00.508981-0500	Nexy	<FBSWorkspaceScenesClient:0x7c0d34780 <private>> was invalidated
default	14:52:00.509022-0500	Nexy	FBSWorkspace unregistering source: <private>
error	14:52:00.509150-0500	Nexy	Error creating <FBSScene: 0x7c0d346e0; com.apple.controlcenter:EC2154FB-DFCF-4721-94D7-0D9624587FD6>: <NSError: 0x7bec07990; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	14:52:00.509176-0500	Nexy	No scene exists for identity: com.apple.controlcenter:EC2154FB-DFCF-4721-94D7-0D9624587FD6
default	14:52:00.509227-0500	Nexy	Requesting scene <FBSScene: 0x7c0d34d20; com.apple.controlcenter:EC2154FB-DFCF-4721-94D7-0D9624587FD6-Aux[4]-NSStatusItemView> from com.apple.controlcenter.statusitems
error	14:52:00.509394-0500	Nexy	Error creating <FBSScene: 0x7c0d34d20; com.apple.controlcenter:EC2154FB-DFCF-4721-94D7-0D9624587FD6-Aux[4]-NSStatusItemView>: <NSError: 0x7bec07930; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
default	14:52:00.509449-0500	Nexy	Request for <FBSScene: 0x7c0d34d20; com.apple.controlcenter:EC2154FB-DFCF-4721-94D7-0D9624587FD6-Aux[4]-NSStatusItemView> complete!
error	14:52:00.509681-0500	Nexy	scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	14:52:00.509708-0500	Nexy	[com.apple.controlcenter:EC2154FB-DFCF-4721-94D7-0D9624587FD6] No matching scene to invalidate for this identity.
error	14:52:00.509747-0500	Nexy	auxiliary scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	14:52:00.509790-0500	Nexy	Unhandled disconnected scene <private>
error	14:52:00.509874-0500	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
default	14:52:00.541188-0500	Nexy	                AUHAL.cpp:420   AUHAL: (0x7bf0a8e40) Selecting device 71 from constructor
default	14:52:00.541223-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0x7bf0a8e40)
default	14:52:00.541239-0500	Nexy	                AUHAL.cpp:676   SelectDevice: (0x7bf0a8e40) not already running
default	14:52:00.541253-0500	Nexy	                AUHAL.cpp:752   SelectDevice: (0x7bf0a8e40) nothing to teardown
default	14:52:00.541264-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0x7bf0a8e40) connecting device 71
default	14:52:00.541500-0500	Nexy	                AUHAL.cpp:3413  IsDeviceUsable: (0x7bf0a8e40) Device ID: 71 (Input:No | Output:Yes): true
default	14:52:00.541810-0500	Nexy	                AUHAL.cpp:769   SelectDevice: (0x7bf0a8e40) created ioproc 0xb for device 71
default	14:52:00.542138-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x7bf0a8e40) adding 7 device listeners to device 71
default	14:52:00.542658-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x7bf0a8e40) adding 0 device delegate listeners to device 71
default	14:52:00.542682-0500	Nexy	                AUHAL.cpp:1581  UpdateStreamFormats: -> (0x7bf0a8e40)
default	14:52:00.542880-0500	Nexy	                AUHAL.cpp:1677  UpdateStreamFormats: 
  output stream 0 [0x48]:  2 ch,  48000 Hz, Float32, interleaved
default	14:52:00.542905-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 1 output streams; not all mono
default	14:52:00.542922-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	14:52:00.542942-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 0 input streams; not all mono
default	14:52:00.542963-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	14:52:00.543237-0500	Nexy	                AUHAL.cpp:1771  UpdateStreamFormats: AUHAL(0x7bf0a8e40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	14:52:00.543267-0500	Nexy	                AUHAL.cpp:1777  UpdateStreamFormats: AUHAL(0x7bf0a8e40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	14:52:00.543282-0500	Nexy	                AUHAL.cpp:1787  UpdateStreamFormats: <-
default	14:52:00.543297-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x7bf0a8e40) removing 0 device listeners from device 0
default	14:52:00.543308-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x7bf0a8e40) removing 0 device delegate listeners from device 0
default	14:52:00.543320-0500	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0x7bf0a8e40)
default	14:52:00.543349-0500	Nexy	                AUHAL.cpp:2298  SetProperty: (0x7bf0a8e40) caller requesting device change from 71 to 71
default	14:52:00.543363-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0x7bf0a8e40)
default	14:52:00.543375-0500	Nexy	                AUHAL.cpp:659   SelectDevice: <- (0x7bf0a8e40) exiting with nothing to do
default	14:52:00.544378-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	14:52:00.545083-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	14:52:00.549458-0500	Nexy	                AUHAL.cpp:473   ~AUHAL: (0x7bf0a8e40) Selecting device 0 from destructor
default	14:52:00.549477-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0x7bf0a8e40)
default	14:52:00.549489-0500	Nexy	                AUHAL.cpp:676   SelectDevice: (0x7bf0a8e40) not already running
default	14:52:00.549499-0500	Nexy	                AUHAL.cpp:682   SelectDevice: (0x7bf0a8e40) disconnecting device 71
default	14:52:00.549508-0500	Nexy	                AUHAL.cpp:746   SelectDevice: (0x7bf0a8e40) destroying ioproc 0xb for device 71
default	14:52:00.549549-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Output {BuiltInSpeakerDevice, 0xb}
default	14:52:00.549628-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	14:52:00.549838-0500	Nexy	                AUHAL.cpp:848   SelectDevice: (0x7bf0a8e40) nothing to setup
default	14:52:00.549859-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x7bf0a8e40) adding 0 device listeners to device 0
default	14:52:00.549869-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x7bf0a8e40) adding 0 device delegate listeners to device 0
default	14:52:00.549879-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x7bf0a8e40) removing 7 device listeners from device 71
default	14:52:00.550271-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x7bf0a8e40) removing 0 device delegate listeners from device 71
default	14:52:00.550295-0500	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0x7bf0a8e40)
default	14:52:00.551808-0500	Nexy	                AUHAL.cpp:420   AUHAL: (0x7bf0a8e40) Selecting device 71 from constructor
default	14:52:00.551827-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0x7bf0a8e40)
default	14:52:00.551837-0500	Nexy	                AUHAL.cpp:676   SelectDevice: (0x7bf0a8e40) not already running
default	14:52:00.551846-0500	Nexy	                AUHAL.cpp:752   SelectDevice: (0x7bf0a8e40) nothing to teardown
default	14:52:00.551867-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0x7bf0a8e40) connecting device 71
default	14:52:00.552009-0500	Nexy	                AUHAL.cpp:3413  IsDeviceUsable: (0x7bf0a8e40) Device ID: 71 (Input:No | Output:Yes): true
default	14:52:00.552175-0500	Nexy	                AUHAL.cpp:769   SelectDevice: (0x7bf0a8e40) created ioproc 0xc for device 71
default	14:52:00.552359-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x7bf0a8e40) adding 7 device listeners to device 71
default	14:52:00.552670-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x7bf0a8e40) adding 0 device delegate listeners to device 71
default	14:52:00.552687-0500	Nexy	                AUHAL.cpp:1581  UpdateStreamFormats: -> (0x7bf0a8e40)
default	14:52:00.552819-0500	Nexy	                AUHAL.cpp:1677  UpdateStreamFormats: 
  output stream 0 [0x48]:  2 ch,  48000 Hz, Float32, interleaved
default	14:52:00.552835-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 1 output streams; not all mono
default	14:52:00.552846-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	14:52:00.552859-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 0 input streams; not all mono
default	14:52:00.552871-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	14:52:00.553049-0500	Nexy	                AUHAL.cpp:1771  UpdateStreamFormats: AUHAL(0x7bf0a8e40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	14:52:00.553066-0500	Nexy	                AUHAL.cpp:1777  UpdateStreamFormats: AUHAL(0x7bf0a8e40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	14:52:00.553076-0500	Nexy	                AUHAL.cpp:1787  UpdateStreamFormats: <-
default	14:52:00.553085-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x7bf0a8e40) removing 0 device listeners from device 0
default	14:52:00.553092-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x7bf0a8e40) removing 0 device delegate listeners from device 0
default	14:52:00.553098-0500	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0x7bf0a8e40)
default	14:52:00.553117-0500	Nexy	                AUHAL.cpp:2298  SetProperty: (0x7bf0a8e40) caller requesting device change from 71 to 71
default	14:52:00.553123-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0x7bf0a8e40)
default	14:52:00.553131-0500	Nexy	                AUHAL.cpp:659   SelectDevice: <- (0x7bf0a8e40) exiting with nothing to do
default	14:52:00.553141-0500	Nexy	AudioHardware-mac-imp.cpp:1299   AudioObjectAddPropertyListener: listener was already added
default	14:52:00.554018-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	14:52:00.554435-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	14:52:00.558012-0500	runningboardd	ignoring [app<application.com.nexy.assistant.21074037.21074043(501)>:39688] as candidate for concrete target as it is terminating
default	14:52:00.558094-0500	runningboardd	Acquiring assertion targeting 39688 from originator [app<application.com.nexy.assistant.21074037.21074043(501)>:39688] with description <RBSAssertionDescriptor| "AudioHAL" ID:398-39688-1518821 target:39688 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	14:52:00.558471-0500	runningboardd	ignoring [app<application.com.nexy.assistant.21074037.21074043(501)>:39688] as candidate for concrete target as it is terminating
error	14:52:00.558593-0500	Nexy	Error acquiring assertion: <Error Domain=RBSAssertionErrorDomain Code=2 "Specified target process 39688 does not exist" UserInfo={NSLocalizedFailureReason=Specified target process 39688 does not exist}>
error	14:52:00.558620-0500	Nexy	          HALRBSAssertionGlue.mm:98    Failed to acquire the AudioHAL RBSAssertion for pid: 39688 with code: 2 - RBSAssertionErrorDomain
default	14:52:00.585156-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {BuiltInSpeakerDevice, 0xc}
default	14:52:00.586417-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ef2c0","name":"Nexy(39688)"}, "details":{"deviceUIDs":[],"implicit_category":"MediaPlayback","input_running":false,"output_running":true} }
default	14:52:00.586519-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 705, PID = 39688, Name = sid:0x1ef2c0, Nexy(39688), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	14:52:00.586553-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Category/Mode changed -- The score for sid:0x1ef2c0, Nexy(39688), 'prim'/com.nexy.assistant was not correct. Old score = 201
default	14:52:00.586585-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 705, PID = 39688, Name = sid:0x1ef2c0, Nexy(39688), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	14:52:00.586633-0500	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1ef2c0, Nexy(39688), 'prim'', AudioCategory changed to 'MediaPlayback'
default	14:52:00.586678-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:52:00.586733-0500	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 705, PID = 39688, Name = sid:0x1ef2c0, Nexy(39688), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO> is going active
default	14:52:00.586757-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsPlaying:]: MXCoreSession com.nexy.assistant with category/mode MediaPlayback/Default and coreSessionID = 705 starting playing
default	14:52:00.586863-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:52:00.586901-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:52:00.586833-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 705, PID = 39688, Name = sid:0x1ef2c0, Nexy(39688), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	14:52:00.586913-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 705, PID = 39688, Name = sid:0x1ef2c0, Nexy(39688), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO>
default	14:52:00.586975-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1ef2c0, Nexy(39688), 'prim'', displayID:'com.nexy.assistant'}
default	14:52:00.587048-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Will try to see if we can get the shared route for session = <ID: 705, PID = 39688, Name = sid:0x1ef2c0, Nexy(39688), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO>. Old (200) and New (201) scores.
default	14:52:00.587162-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 201, deviceID = <private>
default	14:52:00.587244-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 1]. BT device UIDS: {(
)}
default	14:52:00.587172-0500	audiomxd	AudioApplicationInfoImpl.mm:395   Successfully updated session 0x1ef2c0 to isSessionRecording: 0
	app: {"name":"[implicit] Nexy","pid":39688}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1ef2c0, sessionType: 'prim', isRecording: false }, 
]
default	14:52:00.587258-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	14:52:00.588907-0500	audioaccessoryd	Routing request Wx NULL score 201 flag 0x1 < Hijack > app com.nexy.assistant CID 0xD310001 category Not set
default	14:52:00.589159-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	14:52:00.589253-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 201,
}
default	14:52:00.589282-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	14:52:00.589299-0500	audioaccessoryd	AudioStateChanged: Added audio session app com.nexy.assistant NULL -> 201 count 2
default	14:52:00.589312-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 201
error	14:52:00.589334-0500	audioaccessoryd	Updating local audio category 100 -> 201 app com.nexy.assistant
default	14:52:00.589379-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.nexy.assistant
default	14:52:01.419459-0500	Nexy	void _updateToReflectAutomaticTerminationState(void) Setting _kLSApplicationWouldBeTerminatedByTALKey=1
default	14:52:01.511169-0500	Nexy	FBSWorkspace registering source: <private>
default	14:52:01.511198-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	14:52:01.511291-0500	Nexy	<FBSWorkspaceScenesClient:0x7c0d34780 <private>> attempting immediate handshake from activate
default	14:52:01.511322-0500	Nexy	<FBSWorkspaceScenesClient:0x7c0d34780 <private>> sent handshake
default	14:52:01.511590-0500	Nexy	Requesting scene <FBSScene: 0x7c0d34d20; com.apple.controlcenter:7B2C1C28-8461-46E6-9187-5C378CFB2999> from com.apple.controlcenter.statusitems
default	14:52:01.511832-0500	Nexy	Request for <FBSScene: 0x7c0d34d20; com.apple.controlcenter:7B2C1C28-8461-46E6-9187-5C378CFB2999> complete!
default	14:52:01.512188-0500	Nexy	Requesting scene <FBSScene: 0x7c0d34c80; com.apple.controlcenter:7B2C1C28-8461-46E6-9187-5C378CFB2999-Aux[5]-NSStatusItemView> from com.apple.controlcenter.statusitems
default	14:52:01.512243-0500	Nexy	<FBSWorkspaceScenesClient:0x7c0d34780 <private>> was invalidated
default	14:52:01.512270-0500	Nexy	FBSWorkspace unregistering source: <private>
error	14:52:01.512326-0500	Nexy	Error creating <FBSScene: 0x7c0d34d20; com.apple.controlcenter:7B2C1C28-8461-46E6-9187-5C378CFB2999>: <NSError: 0x7be9f2790; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	14:52:01.512341-0500	Nexy	No scene exists for identity: com.apple.controlcenter:7B2C1C28-8461-46E6-9187-5C378CFB2999
error	14:52:01.512372-0500	Nexy	Error creating <FBSScene: 0x7c0d34c80; com.apple.controlcenter:7B2C1C28-8461-46E6-9187-5C378CFB2999-Aux[5]-NSStatusItemView>: <NSError: 0x7be9f2af0; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
default	14:52:01.512373-0500	Nexy	Request for <FBSScene: 0x7c0d34c80; com.apple.controlcenter:7B2C1C28-8461-46E6-9187-5C378CFB2999-Aux[5]-NSStatusItemView> complete!
error	14:52:01.512383-0500	Nexy	No scene exists for identity: com.apple.controlcenter:7B2C1C28-8461-46E6-9187-5C378CFB2999-Aux[5]-NSStatusItemView
error	14:52:01.512526-0500	Nexy	scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	14:52:01.512542-0500	Nexy	[com.apple.controlcenter:7B2C1C28-8461-46E6-9187-5C378CFB2999] No matching scene to invalidate for this identity.
error	14:52:01.512563-0500	Nexy	auxiliary scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	14:52:01.512630-0500	Nexy	Unhandled disconnected scene <private>
error	14:52:01.512690-0500	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
default	14:52:01.570144-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=39735.1, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=39688, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.osascript, pid=39735, auid=501, euid=501, binary_path=/usr/bin/osascript}, },
default	14:52:01.571657-0500	tccd	AUTHREQ_SUBJECT: msgID=39735.1, subject=com.nexy.assistant,
default	14:52:01.572314-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d116700 at /Applications/Nexy.app
default	14:52:01.588985-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=393.17778, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=39688, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.osascript, pid=39735, auid=501, euid=501, binary_path=/usr/bin/osascript}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=393, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	14:52:01.589922-0500	tccd	AUTHREQ_SUBJECT: msgID=393.17778, subject=com.nexy.assistant,
default	14:52:01.590500-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d116700 at /Applications/Nexy.app
default	14:52:01.619460-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d116700 at /Applications/Nexy.app
default	14:52:01.636432-0500	System Events	TCCAccessRequestIndirect: TCCAccessRequestIndirect with pid 39696: target_identity: {
    kTCCCodeIdentityAuditToken = {length = 32, bytes = 0xf5010000 f5010000 14000000 f5010000 ... b7860100 a1fb2800 };
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
default	14:52:01.646840-0500	tccd	target_executable_path_URL: file:///Applications/Nexy.app/Contents/MacOS/Nexy
default	14:52:02.080194-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Output {BuiltInSpeakerDevice, 0xc}
default	14:52:02.080744-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ef2c0","name":"Nexy(39688)"}, "details":{"deviceUIDs":[],"implicit_category":"","input_running":false,"output_running":false} }
default	14:52:02.080897-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsPlaying:]: MXCoreSession com.nexy.assistant with category/mode MediaPlayback/Default and coreSessionID = 705 stopping playing
default	14:52:02.080981-0500	audiomxd	-MXCoreSession- -[MXCoreSession endInterruption:]: Session <ID: 705, PID = 39688, Name = sid:0x1ef2c0, Nexy(39688), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> is going inactive
default	14:52:02.081058-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 705, PID = 39688, Name = sid:0x1ef2c0, Nexy(39688), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	14:52:02.081161-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 705, PID = 39688, Name = sid:0x1ef2c0, Nexy(39688), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	14:52:02.081319-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:52:02.081418-0500	audiomxd	AudioApplicationInfoImpl.mm:395   Successfully updated session 0x1ef2c0 to isSessionRecording: 0
	app: {"name":"[implicit] Nexy","pid":39688}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1ef2c0, sessionType: 'prim', isRecording: false }, 
]
default	14:52:02.081537-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 0]. BT device UIDS: {(
)}
default	14:52:02.081561-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	14:52:02.081578-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:52:02.081671-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:52:02.081716-0500	audioaccessoryd	AudioStateChanged: Removed audio session app com.nexy.assistant 201 count 1
default	14:52:02.186425-0500	Nexy	                AUHAL.cpp:473   ~AUHAL: (0x7bf0a8e40) Selecting device 0 from destructor
default	14:52:02.186455-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0x7bf0a8e40)
default	14:52:02.186470-0500	Nexy	                AUHAL.cpp:676   SelectDevice: (0x7bf0a8e40) not already running
default	14:52:02.186485-0500	Nexy	                AUHAL.cpp:682   SelectDevice: (0x7bf0a8e40) disconnecting device 71
default	14:52:02.186501-0500	Nexy	                AUHAL.cpp:746   SelectDevice: (0x7bf0a8e40) destroying ioproc 0xc for device 71
default	14:52:02.186558-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Output {BuiltInSpeakerDevice, 0xc}
default	14:52:02.186630-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	14:52:02.186955-0500	Nexy	                AUHAL.cpp:848   SelectDevice: (0x7bf0a8e40) nothing to setup
default	14:52:02.186984-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x7bf0a8e40) adding 0 device listeners to device 0
default	14:52:02.186997-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x7bf0a8e40) adding 0 device delegate listeners to device 0
default	14:52:02.187011-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x7bf0a8e40) removing 7 device listeners from device 71
default	14:52:02.187522-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x7bf0a8e40) removing 0 device delegate listeners from device 71
default	14:52:02.187551-0500	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0x7bf0a8e40)
default	14:52:02.514209-0500	Nexy	FBSWorkspace registering source: <private>
default	14:52:02.514269-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	14:52:02.514425-0500	Nexy	<FBSWorkspaceScenesClient:0x7c0d34780 <private>> attempting immediate handshake from activate
default	14:52:02.514478-0500	Nexy	<FBSWorkspaceScenesClient:0x7c0d34780 <private>> sent handshake
default	14:52:02.514961-0500	Nexy	Requesting scene <FBSScene: 0x7c0d34d20; com.apple.controlcenter:0CC90B34-2E1C-49C8-BAF9-4EC080F291F6> from com.apple.controlcenter.statusitems
default	14:52:02.515389-0500	Nexy	Request for <FBSScene: 0x7c0d34d20; com.apple.controlcenter:0CC90B34-2E1C-49C8-BAF9-4EC080F291F6> complete!
default	14:52:02.515896-0500	Nexy	<FBSWorkspaceScenesClient:0x7c0d34780 <private>> was invalidated
default	14:52:02.515965-0500	Nexy	FBSWorkspace unregistering source: <private>
default	14:52:02.516064-0500	Nexy	FBSWorkspace registering source: <private>
default	14:52:02.516102-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	14:52:02.516195-0500	Nexy	<FBSWorkspaceScenesClient:0x7c0d34820 <private>> attempting immediate handshake from activate
default	14:52:02.516236-0500	Nexy	<FBSWorkspaceScenesClient:0x7c0d34820 <private>> sent handshake
error	14:52:02.516349-0500	Nexy	Error creating <FBSScene: 0x7c0d34d20; com.apple.controlcenter:0CC90B34-2E1C-49C8-BAF9-4EC080F291F6>: <NSError: 0x7bec078d0; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	14:52:02.516385-0500	Nexy	No scene exists for identity: com.apple.controlcenter:0CC90B34-2E1C-49C8-BAF9-4EC080F291F6
default	14:52:02.516510-0500	Nexy	Requesting scene <FBSScene: 0x7c0d34a00; com.apple.controlcenter:0CC90B34-2E1C-49C8-BAF9-4EC080F291F6-Aux[6]-NSStatusItemView> from com.apple.controlcenter.statusitems
default	14:52:02.516841-0500	Nexy	Request for <FBSScene: 0x7c0d34a00; com.apple.controlcenter:0CC90B34-2E1C-49C8-BAF9-4EC080F291F6-Aux[6]-NSStatusItemView> complete!
default	14:52:02.517122-0500	Nexy	<FBSWorkspaceScenesClient:0x7c0d34820 <private>> was invalidated
default	14:52:02.517174-0500	Nexy	FBSWorkspace unregistering source: <private>
error	14:52:02.517271-0500	Nexy	Error creating <FBSScene: 0x7c0d34a00; com.apple.controlcenter:0CC90B34-2E1C-49C8-BAF9-4EC080F291F6-Aux[6]-NSStatusItemView>: <NSError: 0x7bec07720; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	14:52:02.517304-0500	Nexy	No scene exists for identity: com.apple.controlcenter:0CC90B34-2E1C-49C8-BAF9-4EC080F291F6-Aux[6]-NSStatusItemView
default	14:52:02.517689-0500	Nexy	[com.apple.controlcenter:0CC90B34-2E1C-49C8-BAF9-4EC080F291F6-Aux[6]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
error	14:52:02.518079-0500	Nexy	scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	14:52:02.518111-0500	Nexy	[com.apple.controlcenter:0CC90B34-2E1C-49C8-BAF9-4EC080F291F6] No matching scene to invalidate for this identity.
error	14:52:02.518168-0500	Nexy	auxiliary scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	14:52:02.518198-0500	Nexy	[com.apple.controlcenter:0CC90B34-2E1C-49C8-BAF9-4EC080F291F6-Aux[6]-NSStatusItemView] No matching scene to invalidate for this identity.
error	14:52:02.518832-0500	Nexy	Unhandled disconnected scene <private>
error	14:52:02.518951-0500	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
error	14:52:02.519046-0500	Nexy	Unhandled disconnected auxiliary scene <private>
error	14:52:02.519110-0500	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
default	14:52:02.794503-0500	Nexy	                AUHAL.cpp:420   AUHAL: (0x7bf0a8e40) Selecting device 71 from constructor
default	14:52:02.794533-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0x7bf0a8e40)
default	14:52:02.794543-0500	Nexy	                AUHAL.cpp:676   SelectDevice: (0x7bf0a8e40) not already running
default	14:52:02.794552-0500	Nexy	                AUHAL.cpp:752   SelectDevice: (0x7bf0a8e40) nothing to teardown
default	14:52:02.794558-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0x7bf0a8e40) connecting device 71
default	14:52:02.794737-0500	Nexy	                AUHAL.cpp:3413  IsDeviceUsable: (0x7bf0a8e40) Device ID: 71 (Input:No | Output:Yes): true
default	14:52:02.794941-0500	Nexy	                AUHAL.cpp:769   SelectDevice: (0x7bf0a8e40) created ioproc 0xd for device 71
default	14:52:02.795120-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x7bf0a8e40) adding 7 device listeners to device 71
default	14:52:02.795435-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x7bf0a8e40) adding 0 device delegate listeners to device 71
default	14:52:02.795458-0500	Nexy	                AUHAL.cpp:1581  UpdateStreamFormats: -> (0x7bf0a8e40)
default	14:52:02.795618-0500	Nexy	                AUHAL.cpp:1677  UpdateStreamFormats: 
  output stream 0 [0x48]:  2 ch,  48000 Hz, Float32, interleaved
default	14:52:02.795633-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 1 output streams; not all mono
default	14:52:02.795644-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	14:52:02.795658-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 0 input streams; not all mono
default	14:52:02.795689-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	14:52:02.795851-0500	Nexy	                AUHAL.cpp:1771  UpdateStreamFormats: AUHAL(0x7bf0a8e40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	14:52:02.795869-0500	Nexy	                AUHAL.cpp:1777  UpdateStreamFormats: AUHAL(0x7bf0a8e40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	14:52:02.795876-0500	Nexy	                AUHAL.cpp:1787  UpdateStreamFormats: <-
default	14:52:02.795883-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x7bf0a8e40) removing 0 device listeners from device 0
default	14:52:02.795890-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x7bf0a8e40) removing 0 device delegate listeners from device 0
default	14:52:02.795896-0500	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0x7bf0a8e40)
default	14:52:02.795917-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Output stream enables: Stream 0 is DISABLED
default	14:52:02.796025-0500	Nexy	                AUHAL.cpp:2298  SetProperty: (0x7bf0a8e40) caller requesting device change from 71 to 78
default	14:52:02.796036-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0x7bf0a8e40)
default	14:52:02.796046-0500	Nexy	                AUHAL.cpp:676   SelectDevice: (0x7bf0a8e40) not already running
default	14:52:02.796051-0500	Nexy	                AUHAL.cpp:682   SelectDevice: (0x7bf0a8e40) disconnecting device 71
default	14:52:02.796058-0500	Nexy	                AUHAL.cpp:746   SelectDevice: (0x7bf0a8e40) destroying ioproc 0xd for device 71
default	14:52:02.796089-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped Unknown {BuiltInSpeakerDevice, 0xd}
default	14:52:02.796143-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	14:52:02.796267-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0x7bf0a8e40) connecting device 78
default	14:52:02.796411-0500	Nexy	                AUHAL.cpp:3413  IsDeviceUsable: (0x7bf0a8e40) Device ID: 78 (Input:Yes | Output:No): true
default	14:52:02.798763-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.11850, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=39688, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	14:52:02.800611-0500	tccd	AUTHREQ_SUBJECT: msgID=401.11850, subject=com.nexy.assistant,
default	14:52:02.801661-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc37138c00 at /Applications/Nexy.app
default	14:52:02.819642-0500	Nexy	                AUHAL.cpp:769   SelectDevice: (0x7bf0a8e40) created ioproc 0xb for device 78
default	14:52:02.819840-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x7bf0a8e40) adding 7 device listeners to device 78
default	14:52:02.820123-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x7bf0a8e40) adding 0 device delegate listeners to device 78
default	14:52:02.820135-0500	Nexy	                AUHAL.cpp:1581  UpdateStreamFormats: -> (0x7bf0a8e40)
default	14:52:02.820147-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 0 output streams; not all mono
default	14:52:02.820161-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Output render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	14:52:02.820363-0500	Nexy	                AUHAL.cpp:1677  UpdateStreamFormats: 
  input stream 0 [0x4f]:  1 ch,  48000 Hz, Float32
default	14:52:02.820372-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 1 input streams; all mono
default	14:52:02.820378-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Input render format:  1 ch,  48000 Hz, Float32
default	14:52:02.820518-0500	Nexy	                AUHAL.cpp:1771  UpdateStreamFormats: AUHAL(0x7bf0a8e40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	14:52:02.820532-0500	Nexy	                AUHAL.cpp:1777  UpdateStreamFormats: AUHAL(0x7bf0a8e40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	14:52:02.820539-0500	Nexy	                AUHAL.cpp:1787  UpdateStreamFormats: <-
default	14:52:02.820544-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x7bf0a8e40) removing 7 device listeners from device 71
default	14:52:02.820734-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x7bf0a8e40) removing 0 device delegate listeners from device 71
default	14:52:02.820744-0500	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0x7bf0a8e40)
default	14:52:02.821211-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	14:52:02.822815-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.11851, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=39688, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	14:52:02.824090-0500	tccd	AUTHREQ_SUBJECT: msgID=401.11851, subject=com.nexy.assistant,
default	14:52:02.824795-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc37138c00 at /Applications/Nexy.app
default	14:52:02.838764-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	14:52:02.839819-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.11852, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=39688, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	14:52:02.840678-0500	tccd	AUTHREQ_SUBJECT: msgID=401.11852, subject=com.nexy.assistant,
default	14:52:02.841227-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc37138c00 at /Applications/Nexy.app
default	14:52:02.854147-0500	Nexy	                AUHAL.cpp:473   ~AUHAL: (0x7bf0a8e40) Selecting device 0 from destructor
default	14:52:02.854154-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0x7bf0a8e40)
default	14:52:02.854166-0500	Nexy	                AUHAL.cpp:676   SelectDevice: (0x7bf0a8e40) not already running
default	14:52:02.854170-0500	Nexy	                AUHAL.cpp:682   SelectDevice: (0x7bf0a8e40) disconnecting device 78
default	14:52:02.854176-0500	Nexy	                AUHAL.cpp:746   SelectDevice: (0x7bf0a8e40) destroying ioproc 0xb for device 78
default	14:52:02.854201-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {BuiltInMicrophoneDevice, 0xb}
default	14:52:02.854232-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	14:52:02.854331-0500	Nexy	                AUHAL.cpp:848   SelectDevice: (0x7bf0a8e40) nothing to setup
default	14:52:02.854341-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x7bf0a8e40) adding 0 device listeners to device 0
default	14:52:02.854348-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x7bf0a8e40) adding 0 device delegate listeners to device 0
default	14:52:02.854352-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x7bf0a8e40) removing 7 device listeners from device 78
default	14:52:02.854526-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x7bf0a8e40) removing 0 device delegate listeners from device 78
default	14:52:02.854533-0500	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0x7bf0a8e40)
default	14:52:02.855479-0500	Nexy	                AUHAL.cpp:420   AUHAL: (0x7bf0a8e40) Selecting device 71 from constructor
default	14:52:02.855485-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0x7bf0a8e40)
default	14:52:02.855489-0500	Nexy	                AUHAL.cpp:676   SelectDevice: (0x7bf0a8e40) not already running
default	14:52:02.855494-0500	Nexy	                AUHAL.cpp:752   SelectDevice: (0x7bf0a8e40) nothing to teardown
default	14:52:02.855498-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0x7bf0a8e40) connecting device 71
default	14:52:02.855590-0500	Nexy	                AUHAL.cpp:3413  IsDeviceUsable: (0x7bf0a8e40) Device ID: 71 (Input:No | Output:Yes): true
default	14:52:02.855700-0500	Nexy	                AUHAL.cpp:769   SelectDevice: (0x7bf0a8e40) created ioproc 0xe for device 71
default	14:52:02.855834-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x7bf0a8e40) adding 7 device listeners to device 71
default	14:52:02.856010-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x7bf0a8e40) adding 0 device delegate listeners to device 71
default	14:52:02.856021-0500	Nexy	                AUHAL.cpp:1581  UpdateStreamFormats: -> (0x7bf0a8e40)
default	14:52:02.856093-0500	Nexy	                AUHAL.cpp:1677  UpdateStreamFormats: 
  output stream 0 [0x48]:  2 ch,  48000 Hz, Float32, interleaved
default	14:52:02.856102-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 1 output streams; not all mono
default	14:52:02.856107-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	14:52:02.856115-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 0 input streams; not all mono
default	14:52:02.856122-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	14:52:02.856228-0500	Nexy	                AUHAL.cpp:1771  UpdateStreamFormats: AUHAL(0x7bf0a8e40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	14:52:02.856244-0500	Nexy	                AUHAL.cpp:1777  UpdateStreamFormats: AUHAL(0x7bf0a8e40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	14:52:02.856250-0500	Nexy	                AUHAL.cpp:1787  UpdateStreamFormats: <-
default	14:52:02.856255-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x7bf0a8e40) removing 0 device listeners from device 0
default	14:52:02.856259-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x7bf0a8e40) removing 0 device delegate listeners from device 0
default	14:52:02.856262-0500	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0x7bf0a8e40)
default	14:52:02.856273-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Output stream enables: Stream 0 is DISABLED
default	14:52:02.856348-0500	Nexy	                AUHAL.cpp:2298  SetProperty: (0x7bf0a8e40) caller requesting device change from 71 to 78
default	14:52:02.856359-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0x7bf0a8e40)
default	14:52:02.856364-0500	Nexy	                AUHAL.cpp:676   SelectDevice: (0x7bf0a8e40) not already running
default	14:52:02.856369-0500	Nexy	                AUHAL.cpp:682   SelectDevice: (0x7bf0a8e40) disconnecting device 71
default	14:52:02.856379-0500	Nexy	                AUHAL.cpp:746   SelectDevice: (0x7bf0a8e40) destroying ioproc 0xe for device 71
default	14:52:02.856391-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped Unknown {BuiltInSpeakerDevice, 0xe}
default	14:52:02.856432-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	14:52:02.856523-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0x7bf0a8e40) connecting device 78
default	14:52:02.856595-0500	Nexy	                AUHAL.cpp:3413  IsDeviceUsable: (0x7bf0a8e40) Device ID: 78 (Input:Yes | Output:No): true
default	14:52:02.857579-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.11853, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=39688, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	14:52:02.858422-0500	tccd	AUTHREQ_SUBJECT: msgID=401.11853, subject=com.nexy.assistant,
default	14:52:02.858972-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc37138c00 at /Applications/Nexy.app
default	14:52:02.870907-0500	Nexy	                AUHAL.cpp:769   SelectDevice: (0x7bf0a8e40) created ioproc 0xc for device 78
default	14:52:02.871011-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x7bf0a8e40) adding 7 device listeners to device 78
default	14:52:02.871156-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x7bf0a8e40) adding 0 device delegate listeners to device 78
default	14:52:02.871164-0500	Nexy	                AUHAL.cpp:1581  UpdateStreamFormats: -> (0x7bf0a8e40)
default	14:52:02.871170-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 0 output streams; not all mono
default	14:52:02.871179-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Output render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	14:52:02.871304-0500	Nexy	                AUHAL.cpp:1677  UpdateStreamFormats: 
  input stream 0 [0x4f]:  1 ch,  48000 Hz, Float32
default	14:52:02.871315-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 1 input streams; all mono
default	14:52:02.871321-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Input render format:  1 ch,  48000 Hz, Float32
default	14:52:02.871416-0500	Nexy	                AUHAL.cpp:1771  UpdateStreamFormats: AUHAL(0x7bf0a8e40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	14:52:02.871426-0500	Nexy	                AUHAL.cpp:1777  UpdateStreamFormats: AUHAL(0x7bf0a8e40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	14:52:02.871432-0500	Nexy	                AUHAL.cpp:1787  UpdateStreamFormats: <-
default	14:52:02.871436-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x7bf0a8e40) removing 7 device listeners from device 71
default	14:52:02.871592-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x7bf0a8e40) removing 0 device delegate listeners from device 71
default	14:52:02.871599-0500	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0x7bf0a8e40)
default	14:52:02.871606-0500	Nexy	AudioHardware-mac-imp.cpp:1299   AudioObjectAddPropertyListener: listener was already added
default	14:52:02.871988-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	14:52:02.872883-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.11854, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=39688, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	14:52:02.873636-0500	tccd	AUTHREQ_SUBJECT: msgID=401.11854, subject=com.nexy.assistant,
default	14:52:02.874174-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc37138c00 at /Applications/Nexy.app
default	14:52:02.885925-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	14:52:02.886938-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.11855, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=39688, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	14:52:02.887826-0500	tccd	AUTHREQ_SUBJECT: msgID=401.11855, subject=com.nexy.assistant,
default	14:52:02.888396-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc37138c00 at /Applications/Nexy.app
default	14:52:02.900933-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	14:52:02.901845-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.11856, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=39688, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	14:52:02.902600-0500	tccd	AUTHREQ_SUBJECT: msgID=401.11856, subject=com.nexy.assistant,
default	14:52:02.903135-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc37138c00 at /Applications/Nexy.app
default	14:52:02.915857-0500	runningboardd	ignoring [app<application.com.nexy.assistant.21074037.21074043(501)>:39688] as candidate for concrete target as it is terminating
default	14:52:02.915915-0500	runningboardd	Acquiring assertion targeting 39688 from originator [app<application.com.nexy.assistant.21074037.21074043(501)>:39688] with description <RBSAssertionDescriptor| "AudioHAL" ID:398-39688-1518829 target:39688 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
error	14:52:02.916182-0500	Nexy	Error acquiring assertion: <Error Domain=RBSAssertionErrorDomain Code=2 "Specified target process 39688 does not exist" UserInfo={NSLocalizedFailureReason=Specified target process 39688 does not exist}>
error	14:52:02.916198-0500	Nexy	          HALRBSAssertionGlue.mm:98    Failed to acquire the AudioHAL RBSAssertion for pid: 39688 with code: 2 - RBSAssertionErrorDomain
default	14:52:02.916507-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.11857, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=39688, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	14:52:02.917247-0500	tccd	AUTHREQ_SUBJECT: msgID=401.11857, subject=com.nexy.assistant,
default	14:52:02.917757-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc37138c00 at /Applications/Nexy.app
default	14:52:02.931396-0500	runningboardd	ignoring [app<application.com.nexy.assistant.21074037.21074043(501)>:39688] as candidate for concrete target as it is terminating
default	14:52:02.956315-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Input {BuiltInMicrophoneDevice, 0xc}
default	14:52:02.957174-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ef2c0","name":"Nexy(39688)"}, "details":{"deviceUIDs":[],"implicit_category":"Record","input_running":true,"output_running":false} }
default	14:52:02.957271-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 705, PID = 39688, Name = sid:0x1ef2c0, Nexy(39688), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	14:52:02.957304-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Category/Mode changed -- The score for sid:0x1ef2c0, Nexy(39688), 'prim'/com.nexy.assistant was not correct. Old score = 201
default	14:52:02.957335-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 705, PID = 39688, Name = sid:0x1ef2c0, Nexy(39688), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	14:52:02.957393-0500	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1ef2c0, Nexy(39688), 'prim'', AudioCategory changed to 'Record_WithBluetooth'
default	14:52:02.957432-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:52:02.957444-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 705, PID = 39688, Name = sid:0x1ef2c0, Nexy(39688), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	14:52:02.957479-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 705, PID = 39688, Name = sid:0x1ef2c0, Nexy(39688), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	14:52:02.957535-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:52:02.957547-0500	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 705, PID = 39688, Name = sid:0x1ef2c0, Nexy(39688), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> is going active
default	14:52:02.957562-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1ef2c0, Nexy(39688), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 705 starting recording
default	14:52:02.957600-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:52:02.957642-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 705, PID = 39688, Name = sid:0x1ef2c0, Nexy(39688), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	14:52:02.957655-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:52:02.957674-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 705, PID = 39688, Name = sid:0x1ef2c0, Nexy(39688), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	14:52:02.957706-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1ef2c0, Nexy(39688), 'prim'', displayID:'com.nexy.assistant'}
default	14:52:02.957717-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:52:02.957772-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	14:52:02.957801-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [1, 0]. BT device UIDS: {(
)}
default	14:52:02.957809-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	14:52:02.957833-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:52:02.957879-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	14:52:02.957916-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	14:52:02.957931-0500	audioaccessoryd	AudioStateChanged: Added audio session app com.nexy.assistant NULL -> 200 count 2
default	14:52:02.957942-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
error	14:52:02.957966-0500	audioaccessoryd	Updating local audio category 100 -> 200 app com.nexy.assistant
default	14:52:02.958002-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	14:52:02.997335-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	14:52:03.004312-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	14:52:03.004467-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant), [mic] Nexy (com.nexy.assistant)]
default	14:52:03.004575-0500	ControlCenter	Active activity attributions changed to ["scr:com.nexy.assistant", "mic:com.nexy.assistant"]
default	14:52:03.006223-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:52:03.006247-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:52:03.006264-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	14:52:03.006275-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:52:03.006287-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	14:52:03.006299-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	14:52:03.006411-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:52:03.006462-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:52:03.006520-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	14:52:03.006566-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:52:03.006620-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	14:52:03.006612-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	14:52:03.006660-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	14:52:03.006735-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:52:03.006747-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:52:03.006759-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	14:52:03.006768-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:52:03.006778-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	14:52:03.006788-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	14:52:03.006910-0500	ControlCenter	Navigating to new application [com.nexy.assistant]
default	14:52:03.084863-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {BuiltInMicrophoneDevice, 0xc}
default	14:52:03.085283-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ef2c0","name":"Nexy(39688)"}, "details":{"deviceUIDs":[],"implicit_category":"","input_running":false,"output_running":false} }
default	14:52:03.085410-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 705, PID = 39688, Name = sid:0x1ef2c0, Nexy(39688), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	14:52:03.085470-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 705, PID = 39688, Name = sid:0x1ef2c0, Nexy(39688), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	14:52:03.085505-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1ef2c0, Nexy(39688), 'prim'', displayID:'com.nexy.assistant'}
default	14:52:03.085576-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1ef2c0, Nexy(39688), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 705 stopping recording
default	14:52:03.085618-0500	audiomxd	-MXCoreSession- -[MXCoreSession endInterruption:]: Session <ID: 705, PID = 39688, Name = sid:0x1ef2c0, Nexy(39688), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> is going inactive
default	14:52:03.085633-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	14:52:03.085655-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 705, PID = 39688, Name = sid:0x1ef2c0, Nexy(39688), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	14:52:03.085700-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 705, PID = 39688, Name = sid:0x1ef2c0, Nexy(39688), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	14:52:03.085769-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:52:03.085833-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	14:52:03.085869-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 0]. BT device UIDS: {(
)}
default	14:52:03.085897-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	14:52:03.085891-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	14:52:03.085937-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	14:52:03.086026-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:52:03.086062-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	14:52:03.086091-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:52:03.086110-0500	audioaccessoryd	AudioStateChanged: Removed audio session app com.nexy.assistant 201 count 1
default	14:52:03.133398-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	14:52:03.133513-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant)]
default	14:52:03.133590-0500	ControlCenter	Active activity attributions changed to ["scr:com.nexy.assistant"]
default	14:52:03.133611-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	14:52:03.138686-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:52:03.138704-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:52:03.138731-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	14:52:03.138748-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:52:03.138766-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	14:52:03.138803-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	14:52:03.139023-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	14:52:03.191129-0500	Nexy	                AUHAL.cpp:473   ~AUHAL: (0x7bf0a8e40) Selecting device 0 from destructor
default	14:52:03.191164-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0x7bf0a8e40)
default	14:52:03.191176-0500	Nexy	                AUHAL.cpp:676   SelectDevice: (0x7bf0a8e40) not already running
default	14:52:03.191188-0500	Nexy	                AUHAL.cpp:682   SelectDevice: (0x7bf0a8e40) disconnecting device 78
default	14:52:03.191211-0500	Nexy	                AUHAL.cpp:746   SelectDevice: (0x7bf0a8e40) destroying ioproc 0xc for device 78
default	14:52:03.191271-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {BuiltInMicrophoneDevice, 0xc}
default	14:52:03.191332-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	14:52:03.191555-0500	Nexy	                AUHAL.cpp:848   SelectDevice: (0x7bf0a8e40) nothing to setup
default	14:52:03.191570-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x7bf0a8e40) adding 0 device listeners to device 0
default	14:52:03.191576-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x7bf0a8e40) adding 0 device delegate listeners to device 0
default	14:52:03.191584-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x7bf0a8e40) removing 7 device listeners from device 78
default	14:52:03.191824-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x7bf0a8e40) removing 0 device delegate listeners from device 78
default	14:52:03.191839-0500	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0x7bf0a8e40)
default	14:52:03.195624-0500	Nexy	                AUHAL.cpp:420   AUHAL: (0x7bf0a8e40) Selecting device 71 from constructor
default	14:52:03.195647-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0x7bf0a8e40)
default	14:52:03.195666-0500	Nexy	                AUHAL.cpp:676   SelectDevice: (0x7bf0a8e40) not already running
default	14:52:03.195674-0500	Nexy	                AUHAL.cpp:752   SelectDevice: (0x7bf0a8e40) nothing to teardown
default	14:52:03.195686-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0x7bf0a8e40) connecting device 71
default	14:52:03.195875-0500	Nexy	                AUHAL.cpp:3413  IsDeviceUsable: (0x7bf0a8e40) Device ID: 71 (Input:No | Output:Yes): true
default	14:52:03.196108-0500	Nexy	                AUHAL.cpp:769   SelectDevice: (0x7bf0a8e40) created ioproc 0xf for device 71
default	14:52:03.196341-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x7bf0a8e40) adding 7 device listeners to device 71
default	14:52:03.196710-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x7bf0a8e40) adding 0 device delegate listeners to device 71
default	14:52:03.196728-0500	Nexy	                AUHAL.cpp:1581  UpdateStreamFormats: -> (0x7bf0a8e40)
default	14:52:03.196880-0500	Nexy	                AUHAL.cpp:1677  UpdateStreamFormats: 
  output stream 0 [0x48]:  2 ch,  48000 Hz, Float32, interleaved
default	14:52:03.196899-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 1 output streams; not all mono
default	14:52:03.196913-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	14:52:03.196927-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 0 input streams; not all mono
default	14:52:03.196944-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	14:52:03.197133-0500	Nexy	                AUHAL.cpp:1771  UpdateStreamFormats: AUHAL(0x7bf0a8e40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	14:52:03.197154-0500	Nexy	                AUHAL.cpp:1777  UpdateStreamFormats: AUHAL(0x7bf0a8e40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	14:52:03.197166-0500	Nexy	                AUHAL.cpp:1787  UpdateStreamFormats: <-
default	14:52:03.197176-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x7bf0a8e40) removing 0 device listeners from device 0
default	14:52:03.197185-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x7bf0a8e40) removing 0 device delegate listeners from device 0
default	14:52:03.197192-0500	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0x7bf0a8e40)
default	14:52:03.197221-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Output stream enables: Stream 0 is DISABLED
default	14:52:03.197350-0500	Nexy	                AUHAL.cpp:2298  SetProperty: (0x7bf0a8e40) caller requesting device change from 71 to 78
default	14:52:03.197370-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0x7bf0a8e40)
default	14:52:03.197381-0500	Nexy	                AUHAL.cpp:676   SelectDevice: (0x7bf0a8e40) not already running
default	14:52:03.197391-0500	Nexy	                AUHAL.cpp:682   SelectDevice: (0x7bf0a8e40) disconnecting device 71
default	14:52:03.197401-0500	Nexy	                AUHAL.cpp:746   SelectDevice: (0x7bf0a8e40) destroying ioproc 0xf for device 71
default	14:52:03.197429-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped Unknown {BuiltInSpeakerDevice, 0xf}
default	14:52:03.197489-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	14:52:03.197654-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0x7bf0a8e40) connecting device 78
default	14:52:03.197834-0500	Nexy	                AUHAL.cpp:3413  IsDeviceUsable: (0x7bf0a8e40) Device ID: 78 (Input:Yes | Output:No): true
default	14:52:03.200083-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.11858, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=39688, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	14:52:03.201864-0500	tccd	AUTHREQ_SUBJECT: msgID=401.11858, subject=com.nexy.assistant,
default	14:52:03.202541-0500	Nexy	                AUHAL.cpp:420   AUHAL: (0x7bf0a9540) Selecting device 71 from constructor
default	14:52:03.202562-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0x7bf0a9540)
default	14:52:03.202569-0500	Nexy	                AUHAL.cpp:676   SelectDevice: (0x7bf0a9540) not already running
default	14:52:03.202575-0500	Nexy	                AUHAL.cpp:752   SelectDevice: (0x7bf0a9540) nothing to teardown
default	14:52:03.202581-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0x7bf0a9540) connecting device 71
default	14:52:03.202699-0500	Nexy	                AUHAL.cpp:3413  IsDeviceUsable: (0x7bf0a9540) Device ID: 71 (Input:No | Output:Yes): true
default	14:52:03.202852-0500	Nexy	                AUHAL.cpp:769   SelectDevice: (0x7bf0a9540) created ioproc 0x10 for device 71
default	14:52:03.202879-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc37138c00 at /Applications/Nexy.app
default	14:52:03.202980-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x7bf0a9540) adding 7 device listeners to device 71
default	14:52:03.203192-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x7bf0a9540) adding 0 device delegate listeners to device 71
default	14:52:03.203202-0500	Nexy	                AUHAL.cpp:1581  UpdateStreamFormats: -> (0x7bf0a9540)
default	14:52:03.203305-0500	Nexy	                AUHAL.cpp:1677  UpdateStreamFormats: 
  output stream 0 [0x48]:  2 ch,  48000 Hz, Float32, interleaved
default	14:52:03.203315-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 1 output streams; not all mono
default	14:52:03.203324-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	14:52:03.203335-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 0 input streams; not all mono
default	14:52:03.203345-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	14:52:03.203457-0500	Nexy	                AUHAL.cpp:1771  UpdateStreamFormats: AUHAL(0x7bf0a9540) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	14:52:03.203473-0500	Nexy	                AUHAL.cpp:1777  UpdateStreamFormats: AUHAL(0x7bf0a9540) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	14:52:03.203480-0500	Nexy	                AUHAL.cpp:1787  UpdateStreamFormats: <-
default	14:52:03.203485-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x7bf0a9540) removing 0 device listeners from device 0
default	14:52:03.203490-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x7bf0a9540) removing 0 device delegate listeners from device 0
default	14:52:03.203495-0500	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0x7bf0a9540)
default	14:52:03.203511-0500	Nexy	                AUHAL.cpp:2298  SetProperty: (0x7bf0a9540) caller requesting device change from 71 to 71
default	14:52:03.203516-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0x7bf0a9540)
default	14:52:03.203522-0500	Nexy	                AUHAL.cpp:659   SelectDevice: <- (0x7bf0a9540) exiting with nothing to do
default	14:52:03.203530-0500	Nexy	AudioHardware-mac-imp.cpp:1299   AudioObjectAddPropertyListener: listener was already added
default	14:52:03.203963-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	14:52:03.204252-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	14:52:03.209158-0500	runningboardd	ignoring [app<application.com.nexy.assistant.21074037.21074043(501)>:39688] as candidate for concrete target as it is terminating
default	14:52:03.209233-0500	runningboardd	Acquiring assertion targeting 39688 from originator [app<application.com.nexy.assistant.21074037.21074043(501)>:39688] with description <RBSAssertionDescriptor| "AudioHAL" ID:398-39688-1518831 target:39688 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
error	14:52:03.210791-0500	Nexy	Error acquiring assertion: <Error Domain=RBSAssertionErrorDomain Code=2 "Specified target process 39688 does not exist" UserInfo={NSLocalizedFailureReason=Specified target process 39688 does not exist}>
default	14:52:03.210906-0500	runningboardd	ignoring [app<application.com.nexy.assistant.21074037.21074043(501)>:39688] as candidate for concrete target as it is terminating
error	14:52:03.210835-0500	Nexy	          HALRBSAssertionGlue.mm:98    Failed to acquire the AudioHAL RBSAssertion for pid: 39688 with code: 2 - RBSAssertionErrorDomain
default	14:52:03.229943-0500	Nexy	                AUHAL.cpp:769   SelectDevice: (0x7bf0a8e40) created ioproc 0xd for device 78
default	14:52:03.230114-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x7bf0a8e40) adding 7 device listeners to device 78
default	14:52:03.230340-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x7bf0a8e40) adding 0 device delegate listeners to device 78
default	14:52:03.230350-0500	Nexy	                AUHAL.cpp:1581  UpdateStreamFormats: -> (0x7bf0a8e40)
default	14:52:03.230362-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 0 output streams; not all mono
default	14:52:03.230385-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Output render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	14:52:03.230566-0500	Nexy	                AUHAL.cpp:1677  UpdateStreamFormats: 
  input stream 0 [0x4f]:  1 ch,  48000 Hz, Float32
default	14:52:03.230581-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 1 input streams; all mono
default	14:52:03.230588-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Input render format:  1 ch,  48000 Hz, Float32
default	14:52:03.230717-0500	Nexy	                AUHAL.cpp:1771  UpdateStreamFormats: AUHAL(0x7bf0a8e40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	14:52:03.230737-0500	Nexy	                AUHAL.cpp:1777  UpdateStreamFormats: AUHAL(0x7bf0a8e40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	14:52:03.230746-0500	Nexy	                AUHAL.cpp:1787  UpdateStreamFormats: <-
default	14:52:03.230751-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x7bf0a8e40) removing 7 device listeners from device 71
default	14:52:03.230948-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x7bf0a8e40) removing 0 device delegate listeners from device 71
default	14:52:03.230958-0500	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0x7bf0a8e40)
default	14:52:03.230972-0500	Nexy	AudioHardware-mac-imp.cpp:1299   AudioObjectAddPropertyListener: listener was already added
default	14:52:03.231457-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	14:52:03.232973-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.11859, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=39688, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	14:52:03.234190-0500	tccd	AUTHREQ_SUBJECT: msgID=401.11859, subject=com.nexy.assistant,
default	14:52:03.234848-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc37138c00 at /Applications/Nexy.app
default	14:52:03.235517-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {BuiltInSpeakerDevice, 0x10}
default	14:52:03.236445-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ef2c0","name":"Nexy(39688)"}, "details":{"deviceUIDs":[],"implicit_category":"MediaPlayback","input_running":false,"output_running":true} }
default	14:52:03.236552-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 705, PID = 39688, Name = sid:0x1ef2c0, Nexy(39688), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	14:52:03.236579-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Category/Mode changed -- The score for sid:0x1ef2c0, Nexy(39688), 'prim'/com.nexy.assistant was not correct. Old score = 201
default	14:52:03.236617-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 705, PID = 39688, Name = sid:0x1ef2c0, Nexy(39688), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	14:52:03.236680-0500	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1ef2c0, Nexy(39688), 'prim'', AudioCategory changed to 'MediaPlayback'
default	14:52:03.236732-0500	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 705, PID = 39688, Name = sid:0x1ef2c0, Nexy(39688), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO> is going active
default	14:52:03.236732-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:52:03.236747-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsPlaying:]: MXCoreSession com.nexy.assistant with category/mode MediaPlayback/Default and coreSessionID = 705 starting playing
default	14:52:03.236825-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 705, PID = 39688, Name = sid:0x1ef2c0, Nexy(39688), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	14:52:03.236864-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 705, PID = 39688, Name = sid:0x1ef2c0, Nexy(39688), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO>
default	14:52:03.236892-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1ef2c0, Nexy(39688), 'prim'', displayID:'com.nexy.assistant'}
default	14:52:03.236921-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Will try to see if we can get the shared route for session = <ID: 705, PID = 39688, Name = sid:0x1ef2c0, Nexy(39688), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO>. Old (200) and New (201) scores.
default	14:52:03.236915-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:52:03.236985-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:52:03.236974-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 201, deviceID = <private>
default	14:52:03.237001-0500	audiomxd	AudioApplicationInfoImpl.mm:395   Successfully updated session 0x1ef2c0 to isSessionRecording: 0
	app: {"name":"[implicit] Nexy","pid":39688}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1ef2c0, sessionType: 'prim', isRecording: false }, 
]
default	14:52:03.237071-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 1]. BT device UIDS: {(
)}
default	14:52:03.237087-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	14:52:03.237220-0500	audioaccessoryd	Routing request Wx NULL score 201 flag 0x1 < Hijack > app com.nexy.assistant CID 0xD310001 category Not set
default	14:52:03.237392-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	14:52:03.237474-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 201,
}
default	14:52:03.237503-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	14:52:03.237517-0500	audioaccessoryd	AudioStateChanged: Added audio session app com.nexy.assistant NULL -> 201 count 2
default	14:52:03.237528-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 201
error	14:52:03.237550-0500	audioaccessoryd	Updating local audio category 100 -> 201 app com.nexy.assistant
default	14:52:03.237588-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.nexy.assistant
default	14:52:03.248975-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	14:52:03.250077-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.11860, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=39688, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	14:52:03.251014-0500	tccd	AUTHREQ_SUBJECT: msgID=401.11860, subject=com.nexy.assistant,
default	14:52:03.251593-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc37138c00 at /Applications/Nexy.app
default	14:52:03.264256-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	14:52:03.265216-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.11861, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=39688, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	14:52:03.266052-0500	tccd	AUTHREQ_SUBJECT: msgID=401.11861, subject=com.nexy.assistant,
default	14:52:03.266603-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc37138c00 at /Applications/Nexy.app
default	14:52:03.279387-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.11862, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=39688, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	14:52:03.280127-0500	tccd	AUTHREQ_SUBJECT: msgID=401.11862, subject=com.nexy.assistant,
default	14:52:03.280632-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc37138c00 at /Applications/Nexy.app
default	14:52:03.319149-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Input {BuiltInMicrophoneDevice, 0xd}
default	14:52:03.320310-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ef2c0","name":"Nexy(39688)"}, "details":{"deviceUIDs":[],"implicit_category":"PlayAndRecord","input_running":true,"output_running":true} }
default	14:52:03.320396-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 705, PID = 39688, Name = sid:0x1ef2c0, Nexy(39688), 'prim', BundleID = com.nexy.assistant, Category = PlayAndRecord_WithBluetooth, Mode = Default, Active = YES, Playing = YES, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	14:52:03.320425-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Category/Mode changed -- The score for sid:0x1ef2c0, Nexy(39688), 'prim'/com.nexy.assistant was not correct. Old score = 201
default	14:52:03.320452-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 705, PID = 39688, Name = sid:0x1ef2c0, Nexy(39688), 'prim', BundleID = com.nexy.assistant, Category = PlayAndRecord_WithBluetooth, Mode = Default, Active = YES, Playing = YES, Recording = NO>
default	14:52:03.320477-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1ef2c0, Nexy(39688), 'prim'', displayID:'com.nexy.assistant'}
default	14:52:03.320528-0500	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1ef2c0, Nexy(39688), 'prim'', AudioCategory changed to 'PlayAndRecord_WithBluetooth'
default	14:52:03.320554-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 705, PID = 39688, Name = sid:0x1ef2c0, Nexy(39688), 'prim', BundleID = com.nexy.assistant, Category = PlayAndRecord_WithBluetooth, Mode = Default, Active = YES, Playing = YES, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	14:52:03.320579-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	14:52:03.320595-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 705, PID = 39688, Name = sid:0x1ef2c0, Nexy(39688), 'prim', BundleID = com.nexy.assistant, Category = PlayAndRecord_WithBluetooth, Mode = Default, Active = YES, Playing = YES, Recording = NO>
default	14:52:03.320621-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1ef2c0, Nexy(39688), 'prim'', displayID:'com.nexy.assistant'}
default	14:52:03.320674-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 705, PID = 39688, Name = sid:0x1ef2c0, Nexy(39688), 'prim', BundleID = com.nexy.assistant, Category = PlayAndRecord_WithBluetooth, Mode = Default, Active = YES, Playing = YES, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	14:52:03.320691-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	14:52:03.320705-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 705, PID = 39688, Name = sid:0x1ef2c0, Nexy(39688), 'prim', BundleID = com.nexy.assistant, Category = PlayAndRecord_WithBluetooth, Mode = Default, Active = YES, Playing = YES, Recording = NO>
default	14:52:03.320730-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1ef2c0, Nexy(39688), 'prim'', displayID:'com.nexy.assistant'}
default	14:52:03.320741-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 201,
}
default	14:52:03.320775-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1ef2c0, Nexy(39688), 'prim' with category(PlayAndRecord_WithBluetooth)/mode(Default) and coreSessionID = 705 starting recording
default	14:52:03.320796-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	14:52:03.320794-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	14:52:03.320827-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: Bumping the mode to Voice chat for session as session started recording = <ID: 705, PID = 39688, Name = sid:0x1ef2c0, Nexy(39688), 'prim', BundleID = com.nexy.assistant, Category = PlayAndRecord_WithBluetooth, Mode = Default, Active = YES, Playing = YES, Recording = YES>
default	14:52:03.320831-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 201
default	14:52:03.320852-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 705, PID = 39688, Name = sid:0x1ef2c0, Nexy(39688), 'prim', BundleID = com.nexy.assistant, Category = PlayAndRecord_WithBluetooth, Mode = VoiceChat, Active = YES, Playing = YES, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	14:52:03.320875-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Category/Mode changed -- The score for sid:0x1ef2c0, Nexy(39688), 'prim'/com.nexy.assistant was not correct. Old score = 201
default	14:52:03.320899-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 501 for session <ID: 705, PID = 39688, Name = sid:0x1ef2c0, Nexy(39688), 'prim', BundleID = com.nexy.assistant, Category = PlayAndRecord_WithBluetooth, Mode = VoiceChat, Active = YES, Playing = YES, Recording = YES>
default	14:52:03.320909-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 201,
}
default	14:52:03.320940-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.nexy.assistant
default	14:52:03.320955-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 201,
}
default	14:52:03.320977-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	14:52:03.320916-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1ef2c0, Nexy(39688), 'prim'', displayID:'com.nexy.assistant'}
default	14:52:03.320996-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 201
default	14:52:03.321011-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [1, 1]. BT device UIDS: {(
)}
default	14:52:03.321019-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	14:52:03.320935-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Will try to see if we can get the shared route for session = <ID: 705, PID = 39688, Name = sid:0x1ef2c0, Nexy(39688), 'prim', BundleID = com.nexy.assistant, Category = PlayAndRecord_WithBluetooth, Mode = VoiceChat, Active = YES, Playing = YES, Recording = YES>. Old (201) and New (501) scores.
default	14:52:03.321042-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.nexy.assistant
default	14:52:03.321060-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	14:52:03.320986-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 501, deviceID = <private>
default	14:52:03.321068-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 201
default	14:52:03.321098-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.nexy.assistant
default	14:52:03.321178-0500	audioaccessoryd	Routing request Wx NULL score 501 flag 0x1 < Hijack > app com.nexy.assistant CID 0xD310001 category Not set
default	14:52:03.321320-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Start apps {
    "com.nexy.assistant" : 501,
}
default	14:52:03.321382-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 501,
}
default	14:52:03.321403-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 501,
}
default	14:52:03.321414-0500	audioaccessoryd	AudioStateChanged: Added audio session app com.nexy.assistant 201 -> 501 count 2
default	14:52:03.321420-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 501
error	14:52:03.321436-0500	audioaccessoryd	Updating local audio category 201 -> 501 app com.nexy.assistant
default	14:52:03.321463-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 501 App com.nexy.assistant
default	14:52:03.355707-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	14:52:03.362948-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	14:52:03.363112-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant), [mic] Nexy (com.nexy.assistant)]
default	14:52:03.363199-0500	ControlCenter	Active activity attributions changed to ["scr:com.nexy.assistant", "mic:com.nexy.assistant"]
default	14:52:03.364165-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:52:03.364185-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:52:03.364202-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	14:52:03.364212-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:52:03.364223-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	14:52:03.364234-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	14:52:03.364356-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:52:03.364371-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	14:52:03.364418-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:52:03.364473-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	14:52:03.364512-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:52:03.364553-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	14:52:03.364592-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	14:52:03.364665-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:52:03.364698-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:52:03.364712-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	14:52:03.364728-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:52:03.364737-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	14:52:03.364746-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	14:52:03.364814-0500	ControlCenter	Navigating to new application [com.nexy.assistant]
default	14:52:03.481817-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Output {BuiltInSpeakerDevice, 0x10}
default	14:52:03.483305-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ef2c0","name":"Nexy(39688)"}, "details":{"deviceUIDs":[],"implicit_category":"Record","input_running":true,"output_running":false} }
default	14:52:03.483504-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 705, PID = 39688, Name = sid:0x1ef2c0, Nexy(39688), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = YES, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	14:52:03.483557-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Category/Mode changed -- The score for sid:0x1ef2c0, Nexy(39688), 'prim'/com.nexy.assistant was not correct. Old score = 501
default	14:52:03.483639-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 705, PID = 39688, Name = sid:0x1ef2c0, Nexy(39688), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = YES, Recording = YES>
default	14:52:03.483690-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1ef2c0, Nexy(39688), 'prim'', displayID:'com.nexy.assistant'}
default	14:52:03.483771-0500	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1ef2c0, Nexy(39688), 'prim'', AudioCategory changed to 'Record_WithBluetooth'
default	14:52:03.483807-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	14:52:03.483840-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 705, PID = 39688, Name = sid:0x1ef2c0, Nexy(39688), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = YES, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	14:52:03.483894-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 705, PID = 39688, Name = sid:0x1ef2c0, Nexy(39688), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = YES, Recording = YES>
default	14:52:03.483931-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1ef2c0, Nexy(39688), 'prim'', displayID:'com.nexy.assistant'}
default	14:52:03.484004-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsPlaying:]: MXCoreSession com.nexy.assistant with category/mode Record_WithBluetooth/Default and coreSessionID = 705 stopping playing
default	14:52:03.484009-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	14:52:03.484050-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	14:52:03.484124-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	14:52:03.484055-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 705, PID = 39688, Name = sid:0x1ef2c0, Nexy(39688), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	14:52:03.484157-0500	audioaccessoryd	AudioStateChanged: Added audio session app com.nexy.assistant 501 -> 200 count 2
default	14:52:03.484102-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 705, PID = 39688, Name = sid:0x1ef2c0, Nexy(39688), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	14:52:03.484184-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	14:52:03.484148-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1ef2c0, Nexy(39688), 'prim'', displayID:'com.nexy.assistant'}
error	14:52:03.484230-0500	audioaccessoryd	Updating local audio category 501 -> 200 app com.nexy.assistant
default	14:52:03.484260-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	14:52:03.484348-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	14:52:03.484441-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [1, 0]. BT device UIDS: {(
)}
default	14:52:03.484374-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	14:52:03.484471-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	14:52:03.484394-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	14:52:03.484220-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	14:52:03.484303-0500	audiomxd	AudioApplicationInfoImpl.mm:395   Successfully updated session 0x1ef2c0 to isSessionRecording: 1
	app: {"name":"[implicit] Nexy","pid":39688}
	AudioApp.isRecording: true
[ 
	{ sessionID: 0x1ef2c0, sessionType: 'prim', isRecording: true }, 
]
default	14:52:03.484473-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	14:52:03.484503-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	14:52:03.484527-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	14:52:03.484543-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	14:52:03.484724-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	14:52:03.519495-0500	Nexy	FBSWorkspace registering source: <private>
default	14:52:03.519543-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	14:52:03.519654-0500	Nexy	<FBSWorkspaceScenesClient:0x7c0d34820 <private>> attempting immediate handshake from activate
default	14:52:03.519696-0500	Nexy	<FBSWorkspaceScenesClient:0x7c0d34820 <private>> sent handshake
default	14:52:03.520070-0500	Nexy	Requesting scene <FBSScene: 0x7c0d34d20; com.apple.controlcenter:29AEB987-FF8D-453E-9C9D-FF77F4D5B4B2> from com.apple.controlcenter.statusitems
default	14:52:03.520384-0500	Nexy	Request for <FBSScene: 0x7c0d34d20; com.apple.controlcenter:29AEB987-FF8D-453E-9C9D-FF77F4D5B4B2> complete!
default	14:52:03.520845-0500	Nexy	<FBSWorkspaceScenesClient:0x7c0d34820 <private>> was invalidated
default	14:52:03.520881-0500	Nexy	FBSWorkspace unregistering source: <private>
error	14:52:03.520998-0500	Nexy	Error creating <FBSScene: 0x7c0d34d20; com.apple.controlcenter:29AEB987-FF8D-453E-9C9D-FF77F4D5B4B2>: <NSError: 0x7bec07e10; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	14:52:03.521022-0500	Nexy	No scene exists for identity: com.apple.controlcenter:29AEB987-FF8D-453E-9C9D-FF77F4D5B4B2
default	14:52:03.521064-0500	Nexy	Requesting scene <FBSScene: 0x7c0d34a00; com.apple.controlcenter:29AEB987-FF8D-453E-9C9D-FF77F4D5B4B2-Aux[7]-NSStatusItemView> from com.apple.controlcenter.statusitems
error	14:52:03.521193-0500	Nexy	Error creating <FBSScene: 0x7c0d34a00; com.apple.controlcenter:29AEB987-FF8D-453E-9C9D-FF77F4D5B4B2-Aux[7]-NSStatusItemView>: <NSError: 0x7bec07690; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
default	14:52:03.521254-0500	Nexy	Request for <FBSScene: 0x7c0d34a00; com.apple.controlcenter:29AEB987-FF8D-453E-9C9D-FF77F4D5B4B2-Aux[7]-NSStatusItemView> complete!
error	14:52:03.524568-0500	Nexy	scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	14:52:03.524662-0500	Nexy	[com.apple.controlcenter:29AEB987-FF8D-453E-9C9D-FF77F4D5B4B2] No matching scene to invalidate for this identity.
error	14:52:03.524827-0500	Nexy	auxiliary scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	14:52:03.524899-0500	Nexy	Unhandled disconnected scene <private>
error	14:52:03.525118-0500	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
default	14:52:04.396444-0500	Nexy	 [INFO] SLSHWCaptureDesktopProxying:485 request: <private>
default	14:52:04.396576-0500	Nexy	 [INFO] -[RPDaemonProxy proxyCoreGraphicsWithMethodType:config:machPort:completionHandler:]:1486
default	14:52:04.400576-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=31855.5, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=39688, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.replayd, pid=31855, auid=501, euid=501, binary_path=/usr/libexec/replayd}, },
default	14:52:04.400650-0500	tccd	requestor: TCCDProcess: identifier=com.apple.replayd, pid=31855, auid=501, euid=501, binary_path=/usr/libexec/replayd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=39688, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	14:52:04.403764-0500	tccd	AUTHREQ_SUBJECT: msgID=31855.5, subject=com.nexy.assistant,
default	14:52:04.405642-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d116700 at /Applications/Nexy.app
default	14:52:04.460314-0500	Nexy	 [INFO] SLSHWCaptureDesktopProxying_block_invoke:506 request: <private>, error: (null), windowInfo: (null)
default	14:52:04.526145-0500	Nexy	FBSWorkspace registering source: <private>
default	14:52:04.526176-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	14:52:04.526247-0500	Nexy	<FBSWorkspaceScenesClient:0x7c0d34a00 <private>> attempting immediate handshake from activate
default	14:52:04.526267-0500	Nexy	<FBSWorkspaceScenesClient:0x7c0d34a00 <private>> sent handshake
default	14:52:04.526489-0500	Nexy	Requesting scene <FBSScene: 0x7c0d34d20; com.apple.controlcenter:84E70E14-DD58-4367-9FF1-CF882ECB1529> from com.apple.controlcenter.statusitems
default	14:52:04.526681-0500	Nexy	Request for <FBSScene: 0x7c0d34d20; com.apple.controlcenter:84E70E14-DD58-4367-9FF1-CF882ECB1529> complete!
default	14:52:04.527008-0500	Nexy	Requesting scene <FBSScene: 0x7c0d34be0; com.apple.controlcenter:84E70E14-DD58-4367-9FF1-CF882ECB1529-Aux[8]-NSStatusItemView> from com.apple.controlcenter.statusitems
default	14:52:04.527147-0500	Nexy	Request for <FBSScene: 0x7c0d34be0; com.apple.controlcenter:84E70E14-DD58-4367-9FF1-CF882ECB1529-Aux[8]-NSStatusItemView> complete!
default	14:52:04.527553-0500	Nexy	[com.apple.controlcenter:84E70E14-DD58-4367-9FF1-CF882ECB1529-Aux[8]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
default	14:52:04.527571-0500	Nexy	[com.apple.controlcenter:84E70E14-DD58-4367-9FF1-CF882ECB1529-Aux[8]-NSStatusItemView] Dropping transition context because the scene is reconnecting
default	14:52:04.527657-0500	Nexy	<FBSWorkspaceScenesClient:0x7c0d34a00 <private>> was invalidated
default	14:52:04.527687-0500	Nexy	FBSWorkspace unregistering source: <private>
error	14:52:04.527757-0500	Nexy	Error creating <FBSScene: 0x7c0d34d20; com.apple.controlcenter:84E70E14-DD58-4367-9FF1-CF882ECB1529>: <NSError: 0x7be9f2bb0; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	14:52:04.527771-0500	Nexy	No scene exists for identity: com.apple.controlcenter:84E70E14-DD58-4367-9FF1-CF882ECB1529
error	14:52:04.527796-0500	Nexy	Error creating <FBSScene: 0x7c0d34be0; com.apple.controlcenter:84E70E14-DD58-4367-9FF1-CF882ECB1529-Aux[8]-NSStatusItemView>: <NSError: 0x7be9f29a0; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	14:52:04.527810-0500	Nexy	No scene exists for identity: com.apple.controlcenter:84E70E14-DD58-4367-9FF1-CF882ECB1529-Aux[8]-NSStatusItemView
error	14:52:04.528126-0500	Nexy	scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	14:52:04.528142-0500	Nexy	[com.apple.controlcenter:84E70E14-DD58-4367-9FF1-CF882ECB1529] No matching scene to invalidate for this identity.
error	14:52:04.528162-0500	Nexy	auxiliary scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	14:52:04.528179-0500	Nexy	[com.apple.controlcenter:84E70E14-DD58-4367-9FF1-CF882ECB1529-Aux[8]-NSStatusItemView] No matching scene to invalidate for this identity.
error	14:52:04.528206-0500	Nexy	Unhandled disconnected scene <private>
error	14:52:04.528260-0500	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
error	14:52:04.528299-0500	Nexy	Unhandled disconnected auxiliary scene <private>
error	14:52:04.528323-0500	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
default	14:52:04.553455-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	14:52:04.553618-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	14:52:04.553710-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	14:52:04.553869-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	14:52:04.594636-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	14:52:04.599286-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ef2c0","name":"Nexy(39688)"}, "details":{"deviceUIDs":[],"implicit_category":"","input_running":false,"output_running":false} }
default	14:52:04.599129-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {BuiltInMicrophoneDevice, 0xd}
default	14:52:04.599356-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 705, PID = 39688, Name = sid:0x1ef2c0, Nexy(39688), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	14:52:04.599391-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 705, PID = 39688, Name = sid:0x1ef2c0, Nexy(39688), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	14:52:04.599701-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1ef2c0, Nexy(39688), 'prim'', displayID:'com.nexy.assistant'}
default	14:52:04.599971-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1ef2c0, Nexy(39688), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 705 stopping recording
default	14:52:04.600056-0500	audiomxd	-MXCoreSession- -[MXCoreSession endInterruption:]: Session <ID: 705, PID = 39688, Name = sid:0x1ef2c0, Nexy(39688), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> is going inactive
default	14:52:04.600147-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 705, PID = 39688, Name = sid:0x1ef2c0, Nexy(39688), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	14:52:04.600210-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 705, PID = 39688, Name = sid:0x1ef2c0, Nexy(39688), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	14:52:04.600370-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 0]. BT device UIDS: {(
)}
default	14:52:04.600380-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	14:52:04.600375-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	14:52:04.600420-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:52:04.600476-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	14:52:04.600518-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	14:52:04.600544-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	14:52:04.600586-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:52:04.600610-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	14:52:04.600626-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:52:04.600639-0500	audioaccessoryd	AudioStateChanged: Removed audio session app com.nexy.assistant 201 count 0
default	14:52:04.652333-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	14:52:04.652513-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant)]
default	14:52:04.652626-0500	ControlCenter	Active activity attributions changed to ["scr:com.nexy.assistant"]
default	14:52:04.652666-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	14:52:04.654328-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:52:04.654351-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:52:04.654377-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	14:52:04.654392-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:52:04.654405-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	14:52:04.654417-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	14:52:04.654644-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	14:52:04.706690-0500	Nexy	                AUHAL.cpp:473   ~AUHAL: (0x7bf0a8e40) Selecting device 0 from destructor
default	14:52:04.706720-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0x7bf0a8e40)
default	14:52:04.706734-0500	Nexy	                AUHAL.cpp:676   SelectDevice: (0x7bf0a8e40) not already running
default	14:52:04.706748-0500	Nexy	                AUHAL.cpp:682   SelectDevice: (0x7bf0a8e40) disconnecting device 78
default	14:52:04.706762-0500	Nexy	                AUHAL.cpp:746   SelectDevice: (0x7bf0a8e40) destroying ioproc 0xd for device 78
default	14:52:04.706815-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {BuiltInMicrophoneDevice, 0xd}
default	14:52:04.706880-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	14:52:04.707217-0500	Nexy	                AUHAL.cpp:848   SelectDevice: (0x7bf0a8e40) nothing to setup
default	14:52:04.707251-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x7bf0a8e40) adding 0 device listeners to device 0
default	14:52:04.707267-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x7bf0a8e40) adding 0 device delegate listeners to device 0
default	14:52:04.707283-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x7bf0a8e40) removing 7 device listeners from device 78
default	14:52:04.707875-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x7bf0a8e40) removing 0 device delegate listeners from device 78
default	14:52:04.707906-0500	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0x7bf0a8e40)
default	14:52:04.980508-0500	Nexy	nw_path_libinfo_path_check [E3EF8511-6321-4C83-94D6-B8B26AF47E76 Hostname#8ac90fa8:80 tcp, legacy-socket, attribution: developer]
	libinfo check path: <private>
default	14:52:04.980664-0500	mDNSResponder	[R635454] DNSServiceCreateConnection START PID[39688](Nexy)
default	14:52:04.980732-0500	mDNSResponder	[R635455] DNSServiceQueryRecord START -- qname: <mask.hash: 'lETfDsfMRrhKUOGbaqIqQA=='>, qtype: A, flags: 0x1D000, interface index: 0, client pid: 39688 (Nexy), name hash: b360ab20
default	14:52:04.981240-0500	mDNSResponder	[R635456] DNSServiceQueryRecord START -- qname: <mask.hash: 'lETfDsfMRrhKUOGbaqIqQA=='>, qtype: AAAA, flags: 0x1D000, interface index: 0, client pid: 39688 (Nexy), name hash: b360ab20
default	14:52:05.015208-0500	kernel	SK[3]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 3B74D186-F38B-4246-91B7-1C095088CEE1 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.58172,dst=<IPv4-redacted>.80,proto=0x06 mask=0x0000003f,hash=0x7d768592 tp_proto=0x06"
default	14:52:05.015515-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:58172<-><IPv4-redacted>:80] interface: en0 (skipped: 6843)
so_gencnt: 6102404 t_state: SYN_SENT process: Nexy:39688 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x8f37693c
default	14:52:05.029954-0500	kernel	tcp connected: [<IPv4-redacted>:58172<-><IPv4-redacted>:80] interface: en0 (skipped: 6843)
so_gencnt: 6102404 t_state: ESTABLISHED process: Nexy:39688 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x8f37693c
default	14:52:05.236000-0500	kernel	tcp_connection_summary (tcp_usrclosed:3220)[<IPv4-redacted>:58172<-><IPv4-redacted>:80] interface: en0 (skipped: 6843)
so_gencnt: 6102404 t_state: LAST_ACK process: Nexy:39688 Duration: 0.221 sec Conn_Time: 0.015 sec bytes in/out: 398/25046 pkts in/out: 3/8 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 16.218 ms rttvar: 1.875 ms base rtt: 15 ms so_error: 0 svc/tc: 0 flow: 0x8f37693c
default	14:52:05.236030-0500	kernel	tcp_connection_summary [<IPv4-redacted>:58172<-><IPv4-redacted>:80] interface: en0 (skipped: 6843)
so_gencnt: 6102404 t_state: LAST_ACK process: Nexy:39688 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 1/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	14:52:05.252404-0500	runningboardd	ignoring [app<application.com.nexy.assistant.21074037.21074043(501)>:39688] as candidate for concrete target as it is terminating
default	14:52:05.252528-0500	runningboardd	Acquiring assertion targeting 39688 from originator [app<application.com.nexy.assistant.21074037.21074043(501)>:39688] with description <RBSAssertionDescriptor| "AudioHAL" ID:398-39688-1518833 target:39688 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
error	14:52:05.253139-0500	Nexy	Error acquiring assertion: <Error Domain=RBSAssertionErrorDomain Code=2 "Specified target process 39688 does not exist" UserInfo={NSLocalizedFailureReason=Specified target process 39688 does not exist}>
default	14:52:05.253211-0500	runningboardd	ignoring [app<application.com.nexy.assistant.21074037.21074043(501)>:39688] as candidate for concrete target as it is terminating
error	14:52:05.253182-0500	Nexy	          HALRBSAssertionGlue.mm:98    Failed to acquire the AudioHAL RBSAssertion for pid: 39688 with code: 2 - RBSAssertionErrorDomain
default	14:52:05.280627-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {BuiltInSpeakerDevice, 0x10}
default	14:52:05.281744-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ef2c0","name":"Nexy(39688)"}, "details":{"deviceUIDs":[],"implicit_category":"MediaPlayback","input_running":false,"output_running":true} }
default	14:52:05.281826-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 705, PID = 39688, Name = sid:0x1ef2c0, Nexy(39688), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	14:52:05.281856-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Category/Mode changed -- The score for sid:0x1ef2c0, Nexy(39688), 'prim'/com.nexy.assistant was not correct. Old score = 201
default	14:52:05.281888-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 705, PID = 39688, Name = sid:0x1ef2c0, Nexy(39688), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	14:52:05.281938-0500	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1ef2c0, Nexy(39688), 'prim'', AudioCategory changed to 'MediaPlayback'
default	14:52:05.281960-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:52:05.281991-0500	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 705, PID = 39688, Name = sid:0x1ef2c0, Nexy(39688), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO> is going active
default	14:52:05.282016-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsPlaying:]: MXCoreSession com.nexy.assistant with category/mode MediaPlayback/Default and coreSessionID = 705 starting playing
default	14:52:05.282084-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:52:05.282123-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 705, PID = 39688, Name = sid:0x1ef2c0, Nexy(39688), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	14:52:05.282160-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:52:05.282200-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 705, PID = 39688, Name = sid:0x1ef2c0, Nexy(39688), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO>
default	14:52:05.282263-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1ef2c0, Nexy(39688), 'prim'', displayID:'com.nexy.assistant'}
default	14:52:05.282321-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Will try to see if we can get the shared route for session = <ID: 705, PID = 39688, Name = sid:0x1ef2c0, Nexy(39688), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO>. Old (200) and New (201) scores.
default	14:52:05.282495-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 1]. BT device UIDS: {(
)}
default	14:52:05.282507-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	14:52:05.282426-0500	audiomxd	AudioApplicationInfoImpl.mm:395   Successfully updated session 0x1ef2c0 to isSessionRecording: 0
	app: {"name":"[implicit] Nexy","pid":39688}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1ef2c0, sessionType: 'prim', isRecording: false }, 
]
default	14:52:05.282433-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 201, deviceID = <private>
default	14:52:05.282634-0500	audioaccessoryd	Routing request Wx NULL score 201 flag 0x1 < Hijack > app com.nexy.assistant CID 0xD310001 category Not set
default	14:52:05.282804-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	14:52:05.282871-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 201,
}
default	14:52:05.282895-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	14:52:05.282907-0500	audioaccessoryd	AudioStateChanged: Added audio session app com.nexy.assistant NULL -> 201 count 2
default	14:52:05.282917-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 201
error	14:52:05.282934-0500	audioaccessoryd	Updating local audio category 100 -> 201 app com.nexy.assistant
default	14:52:05.282970-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.nexy.assistant
default	14:52:05.313647-0500	runningboardd	ignoring [app<application.com.nexy.assistant.21074037.21074043(501)>:39688] as candidate for concrete target as it is terminating
default	14:52:05.313986-0500	WindowServer	19d0d3[SetFrontProcessWithInfo]: [DeferringManager] Updating policy {
    advicePolicy: .frontmost;
    frontmostProcess: 0x0-0x1a7aa79 (Nexy) mainConnectionID: 19D0D3;
} for reason: updated frontmost process
default	14:52:05.314100-0500	WindowServer	19d0d3[SetFrontProcessWithInfo]: [DeferringManager] Deferring events from frontmost process PSN 0x0-0x1a7aa79 (Nexy) -> <pid: 39688>
default	14:52:05.314258-0500	WindowServer	new deferring rules for pid:393: [
    [393-EEC5]; <keyboardFocus; Nexy:0x0-0x1a7aa79>; () -> <pid: 39688>; reason: frontmost PSN --> outbound target,
    [393-EEC4]; <keyboardFocus; <frontmost>>; () -> <token: Nexy:0x0-0x1a7aa79; pid: 393>; reason: frontmost PSN,
    [393-EEC3]; <keyboardFocus>; () -> <token: <frontmost>; pid: 393>; reason: Deferring to <frontmost>
]
default	14:52:05.314313-0500	WindowServer	[keyboardFocus 0x7facf2b20] setRules:forPID(393): [
    [393-EEC5]; <keyboardFocus; Nexy:0x0-0x1a7aa79>; () -> <pid: 39688>; reason: frontmost PSN --> outbound target,
    [393-EEC4]; <keyboardFocus; <frontmost>>; () -> <token: Nexy:0x0-0x1a7aa79; pid: 393>; reason: frontmost PSN,
    [393-EEC3]; <keyboardFocus>; () -> <token: <frontmost>; pid: 393>; reason: Deferring to <frontmost>
]
default	14:52:05.314826-0500	runningboardd	ignoring [app<application.com.nexy.assistant.21074037.21074043(501)>:39688] as candidate for concrete target as it is terminating
default	14:52:05.315191-0500	WindowServer	chain did update (setDeferringRules) <keyboardFocus; display: null> containsEndOfChain: YES; [
    <token: <frontmost>; pid: 393>,
    <token: Nexy:0x0-0x1a7aa79; pid: 393>,
    <pid: 39688>
]
default	14:52:05.323487-0500	Nexy	[0x7be8b6580] activating connection: mach=false listener=false peer=false name=com.apple.ViewBridgeAuxiliary
default	14:52:05.332741-0500	Nexy	[0x7be8b66c0] activating connection: mach=false listener=false peer=false name=(anonymous)
default	14:52:05.333219-0500	Nexy	[0x7be8b6800] activating connection: mach=false listener=true peer=false name=(anonymous)
default	14:52:05.333228-0500	Nexy	[0x7be8b6800] Connection returned listener port: 0x1f623
default	14:52:05.334275-0500	Nexy	[0x7be8b6580] invalidated after the last release of the connection object
default	14:52:05.392513-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=39740.1, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=39688, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.osascript, pid=39740, auid=501, euid=501, binary_path=/usr/bin/osascript}, },
default	14:52:05.393815-0500	tccd	AUTHREQ_SUBJECT: msgID=39740.1, subject=com.nexy.assistant,
default	14:52:05.394378-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d116700 at /Applications/Nexy.app
default	14:52:05.408303-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=393.17781, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=39688, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.osascript, pid=39740, auid=501, euid=501, binary_path=/usr/bin/osascript}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=393, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	14:52:05.409153-0500	tccd	AUTHREQ_SUBJECT: msgID=393.17781, subject=com.nexy.assistant,
default	14:52:05.409708-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d116700 at /Applications/Nexy.app
default	14:52:05.436661-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d116700 at /Applications/Nexy.app
default	14:52:05.454255-0500	System Events	TCCAccessRequestIndirect: TCCAccessRequestIndirect with pid 39696: target_identity: {
    kTCCCodeIdentityAuditToken = {length = 32, bytes = 0xf5010000 f5010000 14000000 f5010000 ... b7860100 aefb2800 };
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
default	14:52:05.464919-0500	tccd	target_executable_path_URL: file:///Applications/Nexy.app/Contents/MacOS/Nexy
default	14:52:05.485794-0500	WindowServer	0[outside of RPC]: [DeferringManager] Updating policy {
    advicePolicy: .frontmost;
    frontmostProcess: 0x0-0x1a7aa79 (Nexy) mainConnectionID: 19D0D3;
} for reason: deferringPolicyEvaluationSuppression
default	14:52:05.485872-0500	WindowServer	0[outside of RPC]: [DeferringManager] Deferring events from frontmost process PSN 0x0-0x1a7aa79 (Nexy) -> <pid: 39688>
default	14:52:05.485975-0500	WindowServer	new deferring rules for pid:393: [
    [393-EEC8]; <keyboardFocus; Nexy:0x0-0x1a7aa79>; () -> <pid: 39688>; reason: frontmost PSN --> outbound target,
    [393-EEC7]; <keyboardFocus; <frontmost>>; () -> <token: Nexy:0x0-0x1a7aa79; pid: 393>; reason: frontmost PSN,
    [393-EEC6]; <keyboardFocus>; () -> <token: <frontmost>; pid: 393>; reason: Deferring to <frontmost>
]
default	14:52:05.486010-0500	WindowServer	[keyboardFocus 0x7facf2b20] setRules:forPID(393): [
    [393-EEC8]; <keyboardFocus; Nexy:0x0-0x1a7aa79>; () -> <pid: 39688>; reason: frontmost PSN --> outbound target,
    [393-EEC7]; <keyboardFocus; <frontmost>>; () -> <token: Nexy:0x0-0x1a7aa79; pid: 393>; reason: frontmost PSN,
    [393-EEC6]; <keyboardFocus>; () -> <token: <frontmost>; pid: 393>; reason: Deferring to <frontmost>
]
default	14:52:05.486594-0500	WindowServer	chain did update (setDeferringRules) <keyboardFocus; display: null> containsEndOfChain: YES; [
    <token: <frontmost>; pid: 393>,
    <token: Nexy:0x0-0x1a7aa79; pid: 393>,
    <pid: 39688>
]
default	14:52:05.529413-0500	Nexy	FBSWorkspace registering source: <private>
default	14:52:05.529443-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	14:52:05.529503-0500	Nexy	<FBSWorkspaceScenesClient:0x7c0d34d20 <private>> attempting immediate handshake from activate
default	14:52:05.529525-0500	Nexy	<FBSWorkspaceScenesClient:0x7c0d34d20 <private>> sent handshake
default	14:52:05.529752-0500	Nexy	Requesting scene <FBSScene: 0x7c0d34c80; com.apple.controlcenter:04D7E9DD-CD5C-49EC-B683-529961E06FF7> from com.apple.controlcenter.statusitems
default	14:52:05.529937-0500	Nexy	Request for <FBSScene: 0x7c0d34c80; com.apple.controlcenter:04D7E9DD-CD5C-49EC-B683-529961E06FF7> complete!
default	14:52:05.530241-0500	Nexy	Requesting scene <FBSScene: 0x7c0d34e60; com.apple.controlcenter:04D7E9DD-CD5C-49EC-B683-529961E06FF7-Aux[9]-NSStatusItemView> from com.apple.controlcenter.statusitems
default	14:52:05.530375-0500	Nexy	Request for <FBSScene: 0x7c0d34e60; com.apple.controlcenter:04D7E9DD-CD5C-49EC-B683-529961E06FF7-Aux[9]-NSStatusItemView> complete!
default	14:52:05.530534-0500	Nexy	<FBSWorkspaceScenesClient:0x7c0d34d20 <private>> was invalidated
default	14:52:05.530559-0500	Nexy	FBSWorkspace unregistering source: <private>
error	14:52:05.530616-0500	Nexy	Error creating <FBSScene: 0x7c0d34c80; com.apple.controlcenter:04D7E9DD-CD5C-49EC-B683-529961E06FF7>: <NSError: 0x7be9f2610; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	14:52:05.530631-0500	Nexy	No scene exists for identity: com.apple.controlcenter:04D7E9DD-CD5C-49EC-B683-529961E06FF7
error	14:52:05.530654-0500	Nexy	Error creating <FBSScene: 0x7c0d34e60; com.apple.controlcenter:04D7E9DD-CD5C-49EC-B683-529961E06FF7-Aux[9]-NSStatusItemView>: <NSError: 0x7be9f20a0; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	14:52:05.530664-0500	Nexy	No scene exists for identity: com.apple.controlcenter:04D7E9DD-CD5C-49EC-B683-529961E06FF7-Aux[9]-NSStatusItemView
default	14:52:05.530755-0500	Nexy	[com.apple.controlcenter:04D7E9DD-CD5C-49EC-B683-529961E06FF7-Aux[9]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
error	14:52:05.530906-0500	Nexy	scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	14:52:05.530919-0500	Nexy	[com.apple.controlcenter:04D7E9DD-CD5C-49EC-B683-529961E06FF7] No matching scene to invalidate for this identity.
error	14:52:05.530936-0500	Nexy	auxiliary scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	14:52:05.530945-0500	Nexy	[com.apple.controlcenter:04D7E9DD-CD5C-49EC-B683-529961E06FF7-Aux[9]-NSStatusItemView] No matching scene to invalidate for this identity.
error	14:52:05.531280-0500	Nexy	Unhandled disconnected auxiliary scene <private>
error	14:52:05.531325-0500	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
error	14:52:05.531347-0500	Nexy	Unhandled disconnected scene <private>
error	14:52:05.531371-0500	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
default	14:52:05.573410-0500	Nexy	[0x7be8b6580] activating connection: mach=false listener=false peer=false name=com.apple.hiservices-xpcservice
default	14:52:05.576867-0500	Nexy	+[IMKClient subclass]: chose IMKClient_Modern
default	14:52:05.576896-0500	Nexy	+[IMKInputSession subclass]: chose IMKInputSession_Modern
default	14:52:05.579011-0500	Nexy	[0x7be8b6940] activating connection: mach=true listener=false peer=false name=com.apple.inputmethodkit.getxpcendpoint
default	14:52:05.580069-0500	Nexy	[0x7be8b6a80] activating connection: mach=true listener=false peer=false name=com.apple.inputmethodkit.getxpcendpoint
default	14:52:05.580668-0500	Nexy	[0x7be8b6bc0] activating connection: mach=false listener=false peer=false name=(anonymous)
default	14:52:05.580835-0500	Nexy	[0x7be8b6e40] activating connection: mach=false listener=false peer=false name=(anonymous)
default	14:52:05.581149-0500	DictationIM	setting current input controller = com.nexy.assistant
default	14:52:05.581716-0500	Nexy	[0x7be8b6d00] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
error	14:52:05.582931-0500	tccd	TCCDProcess: identifier=com.nexy.assistant, pid=39688, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy attempted to call TCCAccessRequest for kTCCServiceAccessibility without the recommended com.apple.private.tcc.manager.check-by-audit-token entitlement
default	14:52:05.583039-0500	Nexy	[0x7be8b6d00] invalidated after the last release of the connection object
default	14:52:05.587135-0500	Nexy	void _NSDisableAutomaticTerminationAndLog(NSString *) NSAccessibility Request Received
default	14:52:05.666404-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Output {BuiltInSpeakerDevice, 0x10}
default	14:52:05.666735-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ef2c0","name":"Nexy(39688)"}, "details":{"deviceUIDs":[],"implicit_category":"","input_running":false,"output_running":false} }
default	14:52:05.666804-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsPlaying:]: MXCoreSession com.nexy.assistant with category/mode MediaPlayback/Default and coreSessionID = 705 stopping playing
default	14:52:05.666841-0500	audiomxd	-MXCoreSession- -[MXCoreSession endInterruption:]: Session <ID: 705, PID = 39688, Name = sid:0x1ef2c0, Nexy(39688), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> is going inactive
default	14:52:05.666876-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 705, PID = 39688, Name = sid:0x1ef2c0, Nexy(39688), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	14:52:05.666918-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 705, PID = 39688, Name = sid:0x1ef2c0, Nexy(39688), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	14:52:05.666974-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:52:05.667012-0500	audiomxd	AudioApplicationInfoImpl.mm:395   Successfully updated session 0x1ef2c0 to isSessionRecording: 0
	app: {"name":"[implicit] Nexy","pid":39688}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1ef2c0, sessionType: 'prim', isRecording: false }, 
]
default	14:52:05.667078-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 0]. BT device UIDS: {(
)}
default	14:52:05.667088-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	14:52:05.667083-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:52:05.667120-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:52:05.667136-0500	audioaccessoryd	AudioStateChanged: Removed audio session app com.nexy.assistant 201 count 1
default	14:52:06.532865-0500	Nexy	FBSWorkspace registering source: <private>
default	14:52:06.532958-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	14:52:06.533164-0500	Nexy	<FBSWorkspaceScenesClient:0x7c0d354a0 <private>> attempting immediate handshake from activate
default	14:52:06.533267-0500	Nexy	<FBSWorkspaceScenesClient:0x7c0d354a0 <private>> sent handshake
default	14:52:06.534080-0500	Nexy	Requesting scene <FBSScene: 0x7c0d35400; com.apple.controlcenter:50661DBD-19F8-40E0-9294-6450531E8D14> from com.apple.controlcenter.statusitems
default	14:52:06.534666-0500	Nexy	<FBSWorkspaceScenesClient:0x7c0d354a0 <private>> was invalidated
default	14:52:06.534775-0500	Nexy	FBSWorkspace unregistering source: <private>
default	14:52:06.534895-0500	Nexy	Request for <FBSScene: 0x7c0d35400; com.apple.controlcenter:50661DBD-19F8-40E0-9294-6450531E8D14> complete!
error	14:52:06.534975-0500	Nexy	Error creating <FBSScene: 0x7c0d35400; com.apple.controlcenter:50661DBD-19F8-40E0-9294-6450531E8D14>: <NSError: 0x7bec06dc0; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
default	14:52:06.534972-0500	Nexy	LSExceptions shared instance invalidated for timeout.
error	14:52:06.535046-0500	Nexy	No scene exists for identity: com.apple.controlcenter:50661DBD-19F8-40E0-9294-6450531E8D14
default	14:52:06.535247-0500	Nexy	FBSWorkspace registering source: <private>
default	14:52:06.535286-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	14:52:06.535375-0500	Nexy	<FBSWorkspaceScenesClient:0x7c0d35360 <private>> attempting immediate handshake from activate
default	14:52:06.535414-0500	Nexy	<FBSWorkspaceScenesClient:0x7c0d35360 <private>> sent handshake
default	14:52:06.535675-0500	Nexy	Requesting scene <FBSScene: 0x7c0d355e0; com.apple.controlcenter:50661DBD-19F8-40E0-9294-6450531E8D14-Aux[10]-NSStatusItemView> from com.apple.controlcenter.statusitems
default	14:52:06.536079-0500	Nexy	Request for <FBSScene: 0x7c0d355e0; com.apple.controlcenter:50661DBD-19F8-40E0-9294-6450531E8D14-Aux[10]-NSStatusItemView> complete!
default	14:52:06.536375-0500	Nexy	<FBSWorkspaceScenesClient:0x7c0d35360 <private>> was invalidated
default	14:52:06.536426-0500	Nexy	FBSWorkspace unregistering source: <private>
error	14:52:06.536539-0500	Nexy	Error creating <FBSScene: 0x7c0d355e0; com.apple.controlcenter:50661DBD-19F8-40E0-9294-6450531E8D14-Aux[10]-NSStatusItemView>: <NSError: 0x7bec07900; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	14:52:06.536573-0500	Nexy	No scene exists for identity: com.apple.controlcenter:50661DBD-19F8-40E0-9294-6450531E8D14-Aux[10]-NSStatusItemView
default	14:52:06.537379-0500	Nexy	[com.apple.controlcenter:50661DBD-19F8-40E0-9294-6450531E8D14-Aux[10]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
error	14:52:06.537688-0500	Nexy	scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	14:52:06.537748-0500	Nexy	auxiliary scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	14:52:06.537786-0500	Nexy	[com.apple.controlcenter:50661DBD-19F8-40E0-9294-6450531E8D14-Aux[10]-NSStatusItemView] No matching scene to invalidate for this identity.
error	14:52:06.538685-0500	Nexy	Unhandled disconnected auxiliary scene <private>
error	14:52:06.538811-0500	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
default	14:52:07.539309-0500	Nexy	FBSWorkspace registering source: <private>
default	14:52:07.539370-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	14:52:07.539509-0500	Nexy	<FBSWorkspaceScenesClient:0x7c0d355e0 <private>> attempting immediate handshake from activate
default	14:52:07.539560-0500	Nexy	<FBSWorkspaceScenesClient:0x7c0d355e0 <private>> sent handshake
default	14:52:07.540081-0500	Nexy	Requesting scene <FBSScene: 0x7c0d35400; com.apple.controlcenter:07A10DEB-D703-46D8-93FA-653F1FB7A46E> from com.apple.controlcenter.statusitems
default	14:52:07.540577-0500	Nexy	Request for <FBSScene: 0x7c0d35400; com.apple.controlcenter:07A10DEB-D703-46D8-93FA-653F1FB7A46E> complete!
default	14:52:07.541125-0500	Nexy	<FBSWorkspaceScenesClient:0x7c0d355e0 <private>> was invalidated
default	14:52:07.541181-0500	Nexy	FBSWorkspace unregistering source: <private>
default	14:52:07.541289-0500	Nexy	FBSWorkspace registering source: <private>
default	14:52:07.541325-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	14:52:07.541421-0500	Nexy	<FBSWorkspaceScenesClient:0x7c0d35360 <private>> attempting immediate handshake from activate
default	14:52:07.541460-0500	Nexy	<FBSWorkspaceScenesClient:0x7c0d35360 <private>> sent handshake
error	14:52:07.541577-0500	Nexy	Error creating <FBSScene: 0x7c0d35400; com.apple.controlcenter:07A10DEB-D703-46D8-93FA-653F1FB7A46E>: <NSError: 0x7bec075d0; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	14:52:07.541615-0500	Nexy	No scene exists for identity: com.apple.controlcenter:07A10DEB-D703-46D8-93FA-653F1FB7A46E
default	14:52:07.541739-0500	Nexy	Requesting scene <FBSScene: 0x7c0d354a0; com.apple.controlcenter:07A10DEB-D703-46D8-93FA-653F1FB7A46E-Aux[11]-NSStatusItemView> from com.apple.controlcenter.statusitems
default	14:52:07.542062-0500	Nexy	Request for <FBSScene: 0x7c0d354a0; com.apple.controlcenter:07A10DEB-D703-46D8-93FA-653F1FB7A46E-Aux[11]-NSStatusItemView> complete!
default	14:52:07.542438-0500	Nexy	<FBSWorkspaceScenesClient:0x7c0d35360 <private>> was invalidated
default	14:52:07.542486-0500	Nexy	FBSWorkspace unregistering source: <private>
error	14:52:07.542608-0500	Nexy	Error creating <FBSScene: 0x7c0d354a0; com.apple.controlcenter:07A10DEB-D703-46D8-93FA-653F1FB7A46E-Aux[11]-NSStatusItemView>: <NSError: 0x7bec06e80; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	14:52:07.542654-0500	Nexy	No scene exists for identity: com.apple.controlcenter:07A10DEB-D703-46D8-93FA-653F1FB7A46E-Aux[11]-NSStatusItemView
default	14:52:07.542800-0500	Nexy	[com.apple.controlcenter:07A10DEB-D703-46D8-93FA-653F1FB7A46E-Aux[11]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
error	14:52:07.543204-0500	Nexy	scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	14:52:07.543219-0500	Nexy	[com.apple.controlcenter:07A10DEB-D703-46D8-93FA-653F1FB7A46E] No matching scene to invalidate for this identity.
error	14:52:07.543243-0500	Nexy	auxiliary scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	14:52:07.543256-0500	Nexy	[com.apple.controlcenter:07A10DEB-D703-46D8-93FA-653F1FB7A46E-Aux[11]-NSStatusItemView] No matching scene to invalidate for this identity.
error	14:52:07.543682-0500	Nexy	Unhandled disconnected scene <private>
error	14:52:07.543818-0500	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
error	14:52:07.543906-0500	Nexy	Unhandled disconnected auxiliary scene <private>
error	14:52:07.543971-0500	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
default	14:52:08.544831-0500	Nexy	FBSWorkspace registering source: <private>
default	14:52:08.544891-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	14:52:08.545027-0500	Nexy	<FBSWorkspaceScenesClient:0x7c0d354a0 <private>> attempting immediate handshake from activate
default	14:52:08.545077-0500	Nexy	<FBSWorkspaceScenesClient:0x7c0d354a0 <private>> sent handshake
default	14:52:08.545528-0500	Nexy	Requesting scene <FBSScene: 0x7c0d35400; com.apple.controlcenter:C10D7364-6C62-497E-9F08-5B121ECEB9E3> from com.apple.controlcenter.statusitems
default	14:52:08.545941-0500	Nexy	Request for <FBSScene: 0x7c0d35400; com.apple.controlcenter:C10D7364-6C62-497E-9F08-5B121ECEB9E3> complete!
default	14:52:08.546551-0500	Nexy	<FBSWorkspaceScenesClient:0x7c0d354a0 <private>> was invalidated
default	14:52:08.546608-0500	Nexy	FBSWorkspace unregistering source: <private>
error	14:52:08.546767-0500	Nexy	Error creating <FBSScene: 0x7c0d35400; com.apple.controlcenter:C10D7364-6C62-497E-9F08-5B121ECEB9E3>: <NSError: 0x7bec07900; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	14:52:08.546809-0500	Nexy	No scene exists for identity: com.apple.controlcenter:C10D7364-6C62-497E-9F08-5B121ECEB9E3
default	14:52:08.546880-0500	Nexy	Requesting scene <FBSScene: 0x7c0d35360; com.apple.controlcenter:C10D7364-6C62-497E-9F08-5B121ECEB9E3-Aux[12]-NSStatusItemView> from com.apple.controlcenter.statusitems
error	14:52:08.547097-0500	Nexy	Error creating <FBSScene: 0x7c0d35360; com.apple.controlcenter:C10D7364-6C62-497E-9F08-5B121ECEB9E3-Aux[12]-NSStatusItemView>: <NSError: 0x7bec075d0; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
default	14:52:08.547179-0500	Nexy	Request for <FBSScene: 0x7c0d35360; com.apple.controlcenter:C10D7364-6C62-497E-9F08-5B121ECEB9E3-Aux[12]-NSStatusItemView> complete!
error	14:52:08.547441-0500	Nexy	scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	14:52:08.547477-0500	Nexy	[com.apple.controlcenter:C10D7364-6C62-497E-9F08-5B121ECEB9E3] No matching scene to invalidate for this identity.
error	14:52:08.547529-0500	Nexy	auxiliary scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	14:52:08.547585-0500	Nexy	Unhandled disconnected scene <private>
error	14:52:08.547689-0500	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
default	14:52:08.563627-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	14:52:08.563750-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant)]
default	14:52:09.548791-0500	Nexy	FBSWorkspace registering source: <private>
default	14:52:09.548841-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	14:52:09.548955-0500	Nexy	<FBSWorkspaceScenesClient:0x7c0d35360 <private>> attempting immediate handshake from activate
default	14:52:09.548996-0500	Nexy	<FBSWorkspaceScenesClient:0x7c0d35360 <private>> sent handshake
default	14:52:09.549385-0500	Nexy	Requesting scene <FBSScene: 0x7c0d35400; com.apple.controlcenter:5C08B202-E4F9-4E28-81D3-96941D227805> from com.apple.controlcenter.statusitems
default	14:52:09.549731-0500	Nexy	Request for <FBSScene: 0x7c0d35400; com.apple.controlcenter:5C08B202-E4F9-4E28-81D3-96941D227805> complete!
default	14:52:09.550198-0500	Nexy	<FBSWorkspaceScenesClient:0x7c0d35360 <private>> was invalidated
default	14:52:09.550242-0500	Nexy	FBSWorkspace unregistering source: <private>
default	14:52:09.550324-0500	Nexy	FBSWorkspace registering source: <private>
default	14:52:09.550348-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	14:52:09.550417-0500	Nexy	<FBSWorkspaceScenesClient:0x7c0d354a0 <private>> attempting immediate handshake from activate
default	14:52:09.550445-0500	Nexy	<FBSWorkspaceScenesClient:0x7c0d354a0 <private>> sent handshake
error	14:52:09.550534-0500	Nexy	Error creating <FBSScene: 0x7c0d35400; com.apple.controlcenter:5C08B202-E4F9-4E28-81D3-96941D227805>: <NSError: 0x7bec06d90; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	14:52:09.550560-0500	Nexy	No scene exists for identity: com.apple.controlcenter:5C08B202-E4F9-4E28-81D3-96941D227805
default	14:52:09.550633-0500	Nexy	Requesting scene <FBSScene: 0x7c0d355e0; com.apple.controlcenter:5C08B202-E4F9-4E28-81D3-96941D227805-Aux[13]-NSStatusItemView> from com.apple.controlcenter.statusitems
default	14:52:09.550879-0500	Nexy	Request for <FBSScene: 0x7c0d355e0; com.apple.controlcenter:5C08B202-E4F9-4E28-81D3-96941D227805-Aux[13]-NSStatusItemView> complete!
default	14:52:09.551239-0500	Nexy	<FBSWorkspaceScenesClient:0x7c0d354a0 <private>> was invalidated
default	14:52:09.551275-0500	Nexy	FBSWorkspace unregistering source: <private>
error	14:52:09.551354-0500	Nexy	Error creating <FBSScene: 0x7c0d355e0; com.apple.controlcenter:5C08B202-E4F9-4E28-81D3-96941D227805-Aux[13]-NSStatusItemView>: <NSError: 0x7bec06940; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	14:52:09.551382-0500	Nexy	No scene exists for identity: com.apple.controlcenter:5C08B202-E4F9-4E28-81D3-96941D227805-Aux[13]-NSStatusItemView
default	14:52:09.551551-0500	Nexy	[com.apple.controlcenter:5C08B202-E4F9-4E28-81D3-96941D227805-Aux[13]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
error	14:52:09.551873-0500	Nexy	scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	14:52:09.551899-0500	Nexy	[com.apple.controlcenter:5C08B202-E4F9-4E28-81D3-96941D227805] No matching scene to invalidate for this identity.
error	14:52:09.551940-0500	Nexy	auxiliary scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	14:52:09.551961-0500	Nexy	[com.apple.controlcenter:5C08B202-E4F9-4E28-81D3-96941D227805-Aux[13]-NSStatusItemView] No matching scene to invalidate for this identity.
error	14:52:09.552393-0500	Nexy	Unhandled disconnected scene <private>
error	14:52:09.552500-0500	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
error	14:52:09.552567-0500	Nexy	Unhandled disconnected auxiliary scene <private>
error	14:52:09.552613-0500	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
default	14:52:10.553529-0500	Nexy	FBSWorkspace registering source: <private>
default	14:52:10.553589-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	14:52:10.553725-0500	Nexy	<FBSWorkspaceScenesClient:0x7c0d355e0 <private>> attempting immediate handshake from activate
default	14:52:10.553776-0500	Nexy	<FBSWorkspaceScenesClient:0x7c0d355e0 <private>> sent handshake
default	14:52:10.554249-0500	Nexy	Requesting scene <FBSScene: 0x7c0d35400; com.apple.controlcenter:AECCE344-FF21-48BA-A3F4-35FB1628A6F2> from com.apple.controlcenter.statusitems
default	14:52:10.554666-0500	Nexy	Request for <FBSScene: 0x7c0d35400; com.apple.controlcenter:AECCE344-FF21-48BA-A3F4-35FB1628A6F2> complete!
default	14:52:10.555197-0500	Nexy	<FBSWorkspaceScenesClient:0x7c0d355e0 <private>> was invalidated
default	14:52:10.555252-0500	Nexy	FBSWorkspace unregistering source: <private>
default	14:52:10.555341-0500	Nexy	FBSWorkspace registering source: <private>
default	14:52:10.555376-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	14:52:10.555463-0500	Nexy	<FBSWorkspaceScenesClient:0x7c0d35540 <private>> attempting immediate handshake from activate
default	14:52:10.555501-0500	Nexy	<FBSWorkspaceScenesClient:0x7c0d35540 <private>> sent handshake
error	14:52:10.555613-0500	Nexy	Error creating <FBSScene: 0x7c0d35400; com.apple.controlcenter:AECCE344-FF21-48BA-A3F4-35FB1628A6F2>: <NSError: 0x7bec07e70; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	14:52:10.555649-0500	Nexy	No scene exists for identity: com.apple.controlcenter:AECCE344-FF21-48BA-A3F4-35FB1628A6F2
default	14:52:10.555777-0500	Nexy	Requesting scene <FBSScene: 0x7c0d35360; com.apple.controlcenter:AECCE344-FF21-48BA-A3F4-35FB1628A6F2-Aux[14]-NSStatusItemView> from com.apple.controlcenter.statusitems
default	14:52:10.556123-0500	Nexy	Request for <FBSScene: 0x7c0d35360; com.apple.controlcenter:AECCE344-FF21-48BA-A3F4-35FB1628A6F2-Aux[14]-NSStatusItemView> complete!
default	14:52:10.556380-0500	Nexy	<FBSWorkspaceScenesClient:0x7c0d35540 <private>> was invalidated
default	14:52:10.556425-0500	Nexy	FBSWorkspace unregistering source: <private>
error	14:52:10.556525-0500	Nexy	Error creating <FBSScene: 0x7c0d35360; com.apple.controlcenter:AECCE344-FF21-48BA-A3F4-35FB1628A6F2-Aux[14]-NSStatusItemView>: <NSError: 0x7bec079c0; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	14:52:10.556556-0500	Nexy	No scene exists for identity: com.apple.controlcenter:AECCE344-FF21-48BA-A3F4-35FB1628A6F2-Aux[14]-NSStatusItemView
default	14:52:10.556824-0500	Nexy	[com.apple.controlcenter:AECCE344-FF21-48BA-A3F4-35FB1628A6F2-Aux[14]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
error	14:52:10.557145-0500	Nexy	scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	14:52:10.557172-0500	Nexy	[com.apple.controlcenter:AECCE344-FF21-48BA-A3F4-35FB1628A6F2] No matching scene to invalidate for this identity.
error	14:52:10.557214-0500	Nexy	auxiliary scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	14:52:10.557236-0500	Nexy	[com.apple.controlcenter:AECCE344-FF21-48BA-A3F4-35FB1628A6F2-Aux[14]-NSStatusItemView] No matching scene to invalidate for this identity.
error	14:52:10.557702-0500	Nexy	Unhandled disconnected scene <private>
error	14:52:10.557815-0500	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
error	14:52:10.557887-0500	Nexy	Unhandled disconnected auxiliary scene <private>
error	14:52:10.557936-0500	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
default	14:52:10.750369-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	14:52:10.750483-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant)]
default	14:52:11.558765-0500	Nexy	FBSWorkspace registering source: <private>
default	14:52:11.558825-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	14:52:11.558959-0500	Nexy	<FBSWorkspaceScenesClient:0x7c0d35360 <private>> attempting immediate handshake from activate
default	14:52:11.559007-0500	Nexy	<FBSWorkspaceScenesClient:0x7c0d35360 <private>> sent handshake
default	14:52:11.559470-0500	Nexy	Requesting scene <FBSScene: 0x7c0d35400; com.apple.controlcenter:FBF0385C-8FCF-4AAB-8AE1-D5F01611D125> from com.apple.controlcenter.statusitems
default	14:52:11.559880-0500	Nexy	Request for <FBSScene: 0x7c0d35400; com.apple.controlcenter:FBF0385C-8FCF-4AAB-8AE1-D5F01611D125> complete!
default	14:52:11.560430-0500	Nexy	<FBSWorkspaceScenesClient:0x7c0d35360 <private>> was invalidated
default	14:52:11.560487-0500	Nexy	FBSWorkspace unregistering source: <private>
default	14:52:11.560580-0500	Nexy	FBSWorkspace registering source: <private>
default	14:52:11.560616-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	14:52:11.560709-0500	Nexy	<FBSWorkspaceScenesClient:0x7c0d35540 <private>> attempting immediate handshake from activate
default	14:52:11.560750-0500	Nexy	<FBSWorkspaceScenesClient:0x7c0d35540 <private>> sent handshake
error	14:52:11.560862-0500	Nexy	Error creating <FBSScene: 0x7c0d35400; com.apple.controlcenter:FBF0385C-8FCF-4AAB-8AE1-D5F01611D125>: <NSError: 0x7bec072a0; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	14:52:11.560899-0500	Nexy	No scene exists for identity: com.apple.controlcenter:FBF0385C-8FCF-4AAB-8AE1-D5F01611D125
default	14:52:11.561019-0500	Nexy	Requesting scene <FBSScene: 0x7c0d355e0; com.apple.controlcenter:FBF0385C-8FCF-4AAB-8AE1-D5F01611D125-Aux[15]-NSStatusItemView> from com.apple.controlcenter.statusitems
default	14:52:11.561338-0500	Nexy	Request for <FBSScene: 0x7c0d355e0; com.apple.controlcenter:FBF0385C-8FCF-4AAB-8AE1-D5F01611D125-Aux[15]-NSStatusItemView> complete!
default	14:52:11.561630-0500	Nexy	<FBSWorkspaceScenesClient:0x7c0d35540 <private>> was invalidated
default	14:52:11.561669-0500	Nexy	FBSWorkspace unregistering source: <private>
error	14:52:11.561754-0500	Nexy	Error creating <FBSScene: 0x7c0d355e0; com.apple.controlcenter:FBF0385C-8FCF-4AAB-8AE1-D5F01611D125-Aux[15]-NSStatusItemView>: <NSError: 0x7bec07960; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	14:52:11.561784-0500	Nexy	No scene exists for identity: com.apple.controlcenter:FBF0385C-8FCF-4AAB-8AE1-D5F01611D125-Aux[15]-NSStatusItemView
default	14:52:11.562073-0500	Nexy	[com.apple.controlcenter:FBF0385C-8FCF-4AAB-8AE1-D5F01611D125-Aux[15]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
error	14:52:11.562479-0500	Nexy	scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	14:52:11.562519-0500	Nexy	[com.apple.controlcenter:FBF0385C-8FCF-4AAB-8AE1-D5F01611D125] No matching scene to invalidate for this identity.
error	14:52:11.562575-0500	Nexy	auxiliary scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	14:52:11.562604-0500	Nexy	[com.apple.controlcenter:FBF0385C-8FCF-4AAB-8AE1-D5F01611D125-Aux[15]-NSStatusItemView] No matching scene to invalidate for this identity.
error	14:52:11.563157-0500	Nexy	Unhandled disconnected scene <private>
error	14:52:11.563282-0500	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
error	14:52:11.563374-0500	Nexy	Unhandled disconnected auxiliary scene <private>
error	14:52:11.563436-0500	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
default	14:52:12.564150-0500	Nexy	FBSWorkspace registering source: <private>
default	14:52:12.564212-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	14:52:12.564366-0500	Nexy	<FBSWorkspaceScenesClient:0x7c0d355e0 <private>> attempting immediate handshake from activate
default	14:52:12.564415-0500	Nexy	<FBSWorkspaceScenesClient:0x7c0d355e0 <private>> sent handshake
default	14:52:12.564726-0500	Nexy	Requesting scene <FBSScene: 0x7c0d35400; com.apple.controlcenter:4D7A5909-E1ED-4089-B05C-3987FF146255> from com.apple.controlcenter.statusitems
default	14:52:12.565009-0500	Nexy	Request for <FBSScene: 0x7c0d35400; com.apple.controlcenter:4D7A5909-E1ED-4089-B05C-3987FF146255> complete!
default	14:52:12.565458-0500	Nexy	<FBSWorkspaceScenesClient:0x7c0d355e0 <private>> was invalidated
default	14:52:12.565490-0500	Nexy	FBSWorkspace unregistering source: <private>
error	14:52:12.565587-0500	Nexy	Error creating <FBSScene: 0x7c0d35400; com.apple.controlcenter:4D7A5909-E1ED-4089-B05C-3987FF146255>: <NSError: 0x7bec04420; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	14:52:12.565607-0500	Nexy	No scene exists for identity: com.apple.controlcenter:4D7A5909-E1ED-4089-B05C-3987FF146255
error	14:52:12.565676-0500	Nexy	Error creating <FBSScene: 0x7c0d354a0; com.apple.controlcenter:4D7A5909-E1ED-4089-B05C-3987FF146255-Aux[16]-NSStatusItemView>: <NSError: 0x7bec055c0; domain: FBSWorkspaceErrorDomain; code: 1 ("InvalidScene"); "scene <FBSScene: 0x7c0d354a0; com.apple.controlcenter:4D7A5909-E1ED-4089-B05C-3987FF146255-Aux[16]-NSStatusItemView> was invalidated before activation com.apple.controlcenter.statusitems">
error	14:52:12.565696-0500	Nexy	No scene exists for identity: com.apple.controlcenter:4D7A5909-E1ED-4089-B05C-3987FF146255-Aux[16]-NSStatusItemView
error	14:52:12.565857-0500	Nexy	scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	14:52:12.565872-0500	Nexy	[com.apple.controlcenter:4D7A5909-E1ED-4089-B05C-3987FF146255] No matching scene to invalidate for this identity.
error	14:52:12.565916-0500	Nexy	auxiliary scene activation failed: Error Domain=FBSWorkspaceErrorDomain Code=1 UserInfo={BSErrorCodeDescription=InvalidScene, NSLocalizedFailureReason=<private>}
error	14:52:12.565992-0500	Nexy	Unhandled disconnected scene <private>
error	14:52:12.566056-0500	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
default	14:52:13.300122-0500	WindowServer	0[outside of RPC]: Process death: 0x0-0x1a7aa79 (Nexy) connectionID: 19D0D3 pid: 39688 in session 0x101
default	14:52:13.300165-0500	WindowServer	<BSCompoundAssertion:0x7fb0154c0> ([FocusManager:257]-deferringPolicyEvaluationSuppression) acquire for reason:process death - 0x0-0x1a7aa79 (Nexy) acq:0x80278b8c0 count:1
default	14:52:13.303639-0500	audiomxd	  ServerSessionManager.mm:472   { "action":"destroy_session", "session":{"ID":"0x1ef2c0","name":"Nexy(39688)"}, "details":null }
default	14:52:13.303675-0500	audiomxd	AudioApplicationInfoImpl.mm:690   Successfully removed session 0x1ef2c0 from AudioApp, recording state unchanged (app: {"name":"[implicit] Nexy","pid":39688})
default	14:52:13.303687-0500	audiomxd	  ServerSessionManager.mm:1081  destroy audio app instance since was created implicitly by session creation and all sessions now gone (audio app: {"name":"[implicit] Nexy","pid":39688})
default	14:52:13.303963-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 705, PID = 39688, Name = sid:0x1ef2c0, Nexy(39688), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	14:52:13.304054-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 705, PID = 39688, Name = sid:0x1ef2c0, Nexy(39688), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	14:52:13.304270-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:52:13.304371-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:52:13.304466-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:52:13.304157-0500	WindowManager	Connection invalidated | (39688) Nexy
default	14:52:13.304574-0500	WindowServer	0[outside of RPC]: [FocusManager:257] update to deferring policy requested for reason: permitted list updated - 0x0-0x1a7aa79 removed - but we are suppressing evaluation for reasons: {(
    "process death - 0x0-0x1a7aa79 (Nexy)"
)}
default	14:52:13.304526-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:52:13.304939-0500	WindowServer	0[outside of RPC]: [FocusManager:257] update to deferring policy requested for reason: permitted list updated - 0x1-0x9b08 removed - but we are suppressing evaluation for reasons: {(
    "process death - 0x0-0x1a7aa79 (Nexy)"
)}
default	14:52:13.307349-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:52:13.307506-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	14:52:13.313487-0500	runningboardd	XPC connection invalidated: [app<application.com.nexy.assistant.21074037.21074043(501)>:39688]
default	14:52:13.324017-0500	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:58170<-><IPv4-redacted>:443] interface: en0 (skipped: 6843)
so_gencnt: 6102375 t_state: FIN_WAIT_1 process: Nexy:39688 Duration: 16.764 sec Conn_Time: 0.026 sec bytes in/out: 510211/936 pkts in/out: 43/7 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 24 delayed ACKs sent: 0
rtt: 26.781 ms rttvar: 11.562 ms base rtt: 20 ms so_error: 0 svc/tc: 0 flow: 0x8e5a5b61
default	14:52:13.324037-0500	kernel	tcp_connection_summary [<IPv4-redacted>:58170<-><IPv4-redacted>:443] interface: en0 (skipped: 6843)
so_gencnt: 6102375 t_state: FIN_WAIT_1 process: Nexy:39688 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	14:52:13.324237-0500	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:58167<-><IPv4-redacted>:443] interface: en0 (skipped: 6843)
so_gencnt: 6102369 t_state: FIN_WAIT_1 process: Nexy:39688 Duration: 17.235 sec Conn_Time: 0.021 sec bytes in/out: 3360/1734 pkts in/out: 3/4 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 21.468 ms rttvar: 6.687 ms base rtt: 20 ms so_error: 0 svc/tc: 0 flow: 0x81df9cfb
default	14:52:13.324245-0500	kernel	tcp_connection_summary [<IPv4-redacted>:58167<-><IPv4-redacted>:443] interface: en0 (skipped: 6843)
so_gencnt: 6102369 t_state: FIN_WAIT_1 process: Nexy:39688 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	14:52:13.324243-0500	mDNSResponder	[R635454] DNSServiceCreateConnection STOP PID[39688](Nexy)
default	14:52:13.325819-0500	runningboardd	[app<application.com.nexy.assistant.21074037.21074043(501)>:39688] termination reported by launchd (2, 15, 15)
default	14:52:13.325858-0500	runningboardd	Removing process: [app<application.com.nexy.assistant.21074037.21074043(501)>:39688]
default	14:52:13.326131-0500	runningboardd	Removing launch job for: [app<application.com.nexy.assistant.21074037.21074043(501)>:39688]
default	14:52:13.326355-0500	runningboardd	Removed job for [app<application.com.nexy.assistant.21074037.21074043(501)>:39688]
default	14:52:13.326397-0500	runningboardd	Removing assertions for terminated process: [app<application.com.nexy.assistant.21074037.21074043(501)>:39688]
default	14:52:13.331506-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.21074037.21074043(501)>: none (role: None) (endowments: (null))
default	14:52:13.331967-0500	audiomxd	  ServerSessionManager.mm:1322  Monitored process died, pid = 39688, name = Nexy
default	14:52:13.331806-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.21074037.21074043(501)>: none (role: None) (endowments: (null))
default	14:52:13.332571-0500	gamepolicyd	Received state update for 39688 (app<application.com.nexy.assistant.21074037.21074043(501)>, none-NotVisible
default	14:52:13.332681-0500	launchservicesd	Hit the server for a process handle 8c0137200009b08 that resolved to: [app<application.com.nexy.assistant.21074037.21074043(501)>:39688]
default	14:52:13.336050-0500	loginwindow	-[ApplicationManager handleCASEvent:withData:] | CAS notification for appDeath for com.nexy.assistant with asn: LSASN:{hi=0x0;lo=0x1a7aa79} for bundle path: /Applications/Nexy.app with URL: file:///Applications/Nexy.app/
default	14:52:13.336087-0500	loginwindow	-[ApplicationManager(AppDeathHandler) appDeathCleanupHandler:forApp:] | Termination handler for: Nexy : 27765369
default	14:52:13.336162-0500	loginwindow	-[PersistentAppsSupport applicationQuit:] | for app:Nexy, _appTrackingState = 2
default	14:52:16.893537-0500	ControlCenter	Recent activity attributions changed to ["scr:com.nexy.assistant", "mic:com.nexy.assistant"]
default	14:52:16.894968-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:52:16.894984-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:52:16.895000-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	14:52:16.895010-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	14:52:16.895023-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	14:52:16.895044-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	14:52:16.895201-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	14:52:24.654324-0500	ControlCenter	Recent activity attributions changed to ["scr:com.nexy.assistant"]
default	14:53:13.338036-0500	loginwindow	-[ApplicationManager(AppDeathHandler) _appQuitTimer:] | _appQuitTimer fired for: ASN: 27765369, name: Nexy with url: file:///Applications/Nexy.app/
default	14:53:13.338272-0500	loginwindow	-[ApplicationManager(AppDeathHandler) _handleLingeringSubordinateProcesses:forApp:] | Last instance of app Nexy at /Applications/Nexy.app, handle lingering spawns.
default	14:53:13.338304-0500	loginwindow	-[ApplicationManager(AppDeathHandler) _handleLingeringSubordinateProcesses:forApp:] | Child applications for Nexy : (
)
default	14:53:13.338844-0500	loginwindow	-[ApplicationManager(AppDeathHandler) _handleLingeringSubordinateProcesses:forApp:] | App Nexy is fully cleaned up.  No user notification is necessary.  Done with handling.
