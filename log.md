default	11:13:09.620887-0500	lsd	com.nexy.assistant/Unknown Persona:5:5:1:1:Building bundle record for app
default	11:13:09.621033-0500	lsd	com.nexy.assistant/Unknown Persona:5:5:2:1:Built bundle record for app
default	11:13:09.622483-0500	lsd	com.nexy.assistant/Unknown Persona:5:4:2:1:_LSServerRegisterItemInfo result = 0
default	11:13:09.629379-0500	runningboardd	Launch request for app<application.com.nexy.assistant.20931626.20931632(501)>[0] is using uid 501 (divined from auid 501 euid 501)
default	11:13:09.629471-0500	runningboardd	Acquiring assertion targeting app<application.com.nexy.assistant.20931626.20931632(501)> from originator [osservice<com.apple.coreservices.uiagent(501)>:17422] with description <RBSAssertionDescriptor| "LS launch com.nexy.assistant" ID:398-17422-1504570 target:app<application.com.nexy.assistant.20931626.20931632(501)> attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"LaunchRoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	11:13:09.629617-0500	runningboardd	Assertion 398-17422-1504570 (target:app<application.com.nexy.assistant.20931626.20931632(501)>) will be created as active
default	11:13:09.626524-0500	dmd	Received xpc stream event (distributed notification matching) with name: com.apple.LaunchServices.applicationRegistered user info: {
    CFBundleDisplayName = Nexy;
    bundleIDs =     (
        "com.nexy.assistant"
    );
    isPlaceholder = 0;
}
default	11:13:09.632827-0500	runningboardd	Checking PreventLaunch: global:0 exPath:/Applications/Nexy.app/Contents/MacOS/Nexy predicates:(null) allow:(null)
default	11:13:09.632862-0500	runningboardd	Creating and launching job for: app<application.com.nexy.assistant.20931626.20931632(501)>
default	11:13:09.632877-0500	runningboardd	_mutateContextIfNeeded called for com.nexy.assistant
default	11:13:09.632977-0500	runningboardd	app<application.com.nexy.assistant.20931626.20931632(501)>: -[RBPersonaManager personaForIdentity:context:personaUID:personaUniqueString:] required 0.000000 ms (wallclock); resolved to {4294967295, (null)}
default	11:13:09.666753-0500	runningboardd	[app<application.com.nexy.assistant.20931626.20931632(501)>:84850] is not RunningBoard jetsam managed.
default	11:13:09.666768-0500	runningboardd	[app<application.com.nexy.assistant.20931626.20931632(501)>:84850] This process will not be managed.
default	11:13:09.666778-0500	runningboardd	Now tracking process: [app<application.com.nexy.assistant.20931626.20931632(501)>:84850]
default	11:13:09.666914-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.20931626.20931632(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	11:13:09.667522-0500	gamepolicyd	Hit the server for a process handle 31e364c00014b72 that resolved to: [app<application.com.nexy.assistant.20931626.20931632(501)>:84850]
default	11:13:09.667556-0500	gamepolicyd	Received state update for 84850 (app<application.com.nexy.assistant.20931626.20931632(501)>, running-active-NotVisible
default	11:13:09.670932-0500	runningboardd	Using default underlying assertion for app: [app<application.com.nexy.assistant.20931626.20931632(501)>:84850]
default	11:13:09.671001-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.20931626.20931632(501)>:84850] from originator [app<application.com.nexy.assistant.20931626.20931632(501)>:84850] with description <RBSAssertionDescriptor| "RB Underlying Assertion" ID:398-398-1504571 target:84850 attributes:[
	<RBSDomainAttribute| domain:"com.apple.underlying" name:"defaultUnderlyingAppAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	11:13:09.671128-0500	runningboardd	Assertion 398-398-1504571 (target:[app<application.com.nexy.assistant.20931626.20931632(501)>:84850]) will be created as active
default	11:13:09.671307-0500	runningboardd	[app<application.com.nexy.assistant.20931626.20931632(501)>:84850] Ignoring jetsam update because this process is not memory-managed
default	11:13:09.671320-0500	runningboardd	[app<application.com.nexy.assistant.20931626.20931632(501)>:84850] Ignoring suspend because this process is not lifecycle managed
default	11:13:09.671335-0500	runningboardd	[app<application.com.nexy.assistant.20931626.20931632(501)>:84850] Set darwin role to: UserInteractive
default	11:13:09.671344-0500	runningboardd	[app<application.com.nexy.assistant.20931626.20931632(501)>:84850] Ignoring GPU update because this process is not GPU managed
default	11:13:09.671370-0500	runningboardd	[app<application.com.nexy.assistant.20931626.20931632(501)>:84850] Ignoring memory limit update because this process is not memory-managed
default	11:13:09.671431-0500	runningboardd	[app<application.com.nexy.assistant.20931626.20931632(501)>:84850] reported to RB as running
default	11:13:09.672713-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.20931626.20931632(501)>:84850] from originator [osservice<com.apple.coreservices.launchservicesd>:363] with description <RBSAssertionDescriptor| "uielement:84850" ID:398-363-1504572 target:84850 attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"RoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	11:13:09.672796-0500	runningboardd	Assertion 398-363-1504572 (target:[app<application.com.nexy.assistant.20931626.20931632(501)>:84850]) will be created as active
default	11:13:09.672869-0500	CoreServicesUIAgent	LAUNCH: 0x0-0x1972971 com.nexy.assistant starting stopped process.
default	11:13:09.673659-0500	loginwindow	-[Application updateInformation] | Got App URL: file:///Applications/Nexy.app/
default	11:13:09.674207-0500	loginwindow	-[ApplicationManager checkInAppContext:eventData:] | ApplicationManager: Checked in app : Nexy
default	11:13:09.675096-0500	runningboardd	[app<application.com.nexy.assistant.20931626.20931632(501)>:84850] Ignoring jetsam update because this process is not memory-managed
default	11:13:09.675137-0500	runningboardd	[app<application.com.nexy.assistant.20931626.20931632(501)>:84850] Ignoring suspend because this process is not lifecycle managed
default	11:13:09.675163-0500	runningboardd	[app<application.com.nexy.assistant.20931626.20931632(501)>:84850] Ignoring GPU update because this process is not GPU managed
default	11:13:09.675204-0500	runningboardd	[app<application.com.nexy.assistant.20931626.20931632(501)>:84850] Ignoring memory limit update because this process is not memory-managed
default	11:13:09.675332-0500	runningboardd	Successfully acquired underlying assertion for [app<application.com.nexy.assistant.20931626.20931632(501)>:84850]
default	11:13:09.676772-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.20931626.20931632(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	11:13:09.677017-0500	runningboardd	Invalidating assertion 398-17422-1504570 (target:app<application.com.nexy.assistant.20931626.20931632(501)>) from originator [osservice<com.apple.coreservices.uiagent(501)>:17422]
default	11:13:09.677051-0500	runningboardd	[app<application.com.nexy.assistant.20931626.20931632(501)>:84850] Ignoring jetsam update because this process is not memory-managed
default	11:13:09.677148-0500	gamepolicyd	Received state update for 84850 (app<application.com.nexy.assistant.20931626.20931632(501)>, running-active-NotVisible
default	11:13:09.677061-0500	runningboardd	[app<application.com.nexy.assistant.20931626.20931632(501)>:84850] Ignoring suspend because this process is not lifecycle managed
default	11:13:09.677100-0500	runningboardd	[app<application.com.nexy.assistant.20931626.20931632(501)>:84850] Ignoring GPU update because this process is not GPU managed
default	11:13:09.677179-0500	runningboardd	[app<application.com.nexy.assistant.20931626.20931632(501)>:84850] Ignoring memory limit update because this process is not memory-managed
default	11:13:09.679995-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.20931626.20931632(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	11:13:09.784060-0500	runningboardd	[app<application.com.nexy.assistant.20931626.20931632(501)>:84850] Ignoring jetsam update because this process is not memory-managed
default	11:13:09.784070-0500	runningboardd	[app<application.com.nexy.assistant.20931626.20931632(501)>:84850] Ignoring suspend because this process is not lifecycle managed
default	11:13:09.784079-0500	runningboardd	[app<application.com.nexy.assistant.20931626.20931632(501)>:84850] Ignoring GPU update because this process is not GPU managed
default	11:13:09.784097-0500	runningboardd	[app<application.com.nexy.assistant.20931626.20931632(501)>:84850] Ignoring memory limit update because this process is not memory-managed
default	11:13:09.787231-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.20931626.20931632(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	11:13:09.787873-0500	gamepolicyd	Received state update for 84850 (app<application.com.nexy.assistant.20931626.20931632(501)>, running-active-NotVisible
default	11:13:09.813733-0500	syspolicyd	GK evaluateScanResult: 3, PST: (path: a2cffff67b96be6e), (team: 5NKLL2CLB9), (id: com.nexy.assistant), (bundle_id: (null)), 0, 0, 1, 0, 9, 4, 1
default	11:13:09.814877-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=511.169, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=84850, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.syspolicyd, pid=511, auid=0, euid=0, binary_path=/usr/libexec/syspolicyd}, },
default	11:13:09.820573-0500	tccd	AUTHREQ_SUBJECT: msgID=511.169, subject=com.nexy.assistant,
default	11:13:09.821266-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d116100 at /Applications/Nexy.app
default	11:13:09.958687-0500	Nexy	[0x105f20380] activating connection: mach=true listener=false peer=false name=com.apple.cfprefsd.daemon
default	11:13:09.958765-0500	Nexy	[0x105f208c0] activating connection: mach=true listener=false peer=false name=com.apple.cfprefsd.agent
error	11:13:10.215588-0500	Nexy	dlsym cannot find symbol NSMakeRect in CFBundle 0x105f2beb0 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	11:13:10.215826-0500	Nexy	dlsym cannot find symbol NSMakePoint in CFBundle 0x105f2beb0 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	11:13:10.216033-0500	Nexy	dlsym cannot find symbol NSMakeSize in CFBundle 0x105f2beb0 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	11:13:10.216229-0500	Nexy	dlsym cannot find symbol NSMakeRange in CFBundle 0x105f2beb0 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
default	11:13:10.217485-0500	Nexy	[0x105f1eb80] activating connection: mach=true listener=false peer=false name=com.apple.coreservices.launchservicesd
default	11:13:10.218228-0500	Nexy	[0xaa7a1c000] activating connection: mach=true listener=false peer=false name=com.apple.analyticsd
default	11:13:10.218589-0500	Nexy	[0xaa7a1c140] activating connection: mach=true listener=false peer=false name=com.apple.pasteboard.1
default	11:13:10.219022-0500	Nexy	[0xaa7a1c280] activating connection: mach=true listener=false peer=false name=com.apple.distributed_notifications@Uv3
default	11:13:10.219784-0500	Nexy	Received configuration update from daemon (initial)
default	11:13:10.221137-0500	Nexy	void _NSDisableAutomaticTerminationAndLog(NSString *) No windows open yet
default	11:13:10.221507-0500	Nexy	[0xaa7a1c3c0] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	11:13:10.222191-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=84850.1, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=84850, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	11:13:10.223851-0500	tccd	AUTHREQ_SUBJECT: msgID=84850.1, subject=com.nexy.assistant,
default	11:13:10.224522-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d116100 at /Applications/Nexy.app
default	11:13:10.236840-0500	Nexy	[0xaa7a1c3c0] invalidated after the last release of the connection object
default	11:13:10.245922-0500	Nexy	server port 0x0000340f, session port 0x0000340f
default	11:13:10.247031-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=393.16886, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=84850, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=393, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	11:13:10.247056-0500	tccd	requestor: TCCDProcess: identifier=com.apple.WindowServer, pid=393, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=84850, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	11:13:10.248018-0500	tccd	AUTHREQ_SUBJECT: msgID=393.16886, subject=com.nexy.assistant,
default	11:13:10.248622-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d116100 at /Applications/Nexy.app
default	11:13:10.266566-0500	Nexy	New connection 0x1555d3 main
default	11:13:10.268861-0500	Nexy	CHECKIN: pid=84850
default	11:13:10.275377-0500	Nexy	CHECKEDIN: pid=84850 asn=0x0-0x1972971 foreground=0
default	11:13:10.275537-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.20931626.20931632(501)>:84850] from originator [osservice<com.apple.coreservices.launchservicesd>:363] with description <RBSAssertionDescriptor| "uielement:84850" ID:398-363-1504573 target:84850 attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"RoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	11:13:10.275268-0500	launchservicesd	CHECKIN:0x0-0x1972971 84850 com.nexy.assistant
default	11:13:10.275644-0500	runningboardd	Assertion 398-363-1504573 (target:[app<application.com.nexy.assistant.20931626.20931632(501)>:84850]) will be created as active
default	11:13:10.276123-0500	runningboardd	Invalidating assertion 398-363-1504572 (target:[app<application.com.nexy.assistant.20931626.20931632(501)>:84850]) from originator [osservice<com.apple.coreservices.launchservicesd>:363]
default	11:13:10.276264-0500	loginwindow	-[Application updateInformation] | Got App URL: file:///Applications/Nexy.app/
default	11:13:10.275625-0500	Nexy	[0xaa7a1c3c0] activating connection: mach=false listener=true peer=false name=(anonymous)
default	11:13:10.276411-0500	loginwindow	-[ApplicationManager checkInAppContext:eventData:] | ApplicationManager: Checked in app : Nexy
default	11:13:10.275635-0500	Nexy	[0xaa7a1c3c0] Connection returned listener port: 0x4d03
default	11:13:10.275949-0500	Nexy	[0xaa6bfc300] activating connection: mach=false listener=false peer=true name=com.apple.xpc.anonymous.0xaa7a1c3c0.peer[363].0xaa6bfc300
default	11:13:10.280533-0500	WindowServer	1555d3[CreateApplication]: Process creation: 0x0-0x1972971 (Nexy) connectionID: 1555D3 pid: 84850 in session 0x101
default	11:13:10.280181-0500	Nexy	FRONTLOGGING: version 1
default	11:13:10.280231-0500	Nexy	Registered, pid=84850 ASN=0x0,0x1972971
default	11:13:10.281584-0500	Nexy	[0xaa7a1c500] activating connection: mach=true listener=false peer=false name=com.apple.lsd.mapdb
default	11:13:10.281696-0500	Nexy	[0xaa7a1c3c0] Connection returned listener port: 0x4d03
default	11:13:10.282084-0500	Nexy	BringForward: pid=84850 asn=0x0-0x1972971 bringForward=0 foreground=0 uiElement=1 launchedByLS=1 modifiersCount=1 allDisabled=0
default	11:13:10.282111-0500	Nexy	BringFrontModifier: pid=84850 asn=0x0-0x1972971 Modifier 0 hideAfter=0 hideOthers=0 dontMakeFrontmost=0 mouseDown=0/0 seed=0/0
default	11:13:10.282751-0500	Nexy	Current system appearance, (HLTB: 1), (SLS: 0)
default	11:13:10.284185-0500	Nexy	No persisted cache on this platform.
default	11:13:10.285464-0500	Nexy	Current system appearance, (HLTB: 1), (SLS: 0)
default	11:13:10.286026-0500	Nexy	Post-registration system appearance: (HLTB: 1)
default	11:13:10.287938-0500	Nexy	FBSWorkspace: endpoint monitoring is disabled.
default	11:13:10.287946-0500	Nexy	FBSWorkspace: default shell endpoint is disabled.
default	11:13:10.287997-0500	Nexy	Initializing connection
default	11:13:10.288043-0500	Nexy	Removing all cached process handles
default	11:13:10.288073-0500	Nexy	Sending handshake request attempt #1 to server
default	11:13:10.288081-0500	Nexy	Creating connection to com.apple.runningboard
default	11:13:10.288089-0500	Nexy	[0xaa7a1c640] activating connection: mach=true listener=false peer=false name=com.apple.runningboard
default	11:13:10.288532-0500	Nexy	[0xaa7a1c3c0] Connection returned listener port: 0x4d03
default	11:13:10.288558-0500	runningboardd	Setting client for [app<application.com.nexy.assistant.20931626.20931632(501)>:84850] as ready
default	11:13:10.289203-0500	Nexy	Handshake succeeded
default	11:13:10.289221-0500	Nexy	Identity resolved as app<application.com.nexy.assistant.20931626.20931632(501)>
default	11:13:10.289428-0500	distnoted	register name: com.apple.xctest.FakeForceTouchDevice object: com.nexy.assistant token: 1e0000001d pid: 84850
default	11:13:10.292644-0500	Nexy	[0xaa7a1c3c0] Connection returned listener port: 0x4d03
default	11:13:10.296453-0500	Nexy	Created a new Process Instance Registry XPC connection (inactive)
default	11:13:10.296473-0500	Nexy	[0xaa7a1c780] activating connection: mach=true listener=false peer=false name=com.apple.linkd.autoShortcut
default	11:13:10.296581-0500	Nexy	Activated connection to com.apple.linkd.autoShortcut (ApplicationService)
default	11:13:10.296623-0500	Nexy	[0xaa7a1ca00] activating connection: mach=false listener=true peer=false name=(anonymous)
default	11:13:10.298608-0500	Nexy	[0xaa7a1ca00] Connection returned listener port: 0x6903
default	11:13:10.299612-0500	Nexy	Registered process with identifier 84850-2565938
default	11:13:10.520684-0500	Nexy	Registered notify signal com.apple.caulk.alloc.rtdump (0)
default	11:13:10.523439-0500	Nexy	System_Input_Processing_Notification_Handler.mm:456   System_Input_Processing_Notification_Handler::is_vi_available(): Voice isolation DSP is available for client with bundle id com.nexy.assistant (AVFoundation is available, application is not in client deny list, application is not FaceTime variant)
default	11:13:10.525439-0500	Nexy	[0xaa7a1cb40] activating connection: mach=true listener=false peer=false name=com.apple.cmio.registerassistantservice.system-extensions
fault	11:13:10.527998-0500	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.20931626.20931632 AUID=501> and <type=Application identifier=application.com.nexy.assistant.20931626.20931632>
default	11:13:10.532007-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOInitializeListenersForBundleID: for <private> -> <private>
default	11:13:10.533560-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> vpio_preferenceChangedListener: new value ((null)) for key AUVoiceIOClients/com-nexy-assistant/AUVoiceIOChatFlavor, translatedBundleID com.nexy.assistant, bundleIDs {(
    "com.nexy.assistant"
)}
default	11:13:10.533708-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> vpio_preferenceChangedListener: new value ((null)) for key AUVoiceIOClients/com-nexy-assistant/AUVoiceIOIsAutoChatFlavorEnabled, translatedBundleID com.nexy.assistant, bundleIDs {(
    "com.nexy.assistant"
)}
default	11:13:10.533830-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetSupportedChatFlavorsForBundleID: <private>-><private> get supported chat flavors: <private>
default	11:13:10.533843-0500	Nexy	            HALSystem.cpp:134    Enabling HAL Voice Isolation support
default	11:13:10.534099-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetHiddenChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	11:13:10.534224-0500	Nexy	[0xaa7a1cc80] activating connection: mach=true listener=false peer=false name=com.apple.tccd
default	11:13:10.534591-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOHiddenChatFlavors newValue: (
    1
)
default	11:13:10.535360-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=84850.2, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=84850, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	11:13:10.541984-0500	tccd	AUTHREQ_SUBJECT: msgID=84850.2, subject=com.nexy.assistant,
default	11:13:10.542570-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc37138900 at /Applications/Nexy.app
default	11:13:10.553055-0500	Nexy	[0xaa7a1cc80] invalidated after the last release of the connection object
default	11:13:10.553186-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetPreferredChatFlavorForBundleID: <private>-><private> get value: 0
default	11:13:10.553229-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetSupportedChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	11:13:10.553463-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOSupportedChatFlavors newValue: (
    0,
    2
)
default	11:13:10.554872-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.11372, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=84850, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	11:13:10.555671-0500	tccd	AUTHREQ_SUBJECT: msgID=401.11372, subject=com.nexy.assistant,
default	11:13:10.556210-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc37138900 at /Applications/Nexy.app
error	11:13:10.567075-0500	tccd	Request message contains a target_token to accessing_process (TCCDProcess: identifier=com.nexy.assistant, pid=84850, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy) but TCCDProcess: identifier=com.apple.audio.coreaudiod, pid=401, auid=202, euid=202, binary_path=/usr/sbin/coreaudiod is not a TCC manager for service: kTCCServiceScreenCapture.
default	11:13:10.568020-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.11374, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=84850, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	11:13:10.568800-0500	tccd	AUTHREQ_SUBJECT: msgID=401.11374, subject=com.nexy.assistant,
default	11:13:10.569325-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc37138900 at /Applications/Nexy.app
default	11:13:10.581754-0500	Nexy	  HALPlugInManagement.cpp:440    HALPlugInManagement::RegisterPlugIns: skipping in-process plug-ins
error	11:13:10.581948-0500	Nexy	AddInstanceForFactory: No factory registered for id <CFUUID 0xaa79a6520> F8BB1C28-BAE8-11D6-9C31-00039315CD46
error	11:13:10.604182-0500	Nexy	         HALC_ProxyObjectMap.cpp:174   HALC_ProxyObjectMap::_CopyObjectByObjectID: failed to create the local object
error	11:13:10.604191-0500	Nexy	            HALC_ShellDevice.cpp:2673  HALC_ShellDevice::RebuildControlList: couldn't find the control object
default	11:13:10.608609-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	11:13:10.608746-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	11:13:10.613892-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetPreferredChatFlavorForBundleID: <private>-><private> get value: 0
default	11:13:12.945664-0500	kernel	SK[7]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid FF555708-3C4B-4ABA-B3BF-8B2A9DB090A5 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.63085,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0xc691e221 tp_proto=0x06"
default	11:13:12.945755-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:63085<-><IPv4-redacted>:53] interface: en0 (skipped: 6843)
so_gencnt: 5933247 t_state: SYN_SENT process: Nexy:84850 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x8375952e
default	11:13:12.959001-0500	kernel	tcp connected: [<IPv4-redacted>:63085<-><IPv4-redacted>:53] interface: en0 (skipped: 6843)
so_gencnt: 5933247 t_state: ESTABLISHED process: Nexy:84850 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x8375952e
default	11:13:12.959294-0500	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:63085<-><IPv4-redacted>:53] interface: en0 (skipped: 6843)
so_gencnt: 5933247 t_state: FIN_WAIT_1 process: Nexy:84850 Duration: 0.014 sec Conn_Time: 0.014 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 14.000 ms rttvar: 7.000 ms base rtt: 14 ms so_error: 0 svc/tc: 0 flow: 0x8375952e
default	11:13:12.959302-0500	kernel	tcp_connection_summary [<IPv4-redacted>:63085<-><IPv4-redacted>:53] interface: en0 (skipped: 6843)
so_gencnt: 5933247 t_state: FIN_WAIT_1 process: Nexy:84850 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	11:13:12.988660-0500	Nexy	[0xaa7a1cc80] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioComponentRegistrar
default	11:13:13.414625-0500	Nexy	                AUHAL.cpp:420   AUHAL: (0xaa6cc0040) Selecting device 85 from constructor
default	11:13:13.414643-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0xaa6cc0040)
default	11:13:13.414653-0500	Nexy	                AUHAL.cpp:676   SelectDevice: (0xaa6cc0040) not already running
default	11:13:13.414659-0500	Nexy	                AUHAL.cpp:752   SelectDevice: (0xaa6cc0040) nothing to teardown
default	11:13:13.414665-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0xaa6cc0040) connecting device 85
default	11:13:13.414824-0500	Nexy	                AUHAL.cpp:3413  IsDeviceUsable: (0xaa6cc0040) Device ID: 85 (Input:No | Output:Yes): true
default	11:13:13.415563-0500	Nexy	                AUHAL.cpp:769   SelectDevice: (0xaa6cc0040) created ioproc 0xa for device 85
default	11:13:13.415725-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0xaa6cc0040) adding 7 device listeners to device 85
default	11:13:13.415983-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0xaa6cc0040) adding 0 device delegate listeners to device 85
default	11:13:13.415997-0500	Nexy	                AUHAL.cpp:1581  UpdateStreamFormats: -> (0xaa6cc0040)
default	11:13:13.416091-0500	Nexy	                AUHAL.cpp:1677  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  48000 Hz, Float32, interleaved
default	11:13:13.416101-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 1 output streams; not all mono
default	11:13:13.416110-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	11:13:13.416119-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 0 input streams; not all mono
default	11:13:13.416127-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	11:13:13.416263-0500	Nexy	                AUHAL.cpp:1771  UpdateStreamFormats: AUHAL(0xaa6cc0040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	11:13:13.416280-0500	Nexy	                AUHAL.cpp:1777  UpdateStreamFormats: AUHAL(0xaa6cc0040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	11:13:13.416287-0500	Nexy	                AUHAL.cpp:1787  UpdateStreamFormats: <-
default	11:13:13.416301-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0xaa6cc0040) removing 0 device listeners from device 0
default	11:13:13.416311-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0xaa6cc0040) removing 0 device delegate listeners from device 0
default	11:13:13.416317-0500	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0xaa6cc0040)
default	11:13:13.416338-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Output stream enables: Stream 0 is DISABLED
default	11:13:13.416460-0500	Nexy	                AUHAL.cpp:2298  SetProperty: (0xaa6cc0040) caller requesting device change from 85 to 91
default	11:13:13.416471-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0xaa6cc0040)
default	11:13:13.416477-0500	Nexy	                AUHAL.cpp:676   SelectDevice: (0xaa6cc0040) not already running
default	11:13:13.416487-0500	Nexy	                AUHAL.cpp:682   SelectDevice: (0xaa6cc0040) disconnecting device 85
default	11:13:13.416493-0500	Nexy	                AUHAL.cpp:746   SelectDevice: (0xaa6cc0040) destroying ioproc 0xa for device 85
default	11:13:13.416589-0500	Nexy	  AVAudioSession_MacOS.mm:1021  initForMacOS
default	11:13:13.417345-0500	Nexy	[0xaa7a1cf00] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioSession
default	11:13:13.419527-0500	audiomxd	  ServerSessionManager.mm:315   { "action":"create_session", "session":{"ID":"0x1ef2a1","name":"Nexy(84850)"}, "details":{"PID":84850,"session_type":"Primary"} }
default	11:13:13.419636-0500	audiomxd	AudioApplicationInfoImpl.mm:250   Setting initial isRecording state: 0 for newly-created AudioApp
	app: {"name":"[implicit] Nexy","pid":84850}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1ef2a1, sessionType: 'prim', isRecording: false }, 
]
default	11:13:13.420650-0500	audiomxd	  ServerSessionManager.mm:1317  Start process monitoring, pid = 84850, name = Nexy
default	11:13:13.421065-0500	Nexy	    SessionCore_Create.mm:99    Created session 0xaa64b1dc0 with ID: 0x1ef2a1
default	11:13:13.422230-0500	Nexy	[0xaa7a1d040] activating connection: mach=true listener=false peer=false name=com.apple.audioanalyticsd
error	11:13:13.422781-0500	Nexy	Reporter disconnected. { function=sendMessage, reporterID=364427975065601 }
default	11:13:13.422800-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped Unknown {1C-77-54-18-C8-A3:output, 0xa}
default	11:13:13.422875-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	11:13:13.423013-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0xaa6cc0040) connecting device 91
default	11:13:13.423142-0500	Nexy	                AUHAL.cpp:3413  IsDeviceUsable: (0xaa6cc0040) Device ID: 91 (Input:Yes | Output:No): true
default	11:13:13.425040-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.11375, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=84850, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	11:13:13.426600-0500	tccd	AUTHREQ_SUBJECT: msgID=401.11375, subject=com.nexy.assistant,
default	11:13:13.427438-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc37138900 at /Applications/Nexy.app
default	11:13:13.440177-0500	Nexy	                AUHAL.cpp:769   SelectDevice: (0xaa6cc0040) created ioproc 0xa for device 91
default	11:13:13.440314-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0xaa6cc0040) adding 7 device listeners to device 91
default	11:13:13.440510-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0xaa6cc0040) adding 0 device delegate listeners to device 91
default	11:13:13.440521-0500	Nexy	                AUHAL.cpp:1581  UpdateStreamFormats: -> (0xaa6cc0040)
default	11:13:13.440529-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 0 output streams; not all mono
default	11:13:13.440538-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Output render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	11:13:13.440686-0500	Nexy	                AUHAL.cpp:1677  UpdateStreamFormats: 
  input stream 0 [0x5c]:  1 ch,  24000 Hz, Float32
