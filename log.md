default	19:20:18.228666-0500	lsd	com.nexy.assistant/Unknown Persona:5:5:1:1:Building bundle record for app
default	19:20:18.228841-0500	lsd	com.nexy.assistant/Unknown Persona:5:5:2:1:Built bundle record for app
default	19:20:18.230947-0500	lsd	com.nexy.assistant/Unknown Persona:5:4:2:1:_LSServerRegisterItemInfo result = 0
default	19:20:18.241153-0500	runningboardd	Launch request for app<application.com.nexy.assistant.27212639.27212645(501)>[0] is using uid 501 (divined from auid 501 euid 501)
default	19:20:18.241242-0500	runningboardd	Acquiring assertion targeting app<application.com.nexy.assistant.27212639.27212645(501)> from originator [osservice<com.apple.coreservices.uiagent(501)>:3678] with description <RBSAssertionDescriptor| "LS launch com.nexy.assistant" ID:403-3678-153542 target:app<application.com.nexy.assistant.27212639.27212645(501)> attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"LaunchRoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	19:20:18.241337-0500	runningboardd	Assertion 403-3678-153542 (target:app<application.com.nexy.assistant.27212639.27212645(501)>) will be created as active
default	19:20:18.236243-0500	dmd	Received xpc stream event (distributed notification matching) with name: com.apple.LaunchServices.applicationRegistered user info: {
    CFBundleDisplayName = Nexy;
    bundleIDs =     (
        "com.nexy.assistant"
    );
    isPlaceholder = 0;
}
default	19:20:18.244340-0500	runningboardd	Checking PreventLaunch: global:0 exPath:/Applications/Nexy.app/Contents/MacOS/Nexy predicates:(null) allow:(null)
default	19:20:18.244381-0500	runningboardd	Creating and launching job for: app<application.com.nexy.assistant.27212639.27212645(501)>
default	19:20:18.244395-0500	runningboardd	_mutateContextIfNeeded called for com.nexy.assistant
default	19:20:18.244477-0500	runningboardd	app<application.com.nexy.assistant.27212639.27212645(501)>: -[RBPersonaManager personaForIdentity:context:personaUID:personaUniqueString:] required 0.000000 ms (wallclock); resolved to {4294967295, (null)}
default	19:20:18.309889-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645(501)>:5671] is not RunningBoard jetsam managed.
default	19:20:18.309907-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645(501)>:5671] This process will not be managed.
default	19:20:18.309925-0500	runningboardd	Now tracking process: [app<application.com.nexy.assistant.27212639.27212645(501)>:5671]
default	19:20:18.310187-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.27212639.27212645(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	19:20:18.311055-0500	gamepolicyd	Hit the server for a process handle f8c59c400001627 that resolved to: [app<application.com.nexy.assistant.27212639.27212645(501)>:5671]
default	19:20:18.311094-0500	gamepolicyd	Received state update for 5671 (app<application.com.nexy.assistant.27212639.27212645(501)>, running-active-NotVisible
default	19:20:18.314500-0500	runningboardd	Using default underlying assertion for app: [app<application.com.nexy.assistant.27212639.27212645(501)>:5671]
default	19:20:18.314579-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.27212639.27212645(501)>:5671] from originator [app<application.com.nexy.assistant.27212639.27212645(501)>:5671] with description <RBSAssertionDescriptor| "RB Underlying Assertion" ID:403-403-153543 target:5671 attributes:[
	<RBSDomainAttribute| domain:"com.apple.underlying" name:"defaultUnderlyingAppAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	19:20:18.314737-0500	runningboardd	Assertion 403-403-153543 (target:[app<application.com.nexy.assistant.27212639.27212645(501)>:5671]) will be created as active
default	19:20:18.314959-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645(501)>:5671] Ignoring jetsam update because this process is not memory-managed
default	19:20:18.314995-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645(501)>:5671] Ignoring suspend because this process is not lifecycle managed
default	19:20:18.315018-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645(501)>:5671] Set darwin role to: UserInteractive
default	19:20:18.315030-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645(501)>:5671] Ignoring GPU update because this process is not GPU managed
default	19:20:18.315047-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645(501)>:5671] Ignoring memory limit update because this process is not memory-managed
default	19:20:18.315143-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645(501)>:5671] reported to RB as running
default	19:20:18.317174-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.27212639.27212645(501)>:5671] from originator [osservice<com.apple.coreservices.launchservicesd>:367] with description <RBSAssertionDescriptor| "uielement:5671" ID:403-367-153544 target:5671 attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"RoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	19:20:18.317291-0500	runningboardd	Assertion 403-367-153544 (target:[app<application.com.nexy.assistant.27212639.27212645(501)>:5671]) will be created as active
default	19:20:18.317476-0500	CoreServicesUIAgent	LAUNCH: 0x0-0x3a03a0 com.nexy.assistant starting stopped process.
default	19:20:18.320175-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645(501)>:5671] Ignoring jetsam update because this process is not memory-managed
default	19:20:18.319117-0500	loginwindow	-[Application updateInformation] | Got App URL: file:///Applications/Nexy.app/
default	19:20:18.320193-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645(501)>:5671] Ignoring suspend because this process is not lifecycle managed
default	19:20:18.320230-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645(501)>:5671] Ignoring GPU update because this process is not GPU managed
default	19:20:18.320280-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645(501)>:5671] Ignoring memory limit update because this process is not memory-managed
default	19:20:18.320426-0500	runningboardd	Successfully acquired underlying assertion for [app<application.com.nexy.assistant.27212639.27212645(501)>:5671]
default	19:20:18.320521-0500	loginwindow	-[Application setState:] | enter: <Application: 0x84f9b4500: Nexy> state 2
default	19:20:18.320880-0500	loginwindow	-[ApplicationManager checkInAppContext:eventData:] | ApplicationManager: Checked in app : Nexy
default	19:20:18.321446-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.27212639.27212645(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	19:20:18.321782-0500	runningboardd	Invalidating assertion 403-3678-153542 (target:app<application.com.nexy.assistant.27212639.27212645(501)>) from originator [osservice<com.apple.coreservices.uiagent(501)>:3678]
default	19:20:18.321819-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645(501)>:5671] Ignoring jetsam update because this process is not memory-managed
default	19:20:18.321834-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645(501)>:5671] Ignoring suspend because this process is not lifecycle managed
default	19:20:18.321947-0500	gamepolicyd	Received state update for 5671 (app<application.com.nexy.assistant.27212639.27212645(501)>, running-active-NotVisible
default	19:20:18.321850-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645(501)>:5671] Ignoring GPU update because this process is not GPU managed
default	19:20:18.321933-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645(501)>:5671] Ignoring memory limit update because this process is not memory-managed
default	19:20:18.324660-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.27212639.27212645(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	19:20:18.426060-0500	gamepolicyd	Received state update for 5671 (app<application.com.nexy.assistant.27212639.27212645(501)>, running-active-NotVisible
default	19:20:18.428963-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645(501)>:5671] Ignoring jetsam update because this process is not memory-managed
default	19:20:18.428986-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645(501)>:5671] Ignoring suspend because this process is not lifecycle managed
default	19:20:18.429004-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645(501)>:5671] Ignoring GPU update because this process is not GPU managed
default	19:20:18.429038-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645(501)>:5671] Ignoring memory limit update because this process is not memory-managed
default	19:20:18.431833-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.27212639.27212645(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	19:20:18.432188-0500	gamepolicyd	Received state update for 5671 (app<application.com.nexy.assistant.27212639.27212645(501)>, running-active-NotVisible
default	19:20:18.586862-0500	tccd	AUTHREQ_SUBJECT: msgID=483.32, subject=com.nexy.assistant,
default	19:20:18.587544-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x92f17b600 at /Applications/Nexy.app
default	19:20:18.742165-0500	Nexy	[0x1059d97c0] activating connection: mach=true listener=false peer=false name=com.apple.cfprefsd.daemon
default	19:20:18.742244-0500	Nexy	[0x1059d9d00] activating connection: mach=true listener=false peer=false name=com.apple.cfprefsd.agent
error	19:20:19.005590-0500	Nexy	dlsym cannot find symbol NSMakeRect in CFBundle 0xa6a680000 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	19:20:19.005820-0500	Nexy	dlsym cannot find symbol NSMakePoint in CFBundle 0xa6a680000 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	19:20:19.006014-0500	Nexy	dlsym cannot find symbol NSMakeSize in CFBundle 0xa6a680000 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	19:20:19.006203-0500	Nexy	dlsym cannot find symbol NSMakeRange in CFBundle 0xa6a680000 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
default	19:20:19.007345-0500	Nexy	[0x1059c8280] activating connection: mach=true listener=false peer=false name=com.apple.coreservices.launchservicesd
default	19:20:19.008091-0500	Nexy	[0xa69c24000] activating connection: mach=true listener=false peer=false name=com.apple.analyticsd
default	19:20:19.008466-0500	Nexy	[0xa69c24140] activating connection: mach=true listener=false peer=false name=com.apple.pasteboard.1
default	19:20:19.008876-0500	Nexy	[0xa69c24280] activating connection: mach=true listener=false peer=false name=com.apple.distributed_notifications@Uv3
default	19:20:19.009197-0500	Nexy	Received configuration update from daemon (initial)
default	19:20:19.010942-0500	Nexy	void _NSDisableAutomaticTerminationAndLog(NSString *) No windows open yet
default	19:20:19.011331-0500	Nexy	[0xa69c243c0] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	19:20:19.011960-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=5671.1, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=5671, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	19:20:19.013514-0500	tccd	AUTHREQ_SUBJECT: msgID=5671.1, subject=com.nexy.assistant,
default	19:20:19.014286-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x92f178300 at /Applications/Nexy.app
default	19:20:19.028181-0500	Nexy	[0xa69c243c0] invalidated after the last release of the connection object
default	19:20:19.028517-0500	Nexy	server port 0x00003407, session port 0x00003407
default	19:20:19.029552-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=397.2568, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=5671, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=397, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	19:20:19.029577-0500	tccd	requestor: TCCDProcess: identifier=com.apple.WindowServer, pid=397, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=5671, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	19:20:19.030494-0500	tccd	AUTHREQ_SUBJECT: msgID=397.2568, subject=com.nexy.assistant,
default	19:20:19.031337-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x92f178300 at /Applications/Nexy.app
default	19:20:19.047421-0500	Nexy	New connection 0x10e3c3 main
default	19:20:19.050261-0500	Nexy	CHECKIN: pid=5671
default	19:20:19.059099-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.27212639.27212645(501)>:5671] from originator [osservice<com.apple.coreservices.launchservicesd>:367] with description <RBSAssertionDescriptor| "uielement:5671" ID:403-367-153545 target:5671 attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"RoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	19:20:19.059209-0500	runningboardd	Assertion 403-367-153545 (target:[app<application.com.nexy.assistant.27212639.27212645(501)>:5671]) will be created as active
default	19:20:19.059253-0500	Nexy	CHECKEDIN: pid=5671 asn=0x0-0x3a03a0 foreground=0
default	19:20:19.059600-0500	runningboardd	Invalidating assertion 403-367-153544 (target:[app<application.com.nexy.assistant.27212639.27212645(501)>:5671]) from originator [osservice<com.apple.coreservices.launchservicesd>:367]
default	19:20:19.059144-0500	launchservicesd	CHECKIN:0x0-0x3a03a0 5671 com.nexy.assistant
default	19:20:19.059595-0500	loginwindow	-[Application updateInformation] | Got App URL: file:///Applications/Nexy.app/
default	19:20:19.059715-0500	loginwindow	-[ApplicationManager checkInAppContext:eventData:] | ApplicationManager: Checked in app : Nexy
default	19:20:19.059554-0500	Nexy	[0xa69c243c0] activating connection: mach=false listener=true peer=false name=(anonymous)
default	19:20:19.059581-0500	Nexy	[0xa69c243c0] Connection returned listener port: 0x4503
default	19:20:19.060033-0500	Nexy	[0xa69c50300] activating connection: mach=false listener=false peer=true name=com.apple.xpc.anonymous.0xa69c243c0.peer[367].0xa69c50300
default	19:20:19.062268-0500	Nexy	FRONTLOGGING: version 1
default	19:20:19.062279-0500	Nexy	Registered, pid=5671 ASN=0x0,0x3a03a0
default	19:20:19.062613-0500	WindowServer	10e3c3[CreateApplication]: Process creation: 0x0-0x3a03a0 (Nexy) connectionID: 10E3C3 pid: 5671 in session 0x101
default	19:20:19.062700-0500	Nexy	[0xa69c24500] activating connection: mach=true listener=false peer=false name=com.apple.lsd.mapdb
default	19:20:19.075131-0500	Nexy	[0xa69c243c0] Connection returned listener port: 0x4503
default	19:20:19.075752-0500	Nexy	BringForward: pid=5671 asn=0x0-0x3a03a0 bringForward=0 foreground=0 uiElement=1 launchedByLS=1 modifiersCount=1 allDisabled=0
default	19:20:19.075885-0500	Nexy	BringFrontModifier: pid=5671 asn=0x0-0x3a03a0 Modifier 0 hideAfter=0 hideOthers=0 dontMakeFrontmost=0 mouseDown=0/0 seed=0/0
default	19:20:19.076585-0500	Nexy	Current system appearance, (HLTB: 2), (SLS: 1)
default	19:20:19.078594-0500	Nexy	No persisted cache on this platform.
default	19:20:19.080326-0500	Nexy	Current system appearance, (HLTB: 2), (SLS: 1)
default	19:20:19.081132-0500	Nexy	Post-registration system appearance: (HLTB: 2)
default	19:20:19.083787-0500	Nexy	FBSWorkspace: endpoint monitoring is disabled.
default	19:20:19.083798-0500	Nexy	FBSWorkspace: default shell endpoint is disabled.
default	19:20:19.083854-0500	Nexy	Initializing connection
default	19:20:19.083895-0500	Nexy	Removing all cached process handles
default	19:20:19.083916-0500	Nexy	Sending handshake request attempt #1 to server
default	19:20:19.083925-0500	Nexy	Creating connection to com.apple.runningboard
default	19:20:19.083935-0500	Nexy	[0xa69c24780] activating connection: mach=true listener=false peer=false name=com.apple.runningboard
default	19:20:19.084388-0500	runningboardd	Setting client for [app<application.com.nexy.assistant.27212639.27212645(501)>:5671] as ready
default	19:20:19.085031-0500	Nexy	Handshake succeeded
default	19:20:19.085048-0500	Nexy	Identity resolved as app<application.com.nexy.assistant.27212639.27212645(501)>
default	19:20:19.089894-0500	Nexy	[0xa69c243c0] Connection returned listener port: 0x4503
default	19:20:19.091039-0500	distnoted	register name: com.apple.xctest.FakeForceTouchDevice object: com.nexy.assistant token: 1e0000001d pid: 5671
default	19:20:19.093776-0500	Nexy	[0xa69c243c0] Connection returned listener port: 0x4503
default	19:20:19.097552-0500	Nexy	Created a new Process Instance Registry XPC connection (inactive)
default	19:20:19.097579-0500	Nexy	[0xa69c248c0] activating connection: mach=true listener=false peer=false name=com.apple.linkd.autoShortcut
default	19:20:19.097672-0500	Nexy	Activated connection to com.apple.linkd.autoShortcut (ApplicationService)
default	19:20:19.097744-0500	Nexy	[0xa69c24a00] activating connection: mach=false listener=true peer=false name=(anonymous)
default	19:20:19.099071-0500	Nexy	[0xa69c24a00] Connection returned listener port: 0x6903
default	19:20:19.099924-0500	Nexy	Registered process with identifier 5671-1736392
default	19:20:19.345896-0500	Nexy	Registered notify signal com.apple.caulk.alloc.rtdump (0)
default	19:20:19.349092-0500	Nexy	System_Input_Processing_Notification_Handler.mm:456   System_Input_Processing_Notification_Handler::is_vi_available(): Voice isolation DSP is available for client with bundle id com.nexy.assistant (AVFoundation is available, application is not in client deny list, application is not FaceTime variant)
default	19:20:19.351557-0500	Nexy	[0xa69c24b40] activating connection: mach=true listener=false peer=false name=com.apple.cmio.registerassistantservice.system-extensions
fault	19:20:19.357819-0500	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.27212639.27212645 AUID=501> and <type=Application identifier=application.com.nexy.assistant.27212639.27212645>
default	19:20:19.363239-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOInitializeListenersForBundleID: for <private> -> <private>
default	19:20:19.365997-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> vpio_preferenceChangedListener: new value ((null)) for key AUVoiceIOClients/com-nexy-assistant/AUVoiceIOChatFlavor, translatedBundleID com.nexy.assistant, bundleIDs {(
    "com.nexy.assistant"
)}
default	19:20:19.366167-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> vpio_preferenceChangedListener: new value ((null)) for key AUVoiceIOClients/com-nexy-assistant/AUVoiceIOIsAutoChatFlavorEnabled, translatedBundleID com.nexy.assistant, bundleIDs {(
    "com.nexy.assistant"
)}
default	19:20:19.366333-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetSupportedChatFlavorsForBundleID: <private>-><private> get supported chat flavors: <private>
default	19:20:19.366343-0500	Nexy	            HALSystem.cpp:134    Enabling HAL Voice Isolation support
default	19:20:19.366503-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetHiddenChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	19:20:19.366631-0500	Nexy	[0xa69c24c80] activating connection: mach=true listener=false peer=false name=com.apple.tccd
default	19:20:19.366996-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOHiddenChatFlavors newValue: (
    1
)
default	19:20:19.367343-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=5671.2, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=5671, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	19:20:19.377110-0500	tccd	AUTHREQ_SUBJECT: msgID=5671.2, subject=com.nexy.assistant,
default	19:20:19.378530-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc79245800 at /Applications/Nexy.app
default	19:20:19.408533-0500	Nexy	[0xa69c24c80] invalidated after the last release of the connection object
default	19:20:19.408596-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetSupportedChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	19:20:19.412002-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOSupportedChatFlavors newValue: (
)
default	19:20:19.413548-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=411.1476, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=5671, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=398, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	19:20:19.414544-0500	tccd	AUTHREQ_SUBJECT: msgID=411.1476, subject=com.nexy.assistant,
default	19:20:19.415148-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc79245800 at /Applications/Nexy.app
error	19:20:19.441718-0500	tccd	Request message contains a target_token to accessing_process (TCCDProcess: identifier=com.nexy.assistant, pid=5671, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy) but TCCDProcess: identifier=com.apple.audio.coreaudiod, pid=411, auid=202, euid=202, binary_path=/usr/sbin/coreaudiod is not a TCC manager for service: kTCCServiceScreenCapture.
default	19:20:19.442698-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=411.1478, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=5671, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=398, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	19:20:19.443629-0500	tccd	AUTHREQ_SUBJECT: msgID=411.1478, subject=com.nexy.assistant,
default	19:20:19.444226-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc79245800 at /Applications/Nexy.app
default	19:20:19.474984-0500	Nexy	  HALPlugInManagement.cpp:440    HALPlugInManagement::RegisterPlugIns: skipping in-process plug-ins
error	19:20:19.477039-0500	Nexy	AddInstanceForFactory: No factory registered for id <CFUUID 0xa6b58dd80> F8BB1C28-BAE8-11D6-9C31-00039315CD46
default	19:20:19.495933-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	19:20:19.496093-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	19:20:19.500931-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetPreferredChatFlavorForBundleID: <private>-><private> get value: 0
default	19:20:21.879235-0500	kernel	SK[6]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 267679F5-710F-47F7-85E2-F8CD750C0CEC flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.54938,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0xdc02fff3 tp_proto=0x06"
default	19:20:21.879311-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:54938<-><IPv4-redacted>:53] interface: utun6 (skipped: 47531)
so_gencnt: 2850958 t_state: SYN_SENT process: Nexy:5671 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 1 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x958e94b7
default	19:20:21.879957-0500	kernel	tcp connected: [<IPv4-redacted>:54938<-><IPv4-redacted>:53] interface: utun6 (skipped: 47531)
so_gencnt: 2850958 t_state: ESTABLISHED process: Nexy:5671 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 1 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x958e94b7
default	19:20:21.880225-0500	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:54938<-><IPv4-redacted>:53] interface: utun6 (skipped: 47531)
so_gencnt: 2850958 t_state: FIN_WAIT_1 process: Nexy:5671 Duration: 0.002 sec Conn_Time: 0.001 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 1.000 ms rttvar: 0.500 ms base rtt: 1 ms so_error: 0 svc/tc: 0 flow: 0x958e94b7
default	19:20:21.880235-0500	kernel	tcp_connection_summary [<IPv4-redacted>:54938<-><IPv4-redacted>:53] interface: utun6 (skipped: 47531)
so_gencnt: 2850958 t_state: FIN_WAIT_1 process: Nexy:5671 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	19:20:21.910768-0500	Nexy	[0xa69c24c80] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioComponentRegistrar
default	19:20:21.926235-0500	Nexy	                AUHAL.cpp:420   AUHAL: (0xa69a48740) Selecting device 85 from constructor
default	19:20:21.926249-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0xa69a48740)
default	19:20:21.926254-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0xa69a48740) not already running
default	19:20:21.926259-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0xa69a48740) nothing to teardown
default	19:20:21.926263-0500	Nexy	                AUHAL.cpp:762   SelectDevice: (0xa69a48740) connecting device 85
default	19:20:21.926354-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0xa69a48740) Device ID: 85 (Input:No | Output:Yes): true
default	19:20:21.926959-0500	Nexy	                AUHAL.cpp:774   SelectDevice: (0xa69a48740) created ioproc 0xa for device 85
default	19:20:21.927057-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0xa69a48740) adding 7 device listeners to device 85
default	19:20:21.927197-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0xa69a48740) adding 0 device delegate listeners to device 85
default	19:20:21.927207-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0xa69a48740)
default	19:20:21.927275-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  48000 Hz, Float32, interleaved
default	19:20:21.927285-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	19:20:21.927290-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	19:20:21.927298-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	19:20:21.927308-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	19:20:21.927390-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0xa69a48740) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	19:20:21.927401-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0xa69a48740) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	19:20:21.927406-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	19:20:21.927412-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0xa69a48740) removing 0 device listeners from device 0
default	19:20:21.927414-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0xa69a48740) removing 0 device delegate listeners from device 0
default	19:20:21.927423-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0xa69a48740)
default	19:20:21.927438-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is DISABLED
default	19:20:21.927519-0500	Nexy	                AUHAL.cpp:2303  SetProperty: (0xa69a48740) caller requesting device change from 85 to 91
default	19:20:21.927526-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0xa69a48740)
default	19:20:21.927532-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0xa69a48740) not already running
default	19:20:21.927536-0500	Nexy	                AUHAL.cpp:687   SelectDevice: (0xa69a48740) disconnecting device 85
default	19:20:21.927540-0500	Nexy	                AUHAL.cpp:751   SelectDevice: (0xa69a48740) destroying ioproc 0xa for device 85
default	19:20:21.927593-0500	Nexy	  AVAudioSession_MacOS.mm:1021  initForMacOS
default	19:20:21.928355-0500	Nexy	[0xa69c24f00] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioSession
default	19:20:21.930383-0500	audiomxd	  ServerSessionManager.mm:315   { "action":"create_session", "session":{"ID":"0x1e8047","name":"Nexy(5671)"}, "details":{"PID":5671,"session_type":"Primary"} }
default	19:20:21.930490-0500	audiomxd	AudioApplicationInfoImpl.mm:250   Setting initial isRecording state: 0 for newly-created AudioApp
	app: {"name":"[implicit] Nexy","pid":5671}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1e8047, sessionType: 'prim', isRecording: false }, 
]
default	19:20:21.931220-0500	audiomxd	  ServerSessionManager.mm:1322  Start process monitoring, pid = 5671, name = Nexy
default	19:20:21.931478-0500	Nexy	    SessionCore_Create.mm:99    Created session 0xa6a691240 with ID: 0x1e8047
default	19:20:21.932585-0500	Nexy	[0xa69c25040] activating connection: mach=true listener=false peer=false name=com.apple.audioanalyticsd
error	19:20:21.933456-0500	Nexy	Reporter disconnected. { function=sendMessage, reporterID=24356759535617 }
default	19:20:21.933470-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped Unknown {1C-77-54-18-C8-A3:output, 0xa}
default	19:20:21.933526-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	19:20:21.933612-0500	Nexy	                AUHAL.cpp:762   SelectDevice: (0xa69a48740) connecting device 91
default	19:20:21.933689-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0xa69a48740) Device ID: 91 (Input:Yes | Output:No): true
default	19:20:21.935010-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=411.1479, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=5671, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=398, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	19:20:21.936325-0500	tccd	AUTHREQ_SUBJECT: msgID=411.1479, subject=com.nexy.assistant,
default	19:20:21.936975-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc79245800 at /Applications/Nexy.app
default	19:20:21.970202-0500	tccd	AUTHREQ_PROMPTING: msgID=411.1479, service=kTCCServiceMicrophone, subject=Sub:{com.nexy.assistant}Resp:{TCCDProcess: identifier=com.nexy.assistant, pid=5671, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy},
default	19:20:23.286854-0500	runningboardd	Assertion did invalidate due to timeout: 403-403-153543 (target:[app<application.com.nexy.assistant.27212639.27212645(501)>:5671])
default	19:20:23.487739-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645(501)>:5671] Ignoring jetsam update because this process is not memory-managed
default	19:20:23.487766-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645(501)>:5671] Ignoring suspend because this process is not lifecycle managed
default	19:20:23.487785-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645(501)>:5671] Ignoring GPU update because this process is not GPU managed
default	19:20:23.487821-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645(501)>:5671] Ignoring memory limit update because this process is not memory-managed
default	19:20:23.493376-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.27212639.27212645(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	19:20:23.494257-0500	gamepolicyd	Received state update for 5671 (app<application.com.nexy.assistant.27212639.27212645(501)>, running-active-NotVisible
default	19:20:23.685520-0500	tccd	Publishing <TCCDEvent: type=Create, service=kTCCServiceMicrophone, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 3 subscribers: {
    468 = "<TCCDEventSubscriber: token=468, state=Passed, csid=com.apple.chronod>";
    37 = "<TCCDEventSubscriber: token=37, state=Initial, csid=(null)>";
    476 = "<TCCDEventSubscriber: token=476, state=Passed, csid=com.apple.photolibraryd>";
}
default	19:20:23.685915-0500	Nexy	                AUHAL.cpp:774   SelectDevice: (0xa69a48740) created ioproc 0xa for device 91
default	19:20:23.686222-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0xa69a48740) adding 7 device listeners to device 91
default	19:20:23.686575-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0xa69a48740) adding 0 device delegate listeners to device 91
default	19:20:23.686594-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0xa69a48740)
default	19:20:23.686615-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 output streams; not all mono
default	19:20:23.686635-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	19:20:23.686868-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  input stream 0 [0x5c]:  1 ch,  24000 Hz, Float32
default	19:20:23.686889-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 input streams; all mono
default	19:20:23.686899-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  1 ch,  24000 Hz, Float32
default	19:20:23.687046-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0xa69a48740) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	19:20:23.687062-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0xa69a48740) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	19:20:23.687071-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	19:20:23.687077-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0xa69a48740) removing 7 device listeners from device 85
default	19:20:23.687321-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0xa69a48740) removing 0 device delegate listeners from device 85
default	19:20:23.687335-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0xa69a48740)
default	19:20:23.688409-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	19:20:23.686534-0500	chronod	[appAuth:com.nexy.assistant] tcc authorization(s) changed
default	19:20:23.690242-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=411.1480, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=5671, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=398, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	19:20:23.692018-0500	tccd	AUTHREQ_SUBJECT: msgID=411.1480, subject=com.nexy.assistant,
default	19:20:23.693074-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc79245800 at /Applications/Nexy.app
default	19:20:23.717675-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	19:20:23.719753-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=411.1481, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=5671, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=398, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	19:20:23.721626-0500	tccd	AUTHREQ_SUBJECT: msgID=411.1481, subject=com.nexy.assistant,
default	19:20:23.722714-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc79245800 at /Applications/Nexy.app
default	19:20:23.744730-0500	Nexy	Registered notify signal com.apple.caulk.alloc.audiodump (0)
default	19:20:23.746551-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=411.1482, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=5671, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=398, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	19:20:23.747594-0500	tccd	AUTHREQ_SUBJECT: msgID=411.1482, subject=com.nexy.assistant,
default	19:20:23.748254-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc79245800 at /Applications/Nexy.app
default	19:20:23.767539-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetPreferredChatFlavorForBundleID: <private>-><private> get value: 0
default	19:20:23.768030-0500	coreaudiod	>>> NEGOTIATE [com.nexy.assistant]
default	19:20:23.768106-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetSupportedChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	19:20:23.768182-0500	coreaudiod	<<< NEGOTIATE [com.nexy.assistant]
default	19:20:23.771055-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOSupportedChatFlavors newValue: (
    0,
    2
)
default	19:20:23.771095-0500	coreaudiod	>>> ADAPT [com.nexy.assistant]
default	19:20:23.774025-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xa38710c00] Created node ADM::com.nexy.assistant_10285.10209.0_airpods noise suppression studio::in-0 with nodeID 0 - reporting period = 10.000000, sample rate = 24000.000000
default	19:20:23.774091-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xa38710c00] Created node ADM::com.nexy.assistant_10285.10209.0_airpods noise suppression studio::out-0 with nodeID 1 - reporting period = 10.000000, sample rate = 24000.000000
default	19:20:23.891798-0500	coreaudiod	<<< ADAPT [com.nexy.assistant]
default	19:20:23.894412-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:10285 called from <private>
default	19:20:23.894481-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Input {1C-77-54-18-C8-A3:input, 0xa}
default	19:20:23.895692-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:10285 called from <private>
default	19:20:23.896404-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(10285)
default	19:20:23.896424-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:10285 called from <private>
default	19:20:23.896430-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:10285 called from <private>
default	19:20:23.896550-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(10284)
default	19:20:23.897752-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:10284 called from <private>
default	19:20:23.897995-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:10284 called from <private>
default	19:20:23.900413-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.27212639.27212645(501)>:5671] from originator [osservice<com.apple.powerd>:338] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:403-338-153557 target:5671 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	19:20:23.900506-0500	runningboardd	Assertion 403-338-153557 (target:[app<application.com.nexy.assistant.27212639.27212645(501)>:5671]) will be created as active
default	19:20:23.901539-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645(501)>:5671] Ignoring jetsam update because this process is not memory-managed
default	19:20:23.901601-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645(501)>:5671] Ignoring suspend because this process is not lifecycle managed
default	19:20:23.901669-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645(501)>:5671] Ignoring GPU update because this process is not GPU managed
default	19:20:23.901803-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645(501)>:5671] Ignoring memory limit update because this process is not memory-managed
default	19:20:23.902478-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	19:20:23.903564-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
fault	19:20:23.903922-0500	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.27212639.27212645 AUID=501> and <type=Application identifier=application.com.nexy.assistant.27212639.27212645>
default	19:20:23.904285-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(10285)
default	19:20:23.904310-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(10285)
default	19:20:23.904320-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(10285)
default	19:20:23.904320-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:10285 called from <private>
default	19:20:23.904326-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(10285)
default	19:20:23.904330-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:10285 called from <private>
default	19:20:23.904334-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(10285)
default	19:20:23.904344-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:10285 called from <private>
default	19:20:23.904357-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(10285)
default	19:20:23.904388-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:10285 called from <private>
default	19:20:23.904455-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:10285 called from <private>
default	19:20:23.904509-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:10285 called from <private>
default	19:20:23.904541-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:10285 called from <private>
default	19:20:23.904575-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:10285 called from <private>
fault	19:20:23.908498-0500	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.27212639.27212645 AUID=501> and <type=Application identifier=application.com.nexy.assistant.27212639.27212645>
default	19:20:23.904613-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:10285 called from <private>
default	19:20:23.904640-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:10285 called from <private>
default	19:20:23.904684-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:10285 called from <private>
default	19:20:23.917612-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1e8047","name":"Nexy(5671)"}, "details":{"deviceUIDs":["1C-77-54-18-C8-A3:input"],"implicit_category":"Record","input_running":true,"output_running":false} }
default	19:20:23.917845-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 72, PID = 5671, Name = sid:0x1e8047, Nexy(5671), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	19:20:23.918401-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 72, PID = 5671, Name = sid:0x1e8047, Nexy(5671), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	19:20:23.918903-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 72, PID = 5671, Name = sid:0x1e8047, Nexy(5671), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	19:20:23.919070-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 72, PID = 5671, Name = sid:0x1e8047, Nexy(5671), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	19:20:23.918658-0500	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1e8047, Nexy(5671), 'prim'', AudioCategory changed to 'Record_WithBluetooth'
default	19:20:23.904752-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:10285 called from <private>
default	19:20:23.919262-0500	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 72, PID = 5671, Name = sid:0x1e8047, Nexy(5671), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> is going active
default	19:20:23.919318-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1e8047, Nexy(5671), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 72 starting recording
default	19:20:23.918685-0500	audiomxd	UpdateAudioState CID 0x4D120001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	19:20:23.906219-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:10285 called from <private>
default	19:20:23.906285-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:10285 called from <private>
default	19:20:23.920267-0500	audiomxd	UpdateAudioState CID 0x4D120001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	19:20:23.914729-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(10285)
default	19:20:23.915158-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:10285 called from <private>
default	19:20:23.920452-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 72, PID = 5671, Name = sid:0x1e8047, Nexy(5671), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	19:20:23.919578-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(10284)
default	19:20:23.920641-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 72, PID = 5671, Name = sid:0x1e8047, Nexy(5671), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	19:20:23.920600-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:10284 called from <private>
default	19:20:23.920788-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1e8047, Nexy(5671), 'prim'', displayID:'com.nexy.assistant'}
default	19:20:23.920640-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:10284 called from <private>
default	19:20:23.920970-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [1, 0]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:input"
)}
default	19:20:23.921087-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	19:20:23.920881-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=411.1483, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=5671, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=398, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	19:20:23.920177-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	19:20:23.921427-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	19:20:23.920712-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	19:20:23.925831-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.27212639.27212645(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	19:20:23.926469-0500	runningboardd	Invalidating assertion 403-338-153557 (target:[app<application.com.nexy.assistant.27212639.27212645(501)>:5671]) from originator [osservice<com.apple.powerd>:338]
default	19:20:23.927551-0500	gamepolicyd	Received state update for 5671 (app<application.com.nexy.assistant.27212639.27212645(501)>, running-active-NotVisible
default	19:20:23.927786-0500	tccd	AUTHREQ_SUBJECT: msgID=411.1483, subject=com.nexy.assistant,
default	19:20:23.929919-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc79245800 at /Applications/Nexy.app
default	19:20:23.933132-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:10284 called from <private>
default	19:20:23.933154-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:10284 called from <private>
default	19:20:23.933248-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(10284)
default	19:20:23.933866-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(10284)
default	19:20:23.934103-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:10284 called from <private>
default	19:20:23.934117-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:10284 called from <private>
default	19:20:23.934202-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(10284)
default	19:20:23.934777-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(10284)
default	19:20:23.935170-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:10284 called from <private>
default	19:20:23.935183-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:10284 called from <private>
default	19:20:23.937597-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:10284 called from <private>
default	19:20:23.937608-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:10284 called from <private>
default	19:20:23.937640-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:10284 called from <private>
default	19:20:23.937669-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:10284 called from <private>
default	19:20:23.937679-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:10284 called from <private>
default	19:20:23.937685-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:10284 called from <private>
default	19:20:23.937774-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(10284)
default	19:20:23.937784-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:10284 called from <private>
default	19:20:23.937884-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:10284 called from <private>
default	19:20:23.937927-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:10284 called from <private>
default	19:20:23.937975-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:10284 called from <private>
default	19:20:23.938030-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:10284 called from <private>
default	19:20:23.938055-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:10284 called from <private>
default	19:20:23.945210-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	19:20:23.948534-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	19:20:23.938144-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:10284 called from <private>
default	19:20:23.938210-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:10284 called from <private>
default	19:20:23.942226-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(10284)
default	19:20:23.942778-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:10284 called from <private>
default	19:20:23.942827-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:10284 called from <private>
error	19:20:23.966762-0500	audioaccessoryd	Updating local audio category 100 -> 200 app com.nexy.assistant
default	19:20:23.966892-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	19:20:23.968554-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	19:20:23.987678-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	19:20:23.988496-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.27212639.27212645(501)>:5671] from originator [osservice<com.apple.powerd>:338] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:403-338-153558 target:5671 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	19:20:23.988622-0500	runningboardd	Assertion 403-338-153558 (target:[app<application.com.nexy.assistant.27212639.27212645(501)>:5671]) will be created as active
default	19:20:23.996818-0500	tccd	AUTHREQ_SUBJECT: msgID=411.1484, subject=com.nexy.assistant,
default	19:20:23.997020-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	19:20:23.997030-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	19:20:23.997040-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	19:20:23.997049-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	19:20:23.997071-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	19:20:23.997087-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	19:20:23.997201-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	19:20:23.997311-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	19:20:23.997344-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	19:20:23.997359-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	19:20:23.997368-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	19:20:23.997392-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	19:20:23.997454-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	19:20:24.019459-0500	coreaudiod	>>> ADAPT [com.nexy.assistant]
default	19:20:24.022644-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xa380eaa00] Created node ADM::com.nexy.assistant_10285.10209.0_airpods noise suppression studio::in-0 with nodeID 0 - reporting period = 10.000000, sample rate = 24000.000000
default	19:20:24.022712-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xa380eaa00] Created node ADM::com.nexy.assistant_10285.10209.0_airpods noise suppression studio::out-0 with nodeID 1 - reporting period = 10.000000, sample rate = 24000.000000
default	19:20:24.033194-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645(501)>:5671] Ignoring jetsam update because this process is not memory-managed
default	19:20:24.033216-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645(501)>:5671] Ignoring suspend because this process is not lifecycle managed
default	19:20:24.033235-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645(501)>:5671] Ignoring GPU update because this process is not GPU managed
default	19:20:24.033267-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645(501)>:5671] Ignoring memory limit update because this process is not memory-managed
default	19:20:24.036334-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.27212639.27212645(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	19:20:24.036892-0500	gamepolicyd	Received state update for 5671 (app<application.com.nexy.assistant.27212639.27212645(501)>, running-active-NotVisible
default	19:20:24.061768-0500	coreaudiod	<<< ADAPT [com.nexy.assistant]
default	19:20:24.063952-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:10285 called from <private>
default	19:20:24.064006-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:10285 called from <private>
default	19:20:24.064201-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	19:20:24.067132-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:10285 called from <private>
default	19:20:24.067815-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.27212639.27212645(501)>:5671] from originator [osservice<com.apple.powerd>:338] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:403-338-153560 target:5671 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	19:20:24.068197-0500	runningboardd	Assertion 403-338-153560 (target:[app<application.com.nexy.assistant.27212639.27212645(501)>:5671]) will be created as active
default	19:20:24.067281-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(10285)
default	19:20:24.067298-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:10285 called from <private>
default	19:20:24.067306-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:10285 called from <private>
default	19:20:24.068754-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645(501)>:5671] Ignoring jetsam update because this process is not memory-managed
default	19:20:24.068856-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645(501)>:5671] Ignoring suspend because this process is not lifecycle managed
default	19:20:24.068967-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	19:20:24.068941-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645(501)>:5671] Ignoring GPU update because this process is not GPU managed
default	19:20:24.069123-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645(501)>:5671] Ignoring memory limit update because this process is not memory-managed
default	19:20:24.069557-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	19:20:24.070074-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(10285)
default	19:20:24.070398-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:10285 called from <private>
default	19:20:24.070408-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:10285 called from <private>
default	19:20:24.070420-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:10285 called from <private>
default	19:20:24.073681-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=411.1485, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=5671, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=398, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	19:20:24.075851-0500	tccd	AUTHREQ_SUBJECT: msgID=411.1485, subject=com.nexy.assistant,
default	19:20:24.076136-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.27212639.27212645(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	19:20:24.076567-0500	runningboardd	Invalidating assertion 403-338-153560 (target:[app<application.com.nexy.assistant.27212639.27212645(501)>:5671]) from originator [osservice<com.apple.powerd>:338]
default	19:20:24.077150-0500	gamepolicyd	Received state update for 5671 (app<application.com.nexy.assistant.27212639.27212645(501)>, running-active-NotVisible
default	19:20:24.077177-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	19:20:24.077194-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc79245800 at /Applications/Nexy.app
default	19:20:24.077234-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	19:20:24.077279-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	19:20:24.077503-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	19:20:24.077882-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	19:20:24.077908-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	19:20:24.077925-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	19:20:24.077934-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	19:20:24.077958-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	19:20:24.077982-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	19:20:24.078167-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	19:20:24.078183-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	19:20:24.078202-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	19:20:24.078216-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	19:20:24.078223-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	19:20:24.078264-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	19:20:24.078392-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	19:20:24.078826-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	19:20:24.100420-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:10285 called from <private>
default	19:20:24.102572-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.27212639.27212645(501)>:5671] from originator [osservice<com.apple.powerd>:338] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:403-338-153561 target:5671 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	19:20:24.102665-0500	runningboardd	Assertion 403-338-153561 (target:[app<application.com.nexy.assistant.27212639.27212645(501)>:5671]) will be created as active
default	19:20:24.108455-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	19:20:24.108494-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	19:20:24.108539-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	19:20:24.109230-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	19:20:24.109240-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	19:20:24.109251-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	19:20:24.109256-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	19:20:24.109263-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	19:20:24.109272-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	19:20:24.109299-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	19:20:24.109318-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	19:20:24.109347-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	19:20:24.109355-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	19:20:24.109364-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	19:20:24.109371-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	19:20:24.109525-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	19:20:24.110121-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	19:20:24.110152-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	19:20:24.110181-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	19:20:24.110205-0500	ControlCenter	Navigating to new application [com.nexy.assistant]
default	19:20:24.110191-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	19:20:24.110284-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	19:20:24.110340-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	19:20:24.185394-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.nexy.assistant, Score 200, Remote 0 NumofApp 1
default	19:20:24.732745-0500	spindump	Nexy [5671]: spin: not sampling due to conditions 0x400000000
default	19:20:25.127855-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xa}
default	19:20:25.128437-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1e8047","name":"Nexy(5671)"}, "details":{"deviceUIDs":[],"implicit_category":"","input_running":false,"output_running":false} }
default	19:20:25.128676-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 72, PID = 5671, Name = sid:0x1e8047, Nexy(5671), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	19:20:25.128808-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 72, PID = 5671, Name = sid:0x1e8047, Nexy(5671), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	19:20:25.128885-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1e8047, Nexy(5671), 'prim'', displayID:'com.nexy.assistant'}
default	19:20:25.128993-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	19:20:25.129009-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1e8047, Nexy(5671), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 72 stopping recording
default	19:20:25.129067-0500	audiomxd	-MXCoreSession- -[MXCoreSession endInterruption:]: Session <ID: 72, PID = 5671, Name = sid:0x1e8047, Nexy(5671), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> is going inactive
default	19:20:25.129133-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 72, PID = 5671, Name = sid:0x1e8047, Nexy(5671), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	19:20:25.129209-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 72, PID = 5671, Name = sid:0x1e8047, Nexy(5671), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	19:20:25.129530-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 200 flag 0x1 < Hijack > app com.nexy.assistant CID 0x4D120001 category Not set
default	19:20:25.129436-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 0]. BT device UIDS: {(
)}
default	19:20:25.129461-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	19:20:25.134851-0500	runningboardd	Invalidating assertion 403-338-153561 (target:[app<application.com.nexy.assistant.27212639.27212645(501)>:5671]) from originator [osservice<com.apple.powerd>:338]
default	19:20:25.135740-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	19:20:25.135826-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	19:20:25.135510-0500	audiomxd	UpdateAudioState CID 0x4D120001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	19:20:25.135859-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	19:20:25.135629-0500	audiomxd	UpdateAudioState CID 0x4D120001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	19:20:25.135920-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	19:20:25.136008-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	19:20:25.136023-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	19:20:25.136091-0500	audioaccessoryd	AudioStateChanged: Removed audio session app com.nexy.assistant 201 count 0
default	19:20:25.136774-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	19:20:25.141340-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	19:20:25.141360-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	19:20:25.141381-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	19:20:25.141391-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	19:20:25.141403-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	19:20:25.141415-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	19:20:25.141561-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	19:20:25.229353-0500	Nexy	                AUHAL.cpp:473   ~AUHAL: (0xa69a48740) Selecting device 0 from destructor
default	19:20:25.229377-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0xa69a48740)
default	19:20:25.229387-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0xa69a48740) not already running
default	19:20:25.229393-0500	Nexy	                AUHAL.cpp:687   SelectDevice: (0xa69a48740) disconnecting device 91
default	19:20:25.229402-0500	Nexy	                AUHAL.cpp:751   SelectDevice: (0xa69a48740) destroying ioproc 0xa for device 91
default	19:20:25.229444-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xa}
default	19:20:25.229489-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	19:20:25.229691-0500	Nexy	                AUHAL.cpp:853   SelectDevice: (0xa69a48740) nothing to setup
default	19:20:25.229707-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0xa69a48740) adding 0 device listeners to device 0
default	19:20:25.229713-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0xa69a48740) adding 0 device delegate listeners to device 0
default	19:20:25.229722-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0xa69a48740) removing 7 device listeners from device 91
default	19:20:25.229983-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0xa69a48740) removing 0 device delegate listeners from device 91
default	19:20:25.230003-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0xa69a48740)
default	19:20:25.241688-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645(501)>:5671] Ignoring jetsam update because this process is not memory-managed
default	19:20:25.241707-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645(501)>:5671] Ignoring suspend because this process is not lifecycle managed
default	19:20:25.241722-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645(501)>:5671] Ignoring GPU update because this process is not GPU managed
default	19:20:25.241748-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645(501)>:5671] Ignoring memory limit update because this process is not memory-managed
default	19:20:25.245500-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.27212639.27212645(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	19:20:25.246356-0500	gamepolicyd	Received state update for 5671 (app<application.com.nexy.assistant.27212639.27212645(501)>, running-active-NotVisible
default	19:20:25.421704-0500	Nexy	[0xa69c25400] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	19:20:25.422410-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=5671.3, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=5671, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	19:20:25.423583-0500	tccd	AUTHREQ_SUBJECT: msgID=5671.3, subject=com.nexy.assistant,
default	19:20:25.424253-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x92f179b00 at /Applications/Nexy.app
default	19:20:25.438050-0500	Nexy	[0xa69c25400] invalidated after the last release of the connection object
default	19:20:25.439650-0500	Nexy	[0xa69c25400] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	19:20:25.440205-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=5671.4, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=5671, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	19:20:25.441165-0500	tccd	AUTHREQ_SUBJECT: msgID=5671.4, subject=com.nexy.assistant,
default	19:20:25.441888-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x92f179b00 at /Applications/Nexy.app
default	19:20:25.455404-0500	tccd	Notifying for access  kTCCServiceListenEvent for target PID[5671], responsiblePID[5671], responsiblePath: /Applications/Nexy.app to UID: 501
default	19:20:25.455646-0500	Nexy	[0xa69c25400] invalidated after the last release of the connection object
default	19:20:25.552303-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x92f179200 at /Applications/Nexy.app
default	19:20:25.579936-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x92f17a400 at /Applications/Nexy.app
default	19:20:25.586859-0500	tccd	Publishing <TCCDEvent: type=Modify, service=kTCCServiceListenEvent, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 0 subscribers: {
}
default	19:20:27.361541-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(10284)
default	19:20:27.361571-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:10284 called from <private>
default	19:20:27.361578-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:10284 called from <private>
default	19:20:27.362368-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(10285)
default	19:20:27.362387-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:10285 called from <private>
default	19:20:27.362396-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:10285 called from <private>
default	19:20:27.379035-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:10284 called from <private>
default	19:20:27.379095-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:10284 called from <private>
default	19:20:27.394432-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:10284 called from <private>
default	19:20:27.394452-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:10284 called from <private>
default	19:20:27.394546-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(10284)
default	19:20:27.405162-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:10284 called from <private>
default	19:20:28.744162-0500	Nexy	NotifyToken::RegisterDispatch(user.uid.501.com.apple.LaunchServices.database) fired for session key <private>
error	19:20:28.905766-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CAIIugCI3D6x0jkL7BXjcYRl0vPhkk-L5K9mxvc/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:194 loadAuthorizationStates(for:) new entry: kTCCServiceListenEvent com.nexy.assistant none
error	19:20:28.959564-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CAIIugCI3D6x0jkL7BXjcYRl0vPhkk-L5K9mxvc/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:194 loadAuthorizationStates(for:) new entry: kTCCServiceAppleEvents com.nexy.assistant full
error	19:20:28.960026-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CAIIugCI3D6x0jkL7BXjcYRl0vPhkk-L5K9mxvc/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:194 loadAuthorizationStates(for:) new entry: kTCCServiceAppleEvents com.nexy.assistant full
error	19:20:28.961791-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CAIIugCI3D6x0jkL7BXjcYRl0vPhkk-L5K9mxvc/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:194 loadAuthorizationStates(for:) new entry: kTCCServiceMicrophone com.nexy.assistant full
error	19:20:28.962025-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CAIIugCI3D6x0jkL7BXjcYRl0vPhkk-L5K9mxvc/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:194 loadAuthorizationStates(for:) new entry: kTCCServiceMicrophone com.nexy.assistant full
default	19:20:30.104553-0500	Nexy	LSExceptions shared instance invalidated for timeout.
default	19:20:33.416184-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x92f179200 at /Applications/Nexy.app
default	19:20:33.437241-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x92f17a700 at /Applications/Nexy.app
default	19:20:33.447380-0500	tccd	Publishing <TCCDEvent: type=Modify, service=kTCCServiceListenEvent, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 0 subscribers: {
}
error	19:20:33.584103-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CAIIugCI3D6x0jkL7BXjcYRl0vPhkk-L5K9mxvc/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:194 loadAuthorizationStates(for:) new entry: kTCCServiceListenEvent com.nexy.assistant full
error	19:20:33.587893-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CAIIugCI3D6x0jkL7BXjcYRl0vPhkk-L5K9mxvc/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:194 loadAuthorizationStates(for:) new entry: kTCCServiceListenEvent com.nexy.assistant full
error	19:20:33.607201-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CAIIugCI3D6x0jkL7BXjcYRl0vPhkk-L5K9mxvc/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:194 loadAuthorizationStates(for:) new entry: kTCCServiceAppleEvents com.nexy.assistant full
error	19:20:33.607647-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CAIIugCI3D6x0jkL7BXjcYRl0vPhkk-L5K9mxvc/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:194 loadAuthorizationStates(for:) new entry: kTCCServiceMicrophone com.nexy.assistant full
error	19:20:33.609114-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CAIIugCI3D6x0jkL7BXjcYRl0vPhkk-L5K9mxvc/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:194 loadAuthorizationStates(for:) new entry: kTCCServiceAppleEvents com.nexy.assistant full
error	19:20:33.609514-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CAIIugCI3D6x0jkL7BXjcYRl0vPhkk-L5K9mxvc/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:194 loadAuthorizationStates(for:) new entry: kTCCServiceMicrophone com.nexy.assistant full
default	19:20:38.463560-0500	Nexy	                AUHAL.cpp:420   AUHAL: (0xa69a48e40) Selecting device 85 from constructor
default	19:20:38.463581-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0xa69a48e40)
default	19:20:38.463587-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0xa69a48e40) not already running
default	19:20:38.463593-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0xa69a48e40) nothing to teardown
default	19:20:38.463597-0500	Nexy	                AUHAL.cpp:762   SelectDevice: (0xa69a48e40) connecting device 85
default	19:20:38.463716-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0xa69a48e40) Device ID: 85 (Input:No | Output:Yes): true
default	19:20:38.463923-0500	Nexy	                AUHAL.cpp:774   SelectDevice: (0xa69a48e40) created ioproc 0xb for device 85
default	19:20:38.464035-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0xa69a48e40) adding 7 device listeners to device 85
default	19:20:38.464210-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0xa69a48e40) adding 0 device delegate listeners to device 85
default	19:20:38.464220-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0xa69a48e40)
default	19:20:38.464293-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  48000 Hz, Float32, interleaved
default	19:20:38.464303-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	19:20:38.464308-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	19:20:38.464322-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	19:20:38.464334-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	19:20:38.464441-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0xa69a48e40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	19:20:38.464451-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0xa69a48e40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	19:20:38.464456-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	19:20:38.464459-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0xa69a48e40) removing 0 device listeners from device 0
default	19:20:38.464464-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0xa69a48e40) removing 0 device delegate listeners from device 0
default	19:20:38.464471-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0xa69a48e40)
default	19:20:38.464488-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is DISABLED
default	19:20:38.464587-0500	Nexy	                AUHAL.cpp:2303  SetProperty: (0xa69a48e40) caller requesting device change from 85 to 91
default	19:20:38.464598-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0xa69a48e40)
default	19:20:38.464603-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0xa69a48e40) not already running
default	19:20:38.464607-0500	Nexy	                AUHAL.cpp:687   SelectDevice: (0xa69a48e40) disconnecting device 85
default	19:20:38.464612-0500	Nexy	                AUHAL.cpp:751   SelectDevice: (0xa69a48e40) destroying ioproc 0xb for device 85
default	19:20:38.464673-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped Unknown {1C-77-54-18-C8-A3:output, 0xb}
default	19:20:38.464720-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	19:20:38.464792-0500	Nexy	                AUHAL.cpp:762   SelectDevice: (0xa69a48e40) connecting device 91
default	19:20:38.464875-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0xa69a48e40) Device ID: 91 (Input:Yes | Output:No): true
default	19:20:38.466723-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=411.1486, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=5671, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=398, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	19:20:38.468314-0500	tccd	AUTHREQ_SUBJECT: msgID=411.1486, subject=com.nexy.assistant,
default	19:20:38.469166-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc79244300 at /Applications/Nexy.app
default	19:20:38.492630-0500	Nexy	                AUHAL.cpp:774   SelectDevice: (0xa69a48e40) created ioproc 0xb for device 91
default	19:20:38.492826-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0xa69a48e40) adding 7 device listeners to device 91
default	19:20:38.493029-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0xa69a48e40) adding 0 device delegate listeners to device 91
default	19:20:38.493043-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0xa69a48e40)
default	19:20:38.493056-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 output streams; not all mono
default	19:20:38.493068-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	19:20:38.493218-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  input stream 0 [0x5c]:  1 ch,  24000 Hz, Float32
default	19:20:38.493227-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 input streams; all mono
default	19:20:38.493231-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  1 ch,  24000 Hz, Float32
default	19:20:38.493341-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0xa69a48e40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	19:20:38.493362-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0xa69a48e40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	19:20:38.493369-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	19:20:38.493372-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0xa69a48e40) removing 7 device listeners from device 85
default	19:20:38.493532-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0xa69a48e40) removing 0 device delegate listeners from device 85
default	19:20:38.493542-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0xa69a48e40)
default	19:20:38.494221-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	19:20:38.495412-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=411.1487, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=5671, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=398, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	19:20:38.496545-0500	tccd	AUTHREQ_SUBJECT: msgID=411.1487, subject=com.nexy.assistant,
default	19:20:38.497195-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc79244300 at /Applications/Nexy.app
default	19:20:38.515149-0500	Nexy	       ACv2Workarounds.mm:51    com.nexy.assistant: fix84702776_86723525_86479548_89800354_SinglePacketDesc: false
default	19:20:38.515429-0500	Nexy	       AudioConverter.cpp:1044  Created a new in process converter -> 0xa68865380, from  1 ch,  24000 Hz, Float32 to  1 ch,  16000 Hz, Float32
default	19:20:38.515652-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	19:20:38.516675-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=411.1488, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=5671, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=398, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	19:20:38.517595-0500	tccd	AUTHREQ_SUBJECT: msgID=411.1488, subject=com.nexy.assistant,
default	19:20:38.518192-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc79244300 at /Applications/Nexy.app
default	19:20:38.536638-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=411.1489, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=5671, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=398, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	19:20:38.537545-0500	tccd	AUTHREQ_SUBJECT: msgID=411.1489, subject=com.nexy.assistant,
default	19:20:38.538173-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc79244300 at /Applications/Nexy.app
default	19:20:38.555759-0500	coreaudiod	>>> NEGOTIATE [com.nexy.assistant]
default	19:20:38.555975-0500	coreaudiod	<<< NEGOTIATE [com.nexy.assistant]
default	19:20:38.557996-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:10285 called from <private>
default	19:20:38.558052-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Input {1C-77-54-18-C8-A3:input, 0xb}
default	19:20:38.558090-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	19:20:38.558948-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:10285 called from <private>
default	19:20:38.564618-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.27212639.27212645(501)>:5671] from originator [osservice<com.apple.powerd>:338] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:403-338-153674 target:5671 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	19:20:38.564790-0500	runningboardd	Assertion 403-338-153674 (target:[app<application.com.nexy.assistant.27212639.27212645(501)>:5671]) will be created as active
default	19:20:38.559144-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(10285)
default	19:20:38.565351-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645(501)>:5671] Ignoring jetsam update because this process is not memory-managed
default	19:20:38.565408-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645(501)>:5671] Ignoring suspend because this process is not lifecycle managed
default	19:20:38.565537-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645(501)>:5671] Ignoring GPU update because this process is not GPU managed
default	19:20:38.565728-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645(501)>:5671] Ignoring memory limit update because this process is not memory-managed
default	19:20:38.559170-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:10285 called from <private>
default	19:20:38.559176-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:10285 called from <private>
default	19:20:38.559268-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(10284)
default	19:20:38.559854-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:10284 called from <private>
default	19:20:38.560370-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:10284 called from <private>
default	19:20:38.569096-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	19:20:38.569545-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	19:20:38.570348-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(10285)
default	19:20:38.570399-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(10285)
default	19:20:38.570415-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(10285)
default	19:20:38.570430-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(10285)
default	19:20:38.573867-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.27212639.27212645(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	19:20:38.574320-0500	runningboardd	Invalidating assertion 403-338-153674 (target:[app<application.com.nexy.assistant.27212639.27212645(501)>:5671]) from originator [osservice<com.apple.powerd>:338]
default	19:20:38.574728-0500	gamepolicyd	Received state update for 5671 (app<application.com.nexy.assistant.27212639.27212645(501)>, running-active-NotVisible
default	19:20:38.579992-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	19:20:38.580146-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	19:20:38.580209-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	19:20:38.580444-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(10285)
default	19:20:38.580692-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:10285 called from <private>
default	19:20:38.580701-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:10285 called from <private>
default	19:20:38.580714-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:10285 called from <private>
default	19:20:38.580724-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:10285 called from <private>
default	19:20:38.580730-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:10285 called from <private>
default	19:20:38.581549-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1e8047","name":"Nexy(5671)"}, "details":{"deviceUIDs":["1C-77-54-18-C8-A3:input"],"implicit_category":"Record","input_running":true,"output_running":false} }
default	19:20:38.581691-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 72, PID = 5671, Name = sid:0x1e8047, Nexy(5671), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	19:20:38.581800-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Category/Mode changed -- The score for sid:0x1e8047, Nexy(5671), 'prim'/com.nexy.assistant was not correct. Old score = 201
default	19:20:38.582555-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 72, PID = 5671, Name = sid:0x1e8047, Nexy(5671), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	19:20:38.582967-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 72, PID = 5671, Name = sid:0x1e8047, Nexy(5671), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	19:20:38.583087-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 72, PID = 5671, Name = sid:0x1e8047, Nexy(5671), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	19:20:38.583275-0500	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 72, PID = 5671, Name = sid:0x1e8047, Nexy(5671), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> is going active
default	19:20:38.583314-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1e8047, Nexy(5671), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 72 starting recording
default	19:20:38.583265-0500	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1e8047, Nexy(5671), 'prim'', AudioCategory changed to 'Record_WithBluetooth'
default	19:20:38.583584-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 72, PID = 5671, Name = sid:0x1e8047, Nexy(5671), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	19:20:38.580735-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:10285 called from <private>
default	19:20:38.580769-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:10285 called from <private>
default	19:20:38.580811-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:10285 called from <private>
default	19:20:38.580852-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:10285 called from <private>
default	19:20:38.580909-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:10285 called from <private>
default	19:20:38.580945-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:10285 called from <private>
default	19:20:38.584183-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	19:20:38.583663-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 72, PID = 5671, Name = sid:0x1e8047, Nexy(5671), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	19:20:38.584199-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	19:20:38.584244-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	19:20:38.584254-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	19:20:38.583765-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1e8047, Nexy(5671), 'prim'', displayID:'com.nexy.assistant'}
default	19:20:38.583487-0500	audiomxd	UpdateAudioState CID 0x4D120001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	19:20:38.584350-0500	audiomxd	UpdateAudioState CID 0x4D120001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	19:20:38.584341-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	19:20:38.584351-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	19:20:38.586050-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	19:20:38.586077-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	19:20:38.586199-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	19:20:38.586214-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	19:20:38.586225-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	19:20:38.586427-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	19:20:38.586800-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	19:20:38.586843-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	19:20:38.586802-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	19:20:38.586888-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	19:20:38.586921-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	19:20:38.586960-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	19:20:38.586971-0500	ControlCenter	Navigating to new application [com.nexy.assistant]
default	19:20:38.586985-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	19:20:38.581280-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(10284)
default	19:20:38.586113-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	19:20:38.583965-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [1, 0]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:input"
)}
default	19:20:38.584501-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	19:20:38.584086-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	19:20:38.585551-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=411.1490, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=5671, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=398, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	19:20:38.586121-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	19:20:38.589406-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	19:20:38.589900-0500	tccd	AUTHREQ_SUBJECT: msgID=411.1490, subject=com.nexy.assistant,
default	19:20:38.591306-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc79244300 at /Applications/Nexy.app
default	19:20:38.595861-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:10284 called from <private>
default	19:20:38.595881-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:10284 called from <private>
default	19:20:38.595997-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(10284)
default	19:20:38.606276-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(10284)
default	19:20:38.606638-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:10284 called from <private>
default	19:20:38.606667-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:10284 called from <private>
default	19:20:38.606760-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:10284 called from <private>
default	19:20:38.606769-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:10284 called from <private>
default	19:20:38.606775-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:10284 called from <private>
default	19:20:38.606781-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:10284 called from <private>
default	19:20:38.606952-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:10284 called from <private>
default	19:20:38.607069-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:10284 called from <private>
default	19:20:38.607244-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:10284 called from <private>
default	19:20:38.607312-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:10284 called from <private>
default	19:20:38.607453-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(10284)
default	19:20:38.607597-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:10284 called from <private>
default	19:20:38.607681-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:10284 called from <private>
default	19:20:38.611435-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(10284)
default	19:20:38.611762-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:10284 called from <private>
default	19:20:38.611926-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:10284 called from <private>
default	19:20:38.612071-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:10284 called from <private>
default	19:20:38.612206-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:10284 called from <private>
default	19:20:38.612379-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:10284 called from <private>
default	19:20:38.612510-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:10284 called from <private>
default	19:20:38.612771-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(10284)
default	19:20:38.612871-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:10284 called from <private>
default	19:20:38.646478-0500	tccd	AUTHREQ_SUBJECT: msgID=411.1491, subject=com.nexy.assistant,
default	19:20:38.647494-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc79244300 at /Applications/Nexy.app
default	19:20:38.668464-0500	coreaudiod	>>> ADAPT [com.nexy.assistant]
default	19:20:38.669363-0500	coreaudiod	IssueReporting.cpp:492   RTAID [ use_case=Generic report_type=RMS Generic Chain clientID=ADM node=ADM::com.nexy.assistant_10285.10209.0_airpods noise suppression studio::out-0 issue_detected_sample_time=24480.000000 ] -- [ rms:[-43.320686], peaks:[-25.028837] ]
default	19:20:38.669379-0500	coreaudiod	IssueReporting.cpp:492   RTAID [ use_case=Generic report_type=RMS Generic Chain clientID=ADM node=ADM::com.nexy.assistant_10285.10209.0_airpods noise suppression studio::in-0 issue_detected_sample_time=0.000000 ] -- [ rms:[-39.416035], peaks:[-24.116089] ]
default	19:20:38.669631-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xa380eaa00] Created node ADM::com.nexy.assistant_10285.10209.0_airpods noise suppression studio::in-0 with nodeID 0 - reporting period = 10.000000, sample rate = 24000.000000
default	19:20:38.669688-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xa380eaa00] Created node ADM::com.nexy.assistant_10285.10209.0_airpods noise suppression studio::out-0 with nodeID 1 - reporting period = 10.000000, sample rate = 24000.000000
default	19:20:38.680915-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645(501)>:5671] Ignoring jetsam update because this process is not memory-managed
default	19:20:38.680932-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645(501)>:5671] Ignoring suspend because this process is not lifecycle managed
default	19:20:38.680946-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645(501)>:5671] Ignoring GPU update because this process is not GPU managed
default	19:20:38.680973-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645(501)>:5671] Ignoring memory limit update because this process is not memory-managed
default	19:20:38.684218-0500	gamepolicyd	Received state update for 5671 (app<application.com.nexy.assistant.27212639.27212645(501)>, running-active-NotVisible
default	19:20:38.704749-0500	coreaudiod	<<< ADAPT [com.nexy.assistant]
default	19:20:38.706767-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:10285 called from <private>
default	19:20:38.706100-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.27212639.27212645(501)>:5671] from originator [osservice<com.apple.powerd>:338] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:403-338-153677 target:5671 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	19:20:38.708213-0500	runningboardd	Assertion 403-338-153677 (target:[app<application.com.nexy.assistant.27212639.27212645(501)>:5671]) will be created as active
default	19:20:38.708693-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645(501)>:5671] Ignoring jetsam update because this process is not memory-managed
default	19:20:38.708754-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645(501)>:5671] Ignoring suspend because this process is not lifecycle managed
default	19:20:38.709310-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645(501)>:5671] Ignoring GPU update because this process is not GPU managed
default	19:20:38.709412-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645(501)>:5671] Ignoring memory limit update because this process is not memory-managed
default	19:20:38.706789-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:10285 called from <private>
default	19:20:38.707076-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	19:20:38.709305-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:10285 called from <private>
default	19:20:38.709424-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(10285)
default	19:20:38.710280-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	19:20:38.709439-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:10285 called from <private>
default	19:20:38.709446-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:10285 called from <private>
default	19:20:38.710866-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	19:20:38.711458-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(10285)
default	19:20:38.711700-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:10285 called from <private>
default	19:20:38.711711-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:10285 called from <private>
default	19:20:38.711730-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:10285 called from <private>
default	19:20:38.713316-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=411.1492, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=5671, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=398, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	19:20:38.715886-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.27212639.27212645(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	19:20:38.716326-0500	gamepolicyd	Received state update for 5671 (app<application.com.nexy.assistant.27212639.27212645(501)>, running-active-NotVisible
default	19:20:38.716250-0500	runningboardd	Invalidating assertion 403-338-153677 (target:[app<application.com.nexy.assistant.27212639.27212645(501)>:5671]) from originator [osservice<com.apple.powerd>:338]
default	19:20:38.716840-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	19:20:38.716895-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	19:20:38.716932-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	19:20:38.717058-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	19:20:38.717384-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	19:20:38.717394-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	19:20:38.717403-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	19:20:38.717411-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	19:20:38.717432-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	19:20:38.717467-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	19:20:38.717772-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	19:20:38.736188-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:10285 called from <private>
default	19:20:38.737951-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.27212639.27212645(501)>:5671] from originator [osservice<com.apple.powerd>:338] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:403-338-153678 target:5671 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	19:20:38.738013-0500	runningboardd	Assertion 403-338-153678 (target:[app<application.com.nexy.assistant.27212639.27212645(501)>:5671]) will be created as active
default	19:20:38.743199-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	19:20:38.743241-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	19:20:38.743273-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	19:20:38.743611-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	19:20:38.743621-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	19:20:38.743630-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	19:20:38.743642-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	19:20:38.743652-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	19:20:38.743657-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	19:20:38.743671-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	19:20:38.743681-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	19:20:38.743709-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	19:20:38.743716-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	19:20:38.743725-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	19:20:38.743731-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	19:20:38.743832-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	19:20:38.744067-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	19:20:38.744076-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	19:20:38.744083-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	19:20:38.744091-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	19:20:38.744129-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	19:20:38.744133-0500	ControlCenter	Navigating to new application [com.nexy.assistant]
default	19:20:38.744138-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	19:20:39.107228-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.nexy.assistant, Score 200, Remote 0 NumofApp 1
default	19:20:42.185300-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.nexy.assistant, Score 200, Remote 0 NumofApp 1
default	19:20:45.185223-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.nexy.assistant, Score 200, Remote 0 NumofApp 1
default	19:20:48.118741-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.nexy.assistant, Score 200, Remote 0 NumofApp 1
default	19:20:48.736707-0500	coreaudiod	IssueReporting.cpp:492   RTAID [ use_case=Generic report_type=RMS Generic Chain clientID=ADM node=ADM::com.nexy.assistant_10285.10209.0_airpods noise suppression studio::in-0 issue_detected_sample_time=0.000000 ] -- [ rms:[-38.031162], peaks:[-14.589982] ]
default	19:20:48.739228-0500	coreaudiod	IssueReporting.cpp:492   RTAID [ use_case=Generic report_type=RMS Generic Chain clientID=ADM node=ADM::com.nexy.assistant_10285.10209.0_airpods noise suppression studio::out-0 issue_detected_sample_time=240000.000000 ] -- [ rms:[-39.187340], peaks:[-6.994715] ]
default	19:20:51.181663-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.nexy.assistant, Score 200, Remote 0 NumofApp 1
default	19:20:51.608244-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xb}
default	19:20:51.608623-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1e8047","name":"Nexy(5671)"}, "details":{"deviceUIDs":[],"implicit_category":"","input_running":false,"output_running":false} }
default	19:20:51.608813-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 72, PID = 5671, Name = sid:0x1e8047, Nexy(5671), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	19:20:51.609035-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 72, PID = 5671, Name = sid:0x1e8047, Nexy(5671), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	19:20:51.609074-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1e8047, Nexy(5671), 'prim'', displayID:'com.nexy.assistant'}
default	19:20:51.609149-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	19:20:51.609168-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1e8047, Nexy(5671), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 72 stopping recording
default	19:20:51.609216-0500	audiomxd	-MXCoreSession- -[MXCoreSession endInterruption:]: Session <ID: 72, PID = 5671, Name = sid:0x1e8047, Nexy(5671), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> is going inactive
default	19:20:51.609252-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 72, PID = 5671, Name = sid:0x1e8047, Nexy(5671), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	19:20:51.609296-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 72, PID = 5671, Name = sid:0x1e8047, Nexy(5671), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	19:20:51.609405-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 200 flag 0x1 < Hijack > app com.nexy.assistant CID 0x4D120001 category Not set
default	19:20:51.609409-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 0]. BT device UIDS: {(
)}
default	19:20:51.609424-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	19:20:51.612623-0500	runningboardd	Invalidating assertion 403-338-153678 (target:[app<application.com.nexy.assistant.27212639.27212645(501)>:5671]) from originator [osservice<com.apple.powerd>:338]
default	19:20:51.613998-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	19:20:51.614028-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	19:20:51.614044-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	19:20:51.614064-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	19:20:51.614311-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	19:20:51.614373-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	19:20:51.613893-0500	audiomxd	UpdateAudioState CID 0x4D120001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	19:20:51.614432-0500	audioaccessoryd	AudioStateChanged: Removed audio session app com.nexy.assistant 201 count 0
default	19:20:51.613950-0500	audiomxd	UpdateAudioState CID 0x4D120001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	19:20:51.614592-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	19:20:51.616565-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	19:20:51.616575-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	19:20:51.616588-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	19:20:51.616594-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	19:20:51.616600-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	19:20:51.616605-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	19:20:51.616673-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	19:20:51.710120-0500	Nexy	                AUHAL.cpp:473   ~AUHAL: (0xa69a48e40) Selecting device 0 from destructor
default	19:20:51.710139-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0xa69a48e40)
default	19:20:51.710149-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0xa69a48e40) not already running
default	19:20:51.710155-0500	Nexy	                AUHAL.cpp:687   SelectDevice: (0xa69a48e40) disconnecting device 91
default	19:20:51.710161-0500	Nexy	                AUHAL.cpp:751   SelectDevice: (0xa69a48e40) destroying ioproc 0xb for device 91
default	19:20:51.710202-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xb}
default	19:20:51.710247-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	19:20:51.710450-0500	Nexy	                AUHAL.cpp:853   SelectDevice: (0xa69a48e40) nothing to setup
default	19:20:51.710465-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0xa69a48e40) adding 0 device listeners to device 0
default	19:20:51.710474-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0xa69a48e40) adding 0 device delegate listeners to device 0
default	19:20:51.710481-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0xa69a48e40) removing 7 device listeners from device 91
default	19:20:51.710866-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0xa69a48e40) removing 0 device delegate listeners from device 91
default	19:20:51.710895-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0xa69a48e40)
default	19:20:51.713217-0500	Nexy	[0xa69c25540] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	19:20:51.714565-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=5671.5, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=5671, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	19:20:51.716384-0500	tccd	AUTHREQ_SUBJECT: msgID=5671.5, subject=com.nexy.assistant,
default	19:20:51.717444-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x92f17bc00 at /Applications/Nexy.app
default	19:20:51.718765-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645(501)>:5671] Ignoring jetsam update because this process is not memory-managed
default	19:20:51.718780-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645(501)>:5671] Ignoring suspend because this process is not lifecycle managed
default	19:20:51.718790-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645(501)>:5671] Ignoring GPU update because this process is not GPU managed
default	19:20:51.718806-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645(501)>:5671] Ignoring memory limit update because this process is not memory-managed
default	19:20:51.722544-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.27212639.27212645(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	19:20:51.723773-0500	gamepolicyd	Received state update for 5671 (app<application.com.nexy.assistant.27212639.27212645(501)>, running-active-NotVisible
default	19:20:51.739957-0500	tccd	Notifying for access  kTCCServiceScreenCapture for target PID[5671], responsiblePID[5671], responsiblePath: /Applications/Nexy.app to UID: 501
default	19:20:51.740402-0500	Nexy	[0xa69c25540] invalidated after the last release of the connection object
default	19:20:51.788031-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x92f179200 at /Applications/Nexy.app
default	19:20:51.808967-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x92f179800 at /Applications/Nexy.app
default	19:20:51.813410-0500	tccd	Publishing <TCCDEvent: type=Modify, service=kTCCServiceScreenCapture, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 0 subscribers: {
}
error	19:20:51.869529-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CAIIugCI3D6x0jkL7BXjcYRl0vPhkk-L5K9mxvc/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:194 loadAuthorizationStates(for:) new entry: kTCCServiceListenEvent com.nexy.assistant full
error	19:20:51.869654-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CAIIugCI3D6x0jkL7BXjcYRl0vPhkk-L5K9mxvc/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:194 loadAuthorizationStates(for:) new entry: kTCCServiceScreenCapture com.nexy.assistant none
error	19:20:51.872227-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CAIIugCI3D6x0jkL7BXjcYRl0vPhkk-L5K9mxvc/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:194 loadAuthorizationStates(for:) new entry: kTCCServiceListenEvent com.nexy.assistant full
error	19:20:51.872344-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CAIIugCI3D6x0jkL7BXjcYRl0vPhkk-L5K9mxvc/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:194 loadAuthorizationStates(for:) new entry: kTCCServiceScreenCapture com.nexy.assistant none
error	19:20:51.885040-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CAIIugCI3D6x0jkL7BXjcYRl0vPhkk-L5K9mxvc/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:194 loadAuthorizationStates(for:) new entry: kTCCServiceAppleEvents com.nexy.assistant full
error	19:20:51.885447-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CAIIugCI3D6x0jkL7BXjcYRl0vPhkk-L5K9mxvc/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:194 loadAuthorizationStates(for:) new entry: kTCCServiceMicrophone com.nexy.assistant full
error	19:20:51.886780-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CAIIugCI3D6x0jkL7BXjcYRl0vPhkk-L5K9mxvc/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:194 loadAuthorizationStates(for:) new entry: kTCCServiceAppleEvents com.nexy.assistant full
error	19:20:51.887164-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CAIIugCI3D6x0jkL7BXjcYRl0vPhkk-L5K9mxvc/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:194 loadAuthorizationStates(for:) new entry: kTCCServiceMicrophone com.nexy.assistant full
default	19:20:53.835973-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(10284)
default	19:20:53.836031-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:10284 called from <private>
default	19:20:53.836049-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:10284 called from <private>
default	19:20:53.838224-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(10285)
default	19:20:53.838279-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:10285 called from <private>
default	19:20:53.838296-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:10285 called from <private>
default	19:20:53.844816-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:10284 called from <private>
default	19:20:53.844852-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:10284 called from <private>
default	19:20:53.844996-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(10284)
default	19:20:53.845021-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:10284 called from <private>
default	19:20:53.845029-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:10284 called from <private>
default	19:20:53.848433-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(10284)
default	19:20:53.848778-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(10284)
default	19:20:53.851381-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(10284)
default	19:20:53.851386-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:10284 called from <private>
default	19:20:53.851413-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:10284 called from <private>
default	19:20:53.851428-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:10284 called from <private>
default	19:20:53.851438-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:10284 called from <private>
default	19:20:53.851449-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:10284 called from <private>
default	19:20:53.851454-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:10284 called from <private>
default	19:20:53.851502-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:10284 called from <private>
default	19:20:53.851583-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:10284 called from <private>
default	19:20:53.855575-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(10285)
default	19:20:53.855612-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:10285 called from <private>
default	19:20:53.855628-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:10285 called from <private>
default	19:20:53.860487-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(10284)
default	19:20:53.861032-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:10284 called from <private>
default	19:20:53.861049-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:10284 called from <private>
default	19:20:53.874934-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:10284 called from <private>
default	19:20:53.874958-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:10284 called from <private>
default	19:20:53.875103-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(10284)
default	19:20:53.878906-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(10284)
default	19:20:53.879364-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:10284 called from <private>
default	19:20:53.879376-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:10284 called from <private>
default	19:20:53.879529-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(10284)
default	19:20:53.883270-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(10284)
default	19:20:53.883604-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:10284 called from <private>
default	19:20:53.883615-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:10284 called from <private>
default	19:20:53.883663-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:10284 called from <private>
default	19:20:53.883672-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:10284 called from <private>
default	19:20:53.883683-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:10284 called from <private>
default	19:20:53.883692-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:10284 called from <private>
default	19:20:53.883780-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:10284 called from <private>
default	19:20:53.883900-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:10284 called from <private>
default	19:20:53.884087-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:10284 called from <private>
default	19:20:53.884206-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:10284 called from <private>
default	19:20:53.884438-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:10284 called from <private>
default	19:20:53.884665-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:10284 called from <private>
default	19:20:54.913094-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x92f179200 at /Applications/Nexy.app
default	19:20:54.935929-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x92f17b300 at /Applications/Nexy.app
default	19:20:54.945223-0500	tccd	Publishing <TCCDEvent: type=Modify, service=kTCCServiceScreenCapture, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 0 subscribers: {
}
error	19:20:55.069751-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CAIIugCI3D6x0jkL7BXjcYRl0vPhkk-L5K9mxvc/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:194 loadAuthorizationStates(for:) new entry: kTCCServiceListenEvent com.nexy.assistant full
error	19:20:55.069890-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CAIIugCI3D6x0jkL7BXjcYRl0vPhkk-L5K9mxvc/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:194 loadAuthorizationStates(for:) new entry: kTCCServiceScreenCapture com.nexy.assistant full
error	19:20:55.075511-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CAIIugCI3D6x0jkL7BXjcYRl0vPhkk-L5K9mxvc/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:194 loadAuthorizationStates(for:) new entry: kTCCServiceListenEvent com.nexy.assistant full
error	19:20:55.075632-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CAIIugCI3D6x0jkL7BXjcYRl0vPhkk-L5K9mxvc/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:194 loadAuthorizationStates(for:) new entry: kTCCServiceScreenCapture com.nexy.assistant full
error	19:20:55.081343-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CAIIugCI3D6x0jkL7BXjcYRl0vPhkk-L5K9mxvc/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:194 loadAuthorizationStates(for:) new entry: kTCCServiceAppleEvents com.nexy.assistant full
error	19:20:55.081784-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CAIIugCI3D6x0jkL7BXjcYRl0vPhkk-L5K9mxvc/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:194 loadAuthorizationStates(for:) new entry: kTCCServiceMicrophone com.nexy.assistant full
error	19:20:55.086150-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CAIIugCI3D6x0jkL7BXjcYRl0vPhkk-L5K9mxvc/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:194 loadAuthorizationStates(for:) new entry: kTCCServiceAppleEvents com.nexy.assistant full
error	19:20:55.086546-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CAIIugCI3D6x0jkL7BXjcYRl0vPhkk-L5K9mxvc/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:194 loadAuthorizationStates(for:) new entry: kTCCServiceMicrophone com.nexy.assistant full
default	19:21:04.746376-0500	Nexy	[0xa69c25400] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	19:21:04.748399-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=5671.6, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=5671, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	19:21:04.751446-0500	tccd	AUTHREQ_SUBJECT: msgID=5671.6, subject=com.nexy.assistant,
default	19:21:04.752990-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x92f179800 at /Applications/Nexy.app
default	19:21:04.775103-0500	tccd	Notifying for access  kTCCServicePostEvent for target PID[5671], responsiblePID[5671], responsiblePath: /Applications/Nexy.app to UID: 501
default	19:21:04.775530-0500	Nexy	[0xa69c25400] invalidated after the last release of the connection object
default	19:21:04.830151-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x92f17aa00 at /Applications/Nexy.app
default	19:21:04.850255-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x92f179500 at /Applications/Nexy.app
default	19:21:04.854188-0500	tccd	Publishing <TCCDEvent: type=Modify, service=kTCCServicePostEvent, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 0 subscribers: {
}
error	19:21:08.402725-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CAIIugCI3D6x0jkL7BXjcYRl0vPhkk-L5K9mxvc/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:194 loadAuthorizationStates(for:) new entry: kTCCServiceScreenCapture com.nexy.assistant full
error	19:21:08.406105-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CAIIugCI3D6x0jkL7BXjcYRl0vPhkk-L5K9mxvc/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:194 loadAuthorizationStates(for:) new entry: kTCCServiceListenEvent com.nexy.assistant full
error	19:21:08.406409-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CAIIugCI3D6x0jkL7BXjcYRl0vPhkk-L5K9mxvc/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:194 loadAuthorizationStates(for:) new entry: kTCCServiceAccessibility com.nexy.assistant none
error	19:21:08.438554-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CAIIugCI3D6x0jkL7BXjcYRl0vPhkk-L5K9mxvc/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:194 loadAuthorizationStates(for:) new entry: kTCCServiceAppleEvents com.nexy.assistant full
error	19:21:08.438621-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CAIIugCI3D6x0jkL7BXjcYRl0vPhkk-L5K9mxvc/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:194 loadAuthorizationStates(for:) new entry: kTCCServiceAppleEvents com.nexy.assistant full
default	19:21:13.069452-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x92f179800 at /Applications/Nexy.app
default	19:21:13.090588-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x92f17aa00 at /Applications/Nexy.app
default	19:21:13.116944-0500	tccd	Publishing <TCCDEvent: type=Modify, service=kTCCServiceAccessibility, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 0 subscribers: {
}
error	19:21:13.152514-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CAIIugCI3D6x0jkL7BXjcYRl0vPhkk-L5K9mxvc/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:194 loadAuthorizationStates(for:) new entry: kTCCServiceAccessibility com.nexy.assistant full
error	19:21:13.152698-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CAIIugCI3D6x0jkL7BXjcYRl0vPhkk-L5K9mxvc/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:194 loadAuthorizationStates(for:) new entry: kTCCServiceScreenCapture com.nexy.assistant full
error	19:21:13.153031-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CAIIugCI3D6x0jkL7BXjcYRl0vPhkk-L5K9mxvc/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:194 loadAuthorizationStates(for:) new entry: kTCCServiceListenEvent com.nexy.assistant full
error	19:21:13.153141-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CAIIugCI3D6x0jkL7BXjcYRl0vPhkk-L5K9mxvc/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:194 loadAuthorizationStates(for:) new entry: kTCCServiceAccessibility com.nexy.assistant full
error	19:21:13.154397-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CAIIugCI3D6x0jkL7BXjcYRl0vPhkk-L5K9mxvc/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:194 loadAuthorizationStates(for:) new entry: kTCCServiceAccessibility com.nexy.assistant full
error	19:21:13.154561-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CAIIugCI3D6x0jkL7BXjcYRl0vPhkk-L5K9mxvc/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:194 loadAuthorizationStates(for:) new entry: kTCCServiceScreenCapture com.nexy.assistant full
error	19:21:13.154887-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CAIIugCI3D6x0jkL7BXjcYRl0vPhkk-L5K9mxvc/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:194 loadAuthorizationStates(for:) new entry: kTCCServiceListenEvent com.nexy.assistant full
error	19:21:13.154998-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CAIIugCI3D6x0jkL7BXjcYRl0vPhkk-L5K9mxvc/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:194 loadAuthorizationStates(for:) new entry: kTCCServiceAccessibility com.nexy.assistant full
error	19:21:13.167928-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CAIIugCI3D6x0jkL7BXjcYRl0vPhkk-L5K9mxvc/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:194 loadAuthorizationStates(for:) new entry: kTCCServiceAppleEvents com.nexy.assistant full
error	19:21:13.168548-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CAIIugCI3D6x0jkL7BXjcYRl0vPhkk-L5K9mxvc/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:194 loadAuthorizationStates(for:) new entry: kTCCServiceMicrophone com.nexy.assistant full
error	19:21:13.168656-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CAIIugCI3D6x0jkL7BXjcYRl0vPhkk-L5K9mxvc/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:194 loadAuthorizationStates(for:) new entry: kTCCServiceAppleEvents com.nexy.assistant full
error	19:21:13.169202-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CAIIugCI3D6x0jkL7BXjcYRl0vPhkk-L5K9mxvc/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:194 loadAuthorizationStates(for:) new entry: kTCCServiceMicrophone com.nexy.assistant full
default	19:21:19.335992-0500	WindowServer	0[outside of RPC]: Process death: 0x0-0x3a03a0 (Nexy) connectionID: 10E3C3 pid: 5671 in session 0x101
default	19:21:19.336061-0500	WindowServer	<BSCompoundAssertion:0xbe8809580> ([FocusManager:257]-deferringPolicyEvaluationSuppression) acquire for reason:process death - 0x0-0x3a03a0 (Nexy) acq:0xbeb3f56e0 count:1
default	19:21:19.336487-0500	audiomxd	  ServerSessionManager.mm:478   { "action":"destroy_session", "session":{"ID":"0x1e8047","name":"Nexy(5671)"}, "details":null }
default	19:21:19.336564-0500	audiomxd	AudioApplicationInfoImpl.mm:690   Successfully removed session 0x1e8047 from AudioApp, recording state unchanged (app: {"name":"[implicit] Nexy","pid":5671})
default	19:21:19.336594-0500	audiomxd	  ServerSessionManager.mm:1086  destroy audio app instance since was created implicitly by session creation and all sessions now gone (audio app: {"name":"[implicit] Nexy","pid":5671})
default	19:21:19.340055-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 72, PID = 5671, Name = sid:0x1e8047, Nexy(5671), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	19:21:19.340806-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 72, PID = 5671, Name = sid:0x1e8047, Nexy(5671), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	19:21:19.341363-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	19:21:19.341440-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	19:21:19.341469-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	19:21:19.341586-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	19:21:19.342266-0500	WindowServer	0[outside of RPC]: [FocusManager:257] update to deferring policy requested for reason: permitted list updated - 0x0-0x3a03a0 removed - but we are suppressing evaluation for reasons: {(
    "process death - 0x0-0x3a03a0 (Nexy)"
)}
default	19:21:19.341052-0500	audiomxd	UpdateAudioState CID 0x4D120001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	19:21:19.341239-0500	audiomxd	UpdateAudioState CID 0x4D120001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	19:21:19.342765-0500	WindowServer	0[outside of RPC]: [FocusManager:257] update to deferring policy requested for reason: permitted list updated - 0x1-0x1627 removed - but we are suppressing evaluation for reasons: {(
    "process death - 0x0-0x3a03a0 (Nexy)"
)}
default	19:21:19.349210-0500	runningboardd	XPC connection invalidated: [app<application.com.nexy.assistant.27212639.27212645(501)>:5671]
default	19:21:19.350645-0500	coreaudiod	>>> NEGOTIATE [com.nexy.assistant]
default	19:21:19.350887-0500	coreaudiod	<<< NEGOTIATE [com.nexy.assistant]
default	19:21:19.356342-0500	coreaudiod	IssueReporting.cpp:492   RTAID [ use_case=Generic report_type=RMS Generic Chain clientID=ADM node=ADM::com.nexy.assistant_10285.10209.0_airpods noise suppression studio::out-0 issue_detected_sample_time=308640.000000 ] -- [ rms:[-42.233929], peaks:[-25.361877] ]
default	19:21:19.356388-0500	coreaudiod	IssueReporting.cpp:492   RTAID [ use_case=Generic report_type=RMS Generic Chain clientID=ADM node=ADM::com.nexy.assistant_10285.10209.0_airpods noise suppression studio::in-0 issue_detected_sample_time=0.000000 ] -- [ rms:[-39.924557], peaks:[-23.832886] ]
default	19:21:19.357696-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645(501)>:5671] termination reported by launchd (0, 0, 0)
default	19:21:19.357769-0500	runningboardd	Removing process: [app<application.com.nexy.assistant.27212639.27212645(501)>:5671]
default	19:21:19.358014-0500	runningboardd	Removing launch job for: [app<application.com.nexy.assistant.27212639.27212645(501)>:5671]
default	19:21:19.358496-0500	runningboardd	Removed job for [app<application.com.nexy.assistant.27212639.27212645(501)>:5671]
default	19:21:19.358547-0500	runningboardd	Removing assertions for terminated process: [app<application.com.nexy.assistant.27212639.27212645(501)>:5671]
default	19:21:19.363281-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.27212639.27212645(501)>: none (role: None) (endowments: (null))
default	19:21:19.363493-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.27212639.27212645(501)>: none (role: None) (endowments: (null))
default	19:21:19.363622-0500	audiomxd	  ServerSessionManager.mm:1327  Monitored process died, pid = 5671, name = Nexy
default	19:21:19.364033-0500	launchservicesd	Hit the server for a process handle f8c59c400001627 that resolved to: [app<application.com.nexy.assistant.27212639.27212645(501)>:5671]
default	19:21:19.364115-0500	gamepolicyd	Received state update for 5671 (app<application.com.nexy.assistant.27212639.27212645(501)>, none-NotVisible
default	19:21:19.367337-0500	loginwindow	-[ApplicationManager handleCASEvent:withData:] | CAS notification for appDeath for com.nexy.assistant with asn: LSASN:{hi=0x0;lo=0x3a03a0} for bundle path: /Applications/Nexy.app with URL: file:///Applications/Nexy.app/
default	19:21:19.367371-0500	loginwindow	-[Application setState:] | enter: <Application: 0x84f9b4500: Nexy> state 3
default	19:21:19.367388-0500	loginwindow	-[PersistentAppsSupport applicationQuit:] | for app:Nexy, _appTrackingState = 2
default	19:21:19.369457-0500	loginwindow	-[Application setState:] | enter: <Application: 0x84f9b4500: Nexy> state 4
default	19:21:19.369468-0500	loginwindow	-[PersistentAppsSupport applicationQuit:] | for app:Nexy, _appTrackingState = 2
default	19:21:22.419370-0500	logger	launching: /usr/bin/open -n -a /Applications/Nexy.app
default	19:21:22.518459-0500	lsd	com.nexy.assistant/Unknown Persona:5:5:1:1:Building bundle record for app
default	19:21:22.518650-0500	lsd	com.nexy.assistant/Unknown Persona:5:5:2:1:Built bundle record for app
default	19:21:22.520756-0500	lsd	com.nexy.assistant/Unknown Persona:5:4:2:1:_LSServerRegisterItemInfo result = 0
default	19:21:22.525013-0500	dmd	Received xpc stream event (distributed notification matching) with name: com.apple.LaunchServices.applicationRegistered user info: {
    CFBundleDisplayName = Nexy;
    bundleIDs =     (
        "com.nexy.assistant"
    );
    isPlaceholder = 0;
}
default	19:21:22.528058-0500	runningboardd	Launch request for app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>[0] is using uid 501 (divined from auid 501 euid 501)
default	19:21:22.528143-0500	runningboardd	Acquiring assertion targeting app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)> from originator [osservice<com.apple.coreservices.uiagent(501)>:3678] with description <RBSAssertionDescriptor| "LS launch com.nexy.assistant" ID:403-3678-153818 target:app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)> attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"LaunchRoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	19:21:22.528228-0500	runningboardd	Assertion 403-3678-153818 (target:app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>) will be created as active
default	19:21:22.531371-0500	runningboardd	Checking PreventLaunch: global:0 exPath:/Applications/Nexy.app/Contents/MacOS/Nexy predicates:(null) allow:(null)
default	19:21:22.531405-0500	runningboardd	Creating and launching job for: app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>
default	19:21:22.531419-0500	runningboardd	_mutateContextIfNeeded called for com.nexy.assistant
default	19:21:22.531495-0500	runningboardd	app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>: -[RBPersonaManager personaForIdentity:context:personaUID:personaUniqueString:] required 0.000000 ms (wallclock); resolved to {4294967295, (null)}
default	19:21:22.542125-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] is not RunningBoard jetsam managed.
default	19:21:22.542143-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] This process will not be managed.
default	19:21:22.542155-0500	runningboardd	Now tracking process: [app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767]
default	19:21:22.542337-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	19:21:22.543047-0500	gamepolicyd	Hit the server for a process handle fe3ecff00001687 that resolved to: [app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767]
default	19:21:22.543083-0500	gamepolicyd	Received state update for 5767 (app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>, running-active-NotVisible
default	19:21:22.547648-0500	runningboardd	Using default underlying assertion for app: [app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767]
default	19:21:22.547751-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] from originator [app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] with description <RBSAssertionDescriptor| "RB Underlying Assertion" ID:403-403-153819 target:5767 attributes:[
	<RBSDomainAttribute| domain:"com.apple.underlying" name:"defaultUnderlyingAppAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	19:21:22.547914-0500	runningboardd	Assertion 403-403-153819 (target:[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767]) will be created as active
default	19:21:22.548199-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] Ignoring jetsam update because this process is not memory-managed
default	19:21:22.548214-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] Ignoring suspend because this process is not lifecycle managed
default	19:21:22.548233-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] Set darwin role to: UserInteractive
default	19:21:22.548245-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] Ignoring GPU update because this process is not GPU managed
default	19:21:22.548263-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] Ignoring memory limit update because this process is not memory-managed
default	19:21:22.548365-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] reported to RB as running
default	19:21:22.550621-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] from originator [osservice<com.apple.coreservices.launchservicesd>:367] with description <RBSAssertionDescriptor| "uielement:5767" ID:403-367-153820 target:5767 attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"RoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	19:21:22.550767-0500	runningboardd	Assertion 403-367-153820 (target:[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767]) will be created as active
default	19:21:22.550796-0500	CoreServicesUIAgent	LAUNCH: 0x0-0x3b53b5 com.nexy.assistant starting stopped process.
default	19:21:22.552334-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] Ignoring jetsam update because this process is not memory-managed
default	19:21:22.552512-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] Ignoring suspend because this process is not lifecycle managed
default	19:21:22.552634-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] Ignoring GPU update because this process is not GPU managed
default	19:21:22.552660-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] Ignoring memory limit update because this process is not memory-managed
default	19:21:22.552946-0500	runningboardd	Successfully acquired underlying assertion for [app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767]
default	19:21:22.552440-0500	loginwindow	-[Application updateInformation] | Got App URL: file:///Applications/Nexy.app/
default	19:21:22.552665-0500	loginwindow	-[Application setState:] | enter: <Application: 0x84f9b4500: Nexy> state 2
default	19:21:22.552695-0500	loginwindow	-[ApplicationManager checkInAppContext:eventData:] | ApplicationManager: Checked in app : Nexy
default	19:21:22.553801-0500	kernel	Nexy[5767] triggered unnest of range 0x202000000->0x204000000 of DYLD shared region in VM map 0x87d2759ddb4f484b. While not abnormal for debuggers, this increases system memory footprint until the target exits.
default	19:21:22.553827-0500	kernel	Nexy[5767] triggered unnest of range 0x204000000->0x206000000 of DYLD shared region in VM map 0x87d2759ddb4f484b. While not abnormal for debuggers, this increases system memory footprint until the target exits.
default	19:21:22.555634-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	19:21:22.556009-0500	runningboardd	Invalidating assertion 403-3678-153818 (target:app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>) from originator [osservice<com.apple.coreservices.uiagent(501)>:3678]
default	19:21:22.556045-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] Ignoring jetsam update because this process is not memory-managed
default	19:21:22.556138-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] Ignoring suspend because this process is not lifecycle managed
default	19:21:22.556190-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] Ignoring GPU update because this process is not GPU managed
default	19:21:22.556145-0500	gamepolicyd	Received state update for 5767 (app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>, running-active-NotVisible
default	19:21:22.556268-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] Ignoring memory limit update because this process is not memory-managed
default	19:21:22.561106-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	19:21:22.573323-0500	logger	verifying new process for /Applications/Nexy.app/Contents/MacOS/Nexy
default	19:21:22.621486-0500	Nexy	[0x1041b1460] activating connection: mach=true listener=false peer=false name=com.apple.cfprefsd.daemon
default	19:21:22.621553-0500	Nexy	[0x1041b19a0] activating connection: mach=true listener=false peer=false name=com.apple.cfprefsd.agent
default	19:21:22.621794-0500	logger	detected new pid 5767 for /Applications/Nexy.app/Contents/MacOS/Nexy
default	19:21:22.662113-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] Ignoring jetsam update because this process is not memory-managed
default	19:21:22.662127-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] Ignoring suspend because this process is not lifecycle managed
default	19:21:22.662137-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] Ignoring GPU update because this process is not GPU managed
default	19:21:22.662157-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] Ignoring memory limit update because this process is not memory-managed
default	19:21:22.662277-0500	gamepolicyd	Received state update for 5767 (app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>, running-active-NotVisible
default	19:21:22.665457-0500	gamepolicyd	Received state update for 5767 (app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>, running-active-NotVisible
error	19:21:22.743263-0500	Nexy	dlsym cannot find symbol NSMakeRect in CFBundle 0xbb067c000 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	19:21:22.743499-0500	Nexy	dlsym cannot find symbol NSMakePoint in CFBundle 0xbb067c000 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	19:21:22.743705-0500	Nexy	dlsym cannot find symbol NSMakeSize in CFBundle 0xbb067c000 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	19:21:22.743906-0500	Nexy	dlsym cannot find symbol NSMakeRange in CFBundle 0xbb067c000 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
default	19:21:22.744940-0500	Nexy	[0x1041a0280] activating connection: mach=true listener=false peer=false name=com.apple.coreservices.launchservicesd
default	19:21:22.745609-0500	Nexy	[0xbafc98000] activating connection: mach=true listener=false peer=false name=com.apple.analyticsd
default	19:21:22.745923-0500	Nexy	[0xbafc98140] activating connection: mach=true listener=false peer=false name=com.apple.pasteboard.1
default	19:21:22.746321-0500	Nexy	[0xbafc98280] activating connection: mach=true listener=false peer=false name=com.apple.distributed_notifications@Uv3
default	19:21:22.746423-0500	Nexy	Received configuration update from daemon (initial)
default	19:21:22.748519-0500	Nexy	void _NSDisableAutomaticTerminationAndLog(NSString *) No windows open yet
default	19:21:22.748950-0500	Nexy	[0xbafc983c0] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	19:21:22.749639-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=5767.1, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=5767, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	19:21:22.751306-0500	tccd	AUTHREQ_SUBJECT: msgID=5767.1, subject=com.nexy.assistant,
default	19:21:22.752008-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x92f17b300 at /Applications/Nexy.app
default	19:21:22.771984-0500	Nexy	[0xbafc983c0] invalidated after the last release of the connection object
default	19:21:22.772347-0500	Nexy	server port 0x00003713, session port 0x00003713
default	19:21:22.773313-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=397.2634, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=5767, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=397, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	19:21:22.773343-0500	tccd	requestor: TCCDProcess: identifier=com.apple.WindowServer, pid=397, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=5767, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	19:21:22.774203-0500	tccd	AUTHREQ_SUBJECT: msgID=397.2634, subject=com.nexy.assistant,
default	19:21:22.774903-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x92f17b300 at /Applications/Nexy.app
default	19:21:22.800968-0500	Nexy	New connection 0x806e3 main
default	19:21:22.803590-0500	Nexy	CHECKIN: pid=5767
default	19:21:22.812987-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] from originator [osservice<com.apple.coreservices.launchservicesd>:367] with description <RBSAssertionDescriptor| "uielement:5767" ID:403-367-153821 target:5767 attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"RoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	19:21:22.813086-0500	runningboardd	Assertion 403-367-153821 (target:[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767]) will be created as active
default	19:21:22.813533-0500	runningboardd	Invalidating assertion 403-367-153820 (target:[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767]) from originator [osservice<com.apple.coreservices.launchservicesd>:367]
default	19:21:22.813400-0500	Nexy	CHECKEDIN: pid=5767 asn=0x0-0x3b53b5 foreground=0
default	19:21:22.813231-0500	launchservicesd	CHECKIN:0x0-0x3b53b5 5767 com.nexy.assistant
default	19:21:22.813498-0500	loginwindow	-[Application updateInformation] | Got App URL: file:///Applications/Nexy.app/
default	19:21:22.813631-0500	loginwindow	-[ApplicationManager checkInAppContext:eventData:] | ApplicationManager: Checked in app : Nexy
default	19:21:22.813726-0500	Nexy	[0xbafc983c0] activating connection: mach=false listener=true peer=false name=(anonymous)
default	19:21:22.813780-0500	Nexy	[0xbafc983c0] Connection returned listener port: 0x4503
default	19:21:22.814088-0500	Nexy	[0xbafcc4300] activating connection: mach=false listener=false peer=true name=com.apple.xpc.anonymous.0xbafc983c0.peer[367].0xbafcc4300
default	19:21:22.816890-0500	Nexy	FRONTLOGGING: version 1
default	19:21:22.816950-0500	Nexy	Registered, pid=5767 ASN=0x0,0x3b53b5
default	19:21:22.817440-0500	WindowServer	806e3[CreateApplication]: Process creation: 0x0-0x3b53b5 (Nexy) connectionID: 806E3 pid: 5767 in session 0x101
default	19:21:22.817734-0500	Nexy	[0xbafc98500] activating connection: mach=true listener=false peer=false name=com.apple.lsd.mapdb
default	19:21:22.820060-0500	Nexy	[0xbafc983c0] Connection returned listener port: 0x4503
default	19:21:22.821486-0500	Nexy	BringForward: pid=5767 asn=0x0-0x3b53b5 bringForward=0 foreground=0 uiElement=1 launchedByLS=1 modifiersCount=1 allDisabled=0
default	19:21:22.821986-0500	Nexy	BringFrontModifier: pid=5767 asn=0x0-0x3b53b5 Modifier 0 hideAfter=0 hideOthers=0 dontMakeFrontmost=0 mouseDown=0/0 seed=0/0
default	19:21:22.822758-0500	Nexy	Current system appearance, (HLTB: 2), (SLS: 1)
default	19:21:22.827209-0500	Nexy	Post-registration system appearance: (HLTB: 2)
default	19:21:22.831379-0500	Nexy	[0xbafc983c0] Connection returned listener port: 0x4503
default	19:21:22.832526-0500	distnoted	register name: com.apple.xctest.FakeForceTouchDevice object: com.nexy.assistant token: 1e0000001d pid: 5767
default	19:21:22.835347-0500	Nexy	[0xbafc983c0] Connection returned listener port: 0x4503
default	19:21:22.839755-0500	Nexy	Activated connection to com.apple.linkd.autoShortcut (ApplicationService)
default	19:21:22.839967-0500	Nexy	[0xbafc98a00] activating connection: mach=false listener=true peer=false name=(anonymous)
default	19:21:22.970618-0500	Nexy	Registered notify signal com.apple.caulk.alloc.rtdump (0)
default	19:21:22.973284-0500	Nexy	System_Input_Processing_Notification_Handler.mm:456   System_Input_Processing_Notification_Handler::is_vi_available(): Voice isolation DSP is available for client with bundle id com.nexy.assistant (AVFoundation is available, application is not in client deny list, application is not FaceTime variant)
default	19:21:22.974817-0500	Nexy	[0xbafc98b40] activating connection: mach=true listener=false peer=false name=com.apple.cmio.registerassistantservice.system-extensions
fault	19:21:22.977456-0500	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D AUID=501> and <type=Application identifier=application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D>
default	19:21:22.982132-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOInitializeListenersForBundleID: for <private> -> <private>
default	19:21:22.983777-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> vpio_preferenceChangedListener: new value ((null)) for key AUVoiceIOClients/com-nexy-assistant/AUVoiceIOChatFlavor, translatedBundleID com.nexy.assistant, bundleIDs {(
    "com.nexy.assistant"
)}
default	19:21:22.983957-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> vpio_preferenceChangedListener: new value ((null)) for key AUVoiceIOClients/com-nexy-assistant/AUVoiceIOIsAutoChatFlavorEnabled, translatedBundleID com.nexy.assistant, bundleIDs {(
    "com.nexy.assistant"
)}
default	19:21:22.984077-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetSupportedChatFlavorsForBundleID: <private>-><private> get supported chat flavors: <private>
default	19:21:22.984087-0500	Nexy	            HALSystem.cpp:134    Enabling HAL Voice Isolation support
default	19:21:22.984112-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetHiddenChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	19:21:22.984226-0500	Nexy	[0xbafc98c80] activating connection: mach=true listener=false peer=false name=com.apple.tccd
default	19:21:22.984292-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOHiddenChatFlavors newValue: (
    1
)
default	19:21:22.984636-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=5767.2, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=5767, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	19:21:22.990384-0500	tccd	AUTHREQ_SUBJECT: msgID=5767.2, subject=com.nexy.assistant,
default	19:21:22.990962-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc79244300 at /Applications/Nexy.app
default	19:21:23.007009-0500	Nexy	[0xbafc98c80] invalidated after the last release of the connection object
default	19:21:23.007139-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetPreferredChatFlavorForBundleID: <private>-><private> get value: 0
default	19:21:23.007174-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetSupportedChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	19:21:23.007380-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOSupportedChatFlavors newValue: (
    0,
    2
)
default	19:21:23.008430-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=411.1493, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=5767, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=398, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	19:21:23.009224-0500	tccd	AUTHREQ_SUBJECT: msgID=411.1493, subject=com.nexy.assistant,
default	19:21:23.009767-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc79244300 at /Applications/Nexy.app
error	19:21:23.025554-0500	tccd	Request message contains a target_token to accessing_process (TCCDProcess: identifier=com.nexy.assistant, pid=5767, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy) but TCCDProcess: identifier=com.apple.audio.coreaudiod, pid=411, auid=202, euid=202, binary_path=/usr/sbin/coreaudiod is not a TCC manager for service: kTCCServiceScreenCapture.
default	19:21:23.026427-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=411.1495, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=5767, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=398, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	19:21:23.027266-0500	tccd	AUTHREQ_SUBJECT: msgID=411.1495, subject=com.nexy.assistant,
default	19:21:23.027813-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc79244300 at /Applications/Nexy.app
default	19:21:23.041387-0500	Nexy	  HALPlugInManagement.cpp:440    HALPlugInManagement::RegisterPlugIns: skipping in-process plug-ins
error	19:21:23.041405-0500	Nexy	AddInstanceForFactory: No factory registered for id <CFUUID 0xbb1571e00> F8BB1C28-BAE8-11D6-9C31-00039315CD46
error	19:21:23.057420-0500	Nexy	         HALC_ProxyObjectMap.cpp:174   HALC_ProxyObjectMap::_CopyObjectByObjectID: failed to create the local object
error	19:21:23.057432-0500	Nexy	            HALC_ShellDevice.cpp:2673  HALC_ShellDevice::RebuildControlList: couldn't find the control object
default	19:21:23.060094-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	19:21:23.060220-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	19:21:23.064407-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetPreferredChatFlavorForBundleID: <private>-><private> get value: 0
default	19:21:24.539000-0500	kernel	SK[6]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 121F3701-C0AD-433D-A84B-631700CB309E flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.54993,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0x88f70688 tp_proto=0x06"
default	19:21:24.539119-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:54993<-><IPv4-redacted>:53] interface: utun6 (skipped: 47531)
so_gencnt: 2851617 t_state: SYN_SENT process: Nexy:5767 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 1 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x826b16d2
default	19:21:24.540034-0500	kernel	tcp connected: [<IPv4-redacted>:54993<-><IPv4-redacted>:53] interface: utun6 (skipped: 47531)
so_gencnt: 2851617 t_state: ESTABLISHED process: Nexy:5767 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 1 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x826b16d2
default	19:21:24.540317-0500	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:54993<-><IPv4-redacted>:53] interface: utun6 (skipped: 47531)
so_gencnt: 2851617 t_state: FIN_WAIT_1 process: Nexy:5767 Duration: 0.002 sec Conn_Time: 0.002 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 2.000 ms rttvar: 1.000 ms base rtt: 1 ms so_error: 0 svc/tc: 0 flow: 0x826b16d2
default	19:21:24.540328-0500	kernel	tcp_connection_summary [<IPv4-redacted>:54993<-><IPv4-redacted>:53] interface: utun6 (skipped: 47531)
so_gencnt: 2851617 t_state: FIN_WAIT_1 process: Nexy:5767 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	19:21:24.559047-0500	Nexy	[0xbafc98c80] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioComponentRegistrar
default	19:21:24.571213-0500	Nexy	                AUHAL.cpp:420   AUHAL: (0xbb05c9c40) Selecting device 85 from constructor
default	19:21:24.571223-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0xbb05c9c40)
default	19:21:24.571229-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0xbb05c9c40) not already running
default	19:21:24.571234-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0xbb05c9c40) nothing to teardown
default	19:21:24.571238-0500	Nexy	                AUHAL.cpp:762   SelectDevice: (0xbb05c9c40) connecting device 85
default	19:21:24.571336-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0xbb05c9c40) Device ID: 85 (Input:No | Output:Yes): true
default	19:21:24.571429-0500	Nexy	                AUHAL.cpp:774   SelectDevice: (0xbb05c9c40) created ioproc 0xa for device 85
default	19:21:24.571531-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0xbb05c9c40) adding 7 device listeners to device 85
default	19:21:24.571676-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0xbb05c9c40) adding 0 device delegate listeners to device 85
default	19:21:24.571683-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0xbb05c9c40)
default	19:21:24.571755-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  48000 Hz, Float32, interleaved
default	19:21:24.571763-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	19:21:24.571769-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	19:21:24.571775-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	19:21:24.571784-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	19:21:24.571865-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0xbb05c9c40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	19:21:24.571873-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0xbb05c9c40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	19:21:24.571877-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	19:21:24.571888-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0xbb05c9c40) removing 0 device listeners from device 0
default	19:21:24.571894-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0xbb05c9c40) removing 0 device delegate listeners from device 0
default	19:21:24.571898-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0xbb05c9c40)
default	19:21:24.571913-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is DISABLED
default	19:21:24.572001-0500	Nexy	                AUHAL.cpp:2303  SetProperty: (0xbb05c9c40) caller requesting device change from 85 to 91
default	19:21:24.572010-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0xbb05c9c40)
default	19:21:24.572016-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0xbb05c9c40) not already running
default	19:21:24.572019-0500	Nexy	                AUHAL.cpp:687   SelectDevice: (0xbb05c9c40) disconnecting device 85
default	19:21:24.572022-0500	Nexy	                AUHAL.cpp:751   SelectDevice: (0xbb05c9c40) destroying ioproc 0xa for device 85
default	19:21:24.572074-0500	Nexy	  AVAudioSession_MacOS.mm:1021  initForMacOS
default	19:21:24.572530-0500	Nexy	[0xbafc98f00] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioSession
default	19:21:24.573512-0500	audiomxd	  ServerSessionManager.mm:315   { "action":"create_session", "session":{"ID":"0x1e8048","name":"Nexy(5767)"}, "details":{"PID":5767,"session_type":"Primary"} }
default	19:21:24.573601-0500	audiomxd	AudioApplicationInfoImpl.mm:250   Setting initial isRecording state: 0 for newly-created AudioApp
	app: {"name":"[implicit] Nexy","pid":5767}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1e8048, sessionType: 'prim', isRecording: false }, 
]
default	19:21:24.574356-0500	audiomxd	  ServerSessionManager.mm:1322  Start process monitoring, pid = 5767, name = Nexy
default	19:21:24.574606-0500	Nexy	    SessionCore_Create.mm:99    Created session 0xbb068d260 with ID: 0x1e8048
default	19:21:24.575206-0500	Nexy	[0xbafc99040] activating connection: mach=true listener=false peer=false name=com.apple.audioanalyticsd
error	19:21:24.575587-0500	Nexy	Reporter disconnected. { function=sendMessage, reporterID=24769076396033 }
default	19:21:24.575603-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped Unknown {1C-77-54-18-C8-A3:output, 0xa}
default	19:21:24.575654-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	19:21:24.575747-0500	Nexy	                AUHAL.cpp:762   SelectDevice: (0xbb05c9c40) connecting device 91
default	19:21:24.575834-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0xbb05c9c40) Device ID: 91 (Input:Yes | Output:No): true
default	19:21:24.577140-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=411.1496, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=5767, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=398, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	19:21:24.578463-0500	tccd	AUTHREQ_SUBJECT: msgID=411.1496, subject=com.nexy.assistant,
default	19:21:24.579319-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc79244300 at /Applications/Nexy.app
default	19:21:24.597763-0500	Nexy	                AUHAL.cpp:774   SelectDevice: (0xbb05c9c40) created ioproc 0xa for device 91
default	19:21:24.597929-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0xbb05c9c40) adding 7 device listeners to device 91
default	19:21:24.598093-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0xbb05c9c40) adding 0 device delegate listeners to device 91
default	19:21:24.598099-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0xbb05c9c40)
default	19:21:24.598110-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 output streams; not all mono
default	19:21:24.598123-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	19:21:24.598252-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  input stream 0 [0x5c]:  1 ch,  24000 Hz, Float32
default	19:21:24.598259-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 input streams; all mono
default	19:21:24.598267-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  1 ch,  24000 Hz, Float32
default	19:21:24.598351-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0xbb05c9c40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	19:21:24.598360-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0xbb05c9c40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	19:21:24.598365-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	19:21:24.598368-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0xbb05c9c40) removing 7 device listeners from device 85
default	19:21:24.598555-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0xbb05c9c40) removing 0 device delegate listeners from device 85
default	19:21:24.598566-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0xbb05c9c40)
default	19:21:24.599205-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	19:21:24.600471-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=411.1497, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=5767, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=398, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	19:21:24.601593-0500	tccd	AUTHREQ_SUBJECT: msgID=411.1497, subject=com.nexy.assistant,
default	19:21:24.602200-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc79244300 at /Applications/Nexy.app
default	19:21:24.619410-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	19:21:24.620343-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=411.1498, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=5767, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=398, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	19:21:24.621201-0500	tccd	AUTHREQ_SUBJECT: msgID=411.1498, subject=com.nexy.assistant,
default	19:21:24.621819-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc79244300 at /Applications/Nexy.app
default	19:21:24.638113-0500	Nexy	Registered notify signal com.apple.caulk.alloc.audiodump (0)
default	19:21:24.639507-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=411.1499, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=5767, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=398, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	19:21:24.640355-0500	tccd	AUTHREQ_SUBJECT: msgID=411.1499, subject=com.nexy.assistant,
default	19:21:24.640935-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc79244300 at /Applications/Nexy.app
default	19:21:24.657181-0500	coreaudiod	>>> NEGOTIATE [com.nexy.assistant]
default	19:21:24.657361-0500	coreaudiod	<<< NEGOTIATE [com.nexy.assistant]
default	19:21:24.658318-0500	coreaudiod	>>> ADAPT [com.nexy.assistant]
default	19:21:24.658672-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xa380e9b00] Created node ADM::com.nexy.assistant_10301.10209.0_airpods noise suppression studio::in-0 with nodeID 0 - reporting period = 10.000000, sample rate = 24000.000000
default	19:21:24.658735-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xa380e9b00] Created node ADM::com.nexy.assistant_10301.10209.0_airpods noise suppression studio::out-0 with nodeID 1 - reporting period = 10.000000, sample rate = 24000.000000
default	19:21:24.726207-0500	coreaudiod	<<< ADAPT [com.nexy.assistant]
default	19:21:24.727953-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:10301 called from <private>
default	19:21:24.727998-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Input {1C-77-54-18-C8-A3:input, 0xa}
default	19:21:24.728007-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	19:21:24.729722-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:10301 called from <private>
default	19:21:24.729880-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(10301)
default	19:21:24.729898-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:10301 called from <private>
default	19:21:24.729907-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:10301 called from <private>
default	19:21:24.730070-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(10300)
default	19:21:24.730619-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:10300 called from <private>
default	19:21:24.730659-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:10300 called from <private>
default	19:21:24.733935-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] from originator [osservice<com.apple.powerd>:338] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:403-338-153832 target:5767 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	19:21:24.734057-0500	runningboardd	Assertion 403-338-153832 (target:[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767]) will be created as active
fault	19:21:24.736107-0500	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D AUID=501> and <type=Application identifier=application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D>
default	19:21:24.736757-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] Ignoring jetsam update because this process is not memory-managed
default	19:21:24.736895-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] Ignoring suspend because this process is not lifecycle managed
default	19:21:24.736979-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] Ignoring GPU update because this process is not GPU managed
default	19:21:24.737164-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] Ignoring memory limit update because this process is not memory-managed
fault	19:21:24.738358-0500	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D AUID=501> and <type=Application identifier=application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D>
default	19:21:24.740555-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	19:21:24.741079-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	19:21:24.742233-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(10301)
default	19:21:24.742259-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(10301)
default	19:21:24.742264-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:10301 called from <private>
default	19:21:24.742274-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:10301 called from <private>
default	19:21:24.742280-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:10301 called from <private>
default	19:21:24.742285-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:10301 called from <private>
default	19:21:24.742315-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(10301)
default	19:21:24.742326-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(10301)
default	19:21:24.743474-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:10301 called from <private>
default	19:21:24.750372-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1e8048","name":"Nexy(5767)"}, "details":{"deviceUIDs":["1C-77-54-18-C8-A3:input"],"implicit_category":"Record","input_running":true,"output_running":false} }
default	19:21:24.750933-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 73, PID = 5767, Name = sid:0x1e8048, Nexy(5767), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	19:21:24.751097-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 73, PID = 5767, Name = sid:0x1e8048, Nexy(5767), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	19:21:24.751521-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 73, PID = 5767, Name = sid:0x1e8048, Nexy(5767), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	19:21:24.743531-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:10301 called from <private>
default	19:21:24.743608-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:10301 called from <private>
default	19:21:24.748847-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(10301)
default	19:21:24.751337-0500	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1e8048, Nexy(5767), 'prim'', AudioCategory changed to 'Record_WithBluetooth'
default	19:21:24.750500-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(10300)
default	19:21:24.751626-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 73, PID = 5767, Name = sid:0x1e8048, Nexy(5767), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	19:21:24.750706-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:10300 called from <private>
default	19:21:24.750715-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:10300 called from <private>
default	19:21:24.751781-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:10300 called from <private>
default	19:21:24.752238-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=411.1500, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=5767, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=398, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	19:21:24.751866-0500	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 73, PID = 5767, Name = sid:0x1e8048, Nexy(5767), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> is going active
default	19:21:24.751916-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1e8048, Nexy(5767), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 73 starting recording
default	19:21:24.752758-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 73, PID = 5767, Name = sid:0x1e8048, Nexy(5767), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	19:21:24.753482-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 73, PID = 5767, Name = sid:0x1e8048, Nexy(5767), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	19:21:24.751822-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:10300 called from <private>
default	19:21:24.752002-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(10300)
default	19:21:24.752038-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:10300 called from <private>
default	19:21:24.753694-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1e8048, Nexy(5767), 'prim'', displayID:'com.nexy.assistant'}
default	19:21:24.752224-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:10300 called from <private>
default	19:21:24.753912-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [1, 0]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:input"
)}
default	19:21:24.751657-0500	audiomxd	UpdateAudioState CID 0x4D120001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	19:21:24.753922-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	19:21:24.753988-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(10300)
default	19:21:24.754199-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:10300 called from <private>
default	19:21:24.754208-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:10300 called from <private>
default	19:21:24.754285-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:10300 called from <private>
default	19:21:24.754326-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:10300 called from <private>
default	19:21:24.754256-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	19:21:24.754224-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	19:21:24.755390-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:10300 called from <private>
default	19:21:24.755399-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:10300 called from <private>
default	19:21:24.755501-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(10300)
default	19:21:24.755518-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:10300 called from <private>
default	19:21:24.755601-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:10300 called from <private>
default	19:21:24.756197-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(10300)
default	19:21:24.756378-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:10300 called from <private>
default	19:21:24.756386-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:10300 called from <private>
default	19:21:24.756422-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:10300 called from <private>
default	19:21:24.756433-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:10300 called from <private>
default	19:21:24.756611-0500	tccd	AUTHREQ_SUBJECT: msgID=411.1500, subject=com.nexy.assistant,
default	19:21:24.757626-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc79244300 at /Applications/Nexy.app
default	19:21:24.759332-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	19:21:24.760093-0500	runningboardd	Invalidating assertion 403-338-153832 (target:[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767]) from originator [osservice<com.apple.powerd>:338]
default	19:21:24.762042-0500	gamepolicyd	Received state update for 5767 (app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>, running-active-NotVisible
default	19:21:24.772722-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 200 flag 0x1 < Hijack > app com.nexy.assistant CID 0x4D120001 category Not set
default	19:21:24.775614-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	19:21:24.775660-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	19:21:24.777082-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	19:21:24.810022-0500	tccd	AUTHREQ_SUBJECT: msgID=411.1501, subject=com.nexy.assistant,
default	19:21:24.829844-0500	coreaudiod	>>> ADAPT [com.nexy.assistant]
default	19:21:24.831111-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xa380e9b00] Created node ADM::com.nexy.assistant_10301.10209.0_airpods noise suppression studio::in-0 with nodeID 0 - reporting period = 10.000000, sample rate = 24000.000000
default	19:21:24.831181-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xa380e9b00] Created node ADM::com.nexy.assistant_10301.10209.0_airpods noise suppression studio::out-0 with nodeID 1 - reporting period = 10.000000, sample rate = 24000.000000
default	19:21:24.866075-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] Ignoring jetsam update because this process is not memory-managed
default	19:21:24.866087-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] Ignoring suspend because this process is not lifecycle managed
default	19:21:24.866099-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] Ignoring GPU update because this process is not GPU managed
default	19:21:24.866117-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] Ignoring memory limit update because this process is not memory-managed
default	19:21:24.866348-0500	coreaudiod	<<< ADAPT [com.nexy.assistant]
default	19:21:24.869421-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:10301 called from <private>
default	19:21:24.867620-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] from originator [osservice<com.apple.powerd>:338] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:403-338-153835 target:5767 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	19:21:24.869455-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:10301 called from <private>
default	19:21:24.869636-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	19:21:24.867866-0500	runningboardd	Assertion 403-338-153835 (target:[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767]) will be created as active
default	19:21:24.871532-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:10301 called from <private>
default	19:21:24.871646-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(10301)
default	19:21:24.871666-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:10301 called from <private>
default	19:21:24.871673-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:10301 called from <private>
default	19:21:24.872760-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	19:21:24.872972-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	19:21:24.873330-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(10301)
default	19:21:24.873611-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:10301 called from <private>
default	19:21:24.873627-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:10301 called from <private>
default	19:21:24.873644-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:10301 called from <private>
default	19:21:24.875114-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=411.1502, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=5767, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=398, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	19:21:24.876055-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	19:21:24.876353-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] Ignoring jetsam update because this process is not memory-managed
default	19:21:24.876384-0500	tccd	AUTHREQ_SUBJECT: msgID=411.1502, subject=com.nexy.assistant,
default	19:21:24.876508-0500	gamepolicyd	Received state update for 5767 (app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>, running-active-NotVisible
default	19:21:24.876408-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] Ignoring suspend because this process is not lifecycle managed
default	19:21:24.876442-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] Ignoring GPU update because this process is not GPU managed
default	19:21:24.876547-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] Ignoring memory limit update because this process is not memory-managed
default	19:21:24.877129-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc79244300 at /Applications/Nexy.app
default	19:21:24.898233-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:10301 called from <private>
default	19:21:24.898449-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] from originator [osservice<com.apple.powerd>:338] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:403-338-153836 target:5767 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	19:21:24.900602-0500	runningboardd	Assertion 403-338-153836 (target:[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767]) will be created as active
default	19:21:24.905780-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	19:21:24.905857-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	19:21:24.905894-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	19:21:24.906276-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	19:21:24.906287-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	19:21:24.906300-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	19:21:24.906306-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	19:21:24.906316-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	19:21:24.906322-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	19:21:24.906342-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	19:21:24.906393-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	19:21:24.906404-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	19:21:24.906460-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	19:21:24.906492-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	19:21:24.906502-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	19:21:24.906732-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	19:21:24.906847-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	19:21:24.906857-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	19:21:24.906867-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	19:21:24.906873-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	19:21:24.906883-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	19:21:24.906902-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	19:21:24.906913-0500	ControlCenter	Navigating to new application [com.nexy.assistant]
default	19:21:24.982064-0500	gamepolicyd	Received state update for 5767 (app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>, running-active-NotVisible
default	19:21:25.924417-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xa}
default	19:21:25.924964-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1e8048","name":"Nexy(5767)"}, "details":{"deviceUIDs":[],"implicit_category":"","input_running":false,"output_running":false} }
default	19:21:25.925203-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 73, PID = 5767, Name = sid:0x1e8048, Nexy(5767), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	19:21:25.925327-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 73, PID = 5767, Name = sid:0x1e8048, Nexy(5767), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	19:21:25.925400-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1e8048, Nexy(5767), 'prim'', displayID:'com.nexy.assistant'}
default	19:21:25.925510-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	19:21:25.925515-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1e8048, Nexy(5767), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 73 stopping recording
default	19:21:25.925581-0500	audiomxd	-MXCoreSession- -[MXCoreSession endInterruption:]: Session <ID: 73, PID = 5767, Name = sid:0x1e8048, Nexy(5767), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> is going inactive
default	19:21:25.925630-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 73, PID = 5767, Name = sid:0x1e8048, Nexy(5767), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	19:21:25.925718-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 73, PID = 5767, Name = sid:0x1e8048, Nexy(5767), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	19:21:25.925944-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 200 flag 0x1 < Hijack > app com.nexy.assistant CID 0x4D120001 category Not set
default	19:21:25.925893-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 0]. BT device UIDS: {(
)}
default	19:21:25.925908-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	19:21:25.930402-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	19:21:25.929939-0500	runningboardd	Invalidating assertion 403-338-153836 (target:[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767]) from originator [osservice<com.apple.powerd>:338]
default	19:21:25.930438-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	19:21:25.930243-0500	audiomxd	UpdateAudioState CID 0x4D120001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	19:21:25.930463-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	19:21:25.930321-0500	audiomxd	UpdateAudioState CID 0x4D120001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	19:21:25.930485-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	19:21:25.930577-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	19:21:25.930596-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	19:21:25.930613-0500	audioaccessoryd	AudioStateChanged: Removed audio session app com.nexy.assistant 201 count 0
default	19:21:25.932171-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	19:21:25.936152-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	19:21:25.936167-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	19:21:25.936181-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	19:21:25.936187-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	19:21:25.936202-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	19:21:25.936208-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	19:21:25.936340-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	19:21:26.026351-0500	Nexy	                AUHAL.cpp:473   ~AUHAL: (0xbb05c9c40) Selecting device 0 from destructor
default	19:21:26.026371-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0xbb05c9c40)
default	19:21:26.026390-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0xbb05c9c40) not already running
default	19:21:26.026400-0500	Nexy	                AUHAL.cpp:687   SelectDevice: (0xbb05c9c40) disconnecting device 91
default	19:21:26.026407-0500	Nexy	                AUHAL.cpp:751   SelectDevice: (0xbb05c9c40) destroying ioproc 0xa for device 91
default	19:21:26.026446-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xa}
default	19:21:26.026487-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	19:21:26.026676-0500	Nexy	                AUHAL.cpp:853   SelectDevice: (0xbb05c9c40) nothing to setup
default	19:21:26.026688-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0xbb05c9c40) adding 0 device listeners to device 0
default	19:21:26.026694-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0xbb05c9c40) adding 0 device delegate listeners to device 0
default	19:21:26.026701-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0xbb05c9c40) removing 7 device listeners from device 91
default	19:21:26.026921-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0xbb05c9c40) removing 0 device delegate listeners from device 91
default	19:21:26.026937-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0xbb05c9c40)
default	19:21:26.037187-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] Ignoring jetsam update because this process is not memory-managed
default	19:21:26.037201-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] Ignoring suspend because this process is not lifecycle managed
default	19:21:26.037214-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] Ignoring GPU update because this process is not GPU managed
default	19:21:26.037230-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] Ignoring memory limit update because this process is not memory-managed
default	19:21:26.040472-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	19:21:26.041127-0500	gamepolicyd	Received state update for 5767 (app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>, running-active-NotVisible
default	19:21:26.951313-0500	Nexy	[0xbafc99400] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	19:21:26.952265-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=5767.3, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=5767, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	19:21:26.953830-0500	tccd	AUTHREQ_SUBJECT: msgID=5767.3, subject=com.nexy.assistant,
default	19:21:26.954742-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x92f17b300 at /Applications/Nexy.app
default	19:21:26.975199-0500	Nexy	[0xbafc99400] invalidated after the last release of the connection object
default	19:21:26.975559-0500	Nexy	server port 0x00010c23, session port 0x00003713
default	19:21:26.976423-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=397.2636, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=5767, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=397, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	19:21:26.976452-0500	tccd	requestor: TCCDProcess: identifier=com.apple.WindowServer, pid=397, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=5767, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	19:21:26.977349-0500	tccd	AUTHREQ_SUBJECT: msgID=397.2636, subject=com.nexy.assistant,
default	19:21:26.977969-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x92f17b300 at /Applications/Nexy.app
default	19:21:27.004498-0500	kernel	SK[6]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 061FCBEC-C132-4B0D-B216-EECD28B734CD flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.54995,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0x84d997d8 tp_proto=0x06"
default	19:21:27.004570-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:54995<-><IPv4-redacted>:53] interface: utun6 (skipped: 47531)
so_gencnt: 2851624 t_state: SYN_SENT process: Nexy:5767 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 1 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x8b52735e
default	19:21:27.005161-0500	kernel	tcp connected: [<IPv4-redacted>:54995<-><IPv4-redacted>:53] interface: utun6 (skipped: 47531)
so_gencnt: 2851624 t_state: ESTABLISHED process: Nexy:5767 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 1 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x8b52735e
default	19:21:27.005692-0500	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:54995<-><IPv4-redacted>:53] interface: utun6 (skipped: 47531)
so_gencnt: 2851624 t_state: FIN_WAIT_1 process: Nexy:5767 Duration: 0.001 sec Conn_Time: 0.001 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 1.000 ms rttvar: 0.500 ms base rtt: 1 ms so_error: 0 svc/tc: 0 flow: 0x8b52735e
default	19:21:27.005703-0500	kernel	tcp_connection_summary [<IPv4-redacted>:54995<-><IPv4-redacted>:53] interface: utun6 (skipped: 47531)
so_gencnt: 2851624 t_state: FIN_WAIT_1 process: Nexy:5767 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	19:21:27.019223-0500	kernel	SK[7]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 59BCEA42-CA99-439C-8BAA-087B0B729A00 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.54996,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0x764adaea tp_proto=0x06"
default	19:21:27.019264-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:54996<-><IPv4-redacted>:53] interface: utun6 (skipped: 47531)
so_gencnt: 2851625 t_state: SYN_SENT process: Nexy:5767 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 1 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x84400162
default	19:21:27.019403-0500	Nexy	networkd_settings_read_from_file initialized networkd settings by reading plist directly
default	19:21:27.019557-0500	Nexy	networkd_settings_read_from_file initialized networkd settings by reading plist directly
default	19:21:27.019789-0500	kernel	tcp connected: [<IPv4-redacted>:54996<-><IPv4-redacted>:53] interface: utun6 (skipped: 47531)
so_gencnt: 2851625 t_state: ESTABLISHED process: Nexy:5767 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 1 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x84400162
default	19:21:27.019984-0500	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:54996<-><IPv4-redacted>:53] interface: utun6 (skipped: 47531)
so_gencnt: 2851625 t_state: FIN_WAIT_1 process: Nexy:5767 Duration: 0.000 sec Conn_Time: 0.000 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 1.000 ms rttvar: 0.500 ms base rtt: 1 ms so_error: 0 svc/tc: 0 flow: 0x84400162
default	19:21:27.019994-0500	kernel	tcp_connection_summary [<IPv4-redacted>:54996<-><IPv4-redacted>:53] interface: utun6 (skipped: 47531)
so_gencnt: 2851625 t_state: FIN_WAIT_1 process: Nexy:5767 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	19:21:27.020476-0500	Nexy	nw_path_libinfo_path_check [3F7664AB-1207-4C89-9316-8CACE7A93551 IPv4#346cdf38:443 tcp, legacy-socket, attribution: developer]
	libinfo check path: <private>
default	19:21:27.020903-0500	kernel	SK[8]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid D7E0E942-E95E-4799-B985-EB194286406B flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.54997,dst=<IPv4-redacted>.443,proto=0x06 mask=0x0000003f,hash=0xf0b0e705 tp_proto=0x06"
default	19:21:27.020931-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:54997<-><IPv4-redacted>:443] interface: utun6 (skipped: 47531)
so_gencnt: 2851626 t_state: SYN_SENT process: Nexy:5767 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x98f3a352
default	19:21:27.021119-0500	kernel	tcp connected: [<IPv4-redacted>:54997<-><IPv4-redacted>:443] interface: utun6 (skipped: 47531)
so_gencnt: 2851626 t_state: ESTABLISHED process: Nexy:5767 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x98f3a352
default	19:21:27.255629-0500	Nexy	[0xbafc99540] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	19:21:27.256325-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=5767.4, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=5767, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	19:21:27.263111-0500	tccd	AUTHREQ_SUBJECT: msgID=5767.4, subject=com.nexy.assistant,
default	19:21:27.263751-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x92f17aa00 at /Applications/Nexy.app
default	19:21:27.281358-0500	Nexy	[0xbafc99540] invalidated after the last release of the connection object
default	19:21:27.649579-0500	runningboardd	Assertion did invalidate due to timeout: 403-403-153819 (target:[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767])
default	19:21:27.836545-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] Ignoring jetsam update because this process is not memory-managed
default	19:21:27.836569-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] Ignoring suspend because this process is not lifecycle managed
default	19:21:27.836586-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] Ignoring GPU update because this process is not GPU managed
default	19:21:27.836621-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] Ignoring memory limit update because this process is not memory-managed
default	19:21:27.842493-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	19:21:27.843420-0500	gamepolicyd	Received state update for 5767 (app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>, running-active-NotVisible
default	19:21:28.143887-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(10301)
default	19:21:28.143984-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:10301 called from <private>
default	19:21:28.143997-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:10301 called from <private>
default	19:21:28.144539-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(10300)
default	19:21:28.144573-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:10300 called from <private>
default	19:21:28.144587-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:10300 called from <private>
default	19:21:28.157334-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:10300 called from <private>
default	19:21:28.157371-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:10300 called from <private>
default	19:21:28.158129-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(10300)
default	19:21:28.158169-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:10300 called from <private>
default	19:21:28.158179-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:10300 called from <private>
default	19:21:28.160954-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(10300)
default	19:21:28.160991-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(10300)
default	19:21:28.161190-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(10300)
default	19:21:28.161993-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(10300)
default	19:21:28.162699-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(10301)
default	19:21:28.162077-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:10300 called from <private>
default	19:21:28.163448-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:10301 called from <private>
default	19:21:28.163502-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:10300 called from <private>
default	19:21:28.163641-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:10301 called from <private>
default	19:21:28.163846-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:10300 called from <private>
default	19:21:28.164315-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:10300 called from <private>
default	19:21:28.164419-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:10300 called from <private>
default	19:21:28.164539-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:10300 called from <private>
default	19:21:28.164652-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:10300 called from <private>
default	19:21:28.164725-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:10300 called from <private>
default	19:21:28.176161-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:10300 called from <private>
default	19:21:28.176194-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:10300 called from <private>
default	19:21:28.176327-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(10300)
default	19:21:28.183188-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(10300)
default	19:21:28.183543-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:10300 called from <private>
default	19:21:28.183615-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:10300 called from <private>
default	19:21:28.183748-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(10300)
default	19:21:28.187026-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(10300)
default	19:21:28.187537-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:10300 called from <private>
default	19:21:28.187551-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:10300 called from <private>
default	19:21:28.187591-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:10300 called from <private>
default	19:21:28.187598-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:10300 called from <private>
default	19:21:28.187606-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:10300 called from <private>
default	19:21:28.187613-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:10300 called from <private>
default	19:21:28.187787-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:10300 called from <private>
default	19:21:28.187948-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:10300 called from <private>
default	19:21:28.188059-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:10300 called from <private>
default	19:21:28.188188-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:10300 called from <private>
default	19:21:28.188328-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:10300 called from <private>
default	19:21:28.188452-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:10300 called from <private>
default	19:21:28.188630-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:10300 called from <private>
default	19:21:28.188831-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:10300 called from <private>
default	19:21:28.245012-0500	Nexy	[0xbafc997c0] activating connection: mach=true listener=false peer=false name=com.apple.usernoted.client
default	19:21:28.260006-0500	usernoted	Connection com.nexy.assistant with path: /Applications/Nexy.app
default	19:21:28.269073-0500	distnoted	register name: com.apple.nsquiet_safe_quit_give_reason object: com.nexy.assistant token: 2300000021 pid: 5767
default	19:21:28.282713-0500	Nexy	NSApp cache appearance:
-NSRequiresAquaSystemAppearance: 0
-appearance: (null)
-effectiveAppearance: <NSCompositeAppearance: 0xbb15746e0
 (
    "<NSDarkAquaAppearance: 0xbb1574820>",
    "<NSSystemAppearance: 0xbb1574640>"
)>
default	19:21:28.289514-0500	Nexy	[0xbafc99cc0] activating connection: mach=true listener=false peer=false name=com.apple.dock.fullscreen
default	19:21:28.292469-0500	Nexy	[0xbafc99e00] activating connection: mach=true listener=false peer=false name=com.apple.fonts
default	19:21:28.295337-0500	Nexy	(<private>) deleteSearchableItemsWithDomainIdentifiers, protectionClass:(null), domainIdentifiers number:1
default	19:21:28.295650-0500	Nexy	sConnectionName: com.apple.spotlight.IndexAgent
default	19:21:28.295663-0500	Nexy	Start service name com.apple.spotlight.IndexAgent
default	19:21:28.295694-0500	Nexy	[0xbafc99f40] activating connection: mach=true listener=false peer=false name=com.apple.spotlight.IndexAgent
default	19:21:28.296668-0500	suggestd	SGDSpotlightReceiver: deleting 1 domain identifiers (1 after removing overlaps) for com.nexy.assistant: <private>
default	19:21:28.299494-0500	Nexy	[C:1] Alloc com.apple.controlcenter.statusitems
default	19:21:28.299571-0500	Nexy	[0xbafc9a080] activating connection: mach=false listener=false peer=false name=(anonymous)
default	19:21:28.299642-0500	Nexy	FBSWorkspace registering source: <private>
default	19:21:28.301062-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	19:21:28.301259-0500	Nexy	<FBSWorkspaceScenesClient:0xbb15763a0 <private>> attempting immediate handshake from activate
default	19:21:28.301320-0500	Nexy	<FBSWorkspaceScenesClient:0xbb15763a0 <private>> sent handshake
default	19:21:28.301789-0500	Nexy	Realizing settings extension __NSStatusItemSceneHostSettings__ on FBSSceneSettings
default	19:21:28.302361-0500	Nexy	Realizing settings extension __NSStatusItemSceneClientSettings__ on FBSSceneClientSettings
default	19:21:28.301992-0500	ControlCenter	Asked to bootstrap a new process for handle: [app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767]
default	19:21:28.302449-0500	ControlCenter	Creating process (sync=true) for handle: [app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767]
default	19:21:28.303127-0500	ControlCenter	[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D>:5767] Registering event dispatcher at init
default	19:21:28.303483-0500	Nexy	Realizing settings extension FBSSceneSettingsCore on FBSSceneSettings
default	19:21:28.304090-0500	ControlCenter	Created <FBWorkspace: 0x9755970c0; <FBApplicationProcess: 0x971d3b780; app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D>:5767(v1A7FCF)>>
default	19:21:28.304111-0500	ControlCenter	Bootstrapping app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D> with intent background
default	19:21:28.304487-0500	runningboardd	Launch request for app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>[0] is using uid 501 (divined from auid 501 euid 501)
default	19:21:28.304637-0500	runningboardd	Acquiring assertion targeting app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)> from originator [osservice<com.apple.controlcenter(501)>:642] with description <RBSAssertionDescriptor| "FBApplicationProcess" ID:403-642-153842 target:app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)> attributes:[
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableLPRunReason-Suspend" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableRole-NonUI" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableJetsamPriority-Active" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableBootstrapping" sourceEnvironment:"(null)">
	]>
