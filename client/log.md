default	20:18:08.405199-0500	lsd	com.nexy.assistant/Unknown Persona:5:5:1:1:Building bundle record for app
default	20:18:08.405348-0500	lsd	com.nexy.assistant/Unknown Persona:5:5:2:1:Built bundle record for app
default	20:18:08.406794-0500	lsd	com.nexy.assistant/Unknown Persona:5:4:2:1:_LSServerRegisterItemInfo result = 0
default	20:18:08.410518-0500	dmd	Received xpc stream event (distributed notification matching) with name: com.apple.LaunchServices.applicationRegistered user info: {
    CFBundleDisplayName = Nexy;
    bundleIDs =     (
        "com.nexy.assistant"
    );
    isPlaceholder = 0;
}
default	20:18:08.414470-0500	runningboardd	Launch request for app<application.com.nexy.assistant.27241569.27241575(501)>[0] is using uid 501 (divined from auid 501 euid 501)
default	20:18:08.414535-0500	runningboardd	Acquiring assertion targeting app<application.com.nexy.assistant.27241569.27241575(501)> from originator [osservice<com.apple.coreservices.uiagent(501)>:3678] with description <RBSAssertionDescriptor| "LS launch com.nexy.assistant" ID:403-3678-159057 target:app<application.com.nexy.assistant.27241569.27241575(501)> attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"LaunchRoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	20:18:08.414613-0500	runningboardd	Assertion 403-3678-159057 (target:app<application.com.nexy.assistant.27241569.27241575(501)>) will be created as active
default	20:18:08.417277-0500	runningboardd	Checking PreventLaunch: global:0 exPath:/Applications/Nexy.app/Contents/MacOS/Nexy predicates:(null) allow:(null)
default	20:18:08.417306-0500	runningboardd	Creating and launching job for: app<application.com.nexy.assistant.27241569.27241575(501)>
default	20:18:08.417319-0500	runningboardd	_mutateContextIfNeeded called for com.nexy.assistant
default	20:18:08.417407-0500	runningboardd	app<application.com.nexy.assistant.27241569.27241575(501)>: -[RBPersonaManager personaForIdentity:context:personaUID:personaUniqueString:] required 0.000954 ms (wallclock); resolved to {4294967295, (null)}
default	20:18:08.473252-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575(501)>:35241] is not RunningBoard jetsam managed.
default	20:18:08.473268-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575(501)>:35241] This process will not be managed.
default	20:18:08.473278-0500	runningboardd	Now tracking process: [app<application.com.nexy.assistant.27241569.27241575(501)>:35241]
default	20:18:08.473453-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.27241569.27241575(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:18:08.474104-0500	gamepolicyd	Hit the server for a process handle 15e721a3000089a9 that resolved to: [app<application.com.nexy.assistant.27241569.27241575(501)>:35241]
default	20:18:08.474138-0500	gamepolicyd	Received state update for 35241 (app<application.com.nexy.assistant.27241569.27241575(501)>, running-active-NotVisible
default	20:18:08.477164-0500	runningboardd	Using default underlying assertion for app: [app<application.com.nexy.assistant.27241569.27241575(501)>:35241]
default	20:18:08.477224-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.27241569.27241575(501)>:35241] from originator [app<application.com.nexy.assistant.27241569.27241575(501)>:35241] with description <RBSAssertionDescriptor| "RB Underlying Assertion" ID:403-403-159058 target:35241 attributes:[
	<RBSDomainAttribute| domain:"com.apple.underlying" name:"defaultUnderlyingAppAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	20:18:08.477349-0500	runningboardd	Assertion 403-403-159058 (target:[app<application.com.nexy.assistant.27241569.27241575(501)>:35241]) will be created as active
default	20:18:08.477533-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575(501)>:35241] Ignoring jetsam update because this process is not memory-managed
default	20:18:08.477550-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575(501)>:35241] Ignoring suspend because this process is not lifecycle managed
default	20:18:08.477570-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575(501)>:35241] Set darwin role to: UserInteractive
default	20:18:08.477588-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575(501)>:35241] Ignoring GPU update because this process is not GPU managed
default	20:18:08.477627-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575(501)>:35241] Ignoring memory limit update because this process is not memory-managed
default	20:18:08.477690-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575(501)>:35241] reported to RB as running
default	20:18:08.479546-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.27241569.27241575(501)>:35241] from originator [osservice<com.apple.coreservices.launchservicesd>:367] with description <RBSAssertionDescriptor| "uielement:35241" ID:403-367-159059 target:35241 attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"RoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	20:18:08.479696-0500	runningboardd	Assertion 403-367-159059 (target:[app<application.com.nexy.assistant.27241569.27241575(501)>:35241]) will be created as active
default	20:18:08.479800-0500	CoreServicesUIAgent	LAUNCH: 0x0-0x3c13c1 com.nexy.assistant starting stopped process.
default	20:18:08.481231-0500	loginwindow	-[Application updateInformation] | Got App URL: file:///Applications/Nexy.app/
default	20:18:08.482070-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575(501)>:35241] Ignoring jetsam update because this process is not memory-managed
default	20:18:08.482112-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575(501)>:35241] Ignoring suspend because this process is not lifecycle managed
default	20:18:08.482160-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575(501)>:35241] Ignoring GPU update because this process is not GPU managed
default	20:18:08.482249-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575(501)>:35241] Ignoring memory limit update because this process is not memory-managed
default	20:18:08.482419-0500	runningboardd	Successfully acquired underlying assertion for [app<application.com.nexy.assistant.27241569.27241575(501)>:35241]
default	20:18:08.483625-0500	loginwindow	-[Application setState:] | enter: <Application: 0x84f9b6800: Nexy> state 2
default	20:18:08.483673-0500	loginwindow	-[ApplicationManager checkInAppContext:eventData:] | ApplicationManager: Checked in app : Nexy
default	20:18:08.484474-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.27241569.27241575(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:18:08.484890-0500	runningboardd	Invalidating assertion 403-3678-159057 (target:app<application.com.nexy.assistant.27241569.27241575(501)>) from originator [osservice<com.apple.coreservices.uiagent(501)>:3678]
default	20:18:08.484925-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575(501)>:35241] Ignoring jetsam update because this process is not memory-managed
default	20:18:08.484963-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575(501)>:35241] Ignoring suspend because this process is not lifecycle managed
default	20:18:08.485018-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575(501)>:35241] Ignoring GPU update because this process is not GPU managed
default	20:18:08.485054-0500	gamepolicyd	Received state update for 35241 (app<application.com.nexy.assistant.27241569.27241575(501)>, running-active-NotVisible
default	20:18:08.485124-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575(501)>:35241] Ignoring memory limit update because this process is not memory-managed
default	20:18:08.487972-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.27241569.27241575(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:18:08.589164-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575(501)>:35241] Ignoring jetsam update because this process is not memory-managed
default	20:18:08.589179-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575(501)>:35241] Ignoring suspend because this process is not lifecycle managed
default	20:18:08.589195-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575(501)>:35241] Ignoring GPU update because this process is not GPU managed
default	20:18:08.589227-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575(501)>:35241] Ignoring memory limit update because this process is not memory-managed
default	20:18:08.589334-0500	gamepolicyd	Received state update for 35241 (app<application.com.nexy.assistant.27241569.27241575(501)>, running-active-NotVisible
default	20:18:08.592178-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.27241569.27241575(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:18:08.592545-0500	gamepolicyd	Received state update for 35241 (app<application.com.nexy.assistant.27241569.27241575(501)>, running-active-NotVisible
default	20:18:08.654025-0500	syspolicyd	GK evaluateScanResult: 3, PST: (path: a2cffff67b96be6e), (team: 5NKLL2CLB9), (id: com.nexy.assistant), (bundle_id: (null)), 0, 0, 1, 0, 9, 4, 1
default	20:18:08.655219-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=483.33, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=35241, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.syspolicyd, pid=483, auid=0, euid=0, binary_path=/usr/libexec/syspolicyd}, },
default	20:18:08.661448-0500	tccd	AUTHREQ_SUBJECT: msgID=483.33, subject=com.nexy.assistant,
default	20:18:08.662106-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x92f17b600 at /Applications/Nexy.app
default	20:18:08.825222-0500	Nexy	[0x106356110] activating connection: mach=true listener=false peer=false name=com.apple.cfprefsd.daemon
default	20:18:08.825292-0500	Nexy	[0x106356650] activating connection: mach=true listener=false peer=false name=com.apple.cfprefsd.agent
error	20:18:09.093933-0500	Nexy	dlsym cannot find symbol NSMakeRect in CFBundle 0x106360830 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	20:18:09.094171-0500	Nexy	dlsym cannot find symbol NSMakePoint in CFBundle 0x106360830 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	20:18:09.094381-0500	Nexy	dlsym cannot find symbol NSMakeSize in CFBundle 0x106360830 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	20:18:09.094578-0500	Nexy	dlsym cannot find symbol NSMakeRange in CFBundle 0x106360830 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
default	20:18:09.095809-0500	Nexy	[0x1063440e0] activating connection: mach=true listener=false peer=false name=com.apple.coreservices.launchservicesd
default	20:18:09.096574-0500	Nexy	[0x863d48000] activating connection: mach=true listener=false peer=false name=com.apple.analyticsd
default	20:18:09.096932-0500	Nexy	[0x863d48140] activating connection: mach=true listener=false peer=false name=com.apple.pasteboard.1
default	20:18:09.097373-0500	Nexy	[0x863d48280] activating connection: mach=true listener=false peer=false name=com.apple.distributed_notifications@Uv3
default	20:18:09.098279-0500	Nexy	Received configuration update from daemon (initial)
default	20:18:09.099488-0500	Nexy	void _NSDisableAutomaticTerminationAndLog(NSString *) No windows open yet
default	20:18:09.099919-0500	Nexy	[0x863d483c0] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	20:18:09.100779-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=35241.1, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=35241, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	20:18:09.102507-0500	tccd	AUTHREQ_SUBJECT: msgID=35241.1, subject=com.nexy.assistant,
default	20:18:09.103324-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x92f17bc00 at /Applications/Nexy.app
default	20:18:09.140734-0500	Nexy	[0x863d483c0] invalidated after the last release of the connection object
default	20:18:09.141043-0500	Nexy	server port 0x0000320f, session port 0x0000320f
default	20:18:09.142019-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=397.2713, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=35241, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=397, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	20:18:09.142047-0500	tccd	requestor: TCCDProcess: identifier=com.apple.WindowServer, pid=397, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=35241, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	20:18:09.143239-0500	tccd	AUTHREQ_SUBJECT: msgID=397.2713, subject=com.nexy.assistant,
default	20:18:09.144151-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x92f17bc00 at /Applications/Nexy.app
default	20:18:09.177130-0500	Nexy	New connection 0x8bd0b main
default	20:18:09.179636-0500	Nexy	CHECKIN: pid=35241
default	20:18:09.190963-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.27241569.27241575(501)>:35241] from originator [osservice<com.apple.coreservices.launchservicesd>:367] with description <RBSAssertionDescriptor| "uielement:35241" ID:403-367-159061 target:35241 attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"RoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	20:18:09.191072-0500	runningboardd	Assertion 403-367-159061 (target:[app<application.com.nexy.assistant.27241569.27241575(501)>:35241]) will be created as active
default	20:18:09.191519-0500	runningboardd	Invalidating assertion 403-367-159059 (target:[app<application.com.nexy.assistant.27241569.27241575(501)>:35241]) from originator [osservice<com.apple.coreservices.launchservicesd>:367]
default	20:18:09.191426-0500	Nexy	CHECKEDIN: pid=35241 asn=0x0-0x3c13c1 foreground=0
default	20:18:09.191253-0500	launchservicesd	CHECKIN:0x0-0x3c13c1 35241 com.nexy.assistant
default	20:18:09.191731-0500	Nexy	[0x863d483c0] activating connection: mach=false listener=true peer=false name=(anonymous)
default	20:18:09.191823-0500	Nexy	[0x863d483c0] Connection returned listener port: 0x4e03
default	20:18:09.191417-0500	loginwindow	-[Application updateInformation] | Got App URL: file:///Applications/Nexy.app/
default	20:18:09.191540-0500	loginwindow	-[ApplicationManager checkInAppContext:eventData:] | ApplicationManager: Checked in app : Nexy
default	20:18:09.192059-0500	Nexy	[0x862b4c300] activating connection: mach=false listener=false peer=true name=com.apple.xpc.anonymous.0x863d483c0.peer[367].0x862b4c300
default	20:18:09.194004-0500	Nexy	FRONTLOGGING: version 1
default	20:18:09.194011-0500	Nexy	Registered, pid=35241 ASN=0x0,0x3c13c1
default	20:18:09.194298-0500	WindowServer	8bd0b[CreateApplication]: Process creation: 0x0-0x3c13c1 (Nexy) connectionID: 8BD0B pid: 35241 in session 0x101
default	20:18:09.194623-0500	Nexy	[0x863d48500] activating connection: mach=true listener=false peer=false name=com.apple.lsd.mapdb
default	20:18:09.196455-0500	Nexy	[0x863d483c0] Connection returned listener port: 0x4e03
default	20:18:09.197187-0500	Nexy	BringForward: pid=35241 asn=0x0-0x3c13c1 bringForward=0 foreground=0 uiElement=1 launchedByLS=1 modifiersCount=1 allDisabled=0
default	20:18:09.197314-0500	Nexy	BringFrontModifier: pid=35241 asn=0x0-0x3c13c1 Modifier 0 hideAfter=0 hideOthers=0 dontMakeFrontmost=0 mouseDown=0/0 seed=0/0
default	20:18:09.201976-0500	Nexy	Current system appearance, (HLTB: 2), (SLS: 1)
default	20:18:09.203730-0500	Nexy	No persisted cache on this platform.
default	20:18:09.204752-0500	Nexy	Current system appearance, (HLTB: 2), (SLS: 1)
default	20:18:09.205382-0500	Nexy	Post-registration system appearance: (HLTB: 2)
default	20:18:09.207743-0500	Nexy	FBSWorkspace: endpoint monitoring is disabled.
default	20:18:09.207753-0500	Nexy	FBSWorkspace: default shell endpoint is disabled.
default	20:18:09.207823-0500	Nexy	Initializing connection
default	20:18:09.207868-0500	Nexy	Removing all cached process handles
default	20:18:09.207890-0500	Nexy	Sending handshake request attempt #1 to server
default	20:18:09.207899-0500	Nexy	Creating connection to com.apple.runningboard
default	20:18:09.207906-0500	Nexy	[0x863d48640] activating connection: mach=true listener=false peer=false name=com.apple.runningboard
default	20:18:09.208436-0500	runningboardd	Setting client for [app<application.com.nexy.assistant.27241569.27241575(501)>:35241] as ready
default	20:18:09.209105-0500	Nexy	Handshake succeeded
default	20:18:09.209120-0500	Nexy	Identity resolved as app<application.com.nexy.assistant.27241569.27241575(501)>
default	20:18:09.209625-0500	Nexy	[0x863d483c0] Connection returned listener port: 0x4e03
default	20:18:09.210684-0500	distnoted	register name: com.apple.xctest.FakeForceTouchDevice object: com.nexy.assistant token: 1e0000001d pid: 35241
default	20:18:09.217346-0500	Nexy	[0x863d483c0] Connection returned listener port: 0x4e03
default	20:18:09.221183-0500	Nexy	Created a new Process Instance Registry XPC connection (inactive)
default	20:18:09.221215-0500	Nexy	[0x863d48780] activating connection: mach=true listener=false peer=false name=com.apple.linkd.autoShortcut
default	20:18:09.221347-0500	Nexy	Activated connection to com.apple.linkd.autoShortcut (ApplicationService)
default	20:18:09.221399-0500	Nexy	[0x863d48a00] activating connection: mach=false listener=true peer=false name=(anonymous)
default	20:18:09.222587-0500	Nexy	[0x863d48a00] Connection returned listener port: 0x6603
default	20:18:09.223447-0500	Nexy	Registered process with identifier 35241-1785026
default	20:18:09.484601-0500	Nexy	Registered notify signal com.apple.caulk.alloc.rtdump (0)
default	20:18:09.487744-0500	Nexy	System_Input_Processing_Notification_Handler.mm:456   System_Input_Processing_Notification_Handler::is_vi_available(): Voice isolation DSP is available for client with bundle id com.nexy.assistant (AVFoundation is available, application is not in client deny list, application is not FaceTime variant)
default	20:18:09.489428-0500	Nexy	[0x863d48b40] activating connection: mach=true listener=false peer=false name=com.apple.cmio.registerassistantservice.system-extensions
fault	20:18:09.492001-0500	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.27241569.27241575 AUID=501> and <type=Application identifier=application.com.nexy.assistant.27241569.27241575>
default	20:18:09.496085-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOInitializeListenersForBundleID: for <private> -> <private>
default	20:18:09.497752-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> vpio_preferenceChangedListener: new value ((null)) for key AUVoiceIOClients/com-nexy-assistant/AUVoiceIOChatFlavor, translatedBundleID com.nexy.assistant, bundleIDs {(
    "com.nexy.assistant"
)}
default	20:18:09.497906-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> vpio_preferenceChangedListener: new value ((null)) for key AUVoiceIOClients/com-nexy-assistant/AUVoiceIOIsAutoChatFlavorEnabled, translatedBundleID com.nexy.assistant, bundleIDs {(
    "com.nexy.assistant"
)}
default	20:18:09.498044-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetSupportedChatFlavorsForBundleID: <private>-><private> get supported chat flavors: <private>
default	20:18:09.498053-0500	Nexy	            HALSystem.cpp:134    Enabling HAL Voice Isolation support
default	20:18:09.498081-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetHiddenChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	20:18:09.498205-0500	Nexy	[0x863d48c80] activating connection: mach=true listener=false peer=false name=com.apple.tccd
default	20:18:09.498440-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOHiddenChatFlavors newValue: (
    1
)
default	20:18:09.498799-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=35241.2, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=35241, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	20:18:09.504786-0500	tccd	AUTHREQ_SUBJECT: msgID=35241.2, subject=com.nexy.assistant,
default	20:18:09.505387-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc79244300 at /Applications/Nexy.app
default	20:18:09.529161-0500	Nexy	[0x863d48c80] invalidated after the last release of the connection object
default	20:18:09.529212-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetSupportedChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	20:18:09.531907-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOSupportedChatFlavors newValue: (
)
default	20:18:09.533091-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=411.1556, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=35241, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=398, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	20:18:09.534053-0500	tccd	AUTHREQ_SUBJECT: msgID=411.1556, subject=com.nexy.assistant,
default	20:18:09.534629-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc79244300 at /Applications/Nexy.app
error	20:18:09.560457-0500	tccd	Request message contains a target_token to accessing_process (TCCDProcess: identifier=com.nexy.assistant, pid=35241, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy) but TCCDProcess: identifier=com.apple.audio.coreaudiod, pid=411, auid=202, euid=202, binary_path=/usr/sbin/coreaudiod is not a TCC manager for service: kTCCServiceScreenCapture.
default	20:18:09.561413-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=411.1558, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=35241, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=398, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	20:18:09.562359-0500	tccd	AUTHREQ_SUBJECT: msgID=411.1558, subject=com.nexy.assistant,
default	20:18:09.562910-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc79244300 at /Applications/Nexy.app
default	20:18:09.590296-0500	Nexy	  HALPlugInManagement.cpp:440    HALPlugInManagement::RegisterPlugIns: skipping in-process plug-ins
error	20:18:09.590636-0500	Nexy	AddInstanceForFactory: No factory registered for id <CFUUID 0x862a19ca0> F8BB1C28-BAE8-11D6-9C31-00039315CD46
default	20:18:09.610114-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	20:18:09.610241-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	20:18:09.614779-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetPreferredChatFlavorForBundleID: <private>-><private> get value: 0
default	20:18:12.045461-0500	kernel	SK[6]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 70B042C2-34B5-446D-924D-0BFAC1561208 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.58342,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0x17713018 tp_proto=0x06"
default	20:18:12.045555-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:58342<-><IPv4-redacted>:53] interface: utun6 (skipped: 47531)
so_gencnt: 2919306 t_state: SYN_SENT process: Nexy:35241 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 1 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xb248538a
default	20:18:12.046226-0500	kernel	tcp connected: [<IPv4-redacted>:58342<-><IPv4-redacted>:53] interface: utun6 (skipped: 47531)
so_gencnt: 2919306 t_state: ESTABLISHED process: Nexy:35241 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 1 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xb248538a
default	20:18:12.046528-0500	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:58342<-><IPv4-redacted>:53] interface: utun6 (skipped: 47531)
so_gencnt: 2919306 t_state: FIN_WAIT_1 process: Nexy:35241 Duration: 0.001 sec Conn_Time: 0.001 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 1.000 ms rttvar: 0.500 ms base rtt: 1 ms so_error: 0 svc/tc: 0 flow: 0xb248538a
default	20:18:12.046538-0500	kernel	tcp_connection_summary [<IPv4-redacted>:58342<-><IPv4-redacted>:53] interface: utun6 (skipped: 47531)
so_gencnt: 2919306 t_state: FIN_WAIT_1 process: Nexy:35241 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	20:18:12.081674-0500	Nexy	[0x863d48c80] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioComponentRegistrar
default	20:18:12.095170-0500	Nexy	                AUHAL.cpp:420   AUHAL: (0x864e90e40) Selecting device 85 from constructor
default	20:18:12.095181-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0x864e90e40)
default	20:18:12.095190-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0x864e90e40) not already running
default	20:18:12.095194-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0x864e90e40) nothing to teardown
default	20:18:12.095197-0500	Nexy	                AUHAL.cpp:762   SelectDevice: (0x864e90e40) connecting device 85
default	20:18:12.095324-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0x864e90e40) Device ID: 85 (Input:No | Output:Yes): true
default	20:18:12.095439-0500	Nexy	                AUHAL.cpp:774   SelectDevice: (0x864e90e40) created ioproc 0xa for device 85
default	20:18:12.095530-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x864e90e40) adding 7 device listeners to device 85
default	20:18:12.095695-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x864e90e40) adding 0 device delegate listeners to device 85
default	20:18:12.095701-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x864e90e40)
default	20:18:12.095771-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  48000 Hz, Float32, interleaved
default	20:18:12.095777-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	20:18:12.095782-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	20:18:12.095789-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	20:18:12.095798-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	20:18:12.095879-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x864e90e40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	20:18:12.095887-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x864e90e40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	20:18:12.095892-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	20:18:12.095897-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x864e90e40) removing 0 device listeners from device 0
default	20:18:12.095901-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x864e90e40) removing 0 device delegate listeners from device 0
default	20:18:12.095912-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0x864e90e40)
default	20:18:12.095936-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is DISABLED
default	20:18:12.096035-0500	Nexy	                AUHAL.cpp:2303  SetProperty: (0x864e90e40) caller requesting device change from 85 to 91
default	20:18:12.096045-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0x864e90e40)
default	20:18:12.096050-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0x864e90e40) not already running
default	20:18:12.096054-0500	Nexy	                AUHAL.cpp:687   SelectDevice: (0x864e90e40) disconnecting device 85
default	20:18:12.096057-0500	Nexy	                AUHAL.cpp:751   SelectDevice: (0x864e90e40) destroying ioproc 0xa for device 85
default	20:18:12.096127-0500	Nexy	  AVAudioSession_MacOS.mm:1021  initForMacOS
default	20:18:12.096657-0500	Nexy	[0x863d48f00] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioSession
default	20:18:12.097836-0500	audiomxd	  ServerSessionManager.mm:315   { "action":"create_session", "session":{"ID":"0x1e804a","name":"Nexy(35241)"}, "details":{"PID":35241,"session_type":"Primary"} }
default	20:18:12.097927-0500	audiomxd	AudioApplicationInfoImpl.mm:250   Setting initial isRecording state: 0 for newly-created AudioApp
	app: {"name":"[implicit] Nexy","pid":35241}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1e804a, sessionType: 'prim', isRecording: false }, 
]
default	20:18:12.098798-0500	audiomxd	  ServerSessionManager.mm:1322  Start process monitoring, pid = 35241, name = Nexy
default	20:18:12.099081-0500	Nexy	    SessionCore_Create.mm:99    Created session 0x8637c5240 with ID: 0x1e804a
default	20:18:12.100493-0500	Nexy	[0x863d49040] activating connection: mach=true listener=false peer=false name=com.apple.audioanalyticsd
error	20:18:12.100984-0500	Nexy	Reporter disconnected. { function=sendMessage, reporterID=151358942478337 }
default	20:18:12.101001-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped Unknown {1C-77-54-18-C8-A3:output, 0xa}
default	20:18:12.101057-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	20:18:12.101161-0500	Nexy	                AUHAL.cpp:762   SelectDevice: (0x864e90e40) connecting device 91
default	20:18:12.101253-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0x864e90e40) Device ID: 91 (Input:Yes | Output:No): true
default	20:18:12.102979-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=411.1559, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=35241, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=398, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	20:18:12.104480-0500	tccd	AUTHREQ_SUBJECT: msgID=411.1559, subject=com.nexy.assistant,
default	20:18:12.105221-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc79244300 at /Applications/Nexy.app
default	20:18:12.143018-0500	tccd	AUTHREQ_PROMPTING: msgID=411.1559, service=kTCCServiceMicrophone, subject=Sub:{com.nexy.assistant}Resp:{TCCDProcess: identifier=com.nexy.assistant, pid=35241, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy},
default	20:18:14.163475-0500	tccd	Publishing <TCCDEvent: type=Create, service=kTCCServiceMicrophone, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 3 subscribers: {
    468 = "<TCCDEventSubscriber: token=468, state=Passed, csid=com.apple.chronod>";
    37 = "<TCCDEventSubscriber: token=37, state=Initial, csid=(null)>";
    476 = "<TCCDEventSubscriber: token=476, state=Passed, csid=com.apple.photolibraryd>";
}
default	20:18:14.163835-0500	Nexy	                AUHAL.cpp:774   SelectDevice: (0x864e90e40) created ioproc 0xa for device 91
default	20:18:14.164089-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x864e90e40) adding 7 device listeners to device 91
default	20:18:14.164352-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x864e90e40) adding 0 device delegate listeners to device 91
default	20:18:14.164366-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x864e90e40)
default	20:18:14.164381-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 output streams; not all mono
default	20:18:14.164396-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	20:18:14.164607-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  input stream 0 [0x5c]:  1 ch,  24000 Hz, Float32
default	20:18:14.164619-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 input streams; all mono
default	20:18:14.164627-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  1 ch,  24000 Hz, Float32
default	20:18:14.164750-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x864e90e40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	20:18:14.164764-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x864e90e40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	20:18:14.164772-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	20:18:14.164778-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x864e90e40) removing 7 device listeners from device 85
default	20:18:14.164989-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x864e90e40) removing 0 device delegate listeners from device 85
default	20:18:14.165002-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0x864e90e40)
default	20:18:14.165390-0500	chronod	[appAuth:com.nexy.assistant] tcc authorization(s) changed
default	20:18:14.165930-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	20:18:14.167387-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=411.1560, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=35241, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=398, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	20:18:14.169039-0500	tccd	AUTHREQ_SUBJECT: msgID=411.1560, subject=com.nexy.assistant,
default	20:18:14.170351-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc79244300 at /Applications/Nexy.app
default	20:18:14.193432-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	20:18:14.195605-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=411.1561, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=35241, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=398, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	20:18:14.196958-0500	tccd	AUTHREQ_SUBJECT: msgID=411.1561, subject=com.nexy.assistant,
default	20:18:14.198551-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc79244300 at /Applications/Nexy.app
default	20:18:14.234592-0500	Nexy	Registered notify signal com.apple.caulk.alloc.audiodump (0)
default	20:18:14.236131-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=411.1562, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=35241, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=398, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	20:18:14.237056-0500	tccd	AUTHREQ_SUBJECT: msgID=411.1562, subject=com.nexy.assistant,
default	20:18:14.237616-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc79245800 at /Applications/Nexy.app
default	20:18:14.264441-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetPreferredChatFlavorForBundleID: <private>-><private> get value: 0
default	20:18:14.264786-0500	coreaudiod	>>> NEGOTIATE [com.nexy.assistant]
default	20:18:14.264909-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetSupportedChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	20:18:14.264923-0500	coreaudiod	<<< NEGOTIATE [com.nexy.assistant]
default	20:18:14.266033-0500	coreaudiod	>>> ADAPT [com.nexy.assistant]
default	20:18:14.267349-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOSupportedChatFlavors newValue: (
    0,
    2
)
default	20:18:14.267935-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xa38710900] Created node ADM::com.nexy.assistant_10569.10484.0_airpods noise suppression studio::in-0 with nodeID 0 - reporting period = 10.000000, sample rate = 24000.000000
default	20:18:14.267997-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xa38710900] Created node ADM::com.nexy.assistant_10569.10484.0_airpods noise suppression studio::out-0 with nodeID 1 - reporting period = 10.000000, sample rate = 24000.000000
default	20:18:14.298289-0500	runningboardd	Assertion did invalidate due to timeout: 403-403-159058 (target:[app<application.com.nexy.assistant.27241569.27241575(501)>:35241])
default	20:18:14.370534-0500	coreaudiod	<<< ADAPT [com.nexy.assistant]
default	20:18:14.372075-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:10569 called from <private>
default	20:18:14.372137-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	20:18:14.372154-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Input {1C-77-54-18-C8-A3:input, 0xa}
default	20:18:14.372782-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:10569 called from <private>
default	20:18:14.373162-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(10569)
default	20:18:14.375590-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.27241569.27241575(501)>:35241] from originator [osservice<com.apple.powerd>:338] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:403-338-159073 target:35241 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	20:18:14.375668-0500	runningboardd	Assertion 403-338-159073 (target:[app<application.com.nexy.assistant.27241569.27241575(501)>:35241]) will be created as active
default	20:18:14.378326-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
fault	20:18:14.378189-0500	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.27241569.27241575 AUID=501> and <type=Application identifier=application.com.nexy.assistant.27241569.27241575>
default	20:18:14.379116-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575(501)>:35241] Ignoring jetsam update because this process is not memory-managed
default	20:18:14.379308-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575(501)>:35241] Ignoring suspend because this process is not lifecycle managed
default	20:18:14.379196-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	20:18:14.379365-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575(501)>:35241] Ignoring GPU update because this process is not GPU managed
default	20:18:14.373179-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:10569 called from <private>
default	20:18:14.379450-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575(501)>:35241] Ignoring memory limit update because this process is not memory-managed
default	20:18:14.373187-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:10569 called from <private>
default	20:18:14.374728-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(10568)
default	20:18:14.374744-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:10568 called from <private>
default	20:18:14.375073-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:10568 called from <private>
fault	20:18:14.381063-0500	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.27241569.27241575 AUID=501> and <type=Application identifier=application.com.nexy.assistant.27241569.27241575>
default	20:18:14.384707-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(10569)
default	20:18:14.384725-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(10569)
default	20:18:14.384767-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(10569)
default	20:18:14.384810-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(10569)
default	20:18:14.387538-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:10569 called from <private>
default	20:18:14.387547-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:10569 called from <private>
default	20:18:14.387563-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:10569 called from <private>
default	20:18:14.391520-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1e804a","name":"Nexy(35241)"}, "details":{"deviceUIDs":["1C-77-54-18-C8-A3:input"],"implicit_category":"Record","input_running":true,"output_running":false} }
default	20:18:14.391597-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 75, PID = 35241, Name = sid:0x1e804a, Nexy(35241), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	20:18:14.391947-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 75, PID = 35241, Name = sid:0x1e804a, Nexy(35241), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	20:18:14.387573-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:10569 called from <private>
default	20:18:14.387581-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:10569 called from <private>
default	20:18:14.387619-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:10569 called from <private>
default	20:18:14.387653-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:10569 called from <private>
default	20:18:14.392343-0500	audiomxd	UpdateAudioState CID 0x4D120001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:18:14.392257-0500	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1e804a, Nexy(35241), 'prim'', AudioCategory changed to 'Record_WithBluetooth'
default	20:18:14.392909-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 75, PID = 35241, Name = sid:0x1e804a, Nexy(35241), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	20:18:14.393208-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 75, PID = 35241, Name = sid:0x1e804a, Nexy(35241), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	20:18:14.390903-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(10569)
default	20:18:14.393237-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:10568 called from <private>
default	20:18:14.393245-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:10568 called from <private>
default	20:18:14.393383-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(10568)
default	20:18:14.393481-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:10568 called from <private>
default	20:18:14.393517-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:10568 called from <private>
default	20:18:14.394016-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(10568)
default	20:18:14.394071-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(10568)
default	20:18:14.394171-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(10568)
default	20:18:14.394237-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:10568 called from <private>
default	20:18:14.394546-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(10568)
default	20:18:14.394664-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:10568 called from <private>
default	20:18:14.394717-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:10568 called from <private>
default	20:18:14.394756-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:10568 called from <private>
default	20:18:14.394804-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:10568 called from <private>
default	20:18:14.394834-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:10568 called from <private>
default	20:18:14.393666-0500	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 75, PID = 35241, Name = sid:0x1e804a, Nexy(35241), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> is going active
default	20:18:14.394869-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:10568 called from <private>
default	20:18:14.394908-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:10568 called from <private>
default	20:18:14.394942-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:10568 called from <private>
default	20:18:14.393749-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1e804a, Nexy(35241), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 75 starting recording
default	20:18:14.394979-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:10568 called from <private>
default	20:18:14.395080-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:10568 called from <private>
default	20:18:14.395132-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:10568 called from <private>
default	20:18:14.395260-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(10568)
default	20:18:14.395320-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:10568 called from <private>
default	20:18:14.395359-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:10568 called from <private>
default	20:18:14.395677-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(10568)
default	20:18:14.394057-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 75, PID = 35241, Name = sid:0x1e804a, Nexy(35241), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	20:18:14.395360-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 75, PID = 35241, Name = sid:0x1e804a, Nexy(35241), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	20:18:14.395802-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:10568 called from <private>
default	20:18:14.395778-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [1, 0]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:input"
)}
default	20:18:14.395571-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1e804a, Nexy(35241), 'prim'', displayID:'com.nexy.assistant'}
default	20:18:14.395831-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:10568 called from <private>
default	20:18:14.395843-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	20:18:14.395895-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:10568 called from <private>
default	20:18:14.395941-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:10568 called from <private>
default	20:18:14.393796-0500	audiomxd	UpdateAudioState CID 0x4D120001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:18:14.396415-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	20:18:14.399287-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.27241569.27241575(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:18:14.392870-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=411.1563, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=35241, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=398, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	20:18:14.393049-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:18:14.396404-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:18:14.400558-0500	gamepolicyd	Received state update for 35241 (app<application.com.nexy.assistant.27241569.27241575(501)>, running-active-NotVisible
default	20:18:14.399951-0500	runningboardd	Invalidating assertion 403-338-159073 (target:[app<application.com.nexy.assistant.27241569.27241575(501)>:35241]) from originator [osservice<com.apple.powerd>:338]
default	20:18:14.403742-0500	tccd	AUTHREQ_SUBJECT: msgID=411.1563, subject=com.nexy.assistant,
default	20:18:14.408353-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc79245800 at /Applications/Nexy.app
default	20:18:14.437536-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
error	20:18:14.437871-0500	audioaccessoryd	Updating local audio category 100 -> 200 app com.nexy.assistant
default	20:18:14.436894-0500	audiomxd	UpdateAudioState CID 0x4D120001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	20:18:14.458507-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	20:18:14.458570-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	20:18:14.458597-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	20:18:14.458745-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	20:18:14.459815-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:18:14.459827-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:18:14.469949-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:10569 called from <private>
default	20:18:14.471841-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.27241569.27241575(501)>:35241] from originator [osservice<com.apple.powerd>:338] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:403-338-159074 target:35241 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	20:18:14.469965-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:10569 called from <private>
default	20:18:14.469990-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 1 1, id:10569 called from <private>
default	20:18:14.471908-0500	runningboardd	Assertion 403-338-159074 (target:[app<application.com.nexy.assistant.27241569.27241575(501)>:35241]) will be created as active
default	20:18:14.470007-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 1 2 2, id:10569 called from <private>
default	20:18:14.478233-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	20:18:14.478281-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	20:18:14.478321-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	20:18:14.478419-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	20:18:14.478547-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc79245800 at /Applications/Nexy.app
default	20:18:14.479083-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:18:14.479125-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:18:14.479157-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:18:14.479186-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:18:14.479240-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:18:14.479288-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	20:18:14.479592-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	20:18:14.498450-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575(501)>:35241] Ignoring jetsam update because this process is not memory-managed
default	20:18:14.498460-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575(501)>:35241] Ignoring suspend because this process is not lifecycle managed
default	20:18:14.498467-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575(501)>:35241] Ignoring GPU update because this process is not GPU managed
default	20:18:14.498482-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575(501)>:35241] Ignoring memory limit update because this process is not memory-managed
default	20:18:14.506035-0500	coreaudiod	>>> ADAPT [com.nexy.assistant]
default	20:18:14.508121-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xa380eb900] Created node ADM::com.nexy.assistant_10569.10484.0_airpods noise suppression studio::in-0 with nodeID 0 - reporting period = 10.000000, sample rate = 24000.000000
default	20:18:14.508183-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xa380eb900] Created node ADM::com.nexy.assistant_10569.10484.0_airpods noise suppression studio::out-0 with nodeID 1 - reporting period = 10.000000, sample rate = 24000.000000
default	20:18:14.542479-0500	coreaudiod	<<< ADAPT [com.nexy.assistant]
default	20:18:14.544162-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:10569 called from <private>
default	20:18:14.544183-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:10569 called from <private>
default	20:18:14.544574-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	20:18:14.546123-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:10569 called from <private>
default	20:18:14.546896-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.27241569.27241575(501)>:35241] from originator [osservice<com.apple.powerd>:338] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:403-338-159076 target:35241 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	20:18:14.546979-0500	runningboardd	Assertion 403-338-159076 (target:[app<application.com.nexy.assistant.27241569.27241575(501)>:35241]) will be created as active
default	20:18:14.546132-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:10569 called from <private>
default	20:18:14.547466-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575(501)>:35241] Ignoring jetsam update because this process is not memory-managed
default	20:18:14.547524-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	20:18:14.547574-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575(501)>:35241] Ignoring suspend because this process is not lifecycle managed
default	20:18:14.547641-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575(501)>:35241] Ignoring GPU update because this process is not GPU managed
default	20:18:14.546209-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:10569 called from <private>
default	20:18:14.546238-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:10569 called from <private>
default	20:18:14.547775-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575(501)>:35241] Ignoring memory limit update because this process is not memory-managed
default	20:18:14.546245-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:10569 called from <private>
default	20:18:14.547939-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	20:18:14.546453-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(10569)
default	20:18:14.546660-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:10569 called from <private>
default	20:18:14.546710-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:10569 called from <private>
default	20:18:14.548605-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(10569)
default	20:18:14.548887-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:10569 called from <private>
default	20:18:14.548893-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:10569 called from <private>
default	20:18:14.548907-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:10569 called from <private>
default	20:18:14.550992-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=411.1565, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=35241, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=398, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	20:18:14.553533-0500	tccd	AUTHREQ_SUBJECT: msgID=411.1565, subject=com.nexy.assistant,
default	20:18:14.554800-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc79245800 at /Applications/Nexy.app
default	20:18:14.556250-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.27241569.27241575(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:18:14.556560-0500	runningboardd	Invalidating assertion 403-338-159076 (target:[app<application.com.nexy.assistant.27241569.27241575(501)>:35241]) from originator [osservice<com.apple.powerd>:338]
default	20:18:14.557069-0500	gamepolicyd	Received state update for 35241 (app<application.com.nexy.assistant.27241569.27241575(501)>, running-active-NotVisible
default	20:18:14.590490-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:10569 called from <private>
default	20:18:14.592931-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.27241569.27241575(501)>:35241] from originator [osservice<com.apple.powerd>:338] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:403-338-159077 target:35241 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	20:18:14.593007-0500	runningboardd	Assertion 403-338-159077 (target:[app<application.com.nexy.assistant.27241569.27241575(501)>:35241]) will be created as active
default	20:18:14.600089-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	20:18:14.600171-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	20:18:14.600244-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	20:18:14.601294-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:18:14.601346-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:18:14.601376-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:18:14.601402-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:18:14.601443-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:18:14.601510-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	20:18:14.601577-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:18:14.601588-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:18:14.601613-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:18:14.601653-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:18:14.601723-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:18:14.601732-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	20:18:14.601852-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	20:18:14.602190-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:18:14.602199-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:18:14.602207-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:18:14.602240-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:18:14.602274-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:18:14.602296-0500	ControlCenter	Navigating to new application [com.nexy.assistant]
default	20:18:14.602297-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	20:18:15.036221-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.nexy.assistant, Score 200, Remote 100 NumofApp 1
default	20:18:15.617938-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xa}
default	20:18:15.618489-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1e804a","name":"Nexy(35241)"}, "details":{"deviceUIDs":[],"implicit_category":"","input_running":false,"output_running":false} }
default	20:18:15.618726-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 75, PID = 35241, Name = sid:0x1e804a, Nexy(35241), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	20:18:15.618854-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 75, PID = 35241, Name = sid:0x1e804a, Nexy(35241), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	20:18:15.618922-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1e804a, Nexy(35241), 'prim'', displayID:'com.nexy.assistant'}
default	20:18:15.619040-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1e804a, Nexy(35241), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 75 stopping recording
default	20:18:15.619035-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	20:18:15.619105-0500	audiomxd	-MXCoreSession- -[MXCoreSession endInterruption:]: Session <ID: 75, PID = 35241, Name = sid:0x1e804a, Nexy(35241), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> is going inactive
default	20:18:15.619214-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 75, PID = 35241, Name = sid:0x1e804a, Nexy(35241), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	20:18:15.619357-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 75, PID = 35241, Name = sid:0x1e804a, Nexy(35241), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	20:18:15.619591-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 200 flag 0x1 < Hijack > app com.nexy.assistant CID 0x4D120001 category Not set
default	20:18:15.619647-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 0]. BT device UIDS: {(
)}
default	20:18:15.619668-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	20:18:15.620315-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	20:18:15.620377-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	20:18:15.620035-0500	audiomxd	UpdateAudioState CID 0x4D120001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	20:18:15.620412-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	20:18:15.620223-0500	audiomxd	UpdateAudioState CID 0x4D120001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:18:15.620532-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:18:15.620579-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	20:18:15.620609-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:18:15.620660-0500	audioaccessoryd	AudioStateChanged: Removed audio session app com.nexy.assistant 201 count 0
default	20:18:15.624778-0500	runningboardd	Invalidating assertion 403-338-159077 (target:[app<application.com.nexy.assistant.27241569.27241575(501)>:35241]) from originator [osservice<com.apple.powerd>:338]
default	20:18:15.625937-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	20:18:15.628554-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:18:15.628567-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:18:15.628582-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:18:15.628591-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:18:15.628598-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:18:15.628607-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	20:18:15.628730-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	20:18:15.719423-0500	Nexy	                AUHAL.cpp:473   ~AUHAL: (0x864e90e40) Selecting device 0 from destructor
default	20:18:15.719454-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0x864e90e40)
default	20:18:15.719469-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0x864e90e40) not already running
default	20:18:15.719480-0500	Nexy	                AUHAL.cpp:687   SelectDevice: (0x864e90e40) disconnecting device 91
default	20:18:15.719496-0500	Nexy	                AUHAL.cpp:751   SelectDevice: (0x864e90e40) destroying ioproc 0xa for device 91
default	20:18:15.719552-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xa}
default	20:18:15.719623-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	20:18:15.719954-0500	Nexy	                AUHAL.cpp:853   SelectDevice: (0x864e90e40) nothing to setup
default	20:18:15.719984-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x864e90e40) adding 0 device listeners to device 0
default	20:18:15.720000-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x864e90e40) adding 0 device delegate listeners to device 0
default	20:18:15.720015-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x864e90e40) removing 7 device listeners from device 91
default	20:18:15.720503-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x864e90e40) removing 0 device delegate listeners from device 91
default	20:18:15.720536-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0x864e90e40)
default	20:18:15.731671-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575(501)>:35241] Ignoring jetsam update because this process is not memory-managed
default	20:18:15.731702-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575(501)>:35241] Ignoring suspend because this process is not lifecycle managed
default	20:18:15.731718-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575(501)>:35241] Ignoring GPU update because this process is not GPU managed
default	20:18:15.731745-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575(501)>:35241] Ignoring memory limit update because this process is not memory-managed
default	20:18:15.735596-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.27241569.27241575(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:18:15.736366-0500	gamepolicyd	Received state update for 35241 (app<application.com.nexy.assistant.27241569.27241575(501)>, running-active-NotVisible
default	20:18:15.913510-0500	Nexy	[0x863d49400] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	20:18:15.914228-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=35241.3, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=35241, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	20:18:15.915468-0500	tccd	AUTHREQ_SUBJECT: msgID=35241.3, subject=com.nexy.assistant,
default	20:18:15.916146-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x92f17a700 at /Applications/Nexy.app
default	20:18:15.947344-0500	Nexy	[0x863d49400] invalidated after the last release of the connection object
default	20:18:15.949634-0500	Nexy	[0x863d49400] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	20:18:15.950244-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=35241.4, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=35241, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	20:18:15.951358-0500	tccd	AUTHREQ_SUBJECT: msgID=35241.4, subject=com.nexy.assistant,
default	20:18:15.952105-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x92f17b900 at /Applications/Nexy.app
default	20:18:15.987088-0500	tccd	Notifying for access  kTCCServiceListenEvent for target PID[35241], responsiblePID[35241], responsiblePath: /Applications/Nexy.app to UID: 501
default	20:18:15.987397-0500	Nexy	[0x863d49400] invalidated after the last release of the connection object
default	20:18:16.127517-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x92f17a400 at /Applications/Nexy.app
default	20:18:16.164479-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x92f178000 at /Applications/Nexy.app
default	20:18:16.165185-0500	nehelper	Received an apps uninstalled notification with bundle IDs (
    "com.nexy.assistant"
)
default	20:18:16.170066-0500	tccd	Publishing <TCCDEvent: type=Modify, service=kTCCServiceListenEvent, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 0 subscribers: {
}
default	20:18:16.764399-0500	nehelper	Removing UUIDs for (
    "com.nexy.assistant"
)
default	20:18:16.772375-0500	nehelper	Handling an apps uninstalled notification with bundle IDs (
    "com.nexy.assistant"
)
default	20:18:16.792558-0500	nehelper	com.apple.preferences.networkprivacy-F67B3EA9-90A6-470B-B321-9BBD719C692B: Populating the cache with 2 UUID(s) for com.nexy.assistant
default	20:18:17.871470-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:10569 called from <private>
default	20:18:17.887903-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:10568 called from <private>
default	20:18:17.887938-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:10568 called from <private>
default	20:18:19.095071-0500	Nexy	NotifyToken::RegisterDispatch(user.uid.501.com.apple.LaunchServices.database) fired for session key <private>
error	20:18:19.409991-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CAIIugCI3D6x0jkL7BXjcYRl0vPhkk-L5K9mxvc/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:194 loadAuthorizationStates(for:) new entry: kTCCServiceListenEvent com.nexy.assistant none
error	20:18:19.417802-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CAIIugCI3D6x0jkL7BXjcYRl0vPhkk-L5K9mxvc/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:194 loadAuthorizationStates(for:) new entry: kTCCServiceListenEvent com.nexy.assistant none
error	20:18:19.459180-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CAIIugCI3D6x0jkL7BXjcYRl0vPhkk-L5K9mxvc/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:194 loadAuthorizationStates(for:) new entry: kTCCServiceAppleEvents com.nexy.assistant full
error	20:18:19.460786-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CAIIugCI3D6x0jkL7BXjcYRl0vPhkk-L5K9mxvc/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:194 loadAuthorizationStates(for:) new entry: kTCCServiceAppleEvents com.nexy.assistant full
error	20:18:19.461544-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CAIIugCI3D6x0jkL7BXjcYRl0vPhkk-L5K9mxvc/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:194 loadAuthorizationStates(for:) new entry: kTCCServiceMicrophone com.nexy.assistant full
error	20:18:19.462595-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CAIIugCI3D6x0jkL7BXjcYRl0vPhkk-L5K9mxvc/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:194 loadAuthorizationStates(for:) new entry: kTCCServiceMicrophone com.nexy.assistant full
default	20:18:20.242712-0500	nehelper	Received an apps uninstalled notification with bundle IDs (
    "com.nexy.assistant"
)
default	20:18:20.558536-0500	Nexy	LSExceptions shared instance invalidated for timeout.
default	20:18:21.832182-0500	nehelper	Removing UUIDs for (
    "com.nexy.assistant"
)
default	20:18:21.926937-0500	nehelper	Handling an apps uninstalled notification with bundle IDs (
    "com.nexy.assistant"
)
default	20:18:23.359133-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x92f178300 at /Applications/Nexy.app
default	20:18:23.379152-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x92f179200 at /Applications/Nexy.app
default	20:18:23.388340-0500	tccd	Publishing <TCCDEvent: type=Modify, service=kTCCServiceListenEvent, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 0 subscribers: {
}
error	20:18:23.530965-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CAIIugCI3D6x0jkL7BXjcYRl0vPhkk-L5K9mxvc/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:194 loadAuthorizationStates(for:) new entry: kTCCServiceListenEvent com.nexy.assistant full
error	20:18:23.533600-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CAIIugCI3D6x0jkL7BXjcYRl0vPhkk-L5K9mxvc/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:194 loadAuthorizationStates(for:) new entry: kTCCServiceListenEvent com.nexy.assistant full
error	20:18:23.549119-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CAIIugCI3D6x0jkL7BXjcYRl0vPhkk-L5K9mxvc/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:194 loadAuthorizationStates(for:) new entry: kTCCServiceAppleEvents com.nexy.assistant full
error	20:18:23.549998-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CAIIugCI3D6x0jkL7BXjcYRl0vPhkk-L5K9mxvc/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:194 loadAuthorizationStates(for:) new entry: kTCCServiceMicrophone com.nexy.assistant full
error	20:18:23.550097-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CAIIugCI3D6x0jkL7BXjcYRl0vPhkk-L5K9mxvc/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:194 loadAuthorizationStates(for:) new entry: kTCCServiceAppleEvents com.nexy.assistant full
error	20:18:23.551122-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CAIIugCI3D6x0jkL7BXjcYRl0vPhkk-L5K9mxvc/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:194 loadAuthorizationStates(for:) new entry: kTCCServiceMicrophone com.nexy.assistant full
default	20:18:28.996886-0500	Nexy	                AUHAL.cpp:420   AUHAL: (0x864e91540) Selecting device 85 from constructor
default	20:18:28.996934-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0x864e91540)
default	20:18:28.996954-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0x864e91540) not already running
default	20:18:28.996968-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0x864e91540) nothing to teardown
default	20:18:28.996978-0500	Nexy	                AUHAL.cpp:762   SelectDevice: (0x864e91540) connecting device 85
default	20:18:28.997243-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0x864e91540) Device ID: 85 (Input:No | Output:Yes): true
default	20:18:28.997575-0500	Nexy	                AUHAL.cpp:774   SelectDevice: (0x864e91540) created ioproc 0xb for device 85
default	20:18:28.997921-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x864e91540) adding 7 device listeners to device 85
default	20:18:28.998435-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x864e91540) adding 0 device delegate listeners to device 85
default	20:18:28.998465-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x864e91540)
default	20:18:28.998687-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  48000 Hz, Float32, interleaved
default	20:18:28.998712-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	20:18:28.998728-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	20:18:28.998760-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	20:18:28.998788-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	20:18:28.999052-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x864e91540) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	20:18:28.999084-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x864e91540) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	20:18:28.999100-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	20:18:28.999114-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x864e91540) removing 0 device listeners from device 0
default	20:18:28.999125-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x864e91540) removing 0 device delegate listeners from device 0
default	20:18:28.999136-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0x864e91540)
default	20:18:28.999169-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is DISABLED
default	20:18:28.999311-0500	Nexy	                AUHAL.cpp:2303  SetProperty: (0x864e91540) caller requesting device change from 85 to 91
default	20:18:28.999324-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0x864e91540)
default	20:18:28.999330-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0x864e91540) not already running
default	20:18:28.999336-0500	Nexy	                AUHAL.cpp:687   SelectDevice: (0x864e91540) disconnecting device 85
default	20:18:28.999342-0500	Nexy	                AUHAL.cpp:751   SelectDevice: (0x864e91540) destroying ioproc 0xb for device 85
default	20:18:28.999376-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped Unknown {1C-77-54-18-C8-A3:output, 0xb}
default	20:18:28.999428-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	20:18:29.999543-0500	Nexy	                AUHAL.cpp:762   SelectDevice: (0x864e91540) connecting device 91
default	20:18:29.999666-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0x864e91540) Device ID: 91 (Input:Yes | Output:No): true
default	20:18:29.002096-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=411.1566, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=35241, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=398, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	20:18:29.003977-0500	tccd	AUTHREQ_SUBJECT: msgID=411.1566, subject=com.nexy.assistant,
default	20:18:29.005064-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc79244000 at /Applications/Nexy.app
default	20:18:29.029206-0500	Nexy	                AUHAL.cpp:774   SelectDevice: (0x864e91540) created ioproc 0xb for device 91
default	20:18:29.029412-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x864e91540) adding 7 device listeners to device 91
default	20:18:29.029604-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x864e91540) adding 0 device delegate listeners to device 91
default	20:18:29.029617-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x864e91540)
default	20:18:29.029628-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 output streams; not all mono
default	20:18:29.029640-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	20:18:29.029846-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  input stream 0 [0x5c]:  1 ch,  24000 Hz, Float32
default	20:18:29.029856-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 input streams; all mono
default	20:18:29.029863-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  1 ch,  24000 Hz, Float32
default	20:18:29.029977-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x864e91540) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	20:18:29.029994-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x864e91540) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	20:18:29.030000-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	20:18:29.030005-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x864e91540) removing 7 device listeners from device 85
default	20:18:29.030200-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x864e91540) removing 0 device delegate listeners from device 85
default	20:18:29.030209-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0x864e91540)
default	20:18:29.030891-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	20:18:29.032205-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=411.1567, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=35241, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=398, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	20:18:29.033322-0500	tccd	AUTHREQ_SUBJECT: msgID=411.1567, subject=com.nexy.assistant,
default	20:18:29.033972-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc79244000 at /Applications/Nexy.app
default	20:18:29.050623-0500	Nexy	       ACv2Workarounds.mm:51    com.nexy.assistant: fix84702776_86723525_86479548_89800354_SinglePacketDesc: false
default	20:18:29.051702-0500	Nexy	       AudioConverter.cpp:1044  Created a new in process converter -> 0x86506e700, from  1 ch,  24000 Hz, Float32 to  1 ch,  16000 Hz, Float32
default	20:18:29.051903-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	20:18:29.052905-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=411.1568, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=35241, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=398, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	20:18:29.053823-0500	tccd	AUTHREQ_SUBJECT: msgID=411.1568, subject=com.nexy.assistant,
default	20:18:29.054414-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc79244000 at /Applications/Nexy.app
default	20:18:29.072043-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=411.1569, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=35241, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=398, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	20:18:29.072911-0500	tccd	AUTHREQ_SUBJECT: msgID=411.1569, subject=com.nexy.assistant,
default	20:18:29.073493-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc79244000 at /Applications/Nexy.app
default	20:18:29.090367-0500	coreaudiod	>>> NEGOTIATE [com.nexy.assistant]
default	20:18:29.090555-0500	coreaudiod	<<< NEGOTIATE [com.nexy.assistant]
default	20:18:29.092533-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:10569 called from <private>
default	20:18:29.092540-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Input {1C-77-54-18-C8-A3:input, 0xb}
default	20:18:29.092586-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	20:18:29.093426-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:10569 called from <private>
default	20:18:29.097338-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	20:18:29.093606-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(10569)
default	20:18:29.093631-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:10569 called from <private>
default	20:18:29.093638-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:10569 called from <private>
default	20:18:29.095969-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(10568)
default	20:18:29.096606-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:10568 called from <private>
default	20:18:29.096647-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:10568 called from <private>
default	20:18:29.099761-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.27241569.27241575(501)>:35241] from originator [osservice<com.apple.powerd>:338] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:403-338-159200 target:35241 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	20:18:29.099869-0500	runningboardd	Assertion 403-338-159200 (target:[app<application.com.nexy.assistant.27241569.27241575(501)>:35241]) will be created as active
default	20:18:29.099725-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	20:18:29.101421-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575(501)>:35241] Ignoring jetsam update because this process is not memory-managed
default	20:18:29.101583-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575(501)>:35241] Ignoring suspend because this process is not lifecycle managed
default	20:18:29.101733-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575(501)>:35241] Ignoring GPU update because this process is not GPU managed
default	20:18:29.102175-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575(501)>:35241] Ignoring memory limit update because this process is not memory-managed
default	20:18:29.104562-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(10569)
default	20:18:29.104615-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(10569)
default	20:18:29.104628-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(10569)
default	20:18:29.104666-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(10569)
default	20:18:29.105343-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:10569 called from <private>
default	20:18:29.105355-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:10569 called from <private>
default	20:18:29.105375-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:10569 called from <private>
default	20:18:29.107218-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1e804a","name":"Nexy(35241)"}, "details":{"deviceUIDs":["1C-77-54-18-C8-A3:input"],"implicit_category":"Record","input_running":true,"output_running":false} }
default	20:18:29.107321-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 75, PID = 35241, Name = sid:0x1e804a, Nexy(35241), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	20:18:29.107417-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Category/Mode changed -- The score for sid:0x1e804a, Nexy(35241), 'prim'/com.nexy.assistant was not correct. Old score = 201
default	20:18:29.107479-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 75, PID = 35241, Name = sid:0x1e804a, Nexy(35241), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	20:18:29.107903-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:18:29.107697-0500	audiomxd	UpdateAudioState CID 0x4D120001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:18:29.107750-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 75, PID = 35241, Name = sid:0x1e804a, Nexy(35241), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	20:18:29.107881-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 75, PID = 35241, Name = sid:0x1e804a, Nexy(35241), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	20:18:29.108148-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=411.1570, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=35241, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=398, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	20:18:29.108103-0500	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 75, PID = 35241, Name = sid:0x1e804a, Nexy(35241), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> is going active
default	20:18:29.108138-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1e804a, Nexy(35241), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 75 starting recording
default	20:18:29.108467-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 75, PID = 35241, Name = sid:0x1e804a, Nexy(35241), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	20:18:29.108563-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 75, PID = 35241, Name = sid:0x1e804a, Nexy(35241), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	20:18:29.108787-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [1, 0]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:input"
)}
default	20:18:29.108634-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1e804a, Nexy(35241), 'prim'', displayID:'com.nexy.assistant'}
default	20:18:29.108800-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	20:18:29.107609-0500	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1e804a, Nexy(35241), 'prim'', AudioCategory changed to 'Record_WithBluetooth'
default	20:18:29.108812-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	20:18:29.109867-0500	tccd	AUTHREQ_SUBJECT: msgID=411.1570, subject=com.nexy.assistant,
default	20:18:29.115418-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc79244000 at /Applications/Nexy.app
default	20:18:29.118088-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:10568 called from <private>
default	20:18:29.118104-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:10568 called from <private>
default	20:18:29.119442-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.27241569.27241575(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:18:29.120090-0500	runningboardd	Invalidating assertion 403-338-159200 (target:[app<application.com.nexy.assistant.27241569.27241575(501)>:35241]) from originator [osservice<com.apple.powerd>:338]
default	20:18:29.120678-0500	gamepolicyd	Received state update for 35241 (app<application.com.nexy.assistant.27241569.27241575(501)>, running-active-NotVisible
default	20:18:29.121643-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	20:18:29.121759-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	20:18:29.121822-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	20:18:29.121957-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	20:18:29.123773-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(10569)
default	20:18:29.124176-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(10568)
default	20:18:29.124627-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:18:29.124690-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:18:29.124784-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:18:29.125341-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:18:29.127305-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:18:29.127377-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	20:18:29.129189-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	20:18:29.138808-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:10568 called from <private>
default	20:18:29.138819-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:10568 called from <private>
default	20:18:29.138906-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(10568)
default	20:18:29.152004-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:10568 called from <private>
default	20:18:29.154392-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 200 flag 0x1 < Hijack > app com.nexy.assistant CID 0x4D120001 category Not set
default	20:18:29.152107-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:10568 called from <private>
default	20:18:29.152241-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:10568 called from <private>
default	20:18:29.152338-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:10568 called from <private>
default	20:18:29.152662-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:10568 called from <private>
error	20:18:29.177659-0500	Nexy	         HALC_ProxyIOContext.cpp:1075  HALC_ProxyIOContext::_StartIO(): Start failed - StartAndWaitForState returned error 35
default	20:18:29.177669-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:10569 called from <private>
default	20:18:29.177686-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:10569 called from <private>
default	20:18:29.178539-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.27241569.27241575(501)>:35241] from originator [osservice<com.apple.powerd>:338] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:403-338-159201 target:35241 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	20:18:29.177695-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:10569 called from <private>
default	20:18:29.178731-0500	runningboardd	Assertion 403-338-159201 (target:[app<application.com.nexy.assistant.27241569.27241575(501)>:35241]) will be created as active
default	20:18:29.179425-0500	runningboardd	Invalidating assertion 403-338-159201 (target:[app<application.com.nexy.assistant.27241569.27241575(501)>:35241]) from originator [osservice<com.apple.powerd>:338]
default	20:18:29.183321-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc79244000 at /Applications/Nexy.app
default	20:18:29.183516-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	20:18:29.183633-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	20:18:29.183700-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	20:18:29.183986-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	20:18:29.184241-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:18:29.184254-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:18:29.184269-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:18:29.184293-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:18:29.184319-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:18:29.184329-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	20:18:29.184566-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	20:18:29.213795-0500	coreaudiod	>>> ADAPT [com.nexy.assistant]
default	20:18:29.215724-0500	coreaudiod	IssueReporting.cpp:492   RTAID [ use_case=Generic report_type=RMS Generic Chain clientID=ADM node=ADM::com.nexy.assistant_10569.10484.0_airpods noise suppression studio::out-0 issue_detected_sample_time=24480.000000 ] -- [ rms:[-39.345005], peaks:[-21.973515] ]
default	20:18:29.215740-0500	coreaudiod	IssueReporting.cpp:492   RTAID [ use_case=Generic report_type=RMS Generic Chain clientID=ADM node=ADM::com.nexy.assistant_10569.10484.0_airpods noise suppression studio::in-0 issue_detected_sample_time=0.000000 ] -- [ rms:[-36.902515], peaks:[-20.420866] ]
default	20:18:29.216037-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xa380eb900] Created node ADM::com.nexy.assistant_10569.10484.0_airpods noise suppression studio::in-0 with nodeID 0 - reporting period = 10.000000, sample rate = 24000.000000
default	20:18:29.216098-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xa380eb900] Created node ADM::com.nexy.assistant_10569.10484.0_airpods noise suppression studio::out-0 with nodeID 1 - reporting period = 10.000000, sample rate = 24000.000000
default	20:18:29.225347-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575(501)>:35241] Ignoring jetsam update because this process is not memory-managed
default	20:18:29.225367-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575(501)>:35241] Ignoring suspend because this process is not lifecycle managed
default	20:18:29.225383-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575(501)>:35241] Ignoring GPU update because this process is not GPU managed
default	20:18:29.225414-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575(501)>:35241] Ignoring memory limit update because this process is not memory-managed
default	20:18:29.228359-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.27241569.27241575(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:18:29.228915-0500	gamepolicyd	Received state update for 35241 (app<application.com.nexy.assistant.27241569.27241575(501)>, running-active-NotVisible
default	20:18:29.254345-0500	coreaudiod	<<< ADAPT [com.nexy.assistant]
default	20:18:29.256809-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:10569 called from <private>
default	20:18:29.256841-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:10569 called from <private>
default	20:18:29.257045-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	20:18:29.259061-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:10569 called from <private>
default	20:18:29.259186-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(10569)
default	20:18:29.259203-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:10569 called from <private>
default	20:18:29.259732-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.27241569.27241575(501)>:35241] from originator [osservice<com.apple.powerd>:338] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:403-338-159203 target:35241 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	20:18:29.259210-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:10569 called from <private>
default	20:18:29.259833-0500	runningboardd	Assertion 403-338-159203 (target:[app<application.com.nexy.assistant.27241569.27241575(501)>:35241]) will be created as active
default	20:18:29.260117-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	20:18:29.260205-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575(501)>:35241] Ignoring jetsam update because this process is not memory-managed
default	20:18:29.260222-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575(501)>:35241] Ignoring suspend because this process is not lifecycle managed
default	20:18:29.260237-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575(501)>:35241] Ignoring GPU update because this process is not GPU managed
default	20:18:29.260273-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575(501)>:35241] Ignoring memory limit update because this process is not memory-managed
default	20:18:29.260293-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	20:18:29.260850-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(10569)
default	20:18:29.261117-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:10569 called from <private>
default	20:18:29.261126-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:10569 called from <private>
default	20:18:29.261141-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:10569 called from <private>
default	20:18:29.262489-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=411.1572, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=35241, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=398, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	20:18:29.264018-0500	tccd	AUTHREQ_SUBJECT: msgID=411.1572, subject=com.nexy.assistant,
default	20:18:29.264658-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc79244000 at /Applications/Nexy.app
default	20:18:29.266283-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.27241569.27241575(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:18:29.266578-0500	runningboardd	Invalidating assertion 403-338-159203 (target:[app<application.com.nexy.assistant.27241569.27241575(501)>:35241]) from originator [osservice<com.apple.powerd>:338]
default	20:18:29.266680-0500	gamepolicyd	Received state update for 35241 (app<application.com.nexy.assistant.27241569.27241575(501)>, running-active-NotVisible
default	20:18:29.267122-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	20:18:29.267168-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	20:18:29.267206-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	20:18:29.267301-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	20:18:29.267889-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:18:29.267968-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:18:29.268007-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:18:29.268029-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:18:29.268100-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:18:29.268109-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	20:18:29.268230-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	20:18:29.297188-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:10569 called from <private>
default	20:18:29.298826-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.27241569.27241575(501)>:35241] from originator [osservice<com.apple.powerd>:338] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:403-338-159204 target:35241 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	20:18:29.298903-0500	runningboardd	Assertion 403-338-159204 (target:[app<application.com.nexy.assistant.27241569.27241575(501)>:35241]) will be created as active
default	20:18:29.303582-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	20:18:29.303630-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	20:18:29.303667-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	20:18:29.304347-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:18:29.304357-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:18:29.304378-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:18:29.304393-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:18:29.304426-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:18:29.304459-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	20:18:29.304486-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:18:29.304511-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:18:29.304543-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:18:29.304569-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:18:29.304578-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:18:29.304585-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	20:18:29.304733-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	20:18:29.305010-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:18:29.305041-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:18:29.305049-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:18:29.305075-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:18:29.305095-0500	ControlCenter	Navigating to new application [com.nexy.assistant]
default	20:18:29.305108-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:18:29.305139-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	20:18:30.036387-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.nexy.assistant, Score 200, Remote 100 NumofApp 1
default	20:18:33.035819-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.nexy.assistant, Score 200, Remote 100 NumofApp 1
default	20:18:36.036211-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.nexy.assistant, Score 200, Remote 100 NumofApp 1
default	20:18:39.028969-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.nexy.assistant, Score 200, Remote 100 NumofApp 1
default	20:18:39.297550-0500	coreaudiod	IssueReporting.cpp:492   RTAID [ use_case=Generic report_type=RMS Generic Chain clientID=ADM node=ADM::com.nexy.assistant_10569.10484.0_airpods noise suppression studio::in-0 issue_detected_sample_time=0.000000 ] -- [ rms:[-39.138866], peaks:[-8.460249] ]
default	20:18:39.300579-0500	coreaudiod	IssueReporting.cpp:492   RTAID [ use_case=Generic report_type=RMS Generic Chain clientID=ADM node=ADM::com.nexy.assistant_10569.10484.0_airpods noise suppression studio::out-0 issue_detected_sample_time=240000.000000 ] -- [ rms:[-41.082024], peaks:[-13.150961] ]
default	20:18:42.031019-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.nexy.assistant, Score 200, Remote 100 NumofApp 1
default	20:18:42.120795-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xb}
default	20:18:42.121390-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1e804a","name":"Nexy(35241)"}, "details":{"deviceUIDs":[],"implicit_category":"","input_running":false,"output_running":false} }
default	20:18:42.121628-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 75, PID = 35241, Name = sid:0x1e804a, Nexy(35241), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	20:18:42.121773-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 75, PID = 35241, Name = sid:0x1e804a, Nexy(35241), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	20:18:42.121857-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1e804a, Nexy(35241), 'prim'', displayID:'com.nexy.assistant'}
default	20:18:42.121969-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	20:18:42.121989-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1e804a, Nexy(35241), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 75 stopping recording
default	20:18:42.122056-0500	audiomxd	-MXCoreSession- -[MXCoreSession endInterruption:]: Session <ID: 75, PID = 35241, Name = sid:0x1e804a, Nexy(35241), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> is going inactive
default	20:18:42.122123-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 75, PID = 35241, Name = sid:0x1e804a, Nexy(35241), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	20:18:42.122199-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 75, PID = 35241, Name = sid:0x1e804a, Nexy(35241), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	20:18:42.122412-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 0]. BT device UIDS: {(
)}
default	20:18:42.122462-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 200 flag 0x1 < Hijack > app com.nexy.assistant CID 0x4D120001 category Not set
default	20:18:42.122438-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	20:18:42.122946-0500	audiomxd	UpdateAudioState CID 0x4D120001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	20:18:42.123038-0500	audiomxd	UpdateAudioState CID 0x4D120001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:18:42.123135-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	20:18:42.123203-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	20:18:42.123239-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:18:42.123286-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	20:18:42.123419-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	20:18:42.123449-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:18:42.123472-0500	audioaccessoryd	AudioStateChanged: Removed audio session app com.nexy.assistant 201 count 0
default	20:18:42.126329-0500	runningboardd	Invalidating assertion 403-338-159204 (target:[app<application.com.nexy.assistant.27241569.27241575(501)>:35241]) from originator [osservice<com.apple.powerd>:338]
default	20:18:42.128314-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	20:18:42.131092-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:18:42.131104-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:18:42.131119-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:18:42.131125-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:18:42.131133-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:18:42.131138-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	20:18:42.131238-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	20:18:42.223105-0500	Nexy	                AUHAL.cpp:473   ~AUHAL: (0x864e91540) Selecting device 0 from destructor
default	20:18:42.223126-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0x864e91540)
default	20:18:42.223136-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0x864e91540) not already running
default	20:18:42.223144-0500	Nexy	                AUHAL.cpp:687   SelectDevice: (0x864e91540) disconnecting device 91
default	20:18:42.223155-0500	Nexy	                AUHAL.cpp:751   SelectDevice: (0x864e91540) destroying ioproc 0xb for device 91
default	20:18:42.223197-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xb}
default	20:18:42.223249-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	20:18:42.223484-0500	Nexy	                AUHAL.cpp:853   SelectDevice: (0x864e91540) nothing to setup
default	20:18:42.223503-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x864e91540) adding 0 device listeners to device 0
default	20:18:42.223512-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x864e91540) adding 0 device delegate listeners to device 0
default	20:18:42.223520-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x864e91540) removing 7 device listeners from device 91
default	20:18:42.223789-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x864e91540) removing 0 device delegate listeners from device 91
default	20:18:42.223805-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0x864e91540)
default	20:18:42.227006-0500	Nexy	[0x863d49540] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	20:18:42.228553-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=35241.5, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=35241, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	20:18:42.230488-0500	tccd	AUTHREQ_SUBJECT: msgID=35241.5, subject=com.nexy.assistant,
default	20:18:42.231534-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x92f17a700 at /Applications/Nexy.app
default	20:18:42.232352-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575(501)>:35241] Ignoring jetsam update because this process is not memory-managed
default	20:18:42.232368-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575(501)>:35241] Ignoring suspend because this process is not lifecycle managed
default	20:18:42.232381-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575(501)>:35241] Ignoring GPU update because this process is not GPU managed
default	20:18:42.232400-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575(501)>:35241] Ignoring memory limit update because this process is not memory-managed
default	20:18:42.235507-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.27241569.27241575(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:18:42.236144-0500	gamepolicyd	Received state update for 35241 (app<application.com.nexy.assistant.27241569.27241575(501)>, running-active-NotVisible
default	20:18:42.253089-0500	tccd	Notifying for access  kTCCServiceScreenCapture for target PID[35241], responsiblePID[35241], responsiblePath: /Applications/Nexy.app to UID: 501
default	20:18:42.253529-0500	Nexy	[0x863d49540] invalidated after the last release of the connection object
default	20:18:42.304452-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x92f178300 at /Applications/Nexy.app
default	20:18:42.343024-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x92f179200 at /Applications/Nexy.app
default	20:18:42.347362-0500	tccd	Publishing <TCCDEvent: type=Modify, service=kTCCServiceScreenCapture, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 0 subscribers: {
}
default	20:18:44.346630-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(10568)
default	20:18:44.346689-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:10568 called from <private>
default	20:18:44.346709-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:10568 called from <private>
default	20:18:44.347520-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(10569)
default	20:18:44.347543-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:10569 called from <private>
default	20:18:44.347552-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:10569 called from <private>
default	20:18:44.365828-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:10568 called from <private>
default	20:18:44.365853-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:10568 called from <private>
default	20:18:44.366653-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(10568)
default	20:18:44.366682-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:10568 called from <private>
default	20:18:44.366691-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:10568 called from <private>
default	20:18:44.369436-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(10568)
default	20:18:44.370026-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:10568 called from <private>
default	20:18:44.370039-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:10568 called from <private>
default	20:18:44.395664-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 4 4 id:10568 called from <private>
default	20:18:44.395759-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 3 3 id:10568 called from <private>
default	20:18:44.395785-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(10568)
default	20:18:44.398001-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(10568)
default	20:18:44.398437-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:10568 called from <private>
default	20:18:44.398858-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:10568 called from <private>
default	20:18:44.399049-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:10568 called from <private>
default	20:18:44.399271-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:10568 called from <private>
default	20:18:44.399431-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:10568 called from <private>
default	20:18:44.399647-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:10568 called from <private>
default	20:18:44.399806-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:10568 called from <private>
default	20:18:44.399955-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:10568 called from <private>
default	20:18:44.400080-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:10568 called from <private>
default	20:18:44.400211-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:10568 called from <private>
error	20:18:45.020780-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CAIIugCI3D6x0jkL7BXjcYRl0vPhkk-L5K9mxvc/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:194 loadAuthorizationStates(for:) new entry: kTCCServiceScreenCapture com.nexy.assistant none
error	20:18:45.022365-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CAIIugCI3D6x0jkL7BXjcYRl0vPhkk-L5K9mxvc/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:194 loadAuthorizationStates(for:) new entry: kTCCServiceListenEvent com.nexy.assistant full
error	20:18:45.032099-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CAIIugCI3D6x0jkL7BXjcYRl0vPhkk-L5K9mxvc/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:194 loadAuthorizationStates(for:) new entry: kTCCServiceScreenCapture com.nexy.assistant none
error	20:18:45.041471-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CAIIugCI3D6x0jkL7BXjcYRl0vPhkk-L5K9mxvc/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:194 loadAuthorizationStates(for:) new entry: kTCCServiceAppleEvents com.nexy.assistant full
error	20:18:45.042749-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CAIIugCI3D6x0jkL7BXjcYRl0vPhkk-L5K9mxvc/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:194 loadAuthorizationStates(for:) new entry: kTCCServiceMicrophone com.nexy.assistant full
error	20:18:45.051162-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CAIIugCI3D6x0jkL7BXjcYRl0vPhkk-L5K9mxvc/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:194 loadAuthorizationStates(for:) new entry: kTCCServiceAppleEvents com.nexy.assistant full
error	20:18:45.051975-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CAIIugCI3D6x0jkL7BXjcYRl0vPhkk-L5K9mxvc/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:194 loadAuthorizationStates(for:) new entry: kTCCServiceMicrophone com.nexy.assistant full
default	20:18:48.147603-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x92f179800 at /Applications/Nexy.app
default	20:18:48.169960-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x92f179200 at /Applications/Nexy.app
default	20:18:48.179774-0500	tccd	Publishing <TCCDEvent: type=Modify, service=kTCCServiceScreenCapture, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 0 subscribers: {
}
error	20:18:48.236917-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CAIIugCI3D6x0jkL7BXjcYRl0vPhkk-L5K9mxvc/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:194 loadAuthorizationStates(for:) new entry: kTCCServiceScreenCapture com.nexy.assistant full
error	20:18:48.237037-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CAIIugCI3D6x0jkL7BXjcYRl0vPhkk-L5K9mxvc/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:194 loadAuthorizationStates(for:) new entry: kTCCServiceListenEvent com.nexy.assistant full
error	20:18:48.241672-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CAIIugCI3D6x0jkL7BXjcYRl0vPhkk-L5K9mxvc/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:194 loadAuthorizationStates(for:) new entry: kTCCServiceListenEvent com.nexy.assistant full
error	20:18:48.242010-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CAIIugCI3D6x0jkL7BXjcYRl0vPhkk-L5K9mxvc/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:194 loadAuthorizationStates(for:) new entry: kTCCServiceScreenCapture com.nexy.assistant full
error	20:18:48.249408-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CAIIugCI3D6x0jkL7BXjcYRl0vPhkk-L5K9mxvc/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:194 loadAuthorizationStates(for:) new entry: kTCCServiceAppleEvents com.nexy.assistant full
error	20:18:48.249932-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CAIIugCI3D6x0jkL7BXjcYRl0vPhkk-L5K9mxvc/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:194 loadAuthorizationStates(for:) new entry: kTCCServiceMicrophone com.nexy.assistant full
error	20:18:48.253268-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CAIIugCI3D6x0jkL7BXjcYRl0vPhkk-L5K9mxvc/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:194 loadAuthorizationStates(for:) new entry: kTCCServiceAppleEvents com.nexy.assistant full
error	20:18:48.253801-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CAIIugCI3D6x0jkL7BXjcYRl0vPhkk-L5K9mxvc/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:194 loadAuthorizationStates(for:) new entry: kTCCServiceMicrophone com.nexy.assistant full
default	20:18:55.259481-0500	Nexy	[0x863d49540] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	20:18:55.260639-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=35241.6, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=35241, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	20:18:55.262461-0500	tccd	AUTHREQ_SUBJECT: msgID=35241.6, subject=com.nexy.assistant,
default	20:18:55.263490-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x92f17b300 at /Applications/Nexy.app
default	20:18:55.285459-0500	tccd	Notifying for access  kTCCServicePostEvent for target PID[35241], responsiblePID[35241], responsiblePath: /Applications/Nexy.app to UID: 501
default	20:18:55.285936-0500	Nexy	[0x863d49540] invalidated after the last release of the connection object
default	20:18:55.335952-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x92f179800 at /Applications/Nexy.app
default	20:18:55.370944-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x92f179200 at /Applications/Nexy.app
default	20:18:55.374972-0500	tccd	Publishing <TCCDEvent: type=Modify, service=kTCCServicePostEvent, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 0 subscribers: {
}
error	20:18:55.419778-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CAIIugCI3D6x0jkL7BXjcYRl0vPhkk-L5K9mxvc/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:194 loadAuthorizationStates(for:) new entry: kTCCServiceListenEvent com.nexy.assistant full
error	20:18:55.420120-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CAIIugCI3D6x0jkL7BXjcYRl0vPhkk-L5K9mxvc/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:194 loadAuthorizationStates(for:) new entry: kTCCServiceScreenCapture com.nexy.assistant full
error	20:18:55.420231-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CAIIugCI3D6x0jkL7BXjcYRl0vPhkk-L5K9mxvc/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:194 loadAuthorizationStates(for:) new entry: kTCCServiceAccessibility com.nexy.assistant none
error	20:18:55.422065-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CAIIugCI3D6x0jkL7BXjcYRl0vPhkk-L5K9mxvc/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:194 loadAuthorizationStates(for:) new entry: kTCCServiceScreenCapture com.nexy.assistant full
error	20:18:55.422185-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CAIIugCI3D6x0jkL7BXjcYRl0vPhkk-L5K9mxvc/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:194 loadAuthorizationStates(for:) new entry: kTCCServiceListenEvent com.nexy.assistant full
error	20:18:55.422298-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CAIIugCI3D6x0jkL7BXjcYRl0vPhkk-L5K9mxvc/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:194 loadAuthorizationStates(for:) new entry: kTCCServiceAccessibility com.nexy.assistant none
error	20:18:55.435307-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CAIIugCI3D6x0jkL7BXjcYRl0vPhkk-L5K9mxvc/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:194 loadAuthorizationStates(for:) new entry: kTCCServiceAppleEvents com.nexy.assistant full
error	20:18:55.435857-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CAIIugCI3D6x0jkL7BXjcYRl0vPhkk-L5K9mxvc/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:194 loadAuthorizationStates(for:) new entry: kTCCServiceMicrophone com.nexy.assistant full
error	20:18:55.436672-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CAIIugCI3D6x0jkL7BXjcYRl0vPhkk-L5K9mxvc/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:194 loadAuthorizationStates(for:) new entry: kTCCServiceAppleEvents com.nexy.assistant full
error	20:18:55.437184-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CAIIugCI3D6x0jkL7BXjcYRl0vPhkk-L5K9mxvc/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:194 loadAuthorizationStates(for:) new entry: kTCCServiceMicrophone com.nexy.assistant full
default	20:18:58.142046-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x92f179800 at /Applications/Nexy.app
default	20:18:58.179918-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x92f179200 at /Applications/Nexy.app
default	20:18:58.218029-0500	tccd	Publishing <TCCDEvent: type=Modify, service=kTCCServiceAccessibility, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 0 subscribers: {
}
error	20:18:58.248996-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CAIIugCI3D6x0jkL7BXjcYRl0vPhkk-L5K9mxvc/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:194 loadAuthorizationStates(for:) new entry: kTCCServiceAccessibility com.nexy.assistant full
error	20:18:58.249382-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CAIIugCI3D6x0jkL7BXjcYRl0vPhkk-L5K9mxvc/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:194 loadAuthorizationStates(for:) new entry: kTCCServiceScreenCapture com.nexy.assistant full
error	20:18:58.249509-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CAIIugCI3D6x0jkL7BXjcYRl0vPhkk-L5K9mxvc/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:194 loadAuthorizationStates(for:) new entry: kTCCServiceListenEvent com.nexy.assistant full
error	20:18:58.249620-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CAIIugCI3D6x0jkL7BXjcYRl0vPhkk-L5K9mxvc/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:194 loadAuthorizationStates(for:) new entry: kTCCServiceAccessibility com.nexy.assistant full
error	20:18:58.253787-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CAIIugCI3D6x0jkL7BXjcYRl0vPhkk-L5K9mxvc/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:194 loadAuthorizationStates(for:) new entry: kTCCServiceAccessibility com.nexy.assistant full
error	20:18:58.253961-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CAIIugCI3D6x0jkL7BXjcYRl0vPhkk-L5K9mxvc/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:194 loadAuthorizationStates(for:) new entry: kTCCServiceListenEvent com.nexy.assistant full
error	20:18:58.254297-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CAIIugCI3D6x0jkL7BXjcYRl0vPhkk-L5K9mxvc/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:194 loadAuthorizationStates(for:) new entry: kTCCServiceScreenCapture com.nexy.assistant full
error	20:18:58.254415-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CAIIugCI3D6x0jkL7BXjcYRl0vPhkk-L5K9mxvc/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:194 loadAuthorizationStates(for:) new entry: kTCCServiceAccessibility com.nexy.assistant full
error	20:18:58.261445-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CAIIugCI3D6x0jkL7BXjcYRl0vPhkk-L5K9mxvc/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:194 loadAuthorizationStates(for:) new entry: kTCCServiceAppleEvents com.nexy.assistant full
error	20:18:58.261972-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CAIIugCI3D6x0jkL7BXjcYRl0vPhkk-L5K9mxvc/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:194 loadAuthorizationStates(for:) new entry: kTCCServiceMicrophone com.nexy.assistant full
error	20:18:58.265201-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CAIIugCI3D6x0jkL7BXjcYRl0vPhkk-L5K9mxvc/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:194 loadAuthorizationStates(for:) new entry: kTCCServiceAppleEvents com.nexy.assistant full
error	20:18:58.265702-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CAIIugCI3D6x0jkL7BXjcYRl0vPhkk-L5K9mxvc/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:194 loadAuthorizationStates(for:) new entry: kTCCServiceMicrophone com.nexy.assistant full
default	20:19:09.857080-0500	WindowServer	0[outside of RPC]: Process death: 0x0-0x3c13c1 (Nexy) connectionID: 8BD0B pid: 35241 in session 0x101
default	20:19:09.857151-0500	WindowServer	<BSCompoundAssertion:0xbe8809580> ([FocusManager:257]-deferringPolicyEvaluationSuppression) acquire for reason:process death - 0x0-0x3c13c1 (Nexy) acq:0xbecc27bc0 count:1
default	20:19:09.857484-0500	audiomxd	  ServerSessionManager.mm:478   { "action":"destroy_session", "session":{"ID":"0x1e804a","name":"Nexy(35241)"}, "details":null }
default	20:19:09.857578-0500	audiomxd	AudioApplicationInfoImpl.mm:690   Successfully removed session 0x1e804a from AudioApp, recording state unchanged (app: {"name":"[implicit] Nexy","pid":35241})
default	20:19:09.857603-0500	audiomxd	  ServerSessionManager.mm:1086  destroy audio app instance since was created implicitly by session creation and all sessions now gone (audio app: {"name":"[implicit] Nexy","pid":35241})
default	20:19:09.860618-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 75, PID = 35241, Name = sid:0x1e804a, Nexy(35241), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	20:19:09.860932-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 75, PID = 35241, Name = sid:0x1e804a, Nexy(35241), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	20:19:09.862056-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:19:09.862154-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:19:09.862190-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:19:09.861733-0500	audiomxd	UpdateAudioState CID 0x4D120001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:19:09.861897-0500	audiomxd	UpdateAudioState CID 0x4D120001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:19:09.863275-0500	WindowServer	0[outside of RPC]: [FocusManager:257] update to deferring policy requested for reason: permitted list updated - 0x0-0x3c13c1 removed - but we are suppressing evaluation for reasons: {(
    "process death - 0x0-0x3c13c1 (Nexy)"
)}
default	20:19:09.864223-0500	WindowServer	0[outside of RPC]: [FocusManager:257] update to deferring policy requested for reason: permitted list updated - 0x1-0x89a9 removed - but we are suppressing evaluation for reasons: {(
    "process death - 0x0-0x3c13c1 (Nexy)"
)}
default	20:19:09.871611-0500	coreaudiod	>>> NEGOTIATE [com.nexy.assistant]
default	20:19:09.871953-0500	coreaudiod	<<< NEGOTIATE [com.nexy.assistant]
default	20:19:09.873934-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:19:09.876518-0500	runningboardd	XPC connection invalidated: [app<application.com.nexy.assistant.27241569.27241575(501)>:35241]
default	20:19:09.878359-0500	coreaudiod	IssueReporting.cpp:492   RTAID [ use_case=Generic report_type=RMS Generic Chain clientID=ADM node=ADM::com.nexy.assistant_10569.10484.0_airpods noise suppression studio::out-0 issue_detected_sample_time=307680.000000 ] -- [ rms:[-37.719902], peaks:[-14.381990] ]
default	20:19:09.878384-0500	coreaudiod	IssueReporting.cpp:492   RTAID [ use_case=Generic report_type=RMS Generic Chain clientID=ADM node=ADM::com.nexy.assistant_10569.10484.0_airpods noise suppression studio::in-0 issue_detected_sample_time=0.000000 ] -- [ rms:[-35.990845], peaks:[-14.900049] ]
default	20:19:09.883153-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575(501)>:35241] termination reported by launchd (0, 0, 0)
default	20:19:09.883364-0500	runningboardd	Removing process: [app<application.com.nexy.assistant.27241569.27241575(501)>:35241]
default	20:19:09.883682-0500	runningboardd	Removing launch job for: [app<application.com.nexy.assistant.27241569.27241575(501)>:35241]
default	20:19:09.883894-0500	runningboardd	Removed job for [app<application.com.nexy.assistant.27241569.27241575(501)>:35241]
default	20:19:09.883943-0500	runningboardd	Removing assertions for terminated process: [app<application.com.nexy.assistant.27241569.27241575(501)>:35241]
default	20:19:09.887998-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.27241569.27241575(501)>: none (role: None) (endowments: (null))
default	20:19:09.888231-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.27241569.27241575(501)>: none (role: None) (endowments: (null))
default	20:19:09.888381-0500	audiomxd	  ServerSessionManager.mm:1327  Monitored process died, pid = 35241, name = Nexy
default	20:19:09.888844-0500	launchservicesd	Hit the server for a process handle 15e721a3000089a9 that resolved to: [app<application.com.nexy.assistant.27241569.27241575(501)>:35241]
default	20:19:09.888935-0500	gamepolicyd	Received state update for 35241 (app<application.com.nexy.assistant.27241569.27241575(501)>, none-NotVisible
default	20:19:09.892700-0500	loginwindow	-[ApplicationManager handleCASEvent:withData:] | CAS notification for appDeath for com.nexy.assistant with asn: LSASN:{hi=0x0;lo=0x3c13c1} for bundle path: /Applications/Nexy.app with URL: file:///Applications/Nexy.app/
default	20:19:09.892760-0500	loginwindow	-[Application setState:] | enter: <Application: 0x84f9b6800: Nexy> state 3
default	20:19:09.892781-0500	loginwindow	-[PersistentAppsSupport applicationQuit:] | for app:Nexy, _appTrackingState = 2
default	20:19:09.895932-0500	loginwindow	-[Application setState:] | enter: <Application: 0x84f9b6800: Nexy> state 4
default	20:19:09.895946-0500	loginwindow	-[PersistentAppsSupport applicationQuit:] | for app:Nexy, _appTrackingState = 2
default	20:19:12.947917-0500	logger	launching: /usr/bin/open -n -a /Applications/Nexy.app
default	20:19:13.093396-0500	lsd	com.nexy.assistant/Unknown Persona:5:5:1:1:Building bundle record for app
default	20:19:13.093580-0500	lsd	com.nexy.assistant/Unknown Persona:5:5:2:1:Built bundle record for app
default	20:19:13.095386-0500	lsd	com.nexy.assistant/Unknown Persona:5:4:2:1:_LSServerRegisterItemInfo result = 0
default	20:19:13.102582-0500	dmd	Received xpc stream event (distributed notification matching) with name: com.apple.LaunchServices.applicationRegistered user info: {
    CFBundleDisplayName = Nexy;
    bundleIDs =     (
        "com.nexy.assistant"
    );
    isPlaceholder = 0;
}
default	20:19:13.103672-0500	runningboardd	Launch request for app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>[0] is using uid 501 (divined from auid 501 euid 501)
default	20:19:13.103749-0500	runningboardd	Acquiring assertion targeting app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)> from originator [osservice<com.apple.coreservices.uiagent(501)>:3678] with description <RBSAssertionDescriptor| "LS launch com.nexy.assistant" ID:403-3678-159322 target:app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)> attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"LaunchRoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	20:19:13.103832-0500	runningboardd	Assertion 403-3678-159322 (target:app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>) will be created as active
default	20:19:13.107060-0500	runningboardd	Checking PreventLaunch: global:0 exPath:/Applications/Nexy.app/Contents/MacOS/Nexy predicates:(null) allow:(null)
default	20:19:13.107099-0500	runningboardd	Creating and launching job for: app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>
default	20:19:13.107110-0500	runningboardd	_mutateContextIfNeeded called for com.nexy.assistant
default	20:19:13.107194-0500	runningboardd	app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>: -[RBPersonaManager personaForIdentity:context:personaUID:personaUniqueString:] required 0.000000 ms (wallclock); resolved to {4294967295, (null)}
default	20:19:13.118710-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] is not RunningBoard jetsam managed.
default	20:19:13.118725-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] This process will not be managed.
default	20:19:13.118733-0500	runningboardd	Now tracking process: [app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344]
default	20:19:13.118876-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:19:13.119431-0500	gamepolicyd	Hit the server for a process handle 19b8276400008a10 that resolved to: [app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344]
default	20:19:13.119466-0500	gamepolicyd	Received state update for 35344 (app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>, running-active-NotVisible
default	20:19:13.122128-0500	runningboardd	Using default underlying assertion for app: [app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344]
default	20:19:13.122183-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] from originator [app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] with description <RBSAssertionDescriptor| "RB Underlying Assertion" ID:403-403-159323 target:35344 attributes:[
	<RBSDomainAttribute| domain:"com.apple.underlying" name:"defaultUnderlyingAppAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	20:19:13.122296-0500	runningboardd	Assertion 403-403-159323 (target:[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344]) will be created as active
default	20:19:13.122468-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] Ignoring jetsam update because this process is not memory-managed
default	20:19:13.122488-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] Ignoring suspend because this process is not lifecycle managed
default	20:19:13.122503-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] Set darwin role to: UserInteractive
default	20:19:13.122518-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] Ignoring GPU update because this process is not GPU managed
default	20:19:13.122540-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] Ignoring memory limit update because this process is not memory-managed
default	20:19:13.122570-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] reported to RB as running
default	20:19:13.123889-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] from originator [osservice<com.apple.coreservices.launchservicesd>:367] with description <RBSAssertionDescriptor| "uielement:35344" ID:403-367-159324 target:35344 attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"RoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	20:19:13.124017-0500	CoreServicesUIAgent	LAUNCH: 0x0-0x3d63d6 com.nexy.assistant starting stopped process.
default	20:19:13.123995-0500	runningboardd	Assertion 403-367-159324 (target:[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344]) will be created as active
default	20:19:13.124937-0500	loginwindow	-[Application updateInformation] | Got App URL: file:///Applications/Nexy.app/
default	20:19:13.125121-0500	loginwindow	-[Application setState:] | enter: <Application: 0x84f9b6800: Nexy> state 2
default	20:19:13.125142-0500	loginwindow	-[ApplicationManager checkInAppContext:eventData:] | ApplicationManager: Checked in app : Nexy
default	20:19:13.125251-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] Ignoring jetsam update because this process is not memory-managed
default	20:19:13.125282-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] Ignoring suspend because this process is not lifecycle managed
default	20:19:13.125309-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] Ignoring GPU update because this process is not GPU managed
default	20:19:13.125379-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] Ignoring memory limit update because this process is not memory-managed
default	20:19:13.125447-0500	runningboardd	Successfully acquired underlying assertion for [app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344]
default	20:19:13.125822-0500	kernel	Nexy[35344] triggered unnest of range 0x202000000->0x204000000 of DYLD shared region in VM map 0xb6fc158fa54c70a5. While not abnormal for debuggers, this increases system memory footprint until the target exits.
default	20:19:13.125833-0500	kernel	Nexy[35344] triggered unnest of range 0x204000000->0x206000000 of DYLD shared region in VM map 0xb6fc158fa54c70a5. While not abnormal for debuggers, this increases system memory footprint until the target exits.
default	20:19:13.127418-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:19:13.127733-0500	runningboardd	Invalidating assertion 403-3678-159322 (target:app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>) from originator [osservice<com.apple.coreservices.uiagent(501)>:3678]
default	20:19:13.127764-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] Ignoring jetsam update because this process is not memory-managed
default	20:19:13.127787-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] Ignoring suspend because this process is not lifecycle managed
default	20:19:13.127891-0500	gamepolicyd	Received state update for 35344 (app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>, running-active-NotVisible
default	20:19:13.127825-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] Ignoring GPU update because this process is not GPU managed
default	20:19:13.127876-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] Ignoring memory limit update because this process is not memory-managed
default	20:19:13.130414-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:19:13.134207-0500	logger	verifying new process for /Applications/Nexy.app/Contents/MacOS/Nexy
default	20:19:13.166654-0500	logger	detected new pid 35344 for /Applications/Nexy.app/Contents/MacOS/Nexy
default	20:19:13.186428-0500	Nexy	[0x1040f9aa0] activating connection: mach=true listener=false peer=false name=com.apple.cfprefsd.daemon
default	20:19:13.186489-0500	Nexy	[0x1041015f0] activating connection: mach=true listener=false peer=false name=com.apple.cfprefsd.agent
default	20:19:13.234544-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] Ignoring jetsam update because this process is not memory-managed
default	20:19:13.234558-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] Ignoring suspend because this process is not lifecycle managed
default	20:19:13.234568-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] Ignoring GPU update because this process is not GPU managed
default	20:19:13.234587-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] Ignoring memory limit update because this process is not memory-managed
default	20:19:13.234704-0500	gamepolicyd	Received state update for 35344 (app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>, running-active-NotVisible
default	20:19:13.237483-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:19:13.237750-0500	gamepolicyd	Received state update for 35344 (app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>, running-active-NotVisible
error	20:19:13.310003-0500	Nexy	dlsym cannot find symbol NSMakeRect in CFBundle 0x104103e30 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	20:19:13.310221-0500	Nexy	dlsym cannot find symbol NSMakePoint in CFBundle 0x104103e30 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	20:19:13.310421-0500	Nexy	dlsym cannot find symbol NSMakeSize in CFBundle 0x104103e30 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	20:19:13.310611-0500	Nexy	dlsym cannot find symbol NSMakeRange in CFBundle 0x104103e30 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
default	20:19:13.311543-0500	Nexy	[0x1040e80e0] activating connection: mach=true listener=false peer=false name=com.apple.coreservices.launchservicesd
default	20:19:13.312124-0500	Nexy	[0x735af8000] activating connection: mach=true listener=false peer=false name=com.apple.analyticsd
default	20:19:13.312392-0500	Nexy	[0x735af8140] activating connection: mach=true listener=false peer=false name=com.apple.pasteboard.1
default	20:19:13.312746-0500	Nexy	[0x735af8280] activating connection: mach=true listener=false peer=false name=com.apple.distributed_notifications@Uv3
default	20:19:13.314584-0500	Nexy	void _NSDisableAutomaticTerminationAndLog(NSString *) No windows open yet
default	20:19:13.314903-0500	Nexy	[0x735af83c0] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	20:19:13.315466-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=35344.1, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=35344, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	20:19:13.316896-0500	tccd	AUTHREQ_SUBJECT: msgID=35344.1, subject=com.nexy.assistant,
default	20:19:13.318352-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x92f17bc00 at /Applications/Nexy.app
default	20:19:13.322355-0500	Nexy	Received configuration update from daemon (initial)
default	20:19:13.350090-0500	Nexy	[0x735af83c0] invalidated after the last release of the connection object
default	20:19:13.350327-0500	Nexy	server port 0x00003407, session port 0x00003407
default	20:19:13.351201-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=397.2777, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=35344, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=397, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	20:19:13.351226-0500	tccd	requestor: TCCDProcess: identifier=com.apple.WindowServer, pid=397, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=35344, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	20:19:13.352093-0500	tccd	AUTHREQ_SUBJECT: msgID=397.2777, subject=com.nexy.assistant,
default	20:19:13.352708-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x92f17bc00 at /Applications/Nexy.app
default	20:19:13.395268-0500	Nexy	New connection 0x10cb97 main
default	20:19:13.397577-0500	Nexy	CHECKIN: pid=35344
default	20:19:13.405497-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] from originator [osservice<com.apple.coreservices.launchservicesd>:367] with description <RBSAssertionDescriptor| "uielement:35344" ID:403-367-159325 target:35344 attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"RoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	20:19:13.405585-0500	runningboardd	Assertion 403-367-159325 (target:[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344]) will be created as active
default	20:19:13.405906-0500	Nexy	CHECKEDIN: pid=35344 asn=0x0-0x3d63d6 foreground=0
default	20:19:13.405755-0500	launchservicesd	CHECKIN:0x0-0x3d63d6 35344 com.nexy.assistant
default	20:19:13.406121-0500	runningboardd	Invalidating assertion 403-367-159324 (target:[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344]) from originator [osservice<com.apple.coreservices.launchservicesd>:367]
default	20:19:13.406141-0500	Nexy	[0x735af83c0] activating connection: mach=false listener=true peer=false name=(anonymous)
default	20:19:13.405925-0500	loginwindow	-[Application updateInformation] | Got App URL: file:///Applications/Nexy.app/
default	20:19:13.406150-0500	Nexy	[0x735af83c0] Connection returned listener port: 0x4703
default	20:19:13.409374-0500	Nexy	[0x735af8500] activating connection: mach=true listener=false peer=false name=com.apple.lsd.mapdb
default	20:19:13.413832-0500	Nexy	Current system appearance, (HLTB: 2), (SLS: 1)
default	20:19:13.422368-0500	distnoted	register name: com.apple.xctest.FakeForceTouchDevice object: com.nexy.assistant token: 1e0000001d pid: 35344
default	20:19:13.438406-0500	Nexy	Registered process with identifier 35344-1785309
default	20:19:13.563709-0500	Nexy	Registered notify signal com.apple.caulk.alloc.rtdump (0)
default	20:19:13.566055-0500	Nexy	System_Input_Processing_Notification_Handler.mm:456   System_Input_Processing_Notification_Handler::is_vi_available(): Voice isolation DSP is available for client with bundle id com.nexy.assistant (AVFoundation is available, application is not in client deny list, application is not FaceTime variant)
default	20:19:13.567312-0500	Nexy	[0x735af8b40] activating connection: mach=true listener=false peer=false name=com.apple.cmio.registerassistantservice.system-extensions
fault	20:19:13.569188-0500	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F AUID=501> and <type=Application identifier=application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F>
default	20:19:13.573236-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOInitializeListenersForBundleID: for <private> -> <private>
default	20:19:13.574580-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> vpio_preferenceChangedListener: new value ((null)) for key AUVoiceIOClients/com-nexy-assistant/AUVoiceIOChatFlavor, translatedBundleID com.nexy.assistant, bundleIDs {(
    "com.nexy.assistant"
)}
default	20:19:13.574717-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> vpio_preferenceChangedListener: new value ((null)) for key AUVoiceIOClients/com-nexy-assistant/AUVoiceIOIsAutoChatFlavorEnabled, translatedBundleID com.nexy.assistant, bundleIDs {(
    "com.nexy.assistant"
)}
default	20:19:13.574841-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetSupportedChatFlavorsForBundleID: <private>-><private> get supported chat flavors: <private>
default	20:19:13.574850-0500	Nexy	            HALSystem.cpp:134    Enabling HAL Voice Isolation support
default	20:19:13.574877-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetHiddenChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	20:19:13.574979-0500	Nexy	[0x735af8c80] activating connection: mach=true listener=false peer=false name=com.apple.tccd
default	20:19:13.575059-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOHiddenChatFlavors newValue: (
    1
)
default	20:19:13.575404-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=35344.2, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=35344, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	20:19:13.581408-0500	tccd	AUTHREQ_SUBJECT: msgID=35344.2, subject=com.nexy.assistant,
default	20:19:13.582035-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc79244000 at /Applications/Nexy.app
default	20:19:13.611634-0500	Nexy	[0x735af8c80] invalidated after the last release of the connection object
default	20:19:13.611800-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetPreferredChatFlavorForBundleID: <private>-><private> get value: 0
default	20:19:13.611844-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetSupportedChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	20:19:13.612056-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOSupportedChatFlavors newValue: (
    0,
    2
)
default	20:19:13.613121-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=411.1573, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=35344, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=398, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	20:19:13.613991-0500	tccd	AUTHREQ_SUBJECT: msgID=411.1573, subject=com.nexy.assistant,
default	20:19:13.614550-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc79244000 at /Applications/Nexy.app
error	20:19:13.642479-0500	tccd	Request message contains a target_token to accessing_process (TCCDProcess: identifier=com.nexy.assistant, pid=35344, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy) but TCCDProcess: identifier=com.apple.audio.coreaudiod, pid=411, auid=202, euid=202, binary_path=/usr/sbin/coreaudiod is not a TCC manager for service: kTCCServiceScreenCapture.
default	20:19:13.643325-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=411.1575, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=35344, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=398, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	20:19:13.644099-0500	tccd	AUTHREQ_SUBJECT: msgID=411.1575, subject=com.nexy.assistant,
default	20:19:13.644633-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc79244000 at /Applications/Nexy.app
default	20:19:13.671892-0500	Nexy	  HALPlugInManagement.cpp:440    HALPlugInManagement::RegisterPlugIns: skipping in-process plug-ins
error	20:19:13.671911-0500	Nexy	AddInstanceForFactory: No factory registered for id <CFUUID 0x734961c40> F8BB1C28-BAE8-11D6-9C31-00039315CD46
error	20:19:13.687589-0500	Nexy	         HALC_ProxyObjectMap.cpp:174   HALC_ProxyObjectMap::_CopyObjectByObjectID: failed to create the local object
error	20:19:13.687598-0500	Nexy	            HALC_ShellDevice.cpp:2673  HALC_ShellDevice::RebuildControlList: couldn't find the control object
default	20:19:13.690331-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	20:19:13.690464-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	20:19:13.694928-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetPreferredChatFlavorForBundleID: <private>-><private> get value: 0
default	20:19:15.197094-0500	kernel	SK[7]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid C04CAB2A-7987-4E49-8B23-25B91D5F8A8A flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.58416,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0xce28cf41 tp_proto=0x06"
default	20:19:15.197154-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:58416<-><IPv4-redacted>:53] interface: utun6 (skipped: 47531)
so_gencnt: 2920218 t_state: SYN_SENT process: Nexy:35344 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 1 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xbcb4aa12
default	20:19:15.197565-0500	kernel	tcp connected: [<IPv4-redacted>:58416<-><IPv4-redacted>:53] interface: utun6 (skipped: 47531)
so_gencnt: 2920218 t_state: ESTABLISHED process: Nexy:35344 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 1 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xbcb4aa12
default	20:19:15.197803-0500	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:58416<-><IPv4-redacted>:53] interface: utun6 (skipped: 47531)
so_gencnt: 2920218 t_state: FIN_WAIT_1 process: Nexy:35344 Duration: 0.001 sec Conn_Time: 0.001 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 1.000 ms rttvar: 0.500 ms base rtt: 1 ms so_error: 0 svc/tc: 0 flow: 0xbcb4aa12
default	20:19:15.197813-0500	kernel	tcp_connection_summary [<IPv4-redacted>:58416<-><IPv4-redacted>:53] interface: utun6 (skipped: 47531)
so_gencnt: 2920218 t_state: FIN_WAIT_1 process: Nexy:35344 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	20:19:15.214332-0500	Nexy	[0x735af8c80] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioComponentRegistrar
default	20:19:15.226484-0500	Nexy	                AUHAL.cpp:420   AUHAL: (0x737023140) Selecting device 85 from constructor
default	20:19:15.226495-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0x737023140)
default	20:19:15.226500-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0x737023140) not already running
default	20:19:15.226505-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0x737023140) nothing to teardown
default	20:19:15.226507-0500	Nexy	                AUHAL.cpp:762   SelectDevice: (0x737023140) connecting device 85
default	20:19:15.226593-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0x737023140) Device ID: 85 (Input:No | Output:Yes): true
default	20:19:15.226706-0500	Nexy	                AUHAL.cpp:774   SelectDevice: (0x737023140) created ioproc 0xa for device 85
default	20:19:15.226815-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x737023140) adding 7 device listeners to device 85
default	20:19:15.226991-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x737023140) adding 0 device delegate listeners to device 85
default	20:19:15.226999-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x737023140)
default	20:19:15.227076-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  48000 Hz, Float32, interleaved
default	20:19:15.227086-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	20:19:15.227092-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	20:19:15.227099-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	20:19:15.227107-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	20:19:15.227201-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x737023140) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	20:19:15.227214-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x737023140) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	20:19:15.227219-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	20:19:15.227226-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x737023140) removing 0 device listeners from device 0
default	20:19:15.227231-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x737023140) removing 0 device delegate listeners from device 0
default	20:19:15.227235-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0x737023140)
default	20:19:15.227248-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is DISABLED
default	20:19:15.227324-0500	Nexy	                AUHAL.cpp:2303  SetProperty: (0x737023140) caller requesting device change from 85 to 91
default	20:19:15.227330-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0x737023140)
default	20:19:15.227334-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0x737023140) not already running
default	20:19:15.227340-0500	Nexy	                AUHAL.cpp:687   SelectDevice: (0x737023140) disconnecting device 85
default	20:19:15.227345-0500	Nexy	                AUHAL.cpp:751   SelectDevice: (0x737023140) destroying ioproc 0xa for device 85
default	20:19:15.227396-0500	Nexy	  AVAudioSession_MacOS.mm:1021  initForMacOS
default	20:19:15.227797-0500	Nexy	[0x735af8f00] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioSession
default	20:19:15.228614-0500	audiomxd	  ServerSessionManager.mm:315   { "action":"create_session", "session":{"ID":"0x1e804b","name":"Nexy(35344)"}, "details":{"PID":35344,"session_type":"Primary"} }
default	20:19:15.228688-0500	audiomxd	AudioApplicationInfoImpl.mm:250   Setting initial isRecording state: 0 for newly-created AudioApp
	app: {"name":"[implicit] Nexy","pid":35344}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1e804b, sessionType: 'prim', isRecording: false }, 
]
default	20:19:15.229334-0500	audiomxd	  ServerSessionManager.mm:1322  Start process monitoring, pid = 35344, name = Nexy
default	20:19:15.229634-0500	Nexy	    SessionCore_Create.mm:99    Created session 0x7359fd240 with ID: 0x1e804b
default	20:19:15.230249-0500	Nexy	[0x735af9040] activating connection: mach=true listener=false peer=false name=com.apple.audioanalyticsd
error	20:19:15.230635-0500	Nexy	Reporter disconnected. { function=sendMessage, reporterID=151801324109825 }
default	20:19:15.230650-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped Unknown {1C-77-54-18-C8-A3:output, 0xa}
default	20:19:15.230701-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	20:19:15.230791-0500	Nexy	                AUHAL.cpp:762   SelectDevice: (0x737023140) connecting device 91
default	20:19:15.230876-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0x737023140) Device ID: 91 (Input:Yes | Output:No): true
default	20:19:15.232290-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=411.1576, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=35344, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=398, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	20:19:15.233804-0500	tccd	AUTHREQ_SUBJECT: msgID=411.1576, subject=com.nexy.assistant,
default	20:19:15.234532-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc79244000 at /Applications/Nexy.app
default	20:19:15.267601-0500	Nexy	                AUHAL.cpp:774   SelectDevice: (0x737023140) created ioproc 0xa for device 91
default	20:19:15.267760-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x737023140) adding 7 device listeners to device 91
default	20:19:15.267935-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x737023140) adding 0 device delegate listeners to device 91
default	20:19:15.267946-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x737023140)
default	20:19:15.267955-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 output streams; not all mono
default	20:19:15.267966-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	20:19:15.268102-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  input stream 0 [0x5c]:  1 ch,  24000 Hz, Float32
default	20:19:15.268110-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 input streams; all mono
default	20:19:15.268116-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  1 ch,  24000 Hz, Float32
default	20:19:15.268207-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x737023140) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	20:19:15.268217-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x737023140) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	20:19:15.268222-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	20:19:15.268225-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x737023140) removing 7 device listeners from device 85
default	20:19:15.268383-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x737023140) removing 0 device delegate listeners from device 85
default	20:19:15.268392-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0x737023140)
default	20:19:15.269025-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	20:19:15.270273-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=411.1577, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=35344, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=398, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	20:19:15.271289-0500	tccd	AUTHREQ_SUBJECT: msgID=411.1577, subject=com.nexy.assistant,
default	20:19:15.271879-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc79244000 at /Applications/Nexy.app
default	20:19:15.301021-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	20:19:15.302050-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=411.1578, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=35344, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=398, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	20:19:15.303008-0500	tccd	AUTHREQ_SUBJECT: msgID=411.1578, subject=com.nexy.assistant,
default	20:19:15.303605-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc79244000 at /Applications/Nexy.app
default	20:19:15.332726-0500	Nexy	Registered notify signal com.apple.caulk.alloc.audiodump (0)
default	20:19:15.334230-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=411.1579, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=35344, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=398, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	20:19:15.335390-0500	tccd	AUTHREQ_SUBJECT: msgID=411.1579, subject=com.nexy.assistant,
default	20:19:15.336384-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc79244000 at /Applications/Nexy.app
default	20:19:15.370073-0500	coreaudiod	>>> NEGOTIATE [com.nexy.assistant]
default	20:19:15.370223-0500	coreaudiod	<<< NEGOTIATE [com.nexy.assistant]
default	20:19:15.370943-0500	coreaudiod	>>> ADAPT [com.nexy.assistant]
default	20:19:15.371227-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xa380ea700] Created node ADM::com.nexy.assistant_10585.10484.0_airpods noise suppression studio::in-0 with nodeID 0 - reporting period = 10.000000, sample rate = 24000.000000
default	20:19:15.371290-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xa380ea700] Created node ADM::com.nexy.assistant_10585.10484.0_airpods noise suppression studio::out-0 with nodeID 1 - reporting period = 10.000000, sample rate = 24000.000000
default	20:19:15.446974-0500	coreaudiod	<<< ADAPT [com.nexy.assistant]
default	20:19:15.448426-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:10585 called from <private>
default	20:19:15.448503-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Input {1C-77-54-18-C8-A3:input, 0xa}
default	20:19:15.448561-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	20:19:15.450397-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:10585 called from <private>
default	20:19:15.450546-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(10585)
default	20:19:15.453066-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] from originator [osservice<com.apple.powerd>:338] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:403-338-159328 target:35344 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	20:19:15.453900-0500	runningboardd	Assertion 403-338-159328 (target:[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344]) will be created as active
default	20:19:15.450575-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:10585 called from <private>
default	20:19:15.450583-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(10584)
fault	20:19:15.455418-0500	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F AUID=501> and <type=Application identifier=application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F>
default	20:19:15.455444-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] Ignoring jetsam update because this process is not memory-managed
default	20:19:15.455806-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] Ignoring suspend because this process is not lifecycle managed
default	20:19:15.456154-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] Ignoring GPU update because this process is not GPU managed
default	20:19:15.456469-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] Ignoring memory limit update because this process is not memory-managed
default	20:19:15.450864-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:10585 called from <private>
default	20:19:15.450936-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:10584 called from <private>
default	20:19:15.450977-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:10584 called from <private>
fault	20:19:15.458496-0500	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F AUID=501> and <type=Application identifier=application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F>
default	20:19:15.459379-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	20:19:15.459969-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	20:19:15.462934-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(10585)
default	20:19:15.462959-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(10585)
default	20:19:15.462968-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(10585)
default	20:19:15.462979-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(10585)
default	20:19:15.464745-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:10585 called from <private>
default	20:19:15.464755-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:10585 called from <private>
default	20:19:15.464766-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:10585 called from <private>
default	20:19:15.468174-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1e804b","name":"Nexy(35344)"}, "details":{"deviceUIDs":["1C-77-54-18-C8-A3:input"],"implicit_category":"Record","input_running":true,"output_running":false} }
default	20:19:15.468281-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 76, PID = 35344, Name = sid:0x1e804b, Nexy(35344), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	20:19:15.468327-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 76, PID = 35344, Name = sid:0x1e804b, Nexy(35344), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	20:19:15.468415-0500	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1e804b, Nexy(35344), 'prim'', AudioCategory changed to 'Record_WithBluetooth'
default	20:19:15.468774-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:19:15.468523-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 76, PID = 35344, Name = sid:0x1e804b, Nexy(35344), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	20:19:15.468491-0500	audiomxd	UpdateAudioState CID 0x4D120001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:19:15.468688-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 76, PID = 35344, Name = sid:0x1e804b, Nexy(35344), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	20:19:15.469151-0500	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 76, PID = 35344, Name = sid:0x1e804b, Nexy(35344), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> is going active
default	20:19:15.464777-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:10585 called from <private>
default	20:19:15.469729-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1e804b, Nexy(35344), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 76 starting recording
default	20:19:15.470268-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 76, PID = 35344, Name = sid:0x1e804b, Nexy(35344), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	20:19:15.464785-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:10585 called from <private>
default	20:19:15.464824-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:10585 called from <private>
default	20:19:15.470419-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 76, PID = 35344, Name = sid:0x1e804b, Nexy(35344), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	20:19:15.470547-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1e804b, Nexy(35344), 'prim'', displayID:'com.nexy.assistant'}
default	20:19:15.464874-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:10585 called from <private>
default	20:19:15.469455-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(10585)
default	20:19:15.470700-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [1, 0]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:input"
)}
default	20:19:15.470743-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	20:19:15.471349-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(10584)
default	20:19:15.471549-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:10584 called from <private>
default	20:19:15.471601-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:10584 called from <private>
default	20:19:15.470797-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	20:19:15.471648-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:10584 called from <private>
default	20:19:15.471860-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:19:15.471759-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:10584 called from <private>
default	20:19:15.471733-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=411.1580, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=35344, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=398, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	20:19:15.471925-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(10584)
default	20:19:15.471966-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:10584 called from <private>
default	20:19:15.472044-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:10584 called from <private>
default	20:19:15.472481-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(10584)
default	20:19:15.472737-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:10584 called from <private>
default	20:19:15.472794-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:10584 called from <private>
default	20:19:15.473076-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:10584 called from <private>
default	20:19:15.473330-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:10584 called from <private>
default	20:19:15.474277-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:10584 called from <private>
default	20:19:15.474360-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:10584 called from <private>
default	20:19:15.474154-0500	runningboardd	Invalidating assertion 403-338-159328 (target:[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344]) from originator [osservice<com.apple.powerd>:338]
default	20:19:15.474484-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(10584)
default	20:19:15.474499-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:10584 called from <private>
default	20:19:15.474539-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:10584 called from <private>
default	20:19:15.474828-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(10584)
default	20:19:15.475054-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:10584 called from <private>
default	20:19:15.475132-0500	gamepolicyd	Received state update for 35344 (app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>, running-active-NotVisible
default	20:19:15.475064-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:10584 called from <private>
default	20:19:15.475080-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:10584 called from <private>
default	20:19:15.475090-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:10584 called from <private>
default	20:19:15.475816-0500	tccd	AUTHREQ_SUBJECT: msgID=411.1580, subject=com.nexy.assistant,
default	20:19:15.476686-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc79244000 at /Applications/Nexy.app
default	20:19:15.502362-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:19:15.507033-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:19:15.507195-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	20:19:15.509073-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:19:15.515147-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	20:19:15.515239-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	20:19:15.515275-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	20:19:15.515408-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	20:19:15.519977-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:19:15.519990-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:19:15.520004-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:19:15.520009-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:19:15.520016-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:19:15.520024-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	20:19:15.520237-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	20:19:15.530420-0500	coreaudiod	>>> NEGOTIATE [com.nexy.assistant]
default	20:19:15.530567-0500	coreaudiod	<<< NEGOTIATE [com.nexy.assistant]
default	20:19:15.533878-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:10585 called from <private>
default	20:19:15.533917-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:10585 called from <private>
default	20:19:15.533940-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 1 1, id:10585 called from <private>
default	20:19:15.534673-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] from originator [osservice<com.apple.powerd>:338] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:403-338-159329 target:35344 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	20:19:15.534744-0500	runningboardd	Assertion 403-338-159329 (target:[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344]) will be created as active
default	20:19:15.538577-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:10585 called from <private>
default	20:19:15.538590-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:10585 called from <private>
default	20:19:15.538628-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:10585 called from <private>
default	20:19:15.539498-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:10584 called from <private>
default	20:19:15.539531-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:10584 called from <private>
default	20:19:15.539696-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(10584)
default	20:19:15.539887-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(10584)
default	20:19:15.536674-0500	runningboardd	Invalidating assertion 403-338-159329 (target:[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344]) from originator [osservice<com.apple.powerd>:338]
default	20:19:15.540036-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=411.1581, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=35344, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=398, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	20:19:15.540007-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:10584 called from <private>
default	20:19:15.540014-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:10584 called from <private>
default	20:19:15.540093-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:10584 called from <private>
default	20:19:15.540189-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:10584 called from <private>
default	20:19:15.545494-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	20:19:15.545563-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	20:19:15.545608-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	20:19:15.545754-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	20:19:15.546133-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:19:15.546143-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:19:15.546179-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:19:15.546248-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:19:15.546299-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:19:15.546372-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	20:19:15.580425-0500	coreaudiod	>>> ADAPT [com.nexy.assistant]
default	20:19:15.580594-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] Ignoring jetsam update because this process is not memory-managed
default	20:19:15.580605-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] Ignoring suspend because this process is not lifecycle managed
default	20:19:15.580615-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] Ignoring GPU update because this process is not GPU managed
default	20:19:15.580634-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] Ignoring memory limit update because this process is not memory-managed
default	20:19:15.582139-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xa380ea700] Created node ADM::com.nexy.assistant_10585.10484.0_airpods noise suppression studio::in-0 with nodeID 0 - reporting period = 10.000000, sample rate = 24000.000000
default	20:19:15.582204-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xa380ea700] Created node ADM::com.nexy.assistant_10585.10484.0_airpods noise suppression studio::out-0 with nodeID 1 - reporting period = 10.000000, sample rate = 24000.000000
default	20:19:15.584759-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:19:15.585211-0500	gamepolicyd	Received state update for 35344 (app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>, running-active-NotVisible
default	20:19:15.616713-0500	coreaudiod	<<< ADAPT [com.nexy.assistant]
default	20:19:15.618701-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] from originator [osservice<com.apple.powerd>:338] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:403-338-159331 target:35344 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	20:19:15.620254-0500	runningboardd	Assertion 403-338-159331 (target:[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344]) will be created as active
default	20:19:15.620021-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:10585 called from <private>
default	20:19:15.620073-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 1 1 id:10585 called from <private>
default	20:19:15.620093-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 1 1, id:10585 called from <private>
default	20:19:15.620099-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 1 2 2, id:10585 called from <private>
default	20:19:15.620110-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 1 2 2 id:10585 called from <private>
default	20:19:15.620119-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 1 1 id:10585 called from <private>
default	20:19:15.620584-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] Ignoring jetsam update because this process is not memory-managed
default	20:19:15.620091-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	20:19:15.620616-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] Ignoring suspend because this process is not lifecycle managed
default	20:19:15.620661-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] Ignoring GPU update because this process is not GPU managed
default	20:19:15.620735-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] Ignoring memory limit update because this process is not memory-managed
default	20:19:15.621790-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:10585 called from <private>
default	20:19:15.621906-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(10585)
default	20:19:15.621922-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:10585 called from <private>
default	20:19:15.621929-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:10585 called from <private>
default	20:19:15.622631-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	20:19:15.622984-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	20:19:15.623544-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(10585)
default	20:19:15.623784-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:10585 called from <private>
default	20:19:15.623796-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:10585 called from <private>
default	20:19:15.623812-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:10585 called from <private>
default	20:19:15.625085-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=411.1582, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=35344, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=398, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	20:19:15.627938-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:19:15.628284-0500	runningboardd	Invalidating assertion 403-338-159331 (target:[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344]) from originator [osservice<com.apple.powerd>:338]
default	20:19:15.629012-0500	tccd	AUTHREQ_SUBJECT: msgID=411.1582, subject=com.nexy.assistant,
default	20:19:15.629813-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc79244000 at /Applications/Nexy.app
default	20:19:15.630486-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	20:19:15.630589-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	20:19:15.630672-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	20:19:15.631522-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:19:15.631567-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:19:15.631643-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:19:15.631747-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:19:15.631788-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:19:15.631830-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	20:19:15.631881-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:19:15.631922-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:19:15.631953-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:19:15.631984-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:19:15.632028-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:19:15.632066-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	20:19:15.632287-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	20:19:15.632311-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	20:19:15.632540-0500	ControlCenter	Navigating to new application [com.nexy.assistant]
default	20:19:15.636619-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:19:15.636631-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:19:15.636641-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:19:15.636647-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:19:15.636655-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:19:15.636661-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	20:19:15.636743-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	20:19:15.663877-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:10585 called from <private>
default	20:19:15.664731-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] from originator [osservice<com.apple.powerd>:338] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:403-338-159332 target:35344 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	20:19:15.664800-0500	runningboardd	Assertion 403-338-159332 (target:[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344]) will be created as active
default	20:19:15.669822-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	20:19:15.669871-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	20:19:15.669909-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	20:19:15.670284-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:19:15.670293-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:19:15.670305-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:19:15.670311-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:19:15.670320-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:19:15.670327-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	20:19:15.670346-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:19:15.670372-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:19:15.670399-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:19:15.670429-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:19:15.670456-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:19:15.670464-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	20:19:15.670654-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	20:19:15.670804-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:19:15.670814-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:19:15.670821-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:19:15.670829-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:19:15.670841-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:19:15.670849-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	20:19:15.670886-0500	ControlCenter	Navigating to new application [com.nexy.assistant]
default	20:19:15.686212-0500	gamepolicyd	Received state update for 35344 (app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>, running-active-NotVisible
default	20:19:16.690428-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xa}
default	20:19:16.691059-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1e804b","name":"Nexy(35344)"}, "details":{"deviceUIDs":[],"implicit_category":"","input_running":false,"output_running":false} }
default	20:19:16.691267-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 76, PID = 35344, Name = sid:0x1e804b, Nexy(35344), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	20:19:16.691390-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 76, PID = 35344, Name = sid:0x1e804b, Nexy(35344), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	20:19:16.691466-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1e804b, Nexy(35344), 'prim'', displayID:'com.nexy.assistant'}
default	20:19:16.691586-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	20:19:16.691615-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1e804b, Nexy(35344), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 76 stopping recording
default	20:19:16.691678-0500	audiomxd	-MXCoreSession- -[MXCoreSession endInterruption:]: Session <ID: 76, PID = 35344, Name = sid:0x1e804b, Nexy(35344), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> is going inactive
default	20:19:16.691751-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 76, PID = 35344, Name = sid:0x1e804b, Nexy(35344), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	20:19:16.691860-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 76, PID = 35344, Name = sid:0x1e804b, Nexy(35344), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	20:19:16.692141-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 200 flag 0x1 < Hijack > app com.nexy.assistant CID 0x4D120001 category Not set
default	20:19:16.692085-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 0]. BT device UIDS: {(
)}
default	20:19:16.692109-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	20:19:16.692660-0500	audiomxd	UpdateAudioState CID 0x4D120001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	20:19:16.692787-0500	audiomxd	UpdateAudioState CID 0x4D120001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:19:16.692850-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	20:19:16.692898-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	20:19:16.692919-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	20:19:16.692965-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:19:16.693026-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	20:19:16.693043-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:19:16.693075-0500	audioaccessoryd	AudioStateChanged: Removed audio session app com.nexy.assistant 201 count 0
default	20:19:16.695550-0500	runningboardd	Invalidating assertion 403-338-159332 (target:[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344]) from originator [osservice<com.apple.powerd>:338]
default	20:19:16.697791-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	20:19:16.700845-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:19:16.700861-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:19:16.700876-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:19:16.700885-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:19:16.700894-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:19:16.700902-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	20:19:16.701054-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	20:19:16.791977-0500	Nexy	                AUHAL.cpp:473   ~AUHAL: (0x737023140) Selecting device 0 from destructor
default	20:19:16.792002-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0x737023140)
default	20:19:16.792021-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0x737023140) not already running
default	20:19:16.792032-0500	Nexy	                AUHAL.cpp:687   SelectDevice: (0x737023140) disconnecting device 91
default	20:19:16.792042-0500	Nexy	                AUHAL.cpp:751   SelectDevice: (0x737023140) destroying ioproc 0xa for device 91
default	20:19:16.792090-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xa}
default	20:19:16.792145-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	20:19:16.792386-0500	Nexy	                AUHAL.cpp:853   SelectDevice: (0x737023140) nothing to setup
default	20:19:16.792398-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x737023140) adding 0 device listeners to device 0
default	20:19:16.792403-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x737023140) adding 0 device delegate listeners to device 0
default	20:19:16.792411-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x737023140) removing 7 device listeners from device 91
default	20:19:16.792666-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x737023140) removing 0 device delegate listeners from device 91
default	20:19:16.792685-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0x737023140)
default	20:19:16.801868-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] Ignoring jetsam update because this process is not memory-managed
default	20:19:16.801887-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] Ignoring suspend because this process is not lifecycle managed
default	20:19:16.801927-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] Ignoring GPU update because this process is not GPU managed
default	20:19:16.802006-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] Ignoring memory limit update because this process is not memory-managed
default	20:19:16.804980-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:19:16.817014-0500	gamepolicyd	Received state update for 35344 (app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>, running-active-NotVisible
default	20:19:17.635247-0500	Nexy	[0x735af9400] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	20:19:17.636526-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=35344.3, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=35344, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	20:19:17.638355-0500	tccd	AUTHREQ_SUBJECT: msgID=35344.3, subject=com.nexy.assistant,
default	20:19:17.639504-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x92f17bc00 at /Applications/Nexy.app
default	20:19:17.673590-0500	Nexy	[0x735af9400] invalidated after the last release of the connection object
default	20:19:17.673888-0500	Nexy	server port 0x00014483, session port 0x00003407
default	20:19:17.674782-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=397.2778, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=35344, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=397, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	20:19:17.674810-0500	tccd	requestor: TCCDProcess: identifier=com.apple.WindowServer, pid=397, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=35344, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	20:19:17.675801-0500	tccd	AUTHREQ_SUBJECT: msgID=397.2778, subject=com.nexy.assistant,
default	20:19:17.676412-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x92f17bc00 at /Applications/Nexy.app
default	20:19:17.720680-0500	kernel	SK[6]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 2557E5E9-D6A1-424D-BE32-1EF3B3A660D9 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.58417,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0xff0d3da3 tp_proto=0x06"
default	20:19:17.720755-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:58417<-><IPv4-redacted>:53] interface: utun6 (skipped: 47531)
so_gencnt: 2920220 t_state: SYN_SENT process: Nexy:35344 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 1 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x92096876
default	20:19:17.721355-0500	kernel	tcp connected: [<IPv4-redacted>:58417<-><IPv4-redacted>:53] interface: utun6 (skipped: 47531)
so_gencnt: 2920220 t_state: ESTABLISHED process: Nexy:35344 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 1 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x92096876
default	20:19:17.721786-0500	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:58417<-><IPv4-redacted>:53] interface: utun6 (skipped: 47531)
so_gencnt: 2920220 t_state: FIN_WAIT_1 process: Nexy:35344 Duration: 0.001 sec Conn_Time: 0.001 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 1.000 ms rttvar: 0.500 ms base rtt: 1 ms so_error: 0 svc/tc: 0 flow: 0x92096876
default	20:19:17.721797-0500	kernel	tcp_connection_summary [<IPv4-redacted>:58417<-><IPv4-redacted>:53] interface: utun6 (skipped: 47531)
so_gencnt: 2920220 t_state: FIN_WAIT_1 process: Nexy:35344 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	20:19:17.722033-0500	kernel	SK[6]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 70B7B3E8-9EBA-420C-AF96-C8116B73B286 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.58418,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0x943766b1 tp_proto=0x06"
default	20:19:17.722049-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:58418<-><IPv4-redacted>:53] interface: utun6 (skipped: 47531)
so_gencnt: 2920221 t_state: SYN_SENT process: Nexy:35344 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 1 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xa4f0c450
default	20:19:17.722163-0500	kernel	tcp connected: [<IPv4-redacted>:58418<-><IPv4-redacted>:53] interface: utun6 (skipped: 47531)
so_gencnt: 2920221 t_state: ESTABLISHED process: Nexy:35344 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 1 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xa4f0c450
default	20:19:17.722444-0500	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:58418<-><IPv4-redacted>:53] interface: utun6 (skipped: 47531)
so_gencnt: 2920221 t_state: FIN_WAIT_1 process: Nexy:35344 Duration: 0.001 sec Conn_Time: 0.001 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 1.000 ms rttvar: 0.500 ms base rtt: 1 ms so_error: 0 svc/tc: 0 flow: 0xa4f0c450
default	20:19:17.722454-0500	kernel	tcp_connection_summary [<IPv4-redacted>:58418<-><IPv4-redacted>:53] interface: utun6 (skipped: 47531)
so_gencnt: 2920221 t_state: FIN_WAIT_1 process: Nexy:35344 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	20:19:17.736988-0500	Nexy	networkd_settings_read_from_file initialized networkd settings by reading plist directly
default	20:19:17.737162-0500	Nexy	networkd_settings_read_from_file initialized networkd settings by reading plist directly
default	20:19:17.738296-0500	Nexy	nw_path_libinfo_path_check [8A72CF52-DE8D-4AAE-85FA-6ADC8E4DF40A IPv4#3da34e6d:443 tcp, legacy-socket, attribution: developer]
	libinfo check path: <private>
default	20:19:17.738936-0500	kernel	SK[8]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 9BEF2208-BDFE-40F2-A037-6AE9C596FC76 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.58419,dst=<IPv4-redacted>.443,proto=0x06 mask=0x0000003f,hash=0x3441fbf6 tp_proto=0x06"
default	20:19:17.739012-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:58419<-><IPv4-redacted>:443] interface: utun6 (skipped: 47531)
so_gencnt: 2920222 t_state: SYN_SENT process: Nexy:35344 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x9df05a08
default	20:19:17.739658-0500	kernel	tcp connected: [<IPv4-redacted>:58419<-><IPv4-redacted>:443] interface: utun6 (skipped: 47531)
so_gencnt: 2920222 t_state: ESTABLISHED process: Nexy:35344 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x9df05a08
default	20:19:17.952754-0500	Nexy	[0x735af9540] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	20:19:17.953470-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=35344.4, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=35344, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	20:19:17.960252-0500	tccd	AUTHREQ_SUBJECT: msgID=35344.4, subject=com.nexy.assistant,
default	20:19:17.960880-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x92f178300 at /Applications/Nexy.app
default	20:19:17.993375-0500	Nexy	[0x735af9540] invalidated after the last release of the connection object
default	20:19:18.467175-0500	runningboardd	Assertion did invalidate due to timeout: 403-403-159323 (target:[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344])
default	20:19:18.663409-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] Ignoring jetsam update because this process is not memory-managed
default	20:19:18.663445-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] Ignoring suspend because this process is not lifecycle managed
default	20:19:18.663465-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] Ignoring GPU update because this process is not GPU managed
default	20:19:18.663499-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] Ignoring memory limit update because this process is not memory-managed
default	20:19:18.667943-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:19:18.668545-0500	gamepolicyd	Received state update for 35344 (app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>, running-active-NotVisible
default	20:19:18.908448-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(10585)
default	20:19:18.908524-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:10585 called from <private>
default	20:19:18.908533-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:10585 called from <private>
default	20:19:18.908751-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(10584)
default	20:19:18.908771-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:10584 called from <private>
default	20:19:18.908777-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:10584 called from <private>
default	20:19:18.924268-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:10584 called from <private>
default	20:19:18.924300-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:10584 called from <private>
default	20:19:18.924706-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(10584)
default	20:19:18.925730-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(10584)
default	20:19:18.925756-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(10584)
default	20:19:18.925826-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(10584)
default	20:19:18.926141-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(10584)
default	20:19:18.926625-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(10585)
default	20:19:18.926656-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:10585 called from <private>
default	20:19:18.926666-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:10585 called from <private>
default	20:19:18.926949-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:10584 called from <private>
default	20:19:18.927103-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:10584 called from <private>
default	20:19:18.941641-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:10584 called from <private>
default	20:19:18.941673-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:10584 called from <private>
default	20:19:18.943193-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:10584 called from <private>
default	20:19:18.943212-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:10584 called from <private>
default	20:19:18.943334-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(10584)
default	20:19:18.949052-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(10584)
default	20:19:18.949599-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:10584 called from <private>
default	20:19:18.949611-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:10584 called from <private>
default	20:19:18.949779-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(10584)
default	20:19:18.953720-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(10584)
default	20:19:18.953943-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:10584 called from <private>
default	20:19:18.954117-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:10584 called from <private>
default	20:19:18.954412-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:10584 called from <private>
default	20:19:18.955080-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:10584 called from <private>
default	20:19:18.955288-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:10584 called from <private>
default	20:19:18.955429-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:10584 called from <private>
default	20:19:18.955596-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:10584 called from <private>
default	20:19:18.955718-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:10584 called from <private>
default	20:19:18.955853-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:10584 called from <private>
default	20:19:18.956058-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:10584 called from <private>
default	20:19:18.956233-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:10584 called from <private>
default	20:19:18.956377-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:10584 called from <private>
default	20:19:18.956478-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:10584 called from <private>
default	20:19:18.956584-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:10584 called from <private>
default	20:19:18.956679-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:10584 called from <private>
default	20:19:18.956737-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:10584 called from <private>
default	20:19:18.956763-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:10584 called from <private>
default	20:19:18.956794-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:10584 called from <private>
default	20:19:18.956842-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:10584 called from <private>
default	20:19:18.956870-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:10584 called from <private>
default	20:19:18.966382-0500	Nexy	[0x735af97c0] activating connection: mach=true listener=false peer=false name=com.apple.usernoted.client
default	20:19:18.988703-0500	distnoted	register name: com.apple.nsquiet_safe_quit_give_reason object: com.nexy.assistant token: 2300000021 pid: 35344
default	20:19:19.001859-0500	Nexy	NSApp cache appearance:
-NSRequiresAquaSystemAppearance: 0
-appearance: (null)
-effectiveAppearance: <NSCompositeAppearance: 0x7349786e0
 (
    "<NSDarkAquaAppearance: 0x7349788c0>",
    "<NSSystemAppearance: 0x734978780>"
)>
default	20:19:19.008840-0500	Nexy	[0x735af9cc0] activating connection: mach=true listener=false peer=false name=com.apple.dock.fullscreen
default	20:19:19.011023-0500	Nexy	[0x735af9e00] activating connection: mach=true listener=false peer=false name=com.apple.fonts
default	20:19:19.014324-0500	Nexy	(<private>) deleteSearchableItemsWithDomainIdentifiers, protectionClass:(null), domainIdentifiers number:1
default	20:19:19.014653-0500	Nexy	sConnectionName: com.apple.spotlight.IndexAgent
default	20:19:19.014664-0500	Nexy	Start service name com.apple.spotlight.IndexAgent
default	20:19:19.014699-0500	Nexy	[0x735af9f40] activating connection: mach=true listener=false peer=false name=com.apple.spotlight.IndexAgent
default	20:19:19.014750-0500	Nexy	[C:1] Alloc com.apple.controlcenter.statusitems
default	20:19:19.014823-0500	Nexy	[0x735afa080] activating connection: mach=false listener=false peer=false name=(anonymous)
default	20:19:19.014895-0500	Nexy	FBSWorkspace registering source: <private>
default	20:19:19.015804-0500	suggestd	SGDSpotlightReceiver: deleting 1 domain identifiers (1 after removing overlaps) for com.nexy.assistant: <private>
default	20:19:19.016439-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	20:19:19.016541-0500	Nexy	<FBSWorkspaceScenesClient:0x73497a3a0 <private>> attempting immediate handshake from activate
default	20:19:19.016592-0500	Nexy	<FBSWorkspaceScenesClient:0x73497a3a0 <private>> sent handshake
default	20:19:19.016727-0500	Nexy	Realizing settings extension __NSStatusItemSceneHostSettings__ on FBSSceneSettings
default	20:19:19.017272-0500	Nexy	Realizing settings extension __NSStatusItemSceneClientSettings__ on FBSSceneClientSettings
default	20:19:19.017292-0500	ControlCenter	Asked to bootstrap a new process for handle: [app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344]
default	20:19:19.017324-0500	ControlCenter	Creating process (sync=true) for handle: [app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344]
default	20:19:19.017829-0500	ControlCenter	[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F>:35344] Registering event dispatcher at init
default	20:19:19.018750-0500	Nexy	Realizing settings extension FBSSceneSettingsCore on FBSSceneSettings
default	20:19:19.018754-0500	ControlCenter	Created <FBWorkspace: 0x975594000; <FBApplicationProcess: 0x971d38900; app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F>:35344(v1B3DDD)>>
default	20:19:19.018779-0500	ControlCenter	Bootstrapping app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F> with intent background
default	20:19:19.019191-0500	runningboardd	Launch request for app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>[0] is using uid 501 (divined from auid 501 euid 501)
default	20:19:19.019346-0500	runningboardd	Acquiring assertion targeting app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)> from originator [osservice<com.apple.controlcenter(501)>:642] with description <RBSAssertionDescriptor| "FBApplicationProcess" ID:403-642-159337 target:app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)> attributes:[
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableLPRunReason-Suspend" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableRole-NonUI" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableJetsamPriority-Active" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableBootstrapping" sourceEnvironment:"(null)">
	]>