default	11:13:13.440699-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 1 input streams; all mono
default	11:13:13.440705-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Input render format:  1 ch,  24000 Hz, Float32
default	11:13:13.440790-0500	Nexy	                AUHAL.cpp:1771  UpdateStreamFormats: AUHAL(0xaa6cc0040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	11:13:13.440802-0500	Nexy	                AUHAL.cpp:1777  UpdateStreamFormats: AUHAL(0xaa6cc0040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	11:13:13.440808-0500	Nexy	                AUHAL.cpp:1787  UpdateStreamFormats: <-
default	11:13:13.440813-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0xaa6cc0040) removing 7 device listeners from device 85
default	11:13:13.440973-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0xaa6cc0040) removing 0 device delegate listeners from device 85
default	11:13:13.440982-0500	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0xaa6cc0040)
default	11:13:13.441633-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	11:13:13.442811-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.11376, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=84850, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	11:13:13.443805-0500	tccd	AUTHREQ_SUBJECT: msgID=401.11376, subject=com.nexy.assistant,
default	11:13:13.444385-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc37138900 at /Applications/Nexy.app
default	11:13:13.455554-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	11:13:13.456545-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.11377, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=84850, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	11:13:13.457436-0500	tccd	AUTHREQ_SUBJECT: msgID=401.11377, subject=com.nexy.assistant,
default	11:13:13.457992-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc37138900 at /Applications/Nexy.app
default	11:13:13.469620-0500	Nexy	Registered notify signal com.apple.caulk.alloc.audiodump (0)
default	11:13:13.471189-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.11378, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=84850, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	11:13:13.472081-0500	tccd	AUTHREQ_SUBJECT: msgID=401.11378, subject=com.nexy.assistant,
default	11:13:13.472641-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc37138900 at /Applications/Nexy.app
default	11:13:13.484373-0500	coreaudiod	>>> NEGOTIATE [com.nexy.assistant]
default	11:13:13.484520-0500	coreaudiod	<<< NEGOTIATE [com.nexy.assistant]
default	11:13:13.485750-0500	coreaudiod	>>> ADAPT [com.nexy.assistant]
default	11:13:13.487066-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xbf76a5b00] Created node ADM::com.nexy.assistant_61703.61532.0_airpods noise suppression studio::in-0 with nodeID 0 - reporting period = 10.000000, sample rate = 24000.000000
default	11:13:13.487143-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xbf76a5b00] Created node ADM::com.nexy.assistant_61703.61532.0_airpods noise suppression studio::out-0 with nodeID 1 - reporting period = 10.000000, sample rate = 24000.000000
default	11:13:13.563143-0500	coreaudiod	<<< ADAPT [com.nexy.assistant]
default	11:13:13.565886-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Input {1C-77-54-18-C8-A3:input, 0xa}
default	11:13:13.565818-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:61703 called from <private>
default	11:13:13.566214-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	11:13:13.567255-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:61703 called from <private>
default	11:13:13.567429-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(61703)
default	11:13:13.567446-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:61703 called from <private>
default	11:13:13.567454-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:61703 called from <private>
default	11:13:13.572570-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.20931626.20931632(501)>:84850] from originator [osservice<com.apple.powerd>:334] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:398-334-1504575 target:84850 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	11:13:13.573009-0500	runningboardd	Assertion 398-334-1504575 (target:[app<application.com.nexy.assistant.20931626.20931632(501)>:84850]) will be created as active
default	11:13:13.568080-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(61702)
default	11:13:13.568469-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:61702 called from <private>
default	11:13:13.568514-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:61702 called from <private>
default	11:13:13.574227-0500	runningboardd	[app<application.com.nexy.assistant.20931626.20931632(501)>:84850] Ignoring jetsam update because this process is not memory-managed
default	11:13:13.574533-0500	runningboardd	[app<application.com.nexy.assistant.20931626.20931632(501)>:84850] Ignoring suspend because this process is not lifecycle managed
default	11:13:13.574968-0500	runningboardd	[app<application.com.nexy.assistant.20931626.20931632(501)>:84850] Ignoring GPU update because this process is not GPU managed
default	11:13:13.575229-0500	runningboardd	[app<application.com.nexy.assistant.20931626.20931632(501)>:84850] Ignoring memory limit update because this process is not memory-managed
fault	11:13:13.576065-0500	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.20931626.20931632 AUID=501> and <type=Application identifier=application.com.nexy.assistant.20931626.20931632>
default	11:13:13.576925-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	11:13:13.577433-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
fault	11:13:13.578823-0500	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.20931626.20931632 AUID=501> and <type=Application identifier=application.com.nexy.assistant.20931626.20931632>
default	11:13:13.580326-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.20931626.20931632(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	11:13:13.580765-0500	runningboardd	Invalidating assertion 398-334-1504575 (target:[app<application.com.nexy.assistant.20931626.20931632(501)>:84850]) from originator [osservice<com.apple.powerd>:334]
default	11:13:13.583137-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(61703)
default	11:13:13.583170-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(61703)
default	11:13:13.583182-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(61703)
default	11:13:13.583220-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(61703)
default	11:13:13.583818-0500	gamepolicyd	Received state update for 84850 (app<application.com.nexy.assistant.20931626.20931632(501)>, running-active-NotVisible
default	11:13:13.587209-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:61703 called from <private>
default	11:13:13.587227-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:61703 called from <private>
default	11:13:13.587235-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:61703 called from <private>
default	11:13:13.587240-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:61703 called from <private>
default	11:13:13.587249-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:61703 called from <private>
default	11:13:13.587253-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:61703 called from <private>
default	11:13:13.587258-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:61703 called from <private>
default	11:13:13.587270-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:61703 called from <private>
default	11:13:13.587326-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:61703 called from <private>
default	11:13:13.587362-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:61703 called from <private>
default	11:13:13.587599-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ef2a1","name":"Nexy(84850)"}, "details":{"deviceUIDs":["1C-77-54-18-C8-A3:input"],"implicit_category":"Record","input_running":true,"output_running":false} }
default	11:13:13.587699-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 674, PID = 84850, Name = sid:0x1ef2a1, Nexy(84850), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	11:13:13.587784-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 674, PID = 84850, Name = sid:0x1ef2a1, Nexy(84850), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	11:13:13.587866-0500	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1ef2a1, Nexy(84850), 'prim'', AudioCategory changed to 'Record_WithBluetooth'
default	11:13:13.587908-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 674, PID = 84850, Name = sid:0x1ef2a1, Nexy(84850), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	11:13:13.587938-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 674, PID = 84850, Name = sid:0x1ef2a1, Nexy(84850), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	11:13:13.587939-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	11:13:13.587994-0500	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 674, PID = 84850, Name = sid:0x1ef2a1, Nexy(84850), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> is going active
default	11:13:13.588009-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1ef2a1, Nexy(84850), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 674 starting recording
default	11:13:13.588056-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	11:13:13.588370-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	11:13:13.588448-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	11:13:13.588520-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 674, PID = 84850, Name = sid:0x1ef2a1, Nexy(84850), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	11:13:13.588550-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 674, PID = 84850, Name = sid:0x1ef2a1, Nexy(84850), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	11:13:13.588720-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [1, 0]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:input"
)}
default	11:13:13.588574-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1ef2a1, Nexy(84850), 'prim'', displayID:'com.nexy.assistant'}
default	11:13:13.588735-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	11:13:13.588680-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	11:13:13.596381-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(61703)
default	11:13:13.596400-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:61703 called from <private>
default	11:13:13.598438-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(61702)
default	11:13:13.599704-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.11379, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=84850, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	11:13:13.599848-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:61702 called from <private>
default	11:13:13.599860-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:61702 called from <private>
default	11:13:13.601970-0500	tccd	AUTHREQ_SUBJECT: msgID=401.11379, subject=com.nexy.assistant,
default	11:13:13.603351-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc37138900 at /Applications/Nexy.app
default	11:13:13.609303-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:61702 called from <private>
default	11:13:13.609321-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:61702 called from <private>
default	11:13:13.609458-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(61702)
default	11:13:13.610690-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(61702)
default	11:13:13.610985-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:61702 called from <private>
default	11:13:13.610996-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:61702 called from <private>
default	11:13:13.611103-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(61702)
default	11:13:13.615220-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	11:13:13.615362-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	11:13:13.615519-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	11:13:13.618186-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(61702)
default	11:13:13.617553-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:13:13.618779-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:61702 called from <private>
default	11:13:13.618793-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:61702 called from <private>
default	11:13:13.619059-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:61702 called from <private>
default	11:13:13.617614-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:13:13.619069-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:61702 called from <private>
default	11:13:13.619085-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:61702 called from <private>
default	11:13:13.619092-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:61702 called from <private>
default	11:13:13.617772-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	11:13:13.619102-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:61702 called from <private>
default	11:13:13.619136-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:61702 called from <private>
default	11:13:13.617943-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:13:13.619189-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:61702 called from <private>
default	11:13:13.618356-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	11:13:13.619189-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(61702)
default	11:13:13.618666-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	11:13:13.619283-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:61702 called from <private>
default	11:13:13.619345-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:61702 called from <private>
default	11:13:13.619376-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:61702 called from <private>
default	11:13:13.619694-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	11:13:13.619415-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:61702 called from <private>
default	11:13:13.619492-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:61702 called from <private>
default	11:13:13.619546-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:61702 called from <private>
default	11:13:13.619597-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:61702 called from <private>
default	11:13:13.629043-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(61702)
default	11:13:13.629255-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:61702 called from <private>
default	11:13:13.629261-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:61702 called from <private>
default	11:13:13.629271-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:61702 called from <private>
default	11:13:13.629280-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:61702 called from <private>
default	11:13:13.637835-0500	coreaudiod	>>> NEGOTIATE [com.nexy.assistant]
default	11:13:13.647797-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	11:13:13.648520-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	11:13:13.673968-0500	coreaudiod	>>> ADAPT [com.nexy.assistant]
default	11:13:13.675101-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xbf76f4300] Created node ADM::com.nexy.assistant_61703.61532.0_airpods noise suppression studio::in-0 with nodeID 0 - reporting period = 10.000000, sample rate = 24000.000000
default	11:13:13.675165-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xbf76f4300] Created node ADM::com.nexy.assistant_61703.61532.0_airpods noise suppression studio::out-0 with nodeID 1 - reporting period = 10.000000, sample rate = 24000.000000
default	11:13:13.678884-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	11:13:13.687005-0500	runningboardd	[app<application.com.nexy.assistant.20931626.20931632(501)>:84850] Ignoring jetsam update because this process is not memory-managed
default	11:13:13.687017-0500	runningboardd	[app<application.com.nexy.assistant.20931626.20931632(501)>:84850] Ignoring suspend because this process is not lifecycle managed
default	11:13:13.687028-0500	runningboardd	[app<application.com.nexy.assistant.20931626.20931632(501)>:84850] Ignoring GPU update because this process is not GPU managed
default	11:13:13.687093-0500	runningboardd	[app<application.com.nexy.assistant.20931626.20931632(501)>:84850] Ignoring memory limit update because this process is not memory-managed
default	11:13:13.693299-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:13:13.693310-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:13:13.693317-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	11:13:13.693324-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:13:13.693330-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	11:13:13.693336-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	11:13:13.693455-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	11:13:13.709470-0500	coreaudiod	<<< ADAPT [com.nexy.assistant]
default	11:13:13.712779-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:61703 called from <private>
default	11:13:13.713526-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:61703 called from <private>
default	11:13:13.714862-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.20931626.20931632(501)>:84850] from originator [osservice<com.apple.powerd>:334] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:398-334-1504577 target:84850 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	11:13:13.713627-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	11:13:13.714931-0500	runningboardd	Assertion 398-334-1504577 (target:[app<application.com.nexy.assistant.20931626.20931632(501)>:84850]) will be created as active
default	11:13:13.715769-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:61703 called from <private>
default	11:13:13.715946-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(61703)
default	11:13:13.715966-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:61703 called from <private>
default	11:13:13.715974-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:61703 called from <private>
default	11:13:13.716154-0500	runningboardd	[app<application.com.nexy.assistant.20931626.20931632(501)>:84850] Ignoring jetsam update because this process is not memory-managed
default	11:13:13.716218-0500	runningboardd	[app<application.com.nexy.assistant.20931626.20931632(501)>:84850] Ignoring suspend because this process is not lifecycle managed
default	11:13:13.716259-0500	runningboardd	[app<application.com.nexy.assistant.20931626.20931632(501)>:84850] Ignoring GPU update because this process is not GPU managed
default	11:13:13.716377-0500	runningboardd	[app<application.com.nexy.assistant.20931626.20931632(501)>:84850] Ignoring memory limit update because this process is not memory-managed
default	11:13:13.717144-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	11:13:13.717295-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	11:13:13.717772-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(61703)
default	11:13:13.721268-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.20931626.20931632(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	11:13:13.721597-0500	runningboardd	Invalidating assertion 398-334-1504577 (target:[app<application.com.nexy.assistant.20931626.20931632(501)>:84850]) from originator [osservice<com.apple.powerd>:334]
default	11:13:13.721970-0500	tccd	AUTHREQ_SUBJECT: msgID=401.11381, subject=com.nexy.assistant,
default	11:13:13.722760-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc37138900 at /Applications/Nexy.app
default	11:13:13.735379-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	11:13:13.735425-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	11:13:13.735469-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	11:13:13.735876-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:13:13.735893-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:13:13.735919-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	11:13:13.735929-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:13:13.735938-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	11:13:13.735945-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	11:13:13.736001-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:13:13.736012-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:13:13.736021-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	11:13:13.736028-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:13:13.736032-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	11:13:13.736036-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	11:13:13.736068-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	11:13:13.737191-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:13:13.737206-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:13:13.737215-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	11:13:13.737226-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:13:13.737232-0500	ControlCenter	Navigating to new application [com.nexy.assistant]
default	11:13:13.737232-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	11:13:13.737242-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	11:13:13.753146-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	11:13:13.762583-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:13:13.762602-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:13:13.762612-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	11:13:13.762618-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:13:13.762624-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	11:13:13.762629-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	11:13:13.762710-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	11:13:13.768874-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	11:13:13.768996-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	11:13:13.769062-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	11:13:13.782020-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:13:13.782033-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:13:13.782047-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	11:13:13.782052-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:13:13.782058-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	11:13:13.782064-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	11:13:13.782141-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	11:13:13.782123-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:13:13.782182-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:13:13.782193-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	11:13:13.782200-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:13:13.782207-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	11:13:13.782216-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	11:13:13.782618-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:13:13.782628-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:13:13.782634-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	11:13:13.782639-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:13:13.782646-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	11:13:13.782650-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	11:13:13.782675-0500	ControlCenter	Navigating to new application [com.nexy.assistant]
default	11:13:13.794877-0500	gamepolicyd	Received state update for 84850 (app<application.com.nexy.assistant.20931626.20931632(501)>, running-active-NotVisible
default	11:13:14.766578-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xa}
default	11:13:14.767030-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ef2a1","name":"Nexy(84850)"}, "details":{"deviceUIDs":[],"implicit_category":"","input_running":false,"output_running":false} }
default	11:13:14.767175-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 674, PID = 84850, Name = sid:0x1ef2a1, Nexy(84850), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	11:13:14.767242-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 674, PID = 84850, Name = sid:0x1ef2a1, Nexy(84850), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	11:13:14.767277-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1ef2a1, Nexy(84850), 'prim'', displayID:'com.nexy.assistant'}
default	11:13:14.767344-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	11:13:14.767348-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1ef2a1, Nexy(84850), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 674 stopping recording
default	11:13:14.767373-0500	audiomxd	-MXCoreSession- -[MXCoreSession endInterruption:]: Session <ID: 674, PID = 84850, Name = sid:0x1ef2a1, Nexy(84850), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> is going inactive
default	11:13:14.767400-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 674, PID = 84850, Name = sid:0x1ef2a1, Nexy(84850), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	11:13:14.767430-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 674, PID = 84850, Name = sid:0x1ef2a1, Nexy(84850), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	11:13:14.767541-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 0]. BT device UIDS: {(
)}
default	11:13:14.767556-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	11:13:14.767682-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 200 flag 0x1 < Hijack > app com.nexy.assistant CID 0xD310001 category Not set
default	11:13:14.767923-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	11:13:14.767961-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	11:13:14.768013-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	11:13:14.768043-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	11:13:14.768057-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	11:13:14.768074-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	11:13:14.768152-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	11:13:14.768167-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	11:13:14.768177-0500	audioaccessoryd	AudioStateChanged: Removed audio session app com.nexy.assistant 201 count 0
default	11:13:14.771441-0500	runningboardd	Invalidating assertion 398-334-1504578 (target:[app<application.com.nexy.assistant.20931626.20931632(501)>:84850]) from originator [osservice<com.apple.powerd>:334]
default	11:13:14.788971-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	11:13:14.789591-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:13:14.789606-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:13:14.789622-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	11:13:14.789628-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:13:14.789635-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	11:13:14.789642-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	11:13:14.789796-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	11:13:14.868993-0500	Nexy	                AUHAL.cpp:473   ~AUHAL: (0xaa6cc0040) Selecting device 0 from destructor
default	11:13:14.869031-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0xaa6cc0040)
default	11:13:14.869060-0500	Nexy	                AUHAL.cpp:676   SelectDevice: (0xaa6cc0040) not already running
default	11:13:14.869079-0500	Nexy	                AUHAL.cpp:682   SelectDevice: (0xaa6cc0040) disconnecting device 91
default	11:13:14.869093-0500	Nexy	                AUHAL.cpp:746   SelectDevice: (0xaa6cc0040) destroying ioproc 0xa for device 91
default	11:13:14.869153-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xa}
default	11:13:14.869219-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	11:13:14.869527-0500	Nexy	                AUHAL.cpp:848   SelectDevice: (0xaa6cc0040) nothing to setup
default	11:13:14.869543-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0xaa6cc0040) adding 0 device listeners to device 0
default	11:13:14.869549-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0xaa6cc0040) adding 0 device delegate listeners to device 0
default	11:13:14.869559-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0xaa6cc0040) removing 7 device listeners from device 91
default	11:13:14.869792-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0xaa6cc0040) removing 0 device delegate listeners from device 91
default	11:13:14.869811-0500	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0xaa6cc0040)
default	11:13:14.878401-0500	runningboardd	[app<application.com.nexy.assistant.20931626.20931632(501)>:84850] Ignoring jetsam update because this process is not memory-managed
default	11:13:14.878418-0500	runningboardd	[app<application.com.nexy.assistant.20931626.20931632(501)>:84850] Ignoring suspend because this process is not lifecycle managed
default	11:13:14.878433-0500	runningboardd	[app<application.com.nexy.assistant.20931626.20931632(501)>:84850] Ignoring GPU update because this process is not GPU managed
default	11:13:14.878463-0500	runningboardd	[app<application.com.nexy.assistant.20931626.20931632(501)>:84850] Ignoring memory limit update because this process is not memory-managed
default	11:13:14.884152-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.20931626.20931632(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	11:13:14.884721-0500	runningboardd	Assertion did invalidate due to timeout: 398-398-1504571 (target:[app<application.com.nexy.assistant.20931626.20931632(501)>:84850])
default	11:13:14.884960-0500	gamepolicyd	Received state update for 84850 (app<application.com.nexy.assistant.20931626.20931632(501)>, running-active-NotVisible
default	11:13:15.039340-0500	runningboardd	[app<application.com.nexy.assistant.20931626.20931632(501)>:84850] Ignoring jetsam update because this process is not memory-managed
default	11:13:15.039350-0500	runningboardd	[app<application.com.nexy.assistant.20931626.20931632(501)>:84850] Ignoring suspend because this process is not lifecycle managed
default	11:13:15.039359-0500	runningboardd	[app<application.com.nexy.assistant.20931626.20931632(501)>:84850] Ignoring GPU update because this process is not GPU managed
default	11:13:15.039417-0500	runningboardd	[app<application.com.nexy.assistant.20931626.20931632(501)>:84850] Ignoring memory limit update because this process is not memory-managed
default	11:13:15.041979-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.20931626.20931632(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	11:13:15.042367-0500	gamepolicyd	Received state update for 84850 (app<application.com.nexy.assistant.20931626.20931632(501)>, running-active-NotVisible
default	11:13:15.092557-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=84854.1, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=84850, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.osascript, pid=84854, auid=501, euid=501, binary_path=/usr/bin/osascript}, },
default	11:13:15.093940-0500	tccd	AUTHREQ_SUBJECT: msgID=84854.1, subject=com.nexy.assistant,
default	11:13:15.094516-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d116100 at /Applications/Nexy.app
default	11:13:15.107819-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=393.16888, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=84850, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.osascript, pid=84854, auid=501, euid=501, binary_path=/usr/bin/osascript}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=393, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	11:13:15.108844-0500	tccd	AUTHREQ_SUBJECT: msgID=393.16888, subject=com.nexy.assistant,
default	11:13:15.109457-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d116100 at /Applications/Nexy.app
default	11:13:15.142365-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d116100 at /Applications/Nexy.app
default	11:13:15.278964-0500	System Events	TCCAccessRequestIndirect: TCCAccessRequestIndirect with pid 84855: target_identity: {
    kTCCCodeIdentityAuditToken = {length = 32, bytes = 0xf5010000 f5010000 14000000 f5010000 ... b7860100 3d272700 };
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
default	11:13:15.291188-0500	tccd	target_executable_path_URL: file:///Applications/Nexy.app/Contents/MacOS/Nexy
default	11:13:15.533790-0500	Nexy	[0xaa7a1d2c0] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	11:13:15.534533-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=84850.3, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=84850, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	11:13:15.535782-0500	tccd	AUTHREQ_SUBJECT: msgID=84850.3, subject=com.nexy.assistant,
default	11:13:15.536428-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d116100 at /Applications/Nexy.app
default	11:13:15.549500-0500	Nexy	[0xaa7a1d2c0] invalidated after the last release of the connection object
default	11:13:15.553066-0500	Nexy	                AUHAL.cpp:420   AUHAL: (0xaa6cc0040) Selecting device 85 from constructor
default	11:13:15.553081-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0xaa6cc0040)
default	11:13:15.553087-0500	Nexy	                AUHAL.cpp:676   SelectDevice: (0xaa6cc0040) not already running
default	11:13:15.553092-0500	Nexy	                AUHAL.cpp:752   SelectDevice: (0xaa6cc0040) nothing to teardown
default	11:13:15.553097-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0xaa6cc0040) connecting device 85
default	11:13:15.553214-0500	Nexy	                AUHAL.cpp:3413  IsDeviceUsable: (0xaa6cc0040) Device ID: 85 (Input:No | Output:Yes): true
default	11:13:15.553343-0500	Nexy	                AUHAL.cpp:769   SelectDevice: (0xaa6cc0040) created ioproc 0xb for device 85
default	11:13:15.553497-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0xaa6cc0040) adding 7 device listeners to device 85
default	11:13:15.553695-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0xaa6cc0040) adding 0 device delegate listeners to device 85
default	11:13:15.553704-0500	Nexy	                AUHAL.cpp:1581  UpdateStreamFormats: -> (0xaa6cc0040)
default	11:13:15.553791-0500	Nexy	                AUHAL.cpp:1677  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  24000 Hz, Float32, interleaved
default	11:13:15.553802-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 1 output streams; not all mono
default	11:13:15.553807-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Output render format:  2 ch,  24000 Hz, Float32, interleaved
default	11:13:15.553813-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 0 input streams; not all mono
default	11:13:15.553822-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	11:13:15.553920-0500	Nexy	                AUHAL.cpp:1771  UpdateStreamFormats: AUHAL(0xaa6cc0040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	11:13:15.553930-0500	Nexy	                AUHAL.cpp:1777  UpdateStreamFormats: AUHAL(0xaa6cc0040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	11:13:15.553934-0500	Nexy	                AUHAL.cpp:1787  UpdateStreamFormats: <-
default	11:13:15.553937-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0xaa6cc0040) removing 0 device listeners from device 0
default	11:13:15.553941-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0xaa6cc0040) removing 0 device delegate listeners from device 0
default	11:13:15.553946-0500	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0xaa6cc0040)
default	11:13:15.553965-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Output stream enables: Stream 0 is DISABLED
default	11:13:15.554029-0500	Nexy	                AUHAL.cpp:2298  SetProperty: (0xaa6cc0040) caller requesting device change from 85 to 91
default	11:13:15.554037-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0xaa6cc0040)
default	11:13:15.554050-0500	Nexy	                AUHAL.cpp:676   SelectDevice: (0xaa6cc0040) not already running
default	11:13:15.554058-0500	Nexy	                AUHAL.cpp:682   SelectDevice: (0xaa6cc0040) disconnecting device 85
default	11:13:15.554064-0500	Nexy	                AUHAL.cpp:746   SelectDevice: (0xaa6cc0040) destroying ioproc 0xb for device 85
default	11:13:15.554086-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped Unknown {1C-77-54-18-C8-A3:output, 0xb}
default	11:13:15.554133-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	11:13:15.554212-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0xaa6cc0040) connecting device 91
default	11:13:15.554286-0500	Nexy	                AUHAL.cpp:3413  IsDeviceUsable: (0xaa6cc0040) Device ID: 91 (Input:Yes | Output:No): true
default	11:13:15.555650-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.11382, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=84850, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	11:13:15.556863-0500	tccd	AUTHREQ_SUBJECT: msgID=401.11382, subject=com.nexy.assistant,
default	11:13:15.557547-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc37138900 at /Applications/Nexy.app
default	11:13:15.569596-0500	Nexy	                AUHAL.cpp:769   SelectDevice: (0xaa6cc0040) created ioproc 0xb for device 91
default	11:13:15.569758-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0xaa6cc0040) adding 7 device listeners to device 91
default	11:13:15.569964-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0xaa6cc0040) adding 0 device delegate listeners to device 91
default	11:13:15.569977-0500	Nexy	                AUHAL.cpp:1581  UpdateStreamFormats: -> (0xaa6cc0040)
default	11:13:15.569987-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 0 output streams; not all mono
default	11:13:15.569998-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Output render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	11:13:15.570152-0500	Nexy	                AUHAL.cpp:1677  UpdateStreamFormats: 
  input stream 0 [0x5c]:  1 ch,  24000 Hz, Float32
