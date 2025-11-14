default	10:08:37.045850-0500	lsd	com.nexy.assistant/Unknown Persona:5:5:1:1:Building bundle record for app
default	10:08:37.045994-0500	lsd	com.nexy.assistant/Unknown Persona:5:5:2:1:Built bundle record for app
default	10:08:37.047415-0500	lsd	com.nexy.assistant/Unknown Persona:5:4:2:1:_LSServerRegisterItemInfo result = 0
default	10:08:37.053884-0500	runningboardd	Launch request for app<application.com.nexy.assistant.22956984.22956990(501)>[0] is using uid 501 (divined from auid 501 euid 501)
default	10:08:37.053956-0500	runningboardd	Acquiring assertion targeting app<application.com.nexy.assistant.22956984.22956990(501)> from originator [osservice<com.apple.coreservices.uiagent(501)>:941] with description <RBSAssertionDescriptor| "LS launch com.nexy.assistant" ID:585-941-276710 target:app<application.com.nexy.assistant.22956984.22956990(501)> attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"LaunchRoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	10:08:37.054034-0500	runningboardd	Assertion 585-941-276710 (target:app<application.com.nexy.assistant.22956984.22956990(501)>) will be created as active
default	10:08:37.053610-0500	dmd	Received xpc stream event (distributed notification matching) with name: com.apple.LaunchServices.applicationRegistered user info: {
    CFBundleDisplayName = Nexy;
    bundleIDs =     (
        "com.nexy.assistant"
    );
    isPlaceholder = 0;
}
default	10:08:37.058455-0500	runningboardd	Checking PreventLaunch: global:0 exPath:/Applications/Nexy.app/Contents/MacOS/Nexy predicates:(null) allow:(null)
default	10:08:37.058485-0500	runningboardd	Creating and launching job for: app<application.com.nexy.assistant.22956984.22956990(501)>
default	10:08:37.058499-0500	runningboardd	_mutateContextIfNeeded called for com.nexy.assistant
default	10:08:37.058557-0500	runningboardd	app<application.com.nexy.assistant.22956984.22956990(501)>: -[RBPersonaManager personaForIdentity:context:personaUID:personaUniqueString:] required 0.000000 ms (wallclock); resolved to {4294967295, (null)}
default	10:08:37.087766-0500	runningboardd	[app<application.com.nexy.assistant.22956984.22956990(501)>:66242] is not RunningBoard jetsam managed.
default	10:08:37.087790-0500	runningboardd	[app<application.com.nexy.assistant.22956984.22956990(501)>:66242] This process will not be managed.
default	10:08:37.087799-0500	runningboardd	Now tracking process: [app<application.com.nexy.assistant.22956984.22956990(501)>:66242]
default	10:08:37.087990-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.22956984.22956990(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	10:08:37.089874-0500	gamepolicyd	Hit the server for a process handle 5404e5e000102c2 that resolved to: [app<application.com.nexy.assistant.22956984.22956990(501)>:66242]
default	10:08:37.089924-0500	gamepolicyd	Received state update for 66242 (app<application.com.nexy.assistant.22956984.22956990(501)>, running-active-NotVisible
default	10:08:37.095206-0500	runningboardd	Using default underlying assertion for app: [app<application.com.nexy.assistant.22956984.22956990(501)>:66242]
default	10:08:37.095272-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.22956984.22956990(501)>:66242] from originator [app<application.com.nexy.assistant.22956984.22956990(501)>:66242] with description <RBSAssertionDescriptor| "RB Underlying Assertion" ID:585-585-276711 target:66242 attributes:[
	<RBSDomainAttribute| domain:"com.apple.underlying" name:"defaultUnderlyingAppAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	10:08:37.095412-0500	runningboardd	Assertion 585-585-276711 (target:[app<application.com.nexy.assistant.22956984.22956990(501)>:66242]) will be created as active
default	10:08:37.095613-0500	runningboardd	[app<application.com.nexy.assistant.22956984.22956990(501)>:66242] Ignoring jetsam update because this process is not memory-managed
default	10:08:37.095628-0500	runningboardd	[app<application.com.nexy.assistant.22956984.22956990(501)>:66242] Ignoring suspend because this process is not lifecycle managed
default	10:08:37.095644-0500	runningboardd	[app<application.com.nexy.assistant.22956984.22956990(501)>:66242] Set darwin role to: UserInteractive
default	10:08:37.095668-0500	runningboardd	[app<application.com.nexy.assistant.22956984.22956990(501)>:66242] Ignoring GPU update because this process is not GPU managed
default	10:08:37.095700-0500	runningboardd	[app<application.com.nexy.assistant.22956984.22956990(501)>:66242] Ignoring memory limit update because this process is not memory-managed
default	10:08:37.095753-0500	runningboardd	[app<application.com.nexy.assistant.22956984.22956990(501)>:66242] reported to RB as running
default	10:08:37.097676-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.22956984.22956990(501)>:66242] from originator [osservice<com.apple.coreservices.launchservicesd>:549] with description <RBSAssertionDescriptor| "uielement:66242" ID:585-549-276712 target:66242 attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"RoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	10:08:37.097965-0500	runningboardd	Assertion 585-549-276712 (target:[app<application.com.nexy.assistant.22956984.22956990(501)>:66242]) will be created as active
default	10:08:37.097980-0500	CoreServicesUIAgent	LAUNCH: 0x0-0x170170 com.nexy.assistant starting stopped process.
default	10:08:37.099605-0500	loginwindow	-[Application updateInformation] | Got App URL: file:///Applications/Nexy.app/
default	10:08:37.099802-0500	loginwindow	-[Application setState:] | enter: <Application: 0x8f500bde0: Nexy> state 2
default	10:08:37.099828-0500	loginwindow	-[ApplicationManager checkInAppContext:eventData:] | ApplicationManager: Checked in app : Nexy
default	10:08:37.100496-0500	runningboardd	[app<application.com.nexy.assistant.22956984.22956990(501)>:66242] Ignoring jetsam update because this process is not memory-managed
default	10:08:37.100545-0500	runningboardd	[app<application.com.nexy.assistant.22956984.22956990(501)>:66242] Ignoring suspend because this process is not lifecycle managed
default	10:08:37.100613-0500	runningboardd	[app<application.com.nexy.assistant.22956984.22956990(501)>:66242] Ignoring GPU update because this process is not GPU managed
default	10:08:37.100713-0500	runningboardd	[app<application.com.nexy.assistant.22956984.22956990(501)>:66242] Ignoring memory limit update because this process is not memory-managed
default	10:08:37.100805-0500	runningboardd	Successfully acquired underlying assertion for [app<application.com.nexy.assistant.22956984.22956990(501)>:66242]
default	10:08:37.106010-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.22956984.22956990(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	10:08:37.106362-0500	runningboardd	Invalidating assertion 585-941-276710 (target:app<application.com.nexy.assistant.22956984.22956990(501)>) from originator [osservice<com.apple.coreservices.uiagent(501)>:941]
default	10:08:37.106425-0500	runningboardd	[app<application.com.nexy.assistant.22956984.22956990(501)>:66242] Ignoring jetsam update because this process is not memory-managed
default	10:08:37.106488-0500	runningboardd	[app<application.com.nexy.assistant.22956984.22956990(501)>:66242] Ignoring suspend because this process is not lifecycle managed
default	10:08:37.106523-0500	runningboardd	[app<application.com.nexy.assistant.22956984.22956990(501)>:66242] Ignoring GPU update because this process is not GPU managed
default	10:08:37.106617-0500	runningboardd	[app<application.com.nexy.assistant.22956984.22956990(501)>:66242] Ignoring memory limit update because this process is not memory-managed
default	10:08:37.106534-0500	gamepolicyd	Received state update for 66242 (app<application.com.nexy.assistant.22956984.22956990(501)>, running-active-NotVisible
default	10:08:37.112948-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.22956984.22956990(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	10:08:37.210402-0500	runningboardd	[app<application.com.nexy.assistant.22956984.22956990(501)>:66242] Ignoring jetsam update because this process is not memory-managed
default	10:08:37.210422-0500	runningboardd	[app<application.com.nexy.assistant.22956984.22956990(501)>:66242] Ignoring suspend because this process is not lifecycle managed
default	10:08:37.210509-0500	gamepolicyd	Received state update for 66242 (app<application.com.nexy.assistant.22956984.22956990(501)>, running-active-NotVisible
default	10:08:37.210444-0500	runningboardd	[app<application.com.nexy.assistant.22956984.22956990(501)>:66242] Ignoring GPU update because this process is not GPU managed
default	10:08:37.210484-0500	runningboardd	[app<application.com.nexy.assistant.22956984.22956990(501)>:66242] Ignoring memory limit update because this process is not memory-managed
default	10:08:37.216043-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.22956984.22956990(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	10:08:37.216502-0500	gamepolicyd	Received state update for 66242 (app<application.com.nexy.assistant.22956984.22956990(501)>, running-active-NotVisible
default	10:08:37.319885-0500	syspolicyd	GK evaluateScanResult: 3, PST: (path: a2cffff67b96be6e), (team: 5NKLL2CLB9), (id: com.nexy.assistant), (bundle_id: (null)), 0, 0, 1, 0, 9, 4, 1
default	10:08:37.321557-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=636.19, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=66242, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.syspolicyd, pid=636, auid=0, euid=0, binary_path=/usr/libexec/syspolicyd}, },
default	10:08:37.329390-0500	tccd	AUTHREQ_SUBJECT: msgID=636.19, subject=com.nexy.assistant,
default	10:08:37.330991-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc90d7f300 at /Applications/Nexy.app
default	10:08:37.475016-0500	Nexy	[0x1038718e0] activating connection: mach=true listener=false peer=false name=com.apple.cfprefsd.daemon
default	10:08:37.475090-0500	Nexy	[0x103871e20] activating connection: mach=true listener=false peer=false name=com.apple.cfprefsd.agent
error	10:08:37.745595-0500	Nexy	dlsym cannot find symbol NSMakeRect in CFBundle 0x89b6040e0 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	10:08:37.745841-0500	Nexy	dlsym cannot find symbol NSMakePoint in CFBundle 0x89b6040e0 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	10:08:37.746048-0500	Nexy	dlsym cannot find symbol NSMakeSize in CFBundle 0x89b6040e0 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	10:08:37.746248-0500	Nexy	dlsym cannot find symbol NSMakeRange in CFBundle 0x89b6040e0 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
default	10:08:37.747262-0500	Nexy	[0x10387ba00] activating connection: mach=true listener=false peer=false name=com.apple.coreservices.launchservicesd
default	10:08:37.747848-0500	Nexy	[0x89a6c8000] activating connection: mach=true listener=false peer=false name=com.apple.analyticsd
default	10:08:37.748169-0500	Nexy	[0x89a6c8140] activating connection: mach=true listener=false peer=false name=com.apple.pasteboard.1
default	10:08:37.748553-0500	Nexy	[0x89a6c8280] activating connection: mach=true listener=false peer=false name=com.apple.distributed_notifications@Uv3
default	10:08:37.748763-0500	Nexy	Received configuration update from daemon (initial)
default	10:08:37.750361-0500	Nexy	void _NSDisableAutomaticTerminationAndLog(NSString *) No windows open yet
default	10:08:37.750695-0500	Nexy	[0x89a6c83c0] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	10:08:37.751235-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=66242.1, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=66242, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	10:08:37.752526-0500	tccd	AUTHREQ_SUBJECT: msgID=66242.1, subject=com.nexy.assistant,
default	10:08:37.753196-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc90d7d500 at /Applications/Nexy.app
default	10:08:37.766177-0500	Nexy	[0x89a6c83c0] invalidated after the last release of the connection object
default	10:08:37.766494-0500	Nexy	server port 0x0000330f, session port 0x0000330f
default	10:08:37.767347-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=582.1054, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=66242, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=582, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	10:08:37.767370-0500	tccd	requestor: TCCDProcess: identifier=com.apple.WindowServer, pid=582, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=66242, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	10:08:37.768078-0500	tccd	AUTHREQ_SUBJECT: msgID=582.1054, subject=com.nexy.assistant,
default	10:08:37.768861-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc90d7d500 at /Applications/Nexy.app
default	10:08:37.788075-0500	Nexy	New connection 0xc08f3 main
default	10:08:37.790107-0500	Nexy	CHECKIN: pid=66242
default	10:08:37.800524-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.22956984.22956990(501)>:66242] from originator [osservice<com.apple.coreservices.launchservicesd>:549] with description <RBSAssertionDescriptor| "uielement:66242" ID:585-549-276715 target:66242 attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"RoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	10:08:37.800637-0500	launchservicesd	CHECKIN:0x0-0x170170 66242 com.nexy.assistant
default	10:08:37.800620-0500	runningboardd	Assertion 585-549-276715 (target:[app<application.com.nexy.assistant.22956984.22956990(501)>:66242]) will be created as active
default	10:08:37.800765-0500	Nexy	CHECKEDIN: pid=66242 asn=0x0-0x170170 foreground=0
default	10:08:37.801179-0500	runningboardd	Invalidating assertion 585-549-276712 (target:[app<application.com.nexy.assistant.22956984.22956990(501)>:66242]) from originator [osservice<com.apple.coreservices.launchservicesd>:549]
default	10:08:37.801071-0500	Nexy	[0x89a6c83c0] activating connection: mach=false listener=true peer=false name=(anonymous)
default	10:08:37.801146-0500	Nexy	[0x89a6c83c0] Connection returned listener port: 0x4503
default	10:08:37.801376-0500	Nexy	[0x89b724300] activating connection: mach=false listener=false peer=true name=com.apple.xpc.anonymous.0x89a6c83c0.peer[549].0x89b724300
default	10:08:37.802794-0500	loginwindow	-[Application updateInformation] | Got App URL: file:///Applications/Nexy.app/
default	10:08:37.802942-0500	loginwindow	-[ApplicationManager checkInAppContext:eventData:] | ApplicationManager: Checked in app : Nexy
default	10:08:37.805809-0500	Nexy	FRONTLOGGING: version 1
default	10:08:37.805849-0500	Nexy	Registered, pid=66242 ASN=0x0,0x170170
default	10:08:37.806157-0500	WindowServer	c08f3[CreateApplication]: Process creation: 0x0-0x170170 (Nexy) connectionID: C08F3 pid: 66242 in session 0x101
default	10:08:37.806322-0500	Nexy	[0x89a6c8500] activating connection: mach=true listener=false peer=false name=com.apple.lsd.mapdb
default	10:08:37.808902-0500	Nexy	[0x89a6c83c0] Connection returned listener port: 0x4503
default	10:08:37.810189-0500	Nexy	BringForward: pid=66242 asn=0x0-0x170170 bringForward=0 foreground=0 uiElement=1 launchedByLS=1 modifiersCount=1 allDisabled=0
default	10:08:37.810360-0500	Nexy	BringFrontModifier: pid=66242 asn=0x0-0x170170 Modifier 0 hideAfter=0 hideOthers=0 dontMakeFrontmost=0 mouseDown=0/0 seed=0/0
default	10:08:37.810908-0500	Nexy	Current system appearance, (HLTB: 1), (SLS: 0)
default	10:08:37.812191-0500	Nexy	No persisted cache on this platform.
default	10:08:37.813437-0500	Nexy	Current system appearance, (HLTB: 1), (SLS: 0)
default	10:08:37.813957-0500	Nexy	Post-registration system appearance: (HLTB: 1)
default	10:08:37.815853-0500	Nexy	FBSWorkspace: endpoint monitoring is disabled.
default	10:08:37.815864-0500	Nexy	FBSWorkspace: default shell endpoint is disabled.
default	10:08:37.815917-0500	Nexy	Initializing connection
default	10:08:37.815958-0500	Nexy	Removing all cached process handles
default	10:08:37.815984-0500	Nexy	Sending handshake request attempt #1 to server
default	10:08:37.815993-0500	Nexy	Creating connection to com.apple.runningboard
default	10:08:37.816000-0500	Nexy	[0x89a6c8640] activating connection: mach=true listener=false peer=false name=com.apple.runningboard
default	10:08:37.816447-0500	runningboardd	Setting client for [app<application.com.nexy.assistant.22956984.22956990(501)>:66242] as ready
default	10:08:37.817708-0500	Nexy	[0x89a6c83c0] Connection returned listener port: 0x4503
default	10:08:37.820630-0500	distnoted	register name: com.apple.xctest.FakeForceTouchDevice object: com.nexy.assistant token: 1e0000001d pid: 66242
default	10:08:37.821558-0500	Nexy	Handshake succeeded
default	10:08:37.821576-0500	Nexy	Identity resolved as app<application.com.nexy.assistant.22956984.22956990(501)>
default	10:08:37.823678-0500	Nexy	[0x89a6c83c0] Connection returned listener port: 0x4503
default	10:08:37.827311-0500	Nexy	Created a new Process Instance Registry XPC connection (inactive)
default	10:08:37.827332-0500	Nexy	[0x89a6c88c0] activating connection: mach=true listener=false peer=false name=com.apple.linkd.autoShortcut
default	10:08:37.827421-0500	Nexy	Activated connection to com.apple.linkd.autoShortcut (ApplicationService)
default	10:08:37.827474-0500	Nexy	[0x89a6c8780] activating connection: mach=false listener=true peer=false name=(anonymous)
default	10:08:37.828699-0500	Nexy	[0x89a6c8780] Connection returned listener port: 0x6b03
default	10:08:37.829404-0500	Nexy	Registered process with identifier 66242-142034
default	10:08:38.050124-0500	Nexy	Registered notify signal com.apple.caulk.alloc.rtdump (0)
default	10:08:38.053261-0500	Nexy	System_Input_Processing_Notification_Handler.mm:456   System_Input_Processing_Notification_Handler::is_vi_available(): Voice isolation DSP is available for client with bundle id com.nexy.assistant (AVFoundation is available, application is not in client deny list, application is not FaceTime variant)
default	10:08:38.055214-0500	Nexy	[0x89a6c8b40] activating connection: mach=true listener=false peer=false name=com.apple.cmio.registerassistantservice.system-extensions
fault	10:08:38.059467-0500	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.22956984.22956990 AUID=501> and <type=Application identifier=application.com.nexy.assistant.22956984.22956990>
default	10:08:38.063198-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOInitializeListenersForBundleID: for <private> -> <private>
default	10:08:38.064694-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> vpio_preferenceChangedListener: new value ((null)) for key AUVoiceIOClients/com-nexy-assistant/AUVoiceIOChatFlavor, translatedBundleID com.nexy.assistant, bundleIDs {(
    "com.nexy.assistant"
)}
default	10:08:38.064862-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> vpio_preferenceChangedListener: new value ((null)) for key AUVoiceIOClients/com-nexy-assistant/AUVoiceIOIsAutoChatFlavorEnabled, translatedBundleID com.nexy.assistant, bundleIDs {(
    "com.nexy.assistant"
)}
default	10:08:38.064982-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetSupportedChatFlavorsForBundleID: <private>-><private> get supported chat flavors: <private>
default	10:08:38.064991-0500	Nexy	            HALSystem.cpp:134    Enabling HAL Voice Isolation support
default	10:08:38.065186-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetHiddenChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	10:08:38.065308-0500	Nexy	[0x89a6c8c80] activating connection: mach=true listener=false peer=false name=com.apple.tccd
default	10:08:38.065668-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOHiddenChatFlavors newValue: (
    1
)
default	10:08:38.066107-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=66242.2, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=66242, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	10:08:38.072824-0500	tccd	AUTHREQ_SUBJECT: msgID=66242.2, subject=com.nexy.assistant,
default	10:08:38.073577-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x79418c300 at /Applications/Nexy.app
default	10:08:38.085746-0500	Nexy	[0x89a6c8c80] invalidated after the last release of the connection object
default	10:08:38.085794-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetSupportedChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	10:08:38.088376-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOSupportedChatFlavors newValue: (
)
default	10:08:38.089649-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=590.557, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=66242, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=579, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	10:08:38.090437-0500	tccd	AUTHREQ_SUBJECT: msgID=590.557, subject=com.nexy.assistant,
default	10:08:38.090976-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x79418c300 at /Applications/Nexy.app
error	10:08:38.103017-0500	tccd	Request message contains a target_token to accessing_process (TCCDProcess: identifier=com.nexy.assistant, pid=66242, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy) but TCCDProcess: identifier=com.apple.audio.coreaudiod, pid=590, auid=202, euid=202, binary_path=/usr/sbin/coreaudiod is not a TCC manager for service: kTCCServiceScreenCapture.
default	10:08:38.103792-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=590.559, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=66242, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=579, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	10:08:38.104523-0500	tccd	AUTHREQ_SUBJECT: msgID=590.559, subject=com.nexy.assistant,
default	10:08:38.105047-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x79418c300 at /Applications/Nexy.app
default	10:08:38.118505-0500	Nexy	  HALPlugInManagement.cpp:440    HALPlugInManagement::RegisterPlugIns: skipping in-process plug-ins
error	10:08:38.118699-0500	Nexy	AddInstanceForFactory: No factory registered for id <CFUUID 0x89b7fcb80> F8BB1C28-BAE8-11D6-9C31-00039315CD46
default	10:08:38.135354-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	10:08:38.135683-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	10:08:38.141273-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetPreferredChatFlavorForBundleID: <private>-><private> get value: 0
default	10:08:40.454469-0500	kernel	SK[6]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 5EDF340E-E9F7-4A1D-96B3-EDDAB576BC55 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.64350,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0x82cfadff tp_proto=0x06"
default	10:08:40.454514-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:64350<-><IPv4-redacted>:53] interface: utun6 (skipped: 2519)
so_gencnt: 495999 t_state: SYN_SENT process: Nexy:66242 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x85ce6994
default	10:08:40.454828-0500	kernel	tcp connected: [<IPv4-redacted>:64350<-><IPv4-redacted>:53] interface: utun6 (skipped: 2519)
so_gencnt: 495999 t_state: ESTABLISHED process: Nexy:66242 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x85ce6994
default	10:08:40.455095-0500	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:64350<-><IPv4-redacted>:53] interface: utun6 (skipped: 2519)
so_gencnt: 495999 t_state: FIN_WAIT_1 process: Nexy:66242 Duration: 0.001 sec Conn_Time: 0.001 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 1.000 ms rttvar: 0.500 ms base rtt: 1 ms so_error: 0 svc/tc: 0 flow: 0x85ce6994
default	10:08:40.455104-0500	kernel	tcp_connection_summary [<IPv4-redacted>:64350<-><IPv4-redacted>:53] interface: utun6 (skipped: 2519)
so_gencnt: 495999 t_state: FIN_WAIT_1 process: Nexy:66242 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	10:08:40.482284-0500	Nexy	[0x89a6c8c80] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioComponentRegistrar
default	10:08:40.498275-0500	Nexy	                AUHAL.cpp:420   AUHAL: (0x899114040) Selecting device 83 from constructor
default	10:08:40.498286-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0x899114040)
default	10:08:40.498291-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0x899114040) not already running
default	10:08:40.498295-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0x899114040) nothing to teardown
default	10:08:40.498298-0500	Nexy	                AUHAL.cpp:762   SelectDevice: (0x899114040) connecting device 83
default	10:08:40.498372-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0x899114040) Device ID: 83 (Input:No | Output:Yes): true
default	10:08:40.498686-0500	Nexy	                AUHAL.cpp:774   SelectDevice: (0x899114040) created ioproc 0xa for device 83
default	10:08:40.498768-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x899114040) adding 7 device listeners to device 83
default	10:08:40.498898-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x899114040) adding 0 device delegate listeners to device 83
default	10:08:40.498908-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x899114040)
default	10:08:40.498970-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x54]:  2 ch,  48000 Hz, Float32, interleaved
default	10:08:40.498979-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	10:08:40.498985-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	10:08:40.498991-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	10:08:40.499000-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	10:08:40.499077-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x899114040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	10:08:40.499085-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x899114040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	10:08:40.499090-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	10:08:40.499094-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x899114040) removing 0 device listeners from device 0
default	10:08:40.499098-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x899114040) removing 0 device delegate listeners from device 0
default	10:08:40.499102-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0x899114040)
default	10:08:40.499113-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is DISABLED
default	10:08:40.499181-0500	Nexy	                AUHAL.cpp:2303  SetProperty: (0x899114040) caller requesting device change from 83 to 89
default	10:08:40.499187-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0x899114040)
default	10:08:40.499191-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0x899114040) not already running
default	10:08:40.499196-0500	Nexy	                AUHAL.cpp:687   SelectDevice: (0x899114040) disconnecting device 83
default	10:08:40.499202-0500	Nexy	                AUHAL.cpp:751   SelectDevice: (0x899114040) destroying ioproc 0xa for device 83
default	10:08:40.499880-0500	Nexy	  AVAudioSession_MacOS.mm:1021  initForMacOS
default	10:08:40.501111-0500	Nexy	[0x89a6c8f00] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioSession
default	10:08:40.502686-0500	audiomxd	  ServerSessionManager.mm:315   { "action":"create_session", "session":{"ID":"0x280021","name":"Nexy(66242)"}, "details":{"PID":66242,"session_type":"Primary"} }
default	10:08:40.502762-0500	audiomxd	AudioApplicationInfoImpl.mm:250   Setting initial isRecording state: 0 for newly-created AudioApp
	app: {"name":"[implicit] Nexy","pid":66242}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x280021, sessionType: 'prim', isRecording: false }, 
]
default	10:08:40.503340-0500	audiomxd	  ServerSessionManager.mm:1322  Start process monitoring, pid = 66242, name = Nexy
default	10:08:40.503565-0500	Nexy	    SessionCore_Create.mm:99    Created session 0x89a599240 with ID: 0x280021
default	10:08:40.504986-0500	Nexy	[0x89a6c9040] activating connection: mach=true listener=false peer=false name=com.apple.audioanalyticsd
error	10:08:40.505615-0500	Nexy	Reporter disconnected. { function=sendMessage, reporterID=284507223621633 }
default	10:08:40.505630-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped Unknown {1C-77-54-18-C8-A3:output, 0xa}
default	10:08:40.505680-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	10:08:40.505769-0500	Nexy	                AUHAL.cpp:762   SelectDevice: (0x899114040) connecting device 89
default	10:08:40.505846-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0x899114040) Device ID: 89 (Input:Yes | Output:No): true
default	10:08:40.506863-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=590.560, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=66242, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=579, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	10:08:40.507780-0500	tccd	AUTHREQ_SUBJECT: msgID=590.560, subject=com.nexy.assistant,
default	10:08:40.508342-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x79418c300 at /Applications/Nexy.app
default	10:08:40.520842-0500	tccd	AUTHREQ_PROMPTING: msgID=590.560, service=kTCCServiceMicrophone, subject=Sub:{com.nexy.assistant}Resp:{TCCDProcess: identifier=com.nexy.assistant, pid=66242, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy},
default	10:08:42.080691-0500	runningboardd	Assertion did invalidate due to timeout: 585-585-276711 (target:[app<application.com.nexy.assistant.22956984.22956990(501)>:66242])
default	10:08:42.274780-0500	runningboardd	[app<application.com.nexy.assistant.22956984.22956990(501)>:66242] Ignoring jetsam update because this process is not memory-managed
default	10:08:42.274801-0500	runningboardd	[app<application.com.nexy.assistant.22956984.22956990(501)>:66242] Ignoring suspend because this process is not lifecycle managed
default	10:08:42.274816-0500	runningboardd	[app<application.com.nexy.assistant.22956984.22956990(501)>:66242] Ignoring GPU update because this process is not GPU managed
default	10:08:42.274852-0500	runningboardd	[app<application.com.nexy.assistant.22956984.22956990(501)>:66242] Ignoring memory limit update because this process is not memory-managed
default	10:08:42.280632-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.22956984.22956990(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	10:08:42.281315-0500	gamepolicyd	Received state update for 66242 (app<application.com.nexy.assistant.22956984.22956990(501)>, running-active-NotVisible
default	10:08:42.318371-0500	Nexy	                AUHAL.cpp:774   SelectDevice: (0x899114040) created ioproc 0xa for device 89
default	10:08:42.317528-0500	tccd	Publishing <TCCDEvent: type=Create, service=kTCCServiceMicrophone, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 3 subscribers: {
    671 = "<TCCDEventSubscriber: token=671, state=Passed, csid=com.apple.chronod>";
    460 = "<TCCDEventSubscriber: token=460, state=Initial, csid=(null)>";
    476 = "<TCCDEventSubscriber: token=476, state=Passed, csid=com.apple.photolibraryd>";
}
default	10:08:42.318638-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x899114040) adding 7 device listeners to device 89
default	10:08:42.318919-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x899114040) adding 0 device delegate listeners to device 89
default	10:08:42.318938-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x899114040)
default	10:08:42.318953-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 output streams; not all mono
default	10:08:42.318970-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	10:08:42.318845-0500	chronod	[appAuth:com.nexy.assistant] tcc authorization(s) changed
default	10:08:42.319175-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  input stream 0 [0x5a]:  1 ch,  24000 Hz, Float32
default	10:08:42.319192-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 input streams; all mono
default	10:08:42.319200-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  1 ch,  24000 Hz, Float32
default	10:08:42.319341-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x899114040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	10:08:42.319358-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x899114040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	10:08:42.319365-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	10:08:42.319372-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x899114040) removing 7 device listeners from device 83
default	10:08:42.319600-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x899114040) removing 0 device delegate listeners from device 83
default	10:08:42.319614-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0x899114040)
default	10:08:42.320533-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	10:08:42.322300-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=590.561, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=66242, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=579, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	10:08:42.323746-0500	tccd	AUTHREQ_SUBJECT: msgID=590.561, subject=com.nexy.assistant,
default	10:08:42.325104-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x79418c300 at /Applications/Nexy.app
default	10:08:42.341871-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	10:08:42.342971-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=590.562, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=66242, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=579, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	10:08:42.343951-0500	tccd	AUTHREQ_SUBJECT: msgID=590.562, subject=com.nexy.assistant,
default	10:08:42.344554-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x79418c300 at /Applications/Nexy.app
default	10:08:42.360873-0500	Nexy	Registered notify signal com.apple.caulk.alloc.audiodump (0)
default	10:08:42.362916-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=590.563, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=66242, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=579, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	10:08:42.363850-0500	tccd	AUTHREQ_SUBJECT: msgID=590.563, subject=com.nexy.assistant,
default	10:08:42.364588-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x79418c300 at /Applications/Nexy.app
default	10:08:42.377810-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetPreferredChatFlavorForBundleID: <private>-><private> get value: 0
default	10:08:42.378106-0500	coreaudiod	>>> NEGOTIATE [com.nexy.assistant]
default	10:08:42.378261-0500	coreaudiod	<<< NEGOTIATE [com.nexy.assistant]
default	10:08:42.378335-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetSupportedChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	10:08:42.379833-0500	coreaudiod	>>> ADAPT [com.nexy.assistant]
default	10:08:42.380840-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOSupportedChatFlavors newValue: (
    0,
    2
)
default	10:08:42.381537-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xa40759e00] Created node ADM::com.nexy.assistant_2350.2224.0_airpods noise suppression studio::in-0 with nodeID 0 - reporting period = 10.000000, sample rate = 24000.000000
default	10:08:42.381597-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xa40759e00] Created node ADM::com.nexy.assistant_2350.2224.0_airpods noise suppression studio::out-0 with nodeID 1 - reporting period = 10.000000, sample rate = 24000.000000
default	10:08:42.457016-0500	coreaudiod	<<< ADAPT [com.nexy.assistant]
default	10:08:42.458446-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:2350 called from <private>
default	10:08:42.458484-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	10:08:42.458519-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Input {1C-77-54-18-C8-A3:input, 0xa}
default	10:08:42.459275-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2349)
default	10:08:42.459291-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2349 called from <private>
default	10:08:42.459296-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2349 called from <private>
default	10:08:42.459760-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2350 called from <private>
default	10:08:42.459886-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2350)
default	10:08:42.459924-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2350 called from <private>
default	10:08:42.459969-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2350 called from <private>
default	10:08:42.467394-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	10:08:42.468203-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	10:08:42.467658-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.22956984.22956990(501)>:66242] from originator [osservice<com.apple.powerd>:520] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:585-520-276742 target:66242 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	10:08:42.467883-0500	runningboardd	Assertion 585-520-276742 (target:[app<application.com.nexy.assistant.22956984.22956990(501)>:66242]) will be created as active
default	10:08:42.471544-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2350)
default	10:08:42.471565-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2350)
default	10:08:42.471574-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2350)
default	10:08:42.471666-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2350)
default	10:08:42.473126-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2350 called from <private>
default	10:08:42.473134-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2350 called from <private>
default	10:08:42.473148-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2350 called from <private>
default	10:08:42.474947-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x280021","name":"Nexy(66242)"}, "details":{"deviceUIDs":["1C-77-54-18-C8-A3:input"],"implicit_category":"Record","input_running":true,"output_running":false} }
default	10:08:42.475477-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 34, PID = 66242, Name = sid:0x280021, Nexy(66242), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	10:08:42.475833-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 34, PID = 66242, Name = sid:0x280021, Nexy(66242), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	10:08:42.476738-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 34, PID = 66242, Name = sid:0x280021, Nexy(66242), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	10:08:42.476902-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 34, PID = 66242, Name = sid:0x280021, Nexy(66242), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	10:08:42.477097-0500	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 34, PID = 66242, Name = sid:0x280021, Nexy(66242), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> is going active
default	10:08:42.477145-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x280021, Nexy(66242), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 34 starting recording
default	10:08:42.476948-0500	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x280021, Nexy(66242), 'prim'', AudioCategory changed to 'Record_WithBluetooth'
default	10:08:42.473193-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2350 called from <private>
default	10:08:42.473229-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2350 called from <private>
default	10:08:42.477408-0500	audiomxd	UpdateAudioState CID 0xBDB10001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	10:08:42.477515-0500	audiomxd	UpdateAudioState CID 0xBDB10001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	10:08:42.477726-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 34, PID = 66242, Name = sid:0x280021, Nexy(66242), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	10:08:42.473346-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2350 called from <private>
default	10:08:42.473400-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2350 called from <private>
default	10:08:42.477838-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 34, PID = 66242, Name = sid:0x280021, Nexy(66242), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	10:08:42.473685-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2349)
default	10:08:42.474554-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2350)
default	10:08:42.477921-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x280021, Nexy(66242), 'prim'', displayID:'com.nexy.assistant'}
default	10:08:42.476160-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=590.564, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=66242, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=579, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	10:08:42.478149-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [1, 0]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:input"
)}
default	10:08:42.477555-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	10:08:42.478154-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	10:08:42.478177-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	10:08:42.477725-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	10:08:42.484783-0500	tccd	AUTHREQ_SUBJECT: msgID=590.564, subject=com.nexy.assistant,
default	10:08:42.489831-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2349)
default	10:08:42.494560-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2349 called from <private>
default	10:08:42.494680-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2349 called from <private>
default	10:08:42.495570-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2349)
default	10:08:42.511892-0500	audioaccessoryd	MetricLog 'com.apple.bluetooth.SmartRouting.RouteActivity' : { "OtherTipiDeviceModel" : "iPhone", "InTipi" : "YES", "LocalScore" : 200, "RemoteScore" : 100, "NumOfApps" : 0, "BundleID" : "com.nexy.assistant", "ManualRouteUISource" : "NA", "Activity" : "Hijack_Accepted", "HijackVersion" : "V2", "ProductID" : 8219, "ManualRouteInputOutput" : "NA", "DestinationRoute" : "NA", "Route" : "VirtualBluetooth", }
default	10:08:42.511990-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	10:08:42.512001-0500	audioaccessoryd	AudioStateChanged: Added audio session app com.nexy.assistant NULL -> 200 count 1
default	10:08:42.512054-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
error	10:08:42.512203-0500	audioaccessoryd	Updating local audio category 100 -> 200 app com.nexy.assistant
error	10:08:42.512509-0500	audioaccessoryd	Relaying via 24B92680-715A-E821-B5AF-358E78C2DAF9 inWxAddress 1C:77:54:18:C8:A3 to 88:20:0D:45:06:51 with options {
    "playingApp" : "com.nexy.assistant",
    "hostStreamingState" : "NO",
    "btAddress" : "A0:9A:8E:0D:58:86",
    "btName" : "Mac",
    "otherDeviceAudioCategory" : 200,
}
default	10:08:42.516390-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2349 called from <private>
default	10:08:42.537292-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	10:08:42.537363-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	10:08:42.537401-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	10:08:42.537506-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	10:08:42.564191-0500	coreaudiod	>>> ADAPT [com.nexy.assistant]
default	10:08:42.565510-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xa40759e00] Created node ADM::com.nexy.assistant_2350.2224.0_airpods noise suppression studio::in-0 with nodeID 0 - reporting period = 10.000000, sample rate = 24000.000000
default	10:08:42.565571-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xa40759e00] Created node ADM::com.nexy.assistant_2350.2224.0_airpods noise suppression studio::out-0 with nodeID 1 - reporting period = 10.000000, sample rate = 24000.000000
default	10:08:42.600086-0500	coreaudiod	<<< ADAPT [com.nexy.assistant]
default	10:08:42.601845-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:2350 called from <private>
default	10:08:42.603323-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.22956984.22956990(501)>:66242] from originator [osservice<com.apple.powerd>:520] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:585-520-276745 target:66242 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	10:08:42.601881-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:2350 called from <private>
default	10:08:42.603394-0500	runningboardd	Assertion 585-520-276745 (target:[app<application.com.nexy.assistant.22956984.22956990(501)>:66242]) will be created as active
default	10:08:42.602737-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:2350 called from <private>
default	10:08:42.603137-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	10:08:42.604593-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2350 called from <private>
default	10:08:42.604763-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2350)
default	10:08:42.604782-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2350 called from <private>
default	10:08:42.604788-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2350 called from <private>
default	10:08:42.604866-0500	runningboardd	Invalidating assertion 585-520-276745 (target:[app<application.com.nexy.assistant.22956984.22956990(501)>:66242]) from originator [osservice<com.apple.powerd>:520]
default	10:08:42.605397-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	10:08:42.605537-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	10:08:42.605892-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2350)
default	10:08:42.606038-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2350 called from <private>
default	10:08:42.606048-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2350 called from <private>
default	10:08:42.606060-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2350 called from <private>
default	10:08:42.609061-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x79418c300 at /Applications/Nexy.app
default	10:08:42.609756-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	10:08:42.609814-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	10:08:42.609858-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	10:08:42.609980-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	10:08:42.610755-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	10:08:42.610780-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	10:08:42.627441-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:2350 called from <private>
default	10:08:42.629272-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.22956984.22956990(501)>:66242] from originator [osservice<com.apple.powerd>:520] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:585-520-276746 target:66242 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	10:08:42.629348-0500	runningboardd	Assertion 585-520-276746 (target:[app<application.com.nexy.assistant.22956984.22956990(501)>:66242]) will be created as active
default	10:08:42.629410-0500	runningboardd	[app<application.com.nexy.assistant.22956984.22956990(501)>:66242] Ignoring jetsam update because this process is not memory-managed
default	10:08:42.629429-0500	runningboardd	[app<application.com.nexy.assistant.22956984.22956990(501)>:66242] Ignoring suspend because this process is not lifecycle managed
default	10:08:42.629440-0500	runningboardd	[app<application.com.nexy.assistant.22956984.22956990(501)>:66242] Ignoring GPU update because this process is not GPU managed
default	10:08:42.629460-0500	runningboardd	[app<application.com.nexy.assistant.22956984.22956990(501)>:66242] Ignoring memory limit update because this process is not memory-managed
default	10:08:42.636210-0500	runningboardd	[app<application.com.nexy.assistant.22956984.22956990(501)>:66242] Ignoring jetsam update because this process is not memory-managed
default	10:08:42.636228-0500	runningboardd	[app<application.com.nexy.assistant.22956984.22956990(501)>:66242] Ignoring suspend because this process is not lifecycle managed
default	10:08:42.636240-0500	runningboardd	[app<application.com.nexy.assistant.22956984.22956990(501)>:66242] Ignoring GPU update because this process is not GPU managed
default	10:08:42.636295-0500	runningboardd	[app<application.com.nexy.assistant.22956984.22956990(501)>:66242] Ignoring memory limit update because this process is not memory-managed
default	10:08:42.636862-0500	gamepolicyd	Received state update for 66242 (app<application.com.nexy.assistant.22956984.22956990(501)>, running-active-NotVisible
default	10:08:42.640703-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	10:08:42.640742-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	10:08:42.640775-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	10:08:42.645515-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	10:08:42.645525-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	10:08:42.645534-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	10:08:42.645541-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	10:08:42.645586-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	10:08:42.645615-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	10:08:42.645656-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	10:08:42.645678-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	10:08:42.645692-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	10:08:42.645709-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	10:08:42.645740-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	10:08:42.645760-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	10:08:42.645864-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	10:08:42.646184-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	10:08:42.646192-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	10:08:42.646203-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	10:08:42.646209-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	10:08:42.646223-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	10:08:42.646228-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	10:08:43.106920-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.nexy.assistant, Score 200, Remote 100 NumofApp 1
default	10:08:43.657691-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xa}
default	10:08:43.657979-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x280021","name":"Nexy(66242)"}, "details":{"deviceUIDs":[],"implicit_category":"","input_running":false,"output_running":false} }
default	10:08:43.658119-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 34, PID = 66242, Name = sid:0x280021, Nexy(66242), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	10:08:43.658210-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 34, PID = 66242, Name = sid:0x280021, Nexy(66242), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	10:08:43.658262-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x280021, Nexy(66242), 'prim'', displayID:'com.nexy.assistant'}
default	10:08:43.658339-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x280021, Nexy(66242), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 34 stopping recording
default	10:08:43.658337-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	10:08:43.658380-0500	audiomxd	-MXCoreSession- -[MXCoreSession endInterruption:]: Session <ID: 34, PID = 66242, Name = sid:0x280021, Nexy(66242), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> is going inactive
default	10:08:43.658427-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 34, PID = 66242, Name = sid:0x280021, Nexy(66242), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	10:08:43.658660-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 200 flag 0x1 < Hijack > app com.nexy.assistant CID 0xBDB10001 category Not set
default	10:08:43.658478-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 34, PID = 66242, Name = sid:0x280021, Nexy(66242), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	10:08:43.658677-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 0]. BT device UIDS: {(
)}
default	10:08:43.658691-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	10:08:43.659590-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	10:08:43.659642-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	10:08:43.659713-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	10:08:43.659744-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	10:08:43.659307-0500	audiomxd	UpdateAudioState CID 0xBDB10001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	10:08:43.659511-0500	audiomxd	UpdateAudioState CID 0xBDB10001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	10:08:43.659835-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	10:08:43.659857-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	10:08:43.659915-0500	audioaccessoryd	AudioStateChanged: Removed audio session app com.nexy.assistant 201 count 0
default	10:08:43.662012-0500	runningboardd	Invalidating assertion 585-520-276746 (target:[app<application.com.nexy.assistant.22956984.22956990(501)>:66242]) from originator [osservice<com.apple.powerd>:520]
default	10:08:43.664094-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	10:08:43.666903-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	10:08:43.666920-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	10:08:43.666935-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	10:08:43.666944-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	10:08:43.666960-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	10:08:43.666969-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	10:08:43.667309-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	10:08:43.759768-0500	Nexy	                AUHAL.cpp:473   ~AUHAL: (0x899114040) Selecting device 0 from destructor
default	10:08:43.759793-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0x899114040)
default	10:08:43.759807-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0x899114040) not already running
default	10:08:43.759819-0500	Nexy	                AUHAL.cpp:687   SelectDevice: (0x899114040) disconnecting device 89
default	10:08:43.759833-0500	Nexy	                AUHAL.cpp:751   SelectDevice: (0x899114040) destroying ioproc 0xa for device 89
default	10:08:43.759874-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xa}
default	10:08:43.759932-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	10:08:43.760183-0500	Nexy	                AUHAL.cpp:853   SelectDevice: (0x899114040) nothing to setup
default	10:08:43.760210-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x899114040) adding 0 device listeners to device 0
default	10:08:43.760226-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x899114040) adding 0 device delegate listeners to device 0
default	10:08:43.760240-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x899114040) removing 7 device listeners from device 89
default	10:08:43.760726-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x899114040) removing 0 device delegate listeners from device 89
default	10:08:43.760759-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0x899114040)
default	10:08:43.765696-0500	runningboardd	[app<application.com.nexy.assistant.22956984.22956990(501)>:66242] Ignoring jetsam update because this process is not memory-managed
default	10:08:43.765712-0500	runningboardd	[app<application.com.nexy.assistant.22956984.22956990(501)>:66242] Ignoring suspend because this process is not lifecycle managed
default	10:08:43.765727-0500	runningboardd	[app<application.com.nexy.assistant.22956984.22956990(501)>:66242] Ignoring GPU update because this process is not GPU managed
default	10:08:43.765914-0500	runningboardd	[app<application.com.nexy.assistant.22956984.22956990(501)>:66242] Ignoring memory limit update because this process is not memory-managed
default	10:08:43.772206-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.22956984.22956990(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	10:08:43.772828-0500	gamepolicyd	Received state update for 66242 (app<application.com.nexy.assistant.22956984.22956990(501)>, running-active-NotVisible
default	10:08:44.022659-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=66246.1, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=66242, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.osascript, pid=66246, auid=501, euid=501, binary_path=/usr/bin/osascript}, },
default	10:08:44.024627-0500	tccd	AUTHREQ_SUBJECT: msgID=66246.1, subject=com.nexy.assistant,
default	10:08:44.025695-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc90d7d500 at /Applications/Nexy.app
default	10:08:44.042525-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=582.1061, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=66242, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.osascript, pid=66246, auid=501, euid=501, binary_path=/usr/bin/osascript}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=582, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	10:08:44.043538-0500	tccd	AUTHREQ_SUBJECT: msgID=582.1061, subject=com.nexy.assistant,
default	10:08:44.044241-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc90d7d500 at /Applications/Nexy.app
default	10:08:44.093225-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc90d7f300 at /Applications/Nexy.app
default	10:08:44.262767-0500	System Events	TCCAccessRequestIndirect: TCCAccessRequestIndirect with pid 66247: target_identity: {
    kTCCCodeIdentityAuditToken = {length = 32, bytes = 0xf5010000 f5010000 14000000 f5010000 ... af860100 db2a0200 };
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
default	10:08:44.274065-0500	tccd	target_executable_path_URL: file:///Applications/Nexy.app/Contents/MacOS/Nexy
default	10:08:44.533679-0500	Nexy	[0x89a6c9400] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	10:08:44.534400-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=66242.3, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=66242, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	10:08:44.535535-0500	tccd	AUTHREQ_SUBJECT: msgID=66242.3, subject=com.nexy.assistant,
default	10:08:44.536153-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc90d7d500 at /Applications/Nexy.app
default	10:08:44.551263-0500	Nexy	[0x89a6c9400] invalidated after the last release of the connection object
default	10:08:44.554084-0500	Nexy	                AUHAL.cpp:420   AUHAL: (0x899114040) Selecting device 83 from constructor
default	10:08:44.554095-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0x899114040)
default	10:08:44.554100-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0x899114040) not already running
default	10:08:44.554104-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0x899114040) nothing to teardown
default	10:08:44.554109-0500	Nexy	                AUHAL.cpp:762   SelectDevice: (0x899114040) connecting device 83
default	10:08:44.554222-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0x899114040) Device ID: 83 (Input:No | Output:Yes): true
default	10:08:44.554339-0500	Nexy	                AUHAL.cpp:774   SelectDevice: (0x899114040) created ioproc 0xb for device 83
default	10:08:44.554436-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x899114040) adding 7 device listeners to device 83
default	10:08:44.554600-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x899114040) adding 0 device delegate listeners to device 83
default	10:08:44.554606-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x899114040)
default	10:08:44.554678-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x54]:  2 ch,  24000 Hz, Float32, interleaved
default	10:08:44.554687-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	10:08:44.554692-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  24000 Hz, Float32, interleaved
default	10:08:44.554701-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	10:08:44.554708-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	10:08:44.554817-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x899114040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	10:08:44.554830-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x899114040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	10:08:44.554835-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	10:08:44.554846-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x899114040) removing 0 device listeners from device 0
default	10:08:44.554850-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x899114040) removing 0 device delegate listeners from device 0
default	10:08:44.554853-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0x899114040)
default	10:08:44.554872-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is DISABLED
default	10:08:44.554941-0500	Nexy	                AUHAL.cpp:2303  SetProperty: (0x899114040) caller requesting device change from 83 to 89
default	10:08:44.554951-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0x899114040)
default	10:08:44.554955-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0x899114040) not already running
default	10:08:44.554960-0500	Nexy	                AUHAL.cpp:687   SelectDevice: (0x899114040) disconnecting device 83
default	10:08:44.554965-0500	Nexy	                AUHAL.cpp:751   SelectDevice: (0x899114040) destroying ioproc 0xb for device 83
default	10:08:44.554987-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped Unknown {1C-77-54-18-C8-A3:output, 0xb}
default	10:08:44.555022-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	10:08:44.555102-0500	Nexy	                AUHAL.cpp:762   SelectDevice: (0x899114040) connecting device 89
default	10:08:44.555179-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0x899114040) Device ID: 89 (Input:Yes | Output:No): true
default	10:08:44.556426-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=590.567, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=66242, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=579, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	10:08:44.557396-0500	tccd	AUTHREQ_SUBJECT: msgID=590.567, subject=com.nexy.assistant,
default	10:08:44.557997-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x79418c300 at /Applications/Nexy.app
default	10:08:44.571373-0500	Nexy	                AUHAL.cpp:774   SelectDevice: (0x899114040) created ioproc 0xb for device 89
default	10:08:44.571497-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x899114040) adding 7 device listeners to device 89
default	10:08:44.571686-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x899114040) adding 0 device delegate listeners to device 89
default	10:08:44.571698-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x899114040)
default	10:08:44.571706-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 output streams; not all mono
default	10:08:44.571715-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	10:08:44.571836-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  input stream 0 [0x5a]:  1 ch,  24000 Hz, Float32
default	10:08:44.571847-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 input streams; all mono
default	10:08:44.571854-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  1 ch,  24000 Hz, Float32
default	10:08:44.571943-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x899114040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	10:08:44.571957-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x899114040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	10:08:44.571962-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	10:08:44.571965-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x899114040) removing 7 device listeners from device 83
default	10:08:44.572128-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x899114040) removing 0 device delegate listeners from device 83
default	10:08:44.572135-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0x899114040)
default	10:08:44.572716-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	10:08:44.573787-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=590.568, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=66242, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=579, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	10:08:44.574593-0500	tccd	AUTHREQ_SUBJECT: msgID=590.568, subject=com.nexy.assistant,
default	10:08:44.575140-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x79418c300 at /Applications/Nexy.app
default	10:08:44.588352-0500	Nexy	       ACv2Workarounds.mm:51    com.nexy.assistant: fix84702776_86723525_86479548_89800354_SinglePacketDesc: false
default	10:08:44.588448-0500	Nexy	       AudioConverter.cpp:1044  Created a new in process converter -> 0x89b5f2cd0, from  1 ch,  24000 Hz, Float32 to  1 ch,  16000 Hz, Float32
default	10:08:44.588649-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	10:08:44.589879-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=590.569, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=66242, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=579, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	10:08:44.591034-0500	tccd	AUTHREQ_SUBJECT: msgID=590.569, subject=com.nexy.assistant,
default	10:08:44.591743-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x79418c300 at /Applications/Nexy.app
default	10:08:44.607302-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=590.570, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=66242, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=579, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	10:08:44.608181-0500	tccd	AUTHREQ_SUBJECT: msgID=590.570, subject=com.nexy.assistant,
default	10:08:44.608757-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x79418c300 at /Applications/Nexy.app
default	10:08:44.632616-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x280021","name":"Nexy(66242)"}, "details":{"deviceUIDs":["1C-77-54-18-C8-A3:input"],"implicit_category":"Record","input_running":true,"output_running":false} }
default	10:08:44.632687-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 34, PID = 66242, Name = sid:0x280021, Nexy(66242), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	10:08:44.632707-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Category/Mode changed -- The score for sid:0x280021, Nexy(66242), 'prim'/com.nexy.assistant was not correct. Old score = 201
default	10:08:44.632736-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 34, PID = 66242, Name = sid:0x280021, Nexy(66242), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	10:08:44.632774-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.22956984.22956990(501)>:66242] from originator [osservice<com.apple.powerd>:520] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:585-520-276764 target:66242 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	10:08:44.632991-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 34, PID = 66242, Name = sid:0x280021, Nexy(66242), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	10:08:44.632857-0500	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x280021, Nexy(66242), 'prim'', AudioCategory changed to 'Record_WithBluetooth'
default	10:08:44.632855-0500	runningboardd	Assertion 585-520-276764 (target:[app<application.com.nexy.assistant.22956984.22956990(501)>:66242]) will be created as active
default	10:08:44.633081-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 34, PID = 66242, Name = sid:0x280021, Nexy(66242), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	10:08:44.630819-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Input {1C-77-54-18-C8-A3:input, 0xb}
default	10:08:44.633204-0500	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 34, PID = 66242, Name = sid:0x280021, Nexy(66242), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> is going active
default	10:08:44.633239-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x280021, Nexy(66242), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 34 starting recording
default	10:08:44.633455-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 34, PID = 66242, Name = sid:0x280021, Nexy(66242), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	10:08:44.633713-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 34, PID = 66242, Name = sid:0x280021, Nexy(66242), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	10:08:44.633799-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x280021, Nexy(66242), 'prim'', displayID:'com.nexy.assistant'}
default	10:08:44.633733-0500	runningboardd	[app<application.com.nexy.assistant.22956984.22956990(501)>:66242] Ignoring jetsam update because this process is not memory-managed
default	10:08:44.633439-0500	audiomxd	UpdateAudioState CID 0xBDB10001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	10:08:44.633918-0500	runningboardd	[app<application.com.nexy.assistant.22956984.22956990(501)>:66242] Ignoring suspend because this process is not lifecycle managed
default	10:08:44.633959-0500	runningboardd	[app<application.com.nexy.assistant.22956984.22956990(501)>:66242] Ignoring GPU update because this process is not GPU managed
default	10:08:44.633954-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	10:08:44.634007-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	10:08:44.634046-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	10:08:44.634026-0500	runningboardd	[app<application.com.nexy.assistant.22956984.22956990(501)>:66242] Ignoring memory limit update because this process is not memory-managed
default	10:08:44.634118-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	10:08:44.633898-0500	audiomxd	UpdateAudioState CID 0xBDB10001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	10:08:44.634011-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	10:08:44.634407-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 200 flag 0x1 < Hijack > app com.nexy.assistant CID 0xBDB10001 category Not set
default	10:08:44.634910-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	10:08:44.634973-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	10:08:44.635008-0500	audioaccessoryd	AudioStateChanged: Added audio session app com.nexy.assistant NULL -> 200 count 1
default	10:08:44.635037-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
error	10:08:44.635065-0500	audioaccessoryd	Updating local audio category 100 -> 200 app com.nexy.assistant
error	10:08:44.635200-0500	audioaccessoryd	Relaying via 24B92680-715A-E821-B5AF-358E78C2DAF9 inWxAddress 1C:77:54:18:C8:A3 to 88:20:0D:45:06:51 with options {
    "playingApp" : "com.nexy.assistant",
    "hostStreamingState" : "YES",
    "btAddress" : "A0:9A:8E:0D:58:86",
    "btName" : "Mac",
    "otherDeviceAudioCategory" : 200,
}
default	10:08:44.633919-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [1, 0]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:input"
)}
default	10:08:44.633930-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	10:08:44.635318-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	10:08:44.634804-0500	audiomxd	UpdateAudioState CID 0xBDB10001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	10:08:44.642462-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.22956984.22956990(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	10:08:44.643116-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	10:08:44.643162-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	10:08:44.643201-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	10:08:44.643212-0500	gamepolicyd	Received state update for 66242 (app<application.com.nexy.assistant.22956984.22956990(501)>, running-active-NotVisible
default	10:08:44.643584-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	10:08:44.643593-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	10:08:44.643604-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	10:08:44.643623-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	10:08:44.643640-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	10:08:44.643647-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	10:08:44.643676-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	10:08:44.643697-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	10:08:44.643724-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	10:08:44.643738-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	10:08:44.643747-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	10:08:44.643759-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	10:08:44.643965-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	10:08:44.644098-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	10:08:44.644107-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	10:08:44.644128-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	10:08:44.644134-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	10:08:44.644141-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	10:08:44.644148-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	10:08:44.644226-0500	ControlCenter	Navigating to new application [com.nexy.assistant]
default	10:08:46.108529-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.nexy.assistant, Score 200, Remote 100 NumofApp 1
default	10:08:47.520848-0500	audioaccessoryd	MetricLog 'com.apple.bluetooth.SmartRouting.RouteCheck' : { "OnDemandCategory" : "NA", "WxBuildVersion" : "8B21", "WxStreamState" : "SCO", "OtherTipiAudioCategory" : 100, "ProactiveRoutingWxRSSI" : -46, "BannerAction" : "NA", "WxProductID" : 8219, "LocalAudioCategory" : 200, "Trigger" : "NA", "Type" : "Hijack", "OtherTipiDeviceIdleTime" : 0, "HijackScore" : 200, "BluetoothState" : "PoweredOn", "IsPlaying" : true, "Reason" : "NA", "Route" : "Bluetooth", "HijackAnswer" : "Accepted", "OtherTipiDevicePlayingApp" : "Unknown", "IsConnected" : true, "OtherTipiDevice" : "iPhone", "ActivePlayingApp" : "com.nexy.assistant", "InEar" : "YES", "HijackVersion" : "V2", "ProactiveRoutingTrigger" : "", }
default	10:08:47.730146-0500	Nexy	NotifyToken::RegisterDispatch(user.uid.501.com.apple.LaunchServices.database) fired for session key <private>
default	10:08:48.804896-0500	Nexy	LSExceptions shared instance invalidated for timeout.
default	10:08:49.105051-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.nexy.assistant, Score 200, Remote 100 NumofApp 1
default	10:08:52.107798-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.nexy.assistant, Score 200, Remote 100 NumofApp 1
default	10:08:53.608954-0500	coreaudiod	IssueReporting.cpp:492   RTAID [ use_case=Generic report_type=RMS Generic Chain clientID=ADM node=ADM::com.nexy.assistant_2350.2224.0_airpods noise suppression studio::in-0 issue_detected_sample_time=0.000000 ] -- [ rms:[-33.748047], peaks:[-14.499560] ]
default	10:08:53.611407-0500	coreaudiod	IssueReporting.cpp:492   RTAID [ use_case=Generic report_type=RMS Generic Chain clientID=ADM node=ADM::com.nexy.assistant_2350.2224.0_airpods noise suppression studio::out-0 issue_detected_sample_time=240000.000000 ] -- [ rms:[-33.808762], peaks:[-12.758301] ]
default	10:08:55.106190-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.nexy.assistant, Score 200, Remote 100 NumofApp 1
default	10:08:57.654172-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xb}
default	10:08:57.654676-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x280021","name":"Nexy(66242)"}, "details":{"deviceUIDs":[],"implicit_category":"","input_running":false,"output_running":false} }
default	10:08:57.654884-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 34, PID = 66242, Name = sid:0x280021, Nexy(66242), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	10:08:57.654978-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 34, PID = 66242, Name = sid:0x280021, Nexy(66242), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	10:08:57.655042-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x280021, Nexy(66242), 'prim'', displayID:'com.nexy.assistant'}
default	10:08:57.655154-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	10:08:57.655203-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x280021, Nexy(66242), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 34 stopping recording
default	10:08:57.655272-0500	audiomxd	-MXCoreSession- -[MXCoreSession endInterruption:]: Session <ID: 34, PID = 66242, Name = sid:0x280021, Nexy(66242), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> is going inactive
default	10:08:57.655356-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 34, PID = 66242, Name = sid:0x280021, Nexy(66242), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	10:08:57.655431-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 34, PID = 66242, Name = sid:0x280021, Nexy(66242), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	10:08:57.655700-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 200 flag 0x1 < Hijack > app com.nexy.assistant CID 0xBDB10001 category Not set
default	10:08:57.655673-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 0]. BT device UIDS: {(
)}
default	10:08:57.655695-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	10:08:57.656389-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	10:08:57.656455-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	10:08:57.656198-0500	audiomxd	UpdateAudioState CID 0xBDB10001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	10:08:57.656477-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	10:08:57.656290-0500	audiomxd	UpdateAudioState CID 0xBDB10001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	10:08:57.656502-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	10:08:57.656591-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	10:08:57.656610-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	10:08:57.656625-0500	audioaccessoryd	AudioStateChanged: Removed audio session app com.nexy.assistant 201 count 0
default	10:08:57.659488-0500	runningboardd	Invalidating assertion 585-520-276764 (target:[app<application.com.nexy.assistant.22956984.22956990(501)>:66242]) from originator [osservice<com.apple.powerd>:520]
default	10:08:57.661303-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	10:08:57.662764-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	10:08:57.662781-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	10:08:57.662796-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	10:08:57.662805-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	10:08:57.662813-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	10:08:57.662822-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	10:08:57.662966-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	10:08:57.756419-0500	Nexy	                AUHAL.cpp:473   ~AUHAL: (0x899114040) Selecting device 0 from destructor
default	10:08:57.756449-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0x899114040)
default	10:08:57.756464-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0x899114040) not already running
default	10:08:57.756475-0500	Nexy	                AUHAL.cpp:687   SelectDevice: (0x899114040) disconnecting device 89
default	10:08:57.756489-0500	Nexy	                AUHAL.cpp:751   SelectDevice: (0x899114040) destroying ioproc 0xb for device 89
default	10:08:57.756541-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xb}
default	10:08:57.756608-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	10:08:57.756900-0500	Nexy	                AUHAL.cpp:853   SelectDevice: (0x899114040) nothing to setup
default	10:08:57.756930-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x899114040) adding 0 device listeners to device 0
default	10:08:57.756944-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x899114040) adding 0 device delegate listeners to device 0
default	10:08:57.756963-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x899114040) removing 7 device listeners from device 89
default	10:08:57.757477-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x899114040) removing 0 device delegate listeners from device 89
default	10:08:57.757513-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0x899114040)
default	10:08:57.762154-0500	runningboardd	[app<application.com.nexy.assistant.22956984.22956990(501)>:66242] Ignoring jetsam update because this process is not memory-managed
default	10:08:57.762166-0500	runningboardd	[app<application.com.nexy.assistant.22956984.22956990(501)>:66242] Ignoring suspend because this process is not lifecycle managed
default	10:08:57.762178-0500	runningboardd	[app<application.com.nexy.assistant.22956984.22956990(501)>:66242] Ignoring GPU update because this process is not GPU managed
default	10:08:57.762233-0500	runningboardd	[app<application.com.nexy.assistant.22956984.22956990(501)>:66242] Ignoring memory limit update because this process is not memory-managed
default	10:08:57.767461-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.22956984.22956990(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	10:08:57.768229-0500	gamepolicyd	Received state update for 66242 (app<application.com.nexy.assistant.22956984.22956990(501)>, running-active-NotVisible
default	10:08:57.773222-0500	Nexy	[0x89a6c9540] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	10:08:57.774425-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=66242.4, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=66242, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	10:08:57.775979-0500	tccd	AUTHREQ_SUBJECT: msgID=66242.4, subject=com.nexy.assistant,
default	10:08:57.777095-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc90d7d500 at /Applications/Nexy.app
default	10:08:57.796591-0500	tccd	Notifying for access  kTCCServiceListenEvent for target PID[66242], responsiblePID[66242], responsiblePath: /Applications/Nexy.app to UID: 501
default	10:08:57.797014-0500	Nexy	[0x89a6c9540] invalidated after the last release of the connection object
default	10:08:57.889005-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc90d7e700 at /Applications/Nexy.app
default	10:08:57.908137-0500	nehelper	Received an apps uninstalled notification with bundle IDs (
    "com.nexy.assistant"
)
default	10:08:57.908196-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc90d7f300 at /Applications/Nexy.app
default	10:08:57.912647-0500	tccd	Publishing <TCCDEvent: type=Modify, service=kTCCServiceListenEvent, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 0 subscribers: {
}
default	10:08:58.505904-0500	nehelper	Removing UUIDs for (
    "com.nexy.assistant"
)
default	10:08:58.508526-0500	nehelper	Handling an apps uninstalled notification with bundle IDs (
    "com.nexy.assistant"
)
default	10:08:58.523099-0500	nehelper	com.apple.preferences.networkprivacy-F67B3EA9-90A6-470B-B321-9BBD719C692B: Populating the cache with 1 UUID(s) for com.nexy.assistant
error	10:09:01.363749-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CAIIugCI3D6x0jkL7BXjcYRl0vPhkk-L5K9mxvc/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:194 loadAuthorizationStates(for:) new entry: kTCCServiceAppleEvents com.nexy.assistant full
error	10:09:01.364754-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CAIIugCI3D6x0jkL7BXjcYRl0vPhkk-L5K9mxvc/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:194 loadAuthorizationStates(for:) new entry: kTCCServiceMicrophone com.nexy.assistant full
default	10:09:01.953623-0500	nehelper	Removing UUIDs for (
    "com.nexy.assistant"
)
default	10:09:03.065161-0500	nehelper	Handling an apps uninstalled notification with bundle IDs (
    "com.nexy.assistant"
)
default	10:09:03.092856-0500	nehelper	com.apple.preferences.networkprivacy-F67B3EA9-90A6-470B-B321-9BBD719C692B: Populating the cache with 1 UUID(s) for com.nexy.assistant
default	10:09:04.632703-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc90d7d800 at /Applications/Nexy.app
default	10:09:04.651640-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc90d7fc00 at /Applications/Nexy.app
default	10:09:04.661425-0500	tccd	Publishing <TCCDEvent: type=Modify, service=kTCCServiceListenEvent, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 0 subscribers: {
}
error	10:09:04.791265-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CAIIugCI3D6x0jkL7BXjcYRl0vPhkk-L5K9mxvc/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:194 loadAuthorizationStates(for:) new entry: kTCCServiceListenEvent com.nexy.assistant full
error	10:09:04.793037-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CAIIugCI3D6x0jkL7BXjcYRl0vPhkk-L5K9mxvc/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:194 loadAuthorizationStates(for:) new entry: kTCCServiceListenEvent com.nexy.assistant full
error	10:09:04.806358-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CAIIugCI3D6x0jkL7BXjcYRl0vPhkk-L5K9mxvc/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:194 loadAuthorizationStates(for:) new entry: kTCCServiceAppleEvents com.nexy.assistant full
error	10:09:04.806920-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CAIIugCI3D6x0jkL7BXjcYRl0vPhkk-L5K9mxvc/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:194 loadAuthorizationStates(for:) new entry: kTCCServiceAppleEvents com.nexy.assistant full
error	10:09:04.806976-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CAIIugCI3D6x0jkL7BXjcYRl0vPhkk-L5K9mxvc/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:194 loadAuthorizationStates(for:) new entry: kTCCServiceMicrophone com.nexy.assistant full
error	10:09:04.807423-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CAIIugCI3D6x0jkL7BXjcYRl0vPhkk-L5K9mxvc/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:194 loadAuthorizationStates(for:) new entry: kTCCServiceMicrophone com.nexy.assistant full
default	10:09:10.803530-0500	Nexy	[0x89a6c9400] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	10:09:10.805233-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=66242.5, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=66242, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	10:09:10.808973-0500	tccd	AUTHREQ_SUBJECT: msgID=66242.5, subject=com.nexy.assistant,
default	10:09:10.810205-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc90d7f600 at /Applications/Nexy.app
default	10:09:10.830516-0500	tccd	Notifying for access  kTCCServiceScreenCapture for target PID[66242], responsiblePID[66242], responsiblePath: /Applications/Nexy.app to UID: 501
default	10:09:10.830883-0500	Nexy	[0x89a6c9400] invalidated after the last release of the connection object
default	10:09:10.879204-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc90d7d800 at /Applications/Nexy.app
default	10:09:10.894824-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc90d7fc00 at /Applications/Nexy.app
default	10:09:10.898955-0500	tccd	Publishing <TCCDEvent: type=Modify, service=kTCCServiceScreenCapture, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 0 subscribers: {
}
error	10:09:13.843508-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CAIIugCI3D6x0jkL7BXjcYRl0vPhkk-L5K9mxvc/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:194 loadAuthorizationStates(for:) new entry: kTCCServiceAppleEvents com.nexy.assistant full
error	10:09:13.843893-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CAIIugCI3D6x0jkL7BXjcYRl0vPhkk-L5K9mxvc/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:194 loadAuthorizationStates(for:) new entry: kTCCServiceAppleEvents com.nexy.assistant full
error	10:09:13.845047-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CAIIugCI3D6x0jkL7BXjcYRl0vPhkk-L5K9mxvc/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:194 loadAuthorizationStates(for:) new entry: kTCCServiceMicrophone com.nexy.assistant full
error	10:09:13.845247-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CAIIugCI3D6x0jkL7BXjcYRl0vPhkk-L5K9mxvc/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:194 loadAuthorizationStates(for:) new entry: kTCCServiceMicrophone com.nexy.assistant full
default	10:09:16.919045-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc90d7cc00 at /Applications/Nexy.app
default	10:09:16.933965-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc90d7c600 at /Applications/Nexy.app
default	10:09:16.944103-0500	tccd	Publishing <TCCDEvent: type=Modify, service=kTCCServiceScreenCapture, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 0 subscribers: {
}
error	10:09:17.074449-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CAIIugCI3D6x0jkL7BXjcYRl0vPhkk-L5K9mxvc/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:194 loadAuthorizationStates(for:) new entry: kTCCServiceScreenCapture com.nexy.assistant full
error	10:09:17.074577-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CAIIugCI3D6x0jkL7BXjcYRl0vPhkk-L5K9mxvc/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:194 loadAuthorizationStates(for:) new entry: kTCCServiceListenEvent com.nexy.assistant full
error	10:09:17.076181-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CAIIugCI3D6x0jkL7BXjcYRl0vPhkk-L5K9mxvc/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:194 loadAuthorizationStates(for:) new entry: kTCCServiceListenEvent com.nexy.assistant full
error	10:09:17.076476-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CAIIugCI3D6x0jkL7BXjcYRl0vPhkk-L5K9mxvc/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:194 loadAuthorizationStates(for:) new entry: kTCCServiceScreenCapture com.nexy.assistant full
error	10:09:17.089754-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CAIIugCI3D6x0jkL7BXjcYRl0vPhkk-L5K9mxvc/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:194 loadAuthorizationStates(for:) new entry: kTCCServiceAppleEvents com.nexy.assistant full
error	10:09:17.090286-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CAIIugCI3D6x0jkL7BXjcYRl0vPhkk-L5K9mxvc/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:194 loadAuthorizationStates(for:) new entry: kTCCServiceMicrophone com.nexy.assistant full
error	10:09:17.090409-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CAIIugCI3D6x0jkL7BXjcYRl0vPhkk-L5K9mxvc/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:194 loadAuthorizationStates(for:) new entry: kTCCServiceAppleEvents com.nexy.assistant full
error	10:09:17.090840-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CAIIugCI3D6x0jkL7BXjcYRl0vPhkk-L5K9mxvc/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:194 loadAuthorizationStates(for:) new entry: kTCCServiceMicrophone com.nexy.assistant full
default	10:09:25.385255-0500	WindowServer	0[outside of RPC]: Process death: 0x0-0x170170 (Nexy) connectionID: C08F3 pid: 66242 in session 0x101
default	10:09:25.385320-0500	WindowServer	<BSCompoundAssertion:0xc51015580> ([FocusManager:257]-deferringPolicyEvaluationSuppression) acquire for reason:process death - 0x0-0x170170 (Nexy) acq:0xc529caaa0 count:1
default	10:09:25.386298-0500	audiomxd	  ServerSessionManager.mm:478   { "action":"destroy_session", "session":{"ID":"0x280021","name":"Nexy(66242)"}, "details":null }
default	10:09:25.387068-0500	audiomxd	AudioApplicationInfoImpl.mm:690   Successfully removed session 0x280021 from AudioApp, recording state unchanged (app: {"name":"[implicit] Nexy","pid":66242})
default	10:09:25.387104-0500	audiomxd	  ServerSessionManager.mm:1086  destroy audio app instance since was created implicitly by session creation and all sessions now gone (audio app: {"name":"[implicit] Nexy","pid":66242})
default	10:09:25.387831-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 34, PID = 66242, Name = sid:0x280021, Nexy(66242), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	10:09:25.388365-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 34, PID = 66242, Name = sid:0x280021, Nexy(66242), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	10:09:25.388652-0500	audiomxd	UpdateAudioState CID 0xBDB10001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	10:09:25.388906-0500	audiomxd	UpdateAudioState CID 0xBDB10001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	10:09:25.389028-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	10:09:25.389110-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	10:09:25.389153-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	10:09:25.389933-0500	WindowServer	0[outside of RPC]: [FocusManager:257] update to deferring policy requested for reason: permitted list updated - 0x0-0x170170 removed - but we are suppressing evaluation for reasons: {(
    "process death - 0x0-0x170170 (Nexy)"
)}
default	10:09:25.391212-0500	WindowServer	0[outside of RPC]: [FocusManager:257] update to deferring policy requested for reason: permitted list updated - 0x1-0x102c2 removed - but we are suppressing evaluation for reasons: {(
    "process death - 0x0-0x170170 (Nexy)"
)}
default	10:09:25.400718-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	10:09:25.400631-0500	runningboardd	XPC connection invalidated: [app<application.com.nexy.assistant.22956984.22956990(501)>:66242]
default	10:09:25.401734-0500	coreaudiod	>>> NEGOTIATE [com.nexy.assistant]
default	10:09:25.401947-0500	coreaudiod	<<< NEGOTIATE [com.nexy.assistant]
default	10:09:25.405476-0500	coreaudiod	IssueReporting.cpp:492   RTAID [ use_case=Generic report_type=RMS Generic Chain clientID=ADM node=ADM::com.nexy.assistant_2350.2224.0_airpods noise suppression studio::out-0 issue_detected_sample_time=336960.000000 ] -- [ rms:[-36.304512], peaks:[-20.756762] ]
default	10:09:25.405514-0500	coreaudiod	IssueReporting.cpp:492   RTAID [ use_case=Generic report_type=RMS Generic Chain clientID=ADM node=ADM::com.nexy.assistant_2350.2224.0_airpods noise suppression studio::in-0 issue_detected_sample_time=0.000000 ] -- [ rms:[-35.544044], peaks:[-20.533966] ]
default	10:09:25.411581-0500	runningboardd	[app<application.com.nexy.assistant.22956984.22956990(501)>:66242] termination reported by launchd (0, 0, 0)
default	10:09:25.411634-0500	runningboardd	Removing process: [app<application.com.nexy.assistant.22956984.22956990(501)>:66242]
default	10:09:25.411931-0500	runningboardd	Removing launch job for: [app<application.com.nexy.assistant.22956984.22956990(501)>:66242]
default	10:09:25.412166-0500	runningboardd	Removed job for [app<application.com.nexy.assistant.22956984.22956990(501)>:66242]
default	10:09:25.412210-0500	runningboardd	Removing assertions for terminated process: [app<application.com.nexy.assistant.22956984.22956990(501)>:66242]
default	10:09:25.420011-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.22956984.22956990(501)>: none (role: None) (endowments: (null))
default	10:09:25.420541-0500	audiomxd	  ServerSessionManager.mm:1327  Monitored process died, pid = 66242, name = Nexy
default	10:09:25.420804-0500	gamepolicyd	Received state update for 66242 (app<application.com.nexy.assistant.22956984.22956990(501)>, none-NotVisible
default	10:09:25.420851-0500	launchservicesd	Hit the server for a process handle 5404e5e000102c2 that resolved to: [app<application.com.nexy.assistant.22956984.22956990(501)>:66242]
default	10:09:25.421040-0500	gamepolicyd	Received state update for 66242 (app<application.com.nexy.assistant.22956984.22956990(501)>, none-NotVisible
default	10:09:28.475047-0500	logger	launching: /usr/bin/open -n -a /Applications/Nexy.app
default	10:09:28.541702-0500	lsd	com.nexy.assistant/Unknown Persona:5:5:1:1:Building bundle record for app
default	10:09:28.541887-0500	lsd	com.nexy.assistant/Unknown Persona:5:5:2:1:Built bundle record for app
default	10:09:28.543517-0500	lsd	com.nexy.assistant/Unknown Persona:5:4:2:1:_LSServerRegisterItemInfo result = 0
default	10:09:28.547707-0500	runningboardd	Launch request for app<application.com.nexy.assistant.22956984.22956990.7DD7DE9D-9598-4018-AD9F-B1931560DBFC(501)>[0] is using uid 501 (divined from auid 501 euid 501)
default	10:09:28.547774-0500	runningboardd	Acquiring assertion targeting app<application.com.nexy.assistant.22956984.22956990.7DD7DE9D-9598-4018-AD9F-B1931560DBFC(501)> from originator [osservice<com.apple.coreservices.uiagent(501)>:941] with description <RBSAssertionDescriptor| "LS launch com.nexy.assistant" ID:585-941-277079 target:app<application.com.nexy.assistant.22956984.22956990.7DD7DE9D-9598-4018-AD9F-B1931560DBFC(501)> attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"LaunchRoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	10:09:28.547842-0500	runningboardd	Assertion 585-941-277079 (target:app<application.com.nexy.assistant.22956984.22956990.7DD7DE9D-9598-4018-AD9F-B1931560DBFC(501)>) will be created as active
default	10:09:28.552347-0500	runningboardd	Checking PreventLaunch: global:0 exPath:/Applications/Nexy.app/Contents/MacOS/Nexy predicates:(null) allow:(null)
default	10:09:28.552373-0500	runningboardd	Creating and launching job for: app<application.com.nexy.assistant.22956984.22956990.7DD7DE9D-9598-4018-AD9F-B1931560DBFC(501)>
default	10:09:28.552386-0500	runningboardd	_mutateContextIfNeeded called for com.nexy.assistant
default	10:09:28.552450-0500	runningboardd	app<application.com.nexy.assistant.22956984.22956990.7DD7DE9D-9598-4018-AD9F-B1931560DBFC(501)>: -[RBPersonaManager personaForIdentity:context:personaUID:personaUniqueString:] required 0.000000 ms (wallclock); resolved to {4294967295, (null)}
default	10:09:28.556528-0500	dmd	Received xpc stream event (distributed notification matching) with name: com.apple.LaunchServices.applicationRegistered user info: {
    CFBundleDisplayName = Nexy;
    bundleIDs =     (
        "com.nexy.assistant"
    );
    isPlaceholder = 0;
}
default	10:09:28.560616-0500	runningboardd	[app<application.com.nexy.assistant.22956984.22956990.7DD7DE9D-9598-4018-AD9F-B1931560DBFC(501)>:66317] is not RunningBoard jetsam managed.
default	10:09:28.560631-0500	runningboardd	[app<application.com.nexy.assistant.22956984.22956990.7DD7DE9D-9598-4018-AD9F-B1931560DBFC(501)>:66317] This process will not be managed.
default	10:09:28.560641-0500	runningboardd	Now tracking process: [app<application.com.nexy.assistant.22956984.22956990.7DD7DE9D-9598-4018-AD9F-B1931560DBFC(501)>:66317]
default	10:09:28.560777-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.22956984.22956990.7DD7DE9D-9598-4018-AD9F-B1931560DBFC(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	10:09:28.561402-0500	gamepolicyd	Hit the server for a process handle 16b32e540001030d that resolved to: [app<application.com.nexy.assistant.22956984.22956990.7DD7DE9D-9598-4018-AD9F-B1931560DBFC(501)>:66317]
default	10:09:28.561434-0500	gamepolicyd	Received state update for 66317 (app<application.com.nexy.assistant.22956984.22956990.7DD7DE9D-9598-4018-AD9F-B1931560DBFC(501)>, running-active-NotVisible
default	10:09:28.565737-0500	runningboardd	Using default underlying assertion for app: [app<application.com.nexy.assistant.22956984.22956990.7DD7DE9D-9598-4018-AD9F-B1931560DBFC(501)>:66317]
default	10:09:28.565794-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.22956984.22956990.7DD7DE9D-9598-4018-AD9F-B1931560DBFC(501)>:66317] from originator [app<application.com.nexy.assistant.22956984.22956990.7DD7DE9D-9598-4018-AD9F-B1931560DBFC(501)>:66317] with description <RBSAssertionDescriptor| "RB Underlying Assertion" ID:585-585-277080 target:66317 attributes:[
	<RBSDomainAttribute| domain:"com.apple.underlying" name:"defaultUnderlyingAppAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	10:09:28.565908-0500	runningboardd	Assertion 585-585-277080 (target:[app<application.com.nexy.assistant.22956984.22956990.7DD7DE9D-9598-4018-AD9F-B1931560DBFC(501)>:66317]) will be created as active
default	10:09:28.566082-0500	runningboardd	[app<application.com.nexy.assistant.22956984.22956990.7DD7DE9D-9598-4018-AD9F-B1931560DBFC(501)>:66317] Ignoring jetsam update because this process is not memory-managed
default	10:09:28.566102-0500	runningboardd	[app<application.com.nexy.assistant.22956984.22956990.7DD7DE9D-9598-4018-AD9F-B1931560DBFC(501)>:66317] Ignoring suspend because this process is not lifecycle managed
default	10:09:28.566117-0500	runningboardd	[app<application.com.nexy.assistant.22956984.22956990.7DD7DE9D-9598-4018-AD9F-B1931560DBFC(501)>:66317] Set darwin role to: UserInteractive
default	10:09:28.566127-0500	runningboardd	[app<application.com.nexy.assistant.22956984.22956990.7DD7DE9D-9598-4018-AD9F-B1931560DBFC(501)>:66317] Ignoring GPU update because this process is not GPU managed
default	10:09:28.566144-0500	runningboardd	[app<application.com.nexy.assistant.22956984.22956990.7DD7DE9D-9598-4018-AD9F-B1931560DBFC(501)>:66317] Ignoring memory limit update because this process is not memory-managed
default	10:09:28.566184-0500	runningboardd	[app<application.com.nexy.assistant.22956984.22956990.7DD7DE9D-9598-4018-AD9F-B1931560DBFC(501)>:66317] reported to RB as running
default	10:09:28.567500-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.22956984.22956990.7DD7DE9D-9598-4018-AD9F-B1931560DBFC(501)>:66317] from originator [osservice<com.apple.coreservices.launchservicesd>:549] with description <RBSAssertionDescriptor| "uielement:66317" ID:585-549-277081 target:66317 attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"RoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	10:09:28.567604-0500	runningboardd	Assertion 585-549-277081 (target:[app<application.com.nexy.assistant.22956984.22956990.7DD7DE9D-9598-4018-AD9F-B1931560DBFC(501)>:66317]) will be created as active
default	10:09:28.567689-0500	CoreServicesUIAgent	LAUNCH: 0x0-0x186186 com.nexy.assistant starting stopped process.
default	10:09:28.568471-0500	loginwindow	-[Application updateInformation] | Got App URL: file:///Applications/Nexy.app/
default	10:09:28.568605-0500	loginwindow	-[Application setState:] | enter: <Application: 0x8f500bde0: Nexy> state 2
default	10:09:28.568547-0500	runningboardd	[app<application.com.nexy.assistant.22956984.22956990.7DD7DE9D-9598-4018-AD9F-B1931560DBFC(501)>:66317] Ignoring jetsam update because this process is not memory-managed
default	10:09:28.568628-0500	loginwindow	-[ApplicationManager checkInAppContext:eventData:] | ApplicationManager: Checked in app : Nexy
default	10:09:28.568576-0500	runningboardd	[app<application.com.nexy.assistant.22956984.22956990.7DD7DE9D-9598-4018-AD9F-B1931560DBFC(501)>:66317] Ignoring suspend because this process is not lifecycle managed
default	10:09:28.568597-0500	runningboardd	[app<application.com.nexy.assistant.22956984.22956990.7DD7DE9D-9598-4018-AD9F-B1931560DBFC(501)>:66317] Ignoring GPU update because this process is not GPU managed
default	10:09:28.568655-0500	runningboardd	[app<application.com.nexy.assistant.22956984.22956990.7DD7DE9D-9598-4018-AD9F-B1931560DBFC(501)>:66317] Ignoring memory limit update because this process is not memory-managed
default	10:09:28.568770-0500	runningboardd	Successfully acquired underlying assertion for [app<application.com.nexy.assistant.22956984.22956990.7DD7DE9D-9598-4018-AD9F-B1931560DBFC(501)>:66317]
default	10:09:28.569468-0500	kernel	Nexy[66317] triggered unnest of range 0x1f6000000->0x1f8000000 of DYLD shared region in VM map 0x61aa6c9a01e654a3. While not abnormal for debuggers, this increases system memory footprint until the target exits.
default	10:09:28.569479-0500	kernel	Nexy[66317] triggered unnest of range 0x1f8000000->0x1fc000000 of DYLD shared region in VM map 0x61aa6c9a01e654a3. While not abnormal for debuggers, this increases system memory footprint until the target exits.
default	10:09:28.572247-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.22956984.22956990.7DD7DE9D-9598-4018-AD9F-B1931560DBFC(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	10:09:28.572485-0500	runningboardd	Invalidating assertion 585-941-277079 (target:app<application.com.nexy.assistant.22956984.22956990.7DD7DE9D-9598-4018-AD9F-B1931560DBFC(501)>) from originator [osservice<com.apple.coreservices.uiagent(501)>:941]
default	10:09:28.572515-0500	runningboardd	[app<application.com.nexy.assistant.22956984.22956990.7DD7DE9D-9598-4018-AD9F-B1931560DBFC(501)>:66317] Ignoring jetsam update because this process is not memory-managed
default	10:09:28.572529-0500	runningboardd	[app<application.com.nexy.assistant.22956984.22956990.7DD7DE9D-9598-4018-AD9F-B1931560DBFC(501)>:66317] Ignoring suspend because this process is not lifecycle managed
default	10:09:28.572566-0500	runningboardd	[app<application.com.nexy.assistant.22956984.22956990.7DD7DE9D-9598-4018-AD9F-B1931560DBFC(501)>:66317] Ignoring GPU update because this process is not GPU managed
default	10:09:28.572609-0500	gamepolicyd	Received state update for 66317 (app<application.com.nexy.assistant.22956984.22956990.7DD7DE9D-9598-4018-AD9F-B1931560DBFC(501)>, running-active-NotVisible
default	10:09:28.572624-0500	runningboardd	[app<application.com.nexy.assistant.22956984.22956990.7DD7DE9D-9598-4018-AD9F-B1931560DBFC(501)>:66317] Ignoring memory limit update because this process is not memory-managed
default	10:09:28.576793-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.22956984.22956990.7DD7DE9D-9598-4018-AD9F-B1931560DBFC(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	10:09:28.578752-0500	logger	verifying new process for /Applications/Nexy.app/Contents/MacOS/Nexy
default	10:09:28.625052-0500	logger	detected new pid 66317 for /Applications/Nexy.app/Contents/MacOS/Nexy
default	10:09:28.633176-0500	Nexy	[0x1019dd7b0] activating connection: mach=true listener=false peer=false name=com.apple.cfprefsd.daemon
default	10:09:28.633243-0500	Nexy	[0x1019ddcf0] activating connection: mach=true listener=false peer=false name=com.apple.cfprefsd.agent
default	10:09:28.675642-0500	runningboardd	[app<application.com.nexy.assistant.22956984.22956990.7DD7DE9D-9598-4018-AD9F-B1931560DBFC(501)>:66317] Ignoring jetsam update because this process is not memory-managed
default	10:09:28.675654-0500	runningboardd	[app<application.com.nexy.assistant.22956984.22956990.7DD7DE9D-9598-4018-AD9F-B1931560DBFC(501)>:66317] Ignoring suspend because this process is not lifecycle managed
default	10:09:28.675664-0500	runningboardd	[app<application.com.nexy.assistant.22956984.22956990.7DD7DE9D-9598-4018-AD9F-B1931560DBFC(501)>:66317] Ignoring GPU update because this process is not GPU managed
default	10:09:28.675771-0500	gamepolicyd	Received state update for 66317 (app<application.com.nexy.assistant.22956984.22956990.7DD7DE9D-9598-4018-AD9F-B1931560DBFC(501)>, running-active-NotVisible
default	10:09:28.675683-0500	runningboardd	[app<application.com.nexy.assistant.22956984.22956990.7DD7DE9D-9598-4018-AD9F-B1931560DBFC(501)>:66317] Ignoring memory limit update because this process is not memory-managed
default	10:09:28.679774-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.22956984.22956990.7DD7DE9D-9598-4018-AD9F-B1931560DBFC(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	10:09:28.680085-0500	gamepolicyd	Received state update for 66317 (app<application.com.nexy.assistant.22956984.22956990.7DD7DE9D-9598-4018-AD9F-B1931560DBFC(501)>, running-active-NotVisible
error	10:09:28.754806-0500	Nexy	dlsym cannot find symbol NSMakeRect in CFBundle 0x9c14d40e0 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	10:09:28.755028-0500	Nexy	dlsym cannot find symbol NSMakePoint in CFBundle 0x9c14d40e0 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	10:09:28.755228-0500	Nexy	dlsym cannot find symbol NSMakeSize in CFBundle 0x9c14d40e0 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	10:09:28.755426-0500	Nexy	dlsym cannot find symbol NSMakeRange in CFBundle 0x9c14d40e0 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
default	10:09:28.756424-0500	Nexy	[0x1019cc280] activating connection: mach=true listener=false peer=false name=com.apple.coreservices.launchservicesd
default	10:09:28.757062-0500	Nexy	[0x9c0608000] activating connection: mach=true listener=false peer=false name=com.apple.analyticsd
default	10:09:28.757411-0500	Nexy	[0x9c0608140] activating connection: mach=true listener=false peer=false name=com.apple.pasteboard.1
default	10:09:28.757792-0500	Nexy	[0x9c0608280] activating connection: mach=true listener=false peer=false name=com.apple.distributed_notifications@Uv3
default	10:09:28.758390-0500	Nexy	Received configuration update from daemon (initial)
default	10:09:28.759610-0500	Nexy	void _NSDisableAutomaticTerminationAndLog(NSString *) No windows open yet
default	10:09:28.759995-0500	Nexy	[0x9c06083c0] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	10:09:28.760557-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=66317.1, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=66317, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	10:09:28.761847-0500	tccd	AUTHREQ_SUBJECT: msgID=66317.1, subject=com.nexy.assistant,
default	10:09:28.762453-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc90d7ed00 at /Applications/Nexy.app
default	10:09:28.776081-0500	Nexy	[0x9c06083c0] invalidated after the last release of the connection object
default	10:09:28.777012-0500	Nexy	server port 0x00003413, session port 0x00003413
default	10:09:28.777918-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=582.1101, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=66317, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=582, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	10:09:28.777944-0500	tccd	requestor: TCCDProcess: identifier=com.apple.WindowServer, pid=582, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=66317, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	10:09:28.778742-0500	tccd	AUTHREQ_SUBJECT: msgID=582.1101, subject=com.nexy.assistant,
default	10:09:28.779372-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc90d7ed00 at /Applications/Nexy.app
default	10:09:28.795085-0500	Nexy	New connection 0x10043f main
default	10:09:28.797440-0500	Nexy	CHECKIN: pid=66317
default	10:09:28.804991-0500	Nexy	CHECKEDIN: pid=66317 asn=0x0-0x186186 foreground=0
default	10:09:28.804855-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.22956984.22956990.7DD7DE9D-9598-4018-AD9F-B1931560DBFC(501)>:66317] from originator [osservice<com.apple.coreservices.launchservicesd>:549] with description <RBSAssertionDescriptor| "uielement:66317" ID:585-549-277082 target:66317 attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"RoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	10:09:28.804969-0500	runningboardd	Assertion 585-549-277082 (target:[app<application.com.nexy.assistant.22956984.22956990.7DD7DE9D-9598-4018-AD9F-B1931560DBFC(501)>:66317]) will be created as active
default	10:09:28.804883-0500	launchservicesd	CHECKIN:0x0-0x186186 66317 com.nexy.assistant
default	10:09:28.805468-0500	runningboardd	Invalidating assertion 585-549-277081 (target:[app<application.com.nexy.assistant.22956984.22956990.7DD7DE9D-9598-4018-AD9F-B1931560DBFC(501)>:66317]) from originator [osservice<com.apple.coreservices.launchservicesd>:549]
default	10:09:28.805298-0500	Nexy	[0x9c06083c0] activating connection: mach=false listener=true peer=false name=(anonymous)
default	10:09:28.805339-0500	Nexy	[0x9c06083c0] Connection returned listener port: 0x5003
default	10:09:28.805691-0500	Nexy	[0x9c15fc300] activating connection: mach=false listener=false peer=true name=com.apple.xpc.anonymous.0x9c06083c0.peer[549].0x9c15fc300
default	10:09:28.806337-0500	loginwindow	-[Application updateInformation] | Got App URL: file:///Applications/Nexy.app/
default	10:09:28.806464-0500	loginwindow	-[ApplicationManager checkInAppContext:eventData:] | ApplicationManager: Checked in app : Nexy
default	10:09:28.807529-0500	Nexy	FRONTLOGGING: version 1
default	10:09:28.807538-0500	Nexy	Registered, pid=66317 ASN=0x0,0x186186
default	10:09:28.807785-0500	WindowServer	10043f[CreateApplication]: Process creation: 0x0-0x186186 (Nexy) connectionID: 10043F pid: 66317 in session 0x101
default	10:09:28.808034-0500	Nexy	[0x9c0608500] activating connection: mach=true listener=false peer=false name=com.apple.lsd.mapdb
default	10:09:28.809812-0500	Nexy	[0x9c06083c0] Connection returned listener port: 0x5003
default	10:09:28.811285-0500	Nexy	BringForward: pid=66317 asn=0x0-0x186186 bringForward=0 foreground=0 uiElement=1 launchedByLS=1 modifiersCount=1 allDisabled=0
default	10:09:28.811556-0500	Nexy	BringFrontModifier: pid=66317 asn=0x0-0x186186 Modifier 0 hideAfter=0 hideOthers=0 dontMakeFrontmost=0 mouseDown=0/0 seed=0/0
default	10:09:28.812267-0500	Nexy	Current system appearance, (HLTB: 1), (SLS: 0)
default	10:09:28.814369-0500	Nexy	No persisted cache on this platform.
default	10:09:28.816304-0500	Nexy	Current system appearance, (HLTB: 1), (SLS: 0)
default	10:09:28.817250-0500	Nexy	Post-registration system appearance: (HLTB: 1)
default	10:09:28.820611-0500	Nexy	FBSWorkspace: endpoint monitoring is disabled.
default	10:09:28.820624-0500	Nexy	FBSWorkspace: default shell endpoint is disabled.
default	10:09:28.820678-0500	Nexy	Initializing connection
default	10:09:28.820718-0500	Nexy	Removing all cached process handles
default	10:09:28.820734-0500	Nexy	Sending handshake request attempt #1 to server
default	10:09:28.820743-0500	Nexy	Creating connection to com.apple.runningboard
default	10:09:28.820753-0500	Nexy	[0x9c0608780] activating connection: mach=true listener=false peer=false name=com.apple.runningboard
default	10:09:28.821333-0500	runningboardd	Setting client for [app<application.com.nexy.assistant.22956984.22956990.7DD7DE9D-9598-4018-AD9F-B1931560DBFC(501)>:66317] as ready
default	10:09:28.821974-0500	Nexy	Handshake succeeded
default	10:09:28.821988-0500	Nexy	Identity resolved as app<application.com.nexy.assistant.22956984.22956990.7DD7DE9D-9598-4018-AD9F-B1931560DBFC(501)>
default	10:09:28.822494-0500	Nexy	[0x9c06083c0] Connection returned listener port: 0x5003
default	10:09:28.823599-0500	distnoted	register name: com.apple.xctest.FakeForceTouchDevice object: com.nexy.assistant token: 1e0000001d pid: 66317
default	10:09:28.826375-0500	Nexy	[0x9c06083c0] Connection returned listener port: 0x5003
default	10:09:28.831312-0500	Nexy	Created a new Process Instance Registry XPC connection (inactive)
default	10:09:28.831338-0500	Nexy	[0x9c0608640] activating connection: mach=true listener=false peer=false name=com.apple.linkd.autoShortcut
default	10:09:28.831417-0500	Nexy	Activated connection to com.apple.linkd.autoShortcut (ApplicationService)
default	10:09:28.831465-0500	Nexy	[0x9c0608a00] activating connection: mach=false listener=true peer=false name=(anonymous)
default	10:09:28.835041-0500	Nexy	[0x9c0608a00] Connection returned listener port: 0x6d03
default	10:09:28.835911-0500	Nexy	Registered process with identifier 66317-142234
default	10:09:28.963202-0500	Nexy	Registered notify signal com.apple.caulk.alloc.rtdump (0)
default	10:09:28.965599-0500	Nexy	System_Input_Processing_Notification_Handler.mm:456   System_Input_Processing_Notification_Handler::is_vi_available(): Voice isolation DSP is available for client with bundle id com.nexy.assistant (AVFoundation is available, application is not in client deny list, application is not FaceTime variant)
default	10:09:28.966973-0500	Nexy	[0x9c0608b40] activating connection: mach=true listener=false peer=false name=com.apple.cmio.registerassistantservice.system-extensions
fault	10:09:28.968852-0500	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.22956984.22956990.7DD7DE9D-9598-4018-AD9F-B1931560DBFC AUID=501> and <type=Application identifier=application.com.nexy.assistant.22956984.22956990.7DD7DE9D-9598-4018-AD9F-B1931560DBFC>
default	10:09:28.972100-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOInitializeListenersForBundleID: for <private> -> <private>
default	10:09:28.973498-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> vpio_preferenceChangedListener: new value ((null)) for key AUVoiceIOClients/com-nexy-assistant/AUVoiceIOChatFlavor, translatedBundleID com.nexy.assistant, bundleIDs {(
    "com.nexy.assistant"
)}
default	10:09:28.973663-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> vpio_preferenceChangedListener: new value ((null)) for key AUVoiceIOClients/com-nexy-assistant/AUVoiceIOIsAutoChatFlavorEnabled, translatedBundleID com.nexy.assistant, bundleIDs {(
    "com.nexy.assistant"
)}
default	10:09:28.973783-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetSupportedChatFlavorsForBundleID: <private>-><private> get supported chat flavors: <private>
default	10:09:28.973790-0500	Nexy	            HALSystem.cpp:134    Enabling HAL Voice Isolation support
default	10:09:28.973818-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetHiddenChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	10:09:28.973918-0500	Nexy	[0x9c0608c80] activating connection: mach=true listener=false peer=false name=com.apple.tccd
default	10:09:28.974066-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOHiddenChatFlavors newValue: (
    1
)
default	10:09:28.974339-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=66317.2, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=66317, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	10:09:28.980072-0500	tccd	AUTHREQ_SUBJECT: msgID=66317.2, subject=com.nexy.assistant,
default	10:09:28.980652-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x79418c300 at /Applications/Nexy.app
default	10:09:28.992927-0500	Nexy	[0x9c0608c80] invalidated after the last release of the connection object
default	10:09:28.993057-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetPreferredChatFlavorForBundleID: <private>-><private> get value: 0
default	10:09:28.993097-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetSupportedChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	10:09:28.993313-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOSupportedChatFlavors newValue: (
    0,
    2
)
default	10:09:28.994407-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=590.571, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=66317, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=579, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	10:09:28.995155-0500	tccd	AUTHREQ_SUBJECT: msgID=590.571, subject=com.nexy.assistant,
default	10:09:28.995681-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x79418c300 at /Applications/Nexy.app
error	10:09:29.007945-0500	tccd	Request message contains a target_token to accessing_process (TCCDProcess: identifier=com.nexy.assistant, pid=66317, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy) but TCCDProcess: identifier=com.apple.audio.coreaudiod, pid=590, auid=202, euid=202, binary_path=/usr/sbin/coreaudiod is not a TCC manager for service: kTCCServiceScreenCapture.
default	10:09:29.008799-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=590.573, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=66317, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=579, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	10:09:29.009531-0500	tccd	AUTHREQ_SUBJECT: msgID=590.573, subject=com.nexy.assistant,
default	10:09:29.010044-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x79418c300 at /Applications/Nexy.app
default	10:09:29.023730-0500	Nexy	  HALPlugInManagement.cpp:440    HALPlugInManagement::RegisterPlugIns: skipping in-process plug-ins
error	10:09:29.023797-0500	Nexy	AddInstanceForFactory: No factory registered for id <CFUUID 0x9c16ecc20> F8BB1C28-BAE8-11D6-9C31-00039315CD46
error	10:09:29.036534-0500	Nexy	         HALC_ProxyObjectMap.cpp:174   HALC_ProxyObjectMap::_CopyObjectByObjectID: failed to create the local object
error	10:09:29.036542-0500	Nexy	            HALC_ShellDevice.cpp:2673  HALC_ShellDevice::RebuildControlList: couldn't find the control object
default	10:09:29.039010-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	10:09:29.039132-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	10:09:29.043960-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetPreferredChatFlavorForBundleID: <private>-><private> get value: 0
default	10:09:30.482012-0500	kernel	SK[6]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 3AFD9C9F-AF61-4445-B60B-D9328D9010C7 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.64361,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0xadbd3cfc tp_proto=0x06"
default	10:09:30.482095-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:64361<-><IPv4-redacted>:53] interface: utun6 (skipped: 2519)
so_gencnt: 496349 t_state: SYN_SENT process: Nexy:66317 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 1 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xade1b1f0
default	10:09:30.482685-0500	kernel	tcp connected: [<IPv4-redacted>:64361<-><IPv4-redacted>:53] interface: utun6 (skipped: 2519)
so_gencnt: 496349 t_state: ESTABLISHED process: Nexy:66317 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 1 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xade1b1f0
default	10:09:30.482942-0500	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:64361<-><IPv4-redacted>:53] interface: utun6 (skipped: 2519)
so_gencnt: 496349 t_state: FIN_WAIT_1 process: Nexy:66317 Duration: 0.001 sec Conn_Time: 0.001 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 1.000 ms rttvar: 0.500 ms base rtt: 1 ms so_error: 0 svc/tc: 0 flow: 0xade1b1f0
default	10:09:30.482949-0500	kernel	tcp_connection_summary [<IPv4-redacted>:64361<-><IPv4-redacted>:53] interface: utun6 (skipped: 2519)
so_gencnt: 496349 t_state: FIN_WAIT_1 process: Nexy:66317 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	10:09:30.499946-0500	Nexy	[0x9c0608c80] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioComponentRegistrar
default	10:09:30.509620-0500	Nexy	                AUHAL.cpp:420   AUHAL: (0x9c0730040) Selecting device 83 from constructor
default	10:09:30.509634-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0x9c0730040)
default	10:09:30.509640-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0x9c0730040) not already running
default	10:09:30.509644-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0x9c0730040) nothing to teardown
default	10:09:30.509648-0500	Nexy	                AUHAL.cpp:762   SelectDevice: (0x9c0730040) connecting device 83
default	10:09:30.509737-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0x9c0730040) Device ID: 83 (Input:No | Output:Yes): true
default	10:09:30.509840-0500	Nexy	                AUHAL.cpp:774   SelectDevice: (0x9c0730040) created ioproc 0xa for device 83
default	10:09:30.509936-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x9c0730040) adding 7 device listeners to device 83
default	10:09:30.510083-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x9c0730040) adding 0 device delegate listeners to device 83
default	10:09:30.510090-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x9c0730040)
default	10:09:30.510157-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x54]:  2 ch,  48000 Hz, Float32, interleaved
default	10:09:30.510165-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	10:09:30.510173-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	10:09:30.510179-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	10:09:30.510185-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	10:09:30.510262-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x9c0730040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	10:09:30.510272-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x9c0730040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	10:09:30.510278-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	10:09:30.510288-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x9c0730040) removing 0 device listeners from device 0
default	10:09:30.510296-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x9c0730040) removing 0 device delegate listeners from device 0
default	10:09:30.510301-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0x9c0730040)
default	10:09:30.510314-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is DISABLED
default	10:09:30.510392-0500	Nexy	                AUHAL.cpp:2303  SetProperty: (0x9c0730040) caller requesting device change from 83 to 89
default	10:09:30.510400-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0x9c0730040)
default	10:09:30.510404-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0x9c0730040) not already running
default	10:09:30.510407-0500	Nexy	                AUHAL.cpp:687   SelectDevice: (0x9c0730040) disconnecting device 83
default	10:09:30.510411-0500	Nexy	                AUHAL.cpp:751   SelectDevice: (0x9c0730040) destroying ioproc 0xa for device 83
default	10:09:30.510485-0500	Nexy	  AVAudioSession_MacOS.mm:1021  initForMacOS
default	10:09:30.510963-0500	Nexy	[0x9c0608f00] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioSession
default	10:09:30.511893-0500	audiomxd	  ServerSessionManager.mm:315   { "action":"create_session", "session":{"ID":"0x280022","name":"Nexy(66317)"}, "details":{"PID":66317,"session_type":"Primary"} }
default	10:09:30.511976-0500	audiomxd	AudioApplicationInfoImpl.mm:250   Setting initial isRecording state: 0 for newly-created AudioApp
	app: {"name":"[implicit] Nexy","pid":66317}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x280022, sessionType: 'prim', isRecording: false }, 
]
default	10:09:30.512648-0500	audiomxd	  ServerSessionManager.mm:1322  Start process monitoring, pid = 66317, name = Nexy
default	10:09:30.512881-0500	Nexy	    SessionCore_Create.mm:99    Created session 0x9c04d53a0 with ID: 0x280022
default	10:09:30.513526-0500	Nexy	[0x9c0609040] activating connection: mach=true listener=false peer=false name=com.apple.audioanalyticsd
error	10:09:30.513904-0500	Nexy	Reporter disconnected. { function=sendMessage, reporterID=284829346168833 }
default	10:09:30.513920-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped Unknown {1C-77-54-18-C8-A3:output, 0xa}
default	10:09:30.513972-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	10:09:30.514055-0500	Nexy	                AUHAL.cpp:762   SelectDevice: (0x9c0730040) connecting device 89
default	10:09:30.514127-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0x9c0730040) Device ID: 89 (Input:Yes | Output:No): true
default	10:09:30.515433-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=590.574, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=66317, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=579, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	10:09:30.516588-0500	tccd	AUTHREQ_SUBJECT: msgID=590.574, subject=com.nexy.assistant,
default	10:09:30.517220-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x79418c300 at /Applications/Nexy.app
default	10:09:30.530659-0500	Nexy	                AUHAL.cpp:774   SelectDevice: (0x9c0730040) created ioproc 0xa for device 89
default	10:09:30.530785-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x9c0730040) adding 7 device listeners to device 89
default	10:09:30.530939-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x9c0730040) adding 0 device delegate listeners to device 89
default	10:09:30.530947-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x9c0730040)
default	10:09:30.530955-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 output streams; not all mono
default	10:09:30.530965-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	10:09:30.531071-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  input stream 0 [0x5a]:  1 ch,  24000 Hz, Float32
default	10:09:30.531080-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 input streams; all mono
default	10:09:30.531085-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  1 ch,  24000 Hz, Float32
default	10:09:30.531162-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x9c0730040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	10:09:30.531172-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x9c0730040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	10:09:30.531177-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	10:09:30.531182-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x9c0730040) removing 7 device listeners from device 83
default	10:09:30.531327-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x9c0730040) removing 0 device delegate listeners from device 83
default	10:09:30.531335-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0x9c0730040)
default	10:09:30.531883-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	10:09:30.532778-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=590.575, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=66317, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=579, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	10:09:30.533519-0500	tccd	AUTHREQ_SUBJECT: msgID=590.575, subject=com.nexy.assistant,
default	10:09:30.534049-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x79418c300 at /Applications/Nexy.app
default	10:09:30.546451-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	10:09:30.547348-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=590.576, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=66317, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=579, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	10:09:30.548049-0500	tccd	AUTHREQ_SUBJECT: msgID=590.576, subject=com.nexy.assistant,
default	10:09:30.548568-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x79418c300 at /Applications/Nexy.app
default	10:09:30.561410-0500	Nexy	Registered notify signal com.apple.caulk.alloc.audiodump (0)
default	10:09:30.562942-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=590.577, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=66317, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=579, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	10:09:30.563781-0500	tccd	AUTHREQ_SUBJECT: msgID=590.577, subject=com.nexy.assistant,
default	10:09:30.564934-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x79418c300 at /Applications/Nexy.app
default	10:09:30.584629-0500	coreaudiod	>>> NEGOTIATE [com.nexy.assistant]
default	10:09:30.584752-0500	coreaudiod	<<< NEGOTIATE [com.nexy.assistant]
default	10:09:30.585638-0500	coreaudiod	>>> ADAPT [com.nexy.assistant]
default	10:09:30.585948-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xa40759e00] Created node ADM::com.nexy.assistant_2363.2224.0_airpods noise suppression studio::in-0 with nodeID 0 - reporting period = 10.000000, sample rate = 24000.000000
default	10:09:30.586013-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xa40759e00] Created node ADM::com.nexy.assistant_2363.2224.0_airpods noise suppression studio::out-0 with nodeID 1 - reporting period = 10.000000, sample rate = 24000.000000
default	10:09:30.649110-0500	coreaudiod	<<< ADAPT [com.nexy.assistant]
default	10:09:30.650353-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:2363 called from <private>
default	10:09:30.650386-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Input {1C-77-54-18-C8-A3:input, 0xa}
default	10:09:30.653513-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.22956984.22956990.7DD7DE9D-9598-4018-AD9F-B1931560DBFC(501)>:66317] from originator [osservice<com.apple.powerd>:520] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:585-520-277091 target:66317 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	10:09:30.653601-0500	runningboardd	Assertion 585-520-277091 (target:[app<application.com.nexy.assistant.22956984.22956990.7DD7DE9D-9598-4018-AD9F-B1931560DBFC(501)>:66317]) will be created as active
default	10:09:30.651091-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2363 called from <private>
default	10:09:30.651221-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2363)
default	10:09:30.651238-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2363 called from <private>
default	10:09:30.651247-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2363 called from <private>
fault	10:09:30.655199-0500	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.22956984.22956990.7DD7DE9D-9598-4018-AD9F-B1931560DBFC AUID=501> and <type=Application identifier=application.com.nexy.assistant.22956984.22956990.7DD7DE9D-9598-4018-AD9F-B1931560DBFC>
default	10:09:30.655838-0500	runningboardd	[app<application.com.nexy.assistant.22956984.22956990.7DD7DE9D-9598-4018-AD9F-B1931560DBFC(501)>:66317] Ignoring jetsam update because this process is not memory-managed
default	10:09:30.651325-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2362)
default	10:09:30.655888-0500	runningboardd	[app<application.com.nexy.assistant.22956984.22956990.7DD7DE9D-9598-4018-AD9F-B1931560DBFC(501)>:66317] Ignoring suspend because this process is not lifecycle managed
default	10:09:30.651525-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2362 called from <private>
default	10:09:30.651559-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2362 called from <private>
default	10:09:30.655955-0500	runningboardd	[app<application.com.nexy.assistant.22956984.22956990.7DD7DE9D-9598-4018-AD9F-B1931560DBFC(501)>:66317] Ignoring GPU update because this process is not GPU managed
default	10:09:30.656131-0500	runningboardd	[app<application.com.nexy.assistant.22956984.22956990.7DD7DE9D-9598-4018-AD9F-B1931560DBFC(501)>:66317] Ignoring memory limit update because this process is not memory-managed
default	10:09:30.658318-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	10:09:30.658951-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
fault	10:09:30.656781-0500	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.22956984.22956990.7DD7DE9D-9598-4018-AD9F-B1931560DBFC AUID=501> and <type=Application identifier=application.com.nexy.assistant.22956984.22956990.7DD7DE9D-9598-4018-AD9F-B1931560DBFC>
default	10:09:30.663892-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2362)
default	10:09:30.663918-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2363)
default	10:09:30.665692-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x280022","name":"Nexy(66317)"}, "details":{"deviceUIDs":["1C-77-54-18-C8-A3:input"],"implicit_category":"Record","input_running":true,"output_running":false} }
default	10:09:30.666136-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 35, PID = 66317, Name = sid:0x280022, Nexy(66317), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	10:09:30.666301-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 35, PID = 66317, Name = sid:0x280022, Nexy(66317), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	10:09:30.666817-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 35, PID = 66317, Name = sid:0x280022, Nexy(66317), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	10:09:30.667471-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 35, PID = 66317, Name = sid:0x280022, Nexy(66317), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	10:09:30.667702-0500	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 35, PID = 66317, Name = sid:0x280022, Nexy(66317), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> is going active
default	10:09:30.668206-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x280022, Nexy(66317), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 35 starting recording
default	10:09:30.668598-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 35, PID = 66317, Name = sid:0x280022, Nexy(66317), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	10:09:30.663929-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2363)
default	10:09:30.663949-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2363)
default	10:09:30.663959-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2363)
default	10:09:30.668781-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 35, PID = 66317, Name = sid:0x280022, Nexy(66317), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	10:09:30.668903-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x280022, Nexy(66317), 'prim'', displayID:'com.nexy.assistant'}
default	10:09:30.665174-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2363 called from <private>
default	10:09:30.666677-0500	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x280022, Nexy(66317), 'prim'', AudioCategory changed to 'Record_WithBluetooth'
default	10:09:30.665184-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2363 called from <private>
default	10:09:30.665196-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2363 called from <private>
default	10:09:30.665463-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2363)
default	10:09:30.669065-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [1, 0]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:input"
)}
default	10:09:30.669117-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	10:09:30.678834-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2362 called from <private>
default	10:09:30.667531-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=590.578, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=66317, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=579, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	10:09:30.678847-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2362 called from <private>
default	10:09:30.669280-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	10:09:30.679047-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2362)
default	10:09:30.683460-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2362)
default	10:09:30.683759-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2362 called from <private>
default	10:09:30.683768-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2362 called from <private>
default	10:09:30.684216-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2362 called from <private>
default	10:09:30.684226-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2362 called from <private>
default	10:09:30.684293-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2362 called from <private>
default	10:09:30.684314-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2362 called from <private>
default	10:09:30.684319-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2362)
default	10:09:30.684345-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2362 called from <private>
default	10:09:30.684477-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2362 called from <private>
default	10:09:30.684564-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2362 called from <private>
default	10:09:30.684633-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2362 called from <private>
default	10:09:30.684712-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2362 called from <private>
default	10:09:30.684768-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2362 called from <private>
default	10:09:30.689579-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2362)
default	10:09:30.689822-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2362 called from <private>
default	10:09:30.689831-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2362 called from <private>
default	10:09:30.689866-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2362 called from <private>
default	10:09:30.689913-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2362 called from <private>
default	10:09:30.690045-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2362 called from <private>
default	10:09:30.690097-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2362 called from <private>
default	10:09:30.690351-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2362)
default	10:09:30.690571-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2362 called from <private>
default	10:09:30.691154-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 200 flag 0x1 < Hijack > app com.nexy.assistant CID 0xBDB10001 category Not set
default	10:09:30.693072-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	10:09:30.693186-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	10:09:30.693296-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	10:09:30.694888-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	10:09:30.695374-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	10:09:30.695698-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	10:09:30.695857-0500	audioaccessoryd	AudioStateChanged: Added audio session app com.nexy.assistant NULL -> 200 count 1
default	10:09:30.695981-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	10:09:30.690665-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2362 called from <private>
error	10:09:30.696050-0500	audioaccessoryd	Updating local audio category 100 -> 200 app com.nexy.assistant
default	10:09:30.690882-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2362)
default	10:09:30.691004-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2362 called from <private>
error	10:09:30.696254-0500	audioaccessoryd	Relaying via 24B92680-715A-E821-B5AF-358E78C2DAF9 inWxAddress 1C:77:54:18:C8:A3 to 88:20:0D:45:06:51 with options {
    "playingApp" : "com.nexy.assistant",
    "hostStreamingState" : "NO",
    "btAddress" : "A0:9A:8E:0D:58:86",
    "btName" : "Mac",
    "otherDeviceAudioCategory" : 200,
}
default	10:09:30.691082-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2362 called from <private>
default	10:09:30.691174-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2362 called from <private>
default	10:09:30.692689-0500	audiomxd	UpdateAudioState CID 0xBDB10001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	10:09:30.691241-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2362 called from <private>
default	10:09:30.696469-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	10:09:30.692990-0500	audiomxd	UpdateAudioState CID 0xBDB10001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	10:09:30.693121-0500	audiomxd	UpdateAudioState CID 0xBDB10001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	10:09:30.702881-0500	gamepolicyd	Received state update for 66317 (app<application.com.nexy.assistant.22956984.22956990.7DD7DE9D-9598-4018-AD9F-B1931560DBFC(501)>, running-active-NotVisible
default	10:09:30.702611-0500	runningboardd	Invalidating assertion 585-520-277091 (target:[app<application.com.nexy.assistant.22956984.22956990.7DD7DE9D-9598-4018-AD9F-B1931560DBFC(501)>:66317]) from originator [osservice<com.apple.powerd>:520]
default	10:09:30.703977-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x79418c300 at /Applications/Nexy.app
default	10:09:30.710134-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	10:09:30.710144-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	10:09:30.710225-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	10:09:30.710688-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	10:09:30.715694-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	10:09:30.715708-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	10:09:30.715720-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	10:09:30.715727-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	10:09:30.715739-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	10:09:30.715744-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	10:09:30.715826-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	10:09:30.721185-0500	runningboardd	Assertion 585-520-277092 (target:[app<application.com.nexy.assistant.22956984.22956990.7DD7DE9D-9598-4018-AD9F-B1931560DBFC(501)>:66317]) will be created as active
default	10:09:30.723377-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:2363 called from <private>
default	10:09:30.723398-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:2363 called from <private>
default	10:09:30.723422-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 1 1, id:2363 called from <private>
default	10:09:30.723433-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 1 2 2, id:2363 called from <private>
default	10:09:30.723426-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	10:09:30.723525-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2363)
default	10:09:30.725395-0500	runningboardd	Invalidating assertion 585-520-277092 (target:[app<application.com.nexy.assistant.22956984.22956990.7DD7DE9D-9598-4018-AD9F-B1931560DBFC(501)>:66317]) from originator [osservice<com.apple.powerd>:520]
default	10:09:30.746273-0500	coreaudiod	>>> ADAPT [com.nexy.assistant]
default	10:09:30.748148-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xa40759e00] Created node ADM::com.nexy.assistant_2363.2224.0_airpods noise suppression studio::in-0 with nodeID 0 - reporting period = 10.000000, sample rate = 24000.000000
default	10:09:30.748217-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xa40759e00] Created node ADM::com.nexy.assistant_2363.2224.0_airpods noise suppression studio::out-0 with nodeID 1 - reporting period = 10.000000, sample rate = 24000.000000
default	10:09:30.787868-0500	coreaudiod	<<< ADAPT [com.nexy.assistant]
default	10:09:30.791145-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:2363 called from <private>
default	10:09:30.791172-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:2363 called from <private>
default	10:09:30.790364-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.22956984.22956990.7DD7DE9D-9598-4018-AD9F-B1931560DBFC(501)>:66317] from originator [osservice<com.apple.powerd>:520] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:585-520-277094 target:66317 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	10:09:30.791182-0500	runningboardd	Assertion 585-520-277094 (target:[app<application.com.nexy.assistant.22956984.22956990.7DD7DE9D-9598-4018-AD9F-B1931560DBFC(501)>:66317]) will be created as active
default	10:09:30.791193-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 1 1, id:2363 called from <private>
default	10:09:30.791199-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 1 2 2, id:2363 called from <private>
default	10:09:30.791316-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2363)
default	10:09:30.791415-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	10:09:30.792978-0500	runningboardd	Invalidating assertion 585-520-277094 (target:[app<application.com.nexy.assistant.22956984.22956990.7DD7DE9D-9598-4018-AD9F-B1931560DBFC(501)>:66317]) from originator [osservice<com.apple.powerd>:520]
default	10:09:30.793725-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	10:09:30.793868-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	10:09:30.794296-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2363)
default	10:09:30.794600-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2363 called from <private>
default	10:09:30.794612-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2363 called from <private>
default	10:09:30.794625-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2363 called from <private>
default	10:09:30.794636-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2363 called from <private>
default	10:09:30.796535-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=590.580, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=66317, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=579, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	10:09:30.797765-0500	tccd	AUTHREQ_SUBJECT: msgID=590.580, subject=com.nexy.assistant,
default	10:09:30.798441-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x79418c300 at /Applications/Nexy.app
default	10:09:30.801043-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	10:09:30.801126-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	10:09:30.801215-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	10:09:30.801358-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	10:09:30.802459-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	10:09:30.802470-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	10:09:30.802483-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	10:09:30.802489-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	10:09:30.802495-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	10:09:30.802501-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	10:09:30.802680-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	10:09:30.810246-0500	runningboardd	[app<application.com.nexy.assistant.22956984.22956990.7DD7DE9D-9598-4018-AD9F-B1931560DBFC(501)>:66317] Ignoring jetsam update because this process is not memory-managed
default	10:09:30.810265-0500	runningboardd	[app<application.com.nexy.assistant.22956984.22956990.7DD7DE9D-9598-4018-AD9F-B1931560DBFC(501)>:66317] Ignoring suspend because this process is not lifecycle managed
default	10:09:30.810281-0500	runningboardd	[app<application.com.nexy.assistant.22956984.22956990.7DD7DE9D-9598-4018-AD9F-B1931560DBFC(501)>:66317] Ignoring GPU update because this process is not GPU managed
default	10:09:30.810309-0500	runningboardd	[app<application.com.nexy.assistant.22956984.22956990.7DD7DE9D-9598-4018-AD9F-B1931560DBFC(501)>:66317] Ignoring memory limit update because this process is not memory-managed
default	10:09:30.844369-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.22956984.22956990.7DD7DE9D-9598-4018-AD9F-B1931560DBFC(501)>:66317] from originator [osservice<com.apple.powerd>:520] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:585-520-277096 target:66317 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	10:09:30.844690-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:2363 called from <private>
default	10:09:30.844718-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:2363 called from <private>
default	10:09:30.844760-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	10:09:30.844685-0500	runningboardd	Assertion 585-520-277096 (target:[app<application.com.nexy.assistant.22956984.22956990.7DD7DE9D-9598-4018-AD9F-B1931560DBFC(501)>:66317]) will be created as active
default	10:09:30.846453-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2363 called from <private>
default	10:09:30.846467-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2363 called from <private>
default	10:09:30.846548-0500	runningboardd	Invalidating assertion 585-520-277096 (target:[app<application.com.nexy.assistant.22956984.22956990.7DD7DE9D-9598-4018-AD9F-B1931560DBFC(501)>:66317]) from originator [osservice<com.apple.powerd>:520]
default	10:09:30.848361-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=590.582, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=66317, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=579, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	10:09:30.873207-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:2363 called from <private>
default	10:09:30.873847-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.22956984.22956990.7DD7DE9D-9598-4018-AD9F-B1931560DBFC(501)>:66317] from originator [osservice<com.apple.powerd>:520] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:585-520-277099 target:66317 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	10:09:30.873938-0500	runningboardd	Assertion 585-520-277099 (target:[app<application.com.nexy.assistant.22956984.22956990.7DD7DE9D-9598-4018-AD9F-B1931560DBFC(501)>:66317]) will be created as active
default	10:09:30.880547-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	10:09:30.880599-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	10:09:30.880645-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	10:09:30.881093-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	10:09:30.881104-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	10:09:30.881119-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	10:09:30.881140-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	10:09:30.881153-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	10:09:30.881222-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	10:09:30.881293-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	10:09:30.881372-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	10:09:30.881401-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	10:09:30.881442-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	10:09:30.881474-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	10:09:30.881520-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	10:09:30.881721-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	10:09:30.881786-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	10:09:30.881828-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	10:09:30.881855-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	10:09:30.881864-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	10:09:30.881871-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	10:09:30.881886-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	10:09:30.881933-0500	ControlCenter	Navigating to new application [com.nexy.assistant]
default	10:09:30.917706-0500	gamepolicyd	Received state update for 66317 (app<application.com.nexy.assistant.22956984.22956990.7DD7DE9D-9598-4018-AD9F-B1931560DBFC(501)>, running-active-NotVisible
default	10:09:31.100317-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.nexy.assistant, Score 200, Remote 100 NumofApp 1
default	10:09:31.902230-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xa}
default	10:09:31.902734-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x280022","name":"Nexy(66317)"}, "details":{"deviceUIDs":[],"implicit_category":"","input_running":false,"output_running":false} }
default	10:09:31.902942-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 35, PID = 66317, Name = sid:0x280022, Nexy(66317), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	10:09:31.903043-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 35, PID = 66317, Name = sid:0x280022, Nexy(66317), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	10:09:31.903098-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x280022, Nexy(66317), 'prim'', displayID:'com.nexy.assistant'}
default	10:09:31.903183-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	10:09:31.903184-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x280022, Nexy(66317), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 35 stopping recording
default	10:09:31.903234-0500	audiomxd	-MXCoreSession- -[MXCoreSession endInterruption:]: Session <ID: 35, PID = 66317, Name = sid:0x280022, Nexy(66317), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> is going inactive
default	10:09:31.903280-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 35, PID = 66317, Name = sid:0x280022, Nexy(66317), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	10:09:31.903332-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 35, PID = 66317, Name = sid:0x280022, Nexy(66317), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	10:09:31.903498-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 0]. BT device UIDS: {(
)}
default	10:09:31.903517-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	10:09:31.903598-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 200 flag 0x1 < Hijack > app com.nexy.assistant CID 0xBDB10001 category Not set
default	10:09:31.903971-0500	audiomxd	UpdateAudioState CID 0xBDB10001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	10:09:31.904114-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	10:09:31.904042-0500	audiomxd	UpdateAudioState CID 0xBDB10001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	10:09:31.904169-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	10:09:31.904195-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	10:09:31.904226-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	10:09:31.904330-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	10:09:31.904357-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	10:09:31.904376-0500	audioaccessoryd	AudioStateChanged: Removed audio session app com.nexy.assistant 201 count 0
default	10:09:31.907022-0500	runningboardd	Invalidating assertion 585-520-277099 (target:[app<application.com.nexy.assistant.22956984.22956990.7DD7DE9D-9598-4018-AD9F-B1931560DBFC(501)>:66317]) from originator [osservice<com.apple.powerd>:520]
default	10:09:31.909816-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	10:09:31.913481-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	10:09:31.913491-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	10:09:31.913506-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	10:09:31.913512-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	10:09:31.913544-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	10:09:31.913579-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	10:09:31.913785-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	10:09:31.958770-0500	runningboardd	[app<application.com.nexy.assistant.22956984.22956990.7DD7DE9D-9598-4018-AD9F-B1931560DBFC(501)>:66317] Ignoring jetsam update because this process is not memory-managed
default	10:09:31.958787-0500	runningboardd	[app<application.com.nexy.assistant.22956984.22956990.7DD7DE9D-9598-4018-AD9F-B1931560DBFC(501)>:66317] Ignoring suspend because this process is not lifecycle managed
default	10:09:31.958798-0500	runningboardd	[app<application.com.nexy.assistant.22956984.22956990.7DD7DE9D-9598-4018-AD9F-B1931560DBFC(501)>:66317] Ignoring GPU update because this process is not GPU managed
default	10:09:31.958825-0500	runningboardd	[app<application.com.nexy.assistant.22956984.22956990.7DD7DE9D-9598-4018-AD9F-B1931560DBFC(501)>:66317] Ignoring memory limit update because this process is not memory-managed
default	10:09:31.964267-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.22956984.22956990.7DD7DE9D-9598-4018-AD9F-B1931560DBFC(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	10:09:31.979295-0500	gamepolicyd	Received state update for 66317 (app<application.com.nexy.assistant.22956984.22956990.7DD7DE9D-9598-4018-AD9F-B1931560DBFC(501)>, running-active-NotVisible
default	10:09:32.004300-0500	Nexy	                AUHAL.cpp:473   ~AUHAL: (0x9c0730040) Selecting device 0 from destructor
default	10:09:32.004329-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0x9c0730040)
default	10:09:32.004343-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0x9c0730040) not already running
default	10:09:32.004350-0500	Nexy	                AUHAL.cpp:687   SelectDevice: (0x9c0730040) disconnecting device 89
default	10:09:32.004359-0500	Nexy	                AUHAL.cpp:751   SelectDevice: (0x9c0730040) destroying ioproc 0xa for device 89
default	10:09:32.004404-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xa}
default	10:09:32.004442-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	10:09:32.004614-0500	Nexy	                AUHAL.cpp:853   SelectDevice: (0x9c0730040) nothing to setup
default	10:09:32.004630-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x9c0730040) adding 0 device listeners to device 0
default	10:09:32.004637-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x9c0730040) adding 0 device delegate listeners to device 0
default	10:09:32.004646-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x9c0730040) removing 7 device listeners from device 89
default	10:09:32.004878-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x9c0730040) removing 0 device delegate listeners from device 89
default	10:09:32.004894-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0x9c0730040)
default	10:09:32.144454-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=66328.1, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=66317, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.osascript, pid=66328, auid=501, euid=501, binary_path=/usr/bin/osascript}, },
default	10:09:32.145915-0500	tccd	AUTHREQ_SUBJECT: msgID=66328.1, subject=com.nexy.assistant,
default	10:09:32.146552-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc90d7ed00 at /Applications/Nexy.app
default	10:09:32.164829-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=582.1102, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=66317, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.osascript, pid=66328, auid=501, euid=501, binary_path=/usr/bin/osascript}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=582, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	10:09:32.165663-0500	tccd	AUTHREQ_SUBJECT: msgID=582.1102, subject=com.nexy.assistant,
default	10:09:32.166333-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc90d7ed00 at /Applications/Nexy.app
default	10:09:32.206885-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc90d7c600 at /Applications/Nexy.app
default	10:09:32.227534-0500	System Events	TCCAccessRequestIndirect: TCCAccessRequestIndirect with pid 66247: target_identity: {
    kTCCCodeIdentityAuditToken = {length = 32, bytes = 0xf5010000 f5010000 14000000 f5010000 ... af860100 ae2b0200 };
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
default	10:09:32.257627-0500	tccd	target_executable_path_URL: file:///Applications/Nexy.app/Contents/MacOS/Nexy
default	10:09:33.236010-0500	Nexy	[0x9c0609400] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
error	10:09:33.236756-0500	tccd	TCCDProcess: identifier=com.nexy.assistant, pid=66317, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy attempted to call TCCAccessRequest for kTCCServiceAccessibility without the recommended com.apple.private.tcc.manager.check-by-audit-token entitlement
default	10:09:33.236949-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=66317.3, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=66317, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.nexy.assistant, pid=66317, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	10:09:33.238198-0500	tccd	AUTHREQ_SUBJECT: msgID=66317.3, subject=com.nexy.assistant,
default	10:09:33.239274-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc90d7ed00 at /Applications/Nexy.app
default	10:09:33.254761-0500	Nexy	[0x9c0609400] invalidated after the last release of the connection object
default	10:09:33.254885-0500	Nexy	[0x9c0609400] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
error	10:09:33.255404-0500	tccd	TCCDProcess: identifier=com.nexy.assistant, pid=66317, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy attempted to call TCCAccessRequest for kTCCServiceAccessibility without the recommended com.apple.private.tcc.manager.check-by-audit-token entitlement
default	10:09:33.255590-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=66317.4, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=66317, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.nexy.assistant, pid=66317, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	10:09:33.256547-0500	tccd	AUTHREQ_SUBJECT: msgID=66317.4, subject=com.nexy.assistant,
default	10:09:33.257253-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc90d7ed00 at /Applications/Nexy.app
default	10:09:33.270989-0500	Nexy	[0x9c0609400] invalidated after the last release of the connection object
default	10:09:33.271081-0500	Nexy	[0x9c0609400] activating connection: mach=true listener=false peer=false name=com.apple.universalaccessAuthWarn
default	10:09:33.271193-0500	Nexy	[0x9c0609400] invalidated after the last release of the connection object
default	10:09:33.272175-0500	Nexy	server port 0x00014a03, session port 0x00003413
default	10:09:33.284153-0500	kernel	SK[8]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid DD91EA9D-8142-443D-9F75-35037C951F62 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.64363,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0x0e25fe68 tp_proto=0x06"
default	10:09:33.284255-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:64363<-><IPv4-redacted>:53] interface: utun6 (skipped: 2519)
so_gencnt: 496352 t_state: SYN_SENT process: Nexy:66317 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 1 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xb773dccb
default	10:09:33.284943-0500	kernel	tcp connected: [<IPv4-redacted>:64363<-><IPv4-redacted>:53] interface: utun6 (skipped: 2519)
so_gencnt: 496352 t_state: ESTABLISHED process: Nexy:66317 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 1 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xb773dccb
default	10:09:33.285370-0500	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:64363<-><IPv4-redacted>:53] interface: utun6 (skipped: 2519)
so_gencnt: 496352 t_state: FIN_WAIT_1 process: Nexy:66317 Duration: 0.002 sec Conn_Time: 0.001 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 1.000 ms rttvar: 0.500 ms base rtt: 1 ms so_error: 0 svc/tc: 0 flow: 0xb773dccb
default	10:09:33.285379-0500	kernel	tcp_connection_summary [<IPv4-redacted>:64363<-><IPv4-redacted>:53] interface: utun6 (skipped: 2519)
so_gencnt: 496352 t_state: FIN_WAIT_1 process: Nexy:66317 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	10:09:33.296823-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc90d7cc00 at /Applications/Nexy.app
default	10:09:33.300365-0500	kernel	SK[9]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid FDA5F016-01E5-4A37-ACAA-30553D1AF144 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.64364,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0x1270b4b8 tp_proto=0x06"
default	10:09:33.300424-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:64364<-><IPv4-redacted>:53] interface: utun6 (skipped: 2519)
so_gencnt: 496353 t_state: SYN_SENT process: Nexy:66317 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 1 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xb34159ec
default	10:09:33.300503-0500	Nexy	networkd_settings_read_from_file initialized networkd settings by reading plist directly
default	10:09:33.300693-0500	Nexy	networkd_settings_read_from_file initialized networkd settings by reading plist directly
default	10:09:33.301135-0500	kernel	tcp connected: [<IPv4-redacted>:64364<-><IPv4-redacted>:53] interface: utun6 (skipped: 2519)
so_gencnt: 496353 t_state: ESTABLISHED process: Nexy:66317 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 1 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xb34159ec
default	10:09:33.301356-0500	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:64364<-><IPv4-redacted>:53] interface: utun6 (skipped: 2519)
so_gencnt: 496353 t_state: FIN_WAIT_1 process: Nexy:66317 Duration: 0.002 sec Conn_Time: 0.001 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 1.000 ms rttvar: 0.500 ms base rtt: 1 ms so_error: 0 svc/tc: 0 flow: 0xb34159ec
default	10:09:33.301367-0500	kernel	tcp_connection_summary [<IPv4-redacted>:64364<-><IPv4-redacted>:53] interface: utun6 (skipped: 2519)
so_gencnt: 496353 t_state: FIN_WAIT_1 process: Nexy:66317 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	10:09:33.301667-0500	Nexy	nw_path_libinfo_path_check [C8869F54-B845-4BFF-B26A-66A0272FB925 IPv4#afab669c:443 tcp, legacy-socket, attribution: developer]
	libinfo check path: <private>
default	10:09:33.302095-0500	kernel	SK[7]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 825C703E-9F8B-4BEF-85FB-B995E67E30AE flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.64365,dst=<IPv4-redacted>.443,proto=0x06 mask=0x0000003f,hash=0x8425ae56 tp_proto=0x06"
default	10:09:33.302125-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:64365<-><IPv4-redacted>:443] interface: utun6 (skipped: 2519)
so_gencnt: 496354 t_state: SYN_SENT process: Nexy:66317 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x8b3cb335
default	10:09:33.302341-0500	kernel	tcp connected: [<IPv4-redacted>:64365<-><IPv4-redacted>:443] interface: utun6 (skipped: 2519)
so_gencnt: 496354 t_state: ESTABLISHED process: Nexy:66317 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x8b3cb335
default	10:09:33.319402-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc90d7c600 at /Applications/Nexy.app
default	10:09:33.324451-0500	tccd	Publishing <TCCDEvent: type=Modify, service=kTCCServiceAccessibility, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 0 subscribers: {
}
default	10:09:33.501511-0500	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:64365<-><IPv4-redacted>:443] interface: utun6 (skipped: 2519)
so_gencnt: 496354 t_state: FIN_WAIT_1 process: Nexy:66317 Duration: 0.200 sec Conn_Time: 0.001 sec bytes in/out: 3863/1889 pkts in/out: 4/5 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 1.000 ms rttvar: 0.250 ms base rtt: 1 ms so_error: 0 svc/tc: 0 flow: 0x8b3cb335
default	10:09:33.501524-0500	kernel	tcp_connection_summary [<IPv4-redacted>:64365<-><IPv4-redacted>:443] interface: utun6 (skipped: 2519)
so_gencnt: 496354 t_state: FIN_WAIT_1 process: Nexy:66317 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	10:09:33.600250-0500	runningboardd	Assertion did invalidate due to timeout: 585-585-277080 (target:[app<application.com.nexy.assistant.22956984.22956990.7DD7DE9D-9598-4018-AD9F-B1931560DBFC(501)>:66317])
default	10:09:33.614983-0500	Nexy	Entering exit handler.
default	10:09:33.615015-0500	Nexy	Queueing exit procedure onto XPC queue. Any further messages sent will be discarded. activeSendTransactions=0
default	10:09:33.615058-0500	Nexy	Cancelling XPC connection. Any further reply handler invocations will not retry messages
default	10:09:33.615065-0500	Nexy	[0x9c0608000] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	10:09:33.615092-0500	Nexy	Exiting exit handler.
default	10:09:33.615099-0500	Nexy	XPC connection invalidated (daemon unloaded/disabled)
default	10:09:33.615518-0500	audiomxd	  ServerSessionManager.mm:478   { "action":"destroy_session", "session":{"ID":"0x280022","name":"Nexy(66317)"}, "details":null }
default	10:09:33.616308-0500	audiomxd	AudioApplicationInfoImpl.mm:690   Successfully removed session 0x280022 from AudioApp, recording state unchanged (app: {"name":"[implicit] Nexy","pid":66317})
default	10:09:33.616336-0500	audiomxd	  ServerSessionManager.mm:1086  destroy audio app instance since was created implicitly by session creation and all sessions now gone (audio app: {"name":"[implicit] Nexy","pid":66317})
default	10:09:33.617006-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 35, PID = 66317, Name = sid:0x280022, Nexy(66317), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	10:09:33.616259-0500	WindowServer	0[outside of RPC]: Process death: 0x0-0x186186 (Nexy) connectionID: 10043F pid: 66317 in session 0x101
default	10:09:33.617104-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 35, PID = 66317, Name = sid:0x280022, Nexy(66317), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	10:09:33.616309-0500	WindowServer	<BSCompoundAssertion:0xc51015580> ([FocusManager:257]-deferringPolicyEvaluationSuppression) acquire for reason:process death - 0x0-0x186186 (Nexy) acq:0xc5354e540 count:1
default	10:09:33.617623-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	10:09:33.617712-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	10:09:33.617396-0500	audiomxd	UpdateAudioState CID 0xBDB10001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	10:09:33.617553-0500	audiomxd	UpdateAudioState CID 0xBDB10001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	10:09:33.618076-0500	WindowServer	0[outside of RPC]: [FocusManager:257] update to deferring policy requested for reason: permitted list updated - 0x0-0x186186 removed - but we are suppressing evaluation for reasons: {(
    "process death - 0x0-0x186186 (Nexy)"
)}
default	10:09:33.618567-0500	WindowServer	0[outside of RPC]: [FocusManager:257] update to deferring policy requested for reason: permitted list updated - 0x1-0x1030d removed - but we are suppressing evaluation for reasons: {(
    "process death - 0x0-0x186186 (Nexy)"
)}
default	10:09:33.622203-0500	runningboardd	[app<application.com.nexy.assistant.22956984.22956990.7DD7DE9D-9598-4018-AD9F-B1931560DBFC(501)>:66317] termination reported by launchd (0, 0, 0)
default	10:09:33.622334-0500	runningboardd	Removing process: [app<application.com.nexy.assistant.22956984.22956990.7DD7DE9D-9598-4018-AD9F-B1931560DBFC(501)>:66317]
default	10:09:33.622699-0500	runningboardd	Removing launch job for: [app<application.com.nexy.assistant.22956984.22956990.7DD7DE9D-9598-4018-AD9F-B1931560DBFC(501)>:66317]
default	10:09:33.623106-0500	runningboardd	Removed job for [app<application.com.nexy.assistant.22956984.22956990.7DD7DE9D-9598-4018-AD9F-B1931560DBFC(501)>:66317]
default	10:09:33.623168-0500	runningboardd	Removing assertions for terminated process: [app<application.com.nexy.assistant.22956984.22956990.7DD7DE9D-9598-4018-AD9F-B1931560DBFC(501)>:66317]
default	10:09:33.623763-0500	coreaudiod	>>> NEGOTIATE [com.nexy.assistant]
default	10:09:33.624068-0500	coreaudiod	<<< NEGOTIATE [com.nexy.assistant]
default	10:09:33.624341-0500	runningboardd	XPC connection invalidated: [app<application.com.nexy.assistant.22956984.22956990.7DD7DE9D-9598-4018-AD9F-B1931560DBFC(501)>:66317]
default	10:09:33.626712-0500	runningboardd	No connection found to send inheritance for process [app<application.com.nexy.assistant.22956984.22956990.7DD7DE9D-9598-4018-AD9F-B1931560DBFC(501)>:66317] with changeSet: <RBSInheritanceChangeSet| gained:(null) lost:{(
    <RBSInheritance| environment:(none) name:com.apple.launchservices.userfacing origID:585-549-277082 0>
)}>
default	10:09:33.628824-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	10:09:33.629019-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	10:09:33.630438-0500	coreaudiod	IssueReporting.cpp:492   RTAID [ use_case=Generic report_type=RMS Generic Chain clientID=ADM node=ADM::com.nexy.assistant_2363.2224.0_airpods noise suppression studio::out-0 issue_detected_sample_time=24480.000000 ] -- [ rms:[-38.978218], peaks:[-21.112564] ]
default	10:09:33.630456-0500	coreaudiod	IssueReporting.cpp:492   RTAID [ use_case=Generic report_type=RMS Generic Chain clientID=ADM node=ADM::com.nexy.assistant_2363.2224.0_airpods noise suppression studio::in-0 issue_detected_sample_time=0.000000 ] -- [ rms:[-37.721947], peaks:[-22.232323] ]
default	10:09:33.634820-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.22956984.22956990.7DD7DE9D-9598-4018-AD9F-B1931560DBFC(501)>: none (role: None) (endowments: (null))
default	10:09:33.635091-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.22956984.22956990.7DD7DE9D-9598-4018-AD9F-B1931560DBFC(501)>: none (role: None) (endowments: (null))
default	10:09:33.635231-0500	audiomxd	  ServerSessionManager.mm:1327  Monitored process died, pid = 66317, name = Nexy
default	10:09:33.635787-0500	launchservicesd	Hit the server for a process handle 16b32e540001030d that resolved to: [app<application.com.nexy.assistant.22956984.22956990.7DD7DE9D-9598-4018-AD9F-B1931560DBFC(501)>:66317]
default	10:09:33.635864-0500	gamepolicyd	Received state update for 66317 (app<application.com.nexy.assistant.22956984.22956990.7DD7DE9D-9598-4018-AD9F-B1931560DBFC(501)>, none-NotVisible
default	10:09:33.637592-0500	loginwindow	-[ApplicationManager handleCASEvent:withData:] | CAS notification for appDeath for com.nexy.assistant with asn: LSASN:{hi=0x0;lo=0x186186} for bundle path: /Applications/Nexy.app with URL: file:///Applications/Nexy.app/
default	10:09:33.637620-0500	loginwindow	-[Application setState:] | enter: <Application: 0x8f500bde0: Nexy> state 3
default	10:09:33.637635-0500	loginwindow	-[PersistentAppsSupport applicationQuit:] | for app:Nexy, _appTrackingState = 2
default	10:09:33.641174-0500	loginwindow	-[Application setState:] | enter: <Application: 0x8f500bde0: Nexy> state 4
default	10:09:33.641185-0500	loginwindow	-[PersistentAppsSupport applicationQuit:] | for app:Nexy, _appTrackingState = 2
error	10:09:33.800514-0500	runningboardd	RBSStateCapture remove item called for untracked item 585-585-277080 (target:[app<application.com.nexy.assistant.22956984.22956990.7DD7DE9D-9598-4018-AD9F-B1931560DBFC(501)>:66317])