default	20:19:19.019519-0500	runningboardd	Assertion 403-642-159337 (target:app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>) will be created as active
default	20:19:19.019556-0500	runningboardd	setting abstract target for <RBSAssertionDescriptor| "FBApplicationProcess" ID:403-642-159337 target:app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)> attributes:[
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableLPRunReason-Suspend" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableRole-NonUI" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableJetsamPriority-Active" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableBootstrapping" sourceEnvironment:"(null)">
	]> to [app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344]
default	20:19:19.019932-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] Ignoring jetsam update because this process is not memory-managed
default	20:19:19.019944-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] Ignoring suspend because this process is not lifecycle managed
default	20:19:19.019956-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] Ignoring GPU update because this process is not GPU managed
default	20:19:19.019973-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] Ignoring memory limit update because this process is not memory-managed
default	20:19:19.020473-0500	Nexy	Realizing settings extension FBSSceneClientSettingsCore on FBSSceneClientSettings
default	20:19:19.021485-0500	Nexy	Requesting scene <FBSScene: 0x73497a760; com.apple.controlcenter:CF336ADA-7E66-44CB-8D20-6275B996AAE4> from com.apple.controlcenter.statusitems
default	20:19:19.025765-0500	Nexy	Realizing settings extension __NSClientHostedViewSceneSettings__ on FBSSceneClientSettings
default	20:19:19.026001-0500	Nexy	Realizing settings extension __NSStatusItemAuxiliaryViewSceneSettings__ on FBSSceneSettings
default	20:19:19.026050-0500	Nexy	Realizing settings extension __NSClientStatusItemAuxiliaryViewSceneSettings__ on FBSSceneClientSettings
default	20:19:19.026325-0500	Nexy	Requesting scene <FBSScene: 0x73497a800; com.apple.controlcenter:CF336ADA-7E66-44CB-8D20-6275B996AAE4-Aux[1]-NSStatusItemView> from com.apple.controlcenter.statusitems
default	20:19:19.026537-0500	Nexy	Request for <FBSScene: 0x73497a800; com.apple.controlcenter:CF336ADA-7E66-44CB-8D20-6275B996AAE4-Aux[1]-NSStatusItemView> complete!
default	20:19:19.027241-0500	ControlCenter	[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F>:35344] Bootstrap success!
default	20:19:19.027792-0500	ControlCenter	[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F>:35344] Setting process visibility to: Background
default	20:19:19.027893-0500	ControlCenter	[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F>:35344] No launch watchdog for this process, dropping initial assertion in 2.0s
default	20:19:19.028513-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] from originator [osservice<com.apple.controlcenter(501)>:642] with description <RBSAssertionDescriptor| "FBWorkspaceDomain: injecting saved endowment" ID:403-642-159338 target:35344 attributes:[
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"WorkspaceEndpointInjection" sourceEnvironment:"(null)">
	]>