default	11:13:15.570163-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 1 input streams; all mono
default	11:13:15.570169-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Input render format:  1 ch,  24000 Hz, Float32
default	11:13:15.570270-0500	Nexy	                AUHAL.cpp:1771  UpdateStreamFormats: AUHAL(0xaa6cc0040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	11:13:15.570283-0500	Nexy	                AUHAL.cpp:1777  UpdateStreamFormats: AUHAL(0xaa6cc0040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	11:13:15.570290-0500	Nexy	                AUHAL.cpp:1787  UpdateStreamFormats: <-
default	11:13:15.570293-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0xaa6cc0040) removing 7 device listeners from device 85
default	11:13:15.570462-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0xaa6cc0040) removing 0 device delegate listeners from device 85
default	11:13:15.570473-0500	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0xaa6cc0040)
default	11:13:15.571093-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	11:13:15.572324-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.11383, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=84850, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	11:13:15.573282-0500	tccd	AUTHREQ_SUBJECT: msgID=401.11383, subject=com.nexy.assistant,
default	11:13:15.573997-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc37138900 at /Applications/Nexy.app
default	11:13:15.586456-0500	Nexy	       ACv2Workarounds.mm:51    com.nexy.assistant: fix84702776_86723525_86479548_89800354_SinglePacketDesc: false
default	11:13:15.586610-0500	Nexy	       AudioConverter.cpp:1042  Created a new in process converter -> 0xaa5f92a60, from  1 ch,  24000 Hz, Float32 to  1 ch,  16000 Hz, Float32
default	11:13:15.586854-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	11:13:15.588084-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.11384, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=84850, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	11:13:15.589071-0500	tccd	AUTHREQ_SUBJECT: msgID=401.11384, subject=com.nexy.assistant,
default	11:13:15.589675-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc37138900 at /Applications/Nexy.app
default	11:13:15.603997-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.11385, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=84850, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	11:13:15.604964-0500	tccd	AUTHREQ_SUBJECT: msgID=401.11385, subject=com.nexy.assistant,
default	11:13:15.605528-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc37138900 at /Applications/Nexy.app
default	11:13:15.622997-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ef2a1","name":"Nexy(84850)"}, "details":{"deviceUIDs":["1C-77-54-18-C8-A3:input"],"implicit_category":"Record","input_running":true,"output_running":false} }
default	11:13:15.623116-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 674, PID = 84850, Name = sid:0x1ef2a1, Nexy(84850), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	11:13:15.623152-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Category/Mode changed -- The score for sid:0x1ef2a1, Nexy(84850), 'prim'/com.nexy.assistant was not correct. Old score = 201
default	11:13:15.621891-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Input {1C-77-54-18-C8-A3:input, 0xb}
default	11:13:15.623188-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 674, PID = 84850, Name = sid:0x1ef2a1, Nexy(84850), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	11:13:15.625946-0500	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1ef2a1, Nexy(84850), 'prim'', AudioCategory changed to 'Record_WithBluetooth'
default	11:13:15.626250-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	11:13:15.626630-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	11:13:15.626322-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 674, PID = 84850, Name = sid:0x1ef2a1, Nexy(84850), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	11:13:15.626442-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 674, PID = 84850, Name = sid:0x1ef2a1, Nexy(84850), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	11:13:15.626686-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	11:13:15.626684-0500	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 674, PID = 84850, Name = sid:0x1ef2a1, Nexy(84850), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> is going active
default	11:13:15.626863-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.20931626.20931632(501)>:84850] from originator [osservice<com.apple.powerd>:334] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:398-334-1504587 target:84850 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	11:13:15.626667-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	11:13:15.626705-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1ef2a1, Nexy(84850), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 674 starting recording
default	11:13:15.626945-0500	runningboardd	Assertion 398-334-1504587 (target:[app<application.com.nexy.assistant.20931626.20931632(501)>:84850]) will be created as active
default	11:13:15.626810-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	11:13:15.626835-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	11:13:15.626929-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 674, PID = 84850, Name = sid:0x1ef2a1, Nexy(84850), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	11:13:15.627022-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 674, PID = 84850, Name = sid:0x1ef2a1, Nexy(84850), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	11:13:15.627187-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1ef2a1, Nexy(84850), 'prim'', displayID:'com.nexy.assistant'}
default	11:13:15.627367-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [1, 0]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:input"
)}
default	11:13:15.627300-0500	runningboardd	[app<application.com.nexy.assistant.20931626.20931632(501)>:84850] Ignoring jetsam update because this process is not memory-managed
default	11:13:15.627342-0500	runningboardd	[app<application.com.nexy.assistant.20931626.20931632(501)>:84850] Ignoring suspend because this process is not lifecycle managed
default	11:13:15.627341-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	11:13:15.627382-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	11:13:15.627368-0500	runningboardd	[app<application.com.nexy.assistant.20931626.20931632(501)>:84850] Ignoring GPU update because this process is not GPU managed
default	11:13:15.627702-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 200 flag 0x1 < Hijack > app com.nexy.assistant CID 0xD310001 category Not set
default	11:13:15.627659-0500	runningboardd	[app<application.com.nexy.assistant.20931626.20931632(501)>:84850] Ignoring memory limit update because this process is not memory-managed
default	11:13:15.627882-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	11:13:15.627959-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	11:13:15.627980-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	11:13:15.627990-0500	audioaccessoryd	AudioStateChanged: Added audio session app com.nexy.assistant NULL -> 200 count 1
default	11:13:15.628056-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
error	11:13:15.628128-0500	audioaccessoryd	Updating local audio category 100 -> 200 app com.nexy.assistant
error	11:13:15.628251-0500	audioaccessoryd	Relaying via 24B92680-715A-E821-B5AF-358E78C2DAF9 inWxAddress 1C:77:54:18:C8:A3 to 88:20:0D:45:06:51 with options {
    "playingApp" : "com.nexy.assistant",
    "hostStreamingState" : "YES",
    "btAddress" : "A0:9A:8E:0D:58:86",
    "btName" : "Mac",
    "otherDeviceAudioCategory" : 200,
}
default	11:13:15.628371-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	11:13:15.631886-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.20931626.20931632(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	11:13:15.632479-0500	gamepolicyd	Received state update for 84850 (app<application.com.nexy.assistant.20931626.20931632(501)>, running-active-NotVisible
default	11:13:15.643508-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	11:13:15.643605-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	11:13:15.643671-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	11:13:15.644396-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:13:15.644418-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:13:15.644435-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	11:13:15.644447-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:13:15.644495-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	11:13:15.644530-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	11:13:15.644567-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:13:15.644639-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:13:15.644695-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	11:13:15.644747-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:13:15.644817-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	11:13:15.644865-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	11:13:15.644963-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	11:13:15.645334-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:13:15.645347-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:13:15.645355-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	11:13:15.645363-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:13:15.645370-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	11:13:15.645378-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	11:13:15.645423-0500	ControlCenter	Navigating to new application [com.nexy.assistant]
default	11:13:18.029990-0500	audioaccessoryd	AudioStateSnapshot: Route:Bluetooth App com.nexy.assistant, Score 200, Remote 100NumofApp 1
default	11:13:20.315701-0500	Nexy	NotifyToken::RegisterDispatch(user.uid.501.com.apple.LaunchServices.database) fired for session key <private>
default	11:13:21.032098-0500	audioaccessoryd	AudioStateSnapshot: Route:Bluetooth App com.nexy.assistant, Score 200, Remote 100NumofApp 1
default	11:13:21.286277-0500	Nexy	LSExceptions shared instance invalidated for timeout.
default	11:13:22.457633-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	11:13:22.457755-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	11:13:24.032222-0500	audioaccessoryd	AudioStateSnapshot: Route:Bluetooth App com.nexy.assistant, Score 200, Remote 100NumofApp 1
default	11:13:24.602432-0500	coreaudiod	IssueReporting.cpp:492   RTAID [ use_case=Generic report_type=RMS Generic Chain clientID=ADM node=ADM::com.nexy.assistant_61703.61532.0_airpods noise suppression studio::in-0 issue_detected_sample_time=0.000000 ] -- [ rms:[-36.528122], peaks:[-13.807059] ]
default	11:13:24.605396-0500	coreaudiod	IssueReporting.cpp:492   RTAID [ use_case=Generic report_type=RMS Generic Chain clientID=ADM node=ADM::com.nexy.assistant_61703.61532.0_airpods noise suppression studio::out-0 issue_detected_sample_time=240000.000000 ] -- [ rms:[-38.870922], peaks:[-11.629615] ]
default	11:13:27.031661-0500	audioaccessoryd	AudioStateSnapshot: Route:Bluetooth App com.nexy.assistant, Score 200, Remote 100NumofApp 1
default	11:13:28.651161-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xb}
default	11:13:28.651675-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ef2a1","name":"Nexy(84850)"}, "details":{"deviceUIDs":[],"implicit_category":"","input_running":false,"output_running":false} }
default	11:13:28.651984-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 674, PID = 84850, Name = sid:0x1ef2a1, Nexy(84850), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	11:13:28.652113-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 674, PID = 84850, Name = sid:0x1ef2a1, Nexy(84850), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	11:13:28.652194-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1ef2a1, Nexy(84850), 'prim'', displayID:'com.nexy.assistant'}
default	11:13:28.652306-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	11:13:28.652367-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1ef2a1, Nexy(84850), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 674 stopping recording
default	11:13:28.652450-0500	audiomxd	-MXCoreSession- -[MXCoreSession endInterruption:]: Session <ID: 674, PID = 84850, Name = sid:0x1ef2a1, Nexy(84850), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> is going inactive
default	11:13:28.652518-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 674, PID = 84850, Name = sid:0x1ef2a1, Nexy(84850), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	11:13:28.652657-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 674, PID = 84850, Name = sid:0x1ef2a1, Nexy(84850), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	11:13:28.653301-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 0]. BT device UIDS: {(
)}
default	11:13:28.653325-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	11:13:28.653698-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 200 flag 0x1 < Hijack > app com.nexy.assistant CID 0xD310001 category Not set
default	11:13:28.659317-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	11:13:28.659470-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	11:13:28.659508-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	11:13:28.659647-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	11:13:28.660007-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	11:13:28.660304-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	11:13:28.660348-0500	audioaccessoryd	AudioStateChanged: Removed audio session app com.nexy.assistant 201 count 0
default	11:13:28.660114-0500	runningboardd	Invalidating assertion 398-334-1504587 (target:[app<application.com.nexy.assistant.20931626.20931632(501)>:84850]) from originator [osservice<com.apple.powerd>:334]
default	11:13:28.656467-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	11:13:28.656563-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	11:13:28.677810-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	11:13:28.678596-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:13:28.678611-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:13:28.678633-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	11:13:28.678643-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:13:28.678652-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	11:13:28.678658-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	11:13:28.678772-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	11:13:28.752778-0500	Nexy	                AUHAL.cpp:473   ~AUHAL: (0xaa6cc0040) Selecting device 0 from destructor
default	11:13:28.752800-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0xaa6cc0040)
default	11:13:28.752813-0500	Nexy	                AUHAL.cpp:676   SelectDevice: (0xaa6cc0040) not already running
default	11:13:28.752820-0500	Nexy	                AUHAL.cpp:682   SelectDevice: (0xaa6cc0040) disconnecting device 91
default	11:13:28.752839-0500	Nexy	                AUHAL.cpp:746   SelectDevice: (0xaa6cc0040) destroying ioproc 0xb for device 91
default	11:13:28.752882-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xb}
default	11:13:28.752923-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	11:13:28.753134-0500	Nexy	                AUHAL.cpp:848   SelectDevice: (0xaa6cc0040) nothing to setup
default	11:13:28.753146-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0xaa6cc0040) adding 0 device listeners to device 0
default	11:13:28.753154-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0xaa6cc0040) adding 0 device delegate listeners to device 0
default	11:13:28.753163-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0xaa6cc0040) removing 7 device listeners from device 91
default	11:13:28.753436-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0xaa6cc0040) removing 0 device delegate listeners from device 91
default	11:13:28.753452-0500	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0xaa6cc0040)
default	11:13:28.766824-0500	runningboardd	[app<application.com.nexy.assistant.20931626.20931632(501)>:84850] Ignoring jetsam update because this process is not memory-managed
default	11:13:28.766863-0500	runningboardd	[app<application.com.nexy.assistant.20931626.20931632(501)>:84850] Ignoring suspend because this process is not lifecycle managed
default	11:13:28.766890-0500	runningboardd	[app<application.com.nexy.assistant.20931626.20931632(501)>:84850] Ignoring GPU update because this process is not GPU managed
default	11:13:28.766943-0500	runningboardd	[app<application.com.nexy.assistant.20931626.20931632(501)>:84850] Ignoring memory limit update because this process is not memory-managed
default	11:13:28.771320-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.20931626.20931632(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	11:13:28.772022-0500	gamepolicyd	Received state update for 84850 (app<application.com.nexy.assistant.20931626.20931632(501)>, running-active-NotVisible
default	11:13:30.886846-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(61702)
default	11:13:30.886893-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(61703)
default	11:13:30.886917-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:61702 called from <private>
default	11:13:30.886923-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:61702 called from <private>
default	11:13:30.886934-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:61703 called from <private>
default	11:13:30.886940-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:61703 called from <private>
default	11:13:30.911736-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(61703)
default	11:13:30.911788-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:61703 called from <private>
default	11:13:30.911798-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:61703 called from <private>
default	11:13:30.912549-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(61702)
default	11:13:30.914705-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:61702 called from <private>
default	11:13:30.914724-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:61702 called from <private>
default	11:13:30.925951-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:61702 called from <private>
default	11:13:30.925981-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:61702 called from <private>
default	11:13:30.926079-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(61702)
default	11:13:30.928491-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(61702)
default	11:13:30.928733-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:61702 called from <private>
default	11:13:30.928745-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:61702 called from <private>
default	11:13:30.928838-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(61702)
default	11:13:30.939482-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(61702)
default	11:13:30.939799-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:61702 called from <private>
default	11:13:30.939811-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:61702 called from <private>
default	11:13:30.940032-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:61702 called from <private>
default	11:13:30.940042-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:61702 called from <private>
default	11:13:30.940057-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:61702 called from <private>
default	11:13:30.940068-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:61702 called from <private>
default	11:13:30.940076-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:61702 called from <private>
default	11:13:30.940082-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:61702 called from <private>
default	11:13:30.940088-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:61702 called from <private>
default	11:13:30.940109-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:61702 called from <private>
default	11:13:30.940139-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:61702 called from <private>
default	11:13:30.940141-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(61702)
default	11:13:30.940171-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:61702 called from <private>
default	11:13:30.940212-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:61702 called from <private>
default	11:13:30.940274-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:61702 called from <private>
default	11:13:30.940313-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:61702 called from <private>
default	11:13:30.940360-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:61702 called from <private>
default	11:13:30.943523-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(61702)
default	11:13:30.943702-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:61702 called from <private>
default	11:13:30.943711-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:61702 called from <private>
default	11:13:30.943723-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:61702 called from <private>
default	11:13:30.943732-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:61702 called from <private>
default	11:13:41.773972-0500	Nexy	[0xaa7a1d180] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	11:13:41.775289-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=84850.4, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=84850, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	11:13:41.777576-0500	tccd	AUTHREQ_SUBJECT: msgID=84850.4, subject=com.nexy.assistant,
default	11:13:41.778506-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d116100 at /Applications/Nexy.app
default	11:13:41.797754-0500	tccd	Notifying for access  kTCCServiceScreenCapture for target PID[84850], responsiblePID[84850], responsiblePath: /Applications/Nexy.app to UID: 501
default	11:13:41.798238-0500	Nexy	[0xaa7a1d180] invalidated after the last release of the connection object
default	11:13:41.884394-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d114600 at /Applications/Nexy.app
default	11:13:41.915783-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d116100 at /Applications/Nexy.app
default	11:13:41.927495-0500	tccd	Publishing <TCCDEvent: type=Modify, service=kTCCServiceScreenCapture, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 0 subscribers: {
}
default	11:13:41.959042-0500	nehelper	Received an apps uninstalled notification with bundle IDs (
    "com.nexy.assistant"
)
default	11:13:41.961432-0500	nehelper	Received an apps uninstalled notification with bundle IDs (
    "com.nexy.assistant"
)
default	11:13:42.560512-0500	nehelper	Removing UUIDs for (
    "com.nexy.assistant"
)
default	11:13:42.566158-0500	nehelper	Handling an apps uninstalled notification with bundle IDs (
    "com.nexy.assistant"
)
default	11:13:42.589060-0500	nehelper	com.apple.preferences.networkprivacy-F67B3EA9-90A6-470B-B321-9BBD719C692B: Populating the cache with 1 UUID(s) for com.nexy.assistant
default	11:13:48.834644-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d116400 at /Applications/Nexy.app
default	11:13:48.850709-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117600 at /Applications/Nexy.app
default	11:13:48.861819-0500	tccd	Publishing <TCCDEvent: type=Modify, service=kTCCServiceScreenCapture, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 0 subscribers: {
}
default	11:13:55.331465-0500	WindowServer	0[outside of RPC]: Process death: 0x0-0x1972971 (Nexy) connectionID: 1555D3 pid: 84850 in session 0x101
default	11:13:55.331515-0500	WindowServer	<BSCompoundAssertion:0x7fb0154c0> ([FocusManager:257]-deferringPolicyEvaluationSuppression) acquire for reason:process death - 0x0-0x1972971 (Nexy) acq:0x8016ccde0 count:1
default	11:13:55.331986-0500	audiomxd	  ServerSessionManager.mm:472   { "action":"destroy_session", "session":{"ID":"0x1ef2a1","name":"Nexy(84850)"}, "details":null }
default	11:13:55.332050-0500	audiomxd	AudioApplicationInfoImpl.mm:690   Successfully removed session 0x1ef2a1 from AudioApp, recording state unchanged (app: {"name":"[implicit] Nexy","pid":84850})
default	11:13:55.332075-0500	audiomxd	  ServerSessionManager.mm:1081  destroy audio app instance since was created implicitly by session creation and all sessions now gone (audio app: {"name":"[implicit] Nexy","pid":84850})
default	11:13:55.332536-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 674, PID = 84850, Name = sid:0x1ef2a1, Nexy(84850), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	11:13:55.332684-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 674, PID = 84850, Name = sid:0x1ef2a1, Nexy(84850), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	11:13:55.335802-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	11:13:55.336971-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	11:13:55.337549-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	11:13:55.337651-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	11:13:55.332804-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	11:13:55.332986-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	11:13:55.337944-0500	WindowServer	0[outside of RPC]: [FocusManager:257] update to deferring policy requested for reason: permitted list updated - 0x0-0x1972971 removed - but we are suppressing evaluation for reasons: {(
    "process death - 0x0-0x1972971 (Nexy)"
)}
default	11:13:55.338434-0500	WindowServer	0[outside of RPC]: [FocusManager:257] update to deferring policy requested for reason: permitted list updated - 0x1-0x14b72 removed - but we are suppressing evaluation for reasons: {(
    "process death - 0x0-0x1972971 (Nexy)"
)}
default	11:13:55.344743-0500	runningboardd	XPC connection invalidated: [app<application.com.nexy.assistant.20931626.20931632(501)>:84850]
default	11:13:55.348237-0500	coreaudiod	>>> NEGOTIATE [com.nexy.assistant]
default	11:13:55.348570-0500	coreaudiod	<<< NEGOTIATE [com.nexy.assistant]
default	11:13:55.350707-0500	coreaudiod	IssueReporting.cpp:492   RTAID [ use_case=Generic report_type=RMS Generic Chain clientID=ADM node=ADM::com.nexy.assistant_61703.61532.0_airpods noise suppression studio::out-0 issue_detected_sample_time=336960.000000 ] -- [ rms:[-42.947956], peaks:[-26.778086] ]
default	11:13:55.350727-0500	coreaudiod	IssueReporting.cpp:492   RTAID [ use_case=Generic report_type=RMS Generic Chain clientID=ADM node=ADM::com.nexy.assistant_61703.61532.0_airpods noise suppression studio::in-0 issue_detected_sample_time=0.000000 ] -- [ rms:[-39.900780], peaks:[-23.753666] ]
default	11:13:55.354389-0500	kernel	Nexy[84850] triggered unnest of range 0x1f6000000->0x1f8000000 of DYLD shared region in VM map 0x34951bf8d8b82587. While not abnormal for debuggers, this increases system memory footprint until the target exits.
default	11:13:55.354408-0500	kernel	Nexy[84850] triggered unnest of range 0x1f8000000->0x1fa000000 of DYLD shared region in VM map 0x34951bf8d8b82587. While not abnormal for debuggers, this increases system memory footprint until the target exits.
default	11:13:55.415535-0500	Nexy	[0x105e80c10] activating connection: mach=true listener=false peer=false name=com.apple.cfprefsd.daemon
default	11:13:55.415613-0500	Nexy	[0x105e81150] activating connection: mach=true listener=false peer=false name=com.apple.cfprefsd.agent
error	11:13:55.548264-0500	Nexy	dlsym cannot find symbol NSMakeRect in CFBundle 0x105e87320 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	11:13:55.548496-0500	Nexy	dlsym cannot find symbol NSMakePoint in CFBundle 0x105e87320 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	11:13:55.548706-0500	Nexy	dlsym cannot find symbol NSMakeSize in CFBundle 0x105e87320 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	11:13:55.548918-0500	Nexy	dlsym cannot find symbol NSMakeRange in CFBundle 0x105e87320 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
default	11:13:55.550096-0500	Nexy	[0x105e81870] activating connection: mach=true listener=false peer=false name=com.apple.coreservices.launchservicesd
default	11:13:55.550873-0500	Nexy	[0xc9f3c4000] activating connection: mach=true listener=false peer=false name=com.apple.analyticsd
default	11:13:55.551259-0500	Nexy	[0xc9f3c4140] activating connection: mach=true listener=false peer=false name=com.apple.pasteboard.1
default	11:13:55.551690-0500	Nexy	[0xc9f3c4280] activating connection: mach=true listener=false peer=false name=com.apple.distributed_notifications@Uv3
default	11:13:55.552073-0500	Nexy	Received configuration update from daemon (initial)
default	11:13:55.553711-0500	Nexy	void _NSDisableAutomaticTerminationAndLog(NSString *) No windows open yet
default	11:13:55.554066-0500	Nexy	[0xc9f3c43c0] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	11:13:55.554743-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=84850.1, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=84850, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	11:13:55.557487-0500	tccd	AUTHREQ_SUBJECT: msgID=84850.1, subject=com.nexy.assistant,
default	11:13:55.558260-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117600 at /Applications/Nexy.app
default	11:13:55.571264-0500	Nexy	[0xc9f3c43c0] invalidated after the last release of the connection object
default	11:13:55.575098-0500	Nexy	server port 0x00003413, session port 0x00003413
default	11:13:55.576272-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=393.16910, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=84850, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=393, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	11:13:55.576297-0500	tccd	requestor: TCCDProcess: identifier=com.apple.WindowServer, pid=393, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=84850, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	11:13:55.577713-0500	tccd	AUTHREQ_SUBJECT: msgID=393.16910, subject=com.nexy.assistant,
default	11:13:55.578708-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117600 at /Applications/Nexy.app
default	11:13:55.594249-0500	Nexy	New connection 0xc79ff main
default	11:13:55.596661-0500	Nexy	CHECKIN: pid=84850
default	11:13:55.603532-0500	launchservicesd	CHECKIN:0x0-0x1972971 84850 com.nexy.assistant
default	11:13:55.603646-0500	Nexy	CHECKEDIN: pid=84850 asn=0x0-0x1972971 foreground=0
default	11:13:55.603893-0500	Nexy	[0xc9f3c43c0] activating connection: mach=false listener=true peer=false name=(anonymous)
default	11:13:55.603902-0500	Nexy	[0xc9f3c43c0] Connection returned listener port: 0x5103
default	11:13:55.604057-0500	Nexy	[0xc9efb8300] activating connection: mach=false listener=false peer=true name=com.apple.xpc.anonymous.0xc9f3c43c0.peer[363].0xc9efb8300
default	11:13:55.604361-0500	loginwindow	-[Application updateInformation] | Got App URL: file:///Applications/Nexy.app/
default	11:13:55.604487-0500	loginwindow	-[ApplicationManager checkInAppContext:eventData:] | ApplicationManager: Checked in app : Nexy
default	11:13:55.605154-0500	Nexy	FRONTLOGGING: version 1
default	11:13:55.605194-0500	Nexy	Registered, pid=84850 ASN=0x0,0x1972971
default	11:13:55.605427-0500	WindowServer	c79ff[CreateApplication]: Process creation: 0x0-0x1972971 (Nexy) connectionID: C79FF pid: 84850 in session 0x101
default	11:13:55.605740-0500	Nexy	[0xc9f3c4640] activating connection: mach=true listener=false peer=false name=com.apple.lsd.mapdb
default	11:13:55.606796-0500	Nexy	[0xc9f3c43c0] Connection returned listener port: 0x5103
default	11:13:55.607259-0500	Nexy	BringForward: pid=84850 asn=0x0-0x1972971 bringForward=0 foreground=0 uiElement=1 launchedByLS=1 modifiersCount=1 allDisabled=0
default	11:13:55.607315-0500	Nexy	BringFrontModifier: pid=84850 asn=0x0-0x1972971 Modifier 0 hideAfter=0 hideOthers=0 dontMakeFrontmost=0 mouseDown=0/0 seed=0/0
default	11:13:55.607883-0500	Nexy	Current system appearance, (HLTB: 1), (SLS: 0)
default	11:13:55.609347-0500	Nexy	No persisted cache on this platform.
default	11:13:55.610508-0500	Nexy	Current system appearance, (HLTB: 1), (SLS: 0)
default	11:13:55.611435-0500	Nexy	Post-registration system appearance: (HLTB: 1)
default	11:13:55.613195-0500	Nexy	FBSWorkspace: endpoint monitoring is disabled.
default	11:13:55.613207-0500	Nexy	FBSWorkspace: default shell endpoint is disabled.
default	11:13:55.613257-0500	Nexy	Initializing connection
default	11:13:55.613300-0500	Nexy	Removing all cached process handles
default	11:13:55.613321-0500	Nexy	Sending handshake request attempt #1 to server
default	11:13:55.613331-0500	Nexy	Creating connection to com.apple.runningboard
default	11:13:55.613337-0500	Nexy	[0xc9f3c4500] activating connection: mach=true listener=false peer=false name=com.apple.runningboard
default	11:13:55.613682-0500	Nexy	[0xc9f3c43c0] Connection returned listener port: 0x5103
default	11:13:55.613750-0500	runningboardd	Setting client for [app<application.com.nexy.assistant.20931626.20931632(501)>:84850] as ready
default	11:13:55.614406-0500	Nexy	Handshake succeeded
default	11:13:55.614422-0500	Nexy	Identity resolved as app<application.com.nexy.assistant.20931626.20931632(501)>
default	11:13:55.614537-0500	distnoted	register name: com.apple.xctest.FakeForceTouchDevice object: com.nexy.assistant token: 1e0000001d pid: 84850
default	11:13:55.617733-0500	Nexy	[0xc9f3c43c0] Connection returned listener port: 0x5103
default	11:13:55.621067-0500	Nexy	Created a new Process Instance Registry XPC connection (inactive)
default	11:13:55.621087-0500	Nexy	[0xc9f3c4780] activating connection: mach=true listener=false peer=false name=com.apple.linkd.autoShortcut
default	11:13:55.621193-0500	Nexy	Activated connection to com.apple.linkd.autoShortcut (ApplicationService)
default	11:13:55.621237-0500	Nexy	[0xc9f3c4a00] activating connection: mach=false listener=true peer=false name=(anonymous)
default	11:13:55.622767-0500	Nexy	[0xc9f3c4a00] Connection returned listener port: 0x6e03
default	11:13:55.623497-0500	Nexy	Registered process with identifier 84850-2566155
default	11:13:55.751003-0500	Nexy	Registered notify signal com.apple.caulk.alloc.rtdump (0)
default	11:13:55.753665-0500	Nexy	System_Input_Processing_Notification_Handler.mm:456   System_Input_Processing_Notification_Handler::is_vi_available(): Voice isolation DSP is available for client with bundle id com.nexy.assistant (AVFoundation is available, application is not in client deny list, application is not FaceTime variant)
default	11:13:55.755220-0500	Nexy	[0xc9f3c4b40] activating connection: mach=true listener=false peer=false name=com.apple.cmio.registerassistantservice.system-extensions
default	11:13:55.757272-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOInitializeListenersForBundleID: for <private> -> <private>
default	11:13:55.758814-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> vpio_preferenceChangedListener: new value ((null)) for key AUVoiceIOClients/com-nexy-assistant/AUVoiceIOChatFlavor, translatedBundleID com.nexy.assistant, bundleIDs {(
    "com.nexy.assistant"
)}
default	11:13:55.758960-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> vpio_preferenceChangedListener: new value ((null)) for key AUVoiceIOClients/com-nexy-assistant/AUVoiceIOIsAutoChatFlavorEnabled, translatedBundleID com.nexy.assistant, bundleIDs {(
    "com.nexy.assistant"
)}
default	11:13:55.759079-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetSupportedChatFlavorsForBundleID: <private>-><private> get supported chat flavors: <private>
default	11:13:55.759090-0500	Nexy	            HALSystem.cpp:134    Enabling HAL Voice Isolation support
default	11:13:55.759124-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetHiddenChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	11:13:55.759241-0500	Nexy	[0xc9f3c4c80] activating connection: mach=true listener=false peer=false name=com.apple.tccd
default	11:13:55.759429-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOHiddenChatFlavors newValue: (
    1
)
default	11:13:55.759780-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=84850.2, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=84850, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	11:13:55.765645-0500	tccd	AUTHREQ_SUBJECT: msgID=84850.2, subject=com.nexy.assistant,
default	11:13:55.766259-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc37138900 at /Applications/Nexy.app
default	11:13:55.777275-0500	Nexy	[0xc9f3c4c80] invalidated after the last release of the connection object
default	11:13:55.777411-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetPreferredChatFlavorForBundleID: <private>-><private> get value: 0
default	11:13:55.777455-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetSupportedChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	11:13:55.777782-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOSupportedChatFlavors newValue: (
    0,
    2
)
default	11:13:55.779068-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.11386, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=84850, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	11:13:55.779887-0500	tccd	AUTHREQ_SUBJECT: msgID=401.11386, subject=com.nexy.assistant,
default	11:13:55.780436-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc37138900 at /Applications/Nexy.app
error	11:13:55.791536-0500	tccd	Request message contains a target_token to accessing_process (TCCDProcess: identifier=com.nexy.assistant, pid=84850, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy) but TCCDProcess: identifier=com.apple.audio.coreaudiod, pid=401, auid=202, euid=202, binary_path=/usr/sbin/coreaudiod is not a TCC manager for service: kTCCServiceScreenCapture.
default	11:13:55.792453-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.11388, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=84850, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	11:13:55.793328-0500	tccd	AUTHREQ_SUBJECT: msgID=401.11388, subject=com.nexy.assistant,
default	11:13:55.793885-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc37138900 at /Applications/Nexy.app
default	11:13:55.807483-0500	Nexy	  HALPlugInManagement.cpp:440    HALPlugInManagement::RegisterPlugIns: skipping in-process plug-ins
error	11:13:55.807513-0500	Nexy	AddInstanceForFactory: No factory registered for id <CFUUID 0xc9f2e24e0> F8BB1C28-BAE8-11D6-9C31-00039315CD46
error	11:13:55.832427-0500	Nexy	         HALC_ProxyObjectMap.cpp:174   HALC_ProxyObjectMap::_CopyObjectByObjectID: failed to create the local object
error	11:13:55.832441-0500	Nexy	            HALC_ShellDevice.cpp:2673  HALC_ShellDevice::RebuildControlList: couldn't find the control object
default	11:13:55.835956-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	11:13:55.836097-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	11:13:55.840806-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetPreferredChatFlavorForBundleID: <private>-><private> get value: 0
default	11:13:57.327835-0500	kernel	SK[6]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid E0D863E8-0B55-4365-892D-7A83A39423DE flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.63102,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0x5ae28091 tp_proto=0x06"
default	11:13:57.327944-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:63102<-><IPv4-redacted>:53] interface: en0 (skipped: 6843)
so_gencnt: 5933695 t_state: SYN_SENT process: Nexy:84850 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 14 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x83217cc3
default	11:13:57.345442-0500	kernel	tcp connected: [<IPv4-redacted>:63102<-><IPv4-redacted>:53] interface: en0 (skipped: 6843)
so_gencnt: 5933695 t_state: ESTABLISHED process: Nexy:84850 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 14 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x83217cc3
default	11:13:57.345738-0500	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:63102<-><IPv4-redacted>:53] interface: en0 (skipped: 6843)
so_gencnt: 5933695 t_state: FIN_WAIT_1 process: Nexy:84850 Duration: 0.018 sec Conn_Time: 0.018 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 18.000 ms rttvar: 9.000 ms base rtt: 14 ms so_error: 0 svc/tc: 0 flow: 0x83217cc3
default	11:13:57.345748-0500	kernel	tcp_connection_summary [<IPv4-redacted>:63102<-><IPv4-redacted>:53] interface: en0 (skipped: 6843)
so_gencnt: 5933695 t_state: FIN_WAIT_1 process: Nexy:84850 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	11:13:57.363082-0500	Nexy	[0xc9f3c4c80] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioComponentRegistrar
default	11:13:57.374511-0500	Nexy	                AUHAL.cpp:420   AUHAL: (0xc9d4f1540) Selecting device 85 from constructor
default	11:13:57.374525-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0xc9d4f1540)
default	11:13:57.374531-0500	Nexy	                AUHAL.cpp:676   SelectDevice: (0xc9d4f1540) not already running
default	11:13:57.374535-0500	Nexy	                AUHAL.cpp:752   SelectDevice: (0xc9d4f1540) nothing to teardown
default	11:13:57.374537-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0xc9d4f1540) connecting device 85
default	11:13:57.374654-0500	Nexy	                AUHAL.cpp:3413  IsDeviceUsable: (0xc9d4f1540) Device ID: 85 (Input:No | Output:Yes): true
default	11:13:57.374758-0500	Nexy	                AUHAL.cpp:769   SelectDevice: (0xc9d4f1540) created ioproc 0xa for device 85
default	11:13:57.374857-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0xc9d4f1540) adding 7 device listeners to device 85
default	11:13:57.375011-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0xc9d4f1540) adding 0 device delegate listeners to device 85
default	11:13:57.375020-0500	Nexy	                AUHAL.cpp:1581  UpdateStreamFormats: -> (0xc9d4f1540)
default	11:13:57.375091-0500	Nexy	                AUHAL.cpp:1677  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  48000 Hz, Float32, interleaved
default	11:13:57.375099-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 1 output streams; not all mono
default	11:13:57.375104-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	11:13:57.375111-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 0 input streams; not all mono
default	11:13:57.375118-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	11:13:57.375206-0500	Nexy	                AUHAL.cpp:1771  UpdateStreamFormats: AUHAL(0xc9d4f1540) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	11:13:57.375215-0500	Nexy	                AUHAL.cpp:1777  UpdateStreamFormats: AUHAL(0xc9d4f1540) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	11:13:57.375220-0500	Nexy	                AUHAL.cpp:1787  UpdateStreamFormats: <-
default	11:13:57.375224-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0xc9d4f1540) removing 0 device listeners from device 0
default	11:13:57.375226-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0xc9d4f1540) removing 0 device delegate listeners from device 0
default	11:13:57.375240-0500	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0xc9d4f1540)
default	11:13:57.375253-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Output stream enables: Stream 0 is DISABLED
default	11:13:57.375345-0500	Nexy	                AUHAL.cpp:2298  SetProperty: (0xc9d4f1540) caller requesting device change from 85 to 91
default	11:13:57.375353-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0xc9d4f1540)
default	11:13:57.375356-0500	Nexy	                AUHAL.cpp:676   SelectDevice: (0xc9d4f1540) not already running
default	11:13:57.375360-0500	Nexy	                AUHAL.cpp:682   SelectDevice: (0xc9d4f1540) disconnecting device 85
default	11:13:57.375365-0500	Nexy	                AUHAL.cpp:746   SelectDevice: (0xc9d4f1540) destroying ioproc 0xa for device 85
default	11:13:57.375422-0500	Nexy	  AVAudioSession_MacOS.mm:1021  initForMacOS
default	11:13:57.375909-0500	Nexy	[0xc9f3c4f00] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioSession
default	11:13:57.376777-0500	audiomxd	  ServerSessionManager.mm:315   { "action":"create_session", "session":{"ID":"0x1ef2a2","name":"Nexy(84850)"}, "details":{"PID":84850,"session_type":"Primary"} }
default	11:13:57.376866-0500	audiomxd	AudioApplicationInfoImpl.mm:250   Setting initial isRecording state: 0 for newly-created AudioApp
	app: {"name":"[implicit] Nexy","pid":84850}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1ef2a2, sessionType: 'prim', isRecording: false }, 
]
default	11:13:57.377207-0500	Nexy	    SessionCore_Create.mm:99    Created session 0xc9ee45280 with ID: 0x1ef2a2
default	11:13:57.377785-0500	Nexy	[0xc9f3c5040] activating connection: mach=true listener=false peer=false name=com.apple.audioanalyticsd
error	11:13:57.378192-0500	Nexy	Reporter disconnected. { function=sendMessage, reporterID=364427975065601 }
default	11:13:57.378206-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped Unknown {1C-77-54-18-C8-A3:output, 0xa}
default	11:13:57.378256-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	11:13:57.378354-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0xc9d4f1540) connecting device 91
default	11:13:57.378434-0500	Nexy	                AUHAL.cpp:3413  IsDeviceUsable: (0xc9d4f1540) Device ID: 91 (Input:Yes | Output:No): true
default	11:13:57.379831-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.11389, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=84850, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	11:13:57.381077-0500	tccd	AUTHREQ_SUBJECT: msgID=401.11389, subject=com.nexy.assistant,
default	11:13:57.381695-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc37138900 at /Applications/Nexy.app
default	11:13:57.393827-0500	Nexy	                AUHAL.cpp:769   SelectDevice: (0xc9d4f1540) created ioproc 0xa for device 91
default	11:13:57.393956-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0xc9d4f1540) adding 7 device listeners to device 91
default	11:13:57.394129-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0xc9d4f1540) adding 0 device delegate listeners to device 91
default	11:13:57.394138-0500	Nexy	                AUHAL.cpp:1581  UpdateStreamFormats: -> (0xc9d4f1540)
default	11:13:57.394145-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 0 output streams; not all mono
default	11:13:57.394155-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Output render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	11:13:57.394275-0500	Nexy	                AUHAL.cpp:1677  UpdateStreamFormats: 
  input stream 0 [0x5c]:  1 ch,  24000 Hz, Float32