default	19:21:28.304816-0500	runningboardd	Assertion 403-642-153842 (target:app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>) will be created as active
default	19:21:28.304851-0500	runningboardd	setting abstract target for <RBSAssertionDescriptor| "FBApplicationProcess" ID:403-642-153842 target:app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)> attributes:[
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableLPRunReason-Suspend" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableRole-NonUI" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableJetsamPriority-Active" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableBootstrapping" sourceEnvironment:"(null)">
	]> to [app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767]
default	19:21:28.305154-0500	Nexy	Realizing settings extension FBSSceneClientSettingsCore on FBSSceneClientSettings
default	19:21:28.305222-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] Ignoring jetsam update because this process is not memory-managed
default	19:21:28.305237-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] Ignoring suspend because this process is not lifecycle managed
default	19:21:28.305248-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] Ignoring GPU update because this process is not GPU managed
default	19:21:28.305269-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] Ignoring memory limit update because this process is not memory-managed
default	19:21:28.306246-0500	Nexy	Requesting scene <FBSScene: 0xbb1576760; com.apple.controlcenter:9D7A84EB-09FA-419F-B4B9-E26DC2689304> from com.apple.controlcenter.statusitems
default	19:21:28.308238-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	19:21:28.308505-0500	Nexy	Request for <FBSScene: 0xbb1576760; com.apple.controlcenter:9D7A84EB-09FA-419F-B4B9-E26DC2689304> complete!
default	19:21:28.308604-0500	Nexy	Realizing settings extension FBSSceneTransitionContextCore on FBSSceneTransitionContext
default	19:21:28.309056-0500	gamepolicyd	Received state update for 5767 (app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>, running-active-NotVisible
default	19:21:28.310089-0500	Nexy	Realizing settings extension __NSHostedViewSceneSettings__ on FBSSceneSettings
default	19:21:28.310331-0500	Nexy	Realizing settings extension __NSClientHostedViewSceneSettings__ on FBSSceneClientSettings
default	19:21:28.310563-0500	Nexy	Realizing settings extension __NSStatusItemAuxiliaryViewSceneSettings__ on FBSSceneSettings
default	19:21:28.310604-0500	Nexy	Realizing settings extension __NSClientStatusItemAuxiliaryViewSceneSettings__ on FBSSceneClientSettings
default	19:21:28.310868-0500	Nexy	Requesting scene <FBSScene: 0xbb15768a0; com.apple.controlcenter:9D7A84EB-09FA-419F-B4B9-E26DC2689304-Aux[1]-NSStatusItemView> from com.apple.controlcenter.statusitems
default	19:21:28.311062-0500	Nexy	Request for <FBSScene: 0xbb15768a0; com.apple.controlcenter:9D7A84EB-09FA-419F-B4B9-E26DC2689304-Aux[1]-NSStatusItemView> complete!
default	19:21:28.311361-0500	ControlCenter	[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D>:5767] Bootstrap success!
default	19:21:28.311852-0500	ControlCenter	[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D>:5767] Setting process visibility to: Background
default	19:21:28.312107-0500	ControlCenter	[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D>:5767] No launch watchdog for this process, dropping initial assertion in 2.0s
default	19:21:28.312766-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] from originator [osservice<com.apple.controlcenter(501)>:642] with description <RBSAssertionDescriptor| "FBWorkspaceDomain: injecting saved endowment" ID:403-642-153843 target:5767 attributes:[
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"WorkspaceEndpointInjection" sourceEnvironment:"(null)">
	]>