default	20:19:19.028599-0500	runningboardd	Assertion 403-642-159338 (target:[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344]) will be created as active
default	20:19:19.028980-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] Ignoring jetsam update because this process is not memory-managed
default	20:19:19.028991-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] Ignoring suspend because this process is not lifecycle managed
default	20:19:19.029001-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] Ignoring GPU update because this process is not GPU managed
default	20:19:19.029020-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] Ignoring memory limit update because this process is not memory-managed
default	20:19:19.037295-0500	Nexy	[com.apple.controlcenter:CF336ADA-7E66-44CB-8D20-6275B996AAE4-Aux[1]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
default	20:19:19.037314-0500	Nexy	[com.apple.controlcenter:CF336ADA-7E66-44CB-8D20-6275B996AAE4-Aux[1]-NSStatusItemView] Dropping transition context because the scene is reconnecting
default	20:19:19.041639-0500	ControlCenter	Asked to bootstrap a new process for handle: [app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344]
default	20:19:19.041686-0500	ControlCenter	A process already exists for this handle: <FBApplicationProcess: 0x971d38900; app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F>:35344(v1B3DDD)>
default	20:19:19.041949-0500	ControlCenter	[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F>:35344] Registered new scene: <FBWorkspaceScene: 0x97447db00; com.apple.controlcenter:CF336ADA-7E66-44CB-8D20-6275B996AAE4> (fromRemnant = 0)
default	20:19:19.041992-0500	ControlCenter	[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F>:35344] Workspace interruption policy did change: reconnect
default	20:19:19.042258-0500	Nexy	Request for <FBSScene: 0x73497a760; com.apple.controlcenter:CF336ADA-7E66-44CB-8D20-6275B996AAE4> complete!
default	20:19:19.042260-0500	ControlCenter	[com.apple.controlcenter:CF336ADA-7E66-44CB-8D20-6275B996AAE4] Client process connected: [app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344]
default	20:19:19.042370-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] from originator [osservice<com.apple.controlcenter(501)>:642] with description <RBSAssertionDescriptor| "com.apple.frontboard.after-life.interrupted" ID:403-642-159339 target:35344 attributes:[
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"AfterLife-Interrupted" sourceEnvironment:"(null)">
	]>
default	20:19:19.042474-0500	runningboardd	Assertion 403-642-159339 (target:[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344]) will be created as inactive as originator process has not exited
default	20:19:19.042570-0500	Nexy	[com.apple.controlcenter:CF336ADA-7E66-44CB-8D20-6275B996AAE4-Aux[1]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
default	20:19:19.042589-0500	Nexy	[com.apple.controlcenter:CF336ADA-7E66-44CB-8D20-6275B996AAE4-Aux[1]-NSStatusItemView] Dropping transition context because the scene is reconnecting
default	20:19:19.042691-0500	Nexy	Warning: the app is using `-[NSStatusBarButton setHighlightsBy:]` to set the highlight behavior. Instead, consider removing that setting. That will enable macOS to highlight the status bar button as appropriate for all configurations (e.g., light, dark, and increased contrast modes).
default	20:19:19.042938-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] from originator [osservice<com.apple.controlcenter(501)>:642] with description <RBSAssertionDescriptor| "FBWorkspace (BG-Active[40])" ID:403-642-159340 target:35344 attributes:[
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableLPRunReason-Suspend" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableRole-NonUI" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableJetsamPriority-Active" sourceEnvironment:"(null)">
	]>
default	20:19:19.043060-0500	runningboardd	Assertion 403-642-159340 (target:[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344]) will be created as active
default	20:19:19.043404-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] Ignoring jetsam update because this process is not memory-managed
default	20:19:19.043436-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] Ignoring suspend because this process is not lifecycle managed
default	20:19:19.043510-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] Ignoring GPU update because this process is not GPU managed
default	20:19:19.043174-0500	ControlCenter	[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F>:35344] Workspace state did change: XX-None[0] --> BG-Active[40] (assertion acquired).
default	20:19:19.043584-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] Ignoring memory limit update because this process is not memory-managed
default	20:19:19.043859-0500	Nexy	<FBSWorkspaceScenesClient:0x73497a3a0 <private>> Reconnecting scene com.apple.controlcenter:CF336ADA-7E66-44CB-8D20-6275B996AAE4
default	20:19:19.044329-0500	Nexy	Request for <FBSScene: 0x73497a800; com.apple.controlcenter:CF336ADA-7E66-44CB-8D20-6275B996AAE4-Aux[1]-NSStatusItemView> complete!
default	20:19:19.044023-0500	ControlCenter	Asked to bootstrap a new process for handle: [app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344]
default	20:19:19.044043-0500	ControlCenter	A process already exists for this handle: <FBApplicationProcess: 0x971d38900; app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F>:35344(v1B3DDD)>
default	20:19:19.044120-0500	ControlCenter	[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F>:35344] Registered new scene: <FBWorkspaceScene: 0x97447e280; com.apple.controlcenter:CF336ADA-7E66-44CB-8D20-6275B996AAE4-Aux[1]-NSStatusItemView> (fromRemnant = 0)
default	20:19:19.044342-0500	ControlCenter	[com.apple.controlcenter:CF336ADA-7E66-44CB-8D20-6275B996AAE4-Aux[1]-NSStatusItemView] Client process connected: [app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344]
default	20:19:19.044832-0500	Nexy	<FBSWorkspaceScenesClient:0x73497a3a0 <private>> Reconnecting scene com.apple.controlcenter:CF336ADA-7E66-44CB-8D20-6275B996AAE4-Aux[1]-NSStatusItemView
default	20:19:19.046807-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:19:19.047324-0500	ControlCenter	Received state update for 35344 (app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>, running-active-NotVisible
default	20:19:19.047573-0500	gamepolicyd	Received state update for 35344 (app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>, running-active-NotVisible
default	20:19:19.059451-0500	Nexy	Registering for test daemon availability notify post.
default	20:19:19.059621-0500	Nexy	notify_get_state check indicated test daemon not ready.
default	20:19:19.059735-0500	Nexy	notify_get_state check indicated test daemon not ready.
default	20:19:19.059823-0500	Nexy	notify_get_state check indicated test daemon not ready.
default	20:19:19.062328-0500	Nexy	[0x735afa440] activating connection: mach=true listener=false peer=false name=com.apple.coreservices.appleevents
default	20:19:19.065609-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x92f178600 at /Applications/Nexy.app
default	20:19:19.070837-0500	Nexy	[0x735af83c0] Connection returned listener port: 0x4703
default	20:19:19.071374-0500	Nexy	SignalReady: pid=35344 asn=0x0-0x3d63d6
default	20:19:19.071890-0500	Nexy	SIGNAL: pid=35344 asn=0x0x-0x3d63d6
default	20:19:19.072666-0500	loginwindow	-[Application updateInformation] | Got App URL: file:///Applications/Nexy.app/
default	20:19:19.083267-0500	Nexy	[com.apple.controlcenter:CF336ADA-7E66-44CB-8D20-6275B996AAE4-Aux[1]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
default	20:19:19.086083-0500	Nexy	[com.apple.controlcenter:CF336ADA-7E66-44CB-8D20-6275B996AAE4-Aux[1]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
default	20:19:19.087852-0500	Nexy	void _NSDisableAutomaticTerminationAndLog(NSString *) Restoring windows
default	20:19:19.087861-0500	Nexy	-[NSApplication _reopenWindowsAsNecessaryIncludingRestorableState:withFullFidelity:completionHandler:] shouldRestoreState=1 hasPersistentStateToRestore=0 shouldStillRestoreStateAfterPrompting=0
default	20:19:19.087913-0500	Nexy	[0x735af9400] activating connection: mach=true listener=false peer=false name=com.apple.window_proxies
default	20:19:19.088001-0500	Nexy	[0x735af9400] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	20:19:19.088990-0500	Nexy	void _NSEnableAutomaticTerminationAndLog(NSString *) Restoring windows
default	20:19:19.091964-0500	ControlCenter	Host properties initialized; (bid:com.nexy.assistant-Item-0-35344). State(applicationItem: true, clientRequestsVisibility: true, neverClip: false)
default	20:19:19.092777-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] from originator [app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] with description <RBSAssertionDescriptor| "AudioHAL" ID:403-35344-159341 target:35344 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	20:19:19.092847-0500	runningboardd	Assertion 403-35344-159341 (target:[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344]) will be created as active
default	20:19:19.093103-0500	ControlCenter	Starting to track host; (bid:com.nexy.assistant-Item-0-35344)
default	20:19:19.093219-0500	runningboardd	Invalidating assertion 403-35344-159341 (target:[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344]) from originator [app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344]
default	20:19:19.093261-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] Ignoring jetsam update because this process is not memory-managed
default	20:19:19.093280-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] Ignoring suspend because this process is not lifecycle managed
default	20:19:19.093336-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] Ignoring GPU update because this process is not GPU managed
default	20:19:19.093410-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] from originator [app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] with description <RBSAssertionDescriptor| "AudioHAL" ID:403-35344-159342 target:35344 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	20:19:19.093449-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] Ignoring memory limit update because this process is not memory-managed
default	20:19:19.093487-0500	runningboardd	Assertion 403-35344-159342 (target:[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344]) will be created as active
default	20:19:19.093677-0500	ControlCenter	Created new displayable type DisplayableAppStatusItemType(9790B666, (bid:com.nexy.assistant-Item-0-35344)) for (bid:com.nexy.assistant-Item-0-35344)
default	20:19:19.095350-0500	ControlCenter	Adding displayable items for status items; [(bid:com.nexy.assistant-Item-0-35344)]
default	20:19:19.096112-0500	ControlCenter	Created instance DisplayableId(3566556F) in .menuBar for DisplayableAppStatusItemType(9790B666, (bid:com.nexy.assistant-Item-0-35344)) .menuBar
default	20:19:19.096642-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:19:19.096894-0500	runningboardd	Invalidating assertion 403-35344-159342 (target:[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344]) from originator [app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344]
default	20:19:19.097248-0500	gamepolicyd	Received state update for 35344 (app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>, running-active-NotVisible
default	20:19:19.097107-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] from originator [app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] with description <RBSAssertionDescriptor| "AudioHAL" ID:403-35344-159343 target:35344 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	20:19:19.097197-0500	runningboardd	Assertion 403-35344-159343 (target:[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344]) will be created as active
default	20:19:19.097203-0500	ControlCenter	Received state update for 35344 (app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>, running-active-NotVisible
default	20:19:19.097716-0500	runningboardd	Invalidating assertion 403-35344-159343 (target:[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344]) from originator [app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344]
default	20:19:19.097821-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] from originator [app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] with description <RBSAssertionDescriptor| "AudioHAL" ID:403-35344-159344 target:35344 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	20:19:19.097861-0500	runningboardd	Assertion 403-35344-159344 (target:[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344]) will be created as active
default	20:19:19.098088-0500	runningboardd	Invalidating assertion 403-35344-159344 (target:[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344]) from originator [app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344]
default	20:19:19.098668-0500	Nexy	[com.apple.controlcenter:CF336ADA-7E66-44CB-8D20-6275B996AAE4-Aux[1]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
default	20:19:19.099288-0500	Nexy	[com.apple.controlcenter:CF336ADA-7E66-44CB-8D20-6275B996AAE4] Sending action(s) in update: NSSceneFenceAction
default	20:19:19.101959-0500	ControlCenter	Created ephemaral instance DisplayableId(3566556F) for (bid:com.nexy.assistant-Item-0-35344) with positioning .ephemeral
default	20:19:19.108223-0500	Nexy	[C:2] Alloc <private>
default	20:19:19.108258-0500	Nexy	[0x735af9400] activating connection: mach=false listener=false peer=false name=(anonymous)
default	20:19:19.109021-0500	Nexy	[com.apple.controlcenter:CF336ADA-7E66-44CB-8D20-6275B996AAE4-Aux[1]-NSStatusItemView] Received action(s) in scene-update: NSSceneFenceAction
default	20:19:19.110004-0500	WindowManager	Connection activated | (35344) Nexy
default	20:19:19.110394-0500	Nexy	[com.apple.controlcenter:CF336ADA-7E66-44CB-8D20-6275B996AAE4-Aux[1]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
default	20:19:19.113789-0500	Nexy	[com.apple.controlcenter:CF336ADA-7E66-44CB-8D20-6275B996AAE4-Aux[1]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
default	20:19:19.114193-0500	Nexy	[com.apple.controlcenter:CF336ADA-7E66-44CB-8D20-6275B996AAE4] Sending action(s) in update: NSSceneFenceAction
default	20:19:19.198805-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] Ignoring jetsam update because this process is not memory-managed
default	20:19:19.198818-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] Ignoring suspend because this process is not lifecycle managed
default	20:19:19.198828-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] Ignoring GPU update because this process is not GPU managed
default	20:19:19.198847-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] Ignoring memory limit update because this process is not memory-managed
default	20:19:19.202104-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:19:19.202644-0500	ControlCenter	Received state update for 35344 (app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>, running-active-NotVisible
default	20:19:19.202692-0500	gamepolicyd	Received state update for 35344 (app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>, running-active-NotVisible
default	20:19:19.204514-0500	Nexy	*warn* MailCS ======%%% _setMailMessageAttributes skip:1
default	20:19:19.209346-0500	Nexy	Start service name com.apple.spotlightknowledged
default	20:19:19.210069-0500	Nexy	[GMS] availability notification token 86
default	20:19:19.318334-0500	ControlCenter	[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F>:35344] Workspace state did change: BG-Active[40] --> XX-None[0] (assertion dropped).
default	20:19:19.318480-0500	runningboardd	Invalidating assertion 403-642-159340 (target:[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344]) from originator [osservice<com.apple.controlcenter(501)>:642]
default	20:19:19.423005-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] Ignoring jetsam update because this process is not memory-managed
default	20:19:19.423018-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] Ignoring suspend because this process is not lifecycle managed
default	20:19:19.423027-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] Ignoring GPU update because this process is not GPU managed
default	20:19:19.423046-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] Ignoring memory limit update because this process is not memory-managed
default	20:19:19.426198-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:19:19.426698-0500	ControlCenter	Received state update for 35344 (app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>, running-active-NotVisible
default	20:19:19.426839-0500	gamepolicyd	Received state update for 35344 (app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>, running-active-NotVisible
default	20:19:19.599126-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] from originator [osservice<com.apple.WindowServer(88)>:397] with description <RBSAssertionDescriptor| "AppDrawing" ID:403-397-159346 target:35344 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"AppDrawing" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	20:19:19.599215-0500	runningboardd	Assertion 403-397-159346 (target:[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344]) will be created as active
default	20:19:19.599602-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] Ignoring jetsam update because this process is not memory-managed
default	20:19:19.599616-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] Ignoring suspend because this process is not lifecycle managed
default	20:19:19.599636-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] Ignoring GPU update because this process is not GPU managed
default	20:19:19.599658-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] Ignoring memory limit update because this process is not memory-managed
default	20:19:19.602880-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:19:19.603252-0500	ControlCenter	Received state update for 35344 (app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>, running-active-NotVisible
default	20:19:19.603365-0500	gamepolicyd	Received state update for 35344 (app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>, running-active-NotVisible
default	20:19:21.127381-0500	runningboardd	Invalidating assertion 403-642-159337 (target:app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>) from originator [osservice<com.apple.controlcenter(501)>:642]
default	20:19:21.234163-0500	runningboardd	Removed last relative-start-date-defining assertion for process app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>
default	20:19:21.235483-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] Ignoring jetsam update because this process is not memory-managed
default	20:19:21.235515-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] Ignoring suspend because this process is not lifecycle managed
default	20:19:21.235538-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] Ignoring GPU update because this process is not GPU managed
default	20:19:21.235585-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] Ignoring memory limit update because this process is not memory-managed
default	20:19:21.240200-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:19:21.245692-0500	ControlCenter	Received state update for 35344 (app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>, running-active-NotVisible
default	20:19:21.245948-0500	gamepolicyd	Received state update for 35344 (app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>, running-active-NotVisible
default	20:19:23.792593-0500	Nexy	NotifyToken::RegisterDispatch(user.uid.501.com.apple.LaunchServices.database) fired for session key <private>
default	20:19:23.990365-0500	Nexy	void _updateToReflectAutomaticTerminationState(void) Setting _kLSApplicationWouldBeTerminatedByTALKey=1
default	20:19:29.960520-0500	Nexy	LSExceptions shared instance invalidated for timeout.
default	20:19:30.907008-0500	Nexy	                AUHAL.cpp:420   AUHAL: (0x737103140) Selecting device 85 from constructor
default	20:19:30.907032-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0x737103140)
default	20:19:30.907042-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0x737103140) not already running
default	20:19:30.907051-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0x737103140) nothing to teardown
default	20:19:30.907057-0500	Nexy	                AUHAL.cpp:762   SelectDevice: (0x737103140) connecting device 85
default	20:19:30.907222-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0x737103140) Device ID: 85 (Input:No | Output:Yes): true
default	20:19:30.907406-0500	Nexy	                AUHAL.cpp:774   SelectDevice: (0x737103140) created ioproc 0xb for device 85
default	20:19:30.907592-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x737103140) adding 7 device listeners to device 85
default	20:19:30.907875-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x737103140) adding 0 device delegate listeners to device 85
default	20:19:30.907890-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x737103140)
default	20:19:30.908004-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  48000 Hz, Float32, interleaved
default	20:19:30.908020-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	20:19:30.908030-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	20:19:30.908042-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	20:19:30.908057-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	20:19:30.908219-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x737103140) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	20:19:30.908236-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x737103140) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	20:19:30.908245-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	20:19:30.908252-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x737103140) removing 0 device listeners from device 0
default	20:19:30.908257-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x737103140) removing 0 device delegate listeners from device 0
default	20:19:30.908265-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0x737103140)
default	20:19:30.908292-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is DISABLED
default	20:19:30.908396-0500	Nexy	                AUHAL.cpp:2303  SetProperty: (0x737103140) caller requesting device change from 85 to 91
default	20:19:30.908409-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0x737103140)
default	20:19:30.908416-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0x737103140) not already running
default	20:19:30.908423-0500	Nexy	                AUHAL.cpp:687   SelectDevice: (0x737103140) disconnecting device 85
default	20:19:30.908448-0500	Nexy	                AUHAL.cpp:751   SelectDevice: (0x737103140) destroying ioproc 0xb for device 85
default	20:19:30.908478-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped Unknown {1C-77-54-18-C8-A3:output, 0xb}
default	20:19:30.908590-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	20:19:30.908726-0500	Nexy	                AUHAL.cpp:762   SelectDevice: (0x737103140) connecting device 91
default	20:19:30.908869-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0x737103140) Device ID: 91 (Input:Yes | Output:No): true
default	20:19:30.911443-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=411.1583, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=35344, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=398, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	20:19:30.915555-0500	tccd	AUTHREQ_SUBJECT: msgID=411.1583, subject=com.nexy.assistant,
default	20:19:30.916829-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc79244000 at /Applications/Nexy.app
default	20:19:30.941627-0500	Nexy	                AUHAL.cpp:774   SelectDevice: (0x737103140) created ioproc 0xb for device 91
default	20:19:30.941818-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x737103140) adding 7 device listeners to device 91
default	20:19:30.942004-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x737103140) adding 0 device delegate listeners to device 91
default	20:19:30.942020-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x737103140)
default	20:19:30.942034-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 output streams; not all mono
default	20:19:30.942049-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	20:19:30.942230-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  input stream 0 [0x5c]:  1 ch,  24000 Hz, Float32
default	20:19:30.942239-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 input streams; all mono
default	20:19:30.942245-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  1 ch,  24000 Hz, Float32
default	20:19:30.942363-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x737103140) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	20:19:30.942379-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x737103140) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	20:19:30.942387-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	20:19:30.942392-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x737103140) removing 7 device listeners from device 85
default	20:19:30.942574-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x737103140) removing 0 device delegate listeners from device 85
default	20:19:30.942584-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0x737103140)
default	20:19:30.943188-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	20:19:30.944466-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=411.1584, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=35344, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=398, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	20:19:30.945550-0500	tccd	AUTHREQ_SUBJECT: msgID=411.1584, subject=com.nexy.assistant,
default	20:19:30.946182-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc79244000 at /Applications/Nexy.app
default	20:19:30.974643-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	20:19:30.975555-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=411.1585, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=35344, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=398, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	20:19:30.976380-0500	tccd	AUTHREQ_SUBJECT: msgID=411.1585, subject=com.nexy.assistant,
default	20:19:30.976938-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc79244000 at /Applications/Nexy.app
default	20:19:31.006809-0500	Nexy	                AUHAL.cpp:473   ~AUHAL: (0x737103140) Selecting device 0 from destructor
default	20:19:31.006817-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0x737103140)
default	20:19:31.006823-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0x737103140) not already running
default	20:19:31.006827-0500	Nexy	                AUHAL.cpp:687   SelectDevice: (0x737103140) disconnecting device 91
default	20:19:31.006830-0500	Nexy	                AUHAL.cpp:751   SelectDevice: (0x737103140) destroying ioproc 0xb for device 91
default	20:19:31.006859-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xb}
default	20:19:31.006889-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	20:19:31.006987-0500	Nexy	                AUHAL.cpp:853   SelectDevice: (0x737103140) nothing to setup
default	20:19:31.006994-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x737103140) adding 0 device listeners to device 0
default	20:19:31.006999-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x737103140) adding 0 device delegate listeners to device 0
default	20:19:31.007004-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x737103140) removing 7 device listeners from device 91
default	20:19:31.007150-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x737103140) removing 0 device delegate listeners from device 91
default	20:19:31.007160-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0x737103140)
default	20:19:31.008086-0500	Nexy	                AUHAL.cpp:420   AUHAL: (0x737103140) Selecting device 85 from constructor
default	20:19:31.008101-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0x737103140)
default	20:19:31.008110-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0x737103140) not already running
default	20:19:31.008115-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0x737103140) nothing to teardown
default	20:19:31.008119-0500	Nexy	                AUHAL.cpp:762   SelectDevice: (0x737103140) connecting device 85
default	20:19:31.008212-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0x737103140) Device ID: 85 (Input:No | Output:Yes): true
default	20:19:31.008304-0500	Nexy	                AUHAL.cpp:774   SelectDevice: (0x737103140) created ioproc 0xc for device 85
default	20:19:31.008388-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x737103140) adding 7 device listeners to device 85
default	20:19:31.008547-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x737103140) adding 0 device delegate listeners to device 85
default	20:19:31.008553-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x737103140)
default	20:19:31.008619-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  48000 Hz, Float32, interleaved
default	20:19:31.008626-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	20:19:31.008635-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	20:19:31.008640-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	20:19:31.008647-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	20:19:31.008749-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x737103140) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	20:19:31.008763-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x737103140) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	20:19:31.008768-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	20:19:31.008771-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x737103140) removing 0 device listeners from device 0
default	20:19:31.008775-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x737103140) removing 0 device delegate listeners from device 0
default	20:19:31.008780-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0x737103140)
default	20:19:31.008790-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is DISABLED
default	20:19:31.008838-0500	Nexy	                AUHAL.cpp:2303  SetProperty: (0x737103140) caller requesting device change from 85 to 91
default	20:19:31.008845-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0x737103140)
default	20:19:31.008850-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0x737103140) not already running
default	20:19:31.008853-0500	Nexy	                AUHAL.cpp:687   SelectDevice: (0x737103140) disconnecting device 85
default	20:19:31.008858-0500	Nexy	                AUHAL.cpp:751   SelectDevice: (0x737103140) destroying ioproc 0xc for device 85
default	20:19:31.008868-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped Unknown {1C-77-54-18-C8-A3:output, 0xc}
default	20:19:31.008888-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	20:19:31.008965-0500	Nexy	                AUHAL.cpp:762   SelectDevice: (0x737103140) connecting device 91
default	20:19:31.009035-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0x737103140) Device ID: 91 (Input:Yes | Output:No): true
default	20:19:31.010088-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=411.1586, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=35344, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=398, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	20:19:31.011075-0500	tccd	AUTHREQ_SUBJECT: msgID=411.1586, subject=com.nexy.assistant,
default	20:19:31.011682-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc79244000 at /Applications/Nexy.app
default	20:19:31.041018-0500	Nexy	                AUHAL.cpp:774   SelectDevice: (0x737103140) created ioproc 0xc for device 91
default	20:19:31.041158-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x737103140) adding 7 device listeners to device 91
default	20:19:31.041320-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x737103140) adding 0 device delegate listeners to device 91
default	20:19:31.041332-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x737103140)
default	20:19:31.041340-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 output streams; not all mono
default	20:19:31.041349-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	20:19:31.041471-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  input stream 0 [0x5c]:  1 ch,  24000 Hz, Float32
default	20:19:31.041481-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 input streams; all mono
default	20:19:31.041487-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  1 ch,  24000 Hz, Float32
default	20:19:31.041575-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x737103140) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	20:19:31.041590-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x737103140) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	20:19:31.041596-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	20:19:31.041600-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x737103140) removing 7 device listeners from device 85
default	20:19:31.041769-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x737103140) removing 0 device delegate listeners from device 85
default	20:19:31.041779-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0x737103140)
default	20:19:31.041790-0500	Nexy	AudioHardware-mac-imp.cpp:1306   AudioObjectAddPropertyListener: listener was already added
default	20:19:31.042325-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	20:19:31.043376-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=411.1587, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=35344, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=398, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	20:19:31.044276-0500	tccd	AUTHREQ_SUBJECT: msgID=411.1587, subject=com.nexy.assistant,
default	20:19:31.044841-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc79244000 at /Applications/Nexy.app
default	20:19:31.075382-0500	Nexy	       ACv2Workarounds.mm:51    com.nexy.assistant: fix84702776_86723525_86479548_89800354_SinglePacketDesc: false
default	20:19:31.075457-0500	Nexy	       AudioConverter.cpp:1044  Created a new in process converter -> 0x7372544e0, from  1 ch,  24000 Hz, Float32 to  1 ch,  48000 Hz, Float32
default	20:19:31.075664-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	20:19:31.076569-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=411.1588, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=35344, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=398, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	20:19:31.077408-0500	tccd	AUTHREQ_SUBJECT: msgID=411.1588, subject=com.nexy.assistant,
default	20:19:31.077941-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc79244000 at /Applications/Nexy.app
default	20:19:31.108979-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] from originator [app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] with description <RBSAssertionDescriptor| "AudioHAL" ID:403-35344-159355 target:35344 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	20:19:31.109069-0500	runningboardd	Assertion 403-35344-159355 (target:[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344]) will be created as active
default	20:19:31.109462-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] Ignoring jetsam update because this process is not memory-managed
default	20:19:31.109477-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] Ignoring suspend because this process is not lifecycle managed
default	20:19:31.109486-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] Ignoring GPU update because this process is not GPU managed
default	20:19:31.109505-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] Ignoring memory limit update because this process is not memory-managed
default	20:19:31.109671-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=411.1589, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=35344, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=398, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	20:19:31.110558-0500	tccd	AUTHREQ_SUBJECT: msgID=411.1589, subject=com.nexy.assistant,
default	20:19:31.111160-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc79244000 at /Applications/Nexy.app
default	20:19:31.112476-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:19:31.113034-0500	ControlCenter	Received state update for 35344 (app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>, running-active-NotVisible
default	20:19:31.113152-0500	gamepolicyd	Received state update for 35344 (app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>, running-active-NotVisible
default	20:19:31.141974-0500	coreaudiod	>>> NEGOTIATE [com.nexy.assistant]
default	20:19:31.142142-0500	coreaudiod	<<< NEGOTIATE [com.nexy.assistant]
default	20:19:31.144444-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:10585 called from <private>
default	20:19:31.144458-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Input {1C-77-54-18-C8-A3:input, 0xc}
default	20:19:31.144491-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	20:19:31.145462-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:10585 called from <private>
default	20:19:31.145688-0500	runningboardd	Invalidating assertion 403-35344-159355 (target:[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344]) from originator [app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344]
default	20:19:31.145642-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(10585)
default	20:19:31.148421-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] from originator [osservice<com.apple.powerd>:338] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:403-338-159356 target:35344 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	20:19:31.148495-0500	runningboardd	Assertion 403-338-159356 (target:[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344]) will be created as active
default	20:19:31.145664-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:10585 called from <private>
default	20:19:31.151402-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] Ignoring jetsam update because this process is not memory-managed
default	20:19:31.152446-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	20:19:31.151798-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] Ignoring suspend because this process is not lifecycle managed
default	20:19:31.145669-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:10585 called from <private>
default	20:19:31.146112-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(10584)
default	20:19:31.151823-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] Ignoring GPU update because this process is not GPU managed
default	20:19:31.146131-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:10584 called from <private>
default	20:19:31.146136-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:10584 called from <private>
default	20:19:31.152898-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] Ignoring memory limit update because this process is not memory-managed
default	20:19:31.154731-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	20:19:31.155541-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(10585)
default	20:19:31.155582-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(10585)
default	20:19:31.155596-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(10585)
default	20:19:31.155611-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(10585)
default	20:19:31.160335-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:19:31.160777-0500	runningboardd	Invalidating assertion 403-338-159356 (target:[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344]) from originator [osservice<com.apple.powerd>:338]
default	20:19:31.160913-0500	ControlCenter	Received state update for 35344 (app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>, running-active-NotVisible
default	20:19:31.161747-0500	gamepolicyd	Received state update for 35344 (app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>, running-active-NotVisible
default	20:19:31.164666-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	20:19:31.164799-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	20:19:31.164890-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:10585 called from <private>
default	20:19:31.164906-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:10585 called from <private>
default	20:19:31.164920-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:10585 called from <private>
default	20:19:31.164930-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:10585 called from <private>
default	20:19:31.164937-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:10585 called from <private>
default	20:19:31.164858-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	20:19:31.164941-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:10585 called from <private>
default	20:19:31.164947-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:10585 called from <private>
default	20:19:31.165343-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	20:19:31.166438-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:19:31.166450-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:19:31.166472-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:19:31.166479-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:19:31.166486-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:19:31.166491-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	20:19:31.166625-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	20:19:31.166996-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:19:31.167010-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:19:31.167081-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:19:31.167299-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:19:31.167346-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:19:31.167357-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	20:19:31.167618-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	20:19:31.169092-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] from originator [app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] with description <RBSAssertionDescriptor| "AudioHAL" ID:403-35344-159357 target:35344 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	20:19:31.168540-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(10585)
default	20:19:31.169228-0500	runningboardd	Assertion 403-35344-159357 (target:[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344]) will be created as active
default	20:19:31.169971-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1e804b","name":"Nexy(35344)"}, "details":{"deviceUIDs":["1C-77-54-18-C8-A3:input"],"implicit_category":"Record","input_running":true,"output_running":false} }
default	20:19:31.169321-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(10584)
default	20:19:31.170130-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 76, PID = 35344, Name = sid:0x1e804b, Nexy(35344), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	20:19:31.170185-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Category/Mode changed -- The score for sid:0x1e804b, Nexy(35344), 'prim'/com.nexy.assistant was not correct. Old score = 201
default	20:19:31.170810-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=411.1590, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=35344, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=398, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	20:19:31.170284-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 76, PID = 35344, Name = sid:0x1e804b, Nexy(35344), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	20:19:31.171515-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 76, PID = 35344, Name = sid:0x1e804b, Nexy(35344), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	20:19:31.172080-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 76, PID = 35344, Name = sid:0x1e804b, Nexy(35344), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	20:19:31.170636-0500	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1e804b, Nexy(35344), 'prim'', AudioCategory changed to 'Record_WithBluetooth'
default	20:19:31.172436-0500	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 76, PID = 35344, Name = sid:0x1e804b, Nexy(35344), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> is going active
default	20:19:31.172468-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1e804b, Nexy(35344), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 76 starting recording
default	20:19:31.172740-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 76, PID = 35344, Name = sid:0x1e804b, Nexy(35344), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	20:19:31.172909-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 76, PID = 35344, Name = sid:0x1e804b, Nexy(35344), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	20:19:31.173221-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [1, 0]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:input"
)}
default	20:19:31.173089-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1e804b, Nexy(35344), 'prim'', displayID:'com.nexy.assistant'}
default	20:19:31.173253-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	20:19:31.174086-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	20:19:31.174840-0500	tccd	AUTHREQ_SUBJECT: msgID=411.1590, subject=com.nexy.assistant,
default	20:19:31.175765-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc79244000 at /Applications/Nexy.app
default	20:19:31.181376-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:10584 called from <private>
default	20:19:31.181390-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:10584 called from <private>
default	20:19:31.182950-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:10584 called from <private>
default	20:19:31.182970-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:10584 called from <private>
default	20:19:31.183067-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(10584)
default	20:19:31.190427-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(10584)
default	20:19:31.190948-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:10584 called from <private>
default	20:19:31.190959-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:10584 called from <private>
default	20:19:31.191063-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(10584)
default	20:19:31.194806-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(10584)
default	20:19:31.195574-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:10584 called from <private>
default	20:19:31.195584-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:10584 called from <private>
default	20:19:31.195619-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:10584 called from <private>
default	20:19:31.195626-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:10584 called from <private>
default	20:19:31.195632-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:10584 called from <private>
default	20:19:31.195637-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:10584 called from <private>
default	20:19:31.196114-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:10584 called from <private>
default	20:19:31.196229-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:10584 called from <private>
default	20:19:31.196365-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:10584 called from <private>
default	20:19:31.196538-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:10584 called from <private>
default	20:19:31.196686-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:10584 called from <private>
default	20:19:31.196834-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:10584 called from <private>
default	20:19:31.197035-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:10584 called from <private>
default	20:19:31.197268-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:10584 called from <private>
default	20:19:31.197669-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(10584)
default	20:19:31.197822-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:10584 called from <private>
default	20:19:31.198061-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:10584 called from <private>
default	20:19:31.203335-0500	audiomxd	UpdateAudioState CID 0x4D120001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:19:31.201499-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:10584 called from <private>
default	20:19:31.203473-0500	audiomxd	UpdateAudioState CID 0x4D120001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:19:31.203671-0500	audiomxd	UpdateAudioState CID 0x4D120001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	20:19:31.206733-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	20:19:31.220583-0500	coreaudiod	>>> NEGOTIATE [com.nexy.assistant]
default	20:19:31.220760-0500	coreaudiod	<<< NEGOTIATE [com.nexy.assistant]
default	20:19:31.229162-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] from originator [app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] with description <RBSAssertionDescriptor| "AudioHAL" ID:403-35344-159359 target:35344 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	20:19:31.229212-0500	runningboardd	Assertion 403-35344-159359 (target:[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344]) will be created as active
default	20:19:31.229614-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=411.1591, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=35344, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=398, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	20:19:31.252259-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] Ignoring jetsam update because this process is not memory-managed
default	20:19:31.252276-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] Ignoring suspend because this process is not lifecycle managed
default	20:19:31.252290-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] Ignoring GPU update because this process is not GPU managed
default	20:19:31.252315-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] Ignoring memory limit update because this process is not memory-managed
default	20:19:31.254841-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:19:31.255117-0500	ControlCenter	Received state update for 35344 (app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>, running-active-NotVisible
default	20:19:31.255290-0500	gamepolicyd	Received state update for 35344 (app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>, running-active-NotVisible
default	20:19:31.263719-0500	coreaudiod	>>> ADAPT [com.nexy.assistant]
default	20:19:31.264849-0500	coreaudiod	IssueReporting.cpp:492   RTAID [ use_case=Generic report_type=RMS Generic Chain clientID=ADM node=ADM::com.nexy.assistant_10585.10484.0_airpods noise suppression studio::out-0 issue_detected_sample_time=24480.000000 ] -- [ rms:[-28.937771], peaks:[-8.524359] ]
default	20:19:31.264868-0500	coreaudiod	IssueReporting.cpp:492   RTAID [ use_case=Generic report_type=RMS Generic Chain clientID=ADM node=ADM::com.nexy.assistant_10585.10484.0_airpods noise suppression studio::in-0 issue_detected_sample_time=0.000000 ] -- [ rms:[-33.169281], peaks:[-16.301252] ]
default	20:19:31.265090-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xa380ea700] Created node ADM::com.nexy.assistant_10585.10484.0_airpods noise suppression studio::in-0 with nodeID 0 - reporting period = 10.000000, sample rate = 24000.000000
default	20:19:31.265147-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xa380ea700] Created node ADM::com.nexy.assistant_10585.10484.0_airpods noise suppression studio::out-0 with nodeID 1 - reporting period = 10.000000, sample rate = 24000.000000
default	20:19:31.298995-0500	coreaudiod	<<< ADAPT [com.nexy.assistant]
default	20:19:31.301266-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:10585 called from <private>
default	20:19:31.302294-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] from originator [osservice<com.apple.powerd>:338] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:403-338-159362 target:35344 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	20:19:31.301342-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:10585 called from <private>
default	20:19:31.302881-0500	runningboardd	Assertion 403-338-159362 (target:[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344]) will be created as active
default	20:19:31.303078-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:10585 called from <private>
default	20:19:31.303178-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	20:19:31.303359-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] Ignoring jetsam update because this process is not memory-managed
default	20:19:31.303556-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] Ignoring suspend because this process is not lifecycle managed
default	20:19:31.303636-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] Ignoring GPU update because this process is not GPU managed
default	20:19:31.303775-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] Ignoring memory limit update because this process is not memory-managed
default	20:19:31.305018-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:10585 called from <private>
default	20:19:31.305171-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(10585)
default	20:19:31.305185-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:10585 called from <private>
default	20:19:31.305191-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:10585 called from <private>
default	20:19:31.305332-0500	runningboardd	Invalidating assertion 403-35344-159359 (target:[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344]) from originator [app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344]
default	20:19:31.306051-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	20:19:31.306235-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	20:19:31.306967-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(10585)
default	20:19:31.307172-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:10585 called from <private>
default	20:19:31.307183-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:10585 called from <private>
default	20:19:31.307199-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:10585 called from <private>
default	20:19:31.307770-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] from originator [app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] with description <RBSAssertionDescriptor| "AudioHAL" ID:403-35344-159363 target:35344 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	20:19:31.307873-0500	runningboardd	Assertion 403-35344-159363 (target:[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344]) will be created as active
default	20:19:31.308706-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=411.1592, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=35344, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=398, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	20:19:31.309951-0500	tccd	AUTHREQ_SUBJECT: msgID=411.1592, subject=com.nexy.assistant,
default	20:19:31.311539-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:19:31.311006-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc79244000 at /Applications/Nexy.app
default	20:19:31.312314-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	20:19:31.312377-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	20:19:31.312135-0500	runningboardd	Invalidating assertion 403-338-159362 (target:[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344]) from originator [osservice<com.apple.powerd>:338]
default	20:19:31.312422-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	20:19:31.312529-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	20:19:31.313330-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:19:31.313340-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:19:31.313350-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:19:31.313358-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:19:31.313365-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:19:31.313371-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	20:19:31.313570-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	20:19:31.347079-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] from originator [osservice<com.apple.powerd>:338] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:403-338-159364 target:35344 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	20:19:31.347155-0500	runningboardd	Assertion 403-338-159364 (target:[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344]) will be created as active
default	20:19:31.347588-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:10585 called from <private>
default	20:19:31.353584-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	20:19:31.353641-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	20:19:31.353688-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	20:19:31.354602-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:19:31.354650-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:19:31.354687-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:19:31.354721-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:19:31.354748-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:19:31.354787-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	20:19:31.354820-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:19:31.354855-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:19:31.354880-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:19:31.354924-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:19:31.354981-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:19:31.355007-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	20:19:31.355209-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	20:19:31.355443-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:19:31.355474-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:19:31.355484-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:19:31.355508-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:19:31.355536-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:19:31.355557-0500	ControlCenter	Navigating to new application [com.nexy.assistant]
default	20:19:31.355567-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	20:19:31.361799-0500	ControlCenter	Received state update for 35344 (app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>, running-active-NotVisible
default	20:19:31.362092-0500	gamepolicyd	Received state update for 35344 (app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>, running-active-NotVisible
default	20:19:31.511452-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xc}
default	20:19:31.511883-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1e804b","name":"Nexy(35344)"}, "details":{"deviceUIDs":[],"implicit_category":"","input_running":false,"output_running":false} }
default	20:19:31.512042-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 76, PID = 35344, Name = sid:0x1e804b, Nexy(35344), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	20:19:31.512120-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 76, PID = 35344, Name = sid:0x1e804b, Nexy(35344), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	20:19:31.512156-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1e804b, Nexy(35344), 'prim'', displayID:'com.nexy.assistant'}
default	20:19:31.512212-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	20:19:31.512223-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1e804b, Nexy(35344), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 76 stopping recording
default	20:19:31.512250-0500	audiomxd	-MXCoreSession- -[MXCoreSession endInterruption:]: Session <ID: 76, PID = 35344, Name = sid:0x1e804b, Nexy(35344), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> is going inactive
default	20:19:31.512278-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 76, PID = 35344, Name = sid:0x1e804b, Nexy(35344), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	20:19:31.512320-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 76, PID = 35344, Name = sid:0x1e804b, Nexy(35344), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	20:19:31.512456-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 0]. BT device UIDS: {(
)}
default	20:19:31.512466-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	20:19:31.512566-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 200 flag 0x1 < Hijack > app com.nexy.assistant CID 0x4D120001 category Not set
default	20:19:31.512841-0500	audiomxd	UpdateAudioState CID 0x4D120001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	20:19:31.512886-0500	audiomxd	UpdateAudioState CID 0x4D120001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:19:31.512947-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	20:19:31.512980-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	20:19:31.512995-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:19:31.513015-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	20:19:31.513082-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	20:19:31.513093-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:19:31.513104-0500	audioaccessoryd	AudioStateChanged: Removed audio session app com.nexy.assistant 201 count 0
default	20:19:31.515536-0500	runningboardd	Invalidating assertion 403-35344-159363 (target:[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344]) from originator [app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344]
default	20:19:31.515615-0500	runningboardd	Invalidating assertion 403-338-159364 (target:[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344]) from originator [osservice<com.apple.powerd>:338]
default	20:19:31.516777-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	20:19:31.518764-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:19:31.518774-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:19:31.518788-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:19:31.518795-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:19:31.518800-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:19:31.518807-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	20:19:31.518907-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	20:19:31.613286-0500	Nexy	                AUHAL.cpp:473   ~AUHAL: (0x737103140) Selecting device 0 from destructor
default	20:19:31.613301-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0x737103140)
default	20:19:31.613307-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0x737103140) not already running
default	20:19:31.613313-0500	Nexy	                AUHAL.cpp:687   SelectDevice: (0x737103140) disconnecting device 91
default	20:19:31.613321-0500	Nexy	                AUHAL.cpp:751   SelectDevice: (0x737103140) destroying ioproc 0xc for device 91
default	20:19:31.613353-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xc}
default	20:19:31.613380-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	20:19:31.613507-0500	Nexy	                AUHAL.cpp:853   SelectDevice: (0x737103140) nothing to setup
default	20:19:31.613518-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x737103140) adding 0 device listeners to device 0
default	20:19:31.613524-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x737103140) adding 0 device delegate listeners to device 0
default	20:19:31.613531-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x737103140) removing 7 device listeners from device 91
default	20:19:31.613769-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x737103140) removing 0 device delegate listeners from device 91
default	20:19:31.613784-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0x737103140)
default	20:19:31.616772-0500	Nexy	                AUHAL.cpp:420   AUHAL: (0x737103140) Selecting device 85 from constructor
default	20:19:31.616786-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0x737103140)
default	20:19:31.616795-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0x737103140) not already running
default	20:19:31.616801-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0x737103140) nothing to teardown
default	20:19:31.616805-0500	Nexy	                AUHAL.cpp:762   SelectDevice: (0x737103140) connecting device 85
default	20:19:31.616895-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0x737103140) Device ID: 85 (Input:No | Output:Yes): true
default	20:19:31.616998-0500	Nexy	                AUHAL.cpp:774   SelectDevice: (0x737103140) created ioproc 0xd for device 85
default	20:19:31.617132-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x737103140) adding 7 device listeners to device 85
default	20:19:31.617327-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x737103140) adding 0 device delegate listeners to device 85
default	20:19:31.617340-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x737103140)
default	20:19:31.617424-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  24000 Hz, Float32, interleaved
default	20:19:31.617434-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	20:19:31.617450-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  24000 Hz, Float32, interleaved
default	20:19:31.617459-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	20:19:31.617466-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	20:19:31.617574-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x737103140) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	20:19:31.617585-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x737103140) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	20:19:31.617592-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	20:19:31.617597-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x737103140) removing 0 device listeners from device 0
default	20:19:31.617600-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x737103140) removing 0 device delegate listeners from device 0
default	20:19:31.617605-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0x737103140)
default	20:19:31.617619-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is DISABLED
default	20:19:31.617681-0500	Nexy	                AUHAL.cpp:2303  SetProperty: (0x737103140) caller requesting device change from 85 to 91
default	20:19:31.617692-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0x737103140)
default	20:19:31.617698-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0x737103140) not already running
default	20:19:31.617703-0500	Nexy	                AUHAL.cpp:687   SelectDevice: (0x737103140) disconnecting device 85
default	20:19:31.617708-0500	Nexy	                AUHAL.cpp:751   SelectDevice: (0x737103140) destroying ioproc 0xd for device 85
default	20:19:31.617722-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped Unknown {1C-77-54-18-C8-A3:output, 0xd}
default	20:19:31.617753-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	20:19:31.617836-0500	Nexy	                AUHAL.cpp:762   SelectDevice: (0x737103140) connecting device 91
default	20:19:31.617928-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0x737103140) Device ID: 91 (Input:Yes | Output:No): true
default	20:19:31.618895-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] Ignoring jetsam update because this process is not memory-managed
default	20:19:31.618911-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] Ignoring suspend because this process is not lifecycle managed
default	20:19:31.618920-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] Ignoring GPU update because this process is not GPU managed
default	20:19:31.618957-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] Ignoring memory limit update because this process is not memory-managed
default	20:19:31.619393-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=411.1593, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=35344, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=398, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	20:19:31.620630-0500	tccd	AUTHREQ_SUBJECT: msgID=411.1593, subject=com.nexy.assistant,
default	20:19:31.621383-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc79244000 at /Applications/Nexy.app
default	20:19:31.621473-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:19:31.621829-0500	ControlCenter	Received state update for 35344 (app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>, running-active-NotVisible
default	20:19:31.621973-0500	Nexy	                AUHAL.cpp:420   AUHAL: (0x735180040) Selecting device 85 from constructor
default	20:19:31.621984-0500	gamepolicyd	Received state update for 35344 (app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>, running-active-NotVisible
default	20:19:31.621985-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0x735180040)
default	20:19:31.621993-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0x735180040) not already running
default	20:19:31.621998-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0x735180040) nothing to teardown
default	20:19:31.622003-0500	Nexy	                AUHAL.cpp:762   SelectDevice: (0x735180040) connecting device 85
default	20:19:31.622088-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0x735180040) Device ID: 85 (Input:No | Output:Yes): true
default	20:19:31.622180-0500	Nexy	                AUHAL.cpp:774   SelectDevice: (0x735180040) created ioproc 0xe for device 85
default	20:19:31.622297-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x735180040) adding 7 device listeners to device 85
default	20:19:31.622483-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x735180040) adding 0 device delegate listeners to device 85
default	20:19:31.622493-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x735180040)
default	20:19:31.622565-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  24000 Hz, Float32, interleaved
default	20:19:31.622574-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	20:19:31.622581-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  24000 Hz, Float32, interleaved
default	20:19:31.622587-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	20:19:31.622596-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	20:19:31.622694-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x735180040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	20:19:31.622710-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x735180040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	20:19:31.622719-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	20:19:31.622724-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x735180040) removing 0 device listeners from device 0
default	20:19:31.622729-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x735180040) removing 0 device delegate listeners from device 0
default	20:19:31.622733-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0x735180040)
default	20:19:31.622740-0500	Nexy	                AUHAL.cpp:2303  SetProperty: (0x735180040) caller requesting device change from 85 to 85
default	20:19:31.622746-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0x735180040)
default	20:19:31.622751-0500	Nexy	                AUHAL.cpp:664   SelectDevice: <- (0x735180040) exiting with nothing to do
default	20:19:31.623425-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	20:19:31.623797-0500	Nexy	       AudioConverter.cpp:1044  Created a new in process converter -> 0x735b76970, from  2 ch,  48000 Hz, Float32, interleaved to  2 ch,  24000 Hz, Float32, interleaved
default	20:19:31.623851-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	20:19:31.625781-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] from originator [app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] with description <RBSAssertionDescriptor| "AudioHAL" ID:403-35344-159365 target:35344 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	20:19:31.625886-0500	runningboardd	Assertion 403-35344-159365 (target:[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344]) will be created as active
default	20:19:31.630752-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] Ignoring jetsam update because this process is not memory-managed
default	20:19:31.630937-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] from originator [osservice<com.apple.powerd>:338] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:403-338-159366 target:35344 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	20:19:31.630963-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] Ignoring suspend because this process is not lifecycle managed
default	20:19:31.631131-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] Ignoring GPU update because this process is not GPU managed
default	20:19:31.631181-0500	runningboardd	Assertion 403-338-159366 (target:[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344]) will be created as active
default	20:19:31.631246-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] Ignoring memory limit update because this process is not memory-managed
default	20:19:31.631566-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xe}
default	20:19:31.632570-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1e804b","name":"Nexy(35344)"}, "details":{"deviceUIDs":["1C-77-54-18-C8-A3:output"],"implicit_category":"MediaPlayback","input_running":false,"output_running":true} }
default	20:19:31.632658-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 76, PID = 35344, Name = sid:0x1e804b, Nexy(35344), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	20:19:31.632683-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Category/Mode changed -- The score for sid:0x1e804b, Nexy(35344), 'prim'/com.nexy.assistant was not correct. Old score = 201
default	20:19:31.632709-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 76, PID = 35344, Name = sid:0x1e804b, Nexy(35344), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	20:19:31.632904-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:19:31.632755-0500	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1e804b, Nexy(35344), 'prim'', AudioCategory changed to 'MediaPlayback'
default	20:19:31.632782-0500	audiomxd	UpdateAudioState CID 0x4D120001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:19:31.632941-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:19:31.632827-0500	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 76, PID = 35344, Name = sid:0x1e804b, Nexy(35344), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO> is going active
default	20:19:31.632848-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsPlaying:]: MXCoreSession com.nexy.assistant with category/mode MediaPlayback/Default and coreSessionID = 76 starting playing
default	20:19:31.633045-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 76, PID = 35344, Name = sid:0x1e804b, Nexy(35344), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	20:19:31.633152-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 76, PID = 35344, Name = sid:0x1e804b, Nexy(35344), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO>
default	20:19:31.633234-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1e804b, Nexy(35344), 'prim'', displayID:'com.nexy.assistant'}
default	20:19:31.633268-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Will try to see if we can get the shared route for session = <ID: 76, PID = 35344, Name = sid:0x1e804b, Nexy(35344), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO>. Old (200) and New (201) scores.
default	20:19:31.633301-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 201, deviceID = <private>
default	20:19:31.633447-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 1]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)}
default	20:19:31.633464-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	20:19:31.633373-0500	audiomxd	AudioApplicationInfoImpl.mm:395   Successfully updated session 0x1e804b to isSessionRecording: 0
	app: {"name":"[implicit] Nexy","pid":35344}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1e804b, sessionType: 'prim', isRecording: false }, 
]
default	20:19:31.633560-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 201 flag 0x1 < Hijack > app com.nexy.assistant CID 0x4D120001 category Not set
default	20:19:31.633735-0500	audiomxd	UpdateAudioState CID 0x4D120001 audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	20:19:31.633802-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 201,
}
default	20:19:31.633821-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	20:19:31.633831-0500	audioaccessoryd	AudioStateChanged: Added audio session app com.nexy.assistant NULL -> 201 count 1
default	20:19:31.633838-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 201
error	20:19:31.633845-0500	audioaccessoryd	Updating local audio category 100 -> 201 app com.nexy.assistant
error	20:19:31.633881-0500	audioaccessoryd	Relaying via 24B92680-715A-E821-B5AF-358E78C2DAF9 inWxAddress 1C:77:54:18:C8:A3 to 88:20:0D:45:06:51 with options {
    "playingApp" : "com.nexy.assistant",
    "hostStreamingState" : "NO",
    "btAddress" : "A0:9A:8E:0D:58:86",
    "btName" : "Mac",
    "otherDeviceAudioCategory" : 201,
}
default	20:19:31.633922-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.nexy.assistant
default	20:19:31.636287-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:19:31.636604-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] Ignoring jetsam update because this process is not memory-managed
default	20:19:31.636620-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] Ignoring suspend because this process is not lifecycle managed
default	20:19:31.636630-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] Ignoring GPU update because this process is not GPU managed
default	20:19:31.636739-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] Ignoring memory limit update because this process is not memory-managed
default	20:19:31.640887-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:19:31.642400-0500	Nexy	[com.apple.controlcenter:CF336ADA-7E66-44CB-8D20-6275B996AAE4] Sending action(s) in update: NSSceneFenceAction
default	20:19:31.659349-0500	Nexy	                AUHAL.cpp:774   SelectDevice: (0x737103140) created ioproc 0xd for device 91
default	20:19:31.659459-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x737103140) adding 7 device listeners to device 91
default	20:19:31.659627-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x737103140) adding 0 device delegate listeners to device 91
default	20:19:31.659640-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x737103140)
default	20:19:31.659646-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 output streams; not all mono
default	20:19:31.659657-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	20:19:31.659812-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  input stream 0 [0x5c]:  1 ch,  24000 Hz, Float32
default	20:19:31.659847-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 input streams; all mono
default	20:19:31.659866-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  1 ch,  24000 Hz, Float32
default	20:19:31.659981-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x737103140) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	20:19:31.659996-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x737103140) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	20:19:31.660001-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	20:19:31.660005-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x737103140) removing 7 device listeners from device 85
default	20:19:31.660170-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x737103140) removing 0 device delegate listeners from device 85
default	20:19:31.660181-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0x737103140)
default	20:19:31.660188-0500	Nexy	AudioHardware-mac-imp.cpp:1306   AudioObjectAddPropertyListener: listener was already added
default	20:19:31.660702-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	20:19:31.661812-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=411.1594, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=35344, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=398, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	20:19:31.662858-0500	tccd	AUTHREQ_SUBJECT: msgID=411.1594, subject=com.nexy.assistant,
default	20:19:31.663479-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc79244000 at /Applications/Nexy.app
default	20:19:31.693403-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	20:19:31.694349-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=411.1595, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=35344, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=398, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	20:19:31.695148-0500	tccd	AUTHREQ_SUBJECT: msgID=411.1595, subject=com.nexy.assistant,
default	20:19:31.695705-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc79244000 at /Applications/Nexy.app
default	20:19:31.728698-0500	ControlCenter	Received state update for 35344 (app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>, running-active-NotVisible
default	20:19:31.728775-0500	gamepolicyd	Received state update for 35344 (app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>, running-active-NotVisible
default	20:19:31.877110-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Output {1C-77-54-18-C8-A3:output, 0xe}
default	20:19:31.877485-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1e804b","name":"Nexy(35344)"}, "details":{"deviceUIDs":[],"implicit_category":"","input_running":false,"output_running":false} }
default	20:19:31.877572-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsPlaying:]: MXCoreSession com.nexy.assistant with category/mode MediaPlayback/Default and coreSessionID = 76 stopping playing
default	20:19:31.877614-0500	audiomxd	-MXCoreSession- -[MXCoreSession endInterruption:]: Session <ID: 76, PID = 35344, Name = sid:0x1e804b, Nexy(35344), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> is going inactive
default	20:19:31.877643-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 76, PID = 35344, Name = sid:0x1e804b, Nexy(35344), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	20:19:31.877691-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 76, PID = 35344, Name = sid:0x1e804b, Nexy(35344), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	20:19:31.877782-0500	audiomxd	UpdateAudioState CID 0x4D120001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:19:31.877813-0500	audiomxd	AudioApplicationInfoImpl.mm:395   Successfully updated session 0x1e804b to isSessionRecording: 0
	app: {"name":"[implicit] Nexy","pid":35344}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1e804b, sessionType: 'prim', isRecording: false }, 
]
default	20:19:31.877899-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 0]. BT device UIDS: {(
)}
default	20:19:31.877918-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	20:19:31.877952-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:19:31.878000-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:19:31.878019-0500	audioaccessoryd	AudioStateChanged: Removed audio session app com.nexy.assistant 201 count 0
default	20:19:31.879867-0500	runningboardd	Invalidating assertion 403-35344-159365 (target:[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344]) from originator [app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344]
default	20:19:31.882021-0500	runningboardd	Invalidating assertion 403-338-159366 (target:[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344]) from originator [osservice<com.apple.powerd>:338]
default	20:19:31.985784-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] Ignoring jetsam update because this process is not memory-managed
default	20:19:31.985800-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] Ignoring suspend because this process is not lifecycle managed
default	20:19:31.985810-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] Ignoring GPU update because this process is not GPU managed
default	20:19:31.985830-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] Ignoring memory limit update because this process is not memory-managed
default	20:19:31.989360-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:19:31.989911-0500	ControlCenter	Received state update for 35344 (app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>, running-active-NotVisible
default	20:19:31.990075-0500	gamepolicyd	Received state update for 35344 (app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>, running-active-NotVisible
default	20:19:32.232887-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] from originator [app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] with description <RBSAssertionDescriptor| "AudioHAL" ID:403-35344-159368 target:35344 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	20:19:32.233083-0500	runningboardd	Assertion 403-35344-159368 (target:[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344]) will be created as active
default	20:19:32.233835-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] Ignoring jetsam update because this process is not memory-managed
default	20:19:32.233866-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] Ignoring suspend because this process is not lifecycle managed
default	20:19:32.233891-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] Ignoring GPU update because this process is not GPU managed
default	20:19:32.233937-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] Ignoring memory limit update because this process is not memory-managed
default	20:19:32.235727-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=411.1596, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=35344, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=398, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	20:19:32.237886-0500	tccd	AUTHREQ_SUBJECT: msgID=411.1596, subject=com.nexy.assistant,
default	20:19:32.238507-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:19:32.239058-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc79244000 at /Applications/Nexy.app
default	20:19:32.239156-0500	ControlCenter	Received state update for 35344 (app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>, running-active-NotVisible
default	20:19:32.239402-0500	gamepolicyd	Received state update for 35344 (app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>, running-active-NotVisible
default	20:19:32.268687-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Input {1C-77-54-18-C8-A3:input, 0xd}
default	20:19:32.271289-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1e804b","name":"Nexy(35344)"}, "details":{"deviceUIDs":["1C-77-54-18-C8-A3:input"],"implicit_category":"Record","input_running":true,"output_running":false} }
default	20:19:32.271383-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 76, PID = 35344, Name = sid:0x1e804b, Nexy(35344), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	20:19:32.271414-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Category/Mode changed -- The score for sid:0x1e804b, Nexy(35344), 'prim'/com.nexy.assistant was not correct. Old score = 201
default	20:19:32.271442-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 76, PID = 35344, Name = sid:0x1e804b, Nexy(35344), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	20:19:32.271608-0500	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1e804b, Nexy(35344), 'prim'', AudioCategory changed to 'Record_WithBluetooth'
default	20:19:32.271724-0500	audiomxd	UpdateAudioState CID 0x4D120001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:19:32.271799-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 76, PID = 35344, Name = sid:0x1e804b, Nexy(35344), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	20:19:32.271873-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 76, PID = 35344, Name = sid:0x1e804b, Nexy(35344), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	20:19:32.271939-0500	audiomxd	UpdateAudioState CID 0x4D120001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:19:32.271946-0500	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 76, PID = 35344, Name = sid:0x1e804b, Nexy(35344), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> is going active
default	20:19:32.271959-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1e804b, Nexy(35344), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 76 starting recording
default	20:19:32.271951-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:19:32.271996-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:19:32.271930-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] from originator [osservice<com.apple.powerd>:338] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:403-338-159369 target:35344 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	20:19:32.272044-0500	runningboardd	Assertion 403-338-159369 (target:[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344]) will be created as active
default	20:19:32.272124-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 76, PID = 35344, Name = sid:0x1e804b, Nexy(35344), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	20:19:32.272193-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 76, PID = 35344, Name = sid:0x1e804b, Nexy(35344), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	20:19:32.272598-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] Ignoring jetsam update because this process is not memory-managed
default	20:19:32.272089-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:19:32.272198-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:19:32.272634-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] Ignoring suspend because this process is not lifecycle managed
default	20:19:32.272665-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] Ignoring GPU update because this process is not GPU managed
default	20:19:32.272751-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] Ignoring memory limit update because this process is not memory-managed
default	20:19:32.272314-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1e804b, Nexy(35344), 'prim'', displayID:'com.nexy.assistant'}
default	20:19:32.272458-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [1, 0]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:input"
)}
default	20:19:32.272469-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	20:19:32.272782-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 200 flag 0x1 < Hijack > app com.nexy.assistant CID 0x4D120001 category Not set
default	20:19:32.272468-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	20:19:32.273380-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	20:19:32.273252-0500	audiomxd	UpdateAudioState CID 0x4D120001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	20:19:32.273406-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	20:19:32.273422-0500	audioaccessoryd	AudioStateChanged: Added audio session app com.nexy.assistant NULL -> 200 count 1
default	20:19:32.273432-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
error	20:19:32.273443-0500	audioaccessoryd	Updating local audio category 100 -> 200 app com.nexy.assistant
error	20:19:32.273593-0500	audioaccessoryd	Relaying via 24B92680-715A-E821-B5AF-358E78C2DAF9 inWxAddress 1C:77:54:18:C8:A3 to 88:20:0D:45:06:51 with options {
    "playingApp" : "com.nexy.assistant",
    "hostStreamingState" : "YES",
    "btAddress" : "A0:9A:8E:0D:58:86",
    "btName" : "Mac",
    "otherDeviceAudioCategory" : 200,
}
default	20:19:32.273742-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	20:19:32.278068-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:19:32.278631-0500	ControlCenter	Received state update for 35344 (app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>, running-active-NotVisible
default	20:19:32.278760-0500	gamepolicyd	Received state update for 35344 (app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>, running-active-NotVisible
default	20:19:32.281544-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	20:19:32.281661-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	20:19:32.281717-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	20:19:32.282440-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:19:32.282452-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:19:32.282465-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:19:32.282474-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:19:32.282480-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:19:32.282502-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	20:19:32.282538-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:19:32.282562-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:19:32.282598-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:19:32.282633-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:19:32.282712-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:19:32.282753-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	20:19:32.282949-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	20:19:32.283425-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:19:32.283436-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:19:32.283446-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:19:32.283452-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:19:32.283461-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:19:32.283487-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	20:19:32.283560-0500	ControlCenter	Navigating to new application [com.nexy.assistant]
default	20:19:33.034990-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.nexy.assistant, Score 200, Remote 100 NumofApp 1
default	20:19:34.784676-0500	Nexy	[0x735afa800] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	20:19:34.786462-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=35344.5, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=35344, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	20:19:34.789408-0500	tccd	AUTHREQ_SUBJECT: msgID=35344.5, subject=com.nexy.assistant,
default	20:19:34.791378-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x92f17aa00 at /Applications/Nexy.app
default	20:19:34.818381-0500	Nexy	[0x735afa800] invalidated after the last release of the connection object
default	20:19:34.819565-0500	Nexy	 [INFO] SLSHWCaptureDesktopProxying:485 request: <private>
default	20:19:34.822160-0500	Nexy	[0x735afa800] activating connection: mach=true listener=false peer=false name=com.apple.replayd
default	20:19:34.822293-0500	Nexy	 [INFO] -[RPDaemonProxy consumeSandboxExtension:processNewConnection:]:568
default	20:19:34.822762-0500	Nexy	 [INFO] -[RPDaemonProxy proxyCoreGraphicsWithMethodType:config:machPort:completionHandler:]:1493
default	20:19:34.830882-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=33784.2, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=35344, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.replayd, pid=33784, auid=501, euid=501, binary_path=/usr/libexec/replayd}, },
default	20:19:34.830912-0500	tccd	requestor: TCCDProcess: identifier=com.apple.replayd, pid=33784, auid=501, euid=501, binary_path=/usr/libexec/replayd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=35344, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	20:19:34.831871-0500	tccd	AUTHREQ_SUBJECT: msgID=33784.2, subject=com.nexy.assistant,
default	20:19:34.832508-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x92f17aa00 at /Applications/Nexy.app
default	20:19:34.871320-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=397.2782, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=35344, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=397, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	20:19:34.871342-0500	tccd	requestor: TCCDProcess: identifier=com.apple.WindowServer, pid=397, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=35344, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	20:19:34.872140-0500	tccd	AUTHREQ_SUBJECT: msgID=397.2782, subject=com.nexy.assistant,
default	20:19:34.872744-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x92f17aa00 at /Applications/Nexy.app
default	20:19:34.923989-0500	Nexy	 [INFO] SLSHWCaptureDesktopProxying_block_invoke:506 request: <private>, error: (null), windowInfo: (null)
default	20:19:34.950262-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	20:19:34.957439-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	20:19:34.957520-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant), [scr] Nexy (com.nexy.assistant)]
default	20:19:34.957552-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant", "scr:com.nexy.assistant"]
default	20:19:34.958240-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:19:34.958260-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:19:34.958292-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:19:34.958362-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:19:34.958503-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:19:34.958544-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	20:19:34.958647-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:19:34.958734-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:19:34.958785-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:19:34.958834-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:19:34.958884-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:19:34.958934-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	20:19:34.959021-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:19:34.959079-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:19:34.959470-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:19:34.959513-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	20:19:34.959543-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:19:34.959608-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:19:34.959655-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	20:19:35.037740-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xd}
default	20:19:35.037997-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1e804b","name":"Nexy(35344)"}, "details":{"deviceUIDs":[],"implicit_category":"","input_running":false,"output_running":false} }
default	20:19:35.038098-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 76, PID = 35344, Name = sid:0x1e804b, Nexy(35344), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	20:19:35.038147-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 76, PID = 35344, Name = sid:0x1e804b, Nexy(35344), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	20:19:35.038175-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1e804b, Nexy(35344), 'prim'', displayID:'com.nexy.assistant'}
default	20:19:35.038222-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1e804b, Nexy(35344), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 76 stopping recording
default	20:19:35.038239-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	20:19:35.038248-0500	audiomxd	-MXCoreSession- -[MXCoreSession endInterruption:]: Session <ID: 76, PID = 35344, Name = sid:0x1e804b, Nexy(35344), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> is going inactive
default	20:19:35.038278-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 76, PID = 35344, Name = sid:0x1e804b, Nexy(35344), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	20:19:35.038319-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 76, PID = 35344, Name = sid:0x1e804b, Nexy(35344), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	20:19:35.038420-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 0]. BT device UIDS: {(
)}
default	20:19:35.038431-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	20:19:35.038492-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 200 flag 0x1 < Hijack > app com.nexy.assistant CID 0x4D120001 category Not set
default	20:19:35.038918-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	20:19:35.038953-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	20:19:35.038994-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	20:19:35.039061-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:19:35.039175-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	20:19:35.039233-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:19:35.039278-0500	audioaccessoryd	AudioStateChanged: Removed audio session app com.nexy.assistant 201 count 0
default	20:19:35.039946-0500	runningboardd	Invalidating assertion 403-35344-159368 (target:[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344]) from originator [app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344]
default	20:19:35.038748-0500	audiomxd	UpdateAudioState CID 0x4D120001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	20:19:35.040564-0500	runningboardd	Invalidating assertion 403-338-159369 (target:[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344]) from originator [osservice<com.apple.powerd>:338]
default	20:19:35.038785-0500	audiomxd	UpdateAudioState CID 0x4D120001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:19:35.049695-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	20:19:35.049777-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant)]
default	20:19:35.049822-0500	ControlCenter	Active activity attributions changed to ["scr:com.nexy.assistant"]
default	20:19:35.049835-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	20:19:35.050343-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:19:35.050369-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:19:35.050410-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:19:35.050435-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:19:35.050463-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:19:35.050493-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	20:19:35.050786-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	20:19:35.143256-0500	Nexy	                AUHAL.cpp:473   ~AUHAL: (0x737103140) Selecting device 0 from destructor
default	20:19:35.143270-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0x737103140)
default	20:19:35.143276-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0x737103140) not already running
default	20:19:35.143282-0500	Nexy	                AUHAL.cpp:687   SelectDevice: (0x737103140) disconnecting device 91
default	20:19:35.143289-0500	Nexy	                AUHAL.cpp:751   SelectDevice: (0x737103140) destroying ioproc 0xd for device 91
default	20:19:35.143313-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xd}
default	20:19:35.143345-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	20:19:35.143481-0500	Nexy	                AUHAL.cpp:853   SelectDevice: (0x737103140) nothing to setup
default	20:19:35.143496-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x737103140) adding 0 device listeners to device 0
default	20:19:35.143505-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x737103140) adding 0 device delegate listeners to device 0
default	20:19:35.143512-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x737103140) removing 7 device listeners from device 91
default	20:19:35.143748-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x737103140) removing 0 device delegate listeners from device 91
default	20:19:35.143768-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0x737103140)
default	20:19:35.146056-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] Ignoring jetsam update because this process is not memory-managed
default	20:19:35.146071-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] Ignoring suspend because this process is not lifecycle managed
default	20:19:35.146096-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] Ignoring GPU update because this process is not GPU managed
default	20:19:35.146162-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] Ignoring memory limit update because this process is not memory-managed
default	20:19:35.148767-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:19:35.149163-0500	ControlCenter	Received state update for 35344 (app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>, running-active-NotVisible
default	20:19:35.149342-0500	gamepolicyd	Received state update for 35344 (app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>, running-active-NotVisible
default	20:19:35.433417-0500	Nexy	nw_path_libinfo_path_check [3DCC1CE2-7CB8-4B7E-92FA-9850F1743475 Hostname#b818a3c8:80 tcp, legacy-socket, attribution: developer]
	libinfo check path: <private>
default	20:19:35.433715-0500	mDNSResponder	[R149202] DNSServiceCreateConnection START PID[35344](Nexy)
default	20:19:35.433816-0500	mDNSResponder	[R149203] DNSServiceQueryRecord START -- qname: <mask.hash: 'HKLMzXHw1FEmCUQzpEBEqw=='>, qtype: A, flags: 0x1D000, interface index: 0, client pid: 35344 (Nexy), name hash: b360ab20
default	20:19:35.434523-0500	mDNSResponder	[R149204] DNSServiceQueryRecord START -- qname: <mask.hash: 'HKLMzXHw1FEmCUQzpEBEqw=='>, qtype: AAAA, flags: 0x1D000, interface index: 0, client pid: 35344 (Nexy), name hash: b360ab20
default	20:19:35.460441-0500	kernel	SK[1]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid C7ABFD1F-CD20-404A-9766-B9753F6F39CA flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.58430,dst=<IPv4-redacted>.80,proto=0x06 mask=0x0000003f,hash=0xee343083 tp_proto=0x06"
default	20:19:35.460536-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:58430<-><IPv4-redacted>:80] interface: utun6 (skipped: 47531)
so_gencnt: 2920265 t_state: SYN_SENT process: Nexy:35344 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xa5298d0e
default	20:19:35.461191-0500	kernel	tcp connected: [<IPv4-redacted>:58430<-><IPv4-redacted>:80] interface: utun6 (skipped: 47531)
so_gencnt: 2920265 t_state: ESTABLISHED process: Nexy:35344 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xa5298d0e
default	20:19:36.159384-0500	kernel	tcp_connection_summary (tcp_usrclosed:3220)[<IPv4-redacted>:58430<-><IPv4-redacted>:80] interface: utun6 (skipped: 47531)
so_gencnt: 2920265 t_state: LAST_ACK process: Nexy:35344 Duration: 0.699 sec Conn_Time: 0.001 sec bytes in/out: 596/60822 pkts in/out: 2/20 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 1.468 ms rttvar: 1.000 ms base rtt: 1 ms so_error: 0 svc/tc: 0 flow: 0xa5298d0e
default	20:19:36.159424-0500	kernel	tcp_connection_summary [<IPv4-redacted>:58430<-><IPv4-redacted>:80] interface: utun6 (skipped: 47531)
so_gencnt: 2920265 t_state: LAST_ACK process: Nexy:35344 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 1/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	20:19:36.180174-0500	kernel	udp connect: [<IPv4-redacted>:49611<-><IPv4-redacted>:443] interface:  (skipped: 0)
so_gencnt: 2920268 so_state: 0x0002 process: Nexy:35344 bytes in/out: 0/0 pkts in/out: 0/0 error: 0 so_error: 0 svc/tc: 0 flow: 0xbc6d8dad
default	20:19:36.180202-0500	kernel	udp_connection_summary [<IPv4-redacted>:49611<-><IPv4-redacted>:443] interface:  (skipped: 0)
so_gencnt: 2920268 so_state: 0x0002 process: Nexy:35344 Duration: 0.000 sec Conn_Time: 0.000 sec bytes in/out: 0/0 pkts in/out: 0/0 rxnospace pkts/bytes: 0/0 so_error: 0 svc/tc: 0 flow: 0xbc6d8dad flowctl: 0us (0x)
default	20:19:36.182214-0500	kernel	SK[1]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 07F3D34C-AB2B-4744-A7C3-AF93A631DEF4 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.58432,dst=<IPv4-redacted>.443,proto=0x06 mask=0x0000003f,hash=0xfe3b9f08 tp_proto=0x06"
default	20:19:36.182281-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:58432<-><IPv4-redacted>:443] interface: utun6 (skipped: 47531)
so_gencnt: 2920270 t_state: SYN_SENT process: Nexy:35344 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 1 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xaf4dcb85
default	20:19:36.182775-0500	kernel	tcp connected: [<IPv4-redacted>:58432<-><IPv4-redacted>:443] interface: utun6 (skipped: 47531)
so_gencnt: 2920270 t_state: ESTABLISHED process: Nexy:35344 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 1 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xaf4dcb85
default	20:19:36.187767-0500	Nexy	[com.apple.controlcenter:CF336ADA-7E66-44CB-8D20-6275B996AAE4] Sending action(s) in update: NSSceneFenceAction
default	20:19:37.266395-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(10584)
default	20:19:37.266460-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:10584 called from <private>
default	20:19:37.266473-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:10584 called from <private>
default	20:19:37.266691-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(10585)
default	20:19:37.266720-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:10585 called from <private>
default	20:19:37.266730-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:10585 called from <private>
default	20:19:37.281192-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(10585)
default	20:19:37.281244-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:10585 called from <private>
default	20:19:37.281254-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:10585 called from <private>
default	20:19:37.283113-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:10584 called from <private>
default	20:19:37.283133-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:10584 called from <private>
default	20:19:37.283689-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(10584)
default	20:19:37.283713-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:10584 called from <private>
default	20:19:37.283746-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:10584 called from <private>
default	20:19:37.285164-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(10584)
default	20:19:37.285248-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(10584)
default	20:19:37.285284-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(10584)
default	20:19:37.285530-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:10584 called from <private>
default	20:19:37.285541-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:10584 called from <private>
default	20:19:37.285655-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:10584 called from <private>
default	20:19:37.285733-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:10584 called from <private>
default	20:19:37.285797-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:10584 called from <private>
default	20:19:37.285846-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:10584 called from <private>
default	20:19:37.285924-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:10584 called from <private>
default	20:19:37.286154-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(10584)
default	20:19:37.286453-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:10584 called from <private>
default	20:19:37.286715-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:10584 called from <private>
default	20:19:37.286807-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:10584 called from <private>
default	20:19:37.302653-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:10584 called from <private>
default	20:19:37.302684-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:10584 called from <private>
default	20:19:37.302814-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(10584)
default	20:19:37.308218-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(10584)
default	20:19:37.308691-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:10584 called from <private>
default	20:19:37.308705-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:10584 called from <private>
default	20:19:37.308856-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(10584)
default	20:19:37.314285-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(10584)
default	20:19:37.314775-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:10584 called from <private>
default	20:19:37.314790-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:10584 called from <private>
default	20:19:37.314850-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:10584 called from <private>
default	20:19:37.314858-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:10584 called from <private>
default	20:19:37.314866-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:10584 called from <private>
default	20:19:37.314872-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:10584 called from <private>
default	20:19:37.314922-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:10584 called from <private>
default	20:19:37.315058-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:10584 called from <private>
default	20:19:37.315264-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:10584 called from <private>
default	20:19:37.315455-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:10584 called from <private>
default	20:19:37.315607-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:10584 called from <private>
default	20:19:37.315829-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:10584 called from <private>
default	20:19:37.321146-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0x735180040) Device ID: 85 (Input:No | Output:Yes): true
default	20:19:37.321188-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x735180040)
default	20:19:37.325490-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  48000 Hz, Float32, interleaved
default	20:19:37.325532-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	20:19:37.325541-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	20:19:37.325607-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	20:19:37.325618-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	20:19:37.326045-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	20:19:37.326428-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x735180040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	20:19:37.326450-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x735180040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	20:19:37.326457-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	20:19:37.326688-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0x735180040) Device ID: 85 (Input:No | Output:Yes): true
default	20:19:37.326703-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x735180040)
default	20:19:37.327497-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  48000 Hz, Float32, interleaved
default	20:19:37.327517-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	20:19:37.327524-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	20:19:37.327542-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	20:19:37.327553-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	20:19:37.328039-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	20:19:37.328253-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x735180040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	20:19:37.328269-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x735180040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	20:19:37.328277-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	20:19:38.328706-0500	Nexy	                AUHAL.cpp:473   ~AUHAL: (0x735180040) Selecting device 0 from destructor
default	20:19:38.328737-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0x735180040)
default	20:19:38.328753-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0x735180040) not already running
default	20:19:38.328767-0500	Nexy	                AUHAL.cpp:687   SelectDevice: (0x735180040) disconnecting device 85
default	20:19:38.328780-0500	Nexy	                AUHAL.cpp:751   SelectDevice: (0x735180040) destroying ioproc 0xe for device 85
default	20:19:38.328834-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Output {1C-77-54-18-C8-A3:output, 0xe}
default	20:19:38.328903-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	20:19:38.329206-0500	Nexy	                AUHAL.cpp:853   SelectDevice: (0x735180040) nothing to setup
default	20:19:38.329236-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x735180040) adding 0 device listeners to device 0
default	20:19:38.329251-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x735180040) adding 0 device delegate listeners to device 0
default	20:19:38.329265-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x735180040) removing 7 device listeners from device 85
default	20:19:38.329751-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x735180040) removing 0 device delegate listeners from device 85
default	20:19:38.329786-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0x735180040)
default	20:19:38.332331-0500	Nexy	                AUHAL.cpp:420   AUHAL: (0x735180040) Selecting device 85 from constructor
default	20:19:38.332355-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0x735180040)
default	20:19:38.332366-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0x735180040) not already running
default	20:19:38.332375-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0x735180040) nothing to teardown
default	20:19:38.332382-0500	Nexy	                AUHAL.cpp:762   SelectDevice: (0x735180040) connecting device 85
default	20:19:38.332557-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0x735180040) Device ID: 85 (Input:No | Output:Yes): true
default	20:19:38.332747-0500	Nexy	                AUHAL.cpp:774   SelectDevice: (0x735180040) created ioproc 0xf for device 85
default	20:19:38.332971-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x735180040) adding 7 device listeners to device 85
default	20:19:38.333321-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x735180040) adding 0 device delegate listeners to device 85
default	20:19:38.333339-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x735180040)
default	20:19:38.333483-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  48000 Hz, Float32, interleaved
default	20:19:38.333502-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	20:19:38.333515-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	20:19:38.333530-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	20:19:38.333548-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	20:19:38.333745-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x735180040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	20:19:38.333767-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x735180040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	20:19:38.333781-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	20:19:38.333791-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x735180040) removing 0 device listeners from device 0
default	20:19:38.333801-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x735180040) removing 0 device delegate listeners from device 0
default	20:19:38.333808-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0x735180040)
default	20:19:38.333827-0500	Nexy	                AUHAL.cpp:2303  SetProperty: (0x735180040) caller requesting device change from 85 to 85
default	20:19:38.333833-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0x735180040)
default	20:19:38.333841-0500	Nexy	                AUHAL.cpp:664   SelectDevice: <- (0x735180040) exiting with nothing to do
default	20:19:38.333851-0500	Nexy	AudioHardware-mac-imp.cpp:1306   AudioObjectAddPropertyListener: listener was already added
default	20:19:38.334462-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	20:19:38.335089-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	20:19:38.338592-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] from originator [app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] with description <RBSAssertionDescriptor| "AudioHAL" ID:403-35344-159375 target:35344 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	20:19:38.338722-0500	runningboardd	Assertion 403-35344-159375 (target:[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344]) will be created as active
default	20:19:38.339176-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] from originator [osservice<com.apple.powerd>:338] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:403-338-159376 target:35344 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	20:19:38.339186-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] Ignoring jetsam update because this process is not memory-managed
default	20:19:38.339200-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] Ignoring suspend because this process is not lifecycle managed
default	20:19:38.339212-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] Ignoring GPU update because this process is not GPU managed
default	20:19:38.339806-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] Ignoring memory limit update because this process is not memory-managed
default	20:19:38.339818-0500	runningboardd	Assertion 403-338-159376 (target:[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344]) will be created as active
default	20:19:38.343611-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:19:38.344007-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] Ignoring jetsam update because this process is not memory-managed
default	20:19:38.344019-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] Ignoring suspend because this process is not lifecycle managed
default	20:19:38.344060-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] Ignoring GPU update because this process is not GPU managed
default	20:19:38.344113-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] Ignoring memory limit update because this process is not memory-managed
default	20:19:38.344255-0500	ControlCenter	Received state update for 35344 (app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>, running-active-NotVisible
default	20:19:38.345623-0500	gamepolicyd	Received state update for 35344 (app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>, running-active-NotVisible
default	20:19:38.347644-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:19:38.348130-0500	ControlCenter	Received state update for 35344 (app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>, running-active-NotVisible
default	20:19:38.348211-0500	gamepolicyd	Received state update for 35344 (app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>, running-active-NotVisible
default	20:19:38.707520-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xf}
default	20:19:38.708470-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1e804b","name":"Nexy(35344)"}, "details":{"deviceUIDs":["1C-77-54-18-C8-A3:output"],"implicit_category":"MediaPlayback","input_running":false,"output_running":true} }
default	20:19:38.708591-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 76, PID = 35344, Name = sid:0x1e804b, Nexy(35344), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	20:19:38.708632-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Category/Mode changed -- The score for sid:0x1e804b, Nexy(35344), 'prim'/com.nexy.assistant was not correct. Old score = 201
default	20:19:38.708671-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 76, PID = 35344, Name = sid:0x1e804b, Nexy(35344), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	20:19:38.708718-0500	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1e804b, Nexy(35344), 'prim'', AudioCategory changed to 'MediaPlayback'
default	20:19:38.708744-0500	audiomxd	UpdateAudioState CID 0x4D120001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:19:38.708766-0500	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 76, PID = 35344, Name = sid:0x1e804b, Nexy(35344), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO> is going active
default	20:19:38.708779-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsPlaying:]: MXCoreSession com.nexy.assistant with category/mode MediaPlayback/Default and coreSessionID = 76 starting playing
default	20:19:38.708929-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:19:38.708982-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:19:38.708889-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 76, PID = 35344, Name = sid:0x1e804b, Nexy(35344), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	20:19:38.708951-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 76, PID = 35344, Name = sid:0x1e804b, Nexy(35344), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO>
default	20:19:38.709026-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1e804b, Nexy(35344), 'prim'', displayID:'com.nexy.assistant'}
default	20:19:38.709098-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Will try to see if we can get the shared route for session = <ID: 76, PID = 35344, Name = sid:0x1e804b, Nexy(35344), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO>. Old (200) and New (201) scores.
default	20:19:38.709144-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 201, deviceID = <private>
default	20:19:38.709296-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 1]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)}
default	20:19:38.709214-0500	audiomxd	AudioApplicationInfoImpl.mm:395   Successfully updated session 0x1e804b to isSessionRecording: 0
	app: {"name":"[implicit] Nexy","pid":35344}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1e804b, sessionType: 'prim', isRecording: false }, 
]
default	20:19:38.709310-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	20:19:38.709367-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 201 flag 0x1 < Hijack > app com.nexy.assistant CID 0x4D120001 category Not set
default	20:19:38.709544-0500	audiomxd	UpdateAudioState CID 0x4D120001 audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	20:19:38.709615-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 201,
}
default	20:19:38.709645-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	20:19:38.709659-0500	audioaccessoryd	AudioStateChanged: Added audio session app com.nexy.assistant NULL -> 201 count 1
default	20:19:38.709667-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 201
error	20:19:38.709677-0500	audioaccessoryd	Updating local audio category 100 -> 201 app com.nexy.assistant
error	20:19:38.709727-0500	audioaccessoryd	Relaying via 24B92680-715A-E821-B5AF-358E78C2DAF9 inWxAddress 1C:77:54:18:C8:A3 to 88:20:0D:45:06:51 with options {
    "playingApp" : "com.nexy.assistant",
    "hostStreamingState" : "YES",
    "btAddress" : "A0:9A:8E:0D:58:86",
    "btName" : "Mac",
    "otherDeviceAudioCategory" : 201,
}
default	20:19:38.709788-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.nexy.assistant
default	20:19:39.034836-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.nexy.assistant, Score 201, Remote 100 NumofApp 1
default	20:19:40.258485-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Output {1C-77-54-18-C8-A3:output, 0xf}
default	20:19:40.258853-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1e804b","name":"Nexy(35344)"}, "details":{"deviceUIDs":[],"implicit_category":"","input_running":false,"output_running":false} }
default	20:19:40.259015-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsPlaying:]: MXCoreSession com.nexy.assistant with category/mode MediaPlayback/Default and coreSessionID = 76 stopping playing
default	20:19:40.259083-0500	audiomxd	-MXCoreSession- -[MXCoreSession endInterruption:]: Session <ID: 76, PID = 35344, Name = sid:0x1e804b, Nexy(35344), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> is going inactive
default	20:19:40.259141-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 76, PID = 35344, Name = sid:0x1e804b, Nexy(35344), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	20:19:40.259253-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 76, PID = 35344, Name = sid:0x1e804b, Nexy(35344), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	20:19:40.259468-0500	audiomxd	UpdateAudioState CID 0x4D120001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:19:40.259599-0500	audiomxd	AudioApplicationInfoImpl.mm:395   Successfully updated session 0x1e804b to isSessionRecording: 0
	app: {"name":"[implicit] Nexy","pid":35344}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1e804b, sessionType: 'prim', isRecording: false }, 
]
default	20:19:40.259732-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:19:40.259820-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:19:40.259746-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 0]. BT device UIDS: {(
)}
default	20:19:40.259851-0500	audioaccessoryd	AudioStateChanged: Removed audio session app com.nexy.assistant 201 count 0
default	20:19:40.259763-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	20:19:40.264389-0500	runningboardd	Invalidating assertion 403-35344-159375 (target:[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344]) from originator [app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344]
default	20:19:40.264544-0500	runningboardd	Invalidating assertion 403-338-159376 (target:[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344]) from originator [osservice<com.apple.powerd>:338]
default	20:19:40.273606-0500	coreaudiod	Sending message. { reporterID=151801324109831, category=IO, type=error, message=["wg_cycles": Optional(1486419), "HostApplicationDisplayID": Optional(com.nexy.assistant), "input_device_uid_list": Optional(), "careporting_timestamp": 1764119980.273278, "HAL_client_IO_duration": Optional(14973250), "io_buffer_size": Optional(512), "num_continuous_silent_io_cycles": Optional(2), "start_time": Optional(2266099604783), "io_page_faults": Optional(0), "issue_type": Optional(overload), "deadline": Optional(76944), "io_cycle_budget": Optional(11354166), "other_active_clients": Optional([  ]), "output_device_source_list": Optional(Unknown), "cause": Optional(ClientHALIODurationExceededBudget,SafetyViolationOccurred), "is_prewarming": Optional(0), "num_continuous_nonzero_io_cycles": Optional(0), "lateness": Optional(193), "smallest_buffer_frame_size": Optional(2147483647), "input_device_transport_list": Optional(), "io_cycle": Optional(144), "safety_violation_time_gap": Optional(0.004645833333333333), "cause_set": Optional(12), "io_page_faults_duration": Opti<…> }
default	20:19:40.361474-0500	Nexy	                AUHAL.cpp:473   ~AUHAL: (0x735180040) Selecting device 0 from destructor
default	20:19:40.361495-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0x735180040)
default	20:19:40.361501-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0x735180040) not already running
default	20:19:40.361509-0500	Nexy	                AUHAL.cpp:687   SelectDevice: (0x735180040) disconnecting device 85
default	20:19:40.361515-0500	Nexy	                AUHAL.cpp:751   SelectDevice: (0x735180040) destroying ioproc 0xf for device 85
default	20:19:40.361550-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Output {1C-77-54-18-C8-A3:output, 0xf}
default	20:19:40.361586-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	20:19:40.361736-0500	Nexy	                AUHAL.cpp:853   SelectDevice: (0x735180040) nothing to setup
default	20:19:40.361749-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x735180040) adding 0 device listeners to device 0
default	20:19:40.361757-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x735180040) adding 0 device delegate listeners to device 0
default	20:19:40.361778-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x735180040) removing 7 device listeners from device 85
default	20:19:40.361987-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x735180040) removing 0 device delegate listeners from device 85
default	20:19:40.362001-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0x735180040)
default	20:19:40.366724-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] Ignoring jetsam update because this process is not memory-managed
default	20:19:40.366738-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] Ignoring suspend because this process is not lifecycle managed
default	20:19:40.366748-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] Ignoring GPU update because this process is not GPU managed
default	20:19:40.366765-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] Ignoring memory limit update because this process is not memory-managed
default	20:19:40.368630-0500	Nexy	                AUHAL.cpp:420   AUHAL: (0x735180040) Selecting device 85 from constructor
default	20:19:40.368648-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0x735180040)
default	20:19:40.368654-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0x735180040) not already running
default	20:19:40.368660-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0x735180040) nothing to teardown
default	20:19:40.368665-0500	Nexy	                AUHAL.cpp:762   SelectDevice: (0x735180040) connecting device 85
default	20:19:40.368769-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0x735180040) Device ID: 85 (Input:No | Output:Yes): true
default	20:19:40.368895-0500	Nexy	                AUHAL.cpp:774   SelectDevice: (0x735180040) created ioproc 0x10 for device 85
default	20:19:40.369020-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x735180040) adding 7 device listeners to device 85
default	20:19:40.369246-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x735180040) adding 0 device delegate listeners to device 85
default	20:19:40.369256-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x735180040)
default	20:19:40.369347-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  48000 Hz, Float32, interleaved
default	20:19:40.369358-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	20:19:40.369365-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	20:19:40.369374-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	20:19:40.369381-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	20:19:40.369503-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x735180040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	20:19:40.369515-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x735180040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	20:19:40.369523-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	20:19:40.369528-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x735180040) removing 0 device listeners from device 0
default	20:19:40.369533-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x735180040) removing 0 device delegate listeners from device 0
default	20:19:40.369537-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0x735180040)
default	20:19:40.369548-0500	Nexy	                AUHAL.cpp:2303  SetProperty: (0x735180040) caller requesting device change from 85 to 85
default	20:19:40.369553-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0x735180040)
default	20:19:40.369558-0500	Nexy	                AUHAL.cpp:664   SelectDevice: <- (0x735180040) exiting with nothing to do
default	20:19:40.369565-0500	Nexy	AudioHardware-mac-imp.cpp:1306   AudioObjectAddPropertyListener: listener was already added
default	20:19:40.369725-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:19:40.369967-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	20:19:40.370244-0500	ControlCenter	Received state update for 35344 (app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>, running-active-NotVisible
default	20:19:40.370327-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	20:19:40.370398-0500	gamepolicyd	Received state update for 35344 (app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>, running-active-NotVisible
default	20:19:40.372909-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] from originator [app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] with description <RBSAssertionDescriptor| "AudioHAL" ID:403-35344-159379 target:35344 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	20:19:40.373024-0500	runningboardd	Assertion 403-35344-159379 (target:[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344]) will be created as active
default	20:19:40.373423-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] Ignoring jetsam update because this process is not memory-managed
default	20:19:40.373413-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] from originator [osservice<com.apple.powerd>:338] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:403-338-159380 target:35344 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	20:19:40.373476-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] Ignoring suspend because this process is not lifecycle managed
default	20:19:40.374095-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] Ignoring GPU update because this process is not GPU managed
default	20:19:40.374140-0500	runningboardd	Assertion 403-338-159380 (target:[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344]) will be created as active
default	20:19:40.374181-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] Ignoring memory limit update because this process is not memory-managed
default	20:19:40.377187-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:19:40.377486-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] Ignoring jetsam update because this process is not memory-managed
default	20:19:40.377496-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] Ignoring suspend because this process is not lifecycle managed
default	20:19:40.377506-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] Ignoring GPU update because this process is not GPU managed
default	20:19:40.377532-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] Ignoring memory limit update because this process is not memory-managed
default	20:19:40.380072-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:19:40.475764-0500	ControlCenter	Received state update for 35344 (app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>, running-active-NotVisible
default	20:19:40.476012-0500	gamepolicyd	Received state update for 35344 (app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>, running-active-NotVisible
default	20:19:40.869652-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0x10}
default	20:19:40.870590-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1e804b","name":"Nexy(35344)"}, "details":{"deviceUIDs":["1C-77-54-18-C8-A3:output"],"implicit_category":"MediaPlayback","input_running":false,"output_running":true} }
default	20:19:40.870769-0500	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 76, PID = 35344, Name = sid:0x1e804b, Nexy(35344), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO> is going active
default	20:19:40.870786-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsPlaying:]: MXCoreSession com.nexy.assistant with category/mode MediaPlayback/Default and coreSessionID = 76 starting playing
default	20:19:40.870862-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 76, PID = 35344, Name = sid:0x1e804b, Nexy(35344), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	20:19:40.870918-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 76, PID = 35344, Name = sid:0x1e804b, Nexy(35344), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO>
default	20:19:40.870949-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1e804b, Nexy(35344), 'prim'', displayID:'com.nexy.assistant'}
default	20:19:40.871005-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 201, deviceID = <private>
default	20:19:40.871043-0500	audiomxd	AudioApplicationInfoImpl.mm:395   Successfully updated session 0x1e804b to isSessionRecording: 0
	app: {"name":"[implicit] Nexy","pid":35344}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1e804b, sessionType: 'prim', isRecording: false }, 
]
default	20:19:40.871140-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 1]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)}
default	20:19:40.871174-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	20:19:40.871310-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 201 flag 0x1 < Hijack > app com.nexy.assistant CID 0x4D120001 category Not set
default	20:19:40.871541-0500	audiomxd	UpdateAudioState CID 0x4D120001 audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	20:19:40.871638-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 201,
}
default	20:19:40.871666-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	20:19:40.871685-0500	audioaccessoryd	AudioStateChanged: Added audio session app com.nexy.assistant NULL -> 201 count 1
default	20:19:40.871695-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 201
error	20:19:40.871707-0500	audioaccessoryd	Updating local audio category 100 -> 201 app com.nexy.assistant
error	20:19:40.871757-0500	audioaccessoryd	Relaying via 24B92680-715A-E821-B5AF-358E78C2DAF9 inWxAddress 1C:77:54:18:C8:A3 to 88:20:0D:45:06:51 with options {
    "playingApp" : "com.nexy.assistant",
    "hostStreamingState" : "YES",
    "btAddress" : "A0:9A:8E:0D:58:86",
    "btName" : "Mac",
    "otherDeviceAudioCategory" : 201,
}
default	20:19:40.871830-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.nexy.assistant
default	20:19:40.881499-0500	Nexy	[com.apple.controlcenter:CF336ADA-7E66-44CB-8D20-6275B996AAE4] Sending action(s) in update: NSSceneFenceAction
default	20:19:41.131896-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Output {1C-77-54-18-C8-A3:output, 0x10}
default	20:19:41.132301-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1e804b","name":"Nexy(35344)"}, "details":{"deviceUIDs":[],"implicit_category":"","input_running":false,"output_running":false} }
default	20:19:41.132457-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsPlaying:]: MXCoreSession com.nexy.assistant with category/mode MediaPlayback/Default and coreSessionID = 76 stopping playing
default	20:19:41.132541-0500	audiomxd	-MXCoreSession- -[MXCoreSession endInterruption:]: Session <ID: 76, PID = 35344, Name = sid:0x1e804b, Nexy(35344), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> is going inactive
default	20:19:41.132616-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 76, PID = 35344, Name = sid:0x1e804b, Nexy(35344), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	20:19:41.132733-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 76, PID = 35344, Name = sid:0x1e804b, Nexy(35344), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	20:19:41.132872-0500	audiomxd	UpdateAudioState CID 0x4D120001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:19:41.132987-0500	audiomxd	AudioApplicationInfoImpl.mm:395   Successfully updated session 0x1e804b to isSessionRecording: 0
	app: {"name":"[implicit] Nexy","pid":35344}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1e804b, sessionType: 'prim', isRecording: false }, 
]
default	20:19:41.133126-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 0]. BT device UIDS: {(
)}
default	20:19:41.133132-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:19:41.133164-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	20:19:41.133225-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:19:41.133265-0500	audioaccessoryd	AudioStateChanged: Removed audio session app com.nexy.assistant 201 count 0
default	20:19:41.138278-0500	runningboardd	Invalidating assertion 403-35344-159379 (target:[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344]) from originator [app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344]
default	20:19:41.138545-0500	runningboardd	Invalidating assertion 403-338-159380 (target:[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344]) from originator [osservice<com.apple.powerd>:338]
default	20:19:41.141536-0500	coreaudiod	Sending message. { reporterID=151801324109832, category=IO, type=error, message=["wg_cycles": Optional(804600), "HostApplicationDisplayID": Optional(com.nexy.assistant), "input_device_uid_list": Optional(), "careporting_timestamp": 1764119981.141336, "HAL_client_IO_duration": Optional(27492583), "io_buffer_size": Optional(512), "num_continuous_silent_io_cycles": Optional(10), "start_time": Optional(2266120265788), "io_page_faults": Optional(0), "issue_type": Optional(overload), "deadline": Optional(14476), "io_cycle_budget": Optional(11354166), "other_active_clients": Optional([  ]), "output_device_source_list": Optional(Unknown), "cause": Optional(ClientHALIODurationExceededBudget,SafetyViolationOccurred), "is_prewarming": Optional(0), "num_continuous_nonzero_io_cycles": Optional(0), "lateness": Optional(784), "smallest_buffer_frame_size": Optional(2147483647), "input_device_transport_list": Optional(), "io_cycle": Optional(22), "safety_violation_time_gap": Optional(0.01695833333333333), "cause_set": Optional(12), "io_page_faults_duration": Option<…> }
default	20:19:41.243153-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] Ignoring jetsam update because this process is not memory-managed
default	20:19:41.243170-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] Ignoring suspend because this process is not lifecycle managed
default	20:19:41.243181-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] Ignoring GPU update because this process is not GPU managed
default	20:19:41.243204-0500	runningboardd	[app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>:35344] Ignoring memory limit update because this process is not memory-managed
default	20:19:41.247623-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:19:41.248209-0500	ControlCenter	Received state update for 35344 (app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>, running-active-NotVisible
default	20:19:41.248351-0500	gamepolicyd	Received state update for 35344 (app<application.com.nexy.assistant.27241569.27241575.92A7CB8C-2703-47F9-BF09-04A06A00E84F(501)>, running-active-NotVisible