default	11:13:57.394282-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 1 input streams; all mono
default	11:13:57.394287-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Input render format:  1 ch,  24000 Hz, Float32
default	11:13:57.394371-0500	Nexy	                AUHAL.cpp:1771  UpdateStreamFormats: AUHAL(0xc9d4f1540) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	11:13:57.394378-0500	Nexy	                AUHAL.cpp:1777  UpdateStreamFormats: AUHAL(0xc9d4f1540) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	11:13:57.394385-0500	Nexy	                AUHAL.cpp:1787  UpdateStreamFormats: <-
default	11:13:57.394388-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0xc9d4f1540) removing 7 device listeners from device 85
default	11:13:57.394542-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0xc9d4f1540) removing 0 device delegate listeners from device 85
default	11:13:57.394551-0500	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0xc9d4f1540)
default	11:13:57.395181-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	11:13:57.396209-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.11390, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=84850, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	11:13:57.397113-0500	tccd	AUTHREQ_SUBJECT: msgID=401.11390, subject=com.nexy.assistant,
default	11:13:57.397691-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc37138900 at /Applications/Nexy.app
default	11:13:57.408648-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	11:13:57.409591-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.11391, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=84850, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	11:13:57.410384-0500	tccd	AUTHREQ_SUBJECT: msgID=401.11391, subject=com.nexy.assistant,
default	11:13:57.410921-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc37138900 at /Applications/Nexy.app
default	11:13:57.422136-0500	Nexy	Registered notify signal com.apple.caulk.alloc.audiodump (0)
default	11:13:57.423496-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.11392, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=84850, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	11:13:57.424240-0500	tccd	AUTHREQ_SUBJECT: msgID=401.11392, subject=com.nexy.assistant,
default	11:13:57.424757-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc37138900 at /Applications/Nexy.app
default	11:13:57.436024-0500	coreaudiod	>>> NEGOTIATE [com.nexy.assistant]
default	11:13:57.436175-0500	coreaudiod	<<< NEGOTIATE [com.nexy.assistant]
default	11:13:57.436943-0500	coreaudiod	>>> ADAPT [com.nexy.assistant]
default	11:13:57.437259-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xbf7741e00] Created node ADM::com.nexy.assistant_61715.61532.0_airpods noise suppression studio::in-0 with nodeID 0 - reporting period = 10.000000, sample rate = 24000.000000
default	11:13:57.437325-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xbf7741e00] Created node ADM::com.nexy.assistant_61715.61532.0_airpods noise suppression studio::out-0 with nodeID 1 - reporting period = 10.000000, sample rate = 24000.000000
default	11:13:57.509291-0500	coreaudiod	<<< ADAPT [com.nexy.assistant]
default	11:13:57.511284-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:61715 called from <private>
default	11:13:57.511341-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	11:13:57.511382-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Input {1C-77-54-18-C8-A3:input, 0xa}
default	11:13:57.513108-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:61715 called from <private>
default	11:13:57.513247-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(61715)
default	11:13:57.513267-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:61715 called from <private>
default	11:13:57.513851-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(61714)
default	11:13:57.516762-0500	runningboardd	ignoring [app<application.com.nexy.assistant.20931626.20931632(501)>:84850] as candidate for concrete target as it is terminating
default	11:13:57.514668-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:61715 called from <private>
default	11:13:57.514740-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:61714 called from <private>
default	11:13:57.514796-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:61714 called from <private>
fault	11:13:57.520771-0500	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.20931626.20931632 AUID=501> and <type=Application identifier=application.com.nexy.assistant.20931626.20931632>
default	11:13:57.521222-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	11:13:57.521967-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
fault	11:13:57.522243-0500	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.20931626.20931632 AUID=501> and <type=Application identifier=application.com.nexy.assistant.20931626.20931632>
default	11:13:57.523914-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(61715)
default	11:13:57.523936-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(61715)
default	11:13:57.523952-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:61715 called from <private>
default	11:13:57.523979-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:61715 called from <private>
default	11:13:57.523989-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:61715 called from <private>
default	11:13:57.523989-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(61715)
default	11:13:57.523996-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:61715 called from <private>
default	11:13:57.524002-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:61715 called from <private>
default	11:13:57.524002-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(61715)
default	11:13:57.524032-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:61715 called from <private>
default	11:13:57.524677-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:61715 called from <private>
default	11:13:57.524732-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:61715 called from <private>
default	11:13:57.528362-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:61715 called from <private>
default	11:13:57.528373-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:61715 called from <private>
default	11:13:57.528702-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ef2a2","name":"Nexy(84850)"}, "details":{"deviceUIDs":["1C-77-54-18-C8-A3:input"],"implicit_category":"Record","input_running":true,"output_running":false} }
default	11:13:57.528803-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 675, PID = 84850, Name = sid:0x1ef2a2, Nexy(84850), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	11:13:57.528862-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 675, PID = 84850, Name = sid:0x1ef2a2, Nexy(84850), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	11:13:57.529078-0500	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1ef2a2, Nexy(84850), 'prim'', AudioCategory changed to 'Record_WithBluetooth'
default	11:13:57.529783-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 675, PID = 84850, Name = sid:0x1ef2a2, Nexy(84850), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	11:13:57.529874-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 675, PID = 84850, Name = sid:0x1ef2a2, Nexy(84850), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	11:13:57.529800-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	11:13:57.530220-0500	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 675, PID = 84850, Name = sid:0x1ef2a2, Nexy(84850), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> is going active
default	11:13:57.530292-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1ef2a2, Nexy(84850), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 675 starting recording
default	11:13:57.531008-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 675, PID = 84850, Name = sid:0x1ef2a2, Nexy(84850), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	11:13:57.530359-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	11:13:57.531393-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 675, PID = 84850, Name = sid:0x1ef2a2, Nexy(84850), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	11:13:57.531663-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1ef2a2, Nexy(84850), 'prim'', displayID:'com.nexy.assistant'}
default	11:13:57.530317-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	11:13:57.531445-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	11:13:57.531861-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [1, 0]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:input"
)}
default	11:13:57.531869-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	11:13:57.532526-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	11:13:57.540966-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:61714 called from <private>
default	11:13:57.540977-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:61714 called from <private>
default	11:13:57.542982-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(61714)
default	11:13:57.542996-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:61714 called from <private>
default	11:13:57.543003-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:61714 called from <private>
default	11:13:57.545589-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(61715)
default	11:13:57.545608-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:61715 called from <private>
default	11:13:57.547542-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(61714)
default	11:13:57.547616-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(61714)
default	11:13:57.547997-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:61714 called from <private>
default	11:13:57.548007-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:61714 called from <private>
default	11:13:57.549340-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.11393, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=84850, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	11:13:57.551846-0500	tccd	AUTHREQ_SUBJECT: msgID=401.11393, subject=com.nexy.assistant,
default	11:13:57.552973-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc37138900 at /Applications/Nexy.app
default	11:13:57.558212-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	11:13:57.558559-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	11:13:57.558758-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:61714 called from <private>
default	11:13:57.558728-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	11:13:57.558796-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:61714 called from <private>
default	11:13:57.560120-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 3 3, id:61714 called from <private>
default	11:13:57.560134-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 4 4, id:61714 called from <private>
default	11:13:57.560210-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(61714)
default	11:13:57.560383-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:13:57.560676-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:13:57.560831-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	11:13:57.560885-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:13:57.560909-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	11:13:57.561016-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	11:13:57.561371-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	11:13:57.565537-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(61714)
default	11:13:57.565795-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 4 4 id:61714 called from <private>
default	11:13:57.565804-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 3 3 id:61714 called from <private>
default	11:13:57.565922-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(61714)
default	11:13:57.567392-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:13:57.567406-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:13:57.567424-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	11:13:57.567430-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:13:57.567437-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	11:13:57.567466-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	11:13:57.567648-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	11:13:57.572957-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(61714)
default	11:13:57.573348-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:61714 called from <private>
default	11:13:57.573360-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:61714 called from <private>
default	11:13:57.573383-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:61714 called from <private>
default	11:13:57.573391-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:61714 called from <private>
default	11:13:57.573396-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:61714 called from <private>
default	11:13:57.573401-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:61714 called from <private>
default	11:13:57.573487-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:61714 called from <private>
default	11:13:57.573529-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:61714 called from <private>
default	11:13:57.573587-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:61714 called from <private>
default	11:13:57.573678-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:61714 called from <private>
default	11:13:57.573748-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:61714 called from <private>
default	11:13:57.573801-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:61714 called from <private>
default	11:13:57.573807-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:61714 called from <private>
default	11:13:57.579554-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	11:13:57.579775-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	11:13:57.580856-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	11:13:57.580867-0500	audioaccessoryd	AudioStateChanged: Added audio session app com.nexy.assistant NULL -> 200 count 1
default	11:13:57.580876-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
error	11:13:57.580948-0500	audioaccessoryd	Updating local audio category 100 -> 200 app com.nexy.assistant
default	11:13:57.598086-0500	tccd	AUTHREQ_SUBJECT: msgID=401.11394, subject=com.nexy.assistant,
default	11:13:57.599009-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc37138900 at /Applications/Nexy.app
default	11:13:57.614443-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	11:13:57.627573-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:13:57.627583-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:13:57.627590-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	11:13:57.627597-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:13:57.627602-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	11:13:57.627607-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	11:13:57.627666-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	11:13:57.683648-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	11:13:57.683713-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	11:13:57.683784-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	11:13:57.684108-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:13:57.684123-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:13:57.684144-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	11:13:57.684150-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:13:57.684158-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	11:13:57.684164-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	11:13:57.684195-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:13:57.684254-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:13:57.684299-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	11:13:57.684362-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:13:57.684377-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	11:13:57.684386-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	11:13:57.684493-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	11:13:57.684653-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:13:57.684668-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:13:57.684675-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	11:13:57.684681-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:13:57.684689-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	11:13:57.684695-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	11:13:57.684699-0500	ControlCenter	Navigating to new application [com.nexy.assistant]
default	11:13:57.712606-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:13:57.712627-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:13:57.712640-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	11:13:57.712682-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:13:57.712724-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	11:13:57.712769-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	11:13:58.718482-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xa}
default	11:13:58.718928-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ef2a2","name":"Nexy(84850)"}, "details":{"deviceUIDs":[],"implicit_category":"","input_running":false,"output_running":false} }
default	11:13:58.719163-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 675, PID = 84850, Name = sid:0x1ef2a2, Nexy(84850), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	11:13:58.719280-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 675, PID = 84850, Name = sid:0x1ef2a2, Nexy(84850), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	11:13:58.719352-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1ef2a2, Nexy(84850), 'prim'', displayID:'com.nexy.assistant'}
default	11:13:58.719461-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	11:13:58.719469-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1ef2a2, Nexy(84850), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 675 stopping recording
default	11:13:58.719544-0500	audiomxd	-MXCoreSession- -[MXCoreSession endInterruption:]: Session <ID: 675, PID = 84850, Name = sid:0x1ef2a2, Nexy(84850), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> is going inactive
default	11:13:58.719608-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 675, PID = 84850, Name = sid:0x1ef2a2, Nexy(84850), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	11:13:58.719685-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 675, PID = 84850, Name = sid:0x1ef2a2, Nexy(84850), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	11:13:58.719985-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 200 flag 0x1 < Hijack > app com.nexy.assistant CID 0xD310001 category Not set
default	11:13:58.719943-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 0]. BT device UIDS: {(
)}
default	11:13:58.719969-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	11:13:58.720480-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	11:13:58.720663-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	11:13:58.720571-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	11:13:58.720741-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	11:13:58.720777-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	11:13:58.720823-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	11:13:58.720949-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	11:13:58.720978-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	11:13:58.721005-0500	audioaccessoryd	AudioStateChanged: Removed audio session app com.nexy.assistant 201 count 0
default	11:13:58.749500-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	11:13:58.750159-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:13:58.750180-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:13:58.750202-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	11:13:58.750214-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:13:58.750225-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	11:13:58.750236-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	11:13:58.750379-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	11:13:58.820125-0500	Nexy	                AUHAL.cpp:473   ~AUHAL: (0xc9d4f1540) Selecting device 0 from destructor
default	11:13:58.820154-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0xc9d4f1540)
default	11:13:58.820168-0500	Nexy	                AUHAL.cpp:676   SelectDevice: (0xc9d4f1540) not already running
default	11:13:58.820178-0500	Nexy	                AUHAL.cpp:682   SelectDevice: (0xc9d4f1540) disconnecting device 91
default	11:13:58.820209-0500	Nexy	                AUHAL.cpp:746   SelectDevice: (0xc9d4f1540) destroying ioproc 0xa for device 91
default	11:13:58.820262-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xa}
default	11:13:58.820317-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	11:13:58.820585-0500	Nexy	                AUHAL.cpp:848   SelectDevice: (0xc9d4f1540) nothing to setup
default	11:13:58.820611-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0xc9d4f1540) adding 0 device listeners to device 0
default	11:13:58.820622-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0xc9d4f1540) adding 0 device delegate listeners to device 0
default	11:13:58.820636-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0xc9d4f1540) removing 7 device listeners from device 91
default	11:13:58.821033-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0xc9d4f1540) removing 0 device delegate listeners from device 91
default	11:13:58.821057-0500	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0xc9d4f1540)
default	11:13:58.950943-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=84928.1, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=84850, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.osascript, pid=84928, auid=501, euid=501, binary_path=/usr/bin/osascript}, },
default	11:13:58.952454-0500	tccd	AUTHREQ_SUBJECT: msgID=84928.1, subject=com.nexy.assistant,
default	11:13:58.953094-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117600 at /Applications/Nexy.app
default	11:13:58.967118-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=393.16914, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=84850, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.osascript, pid=84928, auid=501, euid=501, binary_path=/usr/bin/osascript}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=393, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	11:13:58.968076-0500	tccd	AUTHREQ_SUBJECT: msgID=393.16914, subject=com.nexy.assistant,
default	11:13:58.968686-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117600 at /Applications/Nexy.app
default	11:13:59.003036-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117600 at /Applications/Nexy.app
default	11:13:59.020905-0500	System Events	TCCAccessRequestIndirect: TCCAccessRequestIndirect with pid 84855: target_identity: {
    kTCCCodeIdentityAuditToken = {length = 32, bytes = 0xf5010000 f5010000 14000000 f5010000 ... b7860100 0d282700 };
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
default	11:13:59.033891-0500	tccd	target_executable_path_URL: file:///Applications/Nexy.app/Contents/MacOS/Nexy
default	11:13:59.957432-0500	Nexy	[0xc9f3c5400] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
error	11:13:59.958067-0500	tccd	TCCDProcess: identifier=com.nexy.assistant, pid=84850, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy attempted to call TCCAccessRequest for kTCCServiceAccessibility without the recommended com.apple.private.tcc.manager.check-by-audit-token entitlement
default	11:13:59.958255-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=84850.3, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=84850, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.nexy.assistant, pid=84850, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	11:13:59.959461-0500	tccd	AUTHREQ_SUBJECT: msgID=84850.3, subject=com.nexy.assistant,
default	11:13:59.960131-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117600 at /Applications/Nexy.app
default	11:13:59.971998-0500	Nexy	[0xc9f3c5400] invalidated after the last release of the connection object
default	11:13:59.972100-0500	Nexy	[0xc9f3c5400] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
error	11:13:59.972511-0500	tccd	TCCDProcess: identifier=com.nexy.assistant, pid=84850, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy attempted to call TCCAccessRequest for kTCCServiceAccessibility without the recommended com.apple.private.tcc.manager.check-by-audit-token entitlement
default	11:13:59.972685-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=84850.4, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=84850, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.nexy.assistant, pid=84850, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	11:13:59.973596-0500	tccd	AUTHREQ_SUBJECT: msgID=84850.4, subject=com.nexy.assistant,
default	11:13:59.974195-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117600 at /Applications/Nexy.app
default	11:13:59.985409-0500	Nexy	[0xc9f3c5400] invalidated after the last release of the connection object
default	11:13:59.985471-0500	Nexy	[0xc9f3c5400] activating connection: mach=true listener=false peer=false name=com.apple.universalaccessAuthWarn
default	11:13:59.985557-0500	Nexy	[0xc9f3c5400] invalidated after the last release of the connection object
default	11:13:59.986275-0500	Nexy	server port 0x00014a03, session port 0x00003413
default	11:14:00.014434-0500	kernel	SK[9]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 3F06420B-A0AB-49D5-B0E7-80ABE563B965 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.63103,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0x00631437 tp_proto=0x06"
default	11:14:00.014558-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:63103<-><IPv4-redacted>:53] interface: en0 (skipped: 6843)
so_gencnt: 5933697 t_state: SYN_SENT process: Nexy:84850 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 13 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x9ff6ce4f
default	11:14:00.016022-0500	Nexy	networkd_settings_read_from_file initialized networkd settings by reading plist directly
default	11:14:00.016225-0500	Nexy	networkd_settings_read_from_file initialized networkd settings by reading plist directly
default	11:14:00.017066-0500	Nexy	nw_path_libinfo_path_check [5909D792-43F4-4BE3-8F0E-F92F0191607E IPv4#11017815:443 tcp, legacy-socket, attribution: developer]
	libinfo check path: <private>
default	11:14:00.018089-0500	kernel	SK[7]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid BF3ED4BD-B064-4B4B-8F5B-F1D38575FBBC flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.63104,dst=<IPv4-redacted>.443,proto=0x06 mask=0x0000003f,hash=0x1d24718c tp_proto=0x06"
default	11:14:00.018142-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:63104<-><IPv4-redacted>:443] interface: en0 (skipped: 6843)
so_gencnt: 5933698 t_state: SYN_SENT process: Nexy:84850 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xb90d22f9
default	11:14:00.029560-0500	kernel	tcp connected: [<IPv4-redacted>:63103<-><IPv4-redacted>:53] interface: en0 (skipped: 6843)
so_gencnt: 5933697 t_state: ESTABLISHED process: Nexy:84850 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 13 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x9ff6ce4f
default	11:14:00.030143-0500	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:63103<-><IPv4-redacted>:53] interface: en0 (skipped: 6843)
so_gencnt: 5933697 t_state: FIN_WAIT_1 process: Nexy:84850 Duration: 0.015 sec Conn_Time: 0.015 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 15.000 ms rttvar: 7.500 ms base rtt: 13 ms so_error: 0 svc/tc: 0 flow: 0x9ff6ce4f
default	11:14:00.030153-0500	kernel	tcp_connection_summary [<IPv4-redacted>:63103<-><IPv4-redacted>:53] interface: en0 (skipped: 6843)
so_gencnt: 5933697 t_state: FIN_WAIT_1 process: Nexy:84850 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	11:14:00.030579-0500	kernel	SK[7]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 04EFDB90-755E-4ADE-91CD-CFB563EF4855 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.63105,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0x5d14cd78 tp_proto=0x06"
default	11:14:00.030599-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:63105<-><IPv4-redacted>:53] interface: en0 (skipped: 6843)
so_gencnt: 5933699 t_state: SYN_SENT process: Nexy:84850 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 13 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x9236f7d9
default	11:14:00.039655-0500	kernel	tcp connected: [<IPv4-redacted>:63104<-><IPv4-redacted>:443] interface: en0 (skipped: 6843)
so_gencnt: 5933698 t_state: ESTABLISHED process: Nexy:84850 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xb90d22f9
default	11:14:00.072200-0500	kernel	tcp connected: [<IPv4-redacted>:63105<-><IPv4-redacted>:53] interface: en0 (skipped: 6843)
so_gencnt: 5933699 t_state: ESTABLISHED process: Nexy:84850 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 13 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x9236f7d9
default	11:14:00.072427-0500	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:63105<-><IPv4-redacted>:53] interface: en0 (skipped: 6843)
so_gencnt: 5933699 t_state: FIN_WAIT_1 process: Nexy:84850 Duration: 0.042 sec Conn_Time: 0.041 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 41.000 ms rttvar: 20.500 ms base rtt: 13 ms so_error: 0 svc/tc: 0 flow: 0x9236f7d9
default	11:14:00.072438-0500	kernel	tcp_connection_summary [<IPv4-redacted>:63105<-><IPv4-redacted>:53] interface: en0 (skipped: 6843)
so_gencnt: 5933699 t_state: FIN_WAIT_1 process: Nexy:84850 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	11:14:00.120450-0500	Nexy	[0xc9f3c5680] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	11:14:00.121222-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=84850.5, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=84850, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	11:14:00.122637-0500	Nexy	[0xc9f3c57c0] activating connection: mach=true listener=false peer=false name=com.apple.usernoted.client
default	11:14:00.128124-0500	tccd	AUTHREQ_SUBJECT: msgID=84850.5, subject=com.nexy.assistant,
default	11:14:00.128716-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117600 at /Applications/Nexy.app
default	11:14:00.131236-0500	usernoted	Connection com.nexy.assistant with path: /Applications/Nexy.app
default	11:14:00.135049-0500	distnoted	register name: com.apple.nsquiet_safe_quit_give_reason object: com.nexy.assistant token: 3100000032 pid: 84850
default	11:14:00.139897-0500	Nexy	[0xc9f3c5680] invalidated after the last release of the connection object
default	11:14:00.145471-0500	Nexy	NSApp cache appearance:
-NSRequiresAquaSystemAppearance: 0
-appearance: (null)
-effectiveAppearance: <NSCompositeAppearance: 0xc9f2e8640
 (
    "<NSAquaAppearance: 0xc9f2e8820>",
    "<NSSystemAppearance: 0xc9f2e8780>"
)>
default	11:14:00.151576-0500	Nexy	[0xc9f3c5cc0] activating connection: mach=true listener=false peer=false name=com.apple.dock.fullscreen
default	11:14:00.151833-0500	Nexy	[0xc9f3c5e00] activating connection: mach=true listener=false peer=false name=com.apple.fonts
default	11:14:00.154298-0500	Nexy	(<private>) deleteSearchableItemsWithDomainIdentifiers, protectionClass:(null), domainIdentifiers number:1
default	11:14:00.154527-0500	Nexy	sConnectionName: com.apple.spotlight.IndexAgent
default	11:14:00.154540-0500	Nexy	Start service name com.apple.spotlight.IndexAgent
default	11:14:00.154562-0500	Nexy	[0xc9f3c5f40] activating connection: mach=true listener=false peer=false name=com.apple.spotlight.IndexAgent
default	11:14:00.154640-0500	Nexy	[C:1] Alloc com.apple.controlcenter.statusitems
default	11:14:00.154706-0500	Nexy	[0xc9f3c6080] activating connection: mach=false listener=false peer=false name=(anonymous)
default	11:14:00.154773-0500	Nexy	FBSWorkspace registering source: <private>
default	11:14:00.155241-0500	suggestd	SGDSpotlightReceiver: deleting 1 domain identifiers (1 after removing overlaps) for com.nexy.assistant: <private>
default	11:14:00.155896-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	11:14:00.155962-0500	Nexy	<FBSWorkspaceScenesClient:0xc9f2e9f40 <private>> attempting immediate handshake from activate
default	11:14:00.156003-0500	Nexy	<FBSWorkspaceScenesClient:0xc9f2e9f40 <private>> sent handshake
default	11:14:00.156097-0500	Nexy	Realizing settings extension __NSStatusItemSceneHostSettings__ on FBSSceneSettings
default	11:14:00.160285-0500	Nexy	<FBSWorkspaceScenesClient:0xc9f2e9f40 <private>> was invalidated
default	11:14:00.160303-0500	Nexy	FBSWorkspace unregistering source: <private>
default	11:14:00.160567-0500	Nexy	Realizing settings extension __NSStatusItemSceneClientSettings__ on FBSSceneClientSettings
default	11:14:00.161640-0500	Nexy	Realizing settings extension FBSSceneSettingsCore on FBSSceneSettings
default	11:14:00.162693-0500	Nexy	Realizing settings extension FBSSceneClientSettingsCore on FBSSceneClientSettings
default	11:14:00.163186-0500	Nexy	Requesting scene <FBSScene: 0xc9f2ea1c0; com.apple.controlcenter:AE2CE8AE-D0FC-45E4-A1A2-5EDA9E2DC1AE> from com.apple.controlcenter.statusitems
error	11:14:00.163386-0500	Nexy	Error creating <FBSScene: 0xc9f2ea1c0; com.apple.controlcenter:AE2CE8AE-D0FC-45E4-A1A2-5EDA9E2DC1AE>: <NSError: 0xc9f8be790; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
default	11:14:00.164995-0500	Nexy	Request for <FBSScene: 0xc9f2ea1c0; com.apple.controlcenter:AE2CE8AE-D0FC-45E4-A1A2-5EDA9E2DC1AE> complete!
default	11:14:00.179398-0500	Nexy	Warning: the app is using `-[NSStatusBarButton setHighlightsBy:]` to set the highlight behavior. Instead, consider removing that setting. That will enable macOS to highlight the status bar button as appropriate for all configurations (e.g., light, dark, and increased contrast modes).
default	11:14:00.194081-0500	Nexy	Registering for test daemon availability notify post.
default	11:14:00.194227-0500	Nexy	notify_get_state check indicated test daemon not ready.
default	11:14:00.194318-0500	Nexy	notify_get_state check indicated test daemon not ready.
default	11:14:00.194401-0500	Nexy	notify_get_state check indicated test daemon not ready.
default	11:14:00.195585-0500	Nexy	[0xc9f3c6440] activating connection: mach=true listener=false peer=false name=com.apple.coreservices.appleevents
default	11:14:00.195998-0500	Nexy	[0xc9f3c43c0] Connection returned listener port: 0x5103
default	11:14:00.196333-0500	Nexy	SignalReady: pid=84850 asn=0x0-0x1972971
default	11:14:00.196696-0500	Nexy	SIGNAL: pid=84850 asn=0x0x-0x1972971
default	11:14:00.197139-0500	loginwindow	-[Application updateInformation] | Got App URL: file:///Applications/Nexy.app/
default	11:14:00.198513-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117600 at /Applications/Nexy.app
error	11:14:00.198862-0500	Nexy	scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
default	11:14:00.201929-0500	Nexy	void _NSDisableAutomaticTerminationAndLog(NSString *) Restoring windows
default	11:14:00.201935-0500	Nexy	-[NSApplication _reopenWindowsAsNecessaryIncludingRestorableState:withFullFidelity:completionHandler:] shouldRestoreState=1 hasPersistentStateToRestore=0 shouldStillRestoreStateAfterPrompting=0
default	11:14:00.201948-0500	Nexy	[0xc9f3c5680] activating connection: mach=true listener=false peer=false name=com.apple.window_proxies
default	11:14:00.202008-0500	Nexy	[0xc9f3c5680] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	11:14:00.205517-0500	Nexy	void _NSEnableAutomaticTerminationAndLog(NSString *) Restoring windows
default	11:14:00.207834-0500	Nexy	[C:2] Alloc <private>
default	11:14:00.207873-0500	Nexy	[0xc9f3c5680] activating connection: mach=false listener=false peer=false name=(anonymous)
default	11:14:00.208092-0500	Nexy	NSApplication._react(to:) dock
default	11:14:00.208101-0500	Nexy	NSApplication._react(to:) reactions=83
error	11:14:00.208031-0500	kernel	Sandbox: WindowManager(584) deny(1) mach-task-name others [Nexy(84850)]
default	11:14:00.209036-0500	runningboardd	ignoring [app<application.com.nexy.assistant.20931626.20931632(501)>:84850] as candidate for concrete target as it is terminating
default	11:14:00.209073-0500	runningboardd	Acquiring assertion targeting 84850 from originator [app<application.com.nexy.assistant.20931626.20931632(501)>:84850] with description <RBSAssertionDescriptor| "AudioHAL" ID:398-84850-1504675 target:84850 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
error	11:14:00.209300-0500	Nexy	Error acquiring assertion: <Error Domain=RBSAssertionErrorDomain Code=2 "Specified target process 84850 does not exist" UserInfo={NSLocalizedFailureReason=Specified target process 84850 does not exist}>
error	11:14:00.209312-0500	Nexy	          HALRBSAssertionGlue.mm:98    Failed to acquire the AudioHAL RBSAssertion for pid: 84850 with code: 2 - RBSAssertionErrorDomain
default	11:14:00.209439-0500	WindowManager	Connection activated | (84850) Nexy
default	11:14:00.209479-0500	runningboardd	ignoring [app<application.com.nexy.assistant.20931626.20931632(501)>:84850] as candidate for concrete target as it is terminating
default	11:14:00.209508-0500	runningboardd	Acquiring assertion targeting 84850 from originator [app<application.com.nexy.assistant.20931626.20931632(501)>:84850] with description <RBSAssertionDescriptor| "AudioHAL" ID:398-84850-1504676 target:84850 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
error	11:14:00.209660-0500	Nexy	Error acquiring assertion: <Error Domain=RBSAssertionErrorDomain Code=2 "Specified target process 84850 does not exist" UserInfo={NSLocalizedFailureReason=Specified target process 84850 does not exist}>
error	11:14:00.209670-0500	Nexy	          HALRBSAssertionGlue.mm:98    Failed to acquire the AudioHAL RBSAssertion for pid: 84850 with code: 2 - RBSAssertionErrorDomain
default	11:14:00.209777-0500	runningboardd	ignoring [app<application.com.nexy.assistant.20931626.20931632(501)>:84850] as candidate for concrete target as it is terminating
default	11:14:00.209808-0500	runningboardd	Acquiring assertion targeting 84850 from originator [app<application.com.nexy.assistant.20931626.20931632(501)>:84850] with description <RBSAssertionDescriptor| "AudioHAL" ID:398-84850-1504677 target:84850 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
error	11:14:00.209907-0500	Nexy	Error acquiring assertion: <Error Domain=RBSAssertionErrorDomain Code=2 "Specified target process 84850 does not exist" UserInfo={NSLocalizedFailureReason=Specified target process 84850 does not exist}>
error	11:14:00.209916-0500	Nexy	          HALRBSAssertionGlue.mm:98    Failed to acquire the AudioHAL RBSAssertion for pid: 84850 with code: 2 - RBSAssertionErrorDomain
default	11:14:00.210020-0500	runningboardd	ignoring [app<application.com.nexy.assistant.20931626.20931632(501)>:84850] as candidate for concrete target as it is terminating
default	11:14:00.210042-0500	runningboardd	Acquiring assertion targeting 84850 from originator [app<application.com.nexy.assistant.20931626.20931632(501)>:84850] with description <RBSAssertionDescriptor| "AudioHAL" ID:398-84850-1504678 target:84850 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
error	11:14:00.210165-0500	Nexy	Error acquiring assertion: <Error Domain=RBSAssertionErrorDomain Code=2 "Specified target process 84850 does not exist" UserInfo={NSLocalizedFailureReason=Specified target process 84850 does not exist}>
error	11:14:00.210175-0500	Nexy	          HALRBSAssertionGlue.mm:98    Failed to acquire the AudioHAL RBSAssertion for pid: 84850 with code: 2 - RBSAssertionErrorDomain
default	11:14:00.302634-0500	Nexy	*warn* MailCS ======%%% _setMailMessageAttributes skip:1
default	11:14:00.306687-0500	Nexy	Start service name com.apple.spotlightknowledged
default	11:14:00.307468-0500	Nexy	[GMS] availability notification token 74
default	11:14:00.498888-0500	kernel	udp connect: [<IPv4-redacted>:57713<-><IPv4-redacted>:443] interface:  (skipped: 1081)
so_gencnt: 5933702 so_state: 0x0002 process: Nexy:84850 bytes in/out: 0/0 pkts in/out: 0/0 error: 0 so_error: 0 svc/tc: 0 flow: 0x9a6525fd
default	11:14:00.498905-0500	kernel	udp_connection_summary [<IPv4-redacted>:57713<-><IPv4-redacted>:443] interface:  (skipped: 1081)
so_gencnt: 5933702 so_state: 0x0002 process: Nexy:84850 Duration: 0.000 sec Conn_Time: 0.000 sec bytes in/out: 0/0 pkts in/out: 0/0 rxnospace pkts/bytes: 0/0 so_error: 0 svc/tc: 0 flow: 0x9a6525fd flowctl: 0us (0x)
default	11:14:00.500968-0500	kernel	SK[9]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 3A9CEC99-51FC-420F-8F53-1442AA688D9F flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.63107,dst=<IPv4-redacted>.443,proto=0x06 mask=0x0000003f,hash=0x61461ccb tp_proto=0x06"
default	11:14:00.501085-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:63107<-><IPv4-redacted>:443] interface: en0 (skipped: 6843)
so_gencnt: 5933704 t_state: SYN_SENT process: Nexy:84850 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 22 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x84dce600
default	11:14:00.527177-0500	kernel	tcp connected: [<IPv4-redacted>:63107<-><IPv4-redacted>:443] interface: en0 (skipped: 6843)
so_gencnt: 5933704 t_state: ESTABLISHED process: Nexy:84850 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 22 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x84dce600
default	11:14:00.552089-0500	Nexy	[0xc9f3c5400] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	11:14:00.552795-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=84850.6, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=84850, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	11:14:00.553939-0500	tccd	AUTHREQ_SUBJECT: msgID=84850.6, subject=com.nexy.assistant,
default	11:14:00.554594-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117600 at /Applications/Nexy.app
default	11:14:00.566653-0500	Nexy	[0xc9f3c5400] invalidated after the last release of the connection object
default	11:14:00.567823-0500	Nexy	 [INFO] SLSHWCaptureDesktopProxying:485 request: <private>
default	11:14:00.570532-0500	Nexy	[0xc9f3c5400] activating connection: mach=true listener=false peer=false name=com.apple.replayd
default	11:14:00.570663-0500	Nexy	 [INFO] -[RPDaemonProxy consumeSandboxExtension:processNewConnection:]:568
default	11:14:00.570753-0500	Nexy	 [INFO] -[RPDaemonProxy proxyCoreGraphicsWithMethodType:config:machPort:completionHandler:]:1486
default	11:14:00.575535-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=87854.28, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=84850, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.replayd, pid=87854, auid=501, euid=501, binary_path=/usr/libexec/replayd}, },
default	11:14:00.575563-0500	tccd	requestor: TCCDProcess: identifier=com.apple.replayd, pid=87854, auid=501, euid=501, binary_path=/usr/libexec/replayd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=84850, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	11:14:00.576466-0500	tccd	AUTHREQ_SUBJECT: msgID=87854.28, subject=com.nexy.assistant,
default	11:14:00.577049-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117600 at /Applications/Nexy.app
default	11:14:00.578361-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=84933.1, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=84850, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.osascript, pid=84933, auid=501, euid=501, binary_path=/usr/bin/osascript}, },
default	11:14:00.579541-0500	tccd	AUTHREQ_SUBJECT: msgID=84933.1, subject=com.nexy.assistant,
default	11:14:00.580075-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d114900 at /Applications/Nexy.app
default	11:14:00.593116-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=393.16915, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=84850, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.osascript, pid=84933, auid=501, euid=501, binary_path=/usr/bin/osascript}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=393, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	11:14:00.593935-0500	tccd	AUTHREQ_SUBJECT: msgID=393.16915, subject=com.nexy.assistant,
default	11:14:00.594470-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d114900 at /Applications/Nexy.app
default	11:14:00.607100-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=393.16916, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=84850, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=393, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	11:14:00.607126-0500	tccd	requestor: TCCDProcess: identifier=com.apple.WindowServer, pid=393, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=84850, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	11:14:00.608001-0500	tccd	AUTHREQ_SUBJECT: msgID=393.16916, subject=com.nexy.assistant,
default	11:14:00.608578-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d114900 at /Applications/Nexy.app
default	11:14:00.636863-0500	Nexy	 [INFO] SLSHWCaptureDesktopProxying_block_invoke:506 request: <private>, error: (null), windowInfo: (null)
default	11:14:00.652405-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d114900 at /Applications/Nexy.app
default	11:14:00.668154-0500	System Events	TCCAccessRequestIndirect: TCCAccessRequestIndirect with pid 84855: target_identity: {
    kTCCCodeIdentityAuditToken = {length = 32, bytes = 0xf5010000 f5010000 14000000 f5010000 ... b7860100 17282700 };
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
default	11:14:00.678760-0500	tccd	target_executable_path_URL: file:///Applications/Nexy.app/Contents/MacOS/Nexy
default	11:14:00.949729-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(61714)
default	11:14:00.949800-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(61715)
default	11:14:00.949822-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:61714 called from <private>
default	11:14:00.949834-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:61714 called from <private>
default	11:14:00.949846-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:61715 called from <private>
default	11:14:00.949852-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:61715 called from <private>
default	11:14:00.969765-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(61714)
default	11:14:00.976804-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(61715)
default	11:14:00.976860-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:61715 called from <private>
default	11:14:00.976867-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:61715 called from <private>
default	11:14:00.977236-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:61714 called from <private>
default	11:14:00.977250-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:61714 called from <private>
default	11:14:00.991817-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:61714 called from <private>
default	11:14:00.991833-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:61714 called from <private>
default	11:14:00.991909-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(61714)
default	11:14:01.001708-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(61714)
default	11:14:01.002002-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:61714 called from <private>
default	11:14:01.002011-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:61714 called from <private>
default	11:14:01.002110-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(61714)
default	11:14:01.011598-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(61714)
default	11:14:01.011867-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:61714 called from <private>
default	11:14:01.011878-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:61714 called from <private>
default	11:14:01.012072-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:61714 called from <private>
default	11:14:01.012080-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:61714 called from <private>
default	11:14:01.012100-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:61714 called from <private>
default	11:14:01.012109-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:61714 called from <private>
default	11:14:01.012118-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:61714 called from <private>
default	11:14:01.012125-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:61714 called from <private>
default	11:14:01.012147-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:61714 called from <private>
default	11:14:01.012178-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(61714)
default	11:14:01.012248-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:61714 called from <private>
default	11:14:01.012403-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:61714 called from <private>
default	11:14:01.012501-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:61714 called from <private>
default	11:14:01.012581-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:61714 called from <private>
default	11:14:01.012651-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:61714 called from <private>
default	11:14:01.012712-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:61714 called from <private>
default	11:14:01.012784-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:61714 called from <private>
default	11:14:01.015583-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(61714)
default	11:14:01.015923-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:61714 called from <private>
default	11:14:01.015943-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:61714 called from <private>
default	11:14:01.015958-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:61714 called from <private>
default	11:14:01.015968-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:61714 called from <private>
default	11:14:01.181451-0500	Nexy	                AUHAL.cpp:420   AUHAL: (0xc9d5bd540) Selecting device 85 from constructor
default	11:14:01.181476-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0xc9d5bd540)
default	11:14:01.181484-0500	Nexy	                AUHAL.cpp:676   SelectDevice: (0xc9d5bd540) not already running
default	11:14:01.181490-0500	Nexy	                AUHAL.cpp:752   SelectDevice: (0xc9d5bd540) nothing to teardown
default	11:14:01.181495-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0xc9d5bd540) connecting device 85
default	11:14:01.181617-0500	Nexy	                AUHAL.cpp:3413  IsDeviceUsable: (0xc9d5bd540) Device ID: 85 (Input:No | Output:Yes): true
default	11:14:01.181759-0500	Nexy	                AUHAL.cpp:769   SelectDevice: (0xc9d5bd540) created ioproc 0xb for device 85
default	11:14:01.181895-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0xc9d5bd540) adding 7 device listeners to device 85
default	11:14:01.182100-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0xc9d5bd540) adding 0 device delegate listeners to device 85
default	11:14:01.182111-0500	Nexy	                AUHAL.cpp:1581  UpdateStreamFormats: -> (0xc9d5bd540)
default	11:14:01.182190-0500	Nexy	                AUHAL.cpp:1677  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  48000 Hz, Float32, interleaved
default	11:14:01.182202-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 1 output streams; not all mono
default	11:14:01.182209-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	11:14:01.182216-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 0 input streams; not all mono
default	11:14:01.182225-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	11:14:01.182322-0500	Nexy	                AUHAL.cpp:1771  UpdateStreamFormats: AUHAL(0xc9d5bd540) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	11:14:01.182331-0500	Nexy	                AUHAL.cpp:1777  UpdateStreamFormats: AUHAL(0xc9d5bd540) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	11:14:01.182337-0500	Nexy	                AUHAL.cpp:1787  UpdateStreamFormats: <-
default	11:14:01.182342-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0xc9d5bd540) removing 0 device listeners from device 0
default	11:14:01.182348-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0xc9d5bd540) removing 0 device delegate listeners from device 0
default	11:14:01.182352-0500	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0xc9d5bd540)
default	11:14:01.182368-0500	Nexy	                AUHAL.cpp:2298  SetProperty: (0xc9d5bd540) caller requesting device change from 85 to 85
default	11:14:01.182373-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0xc9d5bd540)
default	11:14:01.182377-0500	Nexy	                AUHAL.cpp:659   SelectDevice: <- (0xc9d5bd540) exiting with nothing to do
default	11:14:01.182821-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	11:14:01.183157-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	11:14:01.184223-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	11:14:01.185866-0500	Nexy	                AUHAL.cpp:473   ~AUHAL: (0xc9d5bd540) Selecting device 0 from destructor
default	11:14:01.185874-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0xc9d5bd540)
default	11:14:01.185880-0500	Nexy	                AUHAL.cpp:676   SelectDevice: (0xc9d5bd540) not already running
default	11:14:01.185884-0500	Nexy	                AUHAL.cpp:682   SelectDevice: (0xc9d5bd540) disconnecting device 85
default	11:14:01.185890-0500	Nexy	                AUHAL.cpp:746   SelectDevice: (0xc9d5bd540) destroying ioproc 0xb for device 85
default	11:14:01.185934-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Output {1C-77-54-18-C8-A3:output, 0xb}
default	11:14:01.185992-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	11:14:01.186110-0500	Nexy	                AUHAL.cpp:848   SelectDevice: (0xc9d5bd540) nothing to setup
default	11:14:01.186122-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0xc9d5bd540) adding 0 device listeners to device 0
default	11:14:01.186127-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0xc9d5bd540) adding 0 device delegate listeners to device 0
default	11:14:01.186135-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0xc9d5bd540) removing 7 device listeners from device 85
default	11:14:01.186322-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0xc9d5bd540) removing 0 device delegate listeners from device 85
default	11:14:01.186336-0500	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0xc9d5bd540)
default	11:14:01.187401-0500	Nexy	                AUHAL.cpp:420   AUHAL: (0xc9d5bd540) Selecting device 85 from constructor
default	11:14:01.187411-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0xc9d5bd540)
default	11:14:01.187417-0500	Nexy	                AUHAL.cpp:676   SelectDevice: (0xc9d5bd540) not already running
default	11:14:01.187422-0500	Nexy	                AUHAL.cpp:752   SelectDevice: (0xc9d5bd540) nothing to teardown
default	11:14:01.187427-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0xc9d5bd540) connecting device 85
default	11:14:01.187515-0500	Nexy	                AUHAL.cpp:3413  IsDeviceUsable: (0xc9d5bd540) Device ID: 85 (Input:No | Output:Yes): true
default	11:14:01.187614-0500	Nexy	                AUHAL.cpp:769   SelectDevice: (0xc9d5bd540) created ioproc 0xc for device 85
default	11:14:01.187714-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0xc9d5bd540) adding 7 device listeners to device 85
default	11:14:01.187886-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0xc9d5bd540) adding 0 device delegate listeners to device 85
default	11:14:01.187896-0500	Nexy	                AUHAL.cpp:1581  UpdateStreamFormats: -> (0xc9d5bd540)
default	11:14:01.187974-0500	Nexy	                AUHAL.cpp:1677  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  48000 Hz, Float32, interleaved
default	11:14:01.187985-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 1 output streams; not all mono
default	11:14:01.187993-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	11:14:01.188000-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 0 input streams; not all mono
default	11:14:01.188009-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	11:14:01.188110-0500	Nexy	                AUHAL.cpp:1771  UpdateStreamFormats: AUHAL(0xc9d5bd540) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	11:14:01.188119-0500	Nexy	                AUHAL.cpp:1777  UpdateStreamFormats: AUHAL(0xc9d5bd540) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	11:14:01.188127-0500	Nexy	                AUHAL.cpp:1787  UpdateStreamFormats: <-
default	11:14:01.188132-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0xc9d5bd540) removing 0 device listeners from device 0
default	11:14:01.188137-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0xc9d5bd540) removing 0 device delegate listeners from device 0
default	11:14:01.188141-0500	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0xc9d5bd540)
default	11:14:01.188153-0500	Nexy	                AUHAL.cpp:2298  SetProperty: (0xc9d5bd540) caller requesting device change from 85 to 85
default	11:14:01.188158-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0xc9d5bd540)
default	11:14:01.188163-0500	Nexy	                AUHAL.cpp:659   SelectDevice: <- (0xc9d5bd540) exiting with nothing to do
default	11:14:01.188169-0500	Nexy	AudioHardware-mac-imp.cpp:1299   AudioObjectAddPropertyListener: listener was already added
default	11:14:01.188718-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	11:14:01.189013-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	11:14:01.191895-0500	runningboardd	ignoring [app<application.com.nexy.assistant.20931626.20931632(501)>:84850] as candidate for concrete target as it is terminating
default	11:14:01.191961-0500	runningboardd	Acquiring assertion targeting 84850 from originator [app<application.com.nexy.assistant.20931626.20931632(501)>:84850] with description <RBSAssertionDescriptor| "AudioHAL" ID:398-84850-1504681 target:84850 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	11:14:01.192316-0500	runningboardd	ignoring [app<application.com.nexy.assistant.20931626.20931632(501)>:84850] as candidate for concrete target as it is terminating
error	11:14:01.192389-0500	Nexy	Error acquiring assertion: <Error Domain=RBSAssertionErrorDomain Code=2 "Specified target process 84850 does not exist" UserInfo={NSLocalizedFailureReason=Specified target process 84850 does not exist}>
error	11:14:01.192415-0500	Nexy	          HALRBSAssertionGlue.mm:98    Failed to acquire the AudioHAL RBSAssertion for pid: 84850 with code: 2 - RBSAssertionErrorDomain
default	11:14:01.200344-0500	Nexy	FBSWorkspace registering source: <private>
default	11:14:01.200387-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	11:14:01.200490-0500	Nexy	<FBSWorkspaceScenesClient:0xca07a0a00 <private>> attempting immediate handshake from activate
default	11:14:01.200526-0500	Nexy	<FBSWorkspaceScenesClient:0xca07a0a00 <private>> sent handshake
default	11:14:01.200916-0500	Nexy	Requesting scene <FBSScene: 0xca07a0aa0; com.apple.controlcenter:D8913A5A-24CE-410F-87DF-549017D1A8AF> from com.apple.controlcenter.statusitems
default	11:14:01.201359-0500	Nexy	<FBSWorkspaceScenesClient:0xca07a0a00 <private>> was invalidated
default	11:14:01.201410-0500	Nexy	Request for <FBSScene: 0xca07a0aa0; com.apple.controlcenter:D8913A5A-24CE-410F-87DF-549017D1A8AF> complete!
default	11:14:01.201427-0500	Nexy	FBSWorkspace unregistering source: <private>
error	11:14:01.201503-0500	Nexy	Error creating <FBSScene: 0xca07a0aa0; com.apple.controlcenter:D8913A5A-24CE-410F-87DF-549017D1A8AF>: <NSError: 0xc9f00e190; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	11:14:01.201559-0500	Nexy	No scene exists for identity: com.apple.controlcenter:D8913A5A-24CE-410F-87DF-549017D1A8AF
default	11:14:01.201565-0500	Nexy	Realizing settings extension FBSSceneTransitionContextCore on FBSSceneTransitionContext
default	11:14:01.204076-0500	Nexy	FBSWorkspace registering source: <private>
default	11:14:01.204092-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	11:14:01.204139-0500	Nexy	<FBSWorkspaceScenesClient:0xca07a0be0 <private>> attempting immediate handshake from activate
default	11:14:01.204159-0500	Nexy	<FBSWorkspaceScenesClient:0xca07a0be0 <private>> sent handshake
default	11:14:01.204231-0500	Nexy	Realizing settings extension __NSHostedViewSceneSettings__ on FBSSceneSettings
default	11:14:01.204585-0500	Nexy	Realizing settings extension __NSClientHostedViewSceneSettings__ on FBSSceneClientSettings
default	11:14:01.204669-0500	Nexy	<FBSWorkspaceScenesClient:0xca07a0be0 <private>> was invalidated
default	11:14:01.204683-0500	Nexy	FBSWorkspace unregistering source: <private>
default	11:14:01.204931-0500	Nexy	Realizing settings extension __NSStatusItemAuxiliaryViewSceneSettings__ on FBSSceneSettings
default	11:14:01.204977-0500	Nexy	Realizing settings extension __NSClientStatusItemAuxiliaryViewSceneSettings__ on FBSSceneClientSettings
default	11:14:01.205324-0500	Nexy	Requesting scene <FBSScene: 0xca07a0820; com.apple.controlcenter:D8913A5A-24CE-410F-87DF-549017D1A8AF-Aux[1]-NSStatusItemView> from com.apple.controlcenter.statusitems
error	11:14:01.205476-0500	Nexy	Error creating <FBSScene: 0xca07a0820; com.apple.controlcenter:D8913A5A-24CE-410F-87DF-549017D1A8AF-Aux[1]-NSStatusItemView>: <NSError: 0xc9f00ff90; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
default	11:14:01.205518-0500	Nexy	Request for <FBSScene: 0xca07a0820; com.apple.controlcenter:D8913A5A-24CE-410F-87DF-549017D1A8AF-Aux[1]-NSStatusItemView> complete!
error	11:14:01.205857-0500	Nexy	scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	11:14:01.205878-0500	Nexy	[com.apple.controlcenter:D8913A5A-24CE-410F-87DF-549017D1A8AF] No matching scene to invalidate for this identity.
error	11:14:01.205902-0500	Nexy	auxiliary scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	11:14:01.205938-0500	Nexy	Unhandled disconnected scene <private>
error	11:14:01.206032-0500	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
default	11:14:01.764435-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xc}
default	11:14:01.765491-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ef2a2","name":"Nexy(84850)"}, "details":{"deviceUIDs":["1C-77-54-18-C8-A3:output"],"implicit_category":"MediaPlayback","input_running":false,"output_running":true} }
default	11:14:01.765600-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 675, PID = 84850, Name = sid:0x1ef2a2, Nexy(84850), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	11:14:01.765635-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Category/Mode changed -- The score for sid:0x1ef2a2, Nexy(84850), 'prim'/com.nexy.assistant was not correct. Old score = 201
default	11:14:01.765670-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 675, PID = 84850, Name = sid:0x1ef2a2, Nexy(84850), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	11:14:01.765717-0500	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1ef2a2, Nexy(84850), 'prim'', AudioCategory changed to 'MediaPlayback'
default	11:14:01.765726-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	11:14:01.765786-0500	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 675, PID = 84850, Name = sid:0x1ef2a2, Nexy(84850), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO> is going active
default	11:14:01.765799-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsPlaying:]: MXCoreSession com.nexy.assistant with category/mode MediaPlayback/Default and coreSessionID = 675 starting playing
default	11:14:01.765918-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	11:14:01.765969-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	11:14:01.765939-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 675, PID = 84850, Name = sid:0x1ef2a2, Nexy(84850), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	11:14:01.765995-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 675, PID = 84850, Name = sid:0x1ef2a2, Nexy(84850), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO>
default	11:14:01.766124-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1ef2a2, Nexy(84850), 'prim'', displayID:'com.nexy.assistant'}
default	11:14:01.766155-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Will try to see if we can get the shared route for session = <ID: 675, PID = 84850, Name = sid:0x1ef2a2, Nexy(84850), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO>. Old (200) and New (201) scores.
default	11:14:01.766242-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 201, deviceID = <private>
default	11:14:01.766300-0500	audiomxd	AudioApplicationInfoImpl.mm:395   Successfully updated session 0x1ef2a2 to isSessionRecording: 0
	app: {"name":"[implicit] Nexy","pid":84850}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1ef2a2, sessionType: 'prim', isRecording: false }, 
]
default	11:14:01.766391-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 1]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)}
default	11:14:01.766412-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	11:14:01.766488-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 201 flag 0x1 < Hijack > app com.nexy.assistant CID 0xD310001 category Not set
default	11:14:01.766674-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	11:14:01.766747-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 201,
}
default	11:14:01.766772-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	11:14:01.766787-0500	audioaccessoryd	AudioStateChanged: Added audio session app com.nexy.assistant NULL -> 201 count 1
default	11:14:01.766796-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 201
error	11:14:01.766805-0500	audioaccessoryd	Updating local audio category 100 -> 201 app com.nexy.assistant
error	11:14:01.766851-0500	audioaccessoryd	Relaying via 24B92680-715A-E821-B5AF-358E78C2DAF9 inWxAddress 1C:77:54:18:C8:A3 to 88:20:0D:45:06:51 with options {
    "playingApp" : "com.nexy.assistant",
    "hostStreamingState" : "YES",
    "btAddress" : "A0:9A:8E:0D:58:86",
    "btName" : "Mac",
    "otherDeviceAudioCategory" : 201,
}
default	11:14:01.766912-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.nexy.assistant
default	11:14:02.207474-0500	Nexy	FBSWorkspace registering source: <private>
default	11:14:02.207535-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	11:14:02.207684-0500	Nexy	<FBSWorkspaceScenesClient:0xca07a0be0 <private>> attempting immediate handshake from activate
default	11:14:02.207736-0500	Nexy	<FBSWorkspaceScenesClient:0xca07a0be0 <private>> sent handshake
default	11:14:02.208219-0500	Nexy	Requesting scene <FBSScene: 0xca07a0820; com.apple.controlcenter:C2D8A201-4387-4BC8-93E9-C96B5CB09D68> from com.apple.controlcenter.statusitems
default	11:14:02.208661-0500	Nexy	Request for <FBSScene: 0xca07a0820; com.apple.controlcenter:C2D8A201-4387-4BC8-93E9-C96B5CB09D68> complete!
default	11:14:02.209166-0500	Nexy	<FBSWorkspaceScenesClient:0xca07a0be0 <private>> was invalidated
default	11:14:02.209235-0500	Nexy	FBSWorkspace unregistering source: <private>
default	11:14:02.209336-0500	Nexy	FBSWorkspace registering source: <private>
default	11:14:02.209371-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	11:14:02.209460-0500	Nexy	<FBSWorkspaceScenesClient:0xca07a0aa0 <private>> attempting immediate handshake from activate
default	11:14:02.209500-0500	Nexy	<FBSWorkspaceScenesClient:0xca07a0aa0 <private>> sent handshake
error	11:14:02.209611-0500	Nexy	Error creating <FBSScene: 0xca07a0820; com.apple.controlcenter:C2D8A201-4387-4BC8-93E9-C96B5CB09D68>: <NSError: 0xc9f00ff30; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	11:14:02.209649-0500	Nexy	No scene exists for identity: com.apple.controlcenter:C2D8A201-4387-4BC8-93E9-C96B5CB09D68
default	11:14:02.209767-0500	Nexy	Requesting scene <FBSScene: 0xca07a0a00; com.apple.controlcenter:C2D8A201-4387-4BC8-93E9-C96B5CB09D68-Aux[2]-NSStatusItemView> from com.apple.controlcenter.statusitems
default	11:14:02.210200-0500	Nexy	Request for <FBSScene: 0xca07a0a00; com.apple.controlcenter:C2D8A201-4387-4BC8-93E9-C96B5CB09D68-Aux[2]-NSStatusItemView> complete!
default	11:14:02.210423-0500	Nexy	<FBSWorkspaceScenesClient:0xca07a0aa0 <private>> was invalidated
default	11:14:02.210469-0500	Nexy	FBSWorkspace unregistering source: <private>
error	11:14:02.210561-0500	Nexy	Error creating <FBSScene: 0xca07a0a00; com.apple.controlcenter:C2D8A201-4387-4BC8-93E9-C96B5CB09D68-Aux[2]-NSStatusItemView>: <NSError: 0xc9f00fba0; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	11:14:02.210592-0500	Nexy	No scene exists for identity: com.apple.controlcenter:C2D8A201-4387-4BC8-93E9-C96B5CB09D68-Aux[2]-NSStatusItemView
default	11:14:02.211489-0500	Nexy	[com.apple.controlcenter:C2D8A201-4387-4BC8-93E9-C96B5CB09D68-Aux[2]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
error	11:14:02.212042-0500	Nexy	scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	11:14:02.212076-0500	Nexy	[com.apple.controlcenter:C2D8A201-4387-4BC8-93E9-C96B5CB09D68] No matching scene to invalidate for this identity.
error	11:14:02.212132-0500	Nexy	auxiliary scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	11:14:02.212163-0500	Nexy	[com.apple.controlcenter:C2D8A201-4387-4BC8-93E9-C96B5CB09D68-Aux[2]-NSStatusItemView] No matching scene to invalidate for this identity.
error	11:14:02.212810-0500	Nexy	Unhandled disconnected scene <private>
error	11:14:02.212937-0500	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
error	11:14:02.213072-0500	Nexy	Unhandled disconnected auxiliary scene <private>
error	11:14:02.213145-0500	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
default	11:14:03.028568-0500	audioaccessoryd	AudioStateSnapshot: Route:Bluetooth App com.nexy.assistant, Score 201, Remote 100NumofApp 1
default	11:14:03.213623-0500	Nexy	FBSWorkspace registering source: <private>
default	11:14:03.213660-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	11:14:03.213748-0500	Nexy	<FBSWorkspaceScenesClient:0xca07a0a00 <private>> attempting immediate handshake from activate
default	11:14:03.213781-0500	Nexy	<FBSWorkspaceScenesClient:0xca07a0a00 <private>> sent handshake
default	11:14:03.214085-0500	Nexy	Requesting scene <FBSScene: 0xca07a0820; com.apple.controlcenter:3F759F76-FA82-4375-9BE5-738904D2E74C> from com.apple.controlcenter.statusitems
default	11:14:03.214345-0500	Nexy	Request for <FBSScene: 0xca07a0820; com.apple.controlcenter:3F759F76-FA82-4375-9BE5-738904D2E74C> complete!
default	11:14:03.214696-0500	Nexy	<FBSWorkspaceScenesClient:0xca07a0a00 <private>> was invalidated
default	11:14:03.214725-0500	Nexy	FBSWorkspace unregistering source: <private>
error	11:14:03.214807-0500	Nexy	Error creating <FBSScene: 0xca07a0820; com.apple.controlcenter:3F759F76-FA82-4375-9BE5-738904D2E74C>: <NSError: 0xc9f00fc90; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	11:14:03.214829-0500	Nexy	No scene exists for identity: com.apple.controlcenter:3F759F76-FA82-4375-9BE5-738904D2E74C
default	11:14:03.214863-0500	Nexy	Requesting scene <FBSScene: 0xca07a0aa0; com.apple.controlcenter:3F759F76-FA82-4375-9BE5-738904D2E74C-Aux[3]-NSStatusItemView> from com.apple.controlcenter.statusitems
error	11:14:03.214965-0500	Nexy	Error creating <FBSScene: 0xca07a0aa0; com.apple.controlcenter:3F759F76-FA82-4375-9BE5-738904D2E74C-Aux[3]-NSStatusItemView>: <NSError: 0xc9f00ff00; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
default	11:14:03.215004-0500	Nexy	Request for <FBSScene: 0xca07a0aa0; com.apple.controlcenter:3F759F76-FA82-4375-9BE5-738904D2E74C-Aux[3]-NSStatusItemView> complete!
error	11:14:03.215184-0500	Nexy	scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	11:14:03.215202-0500	Nexy	[com.apple.controlcenter:3F759F76-FA82-4375-9BE5-738904D2E74C] No matching scene to invalidate for this identity.
error	11:14:03.215224-0500	Nexy	auxiliary scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	11:14:03.215257-0500	Nexy	Unhandled disconnected scene <private>
error	11:14:03.215316-0500	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
default	11:14:04.216499-0500	Nexy	FBSWorkspace registering source: <private>
default	11:14:04.216559-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	11:14:04.216716-0500	Nexy	<FBSWorkspaceScenesClient:0xca07a0aa0 <private>> attempting immediate handshake from activate
default	11:14:04.216772-0500	Nexy	<FBSWorkspaceScenesClient:0xca07a0aa0 <private>> sent handshake
default	11:14:04.217278-0500	Nexy	Requesting scene <FBSScene: 0xca07a0820; com.apple.controlcenter:444A1CAE-4D2B-4399-A86E-51FDF57FC907> from com.apple.controlcenter.statusitems
default	11:14:04.217703-0500	Nexy	Request for <FBSScene: 0xca07a0820; com.apple.controlcenter:444A1CAE-4D2B-4399-A86E-51FDF57FC907> complete!
default	11:14:04.218137-0500	Nexy	<FBSWorkspaceScenesClient:0xca07a0aa0 <private>> was invalidated
default	11:14:04.218194-0500	Nexy	FBSWorkspace unregistering source: <private>
default	11:14:04.218332-0500	Nexy	FBSWorkspace registering source: <private>
default	11:14:04.218364-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	11:14:04.218449-0500	Nexy	<FBSWorkspaceScenesClient:0xca07a0a00 <private>> attempting immediate handshake from activate
default	11:14:04.218480-0500	Nexy	<FBSWorkspaceScenesClient:0xca07a0a00 <private>> sent handshake
error	11:14:04.218585-0500	Nexy	Error creating <FBSScene: 0xca07a0820; com.apple.controlcenter:444A1CAE-4D2B-4399-A86E-51FDF57FC907>: <NSError: 0xc9f00fea0; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	11:14:04.218611-0500	Nexy	No scene exists for identity: com.apple.controlcenter:444A1CAE-4D2B-4399-A86E-51FDF57FC907
default	11:14:04.218707-0500	Nexy	Requesting scene <FBSScene: 0xca07a0be0; com.apple.controlcenter:444A1CAE-4D2B-4399-A86E-51FDF57FC907-Aux[4]-NSStatusItemView> from com.apple.controlcenter.statusitems
default	11:14:04.218998-0500	Nexy	Request for <FBSScene: 0xca07a0be0; com.apple.controlcenter:444A1CAE-4D2B-4399-A86E-51FDF57FC907-Aux[4]-NSStatusItemView> complete!
default	11:14:04.219294-0500	Nexy	<FBSWorkspaceScenesClient:0xca07a0a00 <private>> was invalidated
default	11:14:04.219327-0500	Nexy	FBSWorkspace unregistering source: <private>
error	11:14:04.219420-0500	Nexy	Error creating <FBSScene: 0xca07a0be0; com.apple.controlcenter:444A1CAE-4D2B-4399-A86E-51FDF57FC907-Aux[4]-NSStatusItemView>: <NSError: 0xc9f00e190; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	11:14:04.219445-0500	Nexy	No scene exists for identity: com.apple.controlcenter:444A1CAE-4D2B-4399-A86E-51FDF57FC907-Aux[4]-NSStatusItemView
default	11:14:04.219708-0500	Nexy	[com.apple.controlcenter:444A1CAE-4D2B-4399-A86E-51FDF57FC907-Aux[4]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
error	11:14:04.220057-0500	Nexy	scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	11:14:04.220083-0500	Nexy	[com.apple.controlcenter:444A1CAE-4D2B-4399-A86E-51FDF57FC907] No matching scene to invalidate for this identity.
error	11:14:04.220124-0500	Nexy	auxiliary scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	11:14:04.220148-0500	Nexy	[com.apple.controlcenter:444A1CAE-4D2B-4399-A86E-51FDF57FC907-Aux[4]-NSStatusItemView] No matching scene to invalidate for this identity.
error	11:14:04.220659-0500	Nexy	Unhandled disconnected scene <private>
error	11:14:04.220762-0500	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
error	11:14:04.220861-0500	Nexy	Unhandled disconnected auxiliary scene <private>
error	11:14:04.220927-0500	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
default	11:14:05.136742-0500	Nexy	void _updateToReflectAutomaticTerminationState(void) Setting _kLSApplicationWouldBeTerminatedByTALKey=1
default	11:14:05.220930-0500	Nexy	FBSWorkspace registering source: <private>
default	11:14:05.220989-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	11:14:05.221127-0500	Nexy	<FBSWorkspaceScenesClient:0xca07a0be0 <private>> attempting immediate handshake from activate
default	11:14:05.221178-0500	Nexy	<FBSWorkspaceScenesClient:0xca07a0be0 <private>> sent handshake
default	11:14:05.221690-0500	Nexy	Requesting scene <FBSScene: 0xca07a0820; com.apple.controlcenter:9049E6D1-A9E0-4EF6-878F-A881E3B8580B> from com.apple.controlcenter.statusitems
default	11:14:05.222045-0500	Nexy	Request for <FBSScene: 0xca07a0820; com.apple.controlcenter:9049E6D1-A9E0-4EF6-878F-A881E3B8580B> complete!
default	11:14:05.222383-0500	Nexy	<FBSWorkspaceScenesClient:0xca07a0be0 <private>> was invalidated
default	11:14:05.222419-0500	Nexy	FBSWorkspace unregistering source: <private>
default	11:14:05.222475-0500	Nexy	FBSWorkspace registering source: <private>
default	11:14:05.222498-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	11:14:05.222557-0500	Nexy	<FBSWorkspaceScenesClient:0xca07a0d20 <private>> attempting immediate handshake from activate
default	11:14:05.222582-0500	Nexy	<FBSWorkspaceScenesClient:0xca07a0d20 <private>> sent handshake
error	11:14:05.222671-0500	Nexy	Error creating <FBSScene: 0xca07a0820; com.apple.controlcenter:9049E6D1-A9E0-4EF6-878F-A881E3B8580B>: <NSError: 0xc9f00dcb0; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	11:14:05.222707-0500	Nexy	No scene exists for identity: com.apple.controlcenter:9049E6D1-A9E0-4EF6-878F-A881E3B8580B
default	11:14:05.222832-0500	Nexy	Requesting scene <FBSScene: 0xca07a0aa0; com.apple.controlcenter:9049E6D1-A9E0-4EF6-878F-A881E3B8580B-Aux[5]-NSStatusItemView> from com.apple.controlcenter.statusitems
default	11:14:05.223125-0500	Nexy	Request for <FBSScene: 0xca07a0aa0; com.apple.controlcenter:9049E6D1-A9E0-4EF6-878F-A881E3B8580B-Aux[5]-NSStatusItemView> complete!
default	11:14:05.223417-0500	Nexy	<FBSWorkspaceScenesClient:0xca07a0d20 <private>> was invalidated
default	11:14:05.223458-0500	Nexy	FBSWorkspace unregistering source: <private>
error	11:14:05.223536-0500	Nexy	Error creating <FBSScene: 0xca07a0aa0; com.apple.controlcenter:9049E6D1-A9E0-4EF6-878F-A881E3B8580B-Aux[5]-NSStatusItemView>: <NSError: 0xc9f00fdb0; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	11:14:05.223558-0500	Nexy	No scene exists for identity: com.apple.controlcenter:9049E6D1-A9E0-4EF6-878F-A881E3B8580B-Aux[5]-NSStatusItemView
default	11:14:05.223745-0500	Nexy	[com.apple.controlcenter:9049E6D1-A9E0-4EF6-878F-A881E3B8580B-Aux[5]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
error	11:14:05.224047-0500	Nexy	scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	11:14:05.224076-0500	Nexy	[com.apple.controlcenter:9049E6D1-A9E0-4EF6-878F-A881E3B8580B] No matching scene to invalidate for this identity.
error	11:14:05.224117-0500	Nexy	auxiliary scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	11:14:05.224142-0500	Nexy	[com.apple.controlcenter:9049E6D1-A9E0-4EF6-878F-A881E3B8580B-Aux[5]-NSStatusItemView] No matching scene to invalidate for this identity.
error	11:14:05.224613-0500	Nexy	Unhandled disconnected scene <private>
error	11:14:05.224724-0500	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
error	11:14:05.224788-0500	Nexy	Unhandled disconnected auxiliary scene <private>
error	11:14:05.224838-0500	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
default	11:14:06.030205-0500	audioaccessoryd	AudioStateSnapshot: Route:Bluetooth App com.nexy.assistant, Score 201, Remote 100NumofApp 1
default	11:14:06.225641-0500	Nexy	FBSWorkspace registering source: <private>
default	11:14:06.225697-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	11:14:06.225835-0500	Nexy	<FBSWorkspaceScenesClient:0xca07a0aa0 <private>> attempting immediate handshake from activate
default	11:14:06.225886-0500	Nexy	<FBSWorkspaceScenesClient:0xca07a0aa0 <private>> sent handshake
default	11:14:06.226346-0500	Nexy	Requesting scene <FBSScene: 0xca07a0820; com.apple.controlcenter:0C4077F1-17A3-4816-91A8-A9BD611EADF5> from com.apple.controlcenter.statusitems
default	11:14:06.226691-0500	Nexy	Request for <FBSScene: 0xca07a0820; com.apple.controlcenter:0C4077F1-17A3-4816-91A8-A9BD611EADF5> complete!
default	11:14:06.227015-0500	Nexy	<FBSWorkspaceScenesClient:0xca07a0aa0 <private>> was invalidated
default	11:14:06.227052-0500	Nexy	FBSWorkspace unregistering source: <private>
error	11:14:06.227163-0500	Nexy	Error creating <FBSScene: 0xca07a0820; com.apple.controlcenter:0C4077F1-17A3-4816-91A8-A9BD611EADF5>: <NSError: 0xc9f00dd70; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	11:14:06.227245-0500	Nexy	No scene exists for identity: com.apple.controlcenter:0C4077F1-17A3-4816-91A8-A9BD611EADF5
default	11:14:06.227324-0500	Nexy	FBSWorkspace registering source: <private>
default	11:14:06.227463-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	11:14:06.227617-0500	Nexy	<FBSWorkspaceScenesClient:0xca07a0be0 <private>> attempting immediate handshake from activate
default	11:14:06.227674-0500	Nexy	<FBSWorkspaceScenesClient:0xca07a0be0 <private>> sent handshake
default	11:14:06.227930-0500	Nexy	Requesting scene <FBSScene: 0xca07a0dc0; com.apple.controlcenter:0C4077F1-17A3-4816-91A8-A9BD611EADF5-Aux[6]-NSStatusItemView> from com.apple.controlcenter.statusitems
default	11:14:06.228143-0500	Nexy	Request for <FBSScene: 0xca07a0dc0; com.apple.controlcenter:0C4077F1-17A3-4816-91A8-A9BD611EADF5-Aux[6]-NSStatusItemView> complete!
default	11:14:06.228490-0500	Nexy	<FBSWorkspaceScenesClient:0xca07a0be0 <private>> was invalidated
default	11:14:06.228518-0500	Nexy	FBSWorkspace unregistering source: <private>
error	11:14:06.228586-0500	Nexy	Error creating <FBSScene: 0xca07a0dc0; com.apple.controlcenter:0C4077F1-17A3-4816-91A8-A9BD611EADF5-Aux[6]-NSStatusItemView>: <NSError: 0xc9f00fd50; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	11:14:06.228637-0500	Nexy	No scene exists for identity: com.apple.controlcenter:0C4077F1-17A3-4816-91A8-A9BD611EADF5-Aux[6]-NSStatusItemView
default	11:14:06.228667-0500	Nexy	[com.apple.controlcenter:0C4077F1-17A3-4816-91A8-A9BD611EADF5-Aux[6]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
error	11:14:06.229012-0500	Nexy	scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	11:14:06.229032-0500	Nexy	[com.apple.controlcenter:0C4077F1-17A3-4816-91A8-A9BD611EADF5] No matching scene to invalidate for this identity.
error	11:14:06.229110-0500	Nexy	auxiliary scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	11:14:06.229176-0500	Nexy	[com.apple.controlcenter:0C4077F1-17A3-4816-91A8-A9BD611EADF5-Aux[6]-NSStatusItemView] No matching scene to invalidate for this identity.
error	11:14:06.229629-0500	Nexy	Unhandled disconnected scene <private>
error	11:14:06.229727-0500	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
error	11:14:06.229784-0500	Nexy	Unhandled disconnected auxiliary scene <private>
error	11:14:06.229820-0500	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
default	11:14:06.416268-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	11:14:06.416332-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant)]
default	11:14:06.416368-0500	ControlCenter	Active activity attributions changed to ["scr:com.nexy.assistant"]
default	11:14:06.417557-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:14:06.417583-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:14:06.417597-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	11:14:06.417606-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:14:06.417613-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	11:14:06.417619-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	11:14:06.417720-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	11:14:06.440958-0500	runningboardd	Periodic Run States <RBProcessState| identity:app<application.com.nexy.assistant.20931626.20931632(501)> role:UserInteractive gpuRole:None coalitionLevel:100 explicitJetsamBand:0 memoryLimit:Inactive(Default) flags:60 guaranteedRunning:NO legacyFinishTaskReason:0 inheritances:<RBMutableInheritanceCollection| inheritancesByEnvironment:{
	
	}> primitiveAssertions:[
	<RBSProcessAssertionInfo| type:2 reason:20246 name:"Domain" domain:"com.apple.launchservicesd:RoleUserInteractive" expl:"uielement:84850">
	] endowments:[
	<RBSProcessEndowmentInfo| namespace:com.apple.launchservices.userfacing env:(null)  0>
	]>
default	11:14:06.826859-0500	Nexy	NSApplication._react(to:) dock
default	11:14:06.826870-0500	Nexy	NSApplication._react(to:) reactions=83
default	11:14:07.165983-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Output {1C-77-54-18-C8-A3:output, 0xc}
default	11:14:07.166408-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ef2a2","name":"Nexy(84850)"}, "details":{"deviceUIDs":[],"implicit_category":"","input_running":false,"output_running":false} }
default	11:14:07.166528-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsPlaying:]: MXCoreSession com.nexy.assistant with category/mode MediaPlayback/Default and coreSessionID = 675 stopping playing
default	11:14:07.166588-0500	audiomxd	-MXCoreSession- -[MXCoreSession endInterruption:]: Session <ID: 675, PID = 84850, Name = sid:0x1ef2a2, Nexy(84850), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> is going inactive
default	11:14:07.166630-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 675, PID = 84850, Name = sid:0x1ef2a2, Nexy(84850), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	11:14:07.166702-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 675, PID = 84850, Name = sid:0x1ef2a2, Nexy(84850), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	11:14:07.166793-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	11:14:07.166959-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 0]. BT device UIDS: {(
)}
default	11:14:07.166857-0500	audiomxd	AudioApplicationInfoImpl.mm:395   Successfully updated session 0x1ef2a2 to isSessionRecording: 0
	app: {"name":"[implicit] Nexy","pid":84850}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1ef2a2, sessionType: 'prim', isRecording: false }, 
]
default	11:14:07.166973-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	11:14:07.167013-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	11:14:07.167087-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	11:14:07.167113-0500	audioaccessoryd	AudioStateChanged: Removed audio session app com.nexy.assistant 201 count 0
default	11:14:07.174959-0500	coreaudiod	Sending message. { reporterID=364427975065604, category=IO, type=error, message=["issue_type": Optional(overload), "wg_cycles": Optional(1668477), "smallest_buffer_frame_size": Optional(2147483647), "lateness": Optional(698), "wg_total_wakeups": Optional(5), "start_time": Optional(12960632909316), "wg_instructions": Optional(847860), "anchor_sample_time": Optional(2692), "is_prewarming": Optional(0), "wg_system_time_mach": Optional(3526), "cause": Optional(ClientHALIODurationExceededBudget,SafetyViolationOccurred), "wg_external_wakeups": Optional(3), "cause_set": Optional(12), "io_frame_counter": Optional(258048), "HostApplicationDisplayID": Optional(com.nexy.assistant), "is_recovering": Optional(0), "multi_cycle_io_page_faults_duration": Optional(0), "io_cycle": Optional(504), "other_page_faults": Optional(0), "time_since_prev_overload": Optional(540026397110166), "io_cycle_usage": Optional(1), "num_continuous_silent_io_cycles": Optional(85), "safety_violation_time_gap": Optional(0.015125), "io_page_faults": Optional(0), "num_continuous_nonzero_io<…> }
default	11:14:07.229646-0500	Nexy	FBSWorkspace registering source: <private>
default	11:14:07.229686-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	11:14:07.229770-0500	Nexy	<FBSWorkspaceScenesClient:0xca07a0dc0 <private>> attempting immediate handshake from activate
default	11:14:07.229804-0500	Nexy	<FBSWorkspaceScenesClient:0xca07a0dc0 <private>> sent handshake
default	11:14:07.230119-0500	Nexy	Requesting scene <FBSScene: 0xca07a0be0; com.apple.controlcenter:8393A436-20A2-4D2F-BFF5-26985B81A08B> from com.apple.controlcenter.statusitems
default	11:14:07.230387-0500	Nexy	Request for <FBSScene: 0xca07a0be0; com.apple.controlcenter:8393A436-20A2-4D2F-BFF5-26985B81A08B> complete!
default	11:14:07.230792-0500	Nexy	Requesting scene <FBSScene: 0xca07a0a00; com.apple.controlcenter:8393A436-20A2-4D2F-BFF5-26985B81A08B-Aux[7]-NSStatusItemView> from com.apple.controlcenter.statusitems
default	11:14:07.230823-0500	Nexy	<FBSWorkspaceScenesClient:0xca07a0dc0 <private>> was invalidated
default	11:14:07.230854-0500	Nexy	FBSWorkspace unregistering source: <private>
error	11:14:07.230914-0500	Nexy	Error creating <FBSScene: 0xca07a0be0; com.apple.controlcenter:8393A436-20A2-4D2F-BFF5-26985B81A08B>: <NSError: 0xc9f00db00; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	11:14:07.230933-0500	Nexy	No scene exists for identity: com.apple.controlcenter:8393A436-20A2-4D2F-BFF5-26985B81A08B
error	11:14:07.230969-0500	Nexy	Error creating <FBSScene: 0xca07a0a00; com.apple.controlcenter:8393A436-20A2-4D2F-BFF5-26985B81A08B-Aux[7]-NSStatusItemView>: <NSError: 0xc9f00e460; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
default	11:14:07.230974-0500	Nexy	Request for <FBSScene: 0xca07a0a00; com.apple.controlcenter:8393A436-20A2-4D2F-BFF5-26985B81A08B-Aux[7]-NSStatusItemView> complete!
error	11:14:07.230982-0500	Nexy	No scene exists for identity: com.apple.controlcenter:8393A436-20A2-4D2F-BFF5-26985B81A08B-Aux[7]-NSStatusItemView
error	11:14:07.231133-0500	Nexy	scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	11:14:07.231149-0500	Nexy	[com.apple.controlcenter:8393A436-20A2-4D2F-BFF5-26985B81A08B] No matching scene to invalidate for this identity.
error	11:14:07.231170-0500	Nexy	auxiliary scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	11:14:07.231194-0500	Nexy	Unhandled disconnected scene <private>
error	11:14:07.231257-0500	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
default	11:14:07.380003-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=84935.1, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=84850, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.osascript, pid=84935, auid=501, euid=501, binary_path=/usr/bin/osascript}, },
default	11:14:07.381591-0500	tccd	AUTHREQ_SUBJECT: msgID=84935.1, subject=com.nexy.assistant,
default	11:14:07.382246-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d114900 at /Applications/Nexy.app
default	11:14:07.396198-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=393.16917, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=84850, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.osascript, pid=84935, auid=501, euid=501, binary_path=/usr/bin/osascript}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=393, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	11:14:07.397104-0500	tccd	AUTHREQ_SUBJECT: msgID=393.16917, subject=com.nexy.assistant,
default	11:14:07.397716-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d114900 at /Applications/Nexy.app
default	11:14:07.426451-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d114900 at /Applications/Nexy.app
default	11:14:07.446990-0500	System Events	TCCAccessRequestIndirect: TCCAccessRequestIndirect with pid 84855: target_identity: {
    kTCCCodeIdentityAuditToken = {length = 32, bytes = 0xf5010000 f5010000 14000000 f5010000 ... b7860100 1c282700 };
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
default	11:14:07.463217-0500	tccd	target_executable_path_URL: file:///Applications/Nexy.app/Contents/MacOS/Nexy
default	11:14:08.232469-0500	Nexy	FBSWorkspace registering source: <private>
default	11:14:08.232541-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	11:14:08.232697-0500	Nexy	<FBSWorkspaceScenesClient:0xca07a0dc0 <private>> attempting immediate handshake from activate
default	11:14:08.232772-0500	Nexy	<FBSWorkspaceScenesClient:0xca07a0dc0 <private>> sent handshake
default	11:14:08.233279-0500	Nexy	Requesting scene <FBSScene: 0xca07a0c80; com.apple.controlcenter:B0D85CD0-F418-4F31-9190-D740322B2EF1> from com.apple.controlcenter.statusitems
default	11:14:08.233747-0500	Nexy	Request for <FBSScene: 0xca07a0c80; com.apple.controlcenter:B0D85CD0-F418-4F31-9190-D740322B2EF1> complete!
default	11:14:08.234225-0500	Nexy	<FBSWorkspaceScenesClient:0xca07a0dc0 <private>> was invalidated
default	11:14:08.234287-0500	Nexy	FBSWorkspace unregistering source: <private>
default	11:14:08.234388-0500	Nexy	FBSWorkspace registering source: <private>
default	11:14:08.234422-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	11:14:08.234515-0500	Nexy	<FBSWorkspaceScenesClient:0xca07a0be0 <private>> attempting immediate handshake from activate
default	11:14:08.234554-0500	Nexy	<FBSWorkspaceScenesClient:0xca07a0be0 <private>> sent handshake
error	11:14:08.234666-0500	Nexy	Error creating <FBSScene: 0xca07a0c80; com.apple.controlcenter:B0D85CD0-F418-4F31-9190-D740322B2EF1>: <NSError: 0xc9f00e0d0; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	11:14:08.234703-0500	Nexy	No scene exists for identity: com.apple.controlcenter:B0D85CD0-F418-4F31-9190-D740322B2EF1
default	11:14:08.234793-0500	Nexy	Requesting scene <FBSScene: 0xca07a0820; com.apple.controlcenter:B0D85CD0-F418-4F31-9190-D740322B2EF1-Aux[8]-NSStatusItemView> from com.apple.controlcenter.statusitems
default	11:14:08.235033-0500	Nexy	Request for <FBSScene: 0xca07a0820; com.apple.controlcenter:B0D85CD0-F418-4F31-9190-D740322B2EF1-Aux[8]-NSStatusItemView> complete!
default	11:14:08.235254-0500	Nexy	<FBSWorkspaceScenesClient:0xca07a0be0 <private>> was invalidated
default	11:14:08.235277-0500	Nexy	FBSWorkspace unregistering source: <private>
error	11:14:08.235328-0500	Nexy	Error creating <FBSScene: 0xca07a0820; com.apple.controlcenter:B0D85CD0-F418-4F31-9190-D740322B2EF1-Aux[8]-NSStatusItemView>: <NSError: 0xc9f00db00; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	11:14:08.235343-0500	Nexy	No scene exists for identity: com.apple.controlcenter:B0D85CD0-F418-4F31-9190-D740322B2EF1-Aux[8]-NSStatusItemView
default	11:14:08.235507-0500	Nexy	[com.apple.controlcenter:B0D85CD0-F418-4F31-9190-D740322B2EF1-Aux[8]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
error	11:14:08.235722-0500	Nexy	scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	11:14:08.235738-0500	Nexy	[com.apple.controlcenter:B0D85CD0-F418-4F31-9190-D740322B2EF1] No matching scene to invalidate for this identity.
error	11:14:08.235764-0500	Nexy	auxiliary scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	11:14:08.235776-0500	Nexy	[com.apple.controlcenter:B0D85CD0-F418-4F31-9190-D740322B2EF1-Aux[8]-NSStatusItemView] No matching scene to invalidate for this identity.
error	11:14:08.236213-0500	Nexy	Unhandled disconnected scene <private>
error	11:14:08.236291-0500	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
error	11:14:08.236341-0500	Nexy	Unhandled disconnected auxiliary scene <private>
error	11:14:08.236371-0500	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
default	11:14:09.237205-0500	Nexy	FBSWorkspace registering source: <private>
default	11:14:09.237253-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	11:14:09.237344-0500	Nexy	<FBSWorkspaceScenesClient:0xca07a0820 <private>> attempting immediate handshake from activate
default	11:14:09.237375-0500	Nexy	<FBSWorkspaceScenesClient:0xca07a0820 <private>> sent handshake
default	11:14:09.237673-0500	Nexy	Requesting scene <FBSScene: 0xca07a0c80; com.apple.controlcenter:3BE2EBC9-0DC8-42BE-88A8-788080BA6259> from com.apple.controlcenter.statusitems
default	11:14:09.237926-0500	Nexy	Request for <FBSScene: 0xca07a0c80; com.apple.controlcenter:3BE2EBC9-0DC8-42BE-88A8-788080BA6259> complete!
default	11:14:09.238240-0500	Nexy	<FBSWorkspaceScenesClient:0xca07a0820 <private>> was invalidated
default	11:14:09.238265-0500	Nexy	FBSWorkspace unregistering source: <private>
error	11:14:09.238334-0500	Nexy	Error creating <FBSScene: 0xca07a0c80; com.apple.controlcenter:3BE2EBC9-0DC8-42BE-88A8-788080BA6259>: <NSError: 0xc9f00df80; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	11:14:09.238352-0500	Nexy	No scene exists for identity: com.apple.controlcenter:3BE2EBC9-0DC8-42BE-88A8-788080BA6259
default	11:14:09.238401-0500	Nexy	Requesting scene <FBSScene: 0xca07a0dc0; com.apple.controlcenter:3BE2EBC9-0DC8-42BE-88A8-788080BA6259-Aux[9]-NSStatusItemView> from com.apple.controlcenter.statusitems
error	11:14:09.238500-0500	Nexy	Error creating <FBSScene: 0xca07a0dc0; com.apple.controlcenter:3BE2EBC9-0DC8-42BE-88A8-788080BA6259-Aux[9]-NSStatusItemView>: <NSError: 0xc9f00e460; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
default	11:14:09.238538-0500	Nexy	Request for <FBSScene: 0xca07a0dc0; com.apple.controlcenter:3BE2EBC9-0DC8-42BE-88A8-788080BA6259-Aux[9]-NSStatusItemView> complete!
error	11:14:09.238681-0500	Nexy	scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	11:14:09.238698-0500	Nexy	[com.apple.controlcenter:3BE2EBC9-0DC8-42BE-88A8-788080BA6259] No matching scene to invalidate for this identity.
error	11:14:09.238723-0500	Nexy	auxiliary scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	11:14:09.238748-0500	Nexy	Unhandled disconnected scene <private>
error	11:14:09.238811-0500	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