default	19:21:28.312841-0500	runningboardd	Assertion 403-642-153843 (target:[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767]) will be created as active
default	19:21:28.313210-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] Ignoring jetsam update because this process is not memory-managed
default	19:21:28.313221-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] Ignoring suspend because this process is not lifecycle managed
default	19:21:28.313232-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] Ignoring GPU update because this process is not GPU managed
default	19:21:28.313251-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] Ignoring memory limit update because this process is not memory-managed
default	19:21:28.316076-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	19:21:28.316514-0500	Nexy	[com.apple.controlcenter:9D7A84EB-09FA-419F-B4B9-E26DC2689304-Aux[1]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
default	19:21:28.316665-0500	ControlCenter	Adding: <FBApplicationProcess: 0x971d3b780; app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D>:5767(v1A7FCF)>
default	19:21:28.316533-0500	Nexy	[com.apple.controlcenter:9D7A84EB-09FA-419F-B4B9-E26DC2689304-Aux[1]-NSStatusItemView] Dropping transition context because the scene is reconnecting
default	19:21:28.317089-0500	gamepolicyd	Received state update for 5767 (app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>, running-active-NotVisible
default	19:21:28.317305-0500	ControlCenter	[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D>:5767] Connection established.
default	19:21:28.317399-0500	ControlCenter	[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D>:5767] created proxy of <BSXPCServiceConnectionProxy<FBSWorkspaceServiceServerInterface>: 0x971b5a220>
default	19:21:28.317441-0500	ControlCenter	Received state update for 5767 (app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>, running-active-NotVisible
default	19:21:28.317442-0500	ControlCenter	[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D>:5767] Connection to remote process established!
default	19:21:28.321655-0500	Nexy	[com.apple.controlcenter:9D7A84EB-09FA-419F-B4B9-E26DC2689304-Aux[1]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
default	19:21:28.321674-0500	Nexy	[com.apple.controlcenter:9D7A84EB-09FA-419F-B4B9-E26DC2689304-Aux[1]-NSStatusItemView] Dropping transition context because the scene is reconnecting
default	19:21:28.321768-0500	Nexy	Warning: the app is using `-[NSStatusBarButton setHighlightsBy:]` to set the highlight behavior. Instead, consider removing that setting. That will enable macOS to highlight the status bar button as appropriate for all configurations (e.g., light, dark, and increased contrast modes).
default	19:21:28.324672-0500	ControlCenter	Asked to bootstrap a new process for handle: [app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767]
default	19:21:28.324691-0500	ControlCenter	A process already exists for this handle: <FBApplicationProcess: 0x971d3b780; app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D>:5767(v1A7FCF)>
default	19:21:28.324793-0500	ControlCenter	[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D>:5767] Registered new scene: <FBWorkspaceScene: 0x97447e340; com.apple.controlcenter:9D7A84EB-09FA-419F-B4B9-E26DC2689304> (fromRemnant = 0)
default	19:21:28.324820-0500	ControlCenter	[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D>:5767] Workspace interruption policy did change: reconnect
default	19:21:28.325006-0500	ControlCenter	[com.apple.controlcenter:9D7A84EB-09FA-419F-B4B9-E26DC2689304] Client process connected: [app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767]
default	19:21:28.325012-0500	Nexy	Request for <FBSScene: 0xbb1576760; com.apple.controlcenter:9D7A84EB-09FA-419F-B4B9-E26DC2689304> complete!
default	19:21:28.325064-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] from originator [osservice<com.apple.controlcenter(501)>:642] with description <RBSAssertionDescriptor| "com.apple.frontboard.after-life.interrupted" ID:403-642-153844 target:5767 attributes:[
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"AfterLife-Interrupted" sourceEnvironment:"(null)">
	]>
default	19:21:28.325138-0500	runningboardd	Assertion 403-642-153844 (target:[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767]) will be created as inactive as originator process has not exited
default	19:21:28.325447-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] from originator [osservice<com.apple.controlcenter(501)>:642] with description <RBSAssertionDescriptor| "FBWorkspace (BG-Active[40])" ID:403-642-153845 target:5767 attributes:[
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableLPRunReason-Suspend" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableRole-NonUI" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableJetsamPriority-Active" sourceEnvironment:"(null)">
	]>
default	19:21:28.325541-0500	runningboardd	Assertion 403-642-153845 (target:[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767]) will be created as active
default	19:21:28.325623-0500	ControlCenter	[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D>:5767] Workspace state did change: XX-None[0] --> BG-Active[40] (assertion acquired).
default	19:21:28.325776-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] Ignoring jetsam update because this process is not memory-managed
default	19:21:28.325786-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] Ignoring suspend because this process is not lifecycle managed
default	19:21:28.325794-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] Ignoring GPU update because this process is not GPU managed
default	19:21:28.325886-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] Ignoring memory limit update because this process is not memory-managed
default	19:21:28.326122-0500	ControlCenter	Asked to bootstrap a new process for handle: [app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767]
default	19:21:28.326139-0500	ControlCenter	A process already exists for this handle: <FBApplicationProcess: 0x971d3b780; app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D>:5767(v1A7FCF)>
default	19:21:28.326198-0500	ControlCenter	[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D>:5767] Registered new scene: <FBWorkspaceScene: 0x97447f180; com.apple.controlcenter:9D7A84EB-09FA-419F-B4B9-E26DC2689304-Aux[1]-NSStatusItemView> (fromRemnant = 0)
default	19:21:28.326190-0500	Nexy	<FBSWorkspaceScenesClient:0xbb15763a0 <private>> Reconnecting scene com.apple.controlcenter:9D7A84EB-09FA-419F-B4B9-E26DC2689304
default	19:21:28.326337-0500	ControlCenter	[com.apple.controlcenter:9D7A84EB-09FA-419F-B4B9-E26DC2689304-Aux[1]-NSStatusItemView] Client process connected: [app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767]
default	19:21:28.326390-0500	Nexy	Request for <FBSScene: 0xbb15768a0; com.apple.controlcenter:9D7A84EB-09FA-419F-B4B9-E26DC2689304-Aux[1]-NSStatusItemView> complete!
default	19:21:28.326652-0500	Nexy	<FBSWorkspaceScenesClient:0xbb15763a0 <private>> Reconnecting scene com.apple.controlcenter:9D7A84EB-09FA-419F-B4B9-E26DC2689304-Aux[1]-NSStatusItemView
default	19:21:28.328422-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	19:21:28.328805-0500	ControlCenter	Received state update for 5767 (app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>, running-active-NotVisible
default	19:21:28.328985-0500	gamepolicyd	Received state update for 5767 (app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>, running-active-NotVisible
default	19:21:28.338059-0500	Nexy	Registering for test daemon availability notify post.
default	19:21:28.338196-0500	Nexy	notify_get_state check indicated test daemon not ready.
default	19:21:28.338273-0500	Nexy	notify_get_state check indicated test daemon not ready.
default	19:21:28.338365-0500	Nexy	notify_get_state check indicated test daemon not ready.
default	19:21:28.339601-0500	Nexy	[0xbafc9a440] activating connection: mach=true listener=false peer=false name=com.apple.coreservices.appleevents
default	19:21:28.342232-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x92f179500 at /Applications/Nexy.app
default	19:21:28.347026-0500	Nexy	[0xbafc983c0] Connection returned listener port: 0x4503
default	19:21:28.347517-0500	Nexy	SignalReady: pid=5767 asn=0x0-0x3b53b5
default	19:21:28.347939-0500	Nexy	SIGNAL: pid=5767 asn=0x0x-0x3b53b5
default	19:21:28.348597-0500	loginwindow	-[Application updateInformation] | Got App URL: file:///Applications/Nexy.app/
default	19:21:28.358413-0500	Nexy	[com.apple.controlcenter:9D7A84EB-09FA-419F-B4B9-E26DC2689304-Aux[1]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
default	19:21:28.361011-0500	Nexy	[com.apple.controlcenter:9D7A84EB-09FA-419F-B4B9-E26DC2689304-Aux[1]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
default	19:21:28.362564-0500	Nexy	void _NSDisableAutomaticTerminationAndLog(NSString *) Restoring windows
default	19:21:28.362571-0500	Nexy	-[NSApplication _reopenWindowsAsNecessaryIncludingRestorableState:withFullFidelity:completionHandler:] shouldRestoreState=1 hasPersistentStateToRestore=0 shouldStillRestoreStateAfterPrompting=0
default	19:21:28.362588-0500	Nexy	[0xbafc99400] activating connection: mach=true listener=false peer=false name=com.apple.window_proxies
default	19:21:28.362662-0500	Nexy	[0xbafc99400] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	19:21:28.363568-0500	Nexy	void _NSEnableAutomaticTerminationAndLog(NSString *) Restoring windows
default	19:21:28.365578-0500	Nexy	[C:2] Alloc <private>
default	19:21:28.365608-0500	Nexy	[0xbafc99400] activating connection: mach=false listener=false peer=false name=(anonymous)
default	19:21:28.367160-0500	ControlCenter	Host properties initialized; (bid:com.nexy.assistant-Item-0-5767). State(applicationItem: true, clientRequestsVisibility: true, neverClip: false)
default	19:21:28.367470-0500	WindowManager	Connection activated | (5767) Nexy
default	19:21:28.367556-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] from originator [app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] with description <RBSAssertionDescriptor| "AudioHAL" ID:403-5767-153846 target:5767 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	19:21:28.367619-0500	runningboardd	Assertion 403-5767-153846 (target:[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767]) will be created as active
default	19:21:28.367918-0500	runningboardd	Invalidating assertion 403-5767-153846 (target:[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767]) from originator [app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767]
default	19:21:28.367954-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] Ignoring jetsam update because this process is not memory-managed
default	19:21:28.367966-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] Ignoring suspend because this process is not lifecycle managed
default	19:21:28.367978-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] Ignoring GPU update because this process is not GPU managed
default	19:21:28.368048-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] Ignoring memory limit update because this process is not memory-managed
default	19:21:28.368103-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] from originator [app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] with description <RBSAssertionDescriptor| "AudioHAL" ID:403-5767-153847 target:5767 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	19:21:28.368174-0500	runningboardd	Assertion 403-5767-153847 (target:[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767]) will be created as active
default	19:21:28.368976-0500	ControlCenter	Starting to track host; (bid:com.nexy.assistant-Item-0-5767)
default	19:21:28.369498-0500	ControlCenter	Created new displayable type DisplayableAppStatusItemType(85E530BE, (bid:com.nexy.assistant-Item-0-5767)) for (bid:com.nexy.assistant-Item-0-5767)
default	19:21:28.370614-0500	ControlCenter	Adding displayable items for status items; [(bid:com.nexy.assistant-Item-0-5767)]
default	19:21:28.370651-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	19:21:28.370867-0500	runningboardd	Invalidating assertion 403-5767-153847 (target:[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767]) from originator [app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767]
default	19:21:28.371099-0500	ControlCenter	Received state update for 5767 (app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>, running-active-NotVisible
default	19:21:28.371202-0500	gamepolicyd	Received state update for 5767 (app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>, running-active-NotVisible
default	19:21:28.371300-0500	ControlCenter	Created instance DisplayableId(DF988196) in .menuBar for DisplayableAppStatusItemType(85E530BE, (bid:com.nexy.assistant-Item-0-5767)) .menuBar
default	19:21:28.371092-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] from originator [app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] with description <RBSAssertionDescriptor| "AudioHAL" ID:403-5767-153848 target:5767 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	19:21:28.371176-0500	runningboardd	Assertion 403-5767-153848 (target:[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767]) will be created as active
default	19:21:28.371586-0500	runningboardd	Invalidating assertion 403-5767-153848 (target:[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767]) from originator [app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767]
default	19:21:28.371695-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] from originator [app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] with description <RBSAssertionDescriptor| "AudioHAL" ID:403-5767-153849 target:5767 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	19:21:28.371731-0500	runningboardd	Assertion 403-5767-153849 (target:[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767]) will be created as active
default	19:21:28.371948-0500	runningboardd	Invalidating assertion 403-5767-153849 (target:[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767]) from originator [app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767]
default	19:21:28.375449-0500	Nexy	[com.apple.controlcenter:9D7A84EB-09FA-419F-B4B9-E26DC2689304-Aux[1]-NSStatusItemView] Received action(s) in scene-update: NSSceneFenceAction
default	19:21:28.376323-0500	ControlCenter	Created ephemaral instance DisplayableId(DF988196) for (bid:com.nexy.assistant-Item-0-5767) with positioning .ephemeral
default	19:21:28.376729-0500	Nexy	[com.apple.controlcenter:9D7A84EB-09FA-419F-B4B9-E26DC2689304-Aux[1]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
error	19:21:28.377208-0500	Nexy	It's not legal to call -layoutSubtreeIfNeeded on a view which is already being laid out.  If you are implementing the view's -layout method, you can call -[super layout] instead.  Break on void _NSDetectedLayoutRecursion(void) to debug.  This will be logged only once.  This may break in the future.
default	19:21:28.377319-0500	Nexy	[com.apple.controlcenter:9D7A84EB-09FA-419F-B4B9-E26DC2689304-Aux[1]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
default	19:21:28.379432-0500	Nexy	[com.apple.controlcenter:9D7A84EB-09FA-419F-B4B9-E26DC2689304] Sending action(s) in update: NSSceneFenceAction
default	19:21:28.471138-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] Ignoring jetsam update because this process is not memory-managed
default	19:21:28.471155-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] Ignoring suspend because this process is not lifecycle managed
default	19:21:28.471168-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] Ignoring GPU update because this process is not GPU managed
default	19:21:28.471184-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] Ignoring memory limit update because this process is not memory-managed
default	19:21:28.474344-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	19:21:28.474791-0500	ControlCenter	Received state update for 5767 (app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>, running-active-NotVisible
default	19:21:28.474833-0500	gamepolicyd	Received state update for 5767 (app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>, running-active-NotVisible
default	19:21:28.478665-0500	Nexy	*warn* MailCS ======%%% _setMailMessageAttributes skip:1
default	19:21:28.482844-0500	Nexy	Start service name com.apple.spotlightknowledged
default	19:21:28.483525-0500	Nexy	[GMS] availability notification token 86
default	19:21:28.586276-0500	ControlCenter	[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D>:5767] Workspace state did change: BG-Active[40] --> XX-None[0] (assertion dropped).
default	19:21:28.586371-0500	runningboardd	Invalidating assertion 403-642-153845 (target:[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767]) from originator [osservice<com.apple.controlcenter(501)>:642]
default	19:21:28.682184-0500	kernel	udp connect: [<IPv4-redacted>:55840<-><IPv4-redacted>:443] interface:  (skipped: 0)
so_gencnt: 2851634 so_state: 0x0002 process: Nexy:5767 bytes in/out: 0/0 pkts in/out: 0/0 error: 0 so_error: 0 svc/tc: 0 flow: 0xbf49cb02
default	19:21:28.682209-0500	kernel	udp_connection_summary [<IPv4-redacted>:55840<-><IPv4-redacted>:443] interface:  (skipped: 0)
so_gencnt: 2851634 so_state: 0x0002 process: Nexy:5767 Duration: 0.000 sec Conn_Time: 0.000 sec bytes in/out: 0/0 pkts in/out: 0/0 rxnospace pkts/bytes: 0/0 so_error: 0 svc/tc: 0 flow: 0xbf49cb02 flowctl: 0us (0x)
default	19:21:28.684505-0500	kernel	SK[1]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 4AC0475A-0C9E-4CE5-9EE1-5EADE95DDC70 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.55003,dst=<IPv4-redacted>.443,proto=0x06 mask=0x0000003f,hash=0xdec0168f tp_proto=0x06"
default	19:21:28.684578-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:55003<-><IPv4-redacted>:443] interface: utun6 (skipped: 47531)
so_gencnt: 2851636 t_state: SYN_SENT process: Nexy:5767 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 1 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x8fe408ff
default	19:21:28.685012-0500	kernel	tcp connected: [<IPv4-redacted>:55003<-><IPv4-redacted>:443] interface: utun6 (skipped: 47531)
so_gencnt: 2851636 t_state: ESTABLISHED process: Nexy:5767 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 1 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x8fe408ff
default	19:21:28.695841-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] Ignoring jetsam update because this process is not memory-managed
default	19:21:28.695862-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] Ignoring suspend because this process is not lifecycle managed
default	19:21:28.695874-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] Ignoring GPU update because this process is not GPU managed
default	19:21:28.695930-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] Ignoring memory limit update because this process is not memory-managed
default	19:21:28.699068-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	19:21:28.699487-0500	ControlCenter	Received state update for 5767 (app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>, running-active-NotVisible
default	19:21:28.699666-0500	gamepolicyd	Received state update for 5767 (app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>, running-active-NotVisible
default	19:21:28.869302-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] from originator [osservice<com.apple.WindowServer(88)>:397] with description <RBSAssertionDescriptor| "AppDrawing" ID:403-397-153851 target:5767 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"AppDrawing" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	19:21:28.869508-0500	runningboardd	Assertion 403-397-153851 (target:[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767]) will be created as active
default	19:21:28.870210-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] Ignoring jetsam update because this process is not memory-managed
default	19:21:28.870239-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] Ignoring suspend because this process is not lifecycle managed
default	19:21:28.870259-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] Ignoring GPU update because this process is not GPU managed
default	19:21:28.870302-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] Ignoring memory limit update because this process is not memory-managed
default	19:21:28.875982-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	19:21:28.876559-0500	ControlCenter	Received state update for 5767 (app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>, running-active-NotVisible
default	19:21:28.876768-0500	gamepolicyd	Received state update for 5767 (app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>, running-active-NotVisible
default	19:21:28.939624-0500	kernel	udp connect: [<IPv4-redacted>:61800<-><IPv4-redacted>:443] interface:  (skipped: 0)
so_gencnt: 2851637 so_state: 0x0002 process: Nexy:5767 bytes in/out: 0/0 pkts in/out: 0/0 error: 0 so_error: 0 svc/tc: 0 flow: 0xb8e1171a
default	19:21:28.939645-0500	kernel	udp_connection_summary [<IPv4-redacted>:61800<-><IPv4-redacted>:443] interface:  (skipped: 0)
so_gencnt: 2851637 so_state: 0x0002 process: Nexy:5767 Duration: 0.000 sec Conn_Time: 0.000 sec bytes in/out: 0/0 pkts in/out: 0/0 rxnospace pkts/bytes: 0/0 so_error: 0 svc/tc: 0 flow: 0xb8e1171a flowctl: 0us (0x)
default	19:21:28.940001-0500	kernel	SK[8]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 4B364C3A-7ADD-4555-B1CF-830A1CF11C00 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.55004,dst=<IPv4-redacted>.443,proto=0x06 mask=0x0000003f,hash=0xd6a34a1d tp_proto=0x06"
default	19:21:28.940054-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:55004<-><IPv4-redacted>:443] interface: utun6 (skipped: 47531)
so_gencnt: 2851638 t_state: SYN_SENT process: Nexy:5767 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 1 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xb7f498d0
default	19:21:28.940696-0500	kernel	tcp connected: [<IPv4-redacted>:55004<-><IPv4-redacted>:443] interface: utun6 (skipped: 47531)
so_gencnt: 2851638 t_state: ESTABLISHED process: Nexy:5767 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 1 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xb7f498d0
default	19:21:28.944303-0500	Nexy	                AUHAL.cpp:420   AUHAL: (0xbb05cb840) Selecting device 85 from constructor
default	19:21:28.944317-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0xbb05cb840)
default	19:21:28.944324-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0xbb05cb840) not already running
default	19:21:28.944328-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0xbb05cb840) nothing to teardown
default	19:21:28.944331-0500	Nexy	                AUHAL.cpp:762   SelectDevice: (0xbb05cb840) connecting device 85
default	19:21:28.944425-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0xbb05cb840) Device ID: 85 (Input:No | Output:Yes): true
default	19:21:28.944545-0500	Nexy	                AUHAL.cpp:774   SelectDevice: (0xbb05cb840) created ioproc 0xb for device 85
default	19:21:28.944644-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0xbb05cb840) adding 7 device listeners to device 85
default	19:21:28.944801-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0xbb05cb840) adding 0 device delegate listeners to device 85
default	19:21:28.944811-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0xbb05cb840)
default	19:21:28.944880-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  48000 Hz, Float32, interleaved
default	19:21:28.944889-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	19:21:28.944895-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	19:21:28.944902-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	19:21:28.944911-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	19:21:28.944994-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0xbb05cb840) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	19:21:28.945003-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0xbb05cb840) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	19:21:28.945008-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	19:21:28.945012-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0xbb05cb840) removing 0 device listeners from device 0
default	19:21:28.945015-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0xbb05cb840) removing 0 device delegate listeners from device 0
default	19:21:28.945019-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0xbb05cb840)
default	19:21:28.945030-0500	Nexy	                AUHAL.cpp:2303  SetProperty: (0xbb05cb840) caller requesting device change from 85 to 85
default	19:21:28.945035-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0xbb05cb840)
default	19:21:28.945041-0500	Nexy	                AUHAL.cpp:664   SelectDevice: <- (0xbb05cb840) exiting with nothing to do
default	19:21:28.945522-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	19:21:28.945766-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	19:21:28.947159-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] from originator [app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] with description <RBSAssertionDescriptor| "AudioHAL" ID:403-5767-153852 target:5767 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	19:21:28.947247-0500	runningboardd	Assertion 403-5767-153852 (target:[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767]) will be created as active
default	19:21:28.948205-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] Ignoring jetsam update because this process is not memory-managed
default	19:21:28.948218-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] Ignoring suspend because this process is not lifecycle managed
default	19:21:28.948229-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] Ignoring GPU update because this process is not GPU managed
default	19:21:28.948249-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] Ignoring memory limit update because this process is not memory-managed
default	19:21:28.948604-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] from originator [osservice<com.apple.powerd>:338] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:403-338-153853 target:5767 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	19:21:28.948674-0500	runningboardd	Assertion 403-338-153853 (target:[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767]) will be created as active
default	19:21:28.951823-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	19:21:28.952110-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] Ignoring jetsam update because this process is not memory-managed
default	19:21:28.952121-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] Ignoring suspend because this process is not lifecycle managed
default	19:21:28.952130-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] Ignoring GPU update because this process is not GPU managed
default	19:21:28.952147-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] Ignoring memory limit update because this process is not memory-managed
default	19:21:28.956784-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	19:21:28.976984-0500	ControlCenter	Received state update for 5767 (app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>, running-active-NotVisible
default	19:21:28.977108-0500	gamepolicyd	Received state update for 5767 (app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>, running-active-NotVisible
default	19:21:29.245277-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xb}
default	19:21:29.246295-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1e8048","name":"Nexy(5767)"}, "details":{"deviceUIDs":["1C-77-54-18-C8-A3:output"],"implicit_category":"MediaPlayback","input_running":false,"output_running":true} }
default	19:21:29.246408-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 73, PID = 5767, Name = sid:0x1e8048, Nexy(5767), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	19:21:29.246444-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Category/Mode changed -- The score for sid:0x1e8048, Nexy(5767), 'prim'/com.nexy.assistant was not correct. Old score = 201
default	19:21:29.246476-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 73, PID = 5767, Name = sid:0x1e8048, Nexy(5767), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	19:21:29.246515-0500	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1e8048, Nexy(5767), 'prim'', AudioCategory changed to 'MediaPlayback'
default	19:21:29.246572-0500	audiomxd	UpdateAudioState CID 0x4D120001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	19:21:29.246601-0500	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 73, PID = 5767, Name = sid:0x1e8048, Nexy(5767), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO> is going active
default	19:21:29.246634-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsPlaying:]: MXCoreSession com.nexy.assistant with category/mode MediaPlayback/Default and coreSessionID = 73 starting playing
default	19:21:29.246793-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 73, PID = 5767, Name = sid:0x1e8048, Nexy(5767), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	19:21:29.246854-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	19:21:29.246850-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 73, PID = 5767, Name = sid:0x1e8048, Nexy(5767), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO>
default	19:21:29.246932-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	19:21:29.246938-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1e8048, Nexy(5767), 'prim'', displayID:'com.nexy.assistant'}
default	19:21:29.247000-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Will try to see if we can get the shared route for session = <ID: 73, PID = 5767, Name = sid:0x1e8048, Nexy(5767), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO>. Old (200) and New (201) scores.
default	19:21:29.247117-0500	audiomxd	AudioApplicationInfoImpl.mm:395   Successfully updated session 0x1e8048 to isSessionRecording: 0
	app: {"name":"[implicit] Nexy","pid":5767}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1e8048, sessionType: 'prim', isRecording: false }, 
]
default	19:21:29.247215-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 201, deviceID = <private>
default	19:21:29.247421-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 1]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)}
default	19:21:29.247467-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 201 flag 0x1 < Hijack > app com.nexy.assistant CID 0x4D120001 category Not set
default	19:21:29.247447-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	19:21:29.249253-0500	audiomxd	UpdateAudioState CID 0x4D120001 audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	19:21:29.249454-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 201,
}
default	19:21:29.249483-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	19:21:29.249499-0500	audioaccessoryd	AudioStateChanged: Added audio session app com.nexy.assistant NULL -> 201 count 1
default	19:21:29.249509-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 201
error	19:21:29.249522-0500	audioaccessoryd	Updating local audio category 100 -> 201 app com.nexy.assistant
default	19:21:29.249685-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.nexy.assistant
default	19:21:29.252208-0500	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:55003<-><IPv4-redacted>:443] interface: utun6 (skipped: 47531)
so_gencnt: 2851636 t_state: FIN_WAIT_1 process: Nexy:5767 Duration: 0.568 sec Conn_Time: 0.001 sec bytes in/out: 2065/465 pkts in/out: 2/4 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 1.000 ms rttvar: 0.187 ms base rtt: 1 ms so_error: 0 svc/tc: 0 flow: 0x8fe408ff
default	19:21:29.252229-0500	kernel	tcp_connection_summary [<IPv4-redacted>:55003<-><IPv4-redacted>:443] interface: utun6 (skipped: 47531)
so_gencnt: 2851636 t_state: FIN_WAIT_1 process: Nexy:5767 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	19:21:29.518604-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Output {1C-77-54-18-C8-A3:output, 0xb}
default	19:21:29.519045-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1e8048","name":"Nexy(5767)"}, "details":{"deviceUIDs":[],"implicit_category":"","input_running":false,"output_running":false} }
default	19:21:29.519186-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsPlaying:]: MXCoreSession com.nexy.assistant with category/mode MediaPlayback/Default and coreSessionID = 73 stopping playing
default	19:21:29.519273-0500	audiomxd	-MXCoreSession- -[MXCoreSession endInterruption:]: Session <ID: 73, PID = 5767, Name = sid:0x1e8048, Nexy(5767), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> is going inactive
default	19:21:29.519340-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 73, PID = 5767, Name = sid:0x1e8048, Nexy(5767), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	19:21:29.519433-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 73, PID = 5767, Name = sid:0x1e8048, Nexy(5767), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	19:21:29.519541-0500	audiomxd	UpdateAudioState CID 0x4D120001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	19:21:29.519622-0500	audiomxd	AudioApplicationInfoImpl.mm:395   Successfully updated session 0x1e8048 to isSessionRecording: 0
	app: {"name":"[implicit] Nexy","pid":5767}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1e8048, sessionType: 'prim', isRecording: false }, 
]
default	19:21:29.519716-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 0]. BT device UIDS: {(
)}
default	19:21:29.519738-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	19:21:29.519778-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	19:21:29.519850-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	19:21:29.519887-0500	audioaccessoryd	AudioStateChanged: Removed audio session app com.nexy.assistant 201 count 0
default	19:21:29.524324-0500	runningboardd	Invalidating assertion 403-5767-153852 (target:[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767]) from originator [app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767]
default	19:21:29.524482-0500	runningboardd	Invalidating assertion 403-338-153853 (target:[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767]) from originator [osservice<com.apple.powerd>:338]
default	19:21:29.529783-0500	coreaudiod	Sending message. { reporterID=24769076396035, category=IO, type=error, message=["HostApplicationDisplayID": Optional(com.nexy.assistant), "io_frame_counter": Optional(11776), "is_recovering": Optional(0), "wg_total_wakeups": Optional(5), "io_cycle_usage": Optional(1), "output_device_source_list": Optional(Unknown), "wg_cycles": Optional(1359494), "num_continuous_silent_io_cycles": Optional(11), "wg_system_time_mach": Optional(3223), "other_active_clients": Optional([  ]), "wg_user_time_mach": Optional(14184), "smallest_buffer_frame_size": Optional(2147483647), "safety_violation_sample_gap": Optional(843), "io_page_faults_duration": Optional(0), "num_continuous_nonzero_io_cycles": Optional(0), "io_cycle_budget": Optional(11354166), "io_page_faults": Optional(0), "multi_cycle_io_page_faults": Optional(0), "wg_external_wakeups": Optional(3), "output_device_transport_list": Optional(Bluetooth), "reporting_latency": Optional(27153166), "other_page_faults": Optional(0), "wg_instructions": Optional(796626), "HAL_client_IO_duration": Optional(27999500), "<…> }
default	19:21:29.626404-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] Ignoring jetsam update because this process is not memory-managed
default	19:21:29.626437-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] Ignoring suspend because this process is not lifecycle managed
default	19:21:29.626461-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] Ignoring GPU update because this process is not GPU managed
default	19:21:29.626507-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] Ignoring memory limit update because this process is not memory-managed
default	19:21:29.632625-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	19:21:29.633227-0500	ControlCenter	Received state update for 5767 (app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>, running-active-NotVisible
default	19:21:29.633385-0500	gamepolicyd	Received state update for 5767 (app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>, running-active-NotVisible
default	19:21:30.407866-0500	runningboardd	Invalidating assertion 403-642-153842 (target:app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>) from originator [osservice<com.apple.controlcenter(501)>:642]
default	19:21:30.508919-0500	runningboardd	Removed last relative-start-date-defining assertion for process app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>
default	19:21:30.510179-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] Ignoring jetsam update because this process is not memory-managed
default	19:21:30.510211-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] Ignoring suspend because this process is not lifecycle managed
default	19:21:30.510236-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] Ignoring GPU update because this process is not GPU managed
default	19:21:30.510282-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] Ignoring memory limit update because this process is not memory-managed
default	19:21:30.517232-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	19:21:30.522439-0500	ControlCenter	Received state update for 5767 (app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>, running-active-NotVisible
default	19:21:30.522644-0500	gamepolicyd	Received state update for 5767 (app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>, running-active-NotVisible
default	19:21:30.711443-0500	Nexy	                AUHAL.cpp:473   ~AUHAL: (0xbb05cb840) Selecting device 0 from destructor
default	19:21:30.711476-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0xbb05cb840)
default	19:21:30.711493-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0xbb05cb840) not already running
default	19:21:30.711507-0500	Nexy	                AUHAL.cpp:687   SelectDevice: (0xbb05cb840) disconnecting device 85
default	19:21:30.711520-0500	Nexy	                AUHAL.cpp:751   SelectDevice: (0xbb05cb840) destroying ioproc 0xb for device 85
default	19:21:30.711575-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Output {1C-77-54-18-C8-A3:output, 0xb}
default	19:21:30.711654-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	19:21:30.711921-0500	Nexy	                AUHAL.cpp:853   SelectDevice: (0xbb05cb840) nothing to setup
default	19:21:30.711945-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0xbb05cb840) adding 0 device listeners to device 0
default	19:21:30.711958-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0xbb05cb840) adding 0 device delegate listeners to device 0
default	19:21:30.711971-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0xbb05cb840) removing 7 device listeners from device 85
default	19:21:30.712361-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0xbb05cb840) removing 0 device delegate listeners from device 85
default	19:21:30.712390-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0xbb05cb840)
default	19:21:30.714934-0500	Nexy	                AUHAL.cpp:420   AUHAL: (0xbb05cb840) Selecting device 85 from constructor
default	19:21:30.714962-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0xbb05cb840)
default	19:21:30.714983-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0xbb05cb840) not already running
default	19:21:30.714996-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0xbb05cb840) nothing to teardown
default	19:21:30.715006-0500	Nexy	                AUHAL.cpp:762   SelectDevice: (0xbb05cb840) connecting device 85
default	19:21:30.715230-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0xbb05cb840) Device ID: 85 (Input:No | Output:Yes): true
default	19:21:30.715456-0500	Nexy	                AUHAL.cpp:774   SelectDevice: (0xbb05cb840) created ioproc 0xc for device 85
default	19:21:30.715766-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0xbb05cb840) adding 7 device listeners to device 85
default	19:21:30.716243-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0xbb05cb840) adding 0 device delegate listeners to device 85
default	19:21:30.716272-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0xbb05cb840)
default	19:21:30.716474-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  48000 Hz, Float32, interleaved
default	19:21:30.716495-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	19:21:30.716511-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	19:21:30.716531-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	19:21:30.716553-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	19:21:30.716813-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0xbb05cb840) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	19:21:30.716837-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0xbb05cb840) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	19:21:30.716849-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	19:21:30.716859-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0xbb05cb840) removing 0 device listeners from device 0
default	19:21:30.716882-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0xbb05cb840) removing 0 device delegate listeners from device 0
default	19:21:30.716891-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0xbb05cb840)
default	19:21:30.716911-0500	Nexy	                AUHAL.cpp:2303  SetProperty: (0xbb05cb840) caller requesting device change from 85 to 85
default	19:21:30.716919-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0xbb05cb840)
default	19:21:30.716929-0500	Nexy	                AUHAL.cpp:664   SelectDevice: <- (0xbb05cb840) exiting with nothing to do
default	19:21:30.716943-0500	Nexy	AudioHardware-mac-imp.cpp:1306   AudioObjectAddPropertyListener: listener was already added
default	19:21:30.717972-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	19:21:30.718568-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	19:21:30.722527-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] from originator [app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] with description <RBSAssertionDescriptor| "AudioHAL" ID:403-5767-153857 target:5767 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	19:21:30.722666-0500	runningboardd	Assertion 403-5767-153857 (target:[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767]) will be created as active
default	19:21:30.723166-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] from originator [osservice<com.apple.powerd>:338] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:403-338-153858 target:5767 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	19:21:30.723182-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] Ignoring jetsam update because this process is not memory-managed
default	19:21:30.723200-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] Ignoring suspend because this process is not lifecycle managed
default	19:21:30.723213-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] Ignoring GPU update because this process is not GPU managed
default	19:21:30.723830-0500	runningboardd	Assertion 403-338-153858 (target:[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767]) will be created as active
default	19:21:30.723861-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] Ignoring memory limit update because this process is not memory-managed
default	19:21:30.727977-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	19:21:30.728362-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] Ignoring jetsam update because this process is not memory-managed
default	19:21:30.728375-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] Ignoring suspend because this process is not lifecycle managed
default	19:21:30.728400-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] Ignoring GPU update because this process is not GPU managed
default	19:21:30.728476-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] Ignoring memory limit update because this process is not memory-managed
default	19:21:30.728667-0500	ControlCenter	Received state update for 5767 (app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>, running-active-NotVisible
default	19:21:30.729078-0500	gamepolicyd	Received state update for 5767 (app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>, running-active-NotVisible
default	19:21:30.731951-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	19:21:30.732439-0500	ControlCenter	Received state update for 5767 (app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>, running-active-NotVisible
default	19:21:30.732600-0500	gamepolicyd	Received state update for 5767 (app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>, running-active-NotVisible
default	19:21:31.003043-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xc}
default	19:21:31.003936-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1e8048","name":"Nexy(5767)"}, "details":{"deviceUIDs":["1C-77-54-18-C8-A3:output"],"implicit_category":"MediaPlayback","input_running":false,"output_running":true} }
default	19:21:31.004106-0500	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 73, PID = 5767, Name = sid:0x1e8048, Nexy(5767), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO> is going active
default	19:21:31.004127-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsPlaying:]: MXCoreSession com.nexy.assistant with category/mode MediaPlayback/Default and coreSessionID = 73 starting playing
default	19:21:31.004199-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 73, PID = 5767, Name = sid:0x1e8048, Nexy(5767), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	19:21:31.004250-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 73, PID = 5767, Name = sid:0x1e8048, Nexy(5767), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO>
default	19:21:31.004277-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1e8048, Nexy(5767), 'prim'', displayID:'com.nexy.assistant'}
default	19:21:31.004326-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 201, deviceID = <private>
default	19:21:31.004422-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 1]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)}
default	19:21:31.004363-0500	audiomxd	AudioApplicationInfoImpl.mm:395   Successfully updated session 0x1e8048 to isSessionRecording: 0
	app: {"name":"[implicit] Nexy","pid":5767}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1e8048, sessionType: 'prim', isRecording: false }, 
]
default	19:21:31.004439-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	19:21:31.004642-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 201 flag 0x1 < Hijack > app com.nexy.assistant CID 0x4D120001 category Not set
default	19:21:31.006289-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 201,
}
default	19:21:31.006323-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	19:21:31.006077-0500	audiomxd	UpdateAudioState CID 0x4D120001 audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	19:21:31.006339-0500	audioaccessoryd	AudioStateChanged: Added audio session app com.nexy.assistant NULL -> 201 count 1
default	19:21:31.006347-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 201
error	19:21:31.006361-0500	audioaccessoryd	Updating local audio category 100 -> 201 app com.nexy.assistant
default	19:21:31.006428-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.nexy.assistant
default	19:21:33.185203-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.nexy.assistant, Score 201, Remote 0 NumofApp 1
error	19:21:33.237695-0500	Nexy	         HALC_ProxyIOContext.cpp:1623  HALC_ProxyIOContext::IOWorkLoop: skipping cycle due to overload
default	19:21:33.247477-0500	Nexy	NotifyToken::RegisterDispatch(user.uid.501.com.apple.LaunchServices.database) fired for session key <private>
default	19:21:33.250365-0500	coreaudiod	Sending message. { reporterID=24769076396036, category=IO, type=error, message=["HostApplicationDisplayID": Optional(com.nexy.assistant), "io_frame_counter": Optional(105472), "is_recovering": Optional(0), "wg_total_wakeups": Optional(7), "io_cycle_usage": Optional(1), "output_device_source_list": Optional(Unknown), "wg_cycles": Optional(2601948), "num_continuous_silent_io_cycles": Optional(0), "wg_system_time_mach": Optional(4524), "other_active_clients": Optional([  ]), "wg_user_time_mach": Optional(25419), "smallest_buffer_frame_size": Optional(512), "safety_violation_sample_gap": Optional(1271), "io_page_faults_duration": Optional(0), "num_continuous_nonzero_io_cycles": Optional(198), "io_cycle_budget": Optional(11354166), "io_page_faults": Optional(0), "multi_cycle_io_page_faults": Optional(0), "wg_external_wakeups": Optional(1), "output_device_transport_list": Optional(Bluetooth), "reporting_latency": Optional(37437500), "other_page_faults": Optional(0), "wg_instructions": Optional(2249922), "HAL_client_IO_duration": Optional(36704166), "inp<…> }
default	19:21:33.270956-0500	Nexy	void _updateToReflectAutomaticTerminationState(void) Setting _kLSApplicationWouldBeTerminatedByTALKey=1
default	19:21:35.574819-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Output {1C-77-54-18-C8-A3:output, 0xc}
default	19:21:35.575459-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1e8048","name":"Nexy(5767)"}, "details":{"deviceUIDs":[],"implicit_category":"","input_running":false,"output_running":false} }
default	19:21:35.575643-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsPlaying:]: MXCoreSession com.nexy.assistant with category/mode MediaPlayback/Default and coreSessionID = 73 stopping playing
default	19:21:35.575742-0500	audiomxd	-MXCoreSession- -[MXCoreSession endInterruption:]: Session <ID: 73, PID = 5767, Name = sid:0x1e8048, Nexy(5767), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> is going inactive
default	19:21:35.575819-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 73, PID = 5767, Name = sid:0x1e8048, Nexy(5767), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	19:21:35.575941-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 73, PID = 5767, Name = sid:0x1e8048, Nexy(5767), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	19:21:35.576085-0500	audiomxd	UpdateAudioState CID 0x4D120001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	19:21:35.576181-0500	audiomxd	AudioApplicationInfoImpl.mm:395   Successfully updated session 0x1e8048 to isSessionRecording: 0
	app: {"name":"[implicit] Nexy","pid":5767}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1e8048, sessionType: 'prim', isRecording: false }, 
]
default	19:21:35.576312-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 0]. BT device UIDS: {(
)}
default	19:21:35.576327-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	19:21:35.576364-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	19:21:35.576459-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	19:21:35.576502-0500	audioaccessoryd	AudioStateChanged: Removed audio session app com.nexy.assistant 201 count 0
default	19:21:35.581820-0500	runningboardd	Invalidating assertion 403-5767-153857 (target:[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767]) from originator [app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767]
default	19:21:35.582040-0500	runningboardd	Invalidating assertion 403-338-153858 (target:[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767]) from originator [osservice<com.apple.powerd>:338]
default	19:21:35.585701-0500	coreaudiod	Sending message. { reporterID=24769076396036, category=IO, type=error, message=["HostApplicationDisplayID": Optional(com.nexy.assistant), "io_frame_counter": Optional(111104), "is_recovering": Optional(0), "wg_total_wakeups": Optional(6), "io_cycle_usage": Optional(1), "output_device_source_list": Optional(Unknown), "wg_cycles": Optional(1404448), "num_continuous_silent_io_cycles": Optional(84), "wg_system_time_mach": Optional(4456), "other_active_clients": Optional([  ]), "wg_user_time_mach": Optional(14534), "smallest_buffer_frame_size": Optional(2147483647), "safety_violation_sample_gap": Optional(574), "io_page_faults_duration": Optional(0), "num_continuous_nonzero_io_cycles": Optional(0), "io_cycle_budget": Optional(11354166), "io_page_faults": Optional(0), "multi_cycle_io_page_faults": Optional(0), "wg_external_wakeups": Optional(3), "output_device_transport_list": Optional(Bluetooth), "reporting_latency": Optional(21464750), "other_page_faults": Optional(0), "wg_instructions": Optional(860816), "HAL_client_IO_duration": Optional(22426125), <…> }
default	19:21:35.686238-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] Ignoring jetsam update because this process is not memory-managed
default	19:21:35.686261-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] Ignoring suspend because this process is not lifecycle managed
default	19:21:35.686280-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] Ignoring GPU update because this process is not GPU managed
default	19:21:35.686312-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] Ignoring memory limit update because this process is not memory-managed
default	19:21:35.692028-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	19:21:35.692751-0500	ControlCenter	Received state update for 5767 (app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>, running-active-NotVisible
default	19:21:35.692959-0500	gamepolicyd	Received state update for 5767 (app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>, running-active-NotVisible
default	19:21:39.261187-0500	Nexy	LSExceptions shared instance invalidated for timeout.
default	19:21:47.089839-0500	Nexy	                AUHAL.cpp:420   AUHAL: (0xbb05cb140) Selecting device 85 from constructor
default	19:21:47.089867-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0xbb05cb140)
default	19:21:47.089879-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0xbb05cb140) not already running
default	19:21:47.089889-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0xbb05cb140) nothing to teardown
default	19:21:47.089896-0500	Nexy	                AUHAL.cpp:762   SelectDevice: (0xbb05cb140) connecting device 85
default	19:21:47.090080-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0xbb05cb140) Device ID: 85 (Input:No | Output:Yes): true
default	19:21:47.090269-0500	Nexy	                AUHAL.cpp:774   SelectDevice: (0xbb05cb140) created ioproc 0xd for device 85
default	19:21:47.090483-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0xbb05cb140) adding 7 device listeners to device 85
default	19:21:47.090835-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0xbb05cb140) adding 0 device delegate listeners to device 85
default	19:21:47.090852-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0xbb05cb140)
default	19:21:47.091010-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  48000 Hz, Float32, interleaved
default	19:21:47.091026-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	19:21:47.091037-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	19:21:47.091051-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	19:21:47.091068-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	19:21:47.091260-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0xbb05cb140) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	19:21:47.091279-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0xbb05cb140) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	19:21:47.091295-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	19:21:47.091305-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0xbb05cb140) removing 0 device listeners from device 0
default	19:21:47.091314-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0xbb05cb140) removing 0 device delegate listeners from device 0
default	19:21:47.091324-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0xbb05cb140)
default	19:21:47.091355-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is DISABLED
default	19:21:47.091449-0500	Nexy	                AUHAL.cpp:2303  SetProperty: (0xbb05cb140) caller requesting device change from 85 to 91
default	19:21:47.091470-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0xbb05cb140)
default	19:21:47.091481-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0xbb05cb140) not already running
default	19:21:47.091491-0500	Nexy	                AUHAL.cpp:687   SelectDevice: (0xbb05cb140) disconnecting device 85
default	19:21:47.091501-0500	Nexy	                AUHAL.cpp:751   SelectDevice: (0xbb05cb140) destroying ioproc 0xd for device 85
default	19:21:47.091536-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped Unknown {1C-77-54-18-C8-A3:output, 0xd}
default	19:21:47.091605-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	19:21:47.091768-0500	Nexy	                AUHAL.cpp:762   SelectDevice: (0xbb05cb140) connecting device 91
default	19:21:47.091928-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0xbb05cb140) Device ID: 91 (Input:Yes | Output:No): true
default	19:21:47.094734-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=411.1503, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=5767, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=398, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	19:21:47.098263-0500	tccd	AUTHREQ_SUBJECT: msgID=411.1503, subject=com.nexy.assistant,
default	19:21:47.099853-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc79244300 at /Applications/Nexy.app
default	19:21:47.127077-0500	Nexy	                AUHAL.cpp:774   SelectDevice: (0xbb05cb140) created ioproc 0xb for device 91
default	19:21:47.127264-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0xbb05cb140) adding 7 device listeners to device 91
default	19:21:47.127446-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0xbb05cb140) adding 0 device delegate listeners to device 91
default	19:21:47.127458-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0xbb05cb140)
default	19:21:47.127468-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 output streams; not all mono
default	19:21:47.127480-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	19:21:47.127650-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  input stream 0 [0x5c]:  1 ch,  24000 Hz, Float32
default	19:21:47.127659-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 input streams; all mono
default	19:21:47.127664-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  1 ch,  24000 Hz, Float32
default	19:21:47.127749-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0xbb05cb140) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	19:21:47.127758-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0xbb05cb140) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	19:21:47.127763-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	19:21:47.127768-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0xbb05cb140) removing 7 device listeners from device 85
default	19:21:47.127933-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0xbb05cb140) removing 0 device delegate listeners from device 85
default	19:21:47.127942-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0xbb05cb140)
default	19:21:47.128530-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	19:21:47.129806-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=411.1504, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=5767, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=398, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	19:21:47.130918-0500	tccd	AUTHREQ_SUBJECT: msgID=411.1504, subject=com.nexy.assistant,
default	19:21:47.131560-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc79244300 at /Applications/Nexy.app
default	19:21:47.161602-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	19:21:47.162601-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=411.1505, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=5767, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=398, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	19:21:47.163521-0500	tccd	AUTHREQ_SUBJECT: msgID=411.1505, subject=com.nexy.assistant,
default	19:21:47.164114-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc79244300 at /Applications/Nexy.app
default	19:21:47.193614-0500	Nexy	                AUHAL.cpp:473   ~AUHAL: (0xbb05cb140) Selecting device 0 from destructor
default	19:21:47.193627-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0xbb05cb140)
default	19:21:47.193631-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0xbb05cb140) not already running
default	19:21:47.193635-0500	Nexy	                AUHAL.cpp:687   SelectDevice: (0xbb05cb140) disconnecting device 91
default	19:21:47.193640-0500	Nexy	                AUHAL.cpp:751   SelectDevice: (0xbb05cb140) destroying ioproc 0xb for device 91
default	19:21:47.193665-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xb}
default	19:21:47.193696-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	19:21:47.193789-0500	Nexy	                AUHAL.cpp:853   SelectDevice: (0xbb05cb140) nothing to setup
default	19:21:47.193798-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0xbb05cb140) adding 0 device listeners to device 0
default	19:21:47.193803-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0xbb05cb140) adding 0 device delegate listeners to device 0
default	19:21:47.193813-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0xbb05cb140) removing 7 device listeners from device 91
default	19:21:47.193972-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0xbb05cb140) removing 0 device delegate listeners from device 91
default	19:21:47.193981-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0xbb05cb140)
default	19:21:47.194837-0500	Nexy	                AUHAL.cpp:420   AUHAL: (0xbb05cb140) Selecting device 85 from constructor
default	19:21:47.194847-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0xbb05cb140)
default	19:21:47.194850-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0xbb05cb140) not already running
default	19:21:47.194854-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0xbb05cb140) nothing to teardown
default	19:21:47.194858-0500	Nexy	                AUHAL.cpp:762   SelectDevice: (0xbb05cb140) connecting device 85
default	19:21:47.194955-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0xbb05cb140) Device ID: 85 (Input:No | Output:Yes): true
default	19:21:47.195036-0500	Nexy	                AUHAL.cpp:774   SelectDevice: (0xbb05cb140) created ioproc 0xe for device 85
default	19:21:47.195147-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0xbb05cb140) adding 7 device listeners to device 85
default	19:21:47.195310-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0xbb05cb140) adding 0 device delegate listeners to device 85
default	19:21:47.195319-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0xbb05cb140)
default	19:21:47.195405-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  48000 Hz, Float32, interleaved
default	19:21:47.195414-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	19:21:47.195419-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	19:21:47.195425-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	19:21:47.195432-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	19:21:47.195517-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0xbb05cb140) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	19:21:47.195528-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0xbb05cb140) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	19:21:47.195534-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	19:21:47.195538-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0xbb05cb140) removing 0 device listeners from device 0
default	19:21:47.195543-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0xbb05cb140) removing 0 device delegate listeners from device 0
default	19:21:47.195547-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0xbb05cb140)
default	19:21:47.195557-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is DISABLED
default	19:21:47.195600-0500	Nexy	                AUHAL.cpp:2303  SetProperty: (0xbb05cb140) caller requesting device change from 85 to 91
default	19:21:47.195607-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0xbb05cb140)
default	19:21:47.195611-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0xbb05cb140) not already running
default	19:21:47.195616-0500	Nexy	                AUHAL.cpp:687   SelectDevice: (0xbb05cb140) disconnecting device 85
default	19:21:47.195621-0500	Nexy	                AUHAL.cpp:751   SelectDevice: (0xbb05cb140) destroying ioproc 0xe for device 85
default	19:21:47.195631-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped Unknown {1C-77-54-18-C8-A3:output, 0xe}
default	19:21:47.195655-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	19:21:47.195761-0500	Nexy	                AUHAL.cpp:762   SelectDevice: (0xbb05cb140) connecting device 91
default	19:21:47.195832-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0xbb05cb140) Device ID: 91 (Input:Yes | Output:No): true
default	19:21:47.196793-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=411.1506, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=5767, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=398, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	19:21:47.197676-0500	tccd	AUTHREQ_SUBJECT: msgID=411.1506, subject=com.nexy.assistant,
default	19:21:47.198259-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc79244300 at /Applications/Nexy.app
default	19:21:47.226078-0500	Nexy	                AUHAL.cpp:774   SelectDevice: (0xbb05cb140) created ioproc 0xc for device 91
default	19:21:47.226182-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0xbb05cb140) adding 7 device listeners to device 91
default	19:21:47.226336-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0xbb05cb140) adding 0 device delegate listeners to device 91
default	19:21:47.226351-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0xbb05cb140)
default	19:21:47.226360-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 output streams; not all mono
default	19:21:47.226368-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	19:21:47.226471-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  input stream 0 [0x5c]:  1 ch,  24000 Hz, Float32
default	19:21:47.226480-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 input streams; all mono
default	19:21:47.226486-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  1 ch,  24000 Hz, Float32
default	19:21:47.226569-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0xbb05cb140) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	19:21:47.226581-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0xbb05cb140) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	19:21:47.226586-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	19:21:47.226591-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0xbb05cb140) removing 7 device listeners from device 85
default	19:21:47.226727-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0xbb05cb140) removing 0 device delegate listeners from device 85
default	19:21:47.226735-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0xbb05cb140)
default	19:21:47.226742-0500	Nexy	AudioHardware-mac-imp.cpp:1306   AudioObjectAddPropertyListener: listener was already added
default	19:21:47.227246-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	19:21:47.228151-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=411.1507, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=5767, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=398, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	19:21:47.229006-0500	tccd	AUTHREQ_SUBJECT: msgID=411.1507, subject=com.nexy.assistant,
default	19:21:47.229576-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc79244300 at /Applications/Nexy.app
default	19:21:47.257515-0500	Nexy	       ACv2Workarounds.mm:51    com.nexy.assistant: fix84702776_86723525_86479548_89800354_SinglePacketDesc: false
default	19:21:47.257582-0500	Nexy	       AudioConverter.cpp:1044  Created a new in process converter -> 0xbae85e550, from  1 ch,  24000 Hz, Float32 to  1 ch,  48000 Hz, Float32
default	19:21:47.257754-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	19:21:47.258629-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=411.1508, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=5767, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=398, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	19:21:47.259452-0500	tccd	AUTHREQ_SUBJECT: msgID=411.1508, subject=com.nexy.assistant,
default	19:21:47.260030-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc79244300 at /Applications/Nexy.app
default	19:21:47.288872-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] from originator [app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] with description <RBSAssertionDescriptor| "AudioHAL" ID:403-5767-153882 target:5767 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	19:21:47.288963-0500	runningboardd	Assertion 403-5767-153882 (target:[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767]) will be created as active
default	19:21:47.289346-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] Ignoring jetsam update because this process is not memory-managed
default	19:21:47.289357-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] Ignoring suspend because this process is not lifecycle managed
default	19:21:47.289367-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] Ignoring GPU update because this process is not GPU managed
default	19:21:47.289385-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] Ignoring memory limit update because this process is not memory-managed
default	19:21:47.289427-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=411.1509, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=5767, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=398, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	19:21:47.290246-0500	tccd	AUTHREQ_SUBJECT: msgID=411.1509, subject=com.nexy.assistant,
default	19:21:47.290805-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc79244300 at /Applications/Nexy.app
default	19:21:47.292429-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	19:21:47.293005-0500	ControlCenter	Received state update for 5767 (app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>, running-active-NotVisible
default	19:21:47.293127-0500	gamepolicyd	Received state update for 5767 (app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>, running-active-NotVisible
default	19:21:47.320619-0500	coreaudiod	>>> NEGOTIATE [com.nexy.assistant]
default	19:21:47.320795-0500	coreaudiod	<<< NEGOTIATE [com.nexy.assistant]
default	19:21:47.322561-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:10301 called from <private>
default	19:21:47.322604-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	19:21:47.322607-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Input {1C-77-54-18-C8-A3:input, 0xc}
default	19:21:47.323829-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:10301 called from <private>
default	19:21:47.324024-0500	runningboardd	Invalidating assertion 403-5767-153882 (target:[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767]) from originator [app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767]
default	19:21:47.328289-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] from originator [osservice<com.apple.powerd>:338] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:403-338-153883 target:5767 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	19:21:47.329173-0500	runningboardd	Assertion 403-338-153883 (target:[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767]) will be created as active
default	19:21:47.330121-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	19:21:47.323966-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(10301)
default	19:21:47.324166-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(10300)
default	19:21:47.325056-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:10301 called from <private>
default	19:21:47.325104-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:10300 called from <private>
default	19:21:47.325122-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:10301 called from <private>
default	19:21:47.325134-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:10300 called from <private>
default	19:21:47.330691-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] Ignoring jetsam update because this process is not memory-managed
default	19:21:47.331011-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] Ignoring suspend because this process is not lifecycle managed
default	19:21:47.331429-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] Ignoring GPU update because this process is not GPU managed
default	19:21:47.332087-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] Ignoring memory limit update because this process is not memory-managed
default	19:21:47.332159-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	19:21:47.334101-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(10301)
default	19:21:47.334125-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(10301)
default	19:21:47.334135-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(10301)
default	19:21:47.334146-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(10301)
default	19:21:47.334142-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:10301 called from <private>
default	19:21:47.334168-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:10301 called from <private>
default	19:21:47.334177-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:10301 called from <private>
default	19:21:47.334184-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:10301 called from <private>
default	19:21:47.334337-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:10301 called from <private>
default	19:21:47.334346-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:10301 called from <private>
default	19:21:47.334386-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:10301 called from <private>
default	19:21:47.334482-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:10301 called from <private>
default	19:21:47.340039-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:10301 called from <private>
default	19:21:47.343923-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1e8048","name":"Nexy(5767)"}, "details":{"deviceUIDs":["1C-77-54-18-C8-A3:input"],"implicit_category":"Record","input_running":true,"output_running":false} }
default	19:21:47.344017-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 73, PID = 5767, Name = sid:0x1e8048, Nexy(5767), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	19:21:47.344881-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Category/Mode changed -- The score for sid:0x1e8048, Nexy(5767), 'prim'/com.nexy.assistant was not correct. Old score = 201
default	19:21:47.345104-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 73, PID = 5767, Name = sid:0x1e8048, Nexy(5767), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	19:21:47.345782-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 73, PID = 5767, Name = sid:0x1e8048, Nexy(5767), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	19:21:47.346714-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 73, PID = 5767, Name = sid:0x1e8048, Nexy(5767), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	19:21:47.345495-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] from originator [app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] with description <RBSAssertionDescriptor| "AudioHAL" ID:403-5767-153884 target:5767 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	19:21:47.347115-0500	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 73, PID = 5767, Name = sid:0x1e8048, Nexy(5767), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> is going active
default	19:21:47.346694-0500	runningboardd	Assertion 403-5767-153884 (target:[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767]) will be created as active
default	19:21:47.347212-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1e8048, Nexy(5767), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 73 starting recording
default	19:21:47.347547-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 73, PID = 5767, Name = sid:0x1e8048, Nexy(5767), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	19:21:47.348701-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 73, PID = 5767, Name = sid:0x1e8048, Nexy(5767), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	19:21:47.348896-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1e8048, Nexy(5767), 'prim'', displayID:'com.nexy.assistant'}
default	19:21:47.347199-0500	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1e8048, Nexy(5767), 'prim'', AudioCategory changed to 'Record_WithBluetooth'
default	19:21:47.340054-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:10301 called from <private>
default	19:21:47.343487-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(10301)
default	19:21:47.343506-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:10301 called from <private>
default	19:21:47.343928-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(10300)
default	19:21:47.344376-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:10300 called from <private>
default	19:21:47.344500-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:10300 called from <private>
default	19:21:47.352638-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	19:21:47.349405-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	19:21:47.346688-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=411.1510, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=5767, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=398, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	19:21:47.354264-0500	runningboardd	Invalidating assertion 403-338-153883 (target:[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767]) from originator [osservice<com.apple.powerd>:338]
default	19:21:47.349163-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [1, 0]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:input"
)}
default	19:21:47.352860-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	19:21:47.354729-0500	ControlCenter	Received state update for 5767 (app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>, running-active-NotVisible
default	19:21:47.354724-0500	gamepolicyd	Received state update for 5767 (app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>, running-active-NotVisible
default	19:21:47.359448-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:10300 called from <private>
default	19:21:47.359466-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:10300 called from <private>
default	19:21:47.359617-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(10300)
default	19:21:47.364558-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(10300)
default	19:21:47.364768-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:10300 called from <private>
default	19:21:47.364782-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:10300 called from <private>
default	19:21:47.364866-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(10300)
default	19:21:47.369662-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(10300)
default	19:21:47.368580-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc79244300 at /Applications/Nexy.app
default	19:21:47.369865-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:10300 called from <private>
default	19:21:47.369874-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:10300 called from <private>
default	19:21:47.370145-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:10300 called from <private>
default	19:21:47.370155-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:10300 called from <private>
default	19:21:47.370170-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:10300 called from <private>
default	19:21:47.370179-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:10300 called from <private>
default	19:21:47.370187-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:10300 called from <private>
default	19:21:47.370192-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:10300 called from <private>
default	19:21:47.370198-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:10300 called from <private>
default	19:21:47.370296-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(10300)
default	19:21:47.416773-0500	coreaudiod	>>> NEGOTIATE [com.nexy.assistant]
default	19:21:47.416934-0500	coreaudiod	<<< NEGOTIATE [com.nexy.assistant]
default	19:21:47.421355-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:10301 called from <private>
default	19:21:47.421678-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] from originator [osservice<com.apple.powerd>:338] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:403-338-153885 target:5767 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	19:21:47.421389-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:10301 called from <private>
default	19:21:47.421736-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	19:21:47.421782-0500	runningboardd	Assertion 403-338-153885 (target:[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767]) will be created as active
default	19:21:47.423415-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:10301 called from <private>
default	19:21:47.423547-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(10301)
default	19:21:47.423562-0500	runningboardd	Invalidating assertion 403-5767-153884 (target:[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767]) from originator [app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767]
default	19:21:47.423563-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:10301 called from <private>
default	19:21:47.423569-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:10301 called from <private>
default	19:21:47.423688-0500	runningboardd	Invalidating assertion 403-338-153885 (target:[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767]) from originator [osservice<com.apple.powerd>:338]
default	19:21:47.424329-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	19:21:47.424470-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	19:21:47.424942-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(10301)
default	19:21:47.425124-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:10301 called from <private>
default	19:21:47.425134-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:10301 called from <private>
default	19:21:47.425147-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:10301 called from <private>
default	19:21:47.425549-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] from originator [app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] with description <RBSAssertionDescriptor| "AudioHAL" ID:403-5767-153886 target:5767 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	19:21:47.425611-0500	runningboardd	Assertion 403-5767-153886 (target:[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767]) will be created as active
default	19:21:47.426872-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=411.1511, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=5767, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=398, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	19:21:47.429940-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	19:21:47.429986-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	19:21:47.430036-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	19:21:47.430207-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	19:21:47.430269-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	19:21:47.430416-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	19:21:47.431328-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] Ignoring jetsam update because this process is not memory-managed
default	19:21:47.431359-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] Ignoring suspend because this process is not lifecycle managed
default	19:21:47.435594-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	19:21:47.436113-0500	ControlCenter	Received state update for 5767 (app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>, running-active-NotVisible
default	19:21:47.436351-0500	gamepolicyd	Received state update for 5767 (app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>, running-active-NotVisible
default	19:21:47.465620-0500	coreaudiod	>>> ADAPT [com.nexy.assistant]
default	19:21:47.467112-0500	coreaudiod	IssueReporting.cpp:492   RTAID [ use_case=Generic report_type=RMS Generic Chain clientID=ADM node=ADM::com.nexy.assistant_10301.10209.0_airpods noise suppression studio::out-0 issue_detected_sample_time=24480.000000 ] -- [ rms:[-43.799812], peaks:[-27.225800] ]
default	19:21:47.467128-0500	coreaudiod	IssueReporting.cpp:492   RTAID [ use_case=Generic report_type=RMS Generic Chain clientID=ADM node=ADM::com.nexy.assistant_10301.10209.0_airpods noise suppression studio::in-0 issue_detected_sample_time=0.000000 ] -- [ rms:[-40.642353], peaks:[-24.645382] ]
default	19:21:47.467504-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xa380e9b00] Created node ADM::com.nexy.assistant_10301.10209.0_airpods noise suppression studio::in-0 with nodeID 0 - reporting period = 10.000000, sample rate = 24000.000000
default	19:21:47.467564-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xa380e9b00] Created node ADM::com.nexy.assistant_10301.10209.0_airpods noise suppression studio::out-0 with nodeID 1 - reporting period = 10.000000, sample rate = 24000.000000
default	19:21:47.505394-0500	coreaudiod	<<< ADAPT [com.nexy.assistant]
default	19:21:47.508697-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:10301 called from <private>
default	19:21:47.508754-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:10301 called from <private>
default	19:21:47.508845-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	19:21:47.509973-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] from originator [osservice<com.apple.powerd>:338] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:403-338-153888 target:5767 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	19:21:47.510076-0500	runningboardd	Assertion 403-338-153888 (target:[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767]) will be created as active
default	19:21:47.510468-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] Ignoring jetsam update because this process is not memory-managed
default	19:21:47.510526-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] Ignoring suspend because this process is not lifecycle managed
default	19:21:47.510577-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] Ignoring GPU update because this process is not GPU managed
default	19:21:47.510710-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] Ignoring memory limit update because this process is not memory-managed
default	19:21:47.511699-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:10301 called from <private>
default	19:21:47.512027-0500	runningboardd	Invalidating assertion 403-5767-153886 (target:[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767]) from originator [app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767]
default	19:21:47.511830-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(10301)
default	19:21:47.512717-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	19:21:47.511852-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:10301 called from <private>
default	19:21:47.513119-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	19:21:47.514508-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] from originator [app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] with description <RBSAssertionDescriptor| "AudioHAL" ID:403-5767-153889 target:5767 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	19:21:47.514667-0500	runningboardd	Assertion 403-5767-153889 (target:[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767]) will be created as active
default	19:21:47.511857-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:10301 called from <private>
default	19:21:47.513663-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(10301)
default	19:21:47.513921-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:10301 called from <private>
default	19:21:47.513930-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:10301 called from <private>
default	19:21:47.513942-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:10301 called from <private>
default	19:21:47.515779-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=411.1512, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=5767, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=398, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	19:21:47.518580-0500	tccd	AUTHREQ_SUBJECT: msgID=411.1512, subject=com.nexy.assistant,
default	19:21:47.519390-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc79244300 at /Applications/Nexy.app
default	19:21:47.519582-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	19:21:47.520071-0500	runningboardd	Invalidating assertion 403-338-153888 (target:[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767]) from originator [osservice<com.apple.powerd>:338]
default	19:21:47.523997-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	19:21:47.524080-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	19:21:47.524142-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	19:21:47.524281-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	19:21:47.525243-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	19:21:47.525260-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	19:21:47.525285-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	19:21:47.525300-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	19:21:47.525312-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	19:21:47.525345-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	19:21:47.525625-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	19:21:47.536835-0500	ControlCenter	Received state update for 5767 (app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>, running-active-NotVisible
default	19:21:47.537137-0500	gamepolicyd	Received state update for 5767 (app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>, running-active-NotVisible
default	19:21:47.557467-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:10301 called from <private>
default	19:21:47.559906-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] from originator [osservice<com.apple.powerd>:338] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:403-338-153890 target:5767 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	19:21:47.560039-0500	runningboardd	Assertion 403-338-153890 (target:[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767]) will be created as active
default	19:21:47.566345-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	19:21:47.566395-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	19:21:47.566443-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	19:21:47.567128-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	19:21:47.567162-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	19:21:47.567193-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	19:21:47.567222-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	19:21:47.567231-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	19:21:47.567239-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	19:21:47.567251-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	19:21:47.567261-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	19:21:47.567290-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	19:21:47.567305-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	19:21:47.567364-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	19:21:47.567375-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	19:21:47.567431-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	19:21:47.567636-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	19:21:47.567646-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	19:21:47.567678-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	19:21:47.567701-0500	ControlCenter	Navigating to new application [com.nexy.assistant]
default	19:21:47.567704-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	19:21:47.567755-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	19:21:47.567764-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	19:21:47.720515-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xc}
default	19:21:47.720907-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1e8048","name":"Nexy(5767)"}, "details":{"deviceUIDs":[],"implicit_category":"","input_running":false,"output_running":false} }
default	19:21:47.721045-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 73, PID = 5767, Name = sid:0x1e8048, Nexy(5767), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	19:21:47.721101-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 73, PID = 5767, Name = sid:0x1e8048, Nexy(5767), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	19:21:47.721131-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1e8048, Nexy(5767), 'prim'', displayID:'com.nexy.assistant'}
default	19:21:47.721180-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1e8048, Nexy(5767), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 73 stopping recording
default	19:21:47.721183-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	19:21:47.721204-0500	audiomxd	-MXCoreSession- -[MXCoreSession endInterruption:]: Session <ID: 73, PID = 5767, Name = sid:0x1e8048, Nexy(5767), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> is going inactive
default	19:21:47.721229-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 73, PID = 5767, Name = sid:0x1e8048, Nexy(5767), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	19:21:47.721257-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 73, PID = 5767, Name = sid:0x1e8048, Nexy(5767), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	19:21:47.721349-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 0]. BT device UIDS: {(
)}
default	19:21:47.721359-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	19:21:47.721416-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 200 flag 0x1 < Hijack > app com.nexy.assistant CID 0x4D120001 category Not set
default	19:21:47.724088-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	19:21:47.724118-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	19:21:47.724133-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	19:21:47.724150-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	19:21:47.724275-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	19:21:47.723843-0500	runningboardd	Invalidating assertion 403-5767-153889 (target:[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767]) from originator [app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767]
default	19:21:47.723927-0500	runningboardd	Invalidating assertion 403-338-153890 (target:[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767]) from originator [osservice<com.apple.powerd>:338]
default	19:21:47.723989-0500	audiomxd	UpdateAudioState CID 0x4D120001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	19:21:47.724332-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	19:21:47.724039-0500	audiomxd	UpdateAudioState CID 0x4D120001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	19:21:47.724355-0500	audioaccessoryd	AudioStateChanged: Removed audio session app com.nexy.assistant 201 count 0
default	19:21:47.725495-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	19:21:47.727521-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	19:21:47.727531-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	19:21:47.727541-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	19:21:47.727549-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	19:21:47.727555-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	19:21:47.727562-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	19:21:47.727649-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	19:21:47.821924-0500	Nexy	                AUHAL.cpp:473   ~AUHAL: (0xbb05cb140) Selecting device 0 from destructor
default	19:21:47.821949-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0xbb05cb140)
default	19:21:47.821959-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0xbb05cb140) not already running
default	19:21:47.821965-0500	Nexy	                AUHAL.cpp:687   SelectDevice: (0xbb05cb140) disconnecting device 91
default	19:21:47.821974-0500	Nexy	                AUHAL.cpp:751   SelectDevice: (0xbb05cb140) destroying ioproc 0xc for device 91
default	19:21:47.822016-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xc}
default	19:21:47.822060-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	19:21:47.822247-0500	Nexy	                AUHAL.cpp:853   SelectDevice: (0xbb05cb140) nothing to setup
default	19:21:47.822266-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0xbb05cb140) adding 0 device listeners to device 0
default	19:21:47.822273-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0xbb05cb140) adding 0 device delegate listeners to device 0
default	19:21:47.822283-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0xbb05cb140) removing 7 device listeners from device 91
default	19:21:47.822524-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0xbb05cb140) removing 0 device delegate listeners from device 91
default	19:21:47.822544-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0xbb05cb140)
default	19:21:47.824999-0500	Nexy	                AUHAL.cpp:420   AUHAL: (0xbb05cb140) Selecting device 85 from constructor
default	19:21:47.825012-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0xbb05cb140)
default	19:21:47.825020-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0xbb05cb140) not already running
default	19:21:47.825026-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0xbb05cb140) nothing to teardown
default	19:21:47.825031-0500	Nexy	                AUHAL.cpp:762   SelectDevice: (0xbb05cb140) connecting device 85
default	19:21:47.825165-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0xbb05cb140) Device ID: 85 (Input:No | Output:Yes): true
default	19:21:47.825279-0500	Nexy	                AUHAL.cpp:774   SelectDevice: (0xbb05cb140) created ioproc 0xf for device 85
default	19:21:47.825417-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0xbb05cb140) adding 7 device listeners to device 85
default	19:21:47.825639-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0xbb05cb140) adding 0 device delegate listeners to device 85
default	19:21:47.825649-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0xbb05cb140)
default	19:21:47.825745-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  24000 Hz, Float32, interleaved
default	19:21:47.825757-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	19:21:47.825766-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  24000 Hz, Float32, interleaved
default	19:21:47.825784-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	19:21:47.825797-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	19:21:47.825916-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0xbb05cb140) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	19:21:47.825930-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0xbb05cb140) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	19:21:47.825937-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	19:21:47.825942-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0xbb05cb140) removing 0 device listeners from device 0
default	19:21:47.825948-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0xbb05cb140) removing 0 device delegate listeners from device 0
default	19:21:47.825953-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0xbb05cb140)
default	19:21:47.825972-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is DISABLED
default	19:21:47.826033-0500	Nexy	                AUHAL.cpp:2303  SetProperty: (0xbb05cb140) caller requesting device change from 85 to 91
default	19:21:47.826045-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0xbb05cb140)
default	19:21:47.826051-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0xbb05cb140) not already running
default	19:21:47.826056-0500	Nexy	                AUHAL.cpp:687   SelectDevice: (0xbb05cb140) disconnecting device 85
default	19:21:47.826062-0500	Nexy	                AUHAL.cpp:751   SelectDevice: (0xbb05cb140) destroying ioproc 0xf for device 85
default	19:21:47.826082-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped Unknown {1C-77-54-18-C8-A3:output, 0xf}
default	19:21:47.826114-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	19:21:47.826200-0500	Nexy	                AUHAL.cpp:762   SelectDevice: (0xbb05cb140) connecting device 91
default	19:21:47.826297-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0xbb05cb140) Device ID: 91 (Input:Yes | Output:No): true
default	19:21:47.828435-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=411.1513, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=5767, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=398, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	19:21:47.831815-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] from originator [app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] with description <RBSAssertionDescriptor| "AudioHAL" ID:403-5767-153891 target:5767 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	19:21:47.831959-0500	runningboardd	Assertion 403-5767-153891 (target:[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767]) will be created as active
default	19:21:47.836543-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] Ignoring jetsam update because this process is not memory-managed
default	19:21:47.836687-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] Ignoring suspend because this process is not lifecycle managed
default	19:21:47.836751-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] Ignoring GPU update because this process is not GPU managed
default	19:21:47.836963-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] Ignoring memory limit update because this process is not memory-managed
default	19:21:47.838893-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xc}
default	19:21:47.839040-0500	tccd	AUTHREQ_SUBJECT: msgID=411.1513, subject=com.nexy.assistant,
default	19:21:47.839745-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1e8048","name":"Nexy(5767)"}, "details":{"deviceUIDs":["1C-77-54-18-C8-A3:output"],"implicit_category":"MediaPlayback","input_running":false,"output_running":true} }
default	19:21:47.839863-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 73, PID = 5767, Name = sid:0x1e8048, Nexy(5767), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	19:21:47.839894-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Category/Mode changed -- The score for sid:0x1e8048, Nexy(5767), 'prim'/com.nexy.assistant was not correct. Old score = 201
default	19:21:47.839926-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 73, PID = 5767, Name = sid:0x1e8048, Nexy(5767), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	19:21:47.839972-0500	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1e8048, Nexy(5767), 'prim'', AudioCategory changed to 'MediaPlayback'
default	19:21:47.840034-0500	audiomxd	UpdateAudioState CID 0x4D120001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	19:21:47.840225-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	19:21:47.840084-0500	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 73, PID = 5767, Name = sid:0x1e8048, Nexy(5767), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO> is going active
default	19:21:47.840276-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	19:21:47.840118-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsPlaying:]: MXCoreSession com.nexy.assistant with category/mode MediaPlayback/Default and coreSessionID = 73 starting playing
default	19:21:47.840317-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 73, PID = 5767, Name = sid:0x1e8048, Nexy(5767), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	19:21:47.840425-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 73, PID = 5767, Name = sid:0x1e8048, Nexy(5767), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO>
default	19:21:47.840502-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1e8048, Nexy(5767), 'prim'', displayID:'com.nexy.assistant'}
default	19:21:47.840595-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Will try to see if we can get the shared route for session = <ID: 73, PID = 5767, Name = sid:0x1e8048, Nexy(5767), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO>. Old (200) and New (201) scores.
default	19:21:47.840887-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 1]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)}
default	19:21:47.840897-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	19:21:47.840774-0500	audiomxd	AudioApplicationInfoImpl.mm:395   Successfully updated session 0x1e8048 to isSessionRecording: 0
	app: {"name":"[implicit] Nexy","pid":5767}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1e8048, sessionType: 'prim', isRecording: false }, 
]
default	19:21:47.841160-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 201 flag 0x1 < Hijack > app com.nexy.assistant CID 0x4D120001 category Not set
default	19:21:47.840717-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 201, deviceID = <private>
default	19:21:47.840612-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc79244300 at /Applications/Nexy.app
default	19:21:47.842391-0500	audiomxd	UpdateAudioState CID 0x4D120001 audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	19:21:47.842487-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 201,
}
default	19:21:47.842518-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	19:21:47.842531-0500	audioaccessoryd	AudioStateChanged: Added audio session app com.nexy.assistant NULL -> 201 count 1
default	19:21:47.842540-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 201
error	19:21:47.842552-0500	audioaccessoryd	Updating local audio category 100 -> 201 app com.nexy.assistant
default	19:21:47.842608-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.nexy.assistant
default	19:21:47.844135-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	19:21:47.844541-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] Ignoring jetsam update because this process is not memory-managed
default	19:21:47.844569-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] from originator [osservice<com.apple.powerd>:338] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:403-338-153892 target:5767 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	19:21:47.844615-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] Ignoring suspend because this process is not lifecycle managed
default	19:21:47.844744-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] Ignoring GPU update because this process is not GPU managed
default	19:21:47.844752-0500	ControlCenter	Received state update for 5767 (app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>, running-active-NotVisible
default	19:21:47.844842-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] Ignoring memory limit update because this process is not memory-managed
default	19:21:47.844880-0500	runningboardd	Assertion 403-338-153892 (target:[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767]) will be created as active
default	19:21:47.845010-0500	gamepolicyd	Received state update for 5767 (app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>, running-active-NotVisible
default	19:21:47.848659-0500	Nexy	[com.apple.controlcenter:9D7A84EB-09FA-419F-B4B9-E26DC2689304] Sending action(s) in update: NSSceneFenceAction
default	19:21:47.851038-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	19:21:47.851439-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] Ignoring jetsam update because this process is not memory-managed
default	19:21:47.851459-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] Ignoring suspend because this process is not lifecycle managed
default	19:21:47.851476-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] Ignoring GPU update because this process is not GPU managed
default	19:21:47.851521-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] Ignoring memory limit update because this process is not memory-managed
default	19:21:47.859004-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	19:21:47.886055-0500	Nexy	                AUHAL.cpp:774   SelectDevice: (0xbb05cb140) created ioproc 0xd for device 91
default	19:21:47.886239-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0xbb05cb140) adding 7 device listeners to device 91
default	19:21:47.886436-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0xbb05cb140) adding 0 device delegate listeners to device 91
default	19:21:47.886445-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0xbb05cb140)
default	19:21:47.886457-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 output streams; not all mono
default	19:21:47.886472-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	19:21:47.886626-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  input stream 0 [0x5c]:  1 ch,  24000 Hz, Float32
default	19:21:47.886636-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 input streams; all mono
default	19:21:47.886641-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  1 ch,  24000 Hz, Float32
default	19:21:47.886725-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0xbb05cb140) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	19:21:47.886743-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0xbb05cb140) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	19:21:47.886748-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	19:21:47.886754-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0xbb05cb140) removing 7 device listeners from device 85
default	19:21:47.886903-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0xbb05cb140) removing 0 device delegate listeners from device 85
default	19:21:47.886910-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0xbb05cb140)
default	19:21:47.886920-0500	Nexy	AudioHardware-mac-imp.cpp:1306   AudioObjectAddPropertyListener: listener was already added
default	19:21:47.887540-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	19:21:47.889050-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=411.1514, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=5767, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=398, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	19:21:47.890429-0500	tccd	AUTHREQ_SUBJECT: msgID=411.1514, subject=com.nexy.assistant,
default	19:21:47.891138-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc79244300 at /Applications/Nexy.app
default	19:21:47.922324-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	19:21:47.923558-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=411.1515, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=5767, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=398, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	19:21:47.924765-0500	tccd	AUTHREQ_SUBJECT: msgID=411.1515, subject=com.nexy.assistant,
default	19:21:47.925405-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc79244300 at /Applications/Nexy.app
default	19:21:47.949564-0500	ControlCenter	Received state update for 5767 (app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>, running-active-NotVisible
default	19:21:47.949668-0500	gamepolicyd	Received state update for 5767 (app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>, running-active-NotVisible
default	19:21:48.078402-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Output {1C-77-54-18-C8-A3:output, 0xc}
default	19:21:48.078756-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1e8048","name":"Nexy(5767)"}, "details":{"deviceUIDs":[],"implicit_category":"","input_running":false,"output_running":false} }
default	19:21:48.078835-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsPlaying:]: MXCoreSession com.nexy.assistant with category/mode MediaPlayback/Default and coreSessionID = 73 stopping playing
default	19:21:48.078874-0500	audiomxd	-MXCoreSession- -[MXCoreSession endInterruption:]: Session <ID: 73, PID = 5767, Name = sid:0x1e8048, Nexy(5767), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> is going inactive
default	19:21:48.078907-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 73, PID = 5767, Name = sid:0x1e8048, Nexy(5767), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	19:21:48.078973-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 73, PID = 5767, Name = sid:0x1e8048, Nexy(5767), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	19:21:48.079108-0500	audiomxd	UpdateAudioState CID 0x4D120001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	19:21:48.079155-0500	audiomxd	AudioApplicationInfoImpl.mm:395   Successfully updated session 0x1e8048 to isSessionRecording: 0
	app: {"name":"[implicit] Nexy","pid":5767}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1e8048, sessionType: 'prim', isRecording: false }, 
]
default	19:21:48.079245-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 0]. BT device UIDS: {(
)}
default	19:21:48.079265-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	19:21:48.079267-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	19:21:48.079313-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	19:21:48.079333-0500	audioaccessoryd	AudioStateChanged: Removed audio session app com.nexy.assistant 201 count 0
default	19:21:48.083198-0500	runningboardd	Invalidating assertion 403-5767-153891 (target:[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767]) from originator [app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767]
default	19:21:48.083283-0500	runningboardd	Invalidating assertion 403-338-153892 (target:[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767]) from originator [osservice<com.apple.powerd>:338]
default	19:21:48.188061-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] Ignoring jetsam update because this process is not memory-managed
default	19:21:48.188082-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] Ignoring suspend because this process is not lifecycle managed
default	19:21:48.188093-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] Ignoring GPU update because this process is not GPU managed
default	19:21:48.188112-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] Ignoring memory limit update because this process is not memory-managed
default	19:21:48.191353-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	19:21:48.191926-0500	ControlCenter	Received state update for 5767 (app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>, running-active-NotVisible
default	19:21:48.192092-0500	gamepolicyd	Received state update for 5767 (app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>, running-active-NotVisible
default	19:21:48.470140-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] from originator [app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] with description <RBSAssertionDescriptor| "AudioHAL" ID:403-5767-153894 target:5767 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	19:21:48.470329-0500	runningboardd	Assertion 403-5767-153894 (target:[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767]) will be created as active
default	19:21:48.471065-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] Ignoring jetsam update because this process is not memory-managed
default	19:21:48.471095-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] Ignoring suspend because this process is not lifecycle managed
default	19:21:48.471117-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] Ignoring GPU update because this process is not GPU managed
default	19:21:48.471191-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] Ignoring memory limit update because this process is not memory-managed
default	19:21:48.472934-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=411.1516, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=5767, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=398, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	19:21:48.476000-0500	tccd	AUTHREQ_SUBJECT: msgID=411.1516, subject=com.nexy.assistant,
default	19:21:48.476788-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	19:21:48.477521-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc79244300 at /Applications/Nexy.app
default	19:21:48.477588-0500	ControlCenter	Received state update for 5767 (app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>, running-active-NotVisible
default	19:21:48.477890-0500	gamepolicyd	Received state update for 5767 (app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>, running-active-NotVisible
default	19:21:48.507544-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Input {1C-77-54-18-C8-A3:input, 0xd}
default	19:21:48.510826-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1e8048","name":"Nexy(5767)"}, "details":{"deviceUIDs":["1C-77-54-18-C8-A3:input"],"implicit_category":"Record","input_running":true,"output_running":false} }
default	19:21:48.510935-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 73, PID = 5767, Name = sid:0x1e8048, Nexy(5767), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	19:21:48.510967-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Category/Mode changed -- The score for sid:0x1e8048, Nexy(5767), 'prim'/com.nexy.assistant was not correct. Old score = 201
default	19:21:48.510993-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 73, PID = 5767, Name = sid:0x1e8048, Nexy(5767), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	19:21:48.511159-0500	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1e8048, Nexy(5767), 'prim'', AudioCategory changed to 'Record_WithBluetooth'
default	19:21:48.511322-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 73, PID = 5767, Name = sid:0x1e8048, Nexy(5767), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	19:21:48.511368-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 73, PID = 5767, Name = sid:0x1e8048, Nexy(5767), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	19:21:48.511260-0500	audiomxd	UpdateAudioState CID 0x4D120001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	19:21:48.511420-0500	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 73, PID = 5767, Name = sid:0x1e8048, Nexy(5767), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> is going active
default	19:21:48.511431-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1e8048, Nexy(5767), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 73 starting recording
default	19:21:48.511548-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 73, PID = 5767, Name = sid:0x1e8048, Nexy(5767), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	19:21:48.511523-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	19:21:48.511621-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 73, PID = 5767, Name = sid:0x1e8048, Nexy(5767), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	19:21:48.511562-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	19:21:48.511595-0500	audiomxd	UpdateAudioState CID 0x4D120001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	19:21:48.511496-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] from originator [osservice<com.apple.powerd>:338] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:403-338-153895 target:5767 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	19:21:48.511651-0500	runningboardd	Assertion 403-338-153895 (target:[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767]) will be created as active
default	19:21:48.511734-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	19:21:48.511812-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	19:21:48.512221-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] Ignoring jetsam update because this process is not memory-managed
default	19:21:48.512233-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] Ignoring suspend because this process is not lifecycle managed
default	19:21:48.511780-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [1, 0]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:input"
)}
default	19:21:48.512265-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] Ignoring GPU update because this process is not GPU managed
default	19:21:48.511684-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1e8048, Nexy(5767), 'prim'', displayID:'com.nexy.assistant'}
default	19:21:48.511790-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	19:21:48.512168-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 200 flag 0x1 < Hijack > app com.nexy.assistant CID 0x4D120001 category Not set
default	19:21:48.511821-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	19:21:48.512336-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] Ignoring memory limit update because this process is not memory-managed
default	19:21:48.513576-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	19:21:48.513509-0500	audiomxd	UpdateAudioState CID 0x4D120001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	19:21:48.513602-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	19:21:48.513614-0500	audioaccessoryd	AudioStateChanged: Added audio session app com.nexy.assistant NULL -> 200 count 1
default	19:21:48.513622-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
error	19:21:48.513667-0500	audioaccessoryd	Updating local audio category 100 -> 200 app com.nexy.assistant
default	19:21:48.514075-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	19:21:48.517596-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	19:21:48.518110-0500	ControlCenter	Received state update for 5767 (app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>, running-active-NotVisible
default	19:21:48.518275-0500	gamepolicyd	Received state update for 5767 (app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>, running-active-NotVisible
default	19:21:48.520895-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	19:21:48.520988-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	19:21:48.521045-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	19:21:48.521790-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	19:21:48.521802-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	19:21:48.521816-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	19:21:48.521823-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	19:21:48.521831-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	19:21:48.521838-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	19:21:48.521852-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	19:21:48.521866-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	19:21:48.521888-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	19:21:48.521918-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	19:21:48.521948-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	19:21:48.521966-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	19:21:48.522166-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	19:21:48.522800-0500	ControlCenter	Navigating to new application [com.nexy.assistant]
default	19:21:48.522924-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	19:21:48.522937-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	19:21:48.522947-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	19:21:48.522953-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	19:21:48.522959-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	19:21:48.522965-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	19:21:50.209110-0500	Nexy	[0xbafc9a800] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	19:21:50.210408-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=5767.5, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=5767, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	19:21:50.212097-0500	tccd	AUTHREQ_SUBJECT: msgID=5767.5, subject=com.nexy.assistant,
default	19:21:50.213109-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x92f178000 at /Applications/Nexy.app
default	19:21:50.250475-0500	Nexy	[0xbafc9a800] invalidated after the last release of the connection object
default	19:21:50.251773-0500	Nexy	 [INFO] SLSHWCaptureDesktopProxying:485 request: <private>
default	19:21:50.254348-0500	Nexy	[0xbafc9a800] activating connection: mach=true listener=false peer=false name=com.apple.replayd
default	19:21:50.254590-0500	Nexy	 [INFO] -[RPDaemonProxy consumeSandboxExtension:processNewConnection:]:568
default	19:21:50.255151-0500	Nexy	 [INFO] -[RPDaemonProxy proxyCoreGraphicsWithMethodType:config:machPort:completionHandler:]:1493
default	19:21:50.265744-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=3439.2, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=5767, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.replayd, pid=3439, auid=501, euid=501, binary_path=/usr/libexec/replayd}, },
default	19:21:50.265774-0500	tccd	requestor: TCCDProcess: identifier=com.apple.replayd, pid=3439, auid=501, euid=501, binary_path=/usr/libexec/replayd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=5767, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	19:21:50.266848-0500	tccd	AUTHREQ_SUBJECT: msgID=3439.2, subject=com.nexy.assistant,
default	19:21:50.267534-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x92f178000 at /Applications/Nexy.app
default	19:21:50.308239-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=397.2640, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=5767, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=397, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	19:21:50.308271-0500	tccd	requestor: TCCDProcess: identifier=com.apple.WindowServer, pid=397, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=5767, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	19:21:50.309149-0500	tccd	AUTHREQ_SUBJECT: msgID=397.2640, subject=com.nexy.assistant,
default	19:21:50.309773-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x92f178000 at /Applications/Nexy.app
default	19:21:50.379064-0500	Nexy	 [INFO] SLSHWCaptureDesktopProxying_block_invoke:506 request: <private>, error: (null), windowInfo: (null)
default	19:21:50.416812-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	19:21:50.422246-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	19:21:50.422399-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant), [scr] Nexy (com.nexy.assistant)]
default	19:21:50.422452-0500	ControlCenter	Active activity attributions changed to ["scr:com.nexy.assistant", "mic:com.nexy.assistant"]
default	19:21:50.424262-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	19:21:50.424274-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	19:21:50.424288-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	19:21:50.424297-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	19:21:50.424304-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	19:21:50.424312-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	19:21:50.424341-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	19:21:50.424349-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	19:21:50.424355-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	19:21:50.424360-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	19:21:50.424367-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	19:21:50.424374-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	19:21:50.424504-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	19:21:50.424595-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	19:21:50.424602-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	19:21:50.424611-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	19:21:50.424618-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	19:21:50.424623-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	19:21:50.424629-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	19:21:50.555700-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xd}
default	19:21:50.556066-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1e8048","name":"Nexy(5767)"}, "details":{"deviceUIDs":[],"implicit_category":"","input_running":false,"output_running":false} }
default	19:21:50.556163-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 73, PID = 5767, Name = sid:0x1e8048, Nexy(5767), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	19:21:50.556216-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 73, PID = 5767, Name = sid:0x1e8048, Nexy(5767), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	19:21:50.556241-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1e8048, Nexy(5767), 'prim'', displayID:'com.nexy.assistant'}
default	19:21:50.556291-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1e8048, Nexy(5767), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 73 stopping recording
default	19:21:50.556304-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	19:21:50.556318-0500	audiomxd	-MXCoreSession- -[MXCoreSession endInterruption:]: Session <ID: 73, PID = 5767, Name = sid:0x1e8048, Nexy(5767), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> is going inactive
default	19:21:50.556348-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 73, PID = 5767, Name = sid:0x1e8048, Nexy(5767), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	19:21:50.556389-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 73, PID = 5767, Name = sid:0x1e8048, Nexy(5767), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	19:21:50.556500-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 0]. BT device UIDS: {(
)}
default	19:21:50.556514-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	19:21:50.556565-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 200 flag 0x1 < Hijack > app com.nexy.assistant CID 0x4D120001 category Not set
default	19:21:50.557673-0500	runningboardd	Invalidating assertion 403-5767-153894 (target:[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767]) from originator [app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767]
default	19:21:50.558969-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	19:21:50.558928-0500	runningboardd	Invalidating assertion 403-338-153895 (target:[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767]) from originator [osservice<com.apple.powerd>:338]
default	19:21:50.559010-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	19:21:50.558891-0500	audiomxd	UpdateAudioState CID 0x4D120001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	19:21:50.559041-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	19:21:50.558929-0500	audiomxd	UpdateAudioState CID 0x4D120001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	19:21:50.559108-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	19:21:50.559134-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	19:21:50.559154-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	19:21:50.559165-0500	audioaccessoryd	AudioStateChanged: Removed audio session app com.nexy.assistant 201 count 0
default	19:21:50.565654-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	19:21:50.565762-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant)]
default	19:21:50.565844-0500	ControlCenter	Active activity attributions changed to ["scr:com.nexy.assistant"]
default	19:21:50.565876-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	19:21:50.580468-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	19:21:50.580566-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	19:21:50.580745-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	19:21:50.580816-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	19:21:50.580890-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	19:21:50.581084-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	19:21:50.581686-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	19:21:50.658997-0500	Nexy	                AUHAL.cpp:473   ~AUHAL: (0xbb05cb140) Selecting device 0 from destructor
default	19:21:50.659019-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0xbb05cb140)
default	19:21:50.659030-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0xbb05cb140) not already running
default	19:21:50.659039-0500	Nexy	                AUHAL.cpp:687   SelectDevice: (0xbb05cb140) disconnecting device 91
default	19:21:50.659051-0500	Nexy	                AUHAL.cpp:751   SelectDevice: (0xbb05cb140) destroying ioproc 0xd for device 91
default	19:21:50.659097-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xd}
default	19:21:50.659147-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	19:21:50.659357-0500	Nexy	                AUHAL.cpp:853   SelectDevice: (0xbb05cb140) nothing to setup
default	19:21:50.659383-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0xbb05cb140) adding 0 device listeners to device 0
default	19:21:50.659393-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0xbb05cb140) adding 0 device delegate listeners to device 0
default	19:21:50.659401-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0xbb05cb140) removing 7 device listeners from device 91
default	19:21:50.660059-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0xbb05cb140) removing 0 device delegate listeners from device 91
default	19:21:50.660135-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0xbb05cb140)
default	19:21:50.662599-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] Ignoring jetsam update because this process is not memory-managed
default	19:21:50.662619-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] Ignoring suspend because this process is not lifecycle managed
default	19:21:50.662632-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] Ignoring GPU update because this process is not GPU managed
default	19:21:50.662659-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] Ignoring memory limit update because this process is not memory-managed
default	19:21:50.666403-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	19:21:50.666920-0500	ControlCenter	Received state update for 5767 (app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>, running-active-NotVisible
default	19:21:50.667448-0500	gamepolicyd	Received state update for 5767 (app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>, running-active-NotVisible
default	19:21:50.949019-0500	Nexy	nw_path_libinfo_path_check [E6861503-E32F-4D9F-BD00-78F0C4E9457A Hostname#8918c827:80 tcp, legacy-socket, attribution: developer]
	libinfo check path: <private>
default	19:21:50.949404-0500	mDNSResponder	[R145935] DNSServiceCreateConnection START PID[5767](Nexy)
default	19:21:50.949501-0500	mDNSResponder	[R145936] DNSServiceQueryRecord START -- qname: <mask.hash: 'HKLMzXHw1FEmCUQzpEBEqw=='>, qtype: A, flags: 0x1D000, interface index: 0, client pid: 5767 (Nexy), name hash: b360ab20
default	19:21:50.950212-0500	mDNSResponder	[R145937] DNSServiceQueryRecord START -- qname: <mask.hash: 'HKLMzXHw1FEmCUQzpEBEqw=='>, qtype: AAAA, flags: 0x1D000, interface index: 0, client pid: 5767 (Nexy), name hash: b360ab20
default	19:21:50.978023-0500	kernel	SK[3]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 6C499A13-8E71-4098-867D-D00AECCAB57E flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.55022,dst=<IPv4-redacted>.80,proto=0x06 mask=0x0000003f,hash=0x301a9648 tp_proto=0x06"
default	19:21:50.978100-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:55022<-><IPv4-redacted>:80] interface: utun6 (skipped: 47531)
so_gencnt: 2851982 t_state: SYN_SENT process: Nexy:5767 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x890801ae
default	19:21:50.978566-0500	kernel	tcp connected: [<IPv4-redacted>:55022<-><IPv4-redacted>:80] interface: utun6 (skipped: 47531)
so_gencnt: 2851982 t_state: ESTABLISHED process: Nexy:5767 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x890801ae
default	19:21:51.395251-0500	kernel	tcp_connection_summary (tcp_usrclosed:3220)[<IPv4-redacted>:55022<-><IPv4-redacted>:80] interface: utun6 (skipped: 47531)
so_gencnt: 2851982 t_state: LAST_ACK process: Nexy:5767 Duration: 0.418 sec Conn_Time: 0.001 sec bytes in/out: 380/37922 pkts in/out: 2/12 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 1.125 ms rttvar: 0.500 ms base rtt: 1 ms so_error: 0 svc/tc: 0 flow: 0x890801ae
default	19:21:51.395292-0500	kernel	tcp_connection_summary [<IPv4-redacted>:55022<-><IPv4-redacted>:80] interface: utun6 (skipped: 47531)
so_gencnt: 2851982 t_state: LAST_ACK process: Nexy:5767 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 1/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	19:21:51.409176-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] from originator [app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] with description <RBSAssertionDescriptor| "AudioHAL" ID:403-5767-153900 target:5767 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	19:21:51.409303-0500	runningboardd	Assertion 403-5767-153900 (target:[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767]) will be created as active
default	19:21:51.409876-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] Ignoring jetsam update because this process is not memory-managed
default	19:21:51.409878-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] from originator [osservice<com.apple.powerd>:338] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:403-338-153901 target:5767 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	19:21:51.409914-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] Ignoring suspend because this process is not lifecycle managed
default	19:21:51.409981-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] Ignoring GPU update because this process is not GPU managed
default	19:21:51.410013-0500	runningboardd	Assertion 403-338-153901 (target:[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767]) will be created as active
default	19:21:51.410053-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] Ignoring memory limit update because this process is not memory-managed
default	19:21:51.416523-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xc}
default	19:21:51.418354-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1e8048","name":"Nexy(5767)"}, "details":{"deviceUIDs":["1C-77-54-18-C8-A3:output"],"implicit_category":"MediaPlayback","input_running":false,"output_running":true} }
default	19:21:51.418476-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 73, PID = 5767, Name = sid:0x1e8048, Nexy(5767), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	19:21:51.418518-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Category/Mode changed -- The score for sid:0x1e8048, Nexy(5767), 'prim'/com.nexy.assistant was not correct. Old score = 201
default	19:21:51.418549-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 73, PID = 5767, Name = sid:0x1e8048, Nexy(5767), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	19:21:51.418600-0500	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1e8048, Nexy(5767), 'prim'', AudioCategory changed to 'MediaPlayback'
default	19:21:51.418651-0500	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 73, PID = 5767, Name = sid:0x1e8048, Nexy(5767), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO> is going active
default	19:21:51.418665-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsPlaying:]: MXCoreSession com.nexy.assistant with category/mode MediaPlayback/Default and coreSessionID = 73 starting playing
default	19:21:51.418656-0500	audiomxd	UpdateAudioState CID 0x4D120001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	19:21:51.418894-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	19:21:51.418946-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	19:21:51.418889-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 73, PID = 5767, Name = sid:0x1e8048, Nexy(5767), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	19:21:51.418932-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 73, PID = 5767, Name = sid:0x1e8048, Nexy(5767), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO>
default	19:21:51.418962-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1e8048, Nexy(5767), 'prim'', displayID:'com.nexy.assistant'}
default	19:21:51.419017-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Will try to see if we can get the shared route for session = <ID: 73, PID = 5767, Name = sid:0x1e8048, Nexy(5767), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO>. Old (200) and New (201) scores.
default	19:21:51.419377-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 1]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)}
default	19:21:51.419404-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	19:21:51.419178-0500	audiomxd	AudioApplicationInfoImpl.mm:395   Successfully updated session 0x1e8048 to isSessionRecording: 0
	app: {"name":"[implicit] Nexy","pid":5767}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1e8048, sessionType: 'prim', isRecording: false }, 
]
default	19:21:51.419187-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 201, deviceID = <private>
default	19:21:51.419641-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 201 flag 0x1 < Hijack > app com.nexy.assistant CID 0x4D120001 category Not set
default	19:21:51.420792-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 201,
}
default	19:21:51.420814-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	19:21:51.420705-0500	audiomxd	UpdateAudioState CID 0x4D120001 audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	19:21:51.420825-0500	audioaccessoryd	AudioStateChanged: Added audio session app com.nexy.assistant NULL -> 201 count 1
default	19:21:51.420836-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 201
error	19:21:51.420845-0500	audioaccessoryd	Updating local audio category 100 -> 201 app com.nexy.assistant
default	19:21:51.420891-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.nexy.assistant
default	19:21:51.422138-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	19:21:51.422522-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] Ignoring jetsam update because this process is not memory-managed
default	19:21:51.422540-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] Ignoring suspend because this process is not lifecycle managed
default	19:21:51.422557-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] Ignoring GPU update because this process is not GPU managed
default	19:21:51.422687-0500	ControlCenter	Received state update for 5767 (app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>, running-active-NotVisible
default	19:21:51.422612-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] Ignoring memory limit update because this process is not memory-managed
default	19:21:51.422996-0500	gamepolicyd	Received state update for 5767 (app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>, running-active-NotVisible
default	19:21:51.425451-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	19:21:51.425905-0500	ControlCenter	Received state update for 5767 (app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>, running-active-NotVisible
default	19:21:51.426007-0500	gamepolicyd	Received state update for 5767 (app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>, running-active-NotVisible
default	19:21:51.426000-0500	Nexy	[com.apple.controlcenter:9D7A84EB-09FA-419F-B4B9-E26DC2689304] Sending action(s) in update: NSSceneFenceAction
default	19:21:51.654275-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Output {1C-77-54-18-C8-A3:output, 0xc}
default	19:21:51.654782-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1e8048","name":"Nexy(5767)"}, "details":{"deviceUIDs":[],"implicit_category":"","input_running":false,"output_running":false} }
default	19:21:51.654913-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsPlaying:]: MXCoreSession com.nexy.assistant with category/mode MediaPlayback/Default and coreSessionID = 73 stopping playing
default	19:21:51.654993-0500	audiomxd	-MXCoreSession- -[MXCoreSession endInterruption:]: Session <ID: 73, PID = 5767, Name = sid:0x1e8048, Nexy(5767), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> is going inactive
default	19:21:51.655062-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 73, PID = 5767, Name = sid:0x1e8048, Nexy(5767), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	19:21:51.655163-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 73, PID = 5767, Name = sid:0x1e8048, Nexy(5767), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	19:21:51.655287-0500	audiomxd	UpdateAudioState CID 0x4D120001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	19:21:51.655505-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	19:21:51.655381-0500	audiomxd	AudioApplicationInfoImpl.mm:395   Successfully updated session 0x1e8048 to isSessionRecording: 0
	app: {"name":"[implicit] Nexy","pid":5767}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1e8048, sessionType: 'prim', isRecording: false }, 
]
default	19:21:51.655493-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 0]. BT device UIDS: {(
)}
default	19:21:51.655589-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	19:21:51.655518-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	19:21:51.655631-0500	audioaccessoryd	AudioStateChanged: Removed audio session app com.nexy.assistant 201 count 0
default	19:21:51.660336-0500	runningboardd	Invalidating assertion 403-5767-153900 (target:[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767]) from originator [app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767]
default	19:21:51.660516-0500	runningboardd	Invalidating assertion 403-338-153901 (target:[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767]) from originator [osservice<com.apple.powerd>:338]
default	19:21:51.765714-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] Ignoring jetsam update because this process is not memory-managed
default	19:21:51.765753-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] Ignoring suspend because this process is not lifecycle managed
default	19:21:51.765778-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] Ignoring GPU update because this process is not GPU managed
default	19:21:51.765825-0500	runningboardd	[app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>:5767] Ignoring memory limit update because this process is not memory-managed
default	19:21:51.772543-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	19:21:51.773294-0500	ControlCenter	Received state update for 5767 (app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>, running-active-NotVisible
default	19:21:51.773484-0500	gamepolicyd	Received state update for 5767 (app<application.com.nexy.assistant.27212639.27212645.43E8CDFA-0251-44BF-9B41-34BB73B80B0D(501)>, running-active-NotVisible
default	19:21:52.784035-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(10301)
default	19:21:52.784109-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:10301 called from <private>
default	19:21:52.784127-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:10301 called from <private>
default	19:21:52.784167-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(10300)
default	19:21:52.784265-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:10300 called from <private>
default	19:21:52.784286-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:10300 called from <private>
default	19:21:52.788811-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:10300 called from <private>
default	19:21:52.788839-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:10300 called from <private>
default	19:21:52.788985-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(10300)
default	19:21:52.789005-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:10300 called from <private>
default	19:21:52.789012-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:10300 called from <private>
default	19:21:52.793648-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(10300)
default	19:21:52.793704-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:10300 called from <private>
default	19:21:52.793710-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:10300 called from <private>
default	19:21:52.794775-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(10300)
default	19:21:52.795043-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(10300)
default	19:21:52.797930-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:10300 called from <private>
default	19:21:52.797946-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:10300 called from <private>
default	19:21:52.797960-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:10300 called from <private>
default	19:21:52.797971-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:10300 called from <private>
default	19:21:52.797979-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:10300 called from <private>
default	19:21:52.797985-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:10300 called from <private>
default	19:21:52.799412-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(10301)
default	19:21:52.799438-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:10301 called from <private>
default	19:21:52.799446-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:10301 called from <private>
default	19:21:52.801158-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(10300)
default	19:21:52.802154-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:10300 called from <private>
default	19:21:52.802169-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:10300 called from <private>
default	19:21:52.814943-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:10300 called from <private>
default	19:21:52.814975-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:10300 called from <private>
default	19:21:52.815067-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(10300)
default	19:21:52.818445-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(10300)
default	19:21:52.818794-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:10300 called from <private>
default	19:21:52.818808-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:10300 called from <private>
default	19:21:52.818945-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(10300)
default	19:21:52.823349-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(10300)
default	19:21:52.824177-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:10300 called from <private>
default	19:21:52.824191-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:10300 called from <private>
default	19:21:52.824223-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:10300 called from <private>
default	19:21:52.824229-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:10300 called from <private>
default	19:21:52.824238-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:10300 called from <private>
default	19:21:52.824243-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:10300 called from <private>
default	19:21:52.824294-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:10300 called from <private>
default	19:21:52.824364-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:10300 called from <private>
default	19:21:52.824434-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:10300 called from <private>
default	19:21:52.824529-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:10300 called from <private>
default	19:21:52.824594-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:10300 called from <private>
default	19:21:52.824703-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:10300 called from <private>
default	19:21:52.825540-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0xbb05cb840) Device ID: 85 (Input:No | Output:Yes): true
default	19:21:52.825556-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0xbb05cb840)
default	19:21:52.826045-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  48000 Hz, Float32, interleaved
default	19:21:52.826057-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	19:21:52.826065-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	19:21:52.826102-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	19:21:52.826112-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	19:21:52.827440-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	19:21:52.828672-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0xbb05cb840) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	19:21:52.828691-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0xbb05cb840) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	19:21:52.828699-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	19:21:52.830329-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0xbb05cb840) Device ID: 85 (Input:No | Output:Yes): true
default	19:21:52.830348-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0xbb05cb840)
default	19:21:52.831103-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  48000 Hz, Float32, interleaved
default	19:21:52.831119-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	19:21:52.831130-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	19:21:52.831144-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	19:21:52.831154-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	19:21:52.832413-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED