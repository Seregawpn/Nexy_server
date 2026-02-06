default	11:12:10.124620-0500	lsd	com.nexy.assistant/Unknown Persona:5:5:1:1:Building bundle record for app
default	11:12:10.124844-0500	lsd	com.nexy.assistant/Unknown Persona:5:5:2:1:Built bundle record for app
default	11:12:10.127192-0500	lsd	com.nexy.assistant/Unknown Persona:5:4:2:1:_LSServerRegisterItemInfo result = 0
default	11:12:10.147598-0500	runningboardd	Launch request for app<application.com.nexy.assistant.53053210.53053219(501)>[0] is using uid 501 (divined from auid 501 euid 501)
default	11:12:10.147742-0500	runningboardd	Acquiring assertion targeting app<application.com.nexy.assistant.53053210.53053219(501)> from originator [osservice<com.apple.coreservices.uiagent(501)>:75320] with description <RBSAssertionDescriptor| "LS launch com.nexy.assistant" ID:394-75320-34696 target:app<application.com.nexy.assistant.53053210.53053219(501)> attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"LaunchRoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	11:12:10.147891-0500	runningboardd	Assertion 394-75320-34696 (target:app<application.com.nexy.assistant.53053210.53053219(501)>) will be created as active
default	11:12:10.152168-0500	runningboardd	Checking PreventLaunch: global:0 exPath:/Applications/Nexy.app/Contents/MacOS/Nexy predicates:(null) allow:(null)
default	11:12:10.152223-0500	runningboardd	Creating and launching job for: app<application.com.nexy.assistant.53053210.53053219(501)>
default	11:12:10.152239-0500	runningboardd	_mutateContextIfNeeded called for com.nexy.assistant
default	11:12:10.152337-0500	runningboardd	app<application.com.nexy.assistant.53053210.53053219(501)>: -[RBPersonaManager personaForIdentity:context:personaUID:personaUniqueString:] required 0.001073 ms (wallclock); resolved to {4294967295, (null)}
default	11:12:10.159852-0500	dmd	Received xpc stream event (distributed notification matching) with name: com.apple.LaunchServices.applicationRegistered user info: {
    CFBundleDisplayName = Nexy;
    bundleIDs =     (
        "com.nexy.assistant"
    );
    isPlaceholder = 0;
}
default	11:12:10.216564-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78289] is not RunningBoard jetsam managed.
default	11:12:10.216588-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78289] This process will not be managed.
default	11:12:10.216603-0500	runningboardd	Now tracking process: [app<application.com.nexy.assistant.53053210.53053219(501)>:78289]
default	11:12:10.216788-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.53053210.53053219(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	11:12:10.218197-0500	gamepolicyd	Hit the server for a process handle 62c4f61000131d1 that resolved to: [app<application.com.nexy.assistant.53053210.53053219(501)>:78289]
default	11:12:10.218252-0500	gamepolicyd	Received state update for 78289 (app<application.com.nexy.assistant.53053210.53053219(501)>, running-active-NotVisible
default	11:12:10.224904-0500	runningboardd	Using default underlying assertion for app: [app<application.com.nexy.assistant.53053210.53053219(501)>:78289]
default	11:12:10.225049-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.53053210.53053219(501)>:78289] from originator [app<application.com.nexy.assistant.53053210.53053219(501)>:78289] with description <RBSAssertionDescriptor| "RB Underlying Assertion" ID:394-394-34697 target:78289 attributes:[
	<RBSDomainAttribute| domain:"com.apple.underlying" name:"defaultUnderlyingAppAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	11:12:10.225697-0500	runningboardd	Assertion 394-394-34697 (target:[app<application.com.nexy.assistant.53053210.53053219(501)>:78289]) will be created as active
default	11:12:10.253953-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.53053210.53053219(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	11:12:10.253827-0500	loginwindow	-[Application _updateInformationInternal] | Got App URL: file:///Applications/Nexy.app/
default	11:12:10.254074-0500	loginwindow	-[Application setState:] | enter: <Application: 0x8b953cd20: Nexy> state 2
default	11:12:10.254105-0500	loginwindow	-[ApplicationManager checkInAppContext:eventData:] | ApplicationManager: Checked in app : Nexy
default	11:12:10.257847-0500	gamepolicyd	Received state update for 78289 (app<application.com.nexy.assistant.53053210.53053219(501)>, running-active-NotVisible
default	11:12:10.351828-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78289] Ignoring jetsam update because this process is not memory-managed
default	11:12:10.351844-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78289] Ignoring suspend because this process is not lifecycle managed
default	11:12:10.351856-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78289] Ignoring GPU update because this process is not GPU managed
default	11:12:10.351881-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78289] Ignoring memory limit update because this process is not memory-managed
default	11:12:10.352658-0500	gamepolicyd	Received state update for 78289 (app<application.com.nexy.assistant.53053210.53053219(501)>, running-active-NotVisible
default	11:12:10.510375-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x93ad31e00 at /Applications/Nexy.app
default	11:12:10.801191-0500	Nexy	[0x1024552c0] activating connection: mach=true listener=false peer=false name=com.apple.cfprefsd.daemon
default	11:12:10.801275-0500	Nexy	[0x102455800] activating connection: mach=true listener=false peer=false name=com.apple.cfprefsd.agent
error	11:12:11.029814-0500	Nexy	dlsym cannot find symbol NSMakeRect in CFBundle 0x1024604a0 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	11:12:11.030035-0500	Nexy	dlsym cannot find symbol NSMakePoint in CFBundle 0x1024604a0 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	11:12:11.030240-0500	Nexy	dlsym cannot find symbol NSMakeSize in CFBundle 0x1024604a0 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	11:12:11.030441-0500	Nexy	dlsym cannot find symbol NSMakeRange in CFBundle 0x1024604a0 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
default	11:12:11.031909-0500	Nexy	[0x102453980] activating connection: mach=true listener=false peer=false name=com.apple.coreservices.launchservicesd
default	11:12:11.032543-0500	Nexy	[0x71600c000] activating connection: mach=true listener=false peer=false name=com.apple.analyticsd
default	11:12:11.032835-0500	Nexy	[0x71600c140] activating connection: mach=true listener=false peer=false name=com.apple.pasteboard.1
default	11:12:11.033191-0500	Nexy	[0x71600c280] activating connection: mach=true listener=false peer=false name=com.apple.distributed_notifications@Uv3
default	11:12:11.035193-0500	Nexy	void _NSDisableAutomaticTerminationAndLog(NSString *) No windows open yet
default	11:12:11.035525-0500	Nexy	[0x71600c3c0] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	11:12:11.036117-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=78289.1, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=78289, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	11:12:11.037693-0500	tccd	AUTHREQ_SUBJECT: msgID=78289.1, subject=com.nexy.assistant,
default	11:12:11.038465-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x93ad31e00 at /Applications/Nexy.app
default	11:12:11.052495-0500	Nexy	[0x71600c3c0] invalidated after the last release of the connection object
default	11:12:11.052849-0500	Nexy	server port 0x0000340b, session port 0x0000340b
default	11:12:11.053946-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=387.1593, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=78289, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=387, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	11:12:11.053981-0500	tccd	requestor: TCCDProcess: identifier=com.apple.WindowServer, pid=387, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=78289, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	11:12:11.055032-0500	tccd	AUTHREQ_SUBJECT: msgID=387.1593, subject=com.nexy.assistant,
default	11:12:11.055819-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x93ad31e00 at /Applications/Nexy.app
default	11:12:11.073822-0500	Nexy	Received configuration update from daemon (initial)
default	11:12:11.078047-0500	Nexy	New connection 0x12324b main
default	11:12:11.081150-0500	Nexy	CHECKIN: pid=78289
default	11:12:11.097182-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.53053210.53053219(501)>:78289] from originator [osservice<com.apple.coreservices.launchservicesd>:357] with description <RBSAssertionDescriptor| "uielement:78289" ID:394-357-34707 target:78289 attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"RoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	11:12:11.097306-0500	runningboardd	Assertion 394-357-34707 (target:[app<application.com.nexy.assistant.53053210.53053219(501)>:78289]) will be created as active
default	11:12:11.097702-0500	Nexy	CHECKEDIN: pid=78289 asn=0x0-0x292292 foreground=0
default	11:12:11.097527-0500	launchservicesd	CHECKIN:0x0-0x292292 78289 com.nexy.assistant
default	11:12:11.097691-0500	runningboardd	Invalidating assertion 394-357-34698 (target:[app<application.com.nexy.assistant.53053210.53053219(501)>:78289]) from originator [osservice<com.apple.coreservices.launchservicesd>:357]
default	11:12:11.097934-0500	Nexy	[0x71600c3c0] activating connection: mach=false listener=true peer=false name=(anonymous)
default	11:12:11.097944-0500	Nexy	[0x71600c3c0] Connection returned listener port: 0x4f03
default	11:12:11.098563-0500	loginwindow	-[Application _updateInformationInternal] | Got App URL: file:///Applications/Nexy.app/
default	11:12:11.098500-0500	Nexy	[0x714b50300] activating connection: mach=false listener=false peer=true name=com.apple.xpc.anonymous.0x71600c3c0.peer[357].0x714b50300
default	11:12:11.098655-0500	loginwindow	-[ApplicationManager checkInAppContext:eventData:] | ApplicationManager: Checked in app : Nexy
default	11:12:11.099523-0500	Nexy	FRONTLOGGING: version 1
default	11:12:11.099555-0500	Nexy	Registered, pid=78289 ASN=0x0,0x292292
default	11:12:11.099822-0500	WindowServer	12324b[CreateApplication]: Process creation: 0x0-0x292292 (Nexy) connectionID: 12324B pid: 78289 in session 0x101
default	11:12:11.100018-0500	Nexy	[0x71600c500] activating connection: mach=true listener=false peer=false name=com.apple.lsd.mapdb
default	11:12:11.101444-0500	Nexy	[0x71600c3c0] Connection returned listener port: 0x4f03
default	11:12:11.102269-0500	Nexy	BringForward: pid=78289 asn=0x0-0x292292 bringForward=0 foreground=0 uiElement=1 launchedByLS=1 modifiersCount=1 allDisabled=0
default	11:12:11.102485-0500	Nexy	BringFrontModifier: pid=78289 asn=0x0-0x292292 Modifier 0 hideAfter=0 hideOthers=0 dontMakeFrontmost=0 mouseDown=0/0 seed=0/0
default	11:12:11.103023-0500	Nexy	Current system appearance, (HLTB: 1), (SLS: 0)
default	11:12:11.104125-0500	Nexy	No persisted cache on this platform.
default	11:12:11.105098-0500	Nexy	Current system appearance, (HLTB: 1), (SLS: 0)
default	11:12:11.105614-0500	Nexy	Post-registration system appearance: (HLTB: 1)
default	11:12:11.108319-0500	Nexy	FBSWorkspace: endpoint monitoring is disabled.
default	11:12:11.108329-0500	Nexy	FBSWorkspace: default shell endpoint is disabled.
default	11:12:11.108381-0500	Nexy	Initializing connection
default	11:12:11.108419-0500	Nexy	Removing all cached process handles
default	11:12:11.108444-0500	Nexy	Sending handshake request attempt #1 to server
default	11:12:11.108452-0500	Nexy	Creating connection to com.apple.runningboard
default	11:12:11.108458-0500	Nexy	[0x71600c8c0] activating connection: mach=true listener=false peer=false name=com.apple.runningboard
default	11:12:11.108895-0500	runningboardd	Setting client for [app<application.com.nexy.assistant.53053210.53053219(501)>:78289] as ready
default	11:12:11.109638-0500	Nexy	Handshake succeeded
default	11:12:11.109653-0500	Nexy	Identity resolved as app<application.com.nexy.assistant.53053210.53053219(501)>
default	11:12:11.109947-0500	Nexy	[0x71600c3c0] Connection returned listener port: 0x4f03
default	11:12:11.114079-0500	distnoted	register name: com.apple.xctest.FakeForceTouchDevice object: com.nexy.assistant token: 1e0000001d pid: 78289
default	11:12:11.116478-0500	Nexy	[0x71600c3c0] Connection returned listener port: 0x4f03
default	11:12:11.119707-0500	Nexy	Created a new Process Instance Registry XPC connection (inactive)
default	11:12:11.119725-0500	Nexy	[0x71600c780] activating connection: mach=true listener=false peer=false name=com.apple.linkd.autoShortcut
default	11:12:11.119800-0500	Nexy	Activated connection to com.apple.linkd.autoShortcut (ApplicationService)
default	11:12:11.119837-0500	Nexy	[0x71600ca00] activating connection: mach=false listener=true peer=false name=(anonymous)
default	11:12:11.120907-0500	Nexy	[0x71600ca00] Connection returned listener port: 0x6e03
default	11:12:11.121488-0500	Nexy	Registered process with identifier 78289-596089
default	11:12:12.725624-0500	kernel	SK[7]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 33CC743F-7FFA-4644-9C49-42E0EA05B417 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.54634,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0x0636b050 tp_proto=0x06"
default	11:12:12.725747-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:54634<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 717472 t_state: SYN_SENT process: Nexy:78289 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xb41c3510
default	11:12:12.736562-0500	kernel	tcp connected: [<IPv4-redacted>:54634<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 717472 t_state: ESTABLISHED process: Nexy:78289 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xb41c3510
default	11:12:12.736877-0500	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:54634<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 717472 t_state: FIN_WAIT_1 process: Nexy:78289 Duration: 0.011 sec Conn_Time: 0.011 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 11.000 ms rttvar: 5.500 ms base rtt: 11 ms so_error: 0 svc/tc: 0 flow: 0xb41c3510
default	11:12:12.736887-0500	kernel	tcp_connection_summary [<IPv4-redacted>:54634<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 717472 t_state: FIN_WAIT_1 process: Nexy:78289 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	11:12:13.884978-0500	Nexy	Registered notify signal com.apple.caulk.alloc.rtdump (0)
default	11:12:13.888566-0500	Nexy	System_Input_Processing_Notification_Handler.mm:456   System_Input_Processing_Notification_Handler::is_vi_available(): Voice isolation DSP is available for client with bundle id com.nexy.assistant (AVFoundation is available, application is not in client deny list, application is not FaceTime variant)
default	11:12:13.893090-0500	Nexy	[0x71600cdc0] activating connection: mach=true listener=false peer=false name=com.apple.cmio.registerassistantservice.system-extensions
fault	11:12:13.898428-0500	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.53053210.53053219 AUID=501> and <type=Application identifier=application.com.nexy.assistant.53053210.53053219>
default	11:12:13.903997-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOInitializeListenersForBundleID: for <private> -> <private>
default	11:12:13.906668-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> vpio_preferenceChangedListener: new value ((null)) for key AUVoiceIOClients/com-nexy-assistant/AUVoiceIOChatFlavor, translatedBundleID com.nexy.assistant, bundleIDs {(
    "com.nexy.assistant"
)}
default	11:12:13.906810-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> vpio_preferenceChangedListener: new value ((null)) for key AUVoiceIOClients/com-nexy-assistant/AUVoiceIOIsAutoChatFlavorEnabled, translatedBundleID com.nexy.assistant, bundleIDs {(
    "com.nexy.assistant"
)}
default	11:12:13.906982-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetSupportedChatFlavorsForBundleID: <private>-><private> get supported chat flavors: <private>
default	11:12:13.906995-0500	Nexy	            HALSystem.cpp:134    Enabling HAL Voice Isolation support
default	11:12:13.907368-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetHiddenChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	11:12:13.907490-0500	Nexy	[0x71600cf00] activating connection: mach=true listener=false peer=false name=com.apple.tccd
default	11:12:13.908083-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=78289.2, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=78289, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	11:12:13.908616-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOHiddenChatFlavors newValue: (
    1
)
default	11:12:13.918142-0500	tccd	AUTHREQ_SUBJECT: msgID=78289.2, subject=com.nexy.assistant,
default	11:12:13.918936-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb2ed5c000 at /Applications/Nexy.app
default	11:12:13.931598-0500	Nexy	[0x71600cf00] invalidated after the last release of the connection object
default	11:12:13.931658-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetSupportedChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	11:12:13.934917-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOSupportedChatFlavors newValue: (
)
default	11:12:13.936945-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=399.682, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=78289, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	11:12:13.937966-0500	tccd	AUTHREQ_SUBJECT: msgID=399.682, subject=com.nexy.assistant,
default	11:12:13.938563-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb2ed5c000 at /Applications/Nexy.app
error	11:12:13.951291-0500	tccd	Request message contains a target_token to accessing_process (TCCDProcess: identifier=com.nexy.assistant, pid=78289, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy) but TCCDProcess: identifier=com.apple.audio.coreaudiod, pid=399, auid=202, euid=202, binary_path=/usr/sbin/coreaudiod is not a TCC manager for service: kTCCServiceScreenCapture.
default	11:12:13.952251-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=399.684, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=78289, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	11:12:13.953145-0500	tccd	AUTHREQ_SUBJECT: msgID=399.684, subject=com.nexy.assistant,
default	11:12:13.953690-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb2ed5c000 at /Applications/Nexy.app
default	11:12:13.969594-0500	Nexy	  HALPlugInManagement.cpp:440    HALPlugInManagement::RegisterPlugIns: skipping in-process plug-ins
error	11:12:13.970356-0500	Nexy	AddInstanceForFactory: No factory registered for id <CFUUID 0x716fc2dc0> F8BB1C28-BAE8-11D6-9C31-00039315CD46
default	11:12:13.991482-0500	Nexy	     HALC_ProxyObject.cpp:1456   HALC_Object_PropertyListener: not initialized
default	11:12:13.999269-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	11:12:14.999509-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	11:12:14.004936-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetPreferredChatFlavorForBundleID: <private>-><private> get value: 0
default	11:12:14.010327-0500	Nexy	[0x71600cf00] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioComponentRegistrar
default	11:12:14.025718-0500	Nexy	                AUHAL.cpp:420   AUHAL: (0x717674740) Selecting device 85 from constructor
default	11:12:14.025731-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0x717674740)
default	11:12:14.025736-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0x717674740) not already running
default	11:12:14.025893-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0x717674740) nothing to teardown
default	11:12:14.025898-0500	Nexy	                AUHAL.cpp:762   SelectDevice: (0x717674740) connecting device 85
default	11:12:14.025976-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0x717674740) Device ID: 85 (Input:No | Output:Yes): true
default	11:12:14.026060-0500	Nexy	                AUHAL.cpp:774   SelectDevice: (0x717674740) created ioproc 0xa for device 85
default	11:12:14.026173-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x717674740) adding 7 device listeners to device 85
default	11:12:14.026345-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x717674740) adding 0 device delegate listeners to device 85
default	11:12:14.026355-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x717674740)
default	11:12:14.026432-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  48000 Hz, Float32, interleaved
default	11:12:14.026441-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	11:12:14.026447-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	11:12:14.026453-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	11:12:14.026462-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	11:12:14.026559-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x717674740) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	11:12:14.026571-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x717674740) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	11:12:14.026576-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	11:12:14.026580-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x717674740) removing 0 device listeners from device 0
default	11:12:14.026586-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x717674740) removing 0 device delegate listeners from device 0
default	11:12:14.026597-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0x717674740)
default	11:12:14.026607-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is DISABLED
default	11:12:14.026981-0500	Nexy	                AUHAL.cpp:2303  SetProperty: (0x717674740) caller requesting device change from 85 to 91
default	11:12:14.026989-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0x717674740)
default	11:12:14.026994-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0x717674740) not already running
default	11:12:14.026998-0500	Nexy	                AUHAL.cpp:687   SelectDevice: (0x717674740) disconnecting device 85
default	11:12:14.027003-0500	Nexy	                AUHAL.cpp:751   SelectDevice: (0x717674740) destroying ioproc 0xa for device 85
default	11:12:14.027275-0500	Nexy	  AVAudioSession_MacOS.mm:1021  initForMacOS
default	11:12:14.028105-0500	Nexy	[0x71600d180] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioSession
default	11:12:14.029639-0500	audiomxd	  ServerSessionManager.mm:315   { "action":"create_session", "session":{"ID":"0x1ee028","name":"Nexy(78289)"}, "details":{"PID":78289,"session_type":"Primary"} }
default	11:12:14.029719-0500	audiomxd	AudioApplicationInfoImpl.mm:250   Setting initial isRecording state: 0 for newly-created AudioApp
	app: {"name":"[implicit] Nexy","pid":78289}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1ee028, sessionType: 'prim', isRecording: false }, 
]
default	11:12:14.030421-0500	audiomxd	  ServerSessionManager.mm:1322  Start process monitoring, pid = 78289, name = Nexy
default	11:12:14.030670-0500	Nexy	    SessionCore_Create.mm:99    Created session 0x7149d5280 with ID: 0x1ee028
default	11:12:14.031449-0500	Nexy	[0x71600d2c0] activating connection: mach=true listener=false peer=false name=com.apple.audioanalyticsd
error	11:12:14.031815-0500	Nexy	Reporter disconnected. { function=sendMessage, reporterID=336248694636545 }
default	11:12:14.031831-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped Unknown {1C-77-54-18-C8-A3:output, 0xa}
default	11:12:14.031876-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	11:12:14.031965-0500	Nexy	                AUHAL.cpp:762   SelectDevice: (0x717674740) connecting device 91
default	11:12:14.032053-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0x717674740) Device ID: 91 (Input:Yes | Output:No): true
default	11:12:14.033179-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=399.685, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=78289, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	11:12:14.034497-0500	tccd	AUTHREQ_SUBJECT: msgID=399.685, subject=com.nexy.assistant,
default	11:12:14.035176-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb2ed5c000 at /Applications/Nexy.app
default	11:12:14.052531-0500	tccd	AUTHREQ_PROMPTING: msgID=399.685, service=kTCCServiceMicrophone, subject=Sub:{com.nexy.assistant}Resp:{TCCDProcess: identifier=com.nexy.assistant, pid=78289, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy},
default	11:12:16.131153-0500	tccd	Publishing <TCCDEvent: type=Create, service=kTCCServiceMicrophone, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 3 subscribers: {
    476 = "<TCCDEventSubscriber: token=476, state=Passed, csid=com.apple.photolibraryd>";
    37 = "<TCCDEventSubscriber: token=37, state=Initial, csid=(null)>";
    467 = "<TCCDEventSubscriber: token=467, state=Passed, csid=com.apple.chronod>";
}
default	11:12:16.131711-0500	Nexy	                AUHAL.cpp:774   SelectDevice: (0x717674740) created ioproc 0xa for device 91
default	11:12:16.131947-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x717674740) adding 7 device listeners to device 91
default	11:12:16.132196-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x717674740) adding 0 device delegate listeners to device 91
default	11:12:16.132213-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x717674740)
default	11:12:16.132226-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 output streams; not all mono
default	11:12:16.132244-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	11:12:16.132462-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  input stream 0 [0x5c]:  1 ch,  24000 Hz, Float32
default	11:12:16.132477-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 input streams; all mono
default	11:12:16.132483-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  1 ch,  24000 Hz, Float32
default	11:12:16.132617-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x717674740) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	11:12:16.132637-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x717674740) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	11:12:16.132646-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	11:12:16.132652-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x717674740) removing 7 device listeners from device 85
default	11:12:16.133447-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x717674740) removing 0 device delegate listeners from device 85
default	11:12:16.133464-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0x717674740)
default	11:12:16.134042-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	11:12:16.135420-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=399.686, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=78289, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	11:12:16.137213-0500	tccd	AUTHREQ_SUBJECT: msgID=399.686, subject=com.nexy.assistant,
default	11:12:16.140578-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb2ed5c000 at /Applications/Nexy.app
default	11:12:16.143059-0500	chronod	[appAuth:com.nexy.assistant] tcc authorization(s) changed
default	11:12:16.144854-0500	runningboardd	Assertion did invalidate due to timeout: 394-394-34697 (target:[app<application.com.nexy.assistant.53053210.53053219(501)>:78289])
default	11:12:16.162461-0500	Nexy	       ACv2Workarounds.mm:51    com.nexy.assistant: fix84702776_86723525_86479548_89800354_SinglePacketDesc: false
default	11:12:16.162657-0500	Nexy	Registered notify signal com.apple.caulk.alloc.audiodump (0)
default	11:12:16.163064-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0x7173a3810, from  1 ch,  24000 Hz, Float32 to  1 ch,  16000 Hz, Float32
default	11:12:16.163414-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	11:12:16.164669-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=399.687, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=78289, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	11:12:16.165946-0500	tccd	AUTHREQ_SUBJECT: msgID=399.687, subject=com.nexy.assistant,
default	11:12:16.167145-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb2ed5c000 at /Applications/Nexy.app
default	11:12:16.193283-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=399.688, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=78289, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	11:12:16.194643-0500	tccd	AUTHREQ_SUBJECT: msgID=399.688, subject=com.nexy.assistant,
default	11:12:16.195292-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb2ed5c000 at /Applications/Nexy.app
default	11:12:16.213501-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetPreferredChatFlavorForBundleID: <private>-><private> get value: 0
default	11:12:16.213953-0500	coreaudiod	>>> NEGOTIATE [com.nexy.assistant]
default	11:12:16.214025-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetSupportedChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	11:12:16.214088-0500	coreaudiod	<<< NEGOTIATE [com.nexy.assistant]
default	11:12:16.215898-0500	coreaudiod	>>> ADAPT [com.nexy.assistant]
default	11:12:16.216681-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOSupportedChatFlavors newValue: (
    0,
    2
)
default	11:12:16.217861-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xa2cf23000] Created node ADM::com.nexy.assistant_2286.2212.0_airpods noise suppression studio::in-0 with nodeID 0 - reporting period = 10.000000, sample rate = 24000.000000
default	11:12:16.217921-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xa2cf23000] Created node ADM::com.nexy.assistant_2286.2212.0_airpods noise suppression studio::out-0 with nodeID 1 - reporting period = 10.000000, sample rate = 24000.000000
default	11:12:16.337692-0500	coreaudiod	<<< ADAPT [com.nexy.assistant]
default	11:12:16.340022-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Input {1C-77-54-18-C8-A3:input, 0xa}
default	11:12:16.339996-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:2286 called from <private>
default	11:12:16.340990-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2286 called from <private>
default	11:12:16.341094-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2286)
default	11:12:16.341118-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2286 called from <private>
default	11:12:16.341125-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2286 called from <private>
default	11:12:16.341394-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2286)
default	11:12:16.341406-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:2286 called from <private>
default	11:12:16.341412-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:2286 called from <private>
default	11:12:16.342972-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.53053210.53053219(501)>:78289] from originator [osservice<com.apple.powerd>:328] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:394-328-34715 target:78289 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	11:12:16.343069-0500	runningboardd	Assertion 394-328-34715 (target:[app<application.com.nexy.assistant.53053210.53053219(501)>:78289]) will be created as active
default	11:12:16.343662-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78289] Ignoring jetsam update because this process is not memory-managed
default	11:12:16.343677-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78289] Ignoring suspend because this process is not lifecycle managed
default	11:12:16.343687-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78289] Ignoring GPU update because this process is not GPU managed
default	11:12:16.343774-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78289] Ignoring memory limit update because this process is not memory-managed
fault	11:12:16.345184-0500	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.53053210.53053219 AUID=501> and <type=Application identifier=application.com.nexy.assistant.53053210.53053219>
default	11:12:16.347544-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	11:12:16.348608-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	11:12:16.346599-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2285)
default	11:12:16.346616-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2285 called from <private>
fault	11:12:16.351177-0500	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.53053210.53053219 AUID=501> and <type=Application identifier=application.com.nexy.assistant.53053210.53053219>
default	11:12:16.346621-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2285 called from <private>
default	11:12:16.352577-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2286)
default	11:12:16.352596-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2286)
default	11:12:16.352602-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:2286 called from <private>
default	11:12:16.352611-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:2286 called from <private>
default	11:12:16.352657-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2286)
default	11:12:16.352667-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2286 called from <private>
default	11:12:16.352730-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2286)
default	11:12:16.352782-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2286 called from <private>
default	11:12:16.352849-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2286 called from <private>
default	11:12:16.352880-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2286)
default	11:12:16.352890-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2286 called from <private>
default	11:12:16.352960-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2286 called from <private>
default	11:12:16.353015-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2286 called from <private>
default	11:12:16.353024-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2286 called from <private>
default	11:12:16.362004-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ee028","name":"Nexy(78289)"}, "details":{"deviceUIDs":["1C-77-54-18-C8-A3:input"],"implicit_category":"Record","input_running":true,"output_running":false} }
default	11:12:16.362307-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 41, PID = 78289, Name = sid:0x1ee028, Nexy(78289), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	11:12:16.362777-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 41, PID = 78289, Name = sid:0x1ee028, Nexy(78289), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	11:12:16.362915-0500	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1ee028, Nexy(78289), 'prim'', AudioCategory changed to 'Record_WithBluetooth'
default	11:12:16.363110-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 41, PID = 78289, Name = sid:0x1ee028, Nexy(78289), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	11:12:16.363204-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 41, PID = 78289, Name = sid:0x1ee028, Nexy(78289), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	11:12:16.353069-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2286 called from <private>
default	11:12:16.355110-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2286 called from <private>
default	11:12:16.363363-0500	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 41, PID = 78289, Name = sid:0x1ee028, Nexy(78289), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> is going active
default	11:12:16.363434-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1ee028, Nexy(78289), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 41 starting recording
default	11:12:16.355163-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2286 called from <private>
default	11:12:16.357757-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2286)
default	11:12:16.363821-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 41, PID = 78289, Name = sid:0x1ee028, Nexy(78289), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	11:12:16.357963-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2286 called from <private>
default	11:12:16.362024-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2285 called from <private>
default	11:12:16.362075-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2285 called from <private>
default	11:12:16.363914-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 41, PID = 78289, Name = sid:0x1ee028, Nexy(78289), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	11:12:16.364119-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [1, 0]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:input"
)}
default	11:12:16.364002-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found 2 different sessions firstSession={clientName:'sid:0x1ee003, Browser Helper(1622), 'prim'', displayID:'company.thebrowser.browser.helper'}, secondSession={clientName:'sid:0x1ee028, Nexy(78289), 'prim'', displayID:'com.nexy.assistant'} but will use session={clientName:'(null)', displayID:'(null)'}
default	11:12:16.364257-0500	audiomxd	UpdateAudioState CID 0x45550001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	11:12:16.364172-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	11:12:16.363837-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=399.689, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=78289, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	11:12:16.364914-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	11:12:16.364594-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	11:12:16.369443-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.53053210.53053219(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	11:12:16.373946-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:2285 called from <private>
default	11:12:16.373960-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:2285 called from <private>
default	11:12:16.391401-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	11:12:16.389525-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2285 called from <private>
default	11:12:16.390193-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2285 called from <private>
default	11:12:16.390572-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2285 called from <private>
default	11:12:16.390683-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2285 called from <private>
default	11:12:16.390762-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:2285 called from <private>
default	11:12:16.390815-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:2285 called from <private>
default	11:12:16.392898-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2285)
default	11:12:16.391886-0500	runningboardd	Invalidating assertion 394-328-34715 (target:[app<application.com.nexy.assistant.53053210.53053219(501)>:78289]) from originator [osservice<com.apple.powerd>:328]
default	11:12:16.415950-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	11:12:16.416501-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:12:16.416512-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:12:16.416548-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	11:12:16.416594-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:12:16.416651-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	11:12:16.416671-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	11:12:16.417253-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	11:12:16.450957-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	11:12:16.451194-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=399.690, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=78289, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	11:12:16.455348-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	11:12:16.455481-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:12:16.455495-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:12:16.455506-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	11:12:16.455527-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:12:16.455537-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	11:12:16.455544-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	11:12:16.455699-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	11:12:16.455756-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:12:16.455777-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:12:16.455790-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	11:12:16.455841-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:12:16.456062-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	11:12:16.456115-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	11:12:16.456690-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	11:12:16.475682-0500	coreaudiod	>>> ADAPT [com.nexy.assistant]
default	11:12:16.477284-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xa2cf23000] Created node ADM::com.nexy.assistant_2286.2212.0_airpods noise suppression studio::in-0 with nodeID 0 - reporting period = 10.000000, sample rate = 24000.000000
default	11:12:16.477351-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xa2cf23000] Created node ADM::com.nexy.assistant_2286.2212.0_airpods noise suppression studio::out-0 with nodeID 1 - reporting period = 10.000000, sample rate = 24000.000000
default	11:12:16.497555-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78289] Ignoring jetsam update because this process is not memory-managed
default	11:12:16.497576-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78289] Ignoring suspend because this process is not lifecycle managed
default	11:12:16.497594-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78289] Ignoring GPU update because this process is not GPU managed
default	11:12:16.497626-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78289] Ignoring memory limit update because this process is not memory-managed
default	11:12:16.500611-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.53053210.53053219(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	11:12:16.501079-0500	gamepolicyd	Received state update for 78289 (app<application.com.nexy.assistant.53053210.53053219(501)>, running-active-NotVisible
default	11:12:16.512478-0500	coreaudiod	<<< ADAPT [com.nexy.assistant]
default	11:12:16.513937-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:2286 called from <private>
default	11:12:16.513977-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:2286 called from <private>
default	11:12:16.514302-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	11:12:16.514406-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.53053210.53053219(501)>:78289] from originator [osservice<com.apple.powerd>:328] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:394-328-34721 target:78289 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	11:12:16.514484-0500	runningboardd	Assertion 394-328-34721 (target:[app<application.com.nexy.assistant.53053210.53053219(501)>:78289]) will be created as active
default	11:12:16.514918-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2286 called from <private>
default	11:12:16.515120-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2286)
default	11:12:16.515136-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2286 called from <private>
default	11:12:16.515480-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ee028","name":"Nexy(78289)"}, "details":{"deviceUIDs":[],"implicit_category":"","input_running":false,"output_running":false} }
default	11:12:16.515144-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2286 called from <private>
default	11:12:16.515242-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xa}
default	11:12:16.515593-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 41, PID = 78289, Name = sid:0x1ee028, Nexy(78289), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	11:12:16.515639-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 41, PID = 78289, Name = sid:0x1ee028, Nexy(78289), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	11:12:16.515506-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78289] Ignoring jetsam update because this process is not memory-managed
default	11:12:16.515665-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found 2 different sessions firstSession={clientName:'sid:0x1ee003, Browser Helper(1622), 'prim'', displayID:'company.thebrowser.browser.helper'}, secondSession={clientName:'sid:0x1ee028, Nexy(78289), 'prim'', displayID:'com.nexy.assistant'} but will use session={clientName:'(null)', displayID:'(null)'}
default	11:12:16.515618-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78289] Ignoring suspend because this process is not lifecycle managed
default	11:12:16.515706-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1ee028, Nexy(78289), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 41 stopping recording
default	11:12:16.515707-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78289] Ignoring GPU update because this process is not GPU managed
default	11:12:16.515700-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	11:12:16.515722-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	11:12:16.515767-0500	audiomxd	-MXCoreSession- -[MXCoreSession endInterruption:]: Session <ID: 41, PID = 78289, Name = sid:0x1ee028, Nexy(78289), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> is going inactive
default	11:12:16.515808-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78289] Ignoring memory limit update because this process is not memory-managed
default	11:12:16.515847-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 41, PID = 78289, Name = sid:0x1ee028, Nexy(78289), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	11:12:16.515989-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 41, PID = 78289, Name = sid:0x1ee028, Nexy(78289), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	11:12:16.516263-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 0]. BT device UIDS: {(
)}
default	11:12:16.516272-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	11:12:16.516479-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 200 flag 0x1 < Hijack > app com.nexy.assistant CID 0x45550001 category Not set
default	11:12:16.516320-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	11:12:16.516781-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	11:12:16.516680-0500	audiomxd	UpdateAudioState CID 0x45550001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	11:12:16.516812-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	11:12:16.516719-0500	audiomxd	UpdateAudioState CID 0x45550001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	11:12:16.516828-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	11:12:16.516850-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	11:12:16.517071-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2286)
default	11:12:16.517306-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2286 called from <private>
default	11:12:16.517314-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2286 called from <private>
default	11:12:16.517327-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2286 called from <private>
default	11:12:16.517195-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	11:12:16.517334-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2286 called from <private>
default	11:12:16.517241-0500	audioaccessoryd	AudioStateChanged: Removed audio session app com.nexy.assistant 201 count 2
default	11:12:16.521845-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	11:12:16.521893-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	11:12:16.521933-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	11:12:16.522012-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	11:12:16.522314-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:12:16.522326-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:12:16.522336-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	11:12:16.522341-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:12:16.522347-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	11:12:16.522355-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	11:12:16.522538-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	11:12:16.627305-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78289] Ignoring jetsam update because this process is not memory-managed
default	11:12:16.627327-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78289] Ignoring suspend because this process is not lifecycle managed
default	11:12:16.627350-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78289] Ignoring GPU update because this process is not GPU managed
default	11:12:16.627439-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78289] Ignoring memory limit update because this process is not memory-managed
default	11:12:16.628287-0500	Nexy	                AUHAL.cpp:473   ~AUHAL: (0x717674740) Selecting device 0 from destructor
default	11:12:16.628299-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0x717674740)
default	11:12:16.628307-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0x717674740) not already running
default	11:12:16.628310-0500	Nexy	                AUHAL.cpp:687   SelectDevice: (0x717674740) disconnecting device 91
default	11:12:16.628314-0500	Nexy	                AUHAL.cpp:751   SelectDevice: (0x717674740) destroying ioproc 0xa for device 91
default	11:12:16.628343-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xa}
default	11:12:16.628369-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	11:12:16.628489-0500	Nexy	                AUHAL.cpp:853   SelectDevice: (0x717674740) nothing to setup
default	11:12:16.628499-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x717674740) adding 0 device listeners to device 0
default	11:12:16.628530-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x717674740) adding 0 device delegate listeners to device 0
default	11:12:16.628567-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x717674740) removing 7 device listeners from device 91
default	11:12:16.628756-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x717674740) removing 0 device delegate listeners from device 91
default	11:12:16.628765-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0x717674740)
default	11:12:16.631006-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.53053210.53053219(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	11:12:16.631577-0500	gamepolicyd	Received state update for 78289 (app<application.com.nexy.assistant.53053210.53053219(501)>, running-active-NotVisible
default	11:12:19.141355-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2286)
default	11:12:19.141402-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2286 called from <private>
default	11:12:19.141412-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2286 called from <private>
default	11:12:19.141962-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2285)
default	11:12:19.141987-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2285 called from <private>
default	11:12:19.141993-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2285 called from <private>
default	11:12:19.152479-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2285 called from <private>
default	11:12:19.152508-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2285 called from <private>
default	11:12:19.153105-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2286)
default	11:12:19.153131-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2286 called from <private>
default	11:12:19.153137-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2286 called from <private>
default	11:12:19.153595-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2285)
default	11:12:19.153616-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:2285 called from <private>
default	11:12:19.153624-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:2285 called from <private>
default	11:12:19.154781-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2285)
default	11:12:19.154829-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2285)
default	11:12:19.154879-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2285)
default	11:12:19.155455-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:2285 called from <private>
default	11:12:19.155467-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:2285 called from <private>
default	11:12:19.155481-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2285 called from <private>
default	11:12:19.155492-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2285 called from <private>
default	11:12:19.155498-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2285 called from <private>
default	11:12:19.155524-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2285 called from <private>
default	11:12:19.155627-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2285 called from <private>
default	11:12:19.155688-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2285 called from <private>
default	11:12:19.158435-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2285 called from <private>
default	11:12:19.158461-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2285 called from <private>
default	11:12:19.168756-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:2285 called from <private>
default	11:12:19.168785-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:2285 called from <private>
default	11:12:19.168962-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2285)
default	11:12:19.170516-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2285)
default	11:12:19.170552-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2285)
default	11:12:19.170788-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:2285 called from <private>
default	11:12:19.170799-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:2285 called from <private>
default	11:12:19.170959-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2285)
default	11:12:19.173232-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2285)
default	11:12:19.173264-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2285)
default	11:12:19.173765-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2285 called from <private>
default	11:12:19.173779-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2285 called from <private>
default	11:12:19.173810-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2285 called from <private>
default	11:12:19.173820-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2285 called from <private>
default	11:12:19.173826-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2285 called from <private>
default	11:12:19.173834-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2285 called from <private>
default	11:12:19.173840-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2285 called from <private>
default	11:12:19.173846-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2285 called from <private>
default	11:12:19.173868-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2285 called from <private>
default	11:12:19.173923-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2285 called from <private>
default	11:12:19.173968-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2285 called from <private>
default	11:12:19.174041-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2285 called from <private>
default	11:12:19.174077-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2285 called from <private>
default	11:12:19.174113-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2285 called from <private>
default	11:12:19.181963-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2285)
default	11:12:19.182008-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2285 called from <private>
default	11:12:19.182015-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2285 called from <private>
default	11:12:19.185864-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2285)
default	11:12:19.187428-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2285 called from <private>
default	11:12:19.187717-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2285 called from <private>
default	11:12:20.817507-0500	Nexy	NotifyToken::RegisterDispatch(user.uid.501.com.apple.LaunchServices.database) fired for session key <private>
default	11:12:22.101210-0500	Nexy	LSExceptions shared instance invalidated for timeout.
default	11:12:29.633279-0500	Nexy	                AUHAL.cpp:420   AUHAL: (0x717674740) Selecting device 85 from constructor
default	11:12:29.633301-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0x717674740)
default	11:12:29.633310-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0x717674740) not already running
default	11:12:29.633316-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0x717674740) nothing to teardown
default	11:12:29.633321-0500	Nexy	                AUHAL.cpp:762   SelectDevice: (0x717674740) connecting device 85
default	11:12:29.633476-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0x717674740) Device ID: 85 (Input:No | Output:Yes): true
default	11:12:29.633668-0500	Nexy	                AUHAL.cpp:774   SelectDevice: (0x717674740) created ioproc 0xb for device 85
default	11:12:29.633938-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x717674740) adding 7 device listeners to device 85
default	11:12:29.634191-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x717674740) adding 0 device delegate listeners to device 85
default	11:12:29.634202-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x717674740)
default	11:12:29.634325-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  48000 Hz, Float32, interleaved
default	11:12:29.634335-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	11:12:29.634370-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	11:12:29.634383-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	11:12:29.634394-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	11:12:29.634510-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x717674740) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	11:12:29.634524-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x717674740) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	11:12:29.634531-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	11:12:29.634540-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x717674740) removing 0 device listeners from device 0
default	11:12:29.634571-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x717674740) removing 0 device delegate listeners from device 0
default	11:12:29.634594-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0x717674740)
default	11:12:29.634627-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is DISABLED
default	11:12:29.634720-0500	Nexy	                AUHAL.cpp:2303  SetProperty: (0x717674740) caller requesting device change from 85 to 91
default	11:12:29.634728-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0x717674740)
default	11:12:29.634735-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0x717674740) not already running
default	11:12:29.634740-0500	Nexy	                AUHAL.cpp:687   SelectDevice: (0x717674740) disconnecting device 85
default	11:12:29.634744-0500	Nexy	                AUHAL.cpp:751   SelectDevice: (0x717674740) destroying ioproc 0xb for device 85
default	11:12:29.634783-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped Unknown {1C-77-54-18-C8-A3:output, 0xb}
default	11:12:29.634839-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	11:12:29.634921-0500	Nexy	                AUHAL.cpp:762   SelectDevice: (0x717674740) connecting device 91
default	11:12:29.635023-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0x717674740) Device ID: 91 (Input:Yes | Output:No): true
default	11:12:29.639282-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=399.691, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=78289, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	11:12:29.643620-0500	tccd	AUTHREQ_SUBJECT: msgID=399.691, subject=com.nexy.assistant,
default	11:12:29.645169-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb2ed5db00 at /Applications/Nexy.app
default	11:12:29.670968-0500	Nexy	                AUHAL.cpp:774   SelectDevice: (0x717674740) created ioproc 0xb for device 91
default	11:12:29.671130-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x717674740) adding 7 device listeners to device 91
default	11:12:29.671297-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x717674740) adding 0 device delegate listeners to device 91
default	11:12:29.671303-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x717674740)
default	11:12:29.671315-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 output streams; not all mono
default	11:12:29.671327-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	11:12:29.671446-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  input stream 0 [0x5c]:  1 ch,  24000 Hz, Float32
default	11:12:29.671452-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 input streams; all mono
default	11:12:29.671458-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  1 ch,  24000 Hz, Float32
default	11:12:29.671540-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x717674740) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	11:12:29.671550-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x717674740) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	11:12:29.671555-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	11:12:29.671561-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x717674740) removing 7 device listeners from device 85
default	11:12:29.671704-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x717674740) removing 0 device delegate listeners from device 85
default	11:12:29.671710-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0x717674740)
default	11:12:29.671720-0500	Nexy	AudioHardware-mac-imp.cpp:1306   AudioObjectAddPropertyListener: listener was already added
default	11:12:29.672317-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	11:12:29.673506-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=399.692, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=78289, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	11:12:29.674696-0500	tccd	AUTHREQ_SUBJECT: msgID=399.692, subject=com.nexy.assistant,
default	11:12:29.675308-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb2ed5db00 at /Applications/Nexy.app
default	11:12:29.692569-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0x7173a3810, from  1 ch,  24000 Hz, Float32 to  1 ch,  16000 Hz, Float32
default	11:12:29.692773-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	11:12:29.693685-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=399.693, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=78289, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	11:12:29.694704-0500	tccd	AUTHREQ_SUBJECT: msgID=399.693, subject=com.nexy.assistant,
default	11:12:29.695332-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb2ed5db00 at /Applications/Nexy.app
default	11:12:29.713278-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=399.694, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=78289, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	11:12:29.714215-0500	tccd	AUTHREQ_SUBJECT: msgID=399.694, subject=com.nexy.assistant,
default	11:12:29.714786-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb2ed5db00 at /Applications/Nexy.app
default	11:12:29.731946-0500	coreaudiod	>>> NEGOTIATE [com.nexy.assistant]
default	11:12:29.732111-0500	coreaudiod	<<< NEGOTIATE [com.nexy.assistant]
default	11:12:29.734879-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:2286 called from <private>
default	11:12:29.734900-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Input {1C-77-54-18-C8-A3:input, 0xb}
default	11:12:29.734930-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	11:12:29.736901-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2286 called from <private>
default	11:12:29.737278-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2286)
default	11:12:29.744971-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	11:12:29.745203-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.53053210.53053219(501)>:78289] from originator [osservice<com.apple.powerd>:328] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:394-328-34725 target:78289 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	11:12:29.745362-0500	runningboardd	Assertion 394-328-34725 (target:[app<application.com.nexy.assistant.53053210.53053219(501)>:78289]) will be created as active
default	11:12:29.745857-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	11:12:29.745990-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78289] Ignoring jetsam update because this process is not memory-managed
default	11:12:29.746258-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78289] Ignoring suspend because this process is not lifecycle managed
default	11:12:29.746359-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78289] Ignoring GPU update because this process is not GPU managed
default	11:12:29.746557-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78289] Ignoring memory limit update because this process is not memory-managed
default	11:12:29.737314-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2286 called from <private>
default	11:12:29.737323-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2286 called from <private>
default	11:12:29.738965-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2285)
default	11:12:29.739646-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2285 called from <private>
default	11:12:29.739684-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2285 called from <private>
default	11:12:29.750087-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2286)
default	11:12:29.750118-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2286)
default	11:12:29.750194-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2286)
default	11:12:29.750272-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2286)
default	11:12:29.754544-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:2286 called from <private>
default	11:12:29.754596-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:2286 called from <private>
default	11:12:29.754662-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:2286 called from <private>
default	11:12:29.754736-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:2286 called from <private>
default	11:12:29.754784-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2286 called from <private>
default	11:12:29.754836-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2286 called from <private>
default	11:12:29.754884-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2286 called from <private>
default	11:12:29.754894-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2286 called from <private>
default	11:12:29.754975-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2286 called from <private>
default	11:12:29.755017-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2286 called from <private>
default	11:12:29.755655-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2286)
default	11:12:29.756004-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2286 called from <private>
default	11:12:29.758889-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2285 called from <private>
default	11:12:29.758434-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ee028","name":"Nexy(78289)"}, "details":{"deviceUIDs":["1C-77-54-18-C8-A3:input"],"implicit_category":"Record","input_running":true,"output_running":false} }
default	11:12:29.758900-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2285 called from <private>
default	11:12:29.758860-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 41, PID = 78289, Name = sid:0x1ee028, Nexy(78289), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	11:12:29.759805-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Category/Mode changed -- The score for sid:0x1ee028, Nexy(78289), 'prim'/com.nexy.assistant was not correct. Old score = 201
default	11:12:29.760423-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 41, PID = 78289, Name = sid:0x1ee028, Nexy(78289), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	11:12:29.761183-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 41, PID = 78289, Name = sid:0x1ee028, Nexy(78289), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	11:12:29.761475-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 41, PID = 78289, Name = sid:0x1ee028, Nexy(78289), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	11:12:29.761498-0500	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1ee028, Nexy(78289), 'prim'', AudioCategory changed to 'Record_WithBluetooth'
default	11:12:29.761671-0500	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 41, PID = 78289, Name = sid:0x1ee028, Nexy(78289), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> is going active
default	11:12:29.761748-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1ee028, Nexy(78289), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 41 starting recording
default	11:12:29.762108-0500	audiomxd	UpdateAudioState CID 0x45550001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	11:12:29.762108-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 41, PID = 78289, Name = sid:0x1ee028, Nexy(78289), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	11:12:29.762180-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 41, PID = 78289, Name = sid:0x1ee028, Nexy(78289), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	11:12:29.762337-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found 2 different sessions firstSession={clientName:'sid:0x1ee003, Browser Helper(1622), 'prim'', displayID:'company.thebrowser.browser.helper'}, secondSession={clientName:'sid:0x1ee028, Nexy(78289), 'prim'', displayID:'com.nexy.assistant'} but will use session={clientName:'(null)', displayID:'(null)'}
default	11:12:29.762232-0500	audiomxd	UpdateAudioState CID 0x45550001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	11:12:29.762612-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [1, 0]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:input"
)}
default	11:12:29.762664-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	11:12:29.763382-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	11:12:29.763824-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	11:12:29.763461-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	11:12:29.766918-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.53053210.53053219(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	11:12:29.760653-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=399.695, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=78289, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	11:12:29.768263-0500	runningboardd	Invalidating assertion 394-328-34725 (target:[app<application.com.nexy.assistant.53053210.53053219(501)>:78289]) from originator [osservice<com.apple.powerd>:328]
default	11:12:29.769965-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:2285 called from <private>
default	11:12:29.769988-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:2285 called from <private>
default	11:12:29.770076-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2285)
default	11:12:29.771162-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2285)
default	11:12:29.771183-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2285)
default	11:12:29.771497-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:2285 called from <private>
default	11:12:29.771518-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:2285 called from <private>
default	11:12:29.771639-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2285)
default	11:12:29.772905-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2285)
default	11:12:29.772969-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2285)
default	11:12:29.773220-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2285 called from <private>
default	11:12:29.773291-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2285 called from <private>
default	11:12:29.774880-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2285 called from <private>
default	11:12:29.774889-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2285 called from <private>
default	11:12:29.774904-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:2285 called from <private>
default	11:12:29.774912-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:2285 called from <private>
default	11:12:29.774995-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2285)
default	11:12:29.775062-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:2285 called from <private>
default	11:12:29.775151-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:2285 called from <private>
default	11:12:29.775232-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2285 called from <private>
default	11:12:29.775321-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2285 called from <private>
default	11:12:29.775376-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2285 called from <private>
default	11:12:29.775466-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2285 called from <private>
default	11:12:29.775573-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:2285 called from <private>
default	11:12:29.775679-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:2285 called from <private>
default	11:12:29.775779-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:2285 called from <private>
default	11:12:29.775835-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:2285 called from <private>
default	11:12:29.775878-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:2285 called from <private>
default	11:12:29.785430-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2285)
default	11:12:29.785599-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2285 called from <private>
default	11:12:29.785918-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2285 called from <private>
default	11:12:29.786009-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2285 called from <private>
default	11:12:29.788897-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2285)
default	11:12:29.789346-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2285)
default	11:12:29.791049-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2285 called from <private>
default	11:12:29.816777-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	11:12:29.842812-0500	gamepolicyd	Received state update for 78289 (app<application.com.nexy.assistant.53053210.53053219(501)>, running-active-NotVisible
default	11:12:29.855004-0500	coreaudiod	>>> NEGOTIATE [com.nexy.assistant]
default	11:12:29.855237-0500	coreaudiod	<<< NEGOTIATE [com.nexy.assistant]
default	11:12:29.857567-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:2286 called from <private>
default	11:12:29.857657-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:2286 called from <private>
default	11:12:29.857939-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.53053210.53053219(501)>:78289] from originator [osservice<com.apple.powerd>:328] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:394-328-34729 target:78289 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	11:12:29.858052-0500	runningboardd	Assertion 394-328-34729 (target:[app<application.com.nexy.assistant.53053210.53053219(501)>:78289]) will be created as active
default	11:12:29.862832-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	11:12:29.864799-0500	tccd	AUTHREQ_SUBJECT: msgID=399.696, subject=com.nexy.assistant,
default	11:12:29.866328-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb2ed5db00 at /Applications/Nexy.app
default	11:12:29.868947-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	11:12:29.869086-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	11:12:29.869235-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	11:12:29.869446-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	11:12:29.870263-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:12:29.870282-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:12:29.870299-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	11:12:29.870306-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:12:29.870318-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	11:12:29.870335-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	11:12:29.870460-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	11:12:29.891033-0500	coreaudiod	>>> ADAPT [com.nexy.assistant]
default	11:12:29.892667-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xa2cf23000] Created node ADM::com.nexy.assistant_2286.2212.0_airpods noise suppression studio::in-0 with nodeID 0 - reporting period = 10.000000, sample rate = 24000.000000
default	11:12:29.892725-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xa2cf23000] Created node ADM::com.nexy.assistant_2286.2212.0_airpods noise suppression studio::out-0 with nodeID 1 - reporting period = 10.000000, sample rate = 24000.000000
default	11:12:29.957217-0500	coreaudiod	<<< ADAPT [com.nexy.assistant]
default	11:12:29.959033-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:2286 called from <private>
default	11:12:29.959067-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:2286 called from <private>
default	11:12:29.959276-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	11:12:29.959347-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.53053210.53053219(501)>:78289] from originator [osservice<com.apple.powerd>:328] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:394-328-34730 target:78289 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	11:12:29.959800-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2286 called from <private>
default	11:12:29.960119-0500	runningboardd	Assertion 394-328-34730 (target:[app<application.com.nexy.assistant.53053210.53053219(501)>:78289]) will be created as active
default	11:12:29.959930-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2286)
default	11:12:29.959944-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2286 called from <private>
default	11:12:29.959949-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2286 called from <private>
default	11:12:29.960500-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78289] Ignoring jetsam update because this process is not memory-managed
default	11:12:29.960539-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78289] Ignoring suspend because this process is not lifecycle managed
default	11:12:29.960578-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78289] Ignoring GPU update because this process is not GPU managed
default	11:12:29.960701-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	11:12:29.960654-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78289] Ignoring memory limit update because this process is not memory-managed
default	11:12:29.960850-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	11:12:29.961441-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2286)
default	11:12:29.961680-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2286 called from <private>
default	11:12:29.961694-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2286 called from <private>
default	11:12:29.961704-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2286 called from <private>
default	11:12:29.963079-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=399.697, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=78289, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	11:12:29.964267-0500	tccd	AUTHREQ_SUBJECT: msgID=399.697, subject=com.nexy.assistant,
default	11:12:29.964926-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb2ed5db00 at /Applications/Nexy.app
default	11:12:29.965564-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.53053210.53053219(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	11:12:29.965599-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	11:12:29.965641-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	11:12:29.965677-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	11:12:29.965800-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	11:12:29.965841-0500	runningboardd	Invalidating assertion 394-328-34730 (target:[app<application.com.nexy.assistant.53053210.53053219(501)>:78289]) from originator [osservice<com.apple.powerd>:328]
default	11:12:29.966069-0500	gamepolicyd	Received state update for 78289 (app<application.com.nexy.assistant.53053210.53053219(501)>, running-active-NotVisible
default	11:12:29.966237-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:12:29.966247-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:12:29.966263-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	11:12:29.966268-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:12:29.966274-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	11:12:29.966280-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	11:12:29.966358-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	11:12:29.966475-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:12:29.966483-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:12:29.966489-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	11:12:29.966496-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:12:29.966543-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	11:12:29.966613-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	11:12:29.966861-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	11:12:29.986017-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.53053210.53053219(501)>:78289] from originator [osservice<com.apple.powerd>:328] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:394-328-34731 target:78289 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	11:12:29.986247-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:2286 called from <private>
default	11:12:29.986377-0500	runningboardd	Assertion 394-328-34731 (target:[app<application.com.nexy.assistant.53053210.53053219(501)>:78289]) will be created as active
default	11:12:29.991595-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	11:12:29.991628-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	11:12:29.991660-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	11:12:29.991875-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:12:29.991888-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:12:29.991899-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	11:12:29.991905-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:12:29.991914-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	11:12:29.991921-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	11:12:29.991945-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:12:29.991954-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:12:29.991961-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	11:12:29.991967-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:12:29.991975-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	11:12:29.991981-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	11:12:29.992069-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	11:12:29.992803-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:12:29.992810-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:12:29.992815-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	11:12:29.992824-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:12:29.992830-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	11:12:29.992837-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	11:12:29.992891-0500	ControlCenter	Navigating to new application [com.nexy.assistant]
default	11:12:30.126722-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xb}
default	11:12:30.127120-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ee028","name":"Nexy(78289)"}, "details":{"deviceUIDs":[],"implicit_category":"","input_running":false,"output_running":false} }
default	11:12:30.127368-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 41, PID = 78289, Name = sid:0x1ee028, Nexy(78289), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	11:12:30.127435-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 41, PID = 78289, Name = sid:0x1ee028, Nexy(78289), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	11:12:30.127470-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found 2 different sessions firstSession={clientName:'sid:0x1ee003, Browser Helper(1622), 'prim'', displayID:'company.thebrowser.browser.helper'}, secondSession={clientName:'sid:0x1ee028, Nexy(78289), 'prim'', displayID:'com.nexy.assistant'} but will use session={clientName:'(null)', displayID:'(null)'}
default	11:12:30.127520-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1ee028, Nexy(78289), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 41 stopping recording
default	11:12:30.127541-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	11:12:30.127548-0500	audiomxd	-MXCoreSession- -[MXCoreSession endInterruption:]: Session <ID: 41, PID = 78289, Name = sid:0x1ee028, Nexy(78289), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> is going inactive
default	11:12:30.127578-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 41, PID = 78289, Name = sid:0x1ee028, Nexy(78289), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	11:12:30.127609-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 41, PID = 78289, Name = sid:0x1ee028, Nexy(78289), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	11:12:30.127752-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 0]. BT device UIDS: {(
)}
default	11:12:30.127774-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	11:12:30.127975-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 200 flag 0x1 < Hijack > app com.nexy.assistant CID 0x45550001 category Not set
default	11:12:30.128257-0500	audiomxd	UpdateAudioState CID 0x45550001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	11:12:30.128295-0500	audiomxd	UpdateAudioState CID 0x45550001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	11:12:30.128345-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	11:12:30.128397-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	11:12:30.128417-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	11:12:30.128429-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	11:12:30.129914-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	11:12:30.129961-0500	audioaccessoryd	AudioStateChanged: Removed audio session app com.nexy.assistant 201 count 2
default	11:12:30.130120-0500	runningboardd	Invalidating assertion 394-328-34731 (target:[app<application.com.nexy.assistant.53053210.53053219(501)>:78289]) from originator [osservice<com.apple.powerd>:328]
default	11:12:30.131625-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	11:12:30.134468-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:12:30.134480-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:12:30.134500-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	11:12:30.134506-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:12:30.134515-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	11:12:30.134522-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	11:12:30.134685-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	11:12:30.228405-0500	Nexy	                AUHAL.cpp:473   ~AUHAL: (0x717674740) Selecting device 0 from destructor
default	11:12:30.228421-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0x717674740)
default	11:12:30.228431-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0x717674740) not already running
default	11:12:30.228436-0500	Nexy	                AUHAL.cpp:687   SelectDevice: (0x717674740) disconnecting device 91
default	11:12:30.228445-0500	Nexy	                AUHAL.cpp:751   SelectDevice: (0x717674740) destroying ioproc 0xb for device 91
default	11:12:30.228499-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xb}
default	11:12:30.228547-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	11:12:30.228732-0500	Nexy	                AUHAL.cpp:853   SelectDevice: (0x717674740) nothing to setup
default	11:12:30.228744-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x717674740) adding 0 device listeners to device 0
default	11:12:30.228749-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x717674740) adding 0 device delegate listeners to device 0
default	11:12:30.228756-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x717674740) removing 7 device listeners from device 91
default	11:12:30.228982-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x717674740) removing 0 device delegate listeners from device 91
default	11:12:30.229001-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0x717674740)
default	11:12:30.235162-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78289] Ignoring jetsam update because this process is not memory-managed
default	11:12:30.235186-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78289] Ignoring suspend because this process is not lifecycle managed
default	11:12:30.235196-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78289] Ignoring GPU update because this process is not GPU managed
default	11:12:30.235215-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78289] Ignoring memory limit update because this process is not memory-managed
default	11:12:30.238416-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.53053210.53053219(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	11:12:30.239027-0500	gamepolicyd	Received state update for 78289 (app<application.com.nexy.assistant.53053210.53053219(501)>, running-active-NotVisible
default	11:12:32.484813-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2285)
default	11:12:32.484859-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2285 called from <private>
default	11:12:32.484867-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2285 called from <private>
default	11:12:32.485990-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2286)
default	11:12:32.486020-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2286 called from <private>
default	11:12:32.486026-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2286 called from <private>
default	11:12:32.501966-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2286)
default	11:12:32.502007-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2286 called from <private>
default	11:12:32.502012-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2286 called from <private>
default	11:12:32.504477-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2285 called from <private>
default	11:12:32.504498-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2285 called from <private>
default	11:12:32.518150-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:2285 called from <private>
default	11:12:32.518184-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:2285 called from <private>
default	11:12:32.518321-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2285)
default	11:12:32.521450-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2285)
default	11:12:32.521492-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2285)
default	11:12:32.521955-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:2285 called from <private>
default	11:12:32.521970-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:2285 called from <private>
default	11:12:32.522119-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2285)
default	11:12:32.527473-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2285)
default	11:12:32.527533-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2285)
default	11:12:32.527753-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2285 called from <private>
default	11:12:32.527846-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2285 called from <private>
default	11:12:32.528122-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2285 called from <private>
default	11:12:32.528201-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2285 called from <private>
default	11:12:32.528218-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:2285 called from <private>
default	11:12:32.528304-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:2285 called from <private>
default	11:12:32.528312-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2285)
default	11:12:32.528376-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:2285 called from <private>
default	11:12:32.528449-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:2285 called from <private>
default	11:12:32.528481-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2285 called from <private>
default	11:12:32.528636-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2285 called from <private>
default	11:12:32.528711-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2285 called from <private>
default	11:12:32.528795-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2285 called from <private>
default	11:12:32.528892-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:2285 called from <private>
default	11:12:32.529011-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:2285 called from <private>
default	11:12:32.529076-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:2285 called from <private>
default	11:12:32.529105-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:2285 called from <private>
default	11:12:32.529298-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:2285 called from <private>
default	11:12:32.529454-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:2285 called from <private>
default	11:12:32.534698-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2285)
default	11:12:32.535043-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:2285 called from <private>
default	11:12:32.535471-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2285)
default	11:12:32.535783-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:2285 called from <private>
default	11:12:32.536040-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2285)
default	11:12:32.536273-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2285 called from <private>
default	11:12:32.536510-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2285)
default	11:12:32.536727-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2285 called from <private>
default	11:12:32.537154-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2285 called from <private>
default	11:12:32.537374-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2285 called from <private>
default	11:12:32.537564-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2285 called from <private>
default	11:12:32.537776-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2285 called from <private>
default	11:12:32.538002-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2285 called from <private>
default	11:12:32.541022-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2285 called from <private>
default	11:12:32.541246-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2285 called from <private>
default	11:12:33.249676-0500	Nexy	[0x71600d540] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	11:12:33.251280-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=78289.3, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=78289, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	11:12:33.253551-0500	tccd	AUTHREQ_SUBJECT: msgID=78289.3, subject=com.nexy.assistant,
default	11:12:33.254618-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x93ad31e00 at /Applications/Nexy.app
default	11:12:33.284961-0500	tccd	Notifying for access  kTCCServiceScreenCapture for target PID[78289], responsiblePID[78289], responsiblePath: /Applications/Nexy.app to UID: 501
default	11:12:33.285358-0500	Nexy	[0x71600d540] invalidated after the last release of the connection object
default	11:12:33.490473-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x93ad32400 at /Applications/Nexy.app
default	11:12:33.533260-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x93ad31e00 at /Applications/Nexy.app
default	11:12:33.534533-0500	nehelper	Received an apps uninstalled notification with bundle IDs (
    "com.nexy.assistant"
)
default	11:12:33.539314-0500	tccd	Publishing <TCCDEvent: type=Modify, service=kTCCServiceScreenCapture, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 0 subscribers: {
}
default	11:12:34.134572-0500	nehelper	Removing UUIDs for (
    "com.nexy.assistant"
)
default	11:12:34.140068-0500	nehelper	Handling an apps uninstalled notification with bundle IDs (
    "com.nexy.assistant"
)
default	11:12:34.169301-0500	nehelper	com.apple.preferences.networkprivacy-F67B3EA9-90A6-470B-B321-9BBD719C692B: Populating the cache with 2 UUID(s) for com.nexy.assistant
error	11:12:36.777968-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceScreenCapture com.nexy.assistant none
error	11:12:36.782073-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceScreenCapture com.nexy.assistant none
default	11:12:44.819329-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x93ad30000 at /Applications/Nexy.app
default	11:12:44.843173-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x93ad33600 at /Applications/Nexy.app
default	11:12:44.854182-0500	tccd	Publishing <TCCDEvent: type=Modify, service=kTCCServiceScreenCapture, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 0 subscribers: {
}
error	11:12:44.988859-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceScreenCapture com.nexy.assistant full
error	11:12:44.991152-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceScreenCapture com.nexy.assistant full
error	11:12:45.027024-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceMicrophone com.nexy.assistant full
error	11:12:45.027581-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceMicrophone com.nexy.assistant full
default	11:12:46.304295-0500	Nexy	[0x71600d540] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	11:12:46.305881-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=78289.4, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=78289, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	11:12:46.308860-0500	tccd	AUTHREQ_SUBJECT: msgID=78289.4, subject=com.nexy.assistant,
default	11:12:46.310794-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x93ad33600 at /Applications/Nexy.app
default	11:12:46.341609-0500	Nexy	[0x71600d540] invalidated after the last release of the connection object
default	11:12:46.344949-0500	Nexy	 [INFO] SLSWindowListCreateImageProxying:84 request: <private>
default	11:12:46.348261-0500	Nexy	[0x71600d540] activating connection: mach=true listener=false peer=false name=com.apple.replayd
default	11:12:46.348494-0500	Nexy	 [INFO] -[RPDaemonProxy consumeSandboxExtension:processNewConnection:]:568
default	11:12:46.349133-0500	Nexy	 [INFO] -[RPDaemonProxy proxyCoreGraphicsWithMethodType:config:machPort:completionHandler:]:1493
default	11:12:46.365930-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=96069.71, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=78289, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.replayd, pid=96069, auid=501, euid=501, binary_path=/usr/libexec/replayd}, },
default	11:12:46.366050-0500	tccd	requestor: TCCDProcess: identifier=com.apple.replayd, pid=96069, auid=501, euid=501, binary_path=/usr/libexec/replayd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=78289, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	11:12:46.367305-0500	tccd	AUTHREQ_SUBJECT: msgID=96069.71, subject=com.nexy.assistant,
default	11:12:46.368290-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x93ad33600 at /Applications/Nexy.app
default	11:12:46.398122-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=387.1623, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=78289, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=387, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	11:12:46.398149-0500	tccd	requestor: TCCDProcess: identifier=com.apple.WindowServer, pid=387, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=78289, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	11:12:46.399233-0500	tccd	AUTHREQ_SUBJECT: msgID=387.1623, subject=com.nexy.assistant,
default	11:12:46.399935-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x93ad33600 at /Applications/Nexy.app
default	11:12:46.422118-0500	Nexy	 [INFO] SLSWindowListCreateImageProxying_block_invoke:116 request: <private>, error: (null), output: <private>
default	11:12:46.462935-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	11:12:46.463164-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant)]
default	11:12:46.463251-0500	ControlCenter	Active activity attributions changed to ["scr:com.nexy.assistant"]
default	11:12:46.466619-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:12:46.466633-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:12:46.466646-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	11:12:46.466655-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:12:46.466671-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	11:12:46.466681-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	11:12:46.466869-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	11:12:49.459656-0500	Nexy	[0x71600d680] activating connection: mach=true listener=false peer=false name=com.apple.tccd
default	11:12:49.460537-0500	Nexy	[0x71600d7c0] activating connection: mach=true listener=false peer=false name=com.apple.tccd
default	11:12:49.460663-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=78289.5, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=78289, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	11:12:49.461219-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=78289.6, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=78289, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	11:12:49.462991-0500	tccd	AUTHREQ_SUBJECT: msgID=78289.6, subject=com.nexy.assistant,
default	11:12:49.463318-0500	tccd	AUTHREQ_SUBJECT: msgID=78289.5, subject=com.nexy.assistant,
default	11:12:49.463886-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb2ed5db00 at /Applications/Nexy.app
default	11:12:49.464526-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb2ed5e700 at /Applications/Nexy.app
default	11:12:49.479196-0500	Nexy	[0x71600d7c0] invalidated after the last release of the connection object
default	11:12:49.479298-0500	Nexy	Adding shared photo decorator (includeSharedPhotoContacts=YES)
default	11:12:49.480505-0500	Nexy	[0x71600d7c0] activating connection: mach=true listener=false peer=false name=com.apple.tccd
default	11:12:49.480945-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=78289.7, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=78289, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	11:12:49.481993-0500	tccd	AUTHREQ_SUBJECT: msgID=78289.7, subject=com.nexy.assistant,
default	11:12:49.482605-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb2ed5db00 at /Applications/Nexy.app
default	11:12:49.484498-0500	Nexy	[0x71600d680] invalidated after the last release of the connection object
default	11:12:49.498420-0500	tccd	AUTHREQ_PROMPTING: msgID=78289.7, service=kTCCServiceAddressBook, subject=Sub:{com.nexy.assistant}Resp:{TCCDProcess: identifier=com.nexy.assistant, pid=78289, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy},
default	11:12:50.910800-0500	tccd	Publishing <TCCDEvent: type=Create, service=kTCCServiceAddressBook, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 3 subscribers: {
    476 = "<TCCDEventSubscriber: token=476, state=Passed, csid=com.apple.photolibraryd>";
    37 = "<TCCDEventSubscriber: token=37, state=Initial, csid=(null)>";
    467 = "<TCCDEventSubscriber: token=467, state=Passed, csid=com.apple.chronod>";
}
default	11:12:50.911689-0500	Nexy	[0x71600d7c0] invalidated after the last release of the connection object
default	11:12:50.928936-0500	chronod	[appAuth:com.nexy.assistant] tcc authorization(s) changed
default	11:12:50.972131-0500	Nexy	[0x71600d7c0] activating connection: mach=true listener=false peer=false name=com.apple.AddressBook.ContactsAccountsService
default	11:12:50.973383-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=78272.7, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=78289, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.sandboxd, pid=78272, auid=0, euid=0, binary_path=/usr/libexec/sandboxd}, },
default	11:12:50.975627-0500	tccd	AUTHREQ_SUBJECT: msgID=78272.7, subject=com.nexy.assistant,
default	11:12:51.001539-0500	tccd	AUTHREQ_SUBJECT: msgID=78272.8, subject=com.nexy.assistant,
error	11:12:51.006609-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAddressBook com.nexy.assistant full
error	11:12:51.006724-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAddressBook com.nexy.assistant full
default	11:12:51.074111-0500	Nexy	[0x71600d680] activating connection: mach=true listener=false peer=false name=com.apple.accountsd.accountmanager
fault	11:12:51.075207-0500	Nexy	Attempted to register account monitor for types client is not authorized to access: <private>
error	11:12:51.075268-0500	Nexy	<private> 0x715013000: Store registration failed: Error Domain=com.apple.accounts Code=7 "(null)"
error	11:12:51.075294-0500	Nexy	<private> 0x715013000: Update event received, but store registration failed. This event will be handled, but the behavior is undefined.
default	11:12:51.076050-0500	Nexy	Adding shared photo decorator (includeSharedPhotoContacts=YES)
default	11:12:51.086426-0500	Nexy	[0x71600d900] activating connection: mach=true listener=false peer=false name=com.apple.AddressBook.ContactsAccountsService
default	11:12:51.087129-0500	Nexy	[0x71600d900] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	11:12:51.087167-0500	Nexy	Will add prepared store without migration (path: file:///Users/sergiyzasorin/Library/Application%20Support/AddressBook/AddressBook-v22.abcddb)
default	11:12:51.087364-0500	Nexy	Will add XPC store with options: <private> <private>
default	11:12:51.090034-0500	Nexy	[0x7150bc3c0] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	11:12:51.090989-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=12844.2521, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=78289, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=12844, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	11:12:51.091028-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=12844, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=78289, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	11:12:51.092410-0500	tccd	AUTHREQ_SUBJECT: msgID=12844.2521, subject=com.nexy.assistant,
default	11:12:51.093868-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb2ed5c000 at /Applications/Nexy.app
default	11:12:51.121381-0500	Nexy	[0x7150bc3c0] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	11:12:51.121494-0500	Nexy	[0x7150bc3c0] activating connection: mach=false listener=false peer=false name=(anonymous)
default	11:12:51.121598-0500	Nexy	[0x7150bc500] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	11:12:51.122554-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=12844.2522, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=78289, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=12844, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	11:12:51.122590-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=12844, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=78289, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	11:12:51.124113-0500	tccd	AUTHREQ_SUBJECT: msgID=12844.2522, subject=com.nexy.assistant,
default	11:12:51.124872-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb2ed5c000 at /Applications/Nexy.app
default	11:12:51.151887-0500	Nexy	[0x7150bc500] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	11:12:51.151979-0500	Nexy	[0x7150bc500] activating connection: mach=false listener=false peer=false name=(anonymous)
default	11:12:51.152050-0500	Nexy	[0x7150bc640] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	11:12:51.153008-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=12844.2523, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=78289, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=12844, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	11:12:51.153045-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=12844, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=78289, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	11:12:51.154586-0500	tccd	AUTHREQ_SUBJECT: msgID=12844.2523, subject=com.nexy.assistant,
default	11:12:51.155354-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb2ed5c000 at /Applications/Nexy.app
default	11:12:51.181330-0500	Nexy	[0x7150bc640] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	11:12:51.181441-0500	Nexy	[0x7150bc640] activating connection: mach=false listener=false peer=false name=(anonymous)
default	11:12:51.181524-0500	Nexy	[0x7150bc780] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	11:12:51.182996-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=12844.2524, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=78289, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=12844, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	11:12:51.183043-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=12844, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=78289, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	11:12:51.185427-0500	tccd	AUTHREQ_SUBJECT: msgID=12844.2524, subject=com.nexy.assistant,
default	11:12:51.186419-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb2ed5c000 at /Applications/Nexy.app
default	11:12:51.214145-0500	Nexy	[0x7150bc780] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	11:12:51.214246-0500	Nexy	[0x7150bc780] activating connection: mach=false listener=false peer=false name=(anonymous)
default	11:12:51.228616-0500	Nexy	Did add XPC store
default	11:12:51.228646-0500	Nexy	Did add prepared store without migration (path: file:///Users/sergiyzasorin/Library/Application%20Support/AddressBook/AddressBook-v22.abcddb)
default	11:12:51.232474-0500	Nexy	0x714bb8580: Using cached account information
default	11:12:51.233743-0500	Nexy	[0x71602b6b0] Session created.
default	11:12:51.233764-0500	Nexy	[0x71602b6b0] Session created with Mach Service: <private>
default	11:12:51.233778-0500	Nexy	[0x7150bcdc0] activating connection: mach=true listener=false peer=false name=com.apple.contacts.account-caching
default	11:12:51.233962-0500	Nexy	[0x71602b6b0] Session activated
default	11:12:51.237310-0500	Nexy	[0x7150bcdc0] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	11:12:51.237318-0500	Nexy	[0x71602b6b0] Session canceled.
default	11:12:51.237329-0500	Nexy	[0x71602b6b0] Disposing of session
default	11:12:51.237900-0500	Nexy	[0x7150bcdc0] activating connection: mach=true listener=false peer=false name=com.apple.AddressBook.ContactsAccountsService
default	11:12:51.238709-0500	Nexy	[0x7150bcdc0] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	11:12:51.238738-0500	Nexy	Will add prepared store without migration (path: file:///Users/sergiyzasorin/Library/Application%20Support/AddressBook/Sources/4437DACA-BE14-412E-B504-7A2DD2E9DC7D/AddressBook-v22.abcddb)
default	11:12:51.238759-0500	Nexy	Will add XPC store with options: <private> <private>
default	11:12:51.243632-0500	Nexy	[0x7150bf840] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	11:12:51.244921-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=12844.2525, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=78289, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=12844, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	11:12:51.244965-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=12844, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=78289, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	11:12:51.246859-0500	tccd	AUTHREQ_SUBJECT: msgID=12844.2525, subject=com.nexy.assistant,
default	11:12:51.247672-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb2ed5c000 at /Applications/Nexy.app
default	11:12:51.275861-0500	Nexy	[0x7150bf840] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	11:12:51.275954-0500	Nexy	[0x7150bf840] activating connection: mach=false listener=false peer=false name=(anonymous)
default	11:12:51.276062-0500	Nexy	[0x7150bf980] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	11:12:51.277271-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=12844.2526, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=78289, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=12844, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	11:12:51.277319-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=12844, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=78289, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	11:12:51.279256-0500	tccd	AUTHREQ_SUBJECT: msgID=12844.2526, subject=com.nexy.assistant,
default	11:12:51.280263-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb2ed5c000 at /Applications/Nexy.app
default	11:12:51.305354-0500	Nexy	[0x7150bf980] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	11:12:51.305454-0500	Nexy	[0x7150bf980] activating connection: mach=false listener=false peer=false name=(anonymous)
default	11:12:51.305560-0500	Nexy	[0x7150bfac0] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	11:12:51.306683-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=12844.2527, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=78289, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=12844, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	11:12:51.306720-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=12844, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=78289, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	11:12:51.308317-0500	tccd	AUTHREQ_SUBJECT: msgID=12844.2527, subject=com.nexy.assistant,
default	11:12:51.309252-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb2ed5c000 at /Applications/Nexy.app
default	11:12:51.337013-0500	Nexy	[0x7150bfac0] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	11:12:51.337104-0500	Nexy	[0x7150bfac0] activating connection: mach=false listener=false peer=false name=(anonymous)
default	11:12:51.337186-0500	Nexy	[0x7150bfc00] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	11:12:51.338232-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=12844.2528, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=78289, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=12844, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	11:12:51.338268-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=12844, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=78289, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	11:12:51.339891-0500	tccd	AUTHREQ_SUBJECT: msgID=12844.2528, subject=com.nexy.assistant,
default	11:12:51.340655-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb2ed5c000 at /Applications/Nexy.app
default	11:12:51.369244-0500	Nexy	[0x7150bfc00] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	11:12:51.369359-0500	Nexy	[0x7150bfc00] activating connection: mach=false listener=false peer=false name=(anonymous)
default	11:12:51.381161-0500	Nexy	Did add XPC store
default	11:12:51.381234-0500	Nexy	Did add prepared store without migration (path: file:///Users/sergiyzasorin/Library/Application%20Support/AddressBook/Sources/4437DACA-BE14-412E-B504-7A2DD2E9DC7D/AddressBook-v22.abcddb)
default	11:12:51.381385-0500	Nexy	[0x7150bfe80] activating connection: mach=true listener=false peer=false name=com.apple.AddressBook.ContactsAccountsService
default	11:12:51.382554-0500	Nexy	[0x7150bfe80] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	11:12:51.382757-0500	Nexy	Will add prepared store without migration (path: file:///Users/sergiyzasorin/Library/Application%20Support/AddressBook/AddressBook-v22.abcddb)
default	11:12:51.382791-0500	Nexy	Will add XPC store with options: <private> <private>
default	11:12:51.387547-0500	Nexy	[0x7150e2940] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	11:12:51.389090-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=12844.2529, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=78289, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=12844, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	11:12:51.389127-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=12844, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=78289, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	11:12:51.391083-0500	tccd	AUTHREQ_SUBJECT: msgID=12844.2529, subject=com.nexy.assistant,
default	11:12:51.392066-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb2ed5c000 at /Applications/Nexy.app
default	11:12:51.421610-0500	Nexy	[0x7150e2940] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	11:12:51.421698-0500	Nexy	[0x7150e2940] activating connection: mach=false listener=false peer=false name=(anonymous)
default	11:12:51.421767-0500	Nexy	[0x7150e2a80] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	11:12:51.422869-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=12844.2530, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=78289, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=12844, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	11:12:51.422910-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=12844, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=78289, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	11:12:51.424555-0500	tccd	AUTHREQ_SUBJECT: msgID=12844.2530, subject=com.nexy.assistant,
default	11:12:51.425360-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb2ed5c000 at /Applications/Nexy.app
default	11:12:51.452831-0500	Nexy	[0x7150e2a80] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	11:12:51.452994-0500	Nexy	[0x7150e2a80] activating connection: mach=false listener=false peer=false name=(anonymous)
default	11:12:51.453074-0500	Nexy	[0x7150e2bc0] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	11:12:51.454265-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=12844.2531, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=78289, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=12844, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	11:12:51.454303-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=12844, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=78289, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	11:12:51.455941-0500	tccd	AUTHREQ_SUBJECT: msgID=12844.2531, subject=com.nexy.assistant,
default	11:12:51.456758-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb2ed5c000 at /Applications/Nexy.app
default	11:12:51.484599-0500	Nexy	[0x7150e2bc0] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	11:12:51.484704-0500	Nexy	[0x7150e2bc0] activating connection: mach=false listener=false peer=false name=(anonymous)
default	11:12:51.484783-0500	Nexy	[0x7150e2d00] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	11:12:51.485871-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=12844.2532, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=78289, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=12844, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	11:12:51.485903-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=12844, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=78289, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	11:12:51.487463-0500	tccd	AUTHREQ_SUBJECT: msgID=12844.2532, subject=com.nexy.assistant,
default	11:12:51.488262-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb2ed5c000 at /Applications/Nexy.app
default	11:12:51.514647-0500	Nexy	[0x7150e2d00] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	11:12:51.514733-0500	Nexy	[0x7150e2d00] activating connection: mach=false listener=false peer=false name=(anonymous)
default	11:12:51.516439-0500	Nexy	Did add XPC store
default	11:12:51.516479-0500	Nexy	Did add prepared store without migration (path: file:///Users/sergiyzasorin/Library/Application%20Support/AddressBook/AddressBook-v22.abcddb)
default	11:12:51.539757-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=12844.2533, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=78289, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=12844, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	11:12:51.539815-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=12844, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=78289, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	11:12:51.541800-0500	tccd	AUTHREQ_SUBJECT: msgID=12844.2533, subject=com.nexy.assistant,
default	11:12:51.543016-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb2ed5c000 at /Applications/Nexy.app
default	11:12:51.576760-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=12844.2534, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=78289, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=12844, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	11:12:51.576807-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=12844, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=78289, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	11:12:51.578772-0500	tccd	AUTHREQ_SUBJECT: msgID=12844.2534, subject=com.nexy.assistant,
default	11:12:51.579898-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb2ed5c000 at /Applications/Nexy.app
default	11:12:53.865761-0500	Nexy	[0x7150e30c0] activating connection: mach=true listener=false peer=false name=com.apple.system.opendirectoryd.api
default	11:12:56.524595-0500	ControlCenter	Recent activity attributions changed to ["scr:com.nexy.assistant"]
default	11:13:05.495562-0500	Nexy	[0x7150e3200] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	11:13:05.497392-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=78289.8, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=78289, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	11:13:05.500252-0500	tccd	AUTHREQ_SUBJECT: msgID=78289.8, subject=com.nexy.assistant,
default	11:13:05.501801-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x93ad32700 at /Applications/Nexy.app
default	11:13:05.528222-0500	tccd	Notifying for access  kTCCServiceListenEvent for target PID[78289], responsiblePID[78289], responsiblePath: /Applications/Nexy.app to UID: 501
default	11:13:05.528623-0500	Nexy	[0x7150e3200] invalidated after the last release of the connection object
default	11:13:05.578291-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x93ad33000 at /Applications/Nexy.app
default	11:13:05.598886-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x93ad32700 at /Applications/Nexy.app
default	11:13:05.603091-0500	tccd	Publishing <TCCDEvent: type=Modify, service=kTCCServiceListenEvent, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 0 subscribers: {
}
default	11:13:07.778794-0500	spindump	Nexy [78289]: spin: not sampling due to conditions 0x400000000
default	11:13:10.458735-0500	Nexy	"ACMonitoredAccountStore: Fetching accounts of account type com.apple.account.CardDAV..."
default	11:13:10.487478-0500	Nexy	"ACMonitoredAccountStore: Fetched Accounts"
default	11:13:10.487505-0500	Nexy	"ACMonitoredAccountStore: account was added: <private>"
error	11:13:10.487584-0500	Nexy	<private> 0x715013000: Update event received, but store registration failed. This event will be handled, but the behavior is undefined.
default	11:13:10.989217-0500	Nexy	"ACMonitoredAccountStore: Fetching accounts of account type com.apple.account.CardDAV..."
error	11:13:11.639558-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceListenEvent com.nexy.assistant none
error	11:13:11.641047-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceListenEvent com.nexy.assistant none
error	11:13:11.841057-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAddressBook com.nexy.assistant full
error	11:13:11.841145-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceMicrophone com.nexy.assistant full
error	11:13:11.851676-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceMicrophone com.nexy.assistant full
default	11:13:16.915035-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x93ad31b00 at /Applications/Nexy.app
default	11:13:16.937741-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x93ad32a00 at /Applications/Nexy.app
default	11:13:16.949856-0500	tccd	Publishing <TCCDEvent: type=Modify, service=kTCCServiceListenEvent, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 0 subscribers: {
}
error	11:13:17.084090-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceScreenCapture com.nexy.assistant full
error	11:13:17.084701-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceListenEvent com.nexy.assistant full
error	11:13:17.085633-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceScreenCapture com.nexy.assistant full
error	11:13:17.086215-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceListenEvent com.nexy.assistant full
error	11:13:17.120778-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAddressBook com.nexy.assistant full
error	11:13:17.120784-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAddressBook com.nexy.assistant full
error	11:13:17.122265-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceMicrophone com.nexy.assistant full
error	11:13:17.122375-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceMicrophone com.nexy.assistant full
default	11:13:18.537617-0500	Nexy	server port 0x00010e3f, session port 0x0000340b
default	11:13:18.539589-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=387.1652, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=78289, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=387, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	11:13:18.539686-0500	tccd	requestor: TCCDProcess: identifier=com.apple.WindowServer, pid=387, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=78289, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	11:13:18.542033-0500	tccd	AUTHREQ_SUBJECT: msgID=387.1652, subject=com.nexy.assistant,
default	11:13:18.543678-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x93ad32a00 at /Applications/Nexy.app
default	11:13:21.661132-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x93ad32a00 at /Applications/Nexy.app
default	11:13:21.697792-0500	Nexy	[0x7150e3340] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	11:13:21.699019-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=78289.9, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=78289, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	11:13:21.700860-0500	tccd	AUTHREQ_SUBJECT: msgID=78289.9, subject=com.nexy.assistant,
default	11:13:21.701940-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x93ad32a00 at /Applications/Nexy.app
default	11:13:21.724256-0500	tccd	Notifying for access  kTCCServicePostEvent for target PID[78289], responsiblePID[78289], responsiblePath: /Applications/Nexy.app to UID: 501
default	11:13:21.724785-0500	Nexy	[0x7150e3340] invalidated after the last release of the connection object
default	11:13:21.760410-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x93ad31b00 at /Applications/Nexy.app
default	11:13:21.781533-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x93ad32a00 at /Applications/Nexy.app
default	11:13:21.785960-0500	tccd	Publishing <TCCDEvent: type=Modify, service=kTCCServicePostEvent, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 0 subscribers: {
}
error	11:13:21.845309-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceScreenCapture com.nexy.assistant full
error	11:13:21.845927-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceListenEvent com.nexy.assistant full
error	11:13:21.846055-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAccessibility com.nexy.assistant none
error	11:13:21.847096-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceScreenCapture com.nexy.assistant full
error	11:13:21.847675-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceListenEvent com.nexy.assistant full
error	11:13:21.847790-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAccessibility com.nexy.assistant none
error	11:13:21.878653-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAddressBook com.nexy.assistant full
error	11:13:21.879774-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAddressBook com.nexy.assistant full
error	11:13:21.880167-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceMicrophone com.nexy.assistant full
error	11:13:21.881237-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceMicrophone com.nexy.assistant full
default	11:13:25.179100-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x93ad31b00 at /Applications/Nexy.app
default	11:13:25.200546-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x93ad32a00 at /Applications/Nexy.app
default	11:13:25.226753-0500	tccd	Publishing <TCCDEvent: type=Modify, service=kTCCServiceAccessibility, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 0 subscribers: {
}
error	11:13:25.262284-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAccessibility com.nexy.assistant full
error	11:13:25.262515-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceScreenCapture com.nexy.assistant full
error	11:13:25.263109-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceListenEvent com.nexy.assistant full
error	11:13:25.263231-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAccessibility com.nexy.assistant full
error	11:13:25.268023-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAccessibility com.nexy.assistant full
error	11:13:25.268260-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceScreenCapture com.nexy.assistant full
error	11:13:25.268865-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceListenEvent com.nexy.assistant full
error	11:13:25.268986-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAccessibility com.nexy.assistant full
error	11:13:25.293885-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAddressBook com.nexy.assistant full
error	11:13:25.295299-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceMicrophone com.nexy.assistant full
error	11:13:25.296446-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAddressBook com.nexy.assistant full
error	11:13:25.297746-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceMicrophone com.nexy.assistant full
default	11:13:34.805063-0500	Nexy	[0x7150e3340] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
error	11:13:34.805735-0500	tccd	TCCDProcess: identifier=com.nexy.assistant, pid=78289, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy attempted to call TCCAccessRequest for kTCCServiceAccessibility without the recommended com.apple.private.tcc.manager.check-by-audit-token entitlement
default	11:13:34.805932-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=78289.10, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=78289, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.nexy.assistant, pid=78289, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	11:13:34.807157-0500	tccd	AUTHREQ_SUBJECT: msgID=78289.10, subject=com.nexy.assistant,
default	11:13:34.807884-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x93ad32a00 at /Applications/Nexy.app
default	11:13:34.827433-0500	Nexy	[0x7150e3340] invalidated after the last release of the connection object
default	11:13:37.837266-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=78272.9, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=78289, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.sandboxd, pid=78272, auid=0, euid=0, binary_path=/usr/libexec/sandboxd}, },
default	11:13:37.840579-0500	tccd	AUTHREQ_SUBJECT: msgID=78272.9, subject=com.nexy.assistant,
default	11:13:37.842890-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x93ad32a00 at /Applications/Nexy.app
default	11:13:37.874490-0500	tccd	Publishing <TCCDEvent: type=Create, service=kTCCServiceSystemPolicyAllFiles, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 0 subscribers: {
}
error	11:13:37.874985-0500	kernel	System Policy: Nexy(78289) deny(1) file-read-data /Users/sergiyzasorin/Library/Messages/chat.db
default	11:13:37.964447-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x93ad32a00 at /Applications/Nexy.app
default	11:13:38.899866-0500	Nexy	"ACMonitoredAccountStore: Fetching accounts of account type com.apple.account.CardDAV..."
default	11:13:38.988429-0500	Nexy	"ACMonitoredAccountStore: Fetched Accounts"
error	11:13:39.289333-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceSystemPolicyAllFiles com.nexy.assistant none
error	11:13:39.289730-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAccessibility com.nexy.assistant full
error	11:13:39.290857-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceScreenCapture com.nexy.assistant full
error	11:13:39.291062-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceSystemPolicyAllFiles com.nexy.assistant none
error	11:13:39.291307-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAccessibility com.nexy.assistant full
error	11:13:39.291502-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceListenEvent com.nexy.assistant full
error	11:13:39.292056-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceScreenCapture com.nexy.assistant full
error	11:13:39.424437-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAddressBook com.nexy.assistant full
error	11:13:39.456654-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceMicrophone com.nexy.assistant full
error	11:13:39.457571-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceMicrophone com.nexy.assistant full
default	11:13:43.648252-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x93ad32400 at /Applications/Nexy.app
default	11:13:43.693541-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x93ad32700 at /Applications/Nexy.app
default	11:13:43.704447-0500	tccd	Publishing <TCCDEvent: type=Modify, service=kTCCServiceSystemPolicyAllFiles, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 0 subscribers: {
}
error	11:13:43.869528-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAccessibility com.nexy.assistant full
error	11:13:43.870004-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceSystemPolicyAllFiles com.nexy.assistant full
error	11:13:43.870203-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceListenEvent com.nexy.assistant full
error	11:13:43.870402-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceScreenCapture com.nexy.assistant full
error	11:13:43.870523-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAccessibility com.nexy.assistant full
error	11:13:43.871161-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAccessibility com.nexy.assistant full
error	11:13:43.871359-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceListenEvent com.nexy.assistant full
error	11:13:43.871788-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceSystemPolicyAllFiles com.nexy.assistant full
error	11:13:43.872025-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceScreenCapture com.nexy.assistant full
error	11:13:43.872148-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAccessibility com.nexy.assistant full
error	11:13:43.910666-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAddressBook com.nexy.assistant full
error	11:13:43.910727-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAddressBook com.nexy.assistant full
error	11:13:43.912061-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceMicrophone com.nexy.assistant full
error	11:13:43.912113-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceMicrophone com.nexy.assistant full
default	11:13:51.016753-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=78272.11, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=78289, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.sandboxd, pid=78272, auid=0, euid=0, binary_path=/usr/libexec/sandboxd}, },
default	11:13:51.033191-0500	tccd	AUTHREQ_SUBJECT: msgID=78272.11, subject=com.nexy.assistant,
default	11:13:51.035120-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x93ad32700 at /Applications/Nexy.app
default	11:13:55.100774-0500	Nexy	[0x7150e3480] activating connection: mach=true listener=false peer=false name=com.apple.usernoted.client
default	11:13:55.129822-0500	distnoted	register name: com.apple.nsquiet_safe_quit_give_reason object: com.nexy.assistant token: 3000000033 pid: 78289
default	11:13:55.134202-0500	Nexy	NSApp cache appearance:
-NSRequiresAquaSystemAppearance: 0
-appearance: (null)
-effectiveAppearance: <NSCompositeAppearance: 0x71573c820
 (
    "<NSAquaAppearance: 0x71573c640>",
    "<NSSystemAppearance: 0x71573c780>"
)>
default	11:13:55.138075-0500	usernoted	Connection com.nexy.assistant with path: /Applications/Nexy.app
default	11:13:55.140616-0500	Nexy	[0x7150e3980] activating connection: mach=true listener=false peer=false name=com.apple.dock.fullscreen
default	11:13:55.141923-0500	Nexy	[0x7150e3ac0] activating connection: mach=true listener=false peer=false name=com.apple.fonts
default	11:13:55.145941-0500	Nexy	(<private>) deleteSearchableItemsWithDomainIdentifiers, protectionClass:(null), domainIdentifiers number:1
default	11:13:55.146500-0500	Nexy	sConnectionName: com.apple.spotlight.IndexAgent
default	11:13:55.146547-0500	Nexy	Start service name com.apple.spotlight.IndexAgent
default	11:13:55.146575-0500	Nexy	[0x7150e3c00] activating connection: mach=true listener=false peer=false name=com.apple.spotlight.IndexAgent
default	11:13:55.146923-0500	Nexy	[C:1] Alloc com.apple.controlcenter.statusitems
default	11:13:55.146985-0500	Nexy	[0x7150e3d40] activating connection: mach=false listener=false peer=false name=(anonymous)
default	11:13:55.147058-0500	Nexy	FBSWorkspace registering source: <private>
default	11:13:55.148535-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	11:13:55.148662-0500	Nexy	<FBSWorkspaceScenesClient:0x7179e4140 <private>> attempting immediate handshake from activate
default	11:13:55.148969-0500	Nexy	<FBSWorkspaceScenesClient:0x7179e4140 <private>> sent handshake
default	11:13:55.149101-0500	Nexy	Realizing settings extension __NSStatusItemSceneHostSettings__ on FBSSceneSettings
default	11:13:55.149900-0500	Nexy	Realizing settings extension __NSStatusItemSceneClientSettings__ on FBSSceneClientSettings
default	11:13:55.149887-0500	ControlCenter	Asked to bootstrap a new process for handle: [app<application.com.nexy.assistant.53053210.53053219(501)>:78289]
default	11:13:55.150232-0500	ControlCenter	Creating process (sync=true) for handle: [app<application.com.nexy.assistant.53053210.53053219(501)>:78289]
default	11:13:55.151005-0500	ControlCenter	[app<application.com.nexy.assistant.53053210.53053219>:78289] Registering event dispatcher at init
default	11:13:55.151581-0500	ControlCenter	Created <FBWorkspace: 0xb081a2a80; <FBApplicationProcess: 0xb081c7600; app<application.com.nexy.assistant.53053210.53053219>:78289(v91879)>>
default	11:13:55.151603-0500	ControlCenter	Bootstrapping app<application.com.nexy.assistant.53053210.53053219> with intent background
default	11:13:55.152065-0500	Nexy	Realizing settings extension FBSSceneSettingsCore on FBSSceneSettings
default	11:13:55.152225-0500	runningboardd	Launch request for app<application.com.nexy.assistant.53053210.53053219(501)>[0] is using uid 501 (divined from auid 501 euid 501)
default	11:13:55.152338-0500	runningboardd	Acquiring assertion targeting app<application.com.nexy.assistant.53053210.53053219(501)> from originator [osservice<com.apple.controlcenter(501)>:626] with description <RBSAssertionDescriptor| "FBApplicationProcess" ID:394-626-35008 target:app<application.com.nexy.assistant.53053210.53053219(501)> attributes:[
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableLPRunReason-Suspend" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableRole-NonUI" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableJetsamPriority-Active" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableBootstrapping" sourceEnvironment:"(null)">
	]>
default	11:13:55.152477-0500	runningboardd	Assertion 394-626-35008 (target:app<application.com.nexy.assistant.53053210.53053219(501)>) will be created as active
default	11:13:55.152513-0500	runningboardd	setting abstract target for <RBSAssertionDescriptor| "FBApplicationProcess" ID:394-626-35008 target:app<application.com.nexy.assistant.53053210.53053219(501)> attributes:[
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableLPRunReason-Suspend" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableRole-NonUI" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableJetsamPriority-Active" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableBootstrapping" sourceEnvironment:"(null)">
	]> to [app<application.com.nexy.assistant.53053210.53053219(501)>:78289]
default	11:13:55.154103-0500	Nexy	Realizing settings extension FBSSceneClientSettingsCore on FBSSceneClientSettings
default	11:13:55.155309-0500	Nexy	Requesting scene <FBSScene: 0x7179e6b20; com.apple.controlcenter:8C5A215C-D4E4-4556-8E3B-92BE2E7D6C5F> from com.apple.controlcenter.statusitems
default	11:13:55.152847-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78289] Ignoring jetsam update because this process is not memory-managed
default	11:13:55.155303-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78289] Ignoring suspend because this process is not lifecycle managed
default	11:13:55.156132-0500	suggestd	SGDSpotlightReceiver: deleting 1 domain identifiers (1 after removing overlaps) for com.nexy.assistant: <private>
default	11:13:55.156059-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78289] Ignoring GPU update because this process is not GPU managed
default	11:13:55.156147-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78289] Ignoring memory limit update because this process is not memory-managed
default	11:13:55.157499-0500	Nexy	Request for <FBSScene: 0x7179e6b20; com.apple.controlcenter:8C5A215C-D4E4-4556-8E3B-92BE2E7D6C5F> complete!
default	11:13:55.157593-0500	Nexy	Realizing settings extension FBSSceneTransitionContextCore on FBSSceneTransitionContext
default	11:13:55.158622-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.53053210.53053219(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	11:13:55.159640-0500	gamepolicyd	Received state update for 78289 (app<application.com.nexy.assistant.53053210.53053219(501)>, running-active-NotVisible
default	11:13:55.159780-0500	Nexy	Realizing settings extension __NSHostedViewSceneSettings__ on FBSSceneSettings
default	11:13:55.160052-0500	Nexy	Realizing settings extension __NSClientHostedViewSceneSettings__ on FBSSceneClientSettings
default	11:13:55.160305-0500	Nexy	Realizing settings extension __NSStatusItemAuxiliaryViewSceneSettings__ on FBSSceneSettings
default	11:13:55.160346-0500	Nexy	Realizing settings extension __NSClientStatusItemAuxiliaryViewSceneSettings__ on FBSSceneClientSettings
default	11:13:55.160643-0500	Nexy	Requesting scene <FBSScene: 0x7179e6bc0; com.apple.controlcenter:8C5A215C-D4E4-4556-8E3B-92BE2E7D6C5F-Aux[1]-NSStatusItemView> from com.apple.controlcenter.statusitems
default	11:13:55.160912-0500	Nexy	Request for <FBSScene: 0x7179e6bc0; com.apple.controlcenter:8C5A215C-D4E4-4556-8E3B-92BE2E7D6C5F-Aux[1]-NSStatusItemView> complete!
default	11:13:55.162281-0500	ControlCenter	[app<application.com.nexy.assistant.53053210.53053219>:78289] Bootstrap success!
default	11:13:55.162859-0500	ControlCenter	[app<application.com.nexy.assistant.53053210.53053219>:78289] Setting process visibility to: Background
default	11:13:55.162959-0500	ControlCenter	[app<application.com.nexy.assistant.53053210.53053219>:78289] No launch watchdog for this process, dropping initial assertion in 2.0s
default	11:13:55.163360-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.53053210.53053219(501)>:78289] from originator [osservice<com.apple.controlcenter(501)>:626] with description <RBSAssertionDescriptor| "FBWorkspaceDomain: injecting saved endowment" ID:394-626-35009 target:78289 attributes:[
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"WorkspaceEndpointInjection" sourceEnvironment:"(null)">
	]>
default	11:13:55.163435-0500	runningboardd	Assertion 394-626-35009 (target:[app<application.com.nexy.assistant.53053210.53053219(501)>:78289]) will be created as active
default	11:13:55.163856-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78289] Ignoring jetsam update because this process is not memory-managed
default	11:13:55.163868-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78289] Ignoring suspend because this process is not lifecycle managed
default	11:13:55.163878-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78289] Ignoring GPU update because this process is not GPU managed
default	11:13:55.163902-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78289] Ignoring memory limit update because this process is not memory-managed
default	11:13:55.165045-0500	Nexy	[com.apple.controlcenter:8C5A215C-D4E4-4556-8E3B-92BE2E7D6C5F-Aux[1]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
default	11:13:55.165067-0500	Nexy	[com.apple.controlcenter:8C5A215C-D4E4-4556-8E3B-92BE2E7D6C5F-Aux[1]-NSStatusItemView] Dropping transition context because the scene is reconnecting
default	11:13:55.169414-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.53053210.53053219(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	11:13:55.169668-0500	Nexy	[com.apple.controlcenter:8C5A215C-D4E4-4556-8E3B-92BE2E7D6C5F-Aux[1]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
default	11:13:55.169687-0500	Nexy	[com.apple.controlcenter:8C5A215C-D4E4-4556-8E3B-92BE2E7D6C5F-Aux[1]-NSStatusItemView] Dropping transition context because the scene is reconnecting
default	11:13:55.169919-0500	ControlCenter	Adding: <FBApplicationProcess: 0xb081c7600; app<application.com.nexy.assistant.53053210.53053219>:78289(v91879)>
default	11:13:55.169814-0500	Nexy	Warning: the app is using `-[NSStatusBarButton setHighlightsBy:]` to set the highlight behavior. Instead, consider removing that setting. That will enable macOS to highlight the status bar button as appropriate for all configurations (e.g., light, dark, and increased contrast modes).
default	11:13:55.170329-0500	gamepolicyd	Received state update for 78289 (app<application.com.nexy.assistant.53053210.53053219(501)>, running-active-NotVisible
default	11:13:55.170435-0500	ControlCenter	[app<application.com.nexy.assistant.53053210.53053219>:78289] Connection established.
default	11:13:55.170519-0500	ControlCenter	[app<application.com.nexy.assistant.53053210.53053219>:78289] created proxy of <BSXPCServiceConnectionProxy<FBSWorkspaceServiceServerInterface>: 0xb08210070>
default	11:13:55.170541-0500	ControlCenter	[app<application.com.nexy.assistant.53053210.53053219>:78289] Connection to remote process established!
default	11:13:55.170568-0500	ControlCenter	Received state update for 78289 (app<application.com.nexy.assistant.53053210.53053219(501)>, running-active-NotVisible
default	11:13:55.178487-0500	ControlCenter	Asked to bootstrap a new process for handle: [app<application.com.nexy.assistant.53053210.53053219(501)>:78289]
default	11:13:55.178505-0500	ControlCenter	A process already exists for this handle: <FBApplicationProcess: 0xb081c7600; app<application.com.nexy.assistant.53053210.53053219>:78289(v91879)>
default	11:13:55.178656-0500	ControlCenter	[app<application.com.nexy.assistant.53053210.53053219>:78289] Registered new scene: <FBWorkspaceScene: 0xb074809c0; com.apple.controlcenter:8C5A215C-D4E4-4556-8E3B-92BE2E7D6C5F> (fromRemnant = 0)
default	11:13:55.178700-0500	ControlCenter	[app<application.com.nexy.assistant.53053210.53053219>:78289] Workspace interruption policy did change: reconnect
default	11:13:55.179122-0500	ControlCenter	[com.apple.controlcenter:8C5A215C-D4E4-4556-8E3B-92BE2E7D6C5F] Client process connected: [app<application.com.nexy.assistant.53053210.53053219(501)>:78289]
default	11:13:55.179105-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.53053210.53053219(501)>:78289] from originator [osservice<com.apple.controlcenter(501)>:626] with description <RBSAssertionDescriptor| "com.apple.frontboard.after-life.interrupted" ID:394-626-35010 target:78289 attributes:[
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"AfterLife-Interrupted" sourceEnvironment:"(null)">
	]>
default	11:13:55.179152-0500	Nexy	Request for <FBSScene: 0x7179e6b20; com.apple.controlcenter:8C5A215C-D4E4-4556-8E3B-92BE2E7D6C5F> complete!
default	11:13:55.179229-0500	runningboardd	Assertion 394-626-35010 (target:[app<application.com.nexy.assistant.53053210.53053219(501)>:78289]) will be created as inactive as originator process has not exited
default	11:13:55.180058-0500	ControlCenter	Asked to bootstrap a new process for handle: [app<application.com.nexy.assistant.53053210.53053219(501)>:78289]
default	11:13:55.180073-0500	ControlCenter	A process already exists for this handle: <FBApplicationProcess: 0xb081c7600; app<application.com.nexy.assistant.53053210.53053219>:78289(v91879)>
default	11:13:55.180299-0500	Nexy	Request for <FBSScene: 0x7179e6bc0; com.apple.controlcenter:8C5A215C-D4E4-4556-8E3B-92BE2E7D6C5F-Aux[1]-NSStatusItemView> complete!
default	11:13:55.180121-0500	ControlCenter	[app<application.com.nexy.assistant.53053210.53053219>:78289] Registered new scene: <FBWorkspaceScene: 0xb07480000; com.apple.controlcenter:8C5A215C-D4E4-4556-8E3B-92BE2E7D6C5F-Aux[1]-NSStatusItemView> (fromRemnant = 0)
default	11:13:55.180263-0500	ControlCenter	[com.apple.controlcenter:8C5A215C-D4E4-4556-8E3B-92BE2E7D6C5F-Aux[1]-NSStatusItemView] Client process connected: [app<application.com.nexy.assistant.53053210.53053219(501)>:78289]
default	11:13:55.181166-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.53053210.53053219(501)>:78289] from originator [osservice<com.apple.controlcenter(501)>:626] with description <RBSAssertionDescriptor| "FBWorkspace (BG-Active[40])" ID:394-626-35011 target:78289 attributes:[
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableLPRunReason-Suspend" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableRole-NonUI" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableJetsamPriority-Active" sourceEnvironment:"(null)">
	]>
default	11:13:55.181297-0500	runningboardd	Assertion 394-626-35011 (target:[app<application.com.nexy.assistant.53053210.53053219(501)>:78289]) will be created as active
default	11:13:55.181404-0500	ControlCenter	[app<application.com.nexy.assistant.53053210.53053219>:78289] Workspace state did change: XX-None[0] --> BG-Active[40] (assertion acquired).
default	11:13:55.181778-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78289] Ignoring jetsam update because this process is not memory-managed
default	11:13:55.181864-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78289] Ignoring suspend because this process is not lifecycle managed
default	11:13:55.182034-0500	Nexy	<FBSWorkspaceScenesClient:0x7179e4140 <private>> Reconnecting scene com.apple.controlcenter:8C5A215C-D4E4-4556-8E3B-92BE2E7D6C5F
default	11:13:55.181907-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78289] Ignoring GPU update because this process is not GPU managed
default	11:13:55.182029-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78289] Ignoring memory limit update because this process is not memory-managed
default	11:13:55.185969-0500	Nexy	Registering for test daemon availability notify post.
default	11:13:55.186131-0500	Nexy	notify_get_state check indicated test daemon not ready.
default	11:13:55.186238-0500	Nexy	notify_get_state check indicated test daemon not ready.
default	11:13:55.186331-0500	Nexy	notify_get_state check indicated test daemon not ready.
default	11:13:55.195914-0500	Nexy	[0x71600c3c0] Connection returned listener port: 0x4f03
default	11:13:55.196492-0500	Nexy	SignalReady: pid=78289 asn=0x0-0x292292
default	11:13:55.197288-0500	Nexy	SIGNAL: pid=78289 asn=0x0x-0x292292
default	11:13:55.203670-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x93ad32700 at /Applications/Nexy.app
default	11:13:55.221111-0500	Nexy	0x715013180: Posting CNCDContactStoreDidChangeNotification because accounts changed
default	11:13:55.221366-0500	Nexy	0x714c12dc0: Updating using cached account information
default	11:13:55.230875-0500	Nexy	[com.apple.controlcenter:8C5A215C-D4E4-4556-8E3B-92BE2E7D6C5F-Aux[1]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
default	11:13:55.237368-0500	Nexy	[com.apple.controlcenter:8C5A215C-D4E4-4556-8E3B-92BE2E7D6C5F-Aux[1]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
default	11:13:55.240384-0500	Nexy	void _NSDisableAutomaticTerminationAndLog(NSString *) Restoring windows
default	11:13:55.240396-0500	Nexy	-[NSApplication _reopenWindowsAsNecessaryIncludingRestorableState:withFullFidelity:completionHandler:] shouldRestoreState=1 hasPersistentStateToRestore=0 shouldStillRestoreStateAfterPrompting=0
default	11:13:55.240421-0500	Nexy	[0x71600d400] activating connection: mach=true listener=false peer=false name=com.apple.window_proxies
default	11:13:55.240619-0500	Nexy	[0x71600d400] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	11:13:55.243016-0500	Nexy	void _NSEnableAutomaticTerminationAndLog(NSString *) Restoring windows
default	11:13:55.250654-0500	Nexy	[C:2] Alloc <private>
default	11:13:55.250730-0500	Nexy	[0x71600d400] activating connection: mach=false listener=false peer=false name=(anonymous)
default	11:13:55.257317-0500	ControlCenter	Host properties initialized; (bid:com.nexy.assistant-Item-0-78289). State(applicationItem: true, clientRequestsVisibility: true, neverClip: false)
default	11:13:55.259294-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.53053210.53053219(501)>:78289] from originator [app<application.com.nexy.assistant.53053210.53053219(501)>:78289] with description <RBSAssertionDescriptor| "AudioHAL" ID:394-78289-35012 target:78289 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	11:13:55.259696-0500	runningboardd	Assertion 394-78289-35012 (target:[app<application.com.nexy.assistant.53053210.53053219(501)>:78289]) will be created as active
default	11:13:55.260889-0500	runningboardd	Invalidating assertion 394-78289-35012 (target:[app<application.com.nexy.assistant.53053210.53053219(501)>:78289]) from originator [app<application.com.nexy.assistant.53053210.53053219(501)>:78289]
default	11:13:55.261141-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.53053210.53053219(501)>:78289] from originator [app<application.com.nexy.assistant.53053210.53053219(501)>:78289] with description <RBSAssertionDescriptor| "AudioHAL" ID:394-78289-35013 target:78289 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	11:13:55.261329-0500	runningboardd	Assertion 394-78289-35013 (target:[app<application.com.nexy.assistant.53053210.53053219(501)>:78289]) will be created as active
default	11:13:55.261605-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78289] Ignoring jetsam update because this process is not memory-managed
default	11:13:55.261702-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78289] Ignoring suspend because this process is not lifecycle managed
default	11:13:55.261874-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78289] Ignoring GPU update because this process is not GPU managed
default	11:13:55.262748-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78289] Ignoring memory limit update because this process is not memory-managed
default	11:13:55.280261-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=12844.2785, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=78289, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=12844, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	11:13:55.280397-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=12844, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=78289, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	11:13:55.281948-0500	ControlCenter	Created ephemaral instance DisplayableId(1F2D3E3A) for (bid:com.nexy.assistant-Item-0-78289) with positioning .ephemeral
default	11:13:55.284166-0500	Nexy	[0x71600f840] activating connection: mach=true listener=false peer=false name=com.apple.AddressBook.ContactsAccountsService
default	11:13:55.288070-0500	Nexy	[0x71600f840] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	11:13:55.288130-0500	Nexy	Will add prepared store without migration (path: file:///Users/sergiyzasorin/Library/Application%20Support/AddressBook/Sources/4437DACA-BE14-412E-B504-7A2DD2E9DC7D/AddressBook-v22.abcddb)
default	11:13:55.288382-0500	Nexy	Will add XPC store with options: <private> <private>
default	11:13:55.289141-0500	tccd	AUTHREQ_SUBJECT: msgID=12844.2785, subject=com.nexy.assistant,
default	11:13:55.297007-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb2ed5c000 at /Applications/Nexy.app
default	11:13:55.298968-0500	Nexy	[0x7150bc3c0] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	11:13:55.300930-0500	gamepolicyd	Received state update for 78289 (app<application.com.nexy.assistant.53053210.53053219(501)>, running-active-NotVisible
default	11:13:55.302036-0500	Nexy	[com.apple.controlcenter:8C5A215C-D4E4-4556-8E3B-92BE2E7D6C5F-Aux[1]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
default	11:13:55.302644-0500	Nexy	[com.apple.controlcenter:8C5A215C-D4E4-4556-8E3B-92BE2E7D6C5F] Sending action(s) in update: NSSceneFenceAction
default	11:13:55.303675-0500	Nexy	[com.apple.controlcenter:8C5A215C-D4E4-4556-8E3B-92BE2E7D6C5F-Aux[1]-NSStatusItemView] Received action(s) in scene-update: NSSceneFenceAction
default	11:13:55.304169-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=12844.2786, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=78289, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=12844, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	11:13:55.304269-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=12844, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=78289, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	11:13:55.359246-0500	Nexy	[0x7150bc3c0] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	11:13:55.359345-0500	Nexy	[0x7150bc3c0] activating connection: mach=false listener=false peer=false name=(anonymous)
default	11:13:55.359469-0500	Nexy	[0x7150bc640] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	11:13:55.360512-0500	Nexy	Defaultable: persistentAccounts: <private>
default	11:13:55.360598-0500	Nexy	Defaultable: Rejecting account <ABAccount: 0x7179e68a0: identifier=_acceptedIntroductions, name=Other Known, baseURL=(nil), dsid=(nil)> because it can't become default
default	11:13:55.360646-0500	Nexy	Defaultable: Rejecting account <ABAccount: 0x7179e6800: identifier=_directoryServices, name=Directory Services, baseURL=(nil), dsid=(nil)> because it can't become default
default	11:13:55.361572-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=12844.2787, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=78289, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=12844, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	11:13:55.361633-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=12844, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=78289, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	11:13:55.363786-0500	Nexy	-awakeFromLoad
default	11:13:55.364100-0500	Nexy	-setServername: <private>  Parsed into scheme: https  host: <private>  port: 0  path: <private>
default	11:13:55.364248-0500	Nexy	-initWithUID:persistence: called on thread: <private>
default	11:13:55.364897-0500	tccd	AUTHREQ_SUBJECT: msgID=12844.2787, subject=com.nexy.assistant,
default	11:13:55.364940-0500	Nexy	-clearPrincipalProperties
default	11:13:55.364969-0500	Nexy	-clearHomeContainers
default	11:13:55.366130-0500	Nexy	Defaultable: Final list: <private>
default	11:13:55.366158-0500	Nexy	New account should become the default account
default	11:13:55.366599-0500	Nexy	0x715013180: Posting CNCDContactStoreDidChangeNotification because accounts changed
default	11:13:55.366641-0500	Nexy	0x714c12dc0: Updating using cached account information
default	11:13:55.366894-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb2ed5ed00 at /Applications/Nexy.app
default	11:13:55.369769-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78289] Ignoring jetsam update because this process is not memory-managed
default	11:13:55.369781-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78289] Ignoring suspend because this process is not lifecycle managed
default	11:13:55.369793-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78289] Ignoring GPU update because this process is not GPU managed
default	11:13:55.369812-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78289] Ignoring memory limit update because this process is not memory-managed
default	11:13:55.373531-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.53053210.53053219(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	11:13:55.374646-0500	ControlCenter	Received state update for 78289 (app<application.com.nexy.assistant.53053210.53053219(501)>, running-active-NotVisible
default	11:13:55.376322-0500	gamepolicyd	Received state update for 78289 (app<application.com.nexy.assistant.53053210.53053219(501)>, running-active-NotVisible
default	11:13:55.406512-0500	Nexy	[0x7150bc640] activating connection: mach=false listener=false peer=false name=(anonymous)
default	11:13:55.406657-0500	Nexy	[0x717ab8000] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	11:13:55.408252-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=12844.2788, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=78289, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=12844, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	11:13:55.408323-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=12844, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=78289, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	11:13:55.411331-0500	tccd	AUTHREQ_SUBJECT: msgID=12844.2788, subject=com.nexy.assistant,
default	11:13:55.412887-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb2ed5ed00 at /Applications/Nexy.app
default	11:13:55.453155-0500	Nexy	[0x717ab8000] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	11:13:55.453274-0500	Nexy	[0x717ab8000] activating connection: mach=false listener=false peer=false name=(anonymous)
default	11:13:55.453362-0500	Nexy	[0x717ab8140] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	11:13:55.460236-0500	tccd	AUTHREQ_SUBJECT: msgID=12844.2789, subject=com.nexy.assistant,
default	11:13:55.462474-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb2ed5ed00 at /Applications/Nexy.app
default	11:13:55.470987-0500	Nexy	*warn* MailCS ======%%% _setMailMessageAttributes skip:1
default	11:13:55.480228-0500	Nexy	Start service name com.apple.spotlightknowledged
default	11:13:55.481880-0500	Nexy	[GMS] availability notification token 115
default	11:13:55.508474-0500	Nexy	[0x717ab8140] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	11:13:55.508667-0500	Nexy	[0x717ab8140] activating connection: mach=false listener=false peer=false name=(anonymous)
default	11:13:55.512429-0500	Nexy	Did add XPC store
default	11:13:55.512471-0500	Nexy	Did add prepared store without migration (path: file:///Users/sergiyzasorin/Library/Application%20Support/AddressBook/Sources/4437DACA-BE14-412E-B504-7A2DD2E9DC7D/AddressBook-v22.abcddb)
default	11:13:55.512595-0500	Nexy	[0x717ab8780] activating connection: mach=true listener=false peer=false name=com.apple.AddressBook.ContactsAccountsService
default	11:13:55.513755-0500	Nexy	[0x717ab8780] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	11:13:55.513798-0500	Nexy	Will add prepared store without migration (path: file:///Users/sergiyzasorin/Library/Application%20Support/AddressBook/AddressBook-v22.abcddb)
default	11:13:55.513843-0500	Nexy	Will add XPC store with options: <private> <private>
default	11:13:55.518213-0500	Nexy	[0x717abb200] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	11:13:55.520026-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=12844.2790, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=78289, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=12844, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	11:13:55.520060-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=12844, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=78289, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	11:13:55.520720-0500	ControlCenter	[app<application.com.nexy.assistant.53053210.53053219>:78289] Workspace state did change: BG-Active[40] --> XX-None[0] (assertion dropped).
default	11:13:55.520900-0500	runningboardd	Invalidating assertion 394-626-35011 (target:[app<application.com.nexy.assistant.53053210.53053219(501)>:78289]) from originator [osservice<com.apple.controlcenter(501)>:626]
default	11:13:55.521858-0500	tccd	AUTHREQ_SUBJECT: msgID=12844.2790, subject=com.nexy.assistant,
default	11:13:55.523261-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb2ed5ed00 at /Applications/Nexy.app
default	11:13:55.553802-0500	Nexy	[0x717abb200] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	11:13:55.553891-0500	Nexy	[0x717abb200] activating connection: mach=false listener=false peer=false name=(anonymous)
default	11:13:55.553956-0500	Nexy	[0x717abb340] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	11:13:55.554824-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=12844.2791, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=78289, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=12844, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	11:13:55.554861-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=12844, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=78289, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	11:13:55.556142-0500	tccd	AUTHREQ_SUBJECT: msgID=12844.2791, subject=com.nexy.assistant,
default	11:13:55.556857-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb2ed5ed00 at /Applications/Nexy.app
default	11:13:55.578696-0500	Nexy	[0x717abb340] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	11:13:55.578749-0500	Nexy	[0x717abb480] activating connection: mach=false listener=false peer=false name=(anonymous)
default	11:13:55.578851-0500	Nexy	[0x717abb340] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	11:13:55.581255-0500	tccd	AUTHREQ_SUBJECT: msgID=12844.2792, subject=com.nexy.assistant,
default	11:13:55.582108-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb2ed5ed00 at /Applications/Nexy.app
default	11:13:55.605149-0500	Nexy	[0x717abb340] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	11:13:55.605247-0500	Nexy	[0x717abb340] activating connection: mach=false listener=false peer=false name=(anonymous)
default	11:13:55.605372-0500	Nexy	[0x717abb5c0] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	11:13:55.607441-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=12844.2793, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=78289, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=12844, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	11:13:55.607489-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=12844, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=78289, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	11:13:55.609039-0500	tccd	AUTHREQ_SUBJECT: msgID=12844.2793, subject=com.nexy.assistant,
default	11:13:55.610081-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb2ed5ed00 at /Applications/Nexy.app
default	11:13:55.626935-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78289] Ignoring jetsam update because this process is not memory-managed
default	11:13:55.626952-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78289] Ignoring suspend because this process is not lifecycle managed
default	11:13:55.626965-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78289] Ignoring GPU update because this process is not GPU managed
default	11:13:55.626991-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78289] Ignoring memory limit update because this process is not memory-managed
default	11:13:55.634185-0500	Nexy	[0x717abb5c0] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	11:13:55.634246-0500	Nexy	[0x717abb700] activating connection: mach=false listener=false peer=false name=(anonymous)
default	11:13:55.641031-0500	Nexy	Did add XPC store
default	11:13:55.641062-0500	Nexy	Did add prepared store without migration (path: file:///Users/sergiyzasorin/Library/Application%20Support/AddressBook/AddressBook-v22.abcddb)
default	11:13:55.651246-0500	Nexy	Client change history token is invalid: <private>, current token: <private>, error: Error Domain=NSCocoaErrorDomain Code=134501 UserInfo={NSLocalizedFailureReason=<private>}
error	11:13:55.651567-0500	Nexy	Failed to fetch change history: Error Domain=CNErrorDomain Code=1006 "Full Sync Required" UserInfo={NSLocalizedFailureReason=A full sync is required., NSLocalizedDescription=Full Sync Required, NSUnderlyingError=0x712e10090 {Error Domain=CNErrorDomain Code=604 "Invalid Change History Anchor" UserInfo={NSLocalizedDescription=Invalid Change History Anchor, NSLocalizedFailureReason=The change history anchor is invalid.}}}
default	11:13:55.651822-0500	Nexy	0000 BEGIN: Will execute fetch for request: <private>
default	11:13:55.651835-0500	Nexy	0000 Entry point: executeFetchRequest:error:
default	11:13:55.651849-0500	Nexy	0000 Predicate: (null) <private>
default	11:13:55.665698-0500	Nexy	App is linked against Fall 2022 SDK or later
default	11:13:55.665721-0500	Nexy	Note access is not granted, so Notes are inaccessible
fault	11:13:55.665852-0500	Nexy	Attempt to read notes by an unentitled app
default	11:13:55.681230-0500	Nexy	0000 History anchor returned to client: <CNChangeHistoryAnchor: 0x714db6da0: version=2, token=<NSPersistentHistoryToken - {
    "121C6BBC-8A11-4E34-B252-321D0995C010" = 6;
    "CE445509-54F5-473C-9A96-89025D6F9355" = 4701;
}>>
default	11:13:55.681391-0500	Nexy	0000 Contact: 3EE990C2-437C-497A-B4CF-4787E78B5D0C:ABPerson
default	11:13:55.681410-0500	Nexy	0000 Contact: 2645688D-4F81-4C23-847F-96DEA47CCE6D:ABPerson
default	11:13:55.681418-0500	Nexy	0000 Contact: C822EB31-1F0F-41F6-9120-A322A5874983:ABPerson
default	11:13:55.681427-0500	Nexy	0000 Contact: 50AD2AD1-9340-4D1D-8702-DB033FCB2397:ABPerson
default	11:13:55.681436-0500	Nexy	0000 Contact: EDB979D3-287A-47DC-BC6D-006167336515:ABPerson
default	11:13:55.681443-0500	Nexy	0000 Contact: 9595A838-850C-49DB-8998-80F19667F619:ABPerson
default	11:13:55.681452-0500	Nexy	0000 Contact: 9891AB4D-DDC3-49D3-8FAA-45BFB1995A79:ABPerson
default	11:13:55.681459-0500	Nexy	0000 Contact: 34B7C886-745F-477F-BAF4-C6494310C1C1:ABPerson
default	11:13:55.681478-0500	Nexy	0000 Contact: 3426C1A4-CACA-42EF-8793-7312DCEE5E69:ABPerson
default	11:13:55.681488-0500	Nexy	0000 Contact: AFFBAE3D-BA02-4D6F-AE25-87E55C2E4CD9:ABPerson
default	11:13:55.681498-0500	Nexy	0000 Contact: 55C7A0C2-9163-43BC-95A9-A92E4F5427BD:ABPerson
default	11:13:55.681513-0500	Nexy	0000 Contact: CBAABC59-9B06-47EE-9311-0823CE3EE179:ABPerson
default	11:13:55.681520-0500	Nexy	0000 Contact: FF2BD9DD-8A6D-4E97-BB7D-7B1A5C4FAC0F:ABPerson
default	11:13:55.681530-0500	Nexy	0000 Contact: F6E944AE-3E32-4C0C-BA60-EE94D9402DA7:ABPerson
default	11:13:55.681555-0500	Nexy	0000 Contact: 0E222C4B-C87D-403F-A824-B8B8EAABF29D:ABPerson
default	11:13:55.681566-0500	Nexy	0000 Contact: 160B58EE-E9AF-4BBE-B484-7D4E18CA0CD4:ABPerson
default	11:13:55.681576-0500	Nexy	0000 Contact: D6931A27-6BBA-4ABF-AB86-AA94288C8731:ABPerson
default	11:13:55.681592-0500	Nexy	0000 Contact: 04E7F59A-3D30-4CF9-8395-AE8737EE1154:ABPerson
default	11:13:55.681612-0500	Nexy	0000 Contact: 863252FB-26EB-421B-9B96-91673ED81D35:ABPerson
default	11:13:55.681622-0500	Nexy	0000 Contact: 742C7DAC-D2A9-4D1C-A93D-DC71F37722B9:ABPerson
default	11:13:55.681637-0500	Nexy	0000 Contact: 99649BEC-0C02-4588-9CCA-09103FDC430C:ABPerson
default	11:13:55.681646-0500	Nexy	0000 Contact: 8898FA76-8C7B-4917-B353-30B4A337A32B:ABPerson
default	11:13:55.681655-0500	Nexy	0000 Contact: 75C5C7DD-DD9E-437F-91B9-34AFD56C5A14:ABPerson
default	11:13:55.681670-0500	Nexy	0000 Contact: DDC41FDC-94BF-4147-9863-5AFCC485C4BA:ABPerson
default	11:13:55.681679-0500	Nexy	0000 Contact: B6D0B979-BBDF-4FF5-93A8-0974C5AE45C7:ABPerson
default	11:13:55.681687-0500	Nexy	0000 Contact: B7A8ADD0-A952-45B0-B7A2-D15A3D34A898:ABPerson
default	11:13:55.681706-0500	Nexy	0000 Contact: 35894E4A-BF98-44E4-85B9-33C2A0A01944:ABPerson
default	11:13:55.681718-0500	Nexy	0000 Contact: 67B532BB-C394-4D14-B2E6-C1B93DE930E4:ABPerson
default	11:13:55.681725-0500	Nexy	0000 Contact: A71518ED-EC1D-4740-9D8C-2C5F81C71467:ABPerson
default	11:13:55.681732-0500	Nexy	0000 Contact: EE1E04AC-AF03-428A-97EF-6E8851A86066:ABPerson
default	11:13:55.681740-0500	Nexy	0000 Contact: 54E381BF-247A-4AB7-81FD-8C78CBB93296:ABPerson
default	11:13:55.681756-0500	Nexy	0000 Contact: A5DB19AB-C77E-44EC-87A4-8459DA494E7B:ABPerson
default	11:13:55.681763-0500	Nexy	0000 Contact: FC26680D-B85F-4E40-812F-4F169185AE50:ABPerson
default	11:13:55.681771-0500	Nexy	0000 Contact: E36EA0A4-41F7-4C3F-AAF9-A93099626D77:ABPerson
default	11:13:55.681787-0500	Nexy	0000 Contact: 37E2B276-263E-40A5-BF81-1628796DB605:ABPerson
default	11:13:55.681798-0500	Nexy	0000 Contact: D989E37A-D5DC-4A68-8D47-AD8FEE0B37BA:ABPerson
default	11:13:55.681806-0500	Nexy	0000 Contact: 204F2E81-2324-4937-9859-E8732482C902:ABPerson
default	11:13:55.681813-0500	Nexy	0000 Contact: C4831F25-FE6F-4217-92D2-C4D6C01013BC:ABPerson
default	11:13:55.681824-0500	Nexy	0000 Contact: 4FD77C47-1199-46DF-B186-25C3BB8E54C4:ABPerson
default	11:13:55.681833-0500	Nexy	0000 Contact: 16FA5BBF-AADB-4362-83EB-09668C0C6A84:ABPerson
default	11:13:55.681848-0500	Nexy	0000 Contact: D9A061DB-8A77-472E-A6B3-AF6A4A6727A9:ABPerson
default	11:13:55.681859-0500	Nexy	0000 Contact: 62AC02AD-E5FE-4F18-8DEB-151D2FFD50D2:ABPerson
default	11:13:55.681890-0500	Nexy	0000 Contact: 9D4856E4-4610-4169-9460-115522478752:ABPerson
default	11:13:55.681902-0500	Nexy	0000 Contact: 8038DF9A-4503-4464-BA80-1A8B28F523E6:ABPerson
default	11:13:55.681910-0500	Nexy	0000 Contact: DE31B769-37E8-406B-BC5C-FC44F37A37D1:ABPerson
default	11:13:55.681920-0500	Nexy	0000 Contact: B2E8FADF-3954-4D05-B047-C43474BF8E54:ABPerson
default	11:13:55.681936-0500	Nexy	0000 Contact: 5C30DD83-8C53-4FB6-943A-DF0CED6109D6:ABPerson
default	11:13:55.681946-0500	Nexy	0000 Contact: 16A1EC92-AB39-4C1E-8E16-706B5F47397C:ABPerson
default	11:13:55.681976-0500	Nexy	0000 Contact: 36994EED-FC81-46EF-86F8-8B3217234A98:ABPerson
default	11:13:55.681984-0500	Nexy	0000 Contact: D0D31CD7-6F0F-4030-A30D-197CE5187EED:ABPerson
default	11:13:55.682007-0500	Nexy	0000 Contact: F5676762-711F-4325-8A7A-FCB211127327:ABPerson
default	11:13:55.682017-0500	Nexy	0000 Contact: 99378C4C-7187-4A49-A938-AF1E4D9750E9:ABPerson
default	11:13:55.682024-0500	Nexy	0000 Contact: FE93F61D-6DD6-4CF7-9D17-F972815C60EB:ABPerson
default	11:13:55.682041-0500	Nexy	0000 Contact: E7CCA41A-8A2E-4351-852A-A5CFB6BD2AF5:ABPerson
default	11:13:55.682065-0500	Nexy	0000 Contact: EC41AC6A-1CB5-41D5-B70A-D7D261B5F6B3:ABPerson
default	11:13:55.682075-0500	Nexy	0000 Contact: 2A13AE99-82FE-4A26-A768-1B8C4A11C6C3:ABPerson
default	11:13:55.682096-0500	Nexy	0000 Contact: D5B5277E-F18A-48C2-B93C-E578CEB16C34:ABPerson
default	11:13:55.682121-0500	Nexy	0000 Contact: 1148E024-6D8F-4279-921E-7936B62EB2B8:ABPerson
default	11:13:55.682132-0500	Nexy	0000 Contact: FAF205FC-E995-4261-90F7-336A4D237F48:ABPerson
default	11:13:55.682142-0500	Nexy	0000 Contact: 88E161CA-F779-4608-BE32-D15726C295C6:ABPerson
default	11:13:55.682149-0500	Nexy	0000 Contact: BE244260-8495-47EA-9EFA-A4A129388623:ABPerson
default	11:13:55.682167-0500	Nexy	0000 Contact: FC34E363-0467-4B9C-95B0-F8C585C41741:ABPerson
default	11:13:55.682176-0500	Nexy	0000 Contact: F244F65D-0A57-4A3C-B8B8-9E1C389A5E77:ABPerson
default	11:13:55.682183-0500	Nexy	0000 Contact: 9DE56935-FB3E-470E-9878-89DB593E2DFE:ABPerson
default	11:13:55.682199-0500	Nexy	0000 Contact: 51D61586-1A8A-4EC4-8568-45B5296B1751:ABPerson
default	11:13:55.682208-0500	Nexy	0000 Contact: F34A454E-F1D3-4849-9368-950A6FFA8DD1:ABPerson
default	11:13:55.682215-0500	Nexy	0000 Contact: 5E09571D-9D8E-4D12-8480-F04FD91A55C4:ABPerson
default	11:13:55.682234-0500	Nexy	0000 Contact: 997D7D2F-4504-4C65-A31D-535219B806F5:ABPerson
default	11:13:55.682245-0500	Nexy	0000 Contact: F4D5E6E8-6B00-4329-94DC-82661F45DDB5:ABPerson
default	11:13:55.682252-0500	Nexy	0000 Contact: B3F91E16-48C2-4383-BFDA-F39E45D698A9:ABPerson
default	11:13:55.682270-0500	Nexy	0000 Contact: 972B1CC5-A00E-409A-A1C8-1035B67228F2:ABPerson
default	11:13:55.682293-0500	Nexy	0000 Contact: C9342200-2A80-485B-8777-A59F252176D4:ABPerson
default	11:13:55.682331-0500	Nexy	0000 Contact: FCD5548B-6E7B-4B57-9097-496095F0C27B:ABPerson
default	11:13:55.682354-0500	Nexy	0000 Contact: 32E90B79-BC48-4AFC-A5CE-495011FBE68F:ABPerson
default	11:13:55.682365-0500	Nexy	0000 Contact: 799B442D-0C1B-41A7-982A-5A795CF5AC7E:ABPerson
default	11:13:55.682374-0500	Nexy	0000 Contact: 4BC8FD3A-601A-4905-B4F0-AAEE2EA51FFC:ABPerson
default	11:13:55.682384-0500	Nexy	0000 Contact: EB01D8DC-AD35-4332-B52D-021C69F834F5:ABPerson
default	11:13:55.682394-0500	Nexy	0000 Contact: 34439B56-399C-41AE-8A94-926BE1F059E3:ABPerson
default	11:13:55.682401-0500	Nexy	0000 Contact: 5B2AA695-5EAB-4F85-9EA7-0F11FEE7BF7E:ABPerson
default	11:13:55.682411-0500	Nexy	0000 Contact: 680613B6-43E0-4C77-8B2B-0F21D4D6F558:ABPerson
default	11:13:55.682420-0500	Nexy	0000 Contact: FEFADE95-1917-4F12-AF5F-E9AF0F50E039:ABPerson
default	11:13:55.682445-0500	Nexy	0000 Contact: 1CED5FB1-D054-43C6-BF35-E035DFF16C75:ABPerson
default	11:13:55.682455-0500	Nexy	0000 Contact: 4D6A09F3-71D7-4E04-83FD-9BB5EF7442CF:ABPerson
default	11:13:55.682475-0500	Nexy	0000 Contact: 03F9DBA8-764B-4F5E-AFB8-4FE555600768:ABPerson
default	11:13:55.682487-0500	Nexy	0000 Contact: 33E6AEE6-78CC-42D7-80DA-478EDE698964:ABPerson
default	11:13:55.682495-0500	Nexy	0000 Contact: 2B720652-555E-462B-8C74-277B5F6F5F59:ABPerson
default	11:13:55.682516-0500	Nexy	0000 Contact: D8AB7561-7ABC-404E-A1AD-D9765D7DD983:ABPerson
default	11:13:55.682527-0500	Nexy	0000 Contact: 8256DD81-94E0-404F-BE4E-E6831011073C:ABPerson
default	11:13:55.682543-0500	Nexy	0000 Contact: 260C090E-52D7-4D15-AE22-6804C72C9DBF:ABPerson
default	11:13:55.682552-0500	Nexy	0000 Contact: F5703214-DEA8-429F-ADBF-5465A9AFE1BC:ABPerson
default	11:13:55.682559-0500	Nexy	0000 Contact: 1FBE32BC-B2F2-4B98-8BA8-04A4E25A4F0E:ABPerson
default	11:13:55.682575-0500	Nexy	0000 Contact: 2285EC2D-05CF-42C3-8C59-C4930AD792E3:ABPerson
default	11:13:55.682593-0500	Nexy	0000 Contact: 96E50230-0A5E-4B64-A2E9-A2F57018F4EA:ABPerson
default	11:13:55.682601-0500	Nexy	0000 Contact: 1D80A41C-48FF-40D8-A1F7-EB1FCAF019EC:ABPerson
default	11:13:55.682621-0500	Nexy	0000 Contact: 3C49D81F-04DC-4318-93D4-B25373EDFE30:ABPerson
default	11:13:55.682647-0500	Nexy	0000 Contact: 5B4B2182-FBEA-48F0-B9C7-742552BF6CF6:ABPerson
default	11:13:55.682707-0500	Nexy	0000 Contact: 697396C6-6DF5-4A8D-BBC1-7CFB8C26B531:ABPerson
default	11:13:55.682719-0500	Nexy	0000 Contact: BC83C14B-9BF3-4E6D-A5BD-1252B3AF3A72:ABPerson
default	11:13:55.682729-0500	Nexy	0000 Contact: 29B138C5-7412-4C36-A514-72D80434AC26:ABPerson
default	11:13:55.682735-0500	Nexy	0000 Contact: 93438337-7E2C-4A3D-99F8-28AECEE7A491:ABPerson
default	11:13:55.682770-0500	Nexy	0000 Contact: BEEDDC1A-71AD-4FBD-9241-9F6B4669022C:ABPerson
default	11:13:55.682782-0500	Nexy	0000 Contact: 516FCDD2-D694-4336-9C5C-B3F9398876E3:ABPerson
default	11:13:55.682790-0500	Nexy	0000 Contact: CB798F66-5E15-419F-8CB1-A22A10034846:ABPerson
default	11:13:55.682797-0500	Nexy	0000 Contact: 9BE2908B-57F8-42EB-85AB-E556B53D5008:ABPerson
default	11:13:55.682812-0500	Nexy	0000 Contact: 74E5D1E4-D560-47F5-800D-2B15C8F128ED:ABPerson
default	11:13:55.682821-0500	Nexy	0000 Contact: 73FA4D96-88CD-4E81-B755-D3C151251CB2:ABPerson
default	11:13:55.682838-0500	Nexy	0000 Contact: A159EB30-CDD4-4876-B3EB-7A251E5003A1:ABPerson
default	11:13:55.682847-0500	Nexy	0000 Contact: 2E020885-F8C2-47BB-AEE3-DD7CF66B13B4:ABPerson
default	11:13:55.682873-0500	Nexy	0000 Contact: 05A17C92-D301-4B09-A90C-D64806C4CA53:ABPerson
default	11:13:55.682883-0500	Nexy	0000 Contact: AD733A8E-1D66-4608-811D-8B3CC382D864:ABPerson
default	11:13:55.682892-0500	Nexy	0000 Contact: E567A65A-A157-4ABD-B1FD-82CC549DEDED:ABPerson
default	11:13:55.682909-0500	Nexy	0000 Contact: 7F0336C8-01E0-47A7-A79A-9400EBF86D9C:ABPerson
default	11:13:55.682924-0500	Nexy	0000 Contact: 46F95F55-6525-42E6-A4B3-332AB9ECB6C9:ABPerson
default	11:13:55.682965-0500	Nexy	0000 Contact: 0BF7B2D3-D0E4-4CF5-A2E5-BBAB2F74860F:ABPerson
default	11:13:55.682976-0500	Nexy	0000 Contact: 889A4ED3-ACDE-4D87-9718-586CF8A5A3CC:ABPerson
default	11:13:55.682986-0500	Nexy	0000 Contact: DF05522B-2972-4CAB-8C0F-9FDECE2E3D80:ABPerson
default	11:13:55.683001-0500	Nexy	0000 Contact: 32C28665-F08E-4EE8-AFEB-487908D24319:ABPerson
default	11:13:55.683011-0500	Nexy	0000 Contact: 23512481-0DEF-42CA-8985-3D92A24DC0D9:ABPerson
default	11:13:55.683027-0500	Nexy	0000 Contact: C799BC2E-8783-42B8-BE80-6B9329212F7F:ABPerson
default	11:13:55.683036-0500	Nexy	0000 Contact: AF84B174-40F6-4E9C-A51A-D3FACA6CD75E:ABPerson
default	11:13:55.683043-0500	Nexy	0000 Contact: D41F250E-DF7F-4F9C-9D25-DC402CAC6533:ABPerson
default	11:13:55.683058-0500	Nexy	0000 Contact: E5E58063-920E-46E6-8939-C1A7ACCF23F0:ABPerson
default	11:13:55.683067-0500	Nexy	0000 Contact: F48B9D39-03E0-45D0-AA05-14488FC68C6F:ABPerson
default	11:13:55.683080-0500	Nexy	0000 Contact: B599DEB9-C4DF-472F-9B9E-67C3935077CD:ABPerson
default	11:13:55.683089-0500	Nexy	0000 Contact: CD1D19AA-FC19-4C03-9DC9-C147E8C245D1:ABPerson
default	11:13:55.683096-0500	Nexy	0000 Contact: 4F833F31-870E-4630-825C-0F532CBA3D39:ABPerson
default	11:13:55.683115-0500	Nexy	0000 Contact: BD409DD5-797E-41A8-B955-2CC4520A8769:ABPerson
default	11:13:55.683125-0500	Nexy	0000 Contact: 8A88B309-DB9A-4B6A-B1D9-CD6910D5845B:ABPerson
default	11:13:55.683147-0500	Nexy	0000 Contact: 18BDFAAD-5A5F-42D6-890A-2C5AEA9201D4:ABPerson
default	11:13:55.683156-0500	Nexy	0000 Contact: 96309E07-28A0-4C3F-8B27-7224031FF6EB:ABPerson
default	11:13:55.683173-0500	Nexy	0000 Contact: BF324B31-1F91-4723-87BC-8FE02890D85F:ABPerson
default	11:13:55.683182-0500	Nexy	0000 Contact: A0DA1AD3-5F0A-4625-8A45-AEE2662B5DF7:ABPerson
default	11:13:55.683209-0500	Nexy	0000 Contact: 76DEED21-9E22-4327-83F8-C1C1DDF67DEE:ABPerson
default	11:13:55.683223-0500	Nexy	0000 Contact: 7C25BC81-A7AB-4059-A199-45F36EBE02EB:ABPerson
default	11:13:55.683233-0500	Nexy	0000 Contact: 919E5AE9-2160-41DC-8E41-9C2536932C86:ABPerson
default	11:13:55.683248-0500	Nexy	0000 Contact: 8FC46F73-8C76-4F4F-A480-86AD43FB3197:ABPerson
default	11:13:55.683257-0500	Nexy	0000 Contact: 758B39F6-7626-4392-A342-2F56B6D94427:ABPerson
default	11:13:55.683270-0500	Nexy	0000 Contact: 8A6084C7-9664-4FCF-BD0E-DF7B4AE169BC:ABPerson
default	11:13:55.683279-0500	Nexy	0000 Contact: 51857A1F-41AD-4ABC-BC2E-82377C39162B:ABPerson
default	11:13:55.683291-0500	Nexy	0000 Contact: 0145E52B-5388-4DF4-9BA6-041E2688EA53:ABPerson
default	11:13:55.683303-0500	Nexy	0000 Contact: 7C58562E-BF30-4BE5-AC33-E0A88F42AB76:ABPerson
default	11:13:55.683310-0500	Nexy	0000 Contact: C7C8564C-DF73-4360-B286-BB2CF4C72F17:ABPerson
default	11:13:55.683332-0500	Nexy	0000 Contact: F9EE7585-B534-46B5-848E-58FFD7152121:ABPerson
default	11:13:55.683342-0500	Nexy	0000 Contact: DABCF335-B625-47DD-918B-704381FD587D:ABPerson
default	11:13:55.683350-0500	Nexy	0000 Contact: A68807CD-0A21-4F90-BE39-09BAF83835E8:ABPerson
default	11:13:55.683360-0500	Nexy	0000 Contact: 3B7F983F-D8F3-400C-8462-CA84B84968A4:ABPerson
default	11:13:55.683377-0500	Nexy	0000 Contact: BE53EA52-E9F8-4C18-8446-4FA2489ADE02:ABPerson
default	11:13:55.683386-0500	Nexy	0000 Contact: A804F4AE-3921-4E55-83D8-094B7C4F17A3:ABPerson
default	11:13:55.683393-0500	Nexy	0000 Contact: 489A6364-6AEC-4FC5-8F52-FC08E5527BA0:ABPerson
default	11:13:55.683403-0500	Nexy	0000 Contact: B43BC68C-E9BB-48C1-98C3-A32A09C9A802:ABPerson
default	11:13:55.683410-0500	Nexy	0000 Contact: 05518C4D-4F67-4CD6-83D7-85AA7F2525A5:ABPerson
default	11:13:55.683423-0500	Nexy	0000 Contact: 955CE160-9CC8-4013-829C-A68FD99C7595:ABPerson
default	11:13:55.683433-0500	Nexy	0000 Contact: C13FF96F-DEF6-4C53-83DE-4B45963DD9AF:ABPerson
default	11:13:55.683449-0500	Nexy	0000 Contact: AE65B570-135A-4B14-BA64-EC538224DA56:ABPerson
default	11:13:55.683458-0500	Nexy	0000 Contact: C2132A98-A61A-4358-A681-AF1A1DA20915:ABPerson
default	11:13:55.683465-0500	Nexy	0000 Contact: C3CC1CBC-2410-4DA6-A83E-0477D239E755:ABPerson
default	11:13:55.683479-0500	Nexy	0000 Contact: 0FB60F1D-91EC-4396-A66A-69F15AF14BC5:ABPerson
default	11:13:55.683487-0500	Nexy	0000 Contact: FC6CD704-B936-454E-9EBD-E1701A5DE7D8:ABPerson
default	11:13:55.683501-0500	Nexy	0000 Contact: ED88C6F4-1641-473F-A5BC-DA8C11FCE9D2:ABPerson
default	11:13:55.683509-0500	Nexy	0000 Contact: 88083F13-CF73-4821-896D-8C9EDB5E9029:ABPerson
default	11:13:55.683516-0500	Nexy	0000 Contact: C5BAA4A8-B489-4A59-9400-5C0DFDAA91CA:ABPerson
default	11:13:55.683535-0500	Nexy	0000 Contact: F0187322-8BFE-4EE7-BA9E-BF7D7A056616:ABPerson
default	11:13:55.683542-0500	Nexy	0000 Contact: BA26FE3B-CB6A-471A-8E10-5000CF5332C2:ABPerson
default	11:13:55.683551-0500	Nexy	0000 Contact: DB250DFB-C87D-447B-B125-220B6E3DA663:ABPerson
default	11:13:55.683557-0500	Nexy	0000 Contact: B436BB91-BBBB-49E7-9C6A-93DDDD421478:ABPerson
default	11:13:55.683573-0500	Nexy	0000 Contact: DFCC4D11-6BC3-4ACD-B8C6-F8C46F7C8369:ABPerson
default	11:13:55.683588-0500	Nexy	0000 Contact: 0B435818-E34A-41BF-8808-417BCB956E97:ABPerson
default	11:13:55.683597-0500	Nexy	0000 Contact: E336CBFC-CF06-4672-BEF7-926884FB9BC8:ABPerson
default	11:13:55.683665-0500	Nexy	0000 Contact: A04F02F1-D5E5-4B3E-B5D0-287A46E6DB37:ABPerson
default	11:13:55.683674-0500	Nexy	0000 Contact: 274D78AE-37CF-4B30-B57D-D218F7D433BC:ABPerson
default	11:13:55.683690-0500	Nexy	0000 Contact: AFC75DDF-9D56-451F-8FFA-33CEF512BC9E:ABPerson
default	11:13:55.683703-0500	Nexy	0000 Contact: 36B84A8B-DD90-4609-9407-3BED73397C90:ABPerson
default	11:13:55.683712-0500	Nexy	0000 Contact: 25B2E948-39F0-4DA0-984A-6EAAFC4452BF:ABPerson
default	11:13:55.683722-0500	Nexy	0000 Contact: FD3874CC-9147-45D7-9635-BA7057F1E4CE:ABPerson
default	11:13:55.683731-0500	Nexy	0000 Contact: 93C427E1-DE52-48BF-AFC1-082EC9E9EDA0:ABPerson
default	11:13:55.683737-0500	Nexy	0000 Contact: 0ADD2D08-B0E0-4789-8BA5-3036146B6B78:ABPerson
default	11:13:55.683746-0500	Nexy	0000 Contact: C1626763-A8D5-4907-A0D9-325529F3E7B5:ABPerson
default	11:13:55.683753-0500	Nexy	0000 Contact: A691F96E-80C3-406D-A1F3-443C491D30D0:ABPerson
default	11:13:55.683760-0500	Nexy	0000 Contact: 331AE8C5-F99D-4F0A-B33F-36D558A607C3:ABPerson
default	11:13:55.683768-0500	Nexy	0000 Contact: 5C041266-AB76-41D1-BBBA-5FE4A4792084:ABPerson
default	11:13:55.683775-0500	Nexy	0000 Contact: F3BDC31E-20AF-4198-B696-F389C8F31C9F:ABPerson
default	11:13:55.683784-0500	Nexy	0000 Contact: 0CC4651C-3FC4-4644-BAB9-41107FBFF900:ABPerson
default	11:13:55.683792-0500	Nexy	0000 Contact: 9C0BE147-A58C-44D2-9C4A-FC7DFE653F3E:ABPerson
default	11:13:55.683799-0500	Nexy	0000 Contact: 0C5D18DF-0E63-4D12-AB19-70F9449BFDD3:ABPerson
default	11:13:55.683806-0500	Nexy	0000 Contact: 1EB1F958-3A33-4C17-AEFC-E59EA17F5D5B:ABPerson
default	11:13:55.683815-0500	Nexy	0000 Contact: E9510B2D-16FE-4F94-BBBE-BFACDEEF0759:ABPerson
default	11:13:55.683823-0500	Nexy	0000 Contact: 5D99F42B-5A12-4DD2-9DA9-063C524A30C7:ABPerson
default	11:13:55.683830-0500	Nexy	0000 Contact: 7C44FDAA-3756-43F4-B87F-DDA61E480B1C:ABPerson
default	11:13:55.683836-0500	Nexy	0000 Contact: DFDA976C-6D05-4677-AAA2-604A3688988F:ABPerson
default	11:13:55.683844-0500	Nexy	0000 Contact: 91B8C6A6-858C-4158-B742-E97BCFF7F054:ABPerson
default	11:13:55.683856-0500	Nexy	0000 Contact: 2A16F554-F4B5-4D1A-84FF-1B1B9CD41A6F:ABPerson
default	11:13:55.683866-0500	Nexy	0000 Contact: 51FDBD11-7239-4140-9605-7B2CFF1426E4:ABPerson
default	11:13:55.683872-0500	Nexy	0000 Contact: 2F813EA9-9EFC-409F-A1C4-64F820E4D179:ABPerson
default	11:13:55.683881-0500	Nexy	0000 Contact: 6B7D950D-D374-429D-91CE-A6E1B5D41AAA:ABPerson
default	11:13:55.683890-0500	Nexy	0000 Contact: F7679D0A-6363-40EC-A12A-63E9F2C28321:ABPerson
default	11:13:55.683904-0500	Nexy	0000 Contact: 6703F826-C4D7-43ED-83B5-77B3CBF74E39:ABPerson
default	11:13:55.683912-0500	Nexy	0000 Contact: ED036238-8F1A-4104-98CA-4C44E9BC5990:ABPerson
default	11:13:55.683919-0500	Nexy	0000 Contact: 00F2C374-C9A3-4DD0-B92B-E70CEFC1C968:ABPerson
default	11:13:55.683933-0500	Nexy	0000 Contact: E984A144-E505-46AA-AA38-1CF1EE5DF265:ABPerson
default	11:13:55.683942-0500	Nexy	0000 Contact: 444D762E-7CC5-479E-B3C7-D5172CE8F56B:ABPerson
default	11:13:55.683959-0500	Nexy	0000 Contact: D7D2F3A4-5125-4F75-8CA2-19A18318ABBB:ABPerson
default	11:13:55.683968-0500	Nexy	0000 Contact: AA3A68CB-8A4B-4BAD-94D4-F0B1FDEF6AD2:ABPerson
default	11:13:55.683976-0500	Nexy	0000 Contact: B729AB23-719C-4993-99D4-97F17990CA6E:ABPerson
default	11:13:55.683984-0500	Nexy	0000 Contact: DDD6C0A5-9D08-4756-BB6E-06612386E694:ABPerson
default	11:13:55.684000-0500	Nexy	0000 Contact: DAA81742-1BAC-4E0A-86AB-1805922F5BFB:ABPerson
default	11:13:55.684007-0500	Nexy	0000 Contact: CCCE8074-7CFC-4765-87C4-3DA3398ED5E3:ABPerson
default	11:13:55.684016-0500	Nexy	0000 Contact: B3126A39-DB1F-4EB9-BA9E-057A701FEADB:ABPerson
default	11:13:55.684025-0500	Nexy	0000 Contact: D7A6F43C-FFAB-4219-B325-4345A3EBA5B5:ABPerson
default	11:13:55.684041-0500	Nexy	0000 Contact: F3959633-1472-4370-AE25-6C163A86F28A:ABPerson
default	11:13:55.684051-0500	Nexy	0000 Contact: 818A8D3F-5A2E-44CA-B4CF-47B295DB8C98:ABPerson
default	11:13:55.684060-0500	Nexy	0000 Contact: 228410FA-14BD-488B-A385-35C7112B9635:ABPerson
default	11:13:55.684067-0500	Nexy	0000 Contact: 1A2FDBB3-F370-4D0F-8C9A-34D9C191D7E3:ABPerson
default	11:13:55.684082-0500	Nexy	0000 Contact: 5FDB4463-1088-4EF5-9E20-48795D669908:ABPerson
default	11:13:55.684092-0500	Nexy	0000 Contact: 241E5174-F04C-45D2-BB1E-C4295A53CA80:ABPerson
default	11:13:55.684101-0500	Nexy	0000 Contact: 135FEF8F-5A69-49C6-97E1-E218FAD43A7E:ABPerson
default	11:13:55.684114-0500	Nexy	0000 Contact: F7BF6E9A-A1DE-4F0A-B9FE-DD0E61EBC464:ABPerson
default	11:13:55.684144-0500	Nexy	0000 Contact: F4DA25ED-6C3C-44D5-8A9B-87F14829E713:ABPerson
default	11:13:55.684160-0500	Nexy	0000 Contact: 95FF7EB7-87CC-416D-8811-B8DCC6FE7621:ABPerson
default	11:13:55.684170-0500	Nexy	0000 Contact: 751FAE5C-98A6-414E-B107-317AF0CBED37:ABPerson
default	11:13:55.684184-0500	Nexy	0000 Contact: 5465ECDD-A832-402B-BB73-FDF36810C6E0:ABPerson
default	11:13:55.684192-0500	Nexy	0000 Contact: 52FD2EC7-BEF6-4D05-BCAC-73FBAA131CDF:ABPerson
default	11:13:55.684210-0500	Nexy	0000 Contact: 9D848D63-FDF8-461C-9756-F8AAC3070EFF:ABPerson
default	11:13:55.684220-0500	Nexy	0000 Contact: D6BF6AC9-65CA-41BE-AFA2-C3071A2539F5:ABPerson
default	11:13:55.684230-0500	Nexy	0000 Contact: 4E4C0E62-3EE9-4F23-A226-025907D6882D:ABPerson
default	11:13:55.684238-0500	Nexy	0000 Contact: 1006869C-954C-4394-BFE9-09E9CE09AFB5:ABPerson
default	11:13:55.684256-0500	Nexy	0000 Contact: 339B0201-420C-414B-96CB-1D8150AEF6BB:ABPerson
default	11:13:55.684273-0500	Nexy	0000 Contact: 6A713058-BCB2-4635-BC21-577F0261940C:ABPerson
default	11:13:55.684292-0500	Nexy	0000 Contact: 8B61AAC1-DF6F-440A-B5AC-33331AF930E1:ABPerson
default	11:13:55.684300-0500	Nexy	0000 Contact: B5C0C11D-6F8A-4CCE-872A-DEC086F666A6:ABPerson
default	11:13:55.684329-0500	Nexy	0000 Contact: D17EDFE8-D58A-41FF-B738-D480ED1B54BB:ABPerson
default	11:13:55.684351-0500	Nexy	0000 Contact: 8D969F0D-4878-45C3-A329-14C8F1B9A1C4:ABPerson
default	11:13:55.684370-0500	Nexy	0000 Contact: 4DC763F6-4288-4A25-AE37-52DAC0E54434:ABPerson
default	11:13:55.684390-0500	Nexy	0000 Contact: BB62CE57-7037-4156-BE7F-D1E84FA0B46F:ABPerson
default	11:13:55.684400-0500	Nexy	0000 Contact: 32598CF7-ABA5-4AF8-B60C-8B3F9BB79824:ABPerson
default	11:13:55.684434-0500	Nexy	0000 Contact: 4C93D59E-2641-437E-8D5E-6E5135B4B9D7:ABPerson
default	11:13:55.684458-0500	Nexy	0000 Contact: 95C0601A-0362-4E71-9B56-8E66BA6334DB:ABPerson
default	11:13:55.684467-0500	Nexy	0000 Contact: F23EFEDD-DB9E-4EEE-86A8-A0BB0B161DCE:ABPerson
default	11:13:55.684474-0500	Nexy	0000 Contact: A25C8DA8-E066-47BE-A228-BA3A79122649:ABPerson
default	11:13:55.684483-0500	Nexy	0000 Contact: 7709CB5C-F45D-4130-AFCC-F66EB248B381:ABPerson
default	11:13:55.684499-0500	Nexy	0000 Contact: A95901C1-18E2-412B-9429-B9A87D46EEF1:ABPerson
default	11:13:55.684506-0500	Nexy	0000 Contact: 90CCE3F7-7CB8-44CE-8E3B-0E1FEE5B8574:ABPerson
default	11:13:55.684528-0500	Nexy	0000 Contact: D21F44BE-5C0B-49C1-ACBC-50C7FDD0E574:ABPerson
default	11:13:55.684556-0500	Nexy	0000 Contact: 9A341135-6F8F-42C6-A5D8-776E0F0EF424:ABPerson
default	11:13:55.684576-0500	Nexy	0000 Contact: 60C9F9CC-1758-4215-94FA-79E8E5591D0D:ABPerson
default	11:13:55.684595-0500	Nexy	0000 Contact: 7A0D8FED-170A-4F26-B868-532276E4BDF6:ABPerson
default	11:13:55.684602-0500	Nexy	0000 Contact: 791662EB-B4C3-41EA-8207-065A1C9F0AA0:ABPerson
default	11:13:55.684632-0500	Nexy	0000 Contact: D5AB1F03-8C06-438F-8713-DCCBBCD76892:ABPerson
default	11:13:55.684659-0500	Nexy	0000 Contact: 96EC0E50-9CC0-4769-8082-E7C877889553:ABPerson
default	11:13:55.684684-0500	Nexy	0000 Contact: 33394098-1926-4C5F-AA29-7B8610A5C7E6:ABPerson
default	11:13:55.684700-0500	Nexy	0000 Contact: B5956767-6E1D-49F2-8708-69E0D16EC786:ABPerson
default	11:13:55.684720-0500	Nexy	0000 Contact: 918AF5E7-EDE6-400D-A786-261C7B3BC323:ABPerson
default	11:13:55.684729-0500	Nexy	0000 Contact: 78374AF4-D2CF-4636-B824-5922E7BCDAA7:ABPerson
default	11:13:55.684746-0500	Nexy	0000 Contact: E1E5926D-F19D-45D4-9FFE-12E3198D0E67:ABPerson
default	11:13:55.684753-0500	Nexy	0000 Contact: DB957E68-3771-4194-AB47-1B347BE66F63:ABPerson
default	11:13:55.684768-0500	Nexy	0000 Contact: 2112C6EB-840A-49FE-B03E-5DDBFE2F6992:ABPerson
default	11:13:55.684777-0500	Nexy	0000 Contact: 3E8DAA1B-0AD6-465E-BDAB-A68A5FD23D3E:ABPerson
default	11:13:55.684796-0500	Nexy	0000 Contact: 5B8A6BDC-5927-4718-B89F-674DCC70DA16:ABPerson
default	11:13:55.684804-0500	Nexy	0000 Contact: 44BFDAD7-D780-4604-8369-CD3317F7F3FB:ABPerson
default	11:13:55.684813-0500	Nexy	0000 Contact: DD452BC2-AA0F-4E55-9417-30946834E7D9:ABPerson
default	11:13:55.684820-0500	Nexy	0000 Contact: A79E1C58-6726-4518-9160-5833FD1D9E85:ABPerson
default	11:13:55.684839-0500	Nexy	0000 Contact: EEDB6E81-803C-4D9E-9479-23840064FF07:ABPerson
default	11:13:55.684849-0500	Nexy	0000 Contact: E8BAA178-7C7C-4B0C-837F-07B80E6A8155:ABPerson
default	11:13:55.684858-0500	Nexy	0000 Contact: A8C84C99-FF9C-48DF-A603-CEB3050F0BC6:ABPerson
default	11:13:55.684873-0500	Nexy	0000 Contact: 0FD65269-7801-440C-A119-71EBE23C4E70:ABPerson
default	11:13:55.684890-0500	Nexy	0000 Contact: 0A4FEAE5-C426-4926-8B49-A5260D97B9E6:ABPerson
default	11:13:55.684899-0500	Nexy	0000 Contact: CA81313F-6121-4FF6-B60C-EEE869ECF990:ABPerson
default	11:13:55.684931-0500	Nexy	0000 Contact: EA9B96E2-2F87-4EB2-AD12-46F37DFF0EC9:ABPerson
default	11:13:55.684967-0500	Nexy	0000 Contact: 7A89C56B-6D06-419B-A08D-00F14B94AA1C:ABPerson
default	11:13:55.685000-0500	Nexy	0000 Contact: 660A1E96-3CA3-48B5-B94A-96D6D35A72E6:ABPerson
default	11:13:55.685024-0500	Nexy	0000 Contact: 3F5D85F3-9B89-4AD7-A353-FEFEA5DA1C36:ABPerson
default	11:13:55.685034-0500	Nexy	0000 Contact: 8F99EACB-5E71-4F4C-9899-AE7E1FF5280E:ABPerson
default	11:13:55.685060-0500	Nexy	0000 Contact: 9E8B52AD-B9B2-41CA-8134-7861A90F9A02:ABPerson
default	11:13:55.685070-0500	Nexy	0000 Contact: 98237DEC-70B4-4CA5-A4B8-FEE401C3F3C4:ABPerson
default	11:13:55.685079-0500	Nexy	0000 Contact: BD690A56-23D5-4941-B041-50C06351C977:ABPerson
default	11:13:55.685106-0500	Nexy	0000 Contact: D191A589-BA65-49F2-86A3-08D90FB284FD:ABPerson
default	11:13:55.685121-0500	Nexy	0000 Contact: AAF5FE8A-214C-4B65-9B4F-C2578C97C51D:ABPerson
default	11:13:55.685129-0500	Nexy	0000 Contact: 3D737248-8F03-4732-8B3A-8CDA2D45B5AA:ABPerson
default	11:13:55.685152-0500	Nexy	0000 Contact: E120A189-E8F5-4B5F-A2A2-B1A60E6DF145:ABPerson
default	11:13:55.685168-0500	Nexy	0000 Contact: 46187B48-32E0-4B21-B7CE-D3B44766EEEC:ABPerson
default	11:13:55.685197-0500	Nexy	0000 Contact: B72ACD21-62D9-4BC2-8F5A-F33464EEEED5:ABPerson
default	11:13:55.685214-0500	Nexy	0000 Contact: 1D1B1CB1-D316-4BC5-B11C-BC2D4D437605:ABPerson
default	11:13:55.685236-0500	Nexy	0000 Contact: EEC7F987-F555-4025-8B35-10CBE93E26D7:ABPerson
default	11:13:55.685252-0500	Nexy	0000 Contact: A4F96105-C3FC-4D3D-842F-E729A3F28760:ABPerson
default	11:13:55.685262-0500	Nexy	0000 Contact: F0613D78-6887-4B13-AC52-703B5D1A7060:ABPerson
default	11:13:55.685280-0500	Nexy	0000 Contact: BDD5E012-4C2D-4949-9778-80672887C0EC:ABPerson
default	11:13:55.685287-0500	Nexy	0000 Contact: E03CBC1C-C4D5-476B-A9AE-20A246A5FE73:ABPerson
default	11:13:55.685311-0500	Nexy	0000 Contact: A9567605-C983-4D5B-9877-2D3BC5D341CF:ABPerson
default	11:13:55.685336-0500	Nexy	0000 Contact: 378D10F9-7887-44F8-B0A5-9683F2AF012D:ABPerson
default	11:13:55.685343-0500	Nexy	0000 Contact: 29F7EE25-03CA-4DEA-AB4C-5E84B0046094:ABPerson
default	11:13:55.685362-0500	Nexy	0000 Contact: 6045438B-32EF-4240-BCDE-3A83DD6098C1:ABPerson
default	11:13:55.685370-0500	Nexy	0000 Contact: CC00B3CB-4536-414F-8E8F-116901AAAB66:ABPerson
default	11:13:55.685379-0500	Nexy	0000 Contact: CDF1FCD3-669F-4B16-9D7A-07091B53B43E:ABPerson
default	11:13:55.685395-0500	Nexy	0000 Contact: 1C7A8AAA-2853-4C56-892C-93832C406B2F:ABPerson
default	11:13:55.685404-0500	Nexy	0000 Contact: 5FA233B8-A72C-468F-8344-138CB3A320AD:ABPerson
default	11:13:55.685434-0500	Nexy	0000 Contact: CC42A082-921C-4A2F-9B2A-20AD5E63DE26:ABPerson
default	11:13:55.685441-0500	Nexy	0000 Contact: 4D22B39B-A7C9-4F71-B531-0D0A75E819DC:ABPerson
default	11:13:55.685452-0500	Nexy	0000 Contact: 10DA5D0D-F87E-40C2-A2FB-1B4E18ADEED7:ABPerson
default	11:13:55.685468-0500	Nexy	0000 Contact: 1020F64F-877A-46EF-A85B-0B7B4702F30A:ABPerson
default	11:13:55.685477-0500	Nexy	0000 Contact: 7A3258A0-4EF6-4C07-8BAC-DE67AFC5BF0F:ABPerson
default	11:13:55.685493-0500	Nexy	0000 Contact: D8BF88A0-50CD-408B-91AC-FABB6153F0E7:ABPerson
default	11:13:55.685503-0500	Nexy	0000 Contact: F96FB111-3581-4F57-A0DB-8D18E0A5CE3D:ABPerson
default	11:13:55.685511-0500	Nexy	0000 Contact: F8DEA06B-2666-4B7C-AB2B-2D1C7121121A:ABPerson
default	11:13:55.685529-0500	Nexy	0000 Contact: 2DD46A4A-00EA-4AF2-BED6-A0E4704A401E:ABPerson
default	11:13:55.685538-0500	Nexy	0000 Contact: E75A43A8-9126-46AD-BDE0-2F09D8195FCE:ABPerson
default	11:13:55.685545-0500	Nexy	0000 Contact: 0CE70590-2C7E-400D-AAC3-E2AB83B20E6D:ABPerson
default	11:13:55.685554-0500	Nexy	0000 Contact: C93B2BF3-4882-418D-A785-20AABA5900CA:ABPerson
default	11:13:55.685571-0500	Nexy	0000 Contact: 72A79220-BD0A-4F38-A644-7891B8D6D08C:ABPerson
default	11:13:55.685585-0500	Nexy	0000 Contact: 5168F235-33BF-487B-9C88-9A0977EF3D96:ABPerson
default	11:13:55.685604-0500	Nexy	0000 Contact: EF5D8980-C0E4-4FBD-8942-AC7EC9F886BE:ABPerson
default	11:13:55.685612-0500	Nexy	0000 Contact: 8335160D-3EFF-4C7A-B500-08D4AAF9D6C4:ABPerson
default	11:13:55.685626-0500	Nexy	0000 Contact: F30C415E-480E-47D7-A697-2DDF78C62B78:ABPerson
default	11:13:55.685635-0500	Nexy	0000 Contact: 4B86EE6B-7192-4DEC-9A5D-DB2A68A29544:ABPerson
default	11:13:55.685652-0500	Nexy	0000 Contact: 7028A821-E1BB-4996-9F0A-B483955BBD46:ABPerson
default	11:13:55.685661-0500	Nexy	0000 Contact: 7C930844-C857-4F62-B795-A317F57982E7:ABPerson
default	11:13:55.685667-0500	Nexy	0000 Contact: 2958D2B1-193E-4859-97A7-E9D0A6DDAC5B:ABPerson
default	11:13:55.685676-0500	Nexy	0000 Contact: CF7AC9E0-68F2-4C92-A7E7-2F56630F8B8B:ABPerson
default	11:13:55.685683-0500	Nexy	0000 Contact: ADDCC376-3417-4952-A610-3D53B96EC2BD:ABPerson
default	11:13:55.685698-0500	Nexy	0000 Contact: 19855E2F-023D-4999-A9F8-0515B5257D6F:ABPerson
default	11:13:55.685705-0500	Nexy	0000 Contact: 2BAB4AEF-3D51-42E4-BBCA-4587A6EF5B42:ABPerson
default	11:13:55.685714-0500	Nexy	0000 Contact: B68F306A-9F87-4675-9C7C-73ADAC3CF928:ABPerson
default	11:13:55.685725-0500	Nexy	0000 Contact: EBEFEBC5-E9A8-48CB-B48D-DE0E2C3AE2B9:ABPerson
default	11:13:55.685739-0500	Nexy	0000 Contact: C1E29AB3-927E-4614-A170-469712D37DE0:ABPerson
default	11:13:55.685748-0500	Nexy	0000 Contact: 1E18829A-DFA4-4A9A-AEBA-FFF85B2D3E00:ABPerson
default	11:13:55.685762-0500	Nexy	0000 Contact: 41E94FCB-1477-45AF-AB50-6AF7C4651D76:ABPerson
default	11:13:55.685777-0500	Nexy	0000 Contact: 55D05EF1-7380-43F3-9CCC-FCCBB0A382A9:ABPerson
default	11:13:55.685786-0500	Nexy	0000 Contact: 88B8B688-3607-4FD1-BE7E-73F6DAA20674:ABPerson
default	11:13:55.685794-0500	Nexy	0000 Contact: 6A7FA276-678E-44BC-A5CD-1E7AB887CD37:ABPerson
default	11:13:55.685806-0500	Nexy	0000 Contact: A6FD2708-9CD8-45E0-9E88-5BE836285468:ABPerson
default	11:13:55.685817-0500	Nexy	0000 Contact: FFBA4F3C-8FF6-4FC6-9CB6-F62755FFB90C:ABPerson
default	11:13:55.685831-0500	Nexy	0000 Contact: F5A10DB4-BCD8-4342-9435-C976615D2367:ABPerson
default	11:13:55.685838-0500	Nexy	0000 Contact: 1C210F17-EE8F-4513-8100-4877479969F3:ABPerson
default	11:13:55.685847-0500	Nexy	0000 Contact: E6ACEB4F-3D7F-4D37-8463-568D34A3D393:ABPerson
default	11:13:55.733215-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.53053210.53053219(501)>:78289] from originator [osservice<com.apple.WindowServer(88)>:387] with description <RBSAssertionDescriptor| "AppDrawing" ID:394-387-35019 target:78289 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"AppDrawing" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	11:13:55.733306-0500	runningboardd	Assertion 394-387-35019 (target:[app<application.com.nexy.assistant.53053210.53053219(501)>:78289]) will be created as active
default	11:13:56.091042-0500	WindowServer	0[outside of RPC]: Process death: 0x0-0x292292 (Nexy) connectionID: 12324B pid: 78289 in session 0x101
default	11:13:56.091094-0500	WindowServer	<BSCompoundAssertion:0x96f011540> ([FocusManager:257]-deferringPolicyEvaluationSuppression) acquire for reason:process death - 0x0-0x292292 (Nexy) acq:0x96cf23bc0 count:1
default	11:13:56.098659-0500	ControlCenter	[app<application.com.nexy.assistant.53053210.53053219>:78289] Workspace connection invalidated.
default	11:13:56.099167-0500	audiomxd	  ServerSessionManager.mm:478   { "action":"destroy_session", "session":{"ID":"0x1ee028","name":"Nexy(78289)"}, "details":null }
default	11:13:56.098690-0500	ControlCenter	[app<application.com.nexy.assistant.53053210.53053219>:78289] Now flagged as pending exit for reason: workspace client connection invalidated
default	11:13:56.099212-0500	audiomxd	AudioApplicationInfoImpl.mm:690   Successfully removed session 0x1ee028 from AudioApp, recording state unchanged (app: {"name":"[implicit] Nexy","pid":78289})
default	11:13:56.099224-0500	audiomxd	  ServerSessionManager.mm:1086  destroy audio app instance since was created implicitly by session creation and all sessions now gone (audio app: {"name":"[implicit] Nexy","pid":78289})
default	11:13:56.099615-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 41, PID = 78289, Name = sid:0x1ee028, Nexy(78289), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	11:13:56.100435-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	11:13:56.100502-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	11:13:56.098711-0500	WindowManager	Connection invalidated | (78289) Nexy
default	11:13:56.099746-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 41, PID = 78289, Name = sid:0x1ee028, Nexy(78289), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	11:13:56.098350-0500	WindowServer	0[outside of RPC]: [FocusManager:257] update to deferring policy requested for reason: permitted list updated - 0x0-0x292292 removed - but we are suppressing evaluation for reasons: {(
    "process death - 0x0-0x292292 (Nexy)"
)}
default	11:13:56.100127-0500	audiomxd	UpdateAudioState CID 0x45550001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	11:13:56.102195-0500	WindowServer	0[outside of RPC]: [FocusManager:257] update to deferring policy requested for reason: permitted list updated - 0x1-0x131d1 removed - but we are suppressing evaluation for reasons: {(
    "process death - 0x0-0x292292 (Nexy)"
)}
default	11:13:56.100307-0500	audiomxd	UpdateAudioState CID 0x45550001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	11:13:56.111721-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	11:13:56.111948-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	11:13:56.127407-0500	coreaudiod	>>> NEGOTIATE [com.nexy.assistant]
default	11:13:56.127648-0500	coreaudiod	<<< NEGOTIATE [com.nexy.assistant]
default	11:13:56.131055-0500	runningboardd	XPC connection invalidated: [app<application.com.nexy.assistant.53053210.53053219(501)>:78289]
default	11:13:56.135088-0500	coreaudiod	IssueReporting.cpp:492   RTAID [ use_case=Generic report_type=RMS Generic Chain clientID=ADM node=ADM::com.nexy.assistant_2286.2212.0_airpods noise suppression studio::out-0 issue_detected_sample_time=3360.000000 ] -- [ rms:[-120.000000], peaks:[-240.000000] ]
default	11:13:56.135111-0500	coreaudiod	IssueReporting.cpp:492   RTAID [ use_case=Generic report_type=RMS Generic Chain clientID=ADM node=ADM::com.nexy.assistant_2286.2212.0_airpods noise suppression studio::in-0 issue_detected_sample_time=0.000000 ] -- [ rms:[-120.000000], peaks:[-240.000000] ]
default	11:13:56.148364-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78289] termination reported by launchd (0, 0, 0)
default	11:13:56.148426-0500	runningboardd	Removing process: [app<application.com.nexy.assistant.53053210.53053219(501)>:78289]
default	11:13:56.148699-0500	runningboardd	Removing launch job for: [app<application.com.nexy.assistant.53053210.53053219(501)>:78289]
default	11:13:56.149193-0500	runningboardd	Removed job for [app<application.com.nexy.assistant.53053210.53053219(501)>:78289]
default	11:13:56.149262-0500	runningboardd	Removing assertions for terminated process: [app<application.com.nexy.assistant.53053210.53053219(501)>:78289]
default	11:13:56.161118-0500	ControlCenter	[app<application.com.nexy.assistant.53053210.53053219>:78289] Process exited: <RBSProcessExitContext| voluntary>.
default	11:13:56.161140-0500	ControlCenter	[app<application.com.nexy.assistant.53053210.53053219>:78289] Setting process task state to: Not Running
default	11:13:56.161153-0500	ControlCenter	[app<application.com.nexy.assistant.53053210.53053219>:78289] Setting process visibility to: Unknown
default	11:13:56.161211-0500	ControlCenter	[app<application.com.nexy.assistant.53053210.53053219>:78289] Invalidating workspace.
default	11:13:56.161281-0500	ControlCenter	Removing source registration for processHandle: [app<application.com.nexy.assistant.53053210.53053219(501)>:78289]
default	11:13:56.160569-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.53053210.53053219(501)>: none (role: NonUserInteractive) (endowments: (null))
default	11:13:56.162370-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.53053210.53053219(501)>: none (role: NonUserInteractive) (endowments: (null))
default	11:13:56.161849-0500	ControlCenter	Removing: <FBApplicationProcess: 0xb081c7600; app<application.com.nexy.assistant.53053210.53053219>:78289(v91879)>
default	11:13:56.161891-0500	audiomxd	  ServerSessionManager.mm:1327  Monitored process died, pid = 78289, name = Nexy
default	11:13:56.165201-0500	ControlCenter	Stopping tracking for host; (bid:com.nexy.assistant-Item-0-78289)
default	11:13:56.168749-0500	ControlCenter	Removing ephemeral displayable instance DisplayableId(1F2D3E3A) from menu bar. No corresponding host (bid:com.nexy.assistant-Item-0-78289)
default	11:13:56.168951-0500	ControlCenter	Removing displayables [DisplayableAppStatusItem(1F2D3E3A, (bid:com.nexy.assistant-Item-0-78289))]
default	11:13:56.182322-0500	gamepolicyd	Received state update for 78289 (app<application.com.nexy.assistant.53053210.53053219(501)>, none-NotVisible
default	11:13:56.182439-0500	launchservicesd	Hit the server for a process handle 62c4f61000131d1 that resolved to: [app<application.com.nexy.assistant.53053210.53053219(501)>:78289]
default	11:13:56.184753-0500	loginwindow	-[ApplicationManager handleCASEvent:withData:] | CAS notification for appDeath for com.nexy.assistant with asn: LSASN:{hi=0x0;lo=0x292292} for bundle path: /Applications/Nexy.app with URL: file:///Applications/Nexy.app/
default	11:13:56.184788-0500	loginwindow	-[Application setState:] | enter: <Application: 0x8b953cd20: Nexy> state 3
default	11:13:56.184806-0500	loginwindow	-[PersistentAppsSupport applicationQuit:] | for app:Nexy, _appTrackingState = 2
default	11:13:56.188124-0500	loginwindow	-[Application setState:] | enter: <Application: 0x8b953cd20: Nexy> state 4
default	11:13:56.188139-0500	loginwindow	-[PersistentAppsSupport applicationQuit:] | for app:Nexy, _appTrackingState = 2
default	11:13:57.259483-0500	runningboardd	Invalidating assertion 394-626-35008 (target:app<application.com.nexy.assistant.53053210.53053219(501)>) from originator [osservice<com.apple.controlcenter(501)>:626]
default	11:13:57.363605-0500	runningboardd	Removed last relative-start-date-defining assertion for process app<application.com.nexy.assistant.53053210.53053219(501)>
default	11:13:57.368901-0500	gamepolicyd	Received state update for -1 (app<application.com.nexy.assistant.53053210.53053219(501)>, none-NotVisible
default	11:13:59.241733-0500	logger	launching: /usr/bin/open -a /Applications/Nexy.app
default	11:13:59.341658-0500	lsd	com.nexy.assistant/Unknown Persona:5:5:1:1:Building bundle record for app
default	11:13:59.341836-0500	lsd	com.nexy.assistant/Unknown Persona:5:5:2:1:Built bundle record for app
default	11:13:59.344449-0500	lsd	com.nexy.assistant/Unknown Persona:5:4:2:1:_LSServerRegisterItemInfo result = 0
default	11:13:59.355833-0500	runningboardd	Launch request for app<application.com.nexy.assistant.53053210.53053219(501)>[0] is using uid 501 (divined from auid 501 euid 501)
default	11:13:59.355941-0500	runningboardd	Acquiring assertion targeting app<application.com.nexy.assistant.53053210.53053219(501)> from originator [osservice<com.apple.coreservices.uiagent(501)>:75320] with description <RBSAssertionDescriptor| "LS launch com.nexy.assistant" ID:394-75320-35021 target:app<application.com.nexy.assistant.53053210.53053219(501)> attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"LaunchRoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	11:13:59.356046-0500	runningboardd	Assertion 394-75320-35021 (target:app<application.com.nexy.assistant.53053210.53053219(501)>) will be created as active
default	11:13:59.359707-0500	runningboardd	Checking PreventLaunch: global:0 exPath:/Applications/Nexy.app/Contents/MacOS/Nexy predicates:(null) allow:(null)
default	11:13:59.359735-0500	runningboardd	Creating and launching job for: app<application.com.nexy.assistant.53053210.53053219(501)>
default	11:13:59.359754-0500	runningboardd	_mutateContextIfNeeded called for com.nexy.assistant
default	11:13:59.359918-0500	runningboardd	app<application.com.nexy.assistant.53053210.53053219(501)>: -[RBPersonaManager personaForIdentity:context:personaUID:personaUniqueString:] required 0.000000 ms (wallclock); resolved to {4294967295, (null)}
default	11:13:59.369868-0500	dmd	Received xpc stream event (distributed notification matching) with name: com.apple.LaunchServices.applicationRegistered user info: {
    CFBundleDisplayName = Nexy;
    bundleIDs =     (
        "com.nexy.assistant"
    );
    isPlaceholder = 0;
}
default	11:13:59.373462-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78431] is not RunningBoard jetsam managed.
default	11:13:59.373478-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78431] This process will not be managed.
default	11:13:59.373488-0500	runningboardd	Now tracking process: [app<application.com.nexy.assistant.53053210.53053219(501)>:78431]
default	11:13:59.373677-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.53053210.53053219(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	11:13:59.374411-0500	gamepolicyd	Hit the server for a process handle 1dfb6c450001325f that resolved to: [app<application.com.nexy.assistant.53053210.53053219(501)>:78431]
default	11:13:59.374449-0500	gamepolicyd	Received state update for 78431 (app<application.com.nexy.assistant.53053210.53053219(501)>, running-active-NotVisible
default	11:13:59.377350-0500	runningboardd	Using default underlying assertion for app: [app<application.com.nexy.assistant.53053210.53053219(501)>:78431]
default	11:13:59.377435-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.53053210.53053219(501)>:78431] from originator [app<application.com.nexy.assistant.53053210.53053219(501)>:78431] with description <RBSAssertionDescriptor| "RB Underlying Assertion" ID:394-394-35022 target:78431 attributes:[
	<RBSDomainAttribute| domain:"com.apple.underlying" name:"defaultUnderlyingAppAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	11:13:59.377583-0500	runningboardd	Assertion 394-394-35022 (target:[app<application.com.nexy.assistant.53053210.53053219(501)>:78431]) will be created as active
default	11:13:59.377799-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78431] Ignoring jetsam update because this process is not memory-managed
default	11:13:59.377825-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78431] Ignoring suspend because this process is not lifecycle managed
default	11:13:59.377846-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78431] Set darwin role to: UserInteractive
default	11:13:59.377856-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78431] Ignoring GPU update because this process is not GPU managed
default	11:13:59.377875-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78431] Ignoring memory limit update because this process is not memory-managed
default	11:13:59.377945-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78431] reported to RB as running
default	11:13:59.379548-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.53053210.53053219(501)>:78431] from originator [osservice<com.apple.coreservices.launchservicesd>:357] with description <RBSAssertionDescriptor| "uielement:78431" ID:394-357-35023 target:78431 attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"RoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	11:13:59.379673-0500	runningboardd	Assertion 394-357-35023 (target:[app<application.com.nexy.assistant.53053210.53053219(501)>:78431]) will be created as active
default	11:13:59.379925-0500	CoreServicesUIAgent	LAUNCH: 0x0-0x2af2af com.nexy.assistant starting stopped process.
default	11:13:59.380892-0500	loginwindow	-[Application _updateInformationInternal] | Got App URL: file:///Applications/Nexy.app/
default	11:13:59.381268-0500	loginwindow	-[Application setState:] | enter: <Application: 0x8b953cd20: Nexy> state 2
default	11:13:59.381298-0500	loginwindow	-[ApplicationManager checkInAppContext:eventData:] | ApplicationManager: Checked in app : Nexy
default	11:13:59.381407-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78431] Ignoring jetsam update because this process is not memory-managed
default	11:13:59.381448-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78431] Ignoring suspend because this process is not lifecycle managed
default	11:13:59.381467-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78431] Ignoring GPU update because this process is not GPU managed
default	11:13:59.381520-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78431] Ignoring memory limit update because this process is not memory-managed
default	11:13:59.381618-0500	runningboardd	Successfully acquired underlying assertion for [app<application.com.nexy.assistant.53053210.53053219(501)>:78431]
default	11:13:59.383059-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.53053210.53053219(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	11:13:59.383430-0500	runningboardd	Invalidating assertion 394-75320-35021 (target:app<application.com.nexy.assistant.53053210.53053219(501)>) from originator [osservice<com.apple.coreservices.uiagent(501)>:75320]
default	11:13:59.383481-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78431] Ignoring jetsam update because this process is not memory-managed
default	11:13:59.383522-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78431] Ignoring suspend because this process is not lifecycle managed
default	11:13:59.383553-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78431] Ignoring GPU update because this process is not GPU managed
default	11:13:59.383605-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78431] Ignoring memory limit update because this process is not memory-managed
default	11:13:59.383711-0500	gamepolicyd	Received state update for 78431 (app<application.com.nexy.assistant.53053210.53053219(501)>, running-active-NotVisible
default	11:13:59.387543-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.53053210.53053219(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	11:13:59.406475-0500	logger	verifying new process for /Applications/Nexy.app/Contents/MacOS/Nexy
default	11:13:59.449392-0500	logger	detected new pid 78431 for /Applications/Nexy.app/Contents/MacOS/Nexy
default	11:13:59.471359-0500	Nexy	[0x102f169c0] activating connection: mach=true listener=false peer=false name=com.apple.cfprefsd.daemon
default	11:13:59.471437-0500	Nexy	[0x102f11040] activating connection: mach=true listener=false peer=false name=com.apple.cfprefsd.agent
default	11:13:59.484642-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78431] Ignoring jetsam update because this process is not memory-managed
default	11:13:59.484654-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78431] Ignoring suspend because this process is not lifecycle managed
default	11:13:59.484669-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78431] Ignoring GPU update because this process is not GPU managed
default	11:13:59.484688-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78431] Ignoring memory limit update because this process is not memory-managed
default	11:13:59.484868-0500	gamepolicyd	Received state update for 78431 (app<application.com.nexy.assistant.53053210.53053219(501)>, running-active-NotVisible
default	11:13:59.487739-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.53053210.53053219(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	11:13:59.488085-0500	gamepolicyd	Received state update for 78431 (app<application.com.nexy.assistant.53053210.53053219(501)>, running-active-NotVisible
error	11:13:59.588124-0500	Nexy	dlsym cannot find symbol NSMakeRect in CFBundle 0x102f00180 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	11:13:59.588411-0500	Nexy	dlsym cannot find symbol NSMakePoint in CFBundle 0x102f00180 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	11:13:59.588630-0500	Nexy	dlsym cannot find symbol NSMakeSize in CFBundle 0x102f00180 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	11:13:59.588870-0500	Nexy	dlsym cannot find symbol NSMakeRange in CFBundle 0x102f00180 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
default	11:13:59.590202-0500	Nexy	[0x102f11720] activating connection: mach=true listener=false peer=false name=com.apple.coreservices.launchservicesd
default	11:13:59.591032-0500	Nexy	[0xb72050000] activating connection: mach=true listener=false peer=false name=com.apple.analyticsd
default	11:13:59.591367-0500	Nexy	[0xb72050140] activating connection: mach=true listener=false peer=false name=com.apple.pasteboard.1
default	11:13:59.591754-0500	Nexy	[0xb72050280] activating connection: mach=true listener=false peer=false name=com.apple.distributed_notifications@Uv3
default	11:13:59.593764-0500	Nexy	void _NSDisableAutomaticTerminationAndLog(NSString *) No windows open yet
default	11:13:59.594122-0500	Nexy	[0xb720503c0] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	11:13:59.594943-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=78431.1, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=78431, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	11:13:59.597192-0500	tccd	AUTHREQ_SUBJECT: msgID=78431.1, subject=com.nexy.assistant,
default	11:13:59.598275-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x93ad32700 at /Applications/Nexy.app
default	11:13:59.604073-0500	Nexy	Received configuration update from daemon (initial)
default	11:13:59.621494-0500	Nexy	[0xb720503c0] invalidated after the last release of the connection object
default	11:13:59.621692-0500	Nexy	server port 0x00003413, session port 0x00003413
default	11:13:59.622528-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=387.1683, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=78431, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=387, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	11:13:59.622551-0500	tccd	requestor: TCCDProcess: identifier=com.apple.WindowServer, pid=387, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=78431, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	11:13:59.623666-0500	tccd	AUTHREQ_SUBJECT: msgID=387.1683, subject=com.nexy.assistant,
default	11:13:59.625143-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x93ad32700 at /Applications/Nexy.app
default	11:13:59.656413-0500	Nexy	CHECKIN: pid=78431
default	11:13:59.695571-0500	Nexy	Registered process with identifier 78431-596479
default	11:14:00.679311-0500	kernel	SK[7]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid BA70745F-A969-4E69-A133-12EA95765CAD flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.54688,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0x34678b7b tp_proto=0x06"
default	11:14:00.679378-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:54688<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 718393 t_state: SYN_SENT process: Nexy:78431 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xa16ffe69
default	11:14:00.689503-0500	kernel	tcp connected: [<IPv4-redacted>:54688<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 718393 t_state: ESTABLISHED process: Nexy:78431 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xa16ffe69
default	11:14:00.689851-0500	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:54688<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 718393 t_state: FIN_WAIT_1 process: Nexy:78431 Duration: 0.010 sec Conn_Time: 0.010 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 10.000 ms rttvar: 5.000 ms base rtt: 10 ms so_error: 0 svc/tc: 0 flow: 0xa16ffe69
default	11:14:00.689860-0500	kernel	tcp_connection_summary [<IPv4-redacted>:54688<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 718393 t_state: FIN_WAIT_1 process: Nexy:78431 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	11:14:01.789561-0500	Nexy	[0xb72050dc0] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	11:14:01.790352-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=78431.2, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=78431, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	11:14:01.791383-0500	tccd	AUTHREQ_SUBJECT: msgID=78431.2, subject=com.nexy.assistant,
default	11:14:01.792048-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x93ad32700 at /Applications/Nexy.app
default	11:14:01.811952-0500	Nexy	[0xb72050dc0] invalidated after the last release of the connection object
default	11:14:01.814785-0500	Nexy	server port 0x0000680f, session port 0x00003413
default	11:14:01.815593-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=387.1684, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=78431, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=387, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	11:14:01.815625-0500	tccd	requestor: TCCDProcess: identifier=com.apple.WindowServer, pid=387, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=78431, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	11:14:01.816494-0500	tccd	AUTHREQ_SUBJECT: msgID=387.1684, subject=com.nexy.assistant,
default	11:14:01.817105-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x93ad32700 at /Applications/Nexy.app
default	11:14:01.852948-0500	Nexy	  AVAudioSession_MacOS.mm:1021  initForMacOS
default	11:14:01.853487-0500	Nexy	[0xb72050f00] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioSession
default	11:14:01.854290-0500	audiomxd	  ServerSessionManager.mm:315   { "action":"create_session", "session":{"ID":"0x1ee029","name":"Nexy(78431)"}, "details":{"PID":78431,"session_type":"Primary"} }
default	11:14:01.854360-0500	audiomxd	AudioApplicationInfoImpl.mm:250   Setting initial isRecording state: 0 for newly-created AudioApp
	app: {"name":"[implicit] Nexy","pid":78431}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1ee029, sessionType: 'prim', isRecording: false }, 
]
default	11:14:01.855588-0500	audiomxd	  ServerSessionManager.mm:1322  Start process monitoring, pid = 78431, name = Nexy
default	11:14:01.855854-0500	Nexy	    SessionCore_Create.mm:99    Created session 0xb70914ce0 with ID: 0x1ee029
default	11:14:01.856072-0500	Nexy	Registered notify signal com.apple.caulk.alloc.rtdump (0)
default	11:14:01.857101-0500	Nexy	System_Input_Processing_Notification_Handler.mm:456   System_Input_Processing_Notification_Handler::is_vi_available(): Voice isolation DSP is available for client with bundle id com.nexy.assistant (AVFoundation is available, application is not in client deny list, application is not FaceTime variant)
default	11:14:01.858279-0500	Nexy	[0xb72051040] activating connection: mach=true listener=false peer=false name=com.apple.cmio.registerassistantservice.system-extensions
fault	11:14:01.860464-0500	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.53053210.53053219 AUID=501> and <type=Application identifier=application.com.nexy.assistant.53053210.53053219>
default	11:14:01.864443-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOInitializeListenersForBundleID: for <private> -> <private>
default	11:14:01.865928-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> vpio_preferenceChangedListener: new value ((null)) for key AUVoiceIOClients/com-nexy-assistant/AUVoiceIOChatFlavor, translatedBundleID com.nexy.assistant, bundleIDs {(
    "com.nexy.assistant"
)}
default	11:14:01.866069-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> vpio_preferenceChangedListener: new value ((null)) for key AUVoiceIOClients/com-nexy-assistant/AUVoiceIOIsAutoChatFlavorEnabled, translatedBundleID com.nexy.assistant, bundleIDs {(
    "com.nexy.assistant"
)}
default	11:14:01.866219-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetSupportedChatFlavorsForBundleID: <private>-><private> get supported chat flavors: <private>
default	11:14:01.866231-0500	Nexy	            HALSystem.cpp:134    Enabling HAL Voice Isolation support
default	11:14:01.866264-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetHiddenChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	11:14:01.866383-0500	Nexy	[0xb72051180] activating connection: mach=true listener=false peer=false name=com.apple.tccd
default	11:14:01.866487-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOHiddenChatFlavors newValue: (
    1
)
default	11:14:01.866782-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=78431.3, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=78431, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	11:14:01.872746-0500	tccd	AUTHREQ_SUBJECT: msgID=78431.3, subject=com.nexy.assistant,
default	11:14:01.873553-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb2ed5ed00 at /Applications/Nexy.app
default	11:14:01.890110-0500	Nexy	[0xb72051180] invalidated after the last release of the connection object
default	11:14:01.890249-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetPreferredChatFlavorForBundleID: <private>-><private> get value: 0
default	11:14:01.890286-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetSupportedChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	11:14:01.890481-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOSupportedChatFlavors newValue: (
    0,
    2
)
default	11:14:01.891516-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=399.698, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=78431, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	11:14:01.892487-0500	tccd	AUTHREQ_SUBJECT: msgID=399.698, subject=com.nexy.assistant,
default	11:14:01.893374-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb2ed5ed00 at /Applications/Nexy.app
error	11:14:01.909950-0500	tccd	Request message contains a target_token to accessing_process (TCCDProcess: identifier=com.nexy.assistant, pid=78431, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy) but TCCDProcess: identifier=com.apple.audio.coreaudiod, pid=399, auid=202, euid=202, binary_path=/usr/sbin/coreaudiod is not a TCC manager for service: kTCCServiceScreenCapture.
default	11:14:01.910815-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=399.700, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=78431, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	11:14:01.911752-0500	tccd	AUTHREQ_SUBJECT: msgID=399.700, subject=com.nexy.assistant,
default	11:14:01.912296-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb2ed5ed00 at /Applications/Nexy.app
default	11:14:01.927525-0500	Nexy	  HALPlugInManagement.cpp:440    HALPlugInManagement::RegisterPlugIns: skipping in-process plug-ins
error	11:14:01.927541-0500	Nexy	AddInstanceForFactory: No factory registered for id <CFUUID 0xb73af3680> F8BB1C28-BAE8-11D6-9C31-00039315CD46
error	11:14:01.942039-0500	Nexy	         HALC_ProxyObjectMap.cpp:174   HALC_ProxyObjectMap::_CopyObjectByObjectID: failed to create the local object
error	11:14:01.942050-0500	Nexy	            HALC_ShellDevice.cpp:2673  HALC_ShellDevice::RebuildControlList: couldn't find the control object
default	11:14:01.942544-0500	Nexy	     HALC_ProxyObject.cpp:1456   HALC_Object_PropertyListener: not initialized
default	11:14:01.950151-0500	Nexy	[0xb72051180] activating connection: mach=true listener=false peer=false name=com.apple.audioanalyticsd
error	11:14:01.950505-0500	Nexy	Reporter disconnected. { function=sendMessage, reporterID=336858579992577 }
default	11:14:01.950747-0500	Nexy	       AggregateDevice.mm:887   Creating DefaultDeviceAggregate
default	11:14:01.950784-0500	Nexy	       AggregateDevice.mm:914   fetched default output device, ID = 85
default	11:14:01.950817-0500	Nexy	       AggregateDevice.mm:914   fetched default input device, ID = 91
default	11:14:01.976064-0500	Nexy	  AVAudioSession_MacOS.mm:507   Setting category: AVAudioSessionCategoryPlayback, requires reconfiguration?: NO
default	11:14:01.976130-0500	Nexy	  AVAudioSession_MacOS.mm:883   Activating session
default	11:14:02.999931-0500	Nexy	                AUHAL.cpp:420   AUHAL: (0xb7470e340) Selecting device 85 from constructor
default	11:14:02.999941-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0xb7470e340)
default	11:14:02.999946-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0xb7470e340) not already running
default	11:14:02.999953-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0xb7470e340) nothing to teardown
default	11:14:02.999957-0500	Nexy	                AUHAL.cpp:762   SelectDevice: (0xb7470e340) connecting device 85
default	11:14:02.000037-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0xb7470e340) Device ID: 85 (Input:No | Output:Yes): true
default	11:14:02.000118-0500	Nexy	                AUHAL.cpp:774   SelectDevice: (0xb7470e340) created ioproc 0xa for device 85
default	11:14:02.000220-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0xb7470e340) adding 7 device listeners to device 85
default	11:14:02.000376-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0xb7470e340) adding 0 device delegate listeners to device 85
default	11:14:02.000391-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0xb7470e340)
default	11:14:02.000458-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  48000 Hz, Float32, interleaved
default	11:14:02.000466-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	11:14:02.004153-0500	tccd	AUTHREQ_SUBJECT: msgID=387.1686, subject=com.nexy.assistant,
default	11:14:02.004703-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	11:14:02.004755-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x93ad32700 at /Applications/Nexy.app
default	11:14:02.004919-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	11:14:02.010241-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	11:14:02.010443-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	11:14:02.012023-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0xb73eb3720, from  2 ch,  44100 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	11:14:02.012037-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	11:14:02.012331-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	11:14:02.013103-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0xb73eb36c0, from  2 ch,  48000 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	11:14:02.013112-0500	Nexy	       AudioConverter.cpp:1317  AudioConverter -> 0xb73eb36c0: The in-process GetProperty call returned 1886547824 for property 1886546285 with size 8.
default	11:14:02.013117-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	11:14:02.013117-0500	Nexy	AudioConverter -> 0xb73eb36c0: The in-process SetProperty call returned 1886547824 for property 1936876385 with size 4.
default	11:14:02.013124-0500	Nexy	AudioConverter -> 0xb73eb36c0: The in-process SetProperty call returned 1886547824 for property 1936876401 with size 4.
default	11:14:02.013128-0500	Nexy	AudioConverter -> 0xb73eb36c0: The in-process SetProperty call returned 1886547824 for property 1886547309 with size 4.
default	11:14:02.013772-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0xb73eb36c0, from  2 ch,  48000 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	11:14:02.013784-0500	Nexy	       AudioConverter.cpp:1317  AudioConverter -> 0xb73eb36c0: The in-process GetProperty call returned 1886547824 for property 1886546285 with size 8.
default	11:14:02.013789-0500	Nexy	AudioConverter -> 0xb73eb36c0: The in-process SetProperty call returned 1886547824 for property 1936876385 with size 4.
default	11:14:02.013792-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	11:14:02.013798-0500	Nexy	AudioConverter -> 0xb73eb36c0: The in-process SetProperty call returned 1886547824 for property 1936876401 with size 4.
default	11:14:02.013803-0500	Nexy	AudioConverter -> 0xb73eb36c0: The in-process SetProperty call returned 1886547824 for property 1886547309 with size 4.
default	11:14:02.013956-0500	Nexy	       AudioConverter.cpp:1317  AudioConverter -> 0xb73eb36c0: The in-process GetProperty call returned 1886547824 for property 1886546285 with size 8.
default	11:14:02.015799-0500	kernel	SK[8]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 8C370E40-B62E-4527-A2DA-6A9E9E4C5C4B flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.54691,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0x4b74d91d tp_proto=0x06"
default	11:14:02.015860-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:54691<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 718400 t_state: SYN_SENT process: Nexy:78431 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 6 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xa95fae0e
default	11:14:02.016647-0500	Nexy	networkd_settings_read_from_file initialized networkd settings by reading plist directly
default	11:14:02.016772-0500	Nexy	networkd_settings_read_from_file initialized networkd settings by reading plist directly
default	11:14:02.021859-0500	kernel	tcp connected: [<IPv4-redacted>:54691<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 718400 t_state: ESTABLISHED process: Nexy:78431 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 6 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xa95fae0e
default	11:14:02.021884-0500	Nexy	nw_path_libinfo_path_check [579ED7D1-FBB5-4C03-89EE-1942A637C19A IPv4#b6c54e8d:443 tcp, legacy-socket, attribution: developer]
	libinfo check path: <private>
default	11:14:02.022964-0500	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:54691<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 718400 t_state: FIN_WAIT_1 process: Nexy:78431 Duration: 0.007 sec Conn_Time: 0.006 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 6.000 ms rttvar: 3.000 ms base rtt: 6 ms so_error: 0 svc/tc: 0 flow: 0xa95fae0e
default	11:14:02.022979-0500	kernel	tcp_connection_summary [<IPv4-redacted>:54691<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 718400 t_state: FIN_WAIT_1 process: Nexy:78431 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	11:14:02.023056-0500	kernel	SK[6]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 524CD735-1F63-4C1C-9E1C-D606CBEB51D9 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.54692,dst=<IPv4-redacted>.443,proto=0x06 mask=0x0000003f,hash=0x4471d043 tp_proto=0x06"
default	11:14:02.023088-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:54692<-><IPv4-redacted>:443] interface: en0 (skipped: 0)
so_gencnt: 718401 t_state: SYN_SENT process: Nexy:78431 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x84ce1da3
default	11:14:02.023202-0500	kernel	SK[9]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 4DBE8B34-12AF-4304-8E70-398A1569D08A flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.54693,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0xabefee44 tp_proto=0x06"
default	11:14:02.023221-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:54693<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 718402 t_state: SYN_SENT process: Nexy:78431 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 6 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xb50a025c
default	11:14:02.029324-0500	kernel	tcp connected: [<IPv4-redacted>:54693<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 718402 t_state: ESTABLISHED process: Nexy:78431 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 6 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xb50a025c
default	11:14:02.029509-0500	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:54693<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 718402 t_state: FIN_WAIT_1 process: Nexy:78431 Duration: 0.006 sec Conn_Time: 0.006 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 6.000 ms rttvar: 3.000 ms base rtt: 6 ms so_error: 0 svc/tc: 0 flow: 0xb50a025c
default	11:14:02.029519-0500	kernel	tcp_connection_summary [<IPv4-redacted>:54693<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 718402 t_state: FIN_WAIT_1 process: Nexy:78431 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	11:14:02.037288-0500	kernel	tcp connected: [<IPv4-redacted>:54692<-><IPv4-redacted>:443] interface: en0 (skipped: 0)
so_gencnt: 718401 t_state: ESTABLISHED process: Nexy:78431 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x84ce1da3
default	11:14:02.172288-0500	System Events	TCCAccessRequestIndirect: TCCAccessRequestIndirect with pid 78442: target_identity: {
    kTCCCodeIdentityAuditToken = {length = 32, bytes = 0xf5010000 f5010000 14000000 f5010000 ... b6860100 101a0900 };
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
default	11:14:02.184165-0500	tccd	target_executable_path_URL: file:///Applications/Nexy.app/Contents/MacOS/Nexy
default	11:14:02.194171-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb2ed5db00 at /Applications/Nexy.app
default	11:14:02.211035-0500	tccd	Prompting for access to indirect object System Events by Nexy
default	11:14:02.437490-0500	Nexy	[0xb72051680] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	11:14:02.438137-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=78431.4, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=78431, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	11:14:02.444969-0500	tccd	AUTHREQ_SUBJECT: msgID=78431.4, subject=com.nexy.assistant,
default	11:14:02.445663-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x93ad32700 at /Applications/Nexy.app
default	11:14:02.465686-0500	Nexy	[0xb72051680] invalidated after the last release of the connection object
default	11:14:02.465953-0500	Nexy	[0xb72051680] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	11:14:02.466495-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=78431.5, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=78431, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	11:14:02.467406-0500	tccd	AUTHREQ_SUBJECT: msgID=78431.5, subject=com.nexy.assistant,
default	11:14:02.468053-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x93ad32700 at /Applications/Nexy.app
default	11:14:02.486583-0500	Nexy	[0xb72051680] invalidated after the last release of the connection object
default	11:14:02.486659-0500	Nexy	 [INFO] SLSHWCaptureDesktopProxying:485 request: <private>
default	11:14:02.487078-0500	Nexy	[0xb72051680] activating connection: mach=true listener=false peer=false name=com.apple.replayd
default	11:14:02.487205-0500	Nexy	 [INFO] -[RPDaemonProxy consumeSandboxExtension:processNewConnection:]:568
default	11:14:02.487289-0500	Nexy	 [INFO] -[RPDaemonProxy proxyCoreGraphicsWithMethodType:config:machPort:completionHandler:]:1493
default	11:14:02.489250-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=96069.72, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=78431, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.replayd, pid=96069, auid=501, euid=501, binary_path=/usr/libexec/replayd}, },
default	11:14:02.489279-0500	tccd	requestor: TCCDProcess: identifier=com.apple.replayd, pid=96069, auid=501, euid=501, binary_path=/usr/libexec/replayd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=78431, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	11:14:02.490149-0500	tccd	AUTHREQ_SUBJECT: msgID=96069.72, subject=com.nexy.assistant,
default	11:14:02.490813-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x93ad32700 at /Applications/Nexy.app
default	11:14:02.514683-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=387.1690, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=78431, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=387, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	11:14:02.514709-0500	tccd	requestor: TCCDProcess: identifier=com.apple.WindowServer, pid=387, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=78431, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	11:14:02.515616-0500	tccd	AUTHREQ_SUBJECT: msgID=387.1690, subject=com.nexy.assistant,
default	11:14:02.516315-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x93ad32700 at /Applications/Nexy.app
default	11:14:02.573518-0500	Nexy	 [INFO] SLSHWCaptureDesktopProxying_block_invoke:506 request: <private>, error: (null), windowInfo: (null)
fault	11:14:02.622041-0500	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.53053210.53053219 AUID=501> and <type=Application identifier=application.com.nexy.assistant.53053210.53053219>
fault	11:14:02.624798-0500	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.53053210.53053219 AUID=501> and <type=Application identifier=application.com.nexy.assistant.53053210.53053219>
default	11:14:02.645382-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	11:14:02.645478-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant)]
default	11:14:02.645518-0500	ControlCenter	Active activity attributions changed to ["scr:com.nexy.assistant"]
default	11:14:02.853370-0500	Nexy	  AVAudioSession_MacOS.mm:883   Activating session
default	11:14:02.855731-0500	Nexy	         AVAudioEngine.mm:1182  Engine@0xb709c4650: start, was running 0
default	11:14:02.857394-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.53053210.53053219(501)>:78431] from originator [osservice<com.apple.powerd>:328] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:394-328-35038 target:78431 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	11:14:02.857460-0500	runningboardd	Assertion 394-328-35038 (target:[app<application.com.nexy.assistant.53053210.53053219(501)>:78431]) will be created as active
default	11:14:02.857717-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78431] Ignoring jetsam update because this process is not memory-managed
default	11:14:02.857728-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78431] Ignoring suspend because this process is not lifecycle managed
default	11:14:02.857754-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78431] Ignoring GPU update because this process is not GPU managed
default	11:14:02.857810-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78431] Ignoring memory limit update because this process is not memory-managed
default	11:14:02.861159-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.53053210.53053219(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	11:14:02.861813-0500	gamepolicyd	Received state update for 78431 (app<application.com.nexy.assistant.53053210.53053219(501)>, running-active-NotVisible
default	11:14:02.871503-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xa}
default	11:14:02.872219-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ee029","name":"Nexy(78431)"}, "details":{"deviceUIDs":["1C-77-54-18-C8-A3:output"],"implicit_category":"MediaPlayback","input_running":false,"output_running":true} }
default	11:14:02.872298-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 42, PID = 78431, Name = sid:0x1ee029, Nexy(78431), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	11:14:02.872338-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 42, PID = 78431, Name = sid:0x1ee029, Nexy(78431), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	11:14:02.872380-0500	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1ee029, Nexy(78431), 'prim'', AudioCategory changed to 'MediaPlayback'
default	11:14:02.872409-0500	audiomxd	UpdateAudioState CID 0x45550001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	11:14:02.872437-0500	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 42, PID = 78431, Name = sid:0x1ee029, Nexy(78431), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO> is going active
default	11:14:02.872452-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsPlaying:]: MXCoreSession com.nexy.assistant with category/mode MediaPlayback/Default and coreSessionID = 42 starting playing
default	11:14:02.872519-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 42, PID = 78431, Name = sid:0x1ee029, Nexy(78431), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	11:14:02.872531-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	11:14:02.872556-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 42, PID = 78431, Name = sid:0x1ee029, Nexy(78431), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO>
default	11:14:02.872569-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	11:14:02.872586-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found 2 different sessions firstSession={clientName:'sid:0x1ee003, Browser Helper(1622), 'prim'', displayID:'company.thebrowser.browser.helper'}, secondSession={clientName:'sid:0x1ee029, Nexy(78431), 'prim'', displayID:'com.nexy.assistant'} but will use session={clientName:'(null)', displayID:'(null)'}
default	11:14:02.872704-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 1]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)}
default	11:14:02.872714-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	11:14:02.872623-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 201, deviceID = <private>
default	11:14:02.872637-0500	audiomxd	AudioApplicationInfoImpl.mm:395   Successfully updated session 0x1ee029 to isSessionRecording: 0
	app: {"name":"[implicit] Nexy","pid":78431}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1ee029, sessionType: 'prim', isRecording: false }, 
]
default	11:14:02.872833-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 201 flag 0x1 < Hijack > app com.nexy.assistant CID 0x45550001 category Not set
default	11:14:02.873014-0500	audiomxd	UpdateAudioState CID 0x45550001 audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	11:14:02.873086-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 201,
}
default	11:14:02.873114-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	11:14:02.873126-0500	audioaccessoryd	AudioStateChanged: Added audio session app com.nexy.assistant NULL -> 201 count 3
default	11:14:02.873133-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 201
default	11:14:03.092725-0500	Nexy	[0xb72051a40] activating connection: mach=true listener=false peer=false name=com.apple.usernoted.client
default	11:14:03.106266-0500	distnoted	register name: com.apple.nsquiet_safe_quit_give_reason object: com.nexy.assistant token: 2300000021 pid: 78431
default	11:14:03.106323-0500	usernoted	Connection com.nexy.assistant with path: /Applications/Nexy.app
default	11:14:03.106436-0500	spindump	Nexy [78431]: spin: not sampling due to conditions 0x400000000
default	11:14:03.118879-0500	Nexy	NSApp cache appearance:
-NSRequiresAquaSystemAppearance: 0
-appearance: (null)
-effectiveAppearance: <NSCompositeAppearance: 0xb71a7c780
 (
    "<NSAquaAppearance: 0xb71a7c820>",
    "<NSSystemAppearance: 0xb71a7c6e0>"
)>
default	11:14:03.122371-0500	Nexy	[0xb72051f40] activating connection: mach=true listener=false peer=false name=com.apple.dock.fullscreen
default	11:14:03.123106-0500	Nexy	[0xb72052080] activating connection: mach=true listener=false peer=false name=com.apple.fonts
default	11:14:03.126246-0500	Nexy	(<private>) deleteSearchableItemsWithDomainIdentifiers, protectionClass:(null), domainIdentifiers number:1
default	11:14:03.126621-0500	Nexy	sConnectionName: com.apple.spotlight.IndexAgent
default	11:14:03.126635-0500	Nexy	Start service name com.apple.spotlight.IndexAgent
default	11:14:03.126666-0500	Nexy	[0xb720521c0] activating connection: mach=true listener=false peer=false name=com.apple.spotlight.IndexAgent
default	11:14:03.127788-0500	suggestd	SGDSpotlightReceiver: deleting 1 domain identifiers (1 after removing overlaps) for com.nexy.assistant: <private>
default	11:14:03.132612-0500	Nexy	[C:1] Alloc com.apple.controlcenter.statusitems
default	11:14:03.132687-0500	Nexy	[0xb72052300] activating connection: mach=false listener=false peer=false name=(anonymous)
default	11:14:03.132765-0500	Nexy	FBSWorkspace registering source: <private>
default	11:14:03.133553-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	11:14:03.134330-0500	Nexy	<FBSWorkspaceScenesClient:0xb74849040 <private>> attempting immediate handshake from activate
default	11:14:03.134385-0500	Nexy	<FBSWorkspaceScenesClient:0xb74849040 <private>> sent handshake
default	11:14:03.134517-0500	Nexy	Realizing settings extension __NSStatusItemSceneHostSettings__ on FBSSceneSettings
default	11:14:03.134548-0500	ControlCenter	Asked to bootstrap a new process for handle: [app<application.com.nexy.assistant.53053210.53053219(501)>:78431]
default	11:14:03.134593-0500	ControlCenter	Creating process (sync=true) for handle: [app<application.com.nexy.assistant.53053210.53053219(501)>:78431]
default	11:14:03.134707-0500	ControlCenter	[app<application.com.nexy.assistant.53053210.53053219>:78431] Registering event dispatcher at init
default	11:14:03.134795-0500	ControlCenter	Created <FBWorkspace: 0xb0820e8a0; <FBApplicationProcess: 0xb081c7900; app<application.com.nexy.assistant.53053210.53053219>:78431(v919FF)>>
default	11:14:03.134814-0500	ControlCenter	Bootstrapping app<application.com.nexy.assistant.53053210.53053219> with intent background
default	11:14:03.135219-0500	Nexy	Realizing settings extension __NSStatusItemSceneClientSettings__ on FBSSceneClientSettings
default	11:14:03.135329-0500	runningboardd	Launch request for app<application.com.nexy.assistant.53053210.53053219(501)>[0] is using uid 501 (divined from auid 501 euid 501)
default	11:14:03.135509-0500	runningboardd	Acquiring assertion targeting app<application.com.nexy.assistant.53053210.53053219(501)> from originator [osservice<com.apple.controlcenter(501)>:626] with description <RBSAssertionDescriptor| "FBApplicationProcess" ID:394-626-35039 target:app<application.com.nexy.assistant.53053210.53053219(501)> attributes:[
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableLPRunReason-Suspend" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableRole-NonUI" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableJetsamPriority-Active" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableBootstrapping" sourceEnvironment:"(null)">
	]>
default	11:14:03.135718-0500	runningboardd	Assertion 394-626-35039 (target:app<application.com.nexy.assistant.53053210.53053219(501)>) will be created as active
default	11:14:03.135752-0500	runningboardd	setting abstract target for <RBSAssertionDescriptor| "FBApplicationProcess" ID:394-626-35039 target:app<application.com.nexy.assistant.53053210.53053219(501)> attributes:[
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableLPRunReason-Suspend" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableRole-NonUI" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableJetsamPriority-Active" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableBootstrapping" sourceEnvironment:"(null)">
	]> to [app<application.com.nexy.assistant.53053210.53053219(501)>:78431]
default	11:14:03.136194-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78431] Ignoring jetsam update because this process is not memory-managed
default	11:14:03.136205-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78431] Ignoring suspend because this process is not lifecycle managed
default	11:14:03.136215-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78431] Ignoring GPU update because this process is not GPU managed
default	11:14:03.136936-0500	Nexy	Realizing settings extension FBSSceneSettingsCore on FBSSceneSettings
default	11:14:03.137233-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78431] Ignoring memory limit update because this process is not memory-managed
default	11:14:03.138431-0500	Nexy	Realizing settings extension FBSSceneClientSettingsCore on FBSSceneClientSettings
default	11:14:03.139143-0500	Nexy	Requesting scene <FBSScene: 0xb74849400; com.apple.controlcenter:3102C5D7-32AB-4033-A1B7-0E582F2556E7> from com.apple.controlcenter.statusitems
default	11:14:03.139568-0500	Nexy	Request for <FBSScene: 0xb74849400; com.apple.controlcenter:3102C5D7-32AB-4033-A1B7-0E582F2556E7> complete!
default	11:14:03.139671-0500	Nexy	Realizing settings extension FBSSceneTransitionContextCore on FBSSceneTransitionContext
default	11:14:03.141499-0500	Nexy	Realizing settings extension __NSHostedViewSceneSettings__ on FBSSceneSettings
default	11:14:03.141877-0500	Nexy	Realizing settings extension __NSClientHostedViewSceneSettings__ on FBSSceneClientSettings
default	11:14:03.142124-0500	Nexy	Realizing settings extension __NSStatusItemAuxiliaryViewSceneSettings__ on FBSSceneSettings
default	11:14:03.142160-0500	Nexy	Realizing settings extension __NSClientStatusItemAuxiliaryViewSceneSettings__ on FBSSceneClientSettings
default	11:14:03.142587-0500	Nexy	Requesting scene <FBSScene: 0xb748490e0; com.apple.controlcenter:3102C5D7-32AB-4033-A1B7-0E582F2556E7-Aux[1]-NSStatusItemView> from com.apple.controlcenter.statusitems
default	11:14:03.142859-0500	Nexy	Request for <FBSScene: 0xb748490e0; com.apple.controlcenter:3102C5D7-32AB-4033-A1B7-0E582F2556E7-Aux[1]-NSStatusItemView> complete!
default	11:14:03.143548-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.53053210.53053219(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	11:14:03.144567-0500	ControlCenter	[app<application.com.nexy.assistant.53053210.53053219>:78431] Bootstrap success!
default	11:14:03.144933-0500	gamepolicyd	Received state update for 78431 (app<application.com.nexy.assistant.53053210.53053219(501)>, running-active-NotVisible
default	11:14:03.145159-0500	ControlCenter	[app<application.com.nexy.assistant.53053210.53053219>:78431] Setting process visibility to: Background
default	11:14:03.145236-0500	ControlCenter	[app<application.com.nexy.assistant.53053210.53053219>:78431] No launch watchdog for this process, dropping initial assertion in 2.0s
default	11:14:03.145608-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.53053210.53053219(501)>:78431] from originator [osservice<com.apple.controlcenter(501)>:626] with description <RBSAssertionDescriptor| "FBWorkspaceDomain: injecting saved endowment" ID:394-626-35040 target:78431 attributes:[
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"WorkspaceEndpointInjection" sourceEnvironment:"(null)">
	]>
default	11:14:03.145694-0500	runningboardd	Assertion 394-626-35040 (target:[app<application.com.nexy.assistant.53053210.53053219(501)>:78431]) will be created as active
default	11:14:03.146131-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78431] Ignoring jetsam update because this process is not memory-managed
default	11:14:03.146146-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78431] Ignoring suspend because this process is not lifecycle managed
default	11:14:03.146157-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78431] Ignoring GPU update because this process is not GPU managed
default	11:14:03.146178-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78431] Ignoring memory limit update because this process is not memory-managed
default	11:14:03.149571-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.53053210.53053219(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	11:14:03.150296-0500	ControlCenter	Adding: <FBApplicationProcess: 0xb081c7900; app<application.com.nexy.assistant.53053210.53053219>:78431(v919FF)>
default	11:14:03.150652-0500	gamepolicyd	Received state update for 78431 (app<application.com.nexy.assistant.53053210.53053219(501)>, running-active-NotVisible
default	11:14:03.150717-0500	Nexy	[com.apple.controlcenter:3102C5D7-32AB-4033-A1B7-0E582F2556E7-Aux[1]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
default	11:14:03.150738-0500	Nexy	[com.apple.controlcenter:3102C5D7-32AB-4033-A1B7-0E582F2556E7-Aux[1]-NSStatusItemView] Dropping transition context because the scene is reconnecting
default	11:14:03.150903-0500	ControlCenter	[app<application.com.nexy.assistant.53053210.53053219>:78431] Connection established.
default	11:14:03.150985-0500	ControlCenter	Received state update for 78431 (app<application.com.nexy.assistant.53053210.53053219(501)>, running-active-NotVisible
default	11:14:03.151000-0500	ControlCenter	[app<application.com.nexy.assistant.53053210.53053219>:78431] created proxy of <BSXPCServiceConnectionProxy<FBSWorkspaceServiceServerInterface>: 0xb08210d90>
default	11:14:03.151041-0500	ControlCenter	[app<application.com.nexy.assistant.53053210.53053219>:78431] Connection to remote process established!
default	11:14:03.155303-0500	Nexy	[com.apple.controlcenter:3102C5D7-32AB-4033-A1B7-0E582F2556E7-Aux[1]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
default	11:14:03.155323-0500	Nexy	[com.apple.controlcenter:3102C5D7-32AB-4033-A1B7-0E582F2556E7-Aux[1]-NSStatusItemView] Dropping transition context because the scene is reconnecting
default	11:14:03.155432-0500	Nexy	Warning: the app is using `-[NSStatusBarButton setHighlightsBy:]` to set the highlight behavior. Instead, consider removing that setting. That will enable macOS to highlight the status bar button as appropriate for all configurations (e.g., light, dark, and increased contrast modes).
default	11:14:03.157573-0500	ControlCenter	Asked to bootstrap a new process for handle: [app<application.com.nexy.assistant.53053210.53053219(501)>:78431]
default	11:14:03.157610-0500	ControlCenter	A process already exists for this handle: <FBApplicationProcess: 0xb081c7900; app<application.com.nexy.assistant.53053210.53053219>:78431(v919FF)>
default	11:14:03.157816-0500	ControlCenter	[app<application.com.nexy.assistant.53053210.53053219>:78431] Registered new scene: <FBWorkspaceScene: 0xb07481980; com.apple.controlcenter:3102C5D7-32AB-4033-A1B7-0E582F2556E7> (fromRemnant = 0)
default	11:14:03.157887-0500	ControlCenter	[app<application.com.nexy.assistant.53053210.53053219>:78431] Workspace interruption policy did change: reconnect
default	11:14:03.158201-0500	ControlCenter	[com.apple.controlcenter:3102C5D7-32AB-4033-A1B7-0E582F2556E7] Client process connected: [app<application.com.nexy.assistant.53053210.53053219(501)>:78431]
default	11:14:03.158200-0500	Nexy	Request for <FBSScene: 0xb74849400; com.apple.controlcenter:3102C5D7-32AB-4033-A1B7-0E582F2556E7> complete!
default	11:14:03.158444-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.53053210.53053219(501)>:78431] from originator [osservice<com.apple.controlcenter(501)>:626] with description <RBSAssertionDescriptor| "com.apple.frontboard.after-life.interrupted" ID:394-626-35041 target:78431 attributes:[
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"AfterLife-Interrupted" sourceEnvironment:"(null)">
	]>
default	11:14:03.158588-0500	runningboardd	Assertion 394-626-35041 (target:[app<application.com.nexy.assistant.53053210.53053219(501)>:78431]) will be created as inactive as originator process has not exited
default	11:14:03.159043-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.53053210.53053219(501)>:78431] from originator [osservice<com.apple.controlcenter(501)>:626] with description <RBSAssertionDescriptor| "FBWorkspace (BG-Active[40])" ID:394-626-35042 target:78431 attributes:[
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableLPRunReason-Suspend" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableRole-NonUI" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableJetsamPriority-Active" sourceEnvironment:"(null)">
	]>
default	11:14:03.159178-0500	runningboardd	Assertion 394-626-35042 (target:[app<application.com.nexy.assistant.53053210.53053219(501)>:78431]) will be created as active
default	11:14:03.159189-0500	ControlCenter	Asked to bootstrap a new process for handle: [app<application.com.nexy.assistant.53053210.53053219(501)>:78431]
default	11:14:03.159214-0500	ControlCenter	A process already exists for this handle: <FBApplicationProcess: 0xb081c7900; app<application.com.nexy.assistant.53053210.53053219>:78431(v919FF)>
default	11:14:03.159281-0500	ControlCenter	[app<application.com.nexy.assistant.53053210.53053219>:78431] Workspace state did change: XX-None[0] --> BG-Active[40] (assertion acquired).
default	11:14:03.159296-0500	ControlCenter	[app<application.com.nexy.assistant.53053210.53053219>:78431] Registered new scene: <FBWorkspaceScene: 0xb074809c0; com.apple.controlcenter:3102C5D7-32AB-4033-A1B7-0E582F2556E7-Aux[1]-NSStatusItemView> (fromRemnant = 0)
default	11:14:03.159466-0500	Nexy	Request for <FBSScene: 0xb748490e0; com.apple.controlcenter:3102C5D7-32AB-4033-A1B7-0E582F2556E7-Aux[1]-NSStatusItemView> complete!
default	11:14:03.159481-0500	ControlCenter	[com.apple.controlcenter:3102C5D7-32AB-4033-A1B7-0E582F2556E7-Aux[1]-NSStatusItemView] Client process connected: [app<application.com.nexy.assistant.53053210.53053219(501)>:78431]
default	11:14:03.159512-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78431] Ignoring jetsam update because this process is not memory-managed
default	11:14:03.159557-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78431] Ignoring suspend because this process is not lifecycle managed
default	11:14:03.159588-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78431] Ignoring GPU update because this process is not GPU managed
default	11:14:03.159750-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78431] Ignoring memory limit update because this process is not memory-managed
default	11:14:03.160010-0500	Nexy	<FBSWorkspaceScenesClient:0xb74849040 <private>> Reconnecting scene com.apple.controlcenter:3102C5D7-32AB-4033-A1B7-0E582F2556E7
default	11:14:03.160320-0500	Nexy	<FBSWorkspaceScenesClient:0xb74849040 <private>> Reconnecting scene com.apple.controlcenter:3102C5D7-32AB-4033-A1B7-0E582F2556E7-Aux[1]-NSStatusItemView
default	11:14:03.162997-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.53053210.53053219(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	11:14:03.163738-0500	ControlCenter	Received state update for 78431 (app<application.com.nexy.assistant.53053210.53053219(501)>, running-active-NotVisible
default	11:14:03.163841-0500	Nexy	Registering for test daemon availability notify post.
default	11:14:03.164067-0500	gamepolicyd	Received state update for 78431 (app<application.com.nexy.assistant.53053210.53053219(501)>, running-active-NotVisible
default	11:14:03.164056-0500	Nexy	notify_get_state check indicated test daemon not ready.
default	11:14:03.164201-0500	Nexy	notify_get_state check indicated test daemon not ready.
default	11:14:03.164311-0500	Nexy	notify_get_state check indicated test daemon not ready.
default	11:14:03.166306-0500	Nexy	[0xb720526c0] activating connection: mach=true listener=false peer=false name=com.apple.coreservices.appleevents
default	11:14:03.170711-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x93ad32700 at /Applications/Nexy.app
default	11:14:03.174104-0500	Nexy	[0xb720503c0] Connection returned listener port: 0x4603
default	11:14:03.174690-0500	Nexy	SignalReady: pid=78431 asn=0x0-0x2af2af
default	11:14:03.175244-0500	Nexy	SIGNAL: pid=78431 asn=0x0x-0x2af2af
default	11:14:03.176250-0500	loginwindow	-[Application _updateInformationInternal] | Got App URL: file:///Applications/Nexy.app/
default	11:14:03.193001-0500	Nexy	[com.apple.controlcenter:3102C5D7-32AB-4033-A1B7-0E582F2556E7-Aux[1]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
default	11:14:03.198673-0500	Nexy	[com.apple.controlcenter:3102C5D7-32AB-4033-A1B7-0E582F2556E7-Aux[1]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
default	11:14:03.202286-0500	Nexy	void _NSDisableAutomaticTerminationAndLog(NSString *) Restoring windows
default	11:14:03.202296-0500	Nexy	-[NSApplication _reopenWindowsAsNecessaryIncludingRestorableState:withFullFidelity:completionHandler:] shouldRestoreState=1 hasPersistentStateToRestore=0 shouldStillRestoreStateAfterPrompting=0
default	11:14:03.202313-0500	Nexy	[0xb72051540] activating connection: mach=true listener=false peer=false name=com.apple.window_proxies
default	11:14:03.202500-0500	Nexy	[0xb72051540] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	11:14:03.203819-0500	Nexy	void _NSEnableAutomaticTerminationAndLog(NSString *) Restoring windows
default	11:14:03.206800-0500	Nexy	[C:2] Alloc <private>
default	11:14:03.206841-0500	Nexy	[0xb72051540] activating connection: mach=false listener=false peer=false name=(anonymous)
default	11:14:03.207858-0500	ControlCenter	Host properties initialized; (bid:com.nexy.assistant-Item-0-78431). State(applicationItem: true, clientRequestsVisibility: true, neverClip: false)
default	11:14:03.208587-0500	WindowManager	Connection activated | (78431) Nexy
default	11:14:03.208770-0500	ControlCenter	Starting to track host; (bid:com.nexy.assistant-Item-0-78431)
default	11:14:03.208946-0500	ControlCenter	Created new displayable type DisplayableAppStatusItemType(26D04188, (bid:com.nexy.assistant-Item-0-78431)) for (bid:com.nexy.assistant-Item-0-78431)
default	11:14:03.208992-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.53053210.53053219(501)>:78431] from originator [app<application.com.nexy.assistant.53053210.53053219(501)>:78431] with description <RBSAssertionDescriptor| "AudioHAL" ID:394-78431-35043 target:78431 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	11:14:03.209074-0500	runningboardd	Assertion 394-78431-35043 (target:[app<application.com.nexy.assistant.53053210.53053219(501)>:78431]) will be created as active
default	11:14:03.209513-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78431] Ignoring jetsam update because this process is not memory-managed
default	11:14:03.209532-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78431] Ignoring suspend because this process is not lifecycle managed
default	11:14:03.209611-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78431] Ignoring GPU update because this process is not GPU managed
default	11:14:03.209693-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78431] Ignoring memory limit update because this process is not memory-managed
default	11:14:03.209930-0500	ControlCenter	Adding displayable items for status items; [(bid:com.nexy.assistant-Item-0-78431)]
default	11:14:03.210027-0500	ControlCenter	Created instance DisplayableId(EB23AC06) in .menuBar for DisplayableAppStatusItemType(26D04188, (bid:com.nexy.assistant-Item-0-78431)) .menuBar
default	11:14:03.212877-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.53053210.53053219(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	11:14:03.213478-0500	ControlCenter	Received state update for 78431 (app<application.com.nexy.assistant.53053210.53053219(501)>, running-active-NotVisible
default	11:14:03.213695-0500	gamepolicyd	Received state update for 78431 (app<application.com.nexy.assistant.53053210.53053219(501)>, running-active-NotVisible
default	11:14:03.215512-0500	Nexy	[com.apple.controlcenter:3102C5D7-32AB-4033-A1B7-0E582F2556E7-Aux[1]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
default	11:14:03.216428-0500	Nexy	[com.apple.controlcenter:3102C5D7-32AB-4033-A1B7-0E582F2556E7] Sending action(s) in update: NSSceneFenceAction
default	11:14:03.221141-0500	ControlCenter	Created ephemaral instance DisplayableId(EB23AC06) for (bid:com.nexy.assistant-Item-0-78431) with positioning .ephemeral
default	11:14:03.223948-0500	Nexy	[com.apple.controlcenter:3102C5D7-32AB-4033-A1B7-0E582F2556E7-Aux[1]-NSStatusItemView] Received action(s) in scene-update: NSSceneFenceAction
default	11:14:03.226104-0500	Nexy	[com.apple.controlcenter:3102C5D7-32AB-4033-A1B7-0E582F2556E7-Aux[1]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
default	11:14:03.227299-0500	Nexy	[com.apple.controlcenter:3102C5D7-32AB-4033-A1B7-0E582F2556E7-Aux[1]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
default	11:14:03.233995-0500	Nexy	[com.apple.controlcenter:3102C5D7-32AB-4033-A1B7-0E582F2556E7] Sending action(s) in update: NSSceneFenceAction
default	11:14:03.328783-0500	Nexy	*warn* MailCS ======%%% _setMailMessageAttributes skip:1
default	11:14:03.333054-0500	Nexy	Start service name com.apple.spotlightknowledged
default	11:14:03.335849-0500	Nexy	[GMS] availability notification token 88
default	11:14:03.346179-0500	ControlCenter	[app<application.com.nexy.assistant.53053210.53053219>:78431] Workspace state did change: BG-Active[40] --> XX-None[0] (assertion dropped).
default	11:14:03.346314-0500	runningboardd	Invalidating assertion 394-626-35042 (target:[app<application.com.nexy.assistant.53053210.53053219(501)>:78431]) from originator [osservice<com.apple.controlcenter(501)>:626]
default	11:14:03.349137-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.53053210.53053219(501)>:78431] from originator [osservice<com.apple.controlcenter(501)>:626] with description <RBSAssertionDescriptor| "FBWorkspace (BG-Active[40])" ID:394-626-35044 target:78431 attributes:[
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableLPRunReason-Suspend" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableRole-NonUI" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableJetsamPriority-Active" sourceEnvironment:"(null)">
	]>
default	11:14:03.349298-0500	runningboardd	Assertion 394-626-35044 (target:[app<application.com.nexy.assistant.53053210.53053219(501)>:78431]) will be created as active
default	11:14:03.349433-0500	ControlCenter	[app<application.com.nexy.assistant.53053210.53053219>:78431] Workspace state did change: XX-None[0] --> BG-Active[40] (assertion acquired).
default	11:14:03.451030-0500	ControlCenter	[app<application.com.nexy.assistant.53053210.53053219>:78431] Workspace state did change: BG-Active[40] --> XX-None[0] (assertion dropped).
default	11:14:03.451437-0500	runningboardd	Invalidating assertion 394-626-35044 (target:[app<application.com.nexy.assistant.53053210.53053219(501)>:78431]) from originator [osservice<com.apple.controlcenter(501)>:626]
default	11:14:03.558135-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78431] Ignoring jetsam update because this process is not memory-managed
default	11:14:03.558156-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78431] Ignoring suspend because this process is not lifecycle managed
default	11:14:03.558171-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78431] Ignoring GPU update because this process is not GPU managed
default	11:14:03.558198-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78431] Ignoring memory limit update because this process is not memory-managed
default	11:14:03.562516-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.53053210.53053219(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	11:14:03.563186-0500	ControlCenter	Received state update for 78431 (app<application.com.nexy.assistant.53053210.53053219(501)>, running-active-NotVisible
default	11:14:03.563621-0500	gamepolicyd	Received state update for 78431 (app<application.com.nexy.assistant.53053210.53053219(501)>, running-active-NotVisible
default	11:14:03.697882-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.53053210.53053219(501)>:78431] from originator [osservice<com.apple.WindowServer(88)>:387] with description <RBSAssertionDescriptor| "AppDrawing" ID:394-387-35045 target:78431 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"AppDrawing" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	11:14:03.697946-0500	runningboardd	Assertion 394-387-35045 (target:[app<application.com.nexy.assistant.53053210.53053219(501)>:78431]) will be created as active
default	11:14:03.698278-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78431] Ignoring jetsam update because this process is not memory-managed
default	11:14:03.698352-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78431] Ignoring suspend because this process is not lifecycle managed
default	11:14:03.698398-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78431] Ignoring GPU update because this process is not GPU managed
default	11:14:03.698481-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78431] Ignoring memory limit update because this process is not memory-managed
default	11:14:03.701426-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.53053210.53053219(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	11:14:03.701924-0500	ControlCenter	Received state update for 78431 (app<application.com.nexy.assistant.53053210.53053219(501)>, running-active-NotVisible
default	11:14:03.702037-0500	gamepolicyd	Received state update for 78431 (app<application.com.nexy.assistant.53053210.53053219(501)>, running-active-NotVisible
default	11:14:04.430521-0500	runningboardd	Assertion did invalidate due to timeout: 394-394-35022 (target:[app<application.com.nexy.assistant.53053210.53053219(501)>:78431])
default	11:14:04.632601-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78431] Ignoring jetsam update because this process is not memory-managed
default	11:14:04.632622-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78431] Ignoring suspend because this process is not lifecycle managed
default	11:14:04.632632-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78431] Ignoring GPU update because this process is not GPU managed
default	11:14:04.632651-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78431] Ignoring memory limit update because this process is not memory-managed
default	11:14:04.635616-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.53053210.53053219(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	11:14:04.636359-0500	ControlCenter	Received state update for 78431 (app<application.com.nexy.assistant.53053210.53053219(501)>, running-active-NotVisible
default	11:14:04.636615-0500	gamepolicyd	Received state update for 78431 (app<application.com.nexy.assistant.53053210.53053219(501)>, running-active-NotVisible
default	11:14:04.660043-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb2ed5de00 at /Applications/Nexy.app
default	11:14:04.668214-0500	tccd	Publishing <TCCDEvent: type=Create, service=kTCCServiceAppleEvents, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 3 subscribers: {
    476 = "<TCCDEventSubscriber: token=476, state=Passed, csid=com.apple.photolibraryd>";
    37 = "<TCCDEventSubscriber: token=37, state=Initial, csid=(null)>";
    467 = "<TCCDEventSubscriber: token=467, state=Passed, csid=com.apple.chronod>";
}
default	11:14:04.672760-0500	chronod	[appAuth:com.nexy.assistant] tcc authorization(s) changed
default	11:14:05.243216-0500	runningboardd	Invalidating assertion 394-626-35039 (target:app<application.com.nexy.assistant.53053210.53053219(501)>) from originator [osservice<com.apple.controlcenter(501)>:626]
default	11:14:05.349200-0500	runningboardd	Removed last relative-start-date-defining assertion for process app<application.com.nexy.assistant.53053210.53053219(501)>
default	11:14:05.350334-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78431] Ignoring jetsam update because this process is not memory-managed
default	11:14:05.350359-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78431] Ignoring suspend because this process is not lifecycle managed
default	11:14:05.350378-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78431] Ignoring GPU update because this process is not GPU managed
default	11:14:05.350413-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78431] Ignoring memory limit update because this process is not memory-managed
default	11:14:05.355010-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.53053210.53053219(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	11:14:05.368062-0500	ControlCenter	Received state update for 78431 (app<application.com.nexy.assistant.53053210.53053219(501)>, running-active-NotVisible
default	11:14:05.368320-0500	gamepolicyd	Received state update for 78431 (app<application.com.nexy.assistant.53053210.53053219(501)>, running-active-NotVisible
default	11:14:08.108103-0500	Nexy	void _updateToReflectAutomaticTerminationState(void) Setting _kLSApplicationWouldBeTerminatedByTALKey=1
default	11:14:08.315030-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=387.1693, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=78431, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=387, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	11:14:08.315077-0500	tccd	requestor: TCCDProcess: identifier=com.apple.WindowServer, pid=387, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=78431, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	11:14:08.317142-0500	tccd	AUTHREQ_SUBJECT: msgID=387.1693, subject=com.nexy.assistant,
default	11:14:08.319192-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x93ad32700 at /Applications/Nexy.app
default	11:14:09.936570-0500	Nexy	                AUHAL.cpp:420   AUHAL: (0xb74880e40) Selecting device 85 from constructor
default	11:14:09.936585-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0xb74880e40)
default	11:14:09.936592-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0xb74880e40) not already running
default	11:14:09.936597-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0xb74880e40) nothing to teardown
default	11:14:09.936599-0500	Nexy	                AUHAL.cpp:762   SelectDevice: (0xb74880e40) connecting device 85
default	11:14:09.936698-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0xb74880e40) Device ID: 85 (Input:No | Output:Yes): true
default	11:14:09.936988-0500	Nexy	                AUHAL.cpp:774   SelectDevice: (0xb74880e40) created ioproc 0xb for device 85
default	11:14:09.937165-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0xb74880e40) adding 7 device listeners to device 85
default	11:14:09.937359-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0xb74880e40) adding 0 device delegate listeners to device 85
default	11:14:09.937370-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0xb74880e40)
default	11:14:09.937483-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  48000 Hz, Float32, interleaved
default	11:14:09.937510-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	11:14:09.937520-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	11:14:09.937546-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	11:14:09.937558-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	11:14:09.937647-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0xb74880e40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	11:14:09.937659-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0xb74880e40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	11:14:09.937664-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	11:14:09.937669-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0xb74880e40) removing 0 device listeners from device 0
default	11:14:09.937674-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0xb74880e40) removing 0 device delegate listeners from device 0
default	11:14:09.937679-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0xb74880e40)
default	11:14:09.937701-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is DISABLED
default	11:14:09.937774-0500	Nexy	                AUHAL.cpp:2303  SetProperty: (0xb74880e40) caller requesting device change from 85 to 91
default	11:14:09.937783-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0xb74880e40)
default	11:14:09.937787-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0xb74880e40) not already running
default	11:14:09.937791-0500	Nexy	                AUHAL.cpp:687   SelectDevice: (0xb74880e40) disconnecting device 85
default	11:14:09.937805-0500	Nexy	                AUHAL.cpp:751   SelectDevice: (0xb74880e40) destroying ioproc 0xb for device 85
default	11:14:09.937839-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped Unknown {1C-77-54-18-C8-A3:output, 0xb}
default	11:14:09.938127-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 1]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	11:14:09.938332-0500	Nexy	                AUHAL.cpp:762   SelectDevice: (0xb74880e40) connecting device 91
default	11:14:09.938479-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0xb74880e40) Device ID: 91 (Input:Yes | Output:No): true
default	11:14:09.940051-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=399.701, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=78431, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	11:14:09.944402-0500	tccd	AUTHREQ_SUBJECT: msgID=399.701, subject=com.nexy.assistant,
default	11:14:09.945969-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb2ed5ed00 at /Applications/Nexy.app
default	11:14:09.952477-0500	Nexy	 [INFO] SLSHWCaptureDesktopProxying:485 request: <private>
default	11:14:09.952538-0500	Nexy	 [INFO] -[RPDaemonProxy proxyCoreGraphicsWithMethodType:config:machPort:completionHandler:]:1493
default	11:14:09.954302-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=96069.73, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=78431, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.replayd, pid=96069, auid=501, euid=501, binary_path=/usr/libexec/replayd}, },
default	11:14:09.954329-0500	tccd	requestor: TCCDProcess: identifier=com.apple.replayd, pid=96069, auid=501, euid=501, binary_path=/usr/libexec/replayd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=78431, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	11:14:09.955470-0500	tccd	AUTHREQ_SUBJECT: msgID=96069.73, subject=com.nexy.assistant,
default	11:14:09.956206-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x93ad32700 at /Applications/Nexy.app
default	11:14:09.974647-0500	Nexy	                AUHAL.cpp:774   SelectDevice: (0xb74880e40) created ioproc 0xa for device 91
default	11:14:09.974773-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0xb74880e40) adding 7 device listeners to device 91
default	11:14:09.974968-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0xb74880e40) adding 0 device delegate listeners to device 91
default	11:14:09.974978-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0xb74880e40)
default	11:14:09.974987-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 output streams; not all mono
default	11:14:09.974997-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	11:14:09.975686-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  input stream 0 [0x5c]:  1 ch,  24000 Hz, Float32
default	11:14:09.975694-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 input streams; all mono
default	11:14:09.975699-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  1 ch,  24000 Hz, Float32
default	11:14:09.975802-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0xb74880e40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	11:14:09.975817-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0xb74880e40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	11:14:09.975824-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	11:14:09.975827-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0xb74880e40) removing 7 device listeners from device 85
default	11:14:09.976141-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0xb74880e40) removing 0 device delegate listeners from device 85
default	11:14:09.976151-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0xb74880e40)
default	11:14:09.976952-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	11:14:09.978650-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=399.702, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=78431, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	11:14:09.980786-0500	tccd	AUTHREQ_SUBJECT: msgID=399.702, subject=com.nexy.assistant,
default	11:14:09.981580-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb2ed5ed00 at /Applications/Nexy.app
default	11:14:10.000524-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=387.1696, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=78431, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=387, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	11:14:10.000554-0500	tccd	requestor: TCCDProcess: identifier=com.apple.WindowServer, pid=387, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=78431, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	11:14:10.001406-0500	tccd	AUTHREQ_SUBJECT: msgID=387.1696, subject=com.nexy.assistant,
default	11:14:10.002062-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x93ad32700 at /Applications/Nexy.app
default	11:14:10.005743-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	11:14:10.006983-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=399.703, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=78431, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	11:14:10.008063-0500	tccd	AUTHREQ_SUBJECT: msgID=399.703, subject=com.nexy.assistant,
default	11:14:10.008649-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb2ed5ed00 at /Applications/Nexy.app
default	11:14:10.028996-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=399.704, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=78431, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	11:14:10.030334-0500	Nexy	NotifyToken::RegisterDispatch(user.uid.501.com.apple.LaunchServices.database) fired for session key <private>
default	11:14:10.030525-0500	tccd	AUTHREQ_SUBJECT: msgID=399.704, subject=com.nexy.assistant,
default	11:14:10.031743-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb2ed5ed00 at /Applications/Nexy.app
default	11:14:10.045515-0500	Nexy	 [INFO] SLSHWCaptureDesktopProxying_block_invoke:506 request: <private>, error: (null), windowInfo: (null)
default	11:14:10.056601-0500	coreaudiod	>>> NEGOTIATE [com.nexy.assistant]
default	11:14:10.056725-0500	coreaudiod	<<< NEGOTIATE [com.nexy.assistant]
default	11:14:10.057364-0500	coreaudiod	>>> ADAPT [com.nexy.assistant]
default	11:14:10.057610-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xa2cf23000] Created node ADM::com.nexy.assistant_2302.2212.0_airpods noise suppression studio::in-0 with nodeID 0 - reporting period = 10.000000, sample rate = 24000.000000
default	11:14:10.057670-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xa2cf23000] Created node ADM::com.nexy.assistant_2302.2212.0_airpods noise suppression studio::out-0 with nodeID 1 - reporting period = 10.000000, sample rate = 24000.000000
default	11:14:10.104280-0500	Nexy	 [INFO] SLSHWCaptureDesktopProxying:485 request: <private>
default	11:14:10.104341-0500	Nexy	 [INFO] -[RPDaemonProxy proxyCoreGraphicsWithMethodType:config:machPort:completionHandler:]:1493
default	11:14:10.105634-0500	Nexy	[com.apple.controlcenter:3102C5D7-32AB-4033-A1B7-0E582F2556E7] Sending action(s) in update: NSSceneFenceAction
default	11:14:10.105954-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=96069.74, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=78431, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.replayd, pid=96069, auid=501, euid=501, binary_path=/usr/libexec/replayd}, },
default	11:14:10.105983-0500	tccd	requestor: TCCDProcess: identifier=com.apple.replayd, pid=96069, auid=501, euid=501, binary_path=/usr/libexec/replayd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=78431, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	11:14:10.107750-0500	tccd	AUTHREQ_SUBJECT: msgID=96069.74, subject=com.nexy.assistant,
default	11:14:10.109441-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x93ad32700 at /Applications/Nexy.app
default	11:14:10.129065-0500	coreaudiod	<<< ADAPT [com.nexy.assistant]
default	11:14:10.130261-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:2302 called from <private>
default	11:14:10.130305-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Input {1C-77-54-18-C8-A3:input, 0xa}
default	11:14:10.130307-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	11:14:10.131284-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2302 called from <private>
default	11:14:10.131552-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2302)
default	11:14:10.131571-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2302 called from <private>
default	11:14:10.131596-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2302 called from <private>
default	11:14:10.132424-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2301)
default	11:14:10.132441-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	11:14:10.134090-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2308)
default	11:14:10.134114-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2301 called from <private>
default	11:14:10.134198-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2308 called from <private>
default	11:14:10.134968-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	11:14:10.134207-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2301 called from <private>
default	11:14:10.136496-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	11:14:10.134321-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2308)
default	11:14:10.134443-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2308 called from <private>
default	11:14:10.134538-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2308 called from <private>
default	11:14:10.134567-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2308 called from <private>
default	11:14:10.139491-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2302)
default	11:14:10.139508-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2302)
default	11:14:10.139556-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2302)
default	11:14:10.139595-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2302)
default	11:14:10.139863-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2302 called from <private>
default	11:14:10.139904-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2302 called from <private>
default	11:14:10.134331-0500	runningboardd	Invalidating assertion 394-78431-35043 (target:[app<application.com.nexy.assistant.53053210.53053219(501)>:78431]) from originator [app<application.com.nexy.assistant.53053210.53053219(501)>:78431]
default	11:14:10.139978-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2302 called from <private>
default	11:14:10.140044-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2302 called from <private>
default	11:14:10.140124-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2302 called from <private>
default	11:14:10.140163-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2302 called from <private>
default	11:14:10.140198-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2302 called from <private>
default	11:14:10.143635-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2301 called from <private>
default	11:14:10.134913-0500	runningboardd	Invalidating assertion 394-328-35038 (target:[app<application.com.nexy.assistant.53053210.53053219(501)>:78431]) from originator [osservice<com.apple.powerd>:328]
default	11:14:10.143647-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2301 called from <private>
default	11:14:10.143776-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2301)
default	11:14:10.144017-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:2301 called from <private>
default	11:14:10.144182-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:2301 called from <private>
default	11:14:10.146615-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2301)
default	11:14:10.146785-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:2301 called from <private>
default	11:14:10.140846-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.53053210.53053219(501)>:78431] from originator [app<application.com.nexy.assistant.53053210.53053219(501)>:78431] with description <RBSAssertionDescriptor| "AudioHAL" ID:394-78431-35051 target:78431 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	11:14:10.141040-0500	runningboardd	Assertion 394-78431-35051 (target:[app<application.com.nexy.assistant.53053210.53053219(501)>:78431]) will be created as active
default	11:14:10.146894-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:2301 called from <private>
default	11:14:10.146970-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2301 called from <private>
default	11:14:10.147062-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2301 called from <private>
default	11:14:10.147603-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2301)
default	11:14:10.147671-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2301 called from <private>
error	11:14:10.148694-0500	Nexy	         HALC_ProxyIOContext.cpp:1075  HALC_ProxyIOContext::_StartIO(): Start failed - StartAndWaitForState returned error 35
default	11:14:10.148724-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2301 called from <private>
default	11:14:10.149720-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2301 called from <private>
default	11:14:10.149827-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2301 called from <private>
default	11:14:10.150033-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2301)
default	11:14:10.150129-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2301 called from <private>
default	11:14:10.150177-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2301 called from <private>
default	11:14:10.155194-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2301)
default	11:14:10.156563-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2301)
default	11:14:10.159471-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2301 called from <private>
default	11:14:10.159584-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2301 called from <private>
default	11:14:10.159728-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2301 called from <private>
default	11:14:10.142453-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=399.705, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=78431, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	11:14:10.160331-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2301)
default	11:14:10.160924-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2301)
error	11:14:10.165488-0500	Nexy	         HALC_ProxyIOContext.cpp:1075  HALC_ProxyIOContext::_StartIO(): Start failed - StartAndWaitForState returned error 35
default	11:14:10.165513-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2301 called from <private>
default	11:14:10.165524-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2301 called from <private>
default	11:14:10.165533-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2301 called from <private>
default	11:14:10.165539-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2301 called from <private>
default	11:14:10.165914-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2308)
default	11:14:10.165921-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2302)
error	11:14:10.166038-0500	Nexy	         HALC_ProxyIOContext.cpp:1075  HALC_ProxyIOContext::_StartIO(): Start failed - StartAndWaitForState returned error 35
default	11:14:10.166169-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2301 called from <private>
default	11:14:10.166253-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2301 called from <private>
default	11:14:10.166399-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2301 called from <private>
default	11:14:10.167221-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:2308 called from <private>
default	11:14:10.167247-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:2308 called from <private>
default	11:14:10.169308-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	11:14:10.167690-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2308)
default	11:14:10.169804-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	11:14:10.170816-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2308)
default	11:14:10.170834-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2308)
default	11:14:10.170844-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2308)
default	11:14:10.170852-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2308)
default	11:14:10.170861-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2308)
default	11:14:10.171205-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:2308 called from <private>
default	11:14:10.171215-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:2308 called from <private>
default	11:14:10.171240-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2308 called from <private>
default	11:14:10.171246-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2308 called from <private>
default	11:14:10.171251-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2308 called from <private>
default	11:14:10.171283-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2308 called from <private>
default	11:14:10.171359-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2308 called from <private>
default	11:14:10.171390-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2308 called from <private>
default	11:14:10.171447-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2308 called from <private>
default	11:14:10.171510-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2308 called from <private>
default	11:14:10.178751-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2301 called from <private>
default	11:14:10.178852-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2301 called from <private>
default	11:14:10.178909-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2301 called from <private>
default	11:14:10.178993-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2301 called from <private>
default	11:14:10.179135-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2301 called from <private>
default	11:14:10.192147-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0xb7470e340) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	11:14:10.192153-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	11:14:10.192323-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0xb7470e340) Device ID: 85 (Input:No | Output:Yes): true
default	11:14:10.192292-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 501, deviceID = <private>
default	11:14:10.192756-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 501 flag 0x1 < Hijack > app com.nexy.assistant CID 0x45550001 category Not set
default	11:14:10.192483-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0xb7470e340)
default	11:14:10.192713-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  24000 Hz, Float32, interleaved
default	11:14:10.192789-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	11:14:10.193336-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 201,
}
default	11:14:10.192895-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  24000 Hz, Float32, interleaved
default	11:14:10.193367-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	11:14:10.192969-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	11:14:10.193380-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 201
default	11:14:10.193228-0500	audiomxd	UpdateAudioState CID 0x45550001 audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	11:14:10.193270-0500	audiomxd	UpdateAudioState CID 0x45550001 audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	11:14:10.193078-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	11:14:10.194334-0500	audiomxd	UpdateAudioState CID 0x45550001 audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	11:14:10.194369-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 201,
}
default	11:14:10.194406-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	11:14:10.193519-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0xb748b5ef0, from  2 ch,  48000 Hz, Float32, deinterleaved to  2 ch,  24000 Hz, Float32, interleaved
default	11:14:10.194427-0500	audiomxd	UpdateAudioState CID 0x45550001 audioState Start apps {
    "com.nexy.assistant" : 501,
}
default	11:14:10.194427-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 201
default	11:14:10.193618-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	11:14:10.193731-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xa}
default	11:14:10.194453-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 201,
}
default	11:14:10.207525-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	11:14:10.207566-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 42, PID = 78431, Name = sid:0x1ee029, Nexy(78431), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = YES, Recording = YES>
default	11:14:10.207640-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1ee029, Nexy(78431), 'prim'', displayID:'com.nexy.assistant'}
default	11:14:10.206633-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 501
default	11:14:10.207765-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsPlaying:]: MXCoreSession com.nexy.assistant with category/mode Record_WithBluetooth/Default and coreSessionID = 42 stopping playing
default	11:14:10.206911-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 501 App com.nexy.assistant
default	11:14:10.207863-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 42, PID = 78431, Name = sid:0x1ee029, Nexy(78431), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	11:14:10.207914-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 200 flag 0x1 < Hijack > app com.nexy.assistant CID 0x45550001 category Not set
default	11:14:10.207983-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 42, PID = 78431, Name = sid:0x1ee029, Nexy(78431), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	11:14:10.208097-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1ee029, Nexy(78431), 'prim'', displayID:'com.nexy.assistant'}
default	11:14:10.208537-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [1, 0]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:input"
)}
default	11:14:10.208558-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	11:14:10.208369-0500	audiomxd	AudioApplicationInfoImpl.mm:395   Successfully updated session 0x1ee029 to isSessionRecording: 1
	app: {"name":"[implicit] Nexy","pid":78431}
	AudioApp.isRecording: true
[ 
	{ sessionID: 0x1ee029, sessionType: 'prim', isRecording: true }, 
]
default	11:14:10.209259-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 200 flag 0x1 < Hijack > app com.nexy.assistant CID 0x45550001 category Not set
default	11:14:10.232039-0500	Nexy	 [INFO] SLSHWCaptureDesktopProxying_block_invoke:506 request: <private>, error: (null), windowInfo: (null)
default	11:14:10.240567-0500	gamepolicyd	Received state update for 78431 (app<application.com.nexy.assistant.53053210.53053219(501)>, running-active-NotVisible
default	11:14:10.242338-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:14:10.242356-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:14:10.242369-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	11:14:10.242378-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:14:10.242388-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	11:14:10.242396-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	11:14:10.242506-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	11:14:10.261322-0500	coreaudiod	>>> NEGOTIATE [com.nexy.assistant]
default	11:14:10.261518-0500	coreaudiod	<<< NEGOTIATE [com.nexy.assistant]
default	11:14:10.264015-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:2302 called from <private>
default	11:14:10.264092-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	11:14:10.266159-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2302 called from <private>
error	11:14:10.266191-0500	Nexy	         HALC_ProxyIOContext.cpp:1075  HALC_ProxyIOContext::_StartIO(): Start failed - StartAndWaitForState returned error 89
default	11:14:10.266206-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2302 called from <private>
default	11:14:10.264913-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.53053210.53053219(501)>:78431] from originator [osservice<com.apple.powerd>:328] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:394-328-35055 target:78431 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	11:14:10.265047-0500	runningboardd	Assertion 394-328-35055 (target:[app<application.com.nexy.assistant.53053210.53053219(501)>:78431]) will be created as active
default	11:14:10.268845-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2302 called from <private>
default	11:14:10.269311-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2302 called from <private>
default	11:14:10.269496-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2302 called from <private>
default	11:14:10.269546-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2302 called from <private>
default	11:14:10.279973-0500	tccd	AUTHREQ_SUBJECT: msgID=399.706, subject=com.nexy.assistant,
default	11:14:10.280908-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb2ed5ed00 at /Applications/Nexy.app
default	11:14:10.282726-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	11:14:10.289813-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	11:14:10.289913-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant), [mic] Nexy (com.nexy.assistant)]
default	11:14:10.289974-0500	ControlCenter	Active activity attributions changed to ["scr:com.nexy.assistant", "mic:com.nexy.assistant"]
default	11:14:10.290661-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:14:10.290687-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:14:10.290702-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	11:14:10.290712-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:14:10.290721-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	11:14:10.290730-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	11:14:10.290751-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:14:10.290765-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:14:10.290775-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	11:14:10.290783-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:14:10.290791-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	11:14:10.290800-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	11:14:10.290843-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:14:10.290873-0500	ControlCenter	Navigating to new application [com.nexy.assistant]
default	11:14:10.290867-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:14:10.290921-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	11:14:10.290951-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:14:10.291071-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	11:14:10.291209-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	11:14:10.291296-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	11:14:10.302421-0500	ControlCenter	Active activity attributions changed to ["scr:com.nexy.assistant"]
default	11:14:10.302443-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	11:14:10.317329-0500	Nexy	         AVAudioEngine.mm:1437  Engine@0xb709c4650: iounit configuration changed > posting notification
default	11:14:10.350028-0500	gamepolicyd	Received state update for 78431 (app<application.com.nexy.assistant.53053210.53053219(501)>, running-active-NotVisible
default	11:14:10.363708-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xa2cf23000] Created node ADM::com.nexy.assistant_2302.2212.0_airpods noise suppression studio::in-0 with nodeID 0 - reporting period = 10.000000, sample rate = 24000.000000
default	11:14:10.363831-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xa2cf23000] Created node ADM::com.nexy.assistant_2302.2212.0_airpods noise suppression studio::out-0 with nodeID 1 - reporting period = 10.000000, sample rate = 24000.000000
default	11:14:10.418160-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.53053210.53053219(501)>:78431] from originator [osservice<com.apple.powerd>:328] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:394-328-35058 target:78431 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	11:14:10.418546-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:2302 called from <private>
default	11:14:10.418692-0500	runningboardd	Assertion 394-328-35058 (target:[app<application.com.nexy.assistant.53053210.53053219(501)>:78431]) will be created as active
default	11:14:10.418601-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:2302 called from <private>
default	11:14:10.419035-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78431] Ignoring jetsam update because this process is not memory-managed
default	11:14:10.419127-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78431] Ignoring suspend because this process is not lifecycle managed
default	11:14:10.419163-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78431] Ignoring GPU update because this process is not GPU managed
default	11:14:10.419215-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:2302 called from <private>
default	11:14:10.419320-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	11:14:10.419270-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78431] Ignoring memory limit update because this process is not memory-managed
default	11:14:10.419945-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2302 called from <private>
default	11:14:10.420110-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2302)
default	11:14:10.420129-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2302 called from <private>
default	11:14:10.420136-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2302 called from <private>
default	11:14:10.420269-0500	runningboardd	Invalidating assertion 394-78431-35057 (target:[app<application.com.nexy.assistant.53053210.53053219(501)>:78431]) from originator [app<application.com.nexy.assistant.53053210.53053219(501)>:78431]
default	11:14:10.425743-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=399.707, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=78431, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	11:14:10.426286-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.53053210.53053219(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	11:14:10.426702-0500	runningboardd	Invalidating assertion 394-328-35058 (target:[app<application.com.nexy.assistant.53053210.53053219(501)>:78431]) from originator [osservice<com.apple.powerd>:328]
default	11:14:10.436722-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	11:14:10.467720-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:2302 called from <private>
default	11:14:10.484431-0500	ControlCenter	Received state update for 78431 (app<application.com.nexy.assistant.53053210.53053219(501)>, running-active-NotVisible
default	11:14:10.485814-0500	gamepolicyd	Received state update for 78431 (app<application.com.nexy.assistant.53053210.53053219(501)>, running-active-NotVisible
default	11:14:13.576157-0500	Nexy	LSExceptions shared instance invalidated for timeout.
default	11:14:14.337897-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xa}
default	11:14:14.338463-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ee029","name":"Nexy(78431)"}, "details":{"deviceUIDs":[],"implicit_category":"","input_running":false,"output_running":false} }
default	11:14:14.338608-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 42, PID = 78431, Name = sid:0x1ee029, Nexy(78431), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	11:14:14.338675-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 42, PID = 78431, Name = sid:0x1ee029, Nexy(78431), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	11:14:14.338711-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found 2 different sessions firstSession={clientName:'sid:0x1ee003, Browser Helper(1622), 'prim'', displayID:'company.thebrowser.browser.helper'}, secondSession={clientName:'sid:0x1ee029, Nexy(78431), 'prim'', displayID:'com.nexy.assistant'} but will use session={clientName:'(null)', displayID:'(null)'}
default	11:14:14.338751-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	11:14:14.338763-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1ee029, Nexy(78431), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 42 stopping recording
default	11:14:14.338799-0500	audiomxd	-MXCoreSession- -[MXCoreSession endInterruption:]: Session <ID: 42, PID = 78431, Name = sid:0x1ee029, Nexy(78431), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> is going inactive
default	11:14:14.338824-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 42, PID = 78431, Name = sid:0x1ee029, Nexy(78431), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	11:14:14.338851-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 42, PID = 78431, Name = sid:0x1ee029, Nexy(78431), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	11:14:14.339031-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 0]. BT device UIDS: {(
)}
default	11:14:14.339042-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	11:14:14.339103-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 200 flag 0x1 < Hijack > app com.nexy.assistant CID 0x45550001 category Not set
default	11:14:14.339386-0500	audiomxd	UpdateAudioState CID 0x45550001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	11:14:14.339490-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	11:14:14.339438-0500	audiomxd	UpdateAudioState CID 0x45550001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	11:14:14.339524-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	11:14:14.339555-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	11:14:14.340471-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	11:14:14.340668-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	11:14:14.340686-0500	audioaccessoryd	AudioStateChanged: Removed audio session app com.nexy.assistant 201 count 2
default	11:14:14.340919-0500	runningboardd	Invalidating assertion 394-78431-35059 (target:[app<application.com.nexy.assistant.53053210.53053219(501)>:78431]) from originator [app<application.com.nexy.assistant.53053210.53053219(501)>:78431]
default	11:14:14.341047-0500	runningboardd	Invalidating assertion 394-328-35060 (target:[app<application.com.nexy.assistant.53053210.53053219(501)>:78431]) from originator [osservice<com.apple.powerd>:328]
default	11:14:14.351136-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	11:14:14.351252-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant)]
default	11:14:14.351321-0500	ControlCenter	Active activity attributions changed to ["scr:com.nexy.assistant"]
default	11:14:14.351342-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	11:14:14.351978-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:14:14.351990-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:14:14.352004-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	11:14:14.352010-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:14:14.352019-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	11:14:14.352025-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	11:14:14.352128-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	11:14:14.357403-0500	Nexy	nw_path_libinfo_path_check [1F87BD3C-361B-4204-988C-4EA60749A507 Hostname#12f36931:80 tcp, legacy-socket, attribution: developer]
	libinfo check path: <private>
default	11:14:14.357863-0500	mDNSResponder	[R45780] DNSServiceCreateConnection START PID[78431](Nexy)
default	11:14:14.358362-0500	mDNSResponder	[R45781] DNSServiceQueryRecord START -- qname: <mask.hash: '9CUYq7voeSCipiFnH0GIVQ=='>, qtype: A, flags: 0x1D000, interface index: 0, client pid: 78431 (Nexy), name hash: b360ab20
default	11:14:14.359220-0500	mDNSResponder	[R45782] DNSServiceQueryRecord START -- qname: <mask.hash: '9CUYq7voeSCipiFnH0GIVQ=='>, qtype: AAAA, flags: 0x1D000, interface index: 0, client pid: 78431 (Nexy), name hash: b360ab20
default	11:14:14.370183-0500	kernel	SK[9]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid D160587C-DC51-4A97-81E2-9F7EF92C0270 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.54695,dst=<IPv4-redacted>.80,proto=0x06 mask=0x0000003f,hash=0xbce3bffd tp_proto=0x06"
default	11:14:14.370295-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:54695<-><IPv4-redacted>:80] interface: en0 (skipped: 0)
so_gencnt: 718495 t_state: SYN_SENT process: Nexy:78431 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x915c26cb
default	11:14:14.375643-0500	kernel	tcp connected: [<IPv4-redacted>:54695<-><IPv4-redacted>:80] interface: en0 (skipped: 0)
so_gencnt: 718495 t_state: ESTABLISHED process: Nexy:78431 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x915c26cb
default	11:14:14.442411-0500	Nexy	                AUHAL.cpp:473   ~AUHAL: (0xb74880e40) Selecting device 0 from destructor
default	11:14:14.442425-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0xb74880e40)
default	11:14:14.442434-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0xb74880e40) not already running
default	11:14:14.442440-0500	Nexy	                AUHAL.cpp:687   SelectDevice: (0xb74880e40) disconnecting device 91
default	11:14:14.442446-0500	Nexy	                AUHAL.cpp:751   SelectDevice: (0xb74880e40) destroying ioproc 0xa for device 91
default	11:14:14.442488-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xa}
default	11:14:14.442527-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	11:14:14.442691-0500	Nexy	                AUHAL.cpp:853   SelectDevice: (0xb74880e40) nothing to setup
default	11:14:14.442702-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0xb74880e40) adding 0 device listeners to device 0
default	11:14:14.442707-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0xb74880e40) adding 0 device delegate listeners to device 0
default	11:14:14.442714-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0xb74880e40) removing 7 device listeners from device 91
default	11:14:14.442923-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0xb74880e40) removing 0 device delegate listeners from device 91
default	11:14:14.442939-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0xb74880e40)
default	11:14:14.447547-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78431] Ignoring jetsam update because this process is not memory-managed
default	11:14:14.447567-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78431] Ignoring suspend because this process is not lifecycle managed
default	11:14:14.447577-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78431] Ignoring GPU update because this process is not GPU managed
default	11:14:14.447613-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78431] Ignoring memory limit update because this process is not memory-managed
default	11:14:14.450752-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.53053210.53053219(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	11:14:14.451437-0500	ControlCenter	Received state update for 78431 (app<application.com.nexy.assistant.53053210.53053219(501)>, running-active-NotVisible
default	11:14:14.451708-0500	gamepolicyd	Received state update for 78431 (app<application.com.nexy.assistant.53053210.53053219(501)>, running-active-NotVisible
default	11:14:14.496834-0500	Nexy	[com.apple.controlcenter:3102C5D7-32AB-4033-A1B7-0E582F2556E7] Sending action(s) in update: NSSceneFenceAction
default	11:14:15.182147-0500	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:54695<-><IPv4-redacted>:80] interface: en0 (skipped: 0)
so_gencnt: 718495 t_state: FIN_WAIT_1 process: Nexy:78431 Duration: 0.813 sec Conn_Time: 0.006 sec bytes in/out: 827/107770 pkts in/out: 3/24 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 7.500 ms rttvar: 2.062 ms base rtt: 5 ms so_error: 0 svc/tc: 0 flow: 0x915c26cb
default	11:14:15.182169-0500	kernel	tcp_connection_summary [<IPv4-redacted>:54695<-><IPv4-redacted>:80] interface: en0 (skipped: 0)
so_gencnt: 718495 t_state: FIN_WAIT_1 process: Nexy:78431 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	11:14:16.470413-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2308)
default	11:14:16.470488-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2308 called from <private>
default	11:14:16.470504-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2308 called from <private>
default	11:14:16.473134-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2308)
default	11:14:16.473161-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2302)
default	11:14:16.473184-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2308 called from <private>
default	11:14:16.473195-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2308 called from <private>
default	11:14:16.473189-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2302 called from <private>
default	11:14:16.473208-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2302 called from <private>
default	11:14:16.474417-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2301)
default	11:14:16.474946-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2301 called from <private>
default	11:14:16.474997-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2301 called from <private>
default	11:14:16.490168-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2301 called from <private>
default	11:14:16.490199-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2301 called from <private>
default	11:14:16.490448-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2308)
default	11:14:16.490474-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2302)
default	11:14:16.490489-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2302 called from <private>
default	11:14:16.490495-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2302 called from <private>
default	11:14:16.490967-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2301)
default	11:14:16.491030-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:2301 called from <private>
default	11:14:16.491518-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:2301 called from <private>
default	11:14:16.495373-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2301)
default	11:14:16.495663-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:2301 called from <private>
default	11:14:16.495873-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2301)
default	11:14:16.496066-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:2301 called from <private>
default	11:14:16.496196-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:2308 called from <private>
default	11:14:16.496304-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2301 called from <private>
default	11:14:16.496357-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:2308 called from <private>
default	11:14:16.496398-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2301 called from <private>
default	11:14:16.496193-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2301)
default	11:14:16.496469-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2301 called from <private>
default	11:14:16.496540-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2301 called from <private>
default	11:14:16.496571-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2301 called from <private>
default	11:14:16.496612-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2301 called from <private>
default	11:14:16.496622-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2308)
default	11:14:16.497044-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2301 called from <private>
default	11:14:16.497200-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2301 called from <private>
default	11:14:16.497504-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2301)
default	11:14:16.497684-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:2301 called from <private>
default	11:14:16.497935-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:2301 called from <private>
default	11:14:16.499000-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2301)
default	11:14:16.499232-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:2301 called from <private>
default	11:14:16.499245-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:2301 called from <private>
default	11:14:16.499265-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2301 called from <private>
default	11:14:16.499275-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2301 called from <private>
default	11:14:16.499691-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	11:14:16.499902-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	11:14:16.500560-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2308)
default	11:14:16.500601-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2301)
default	11:14:16.500602-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2308)
default	11:14:16.500618-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2308)
default	11:14:16.500622-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2301)
default	11:14:16.500632-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2308)
default	11:14:16.500628-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2301 called from <private>
default	11:14:16.500643-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2301 called from <private>
default	11:14:16.500653-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2308)
default	11:14:16.500653-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2301 called from <private>
default	11:14:16.500680-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2301 called from <private>
default	11:14:16.500844-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:2308 called from <private>
default	11:14:16.500859-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:2308 called from <private>
default	11:14:16.500902-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2308 called from <private>
default	11:14:16.500914-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2308 called from <private>
default	11:14:16.500922-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2308 called from <private>
default	11:14:16.500930-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2308 called from <private>
default	11:14:16.500936-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2308 called from <private>
default	11:14:16.500941-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2308 called from <private>
default	11:14:16.500950-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2308 called from <private>
default	11:14:16.500956-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2308 called from <private>
default	11:14:16.500962-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2308 called from <private>
default	11:14:16.500967-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2308 called from <private>
default	11:14:16.500972-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2308 called from <private>
default	11:14:16.500977-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2308 called from <private>
default	11:14:16.500982-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:2308 called from <private>
default	11:14:16.501005-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:2308 called from <private>
default	11:14:16.512845-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2301 called from <private>
default	11:14:16.512878-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2301 called from <private>
default	11:14:16.513021-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(2301)
default	11:14:16.515593-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(2301)
default	11:14:16.516040-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2301 called from <private>
default	11:14:16.516056-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2301 called from <private>
default	11:14:16.516109-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:2301 called from <private>
default	11:14:16.516122-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:2301 called from <private>
default	11:14:16.516129-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:2301 called from <private>
default	11:14:16.516134-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:2301 called from <private>
default	11:14:16.517290-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0xb7470e340) Device ID: 85 (Input:No | Output:Yes): true
default	11:14:16.517319-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0xb7470e340)
default	11:14:16.518328-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  48000 Hz, Float32, interleaved
default	11:14:16.518361-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	11:14:16.518371-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	11:14:16.518388-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	11:14:16.518400-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	11:14:16.518851-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0xb7470e340) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	11:14:16.518884-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0xb7470e340) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	11:14:16.525144-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:2301 called from <private>
default	11:14:16.525403-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2308 called from <private>
default	11:14:16.526217-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:2301 called from <private>
default	11:14:16.526990-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0xb7470e340) Device ID: 85 (Input:No | Output:Yes): true
default	11:14:16.527101-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0xb7470e340)
default	11:14:16.530674-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  48000 Hz, Float32, interleaved
default	11:14:16.530719-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	11:14:16.530728-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	11:14:16.530740-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	11:14:16.638204-0500	Nexy	         AVAudioEngine.mm:1437  Engine@0xb709c4650: iounit configuration changed > posting notification
default	11:14:18.135684-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0xb72848660, from  2 ch,  48000 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	11:14:18.135716-0500	Nexy	       AudioConverter.cpp:1317  AudioConverter -> 0xb72848660: The in-process GetProperty call returned 1886547824 for property 1886546285 with size 8.
default	11:14:18.135736-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	11:14:18.135741-0500	Nexy	AudioConverter -> 0xb72848660: The in-process SetProperty call returned 1886547824 for property 1936876385 with size 4.
default	11:14:18.135766-0500	Nexy	AudioConverter -> 0xb72848660: The in-process SetProperty call returned 1886547824 for property 1936876401 with size 4.
default	11:14:18.135777-0500	Nexy	AudioConverter -> 0xb72848660: The in-process SetProperty call returned 1886547824 for property 1886547309 with size 4.
default	11:14:18.136394-0500	Nexy	       AudioConverter.cpp:1317  AudioConverter -> 0xb72848660: The in-process GetProperty call returned 1886547824 for property 1886546285 with size 8.
default	11:14:18.136444-0500	Nexy	         AVAudioEngine.mm:1182  Engine@0xb709c4650: start, was running 0
default	11:14:18.138988-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.53053210.53053219(501)>:78431] from originator [app<application.com.nexy.assistant.53053210.53053219(501)>:78431] with description <RBSAssertionDescriptor| "AudioHAL" ID:394-78431-35067 target:78431 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	11:14:18.139142-0500	runningboardd	Assertion 394-78431-35067 (target:[app<application.com.nexy.assistant.53053210.53053219(501)>:78431]) will be created as active
default	11:14:18.139992-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78431] Ignoring jetsam update because this process is not memory-managed
default	11:14:18.140095-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78431] Ignoring suspend because this process is not lifecycle managed
default	11:14:18.139993-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.53053210.53053219(501)>:78431] from originator [osservice<com.apple.powerd>:328] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:394-328-35068 target:78431 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	11:14:18.140186-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78431] Ignoring GPU update because this process is not GPU managed
default	11:14:18.140288-0500	runningboardd	Assertion 394-328-35068 (target:[app<application.com.nexy.assistant.53053210.53053219(501)>:78431]) will be created as active
default	11:14:18.140343-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78431] Ignoring memory limit update because this process is not memory-managed
default	11:14:18.144134-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.53053210.53053219(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	11:14:18.144514-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78431] Ignoring jetsam update because this process is not memory-managed
default	11:14:18.144566-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78431] Ignoring suspend because this process is not lifecycle managed
default	11:14:18.144601-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78431] Ignoring GPU update because this process is not GPU managed
default	11:14:18.144665-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78431] Ignoring memory limit update because this process is not memory-managed
default	11:14:18.144776-0500	ControlCenter	Received state update for 78431 (app<application.com.nexy.assistant.53053210.53053219(501)>, running-active-NotVisible
default	11:14:18.145942-0500	gamepolicyd	Received state update for 78431 (app<application.com.nexy.assistant.53053210.53053219(501)>, running-active-NotVisible
default	11:14:18.147730-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.53053210.53053219(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	11:14:18.148219-0500	ControlCenter	Received state update for 78431 (app<application.com.nexy.assistant.53053210.53053219(501)>, running-active-NotVisible
default	11:14:18.148391-0500	gamepolicyd	Received state update for 78431 (app<application.com.nexy.assistant.53053210.53053219(501)>, running-active-NotVisible
default	11:14:18.179893-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xa}
default	11:14:18.180644-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ee029","name":"Nexy(78431)"}, "details":{"deviceUIDs":["1C-77-54-18-C8-A3:output"],"implicit_category":"MediaPlayback","input_running":false,"output_running":true} }
default	11:14:18.180743-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 42, PID = 78431, Name = sid:0x1ee029, Nexy(78431), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	11:14:18.180773-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Category/Mode changed -- The score for sid:0x1ee029, Nexy(78431), 'prim'/com.nexy.assistant was not correct. Old score = 201
default	11:14:18.180804-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 42, PID = 78431, Name = sid:0x1ee029, Nexy(78431), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	11:14:18.180845-0500	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1ee029, Nexy(78431), 'prim'', AudioCategory changed to 'MediaPlayback'
default	11:14:18.180866-0500	audiomxd	UpdateAudioState CID 0x45550001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	11:14:18.180892-0500	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 42, PID = 78431, Name = sid:0x1ee029, Nexy(78431), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO> is going active
default	11:14:18.180903-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsPlaying:]: MXCoreSession com.nexy.assistant with category/mode MediaPlayback/Default and coreSessionID = 42 starting playing
default	11:14:18.180951-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 42, PID = 78431, Name = sid:0x1ee029, Nexy(78431), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	11:14:18.180982-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	11:14:18.180984-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 42, PID = 78431, Name = sid:0x1ee029, Nexy(78431), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO>
default	11:14:18.181018-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	11:14:18.181009-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found 2 different sessions firstSession={clientName:'sid:0x1ee003, Browser Helper(1622), 'prim'', displayID:'company.thebrowser.browser.helper'}, secondSession={clientName:'sid:0x1ee029, Nexy(78431), 'prim'', displayID:'com.nexy.assistant'} but will use session={clientName:'(null)', displayID:'(null)'}
default	11:14:18.181046-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 201, deviceID = <private>
default	11:14:18.181185-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 1]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)}
default	11:14:18.181085-0500	audiomxd	AudioApplicationInfoImpl.mm:395   Successfully updated session 0x1ee029 to isSessionRecording: 0
	app: {"name":"[implicit] Nexy","pid":78431}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1ee029, sessionType: 'prim', isRecording: false }, 
]
default	11:14:18.181197-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	11:14:18.181263-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 201 flag 0x1 < Hijack > app com.nexy.assistant CID 0x45550001 category Not set
default	11:14:18.181425-0500	audiomxd	UpdateAudioState CID 0x45550001 audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	11:14:18.181495-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 201,
}
default	11:14:18.181524-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	11:14:18.181539-0500	audioaccessoryd	AudioStateChanged: Added audio session app com.nexy.assistant NULL -> 201 count 3
default	11:14:18.181549-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 201
default	11:14:18.553085-0500	Nexy	nw_path_libinfo_path_check [9AB8B91F-4053-434A-B23A-359E9BB5E3C9 Hostname#91364e9d:443 tcp, legacy-socket, attribution: developer]
	libinfo check path: <private>
default	11:14:18.553241-0500	mDNSResponder	[R45786] DNSServiceQueryRecord START -- qname: <mask.hash: '17YxnKTijmLfapDTa1I9Ag=='>, qtype: A, flags: 0x1D000, interface index: 0, client pid: 78431 (Nexy), name hash: 17e34662
default	11:14:18.554095-0500	mDNSResponder	[R45787] DNSServiceQueryRecord START -- qname: <mask.hash: '17YxnKTijmLfapDTa1I9Ag=='>, qtype: AAAA, flags: 0x1D000, interface index: 0, client pid: 78431 (Nexy), name hash: 17e34662
default	11:14:18.565524-0500	kernel	SK[7]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 06A8CDF6-6DC1-471A-9C01-1CA8D9E848BD flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.54698,dst=<IPv4-redacted>.443,proto=0x06 mask=0x0000003f,hash=0xf5ec1006 tp_proto=0x06"
default	11:14:18.565589-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:54698<-><IPv4-redacted>:443] interface: en0 (skipped: 0)
so_gencnt: 718572 t_state: SYN_SENT process: Nexy:78431 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xb66ad091
default	11:14:18.571146-0500	kernel	tcp connected: [<IPv4-redacted>:54698<-><IPv4-redacted>:443] interface: en0 (skipped: 0)
so_gencnt: 718572 t_state: ESTABLISHED process: Nexy:78431 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xb66ad091
default	11:14:18.602221-0500	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:54698<-><IPv4-redacted>:443] interface: en0 (skipped: 0)
so_gencnt: 718572 t_state: FIN_WAIT_1 process: Nexy:78431 Duration: 0.037 sec Conn_Time: 0.006 sec bytes in/out: 45876/766 pkts in/out: 6/3 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 6.625 ms rttvar: 2.562 ms base rtt: 6 ms so_error: 0 svc/tc: 0 flow: 0xb66ad091
default	11:14:18.602235-0500	kernel	tcp_connection_summary [<IPv4-redacted>:54698<-><IPv4-redacted>:443] interface: en0 (skipped: 0)
so_gencnt: 718572 t_state: FIN_WAIT_1 process: Nexy:78431 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	11:14:18.871570-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=489.36, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=78431, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.syspolicyd, pid=489, auid=0, euid=0, binary_path=/usr/libexec/syspolicyd}, },
default	11:14:18.873011-0500	tccd	AUTHREQ_SUBJECT: msgID=489.36, subject=com.nexy.assistant,
default	11:14:18.873924-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x93ad32700 at /Applications/Nexy.app
default	11:14:22.720464-0500	ControlCenter	Recent activity attributions changed to ["scr:com.nexy.assistant", "mic:com.nexy.assistant"]
default	11:14:22.721700-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:14:22.721726-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:14:22.721750-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	11:14:22.721767-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:14:22.721784-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	11:14:22.721800-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	11:14:22.722069-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	11:14:24.838814-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=78457.1, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=78431, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.google.Chrome, pid=78457, auid=501, euid=501, binary_path=/Applications/Google Chrome.app/Contents/MacOS/Google Chrome}, },
default	11:14:24.840662-0500	tccd	AUTHREQ_SUBJECT: msgID=78457.1, subject=com.nexy.assistant,
default	11:14:24.841702-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x93ad32700 at /Applications/Nexy.app
default	11:14:24.865607-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=387.1698, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=78431, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.google.Chrome, pid=78457, auid=501, euid=501, binary_path=/Applications/Google Chrome.app/Contents/MacOS/Google Chrome}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=387, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	11:14:24.866611-0500	tccd	AUTHREQ_SUBJECT: msgID=387.1698, subject=com.nexy.assistant,
default	11:14:24.867275-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x93ad32700 at /Applications/Nexy.app
default	11:14:24.925228-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=78272.14, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=78431, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.google.Chrome, pid=78457, auid=501, euid=501, binary_path=/Applications/Google Chrome.app/Contents/MacOS/Google Chrome}, requesting={TCCDProcess: identifier=com.apple.sandboxd, pid=78272, auid=0, euid=0, binary_path=/usr/libexec/sandboxd}, },
default	11:14:24.935080-0500	tccd	AUTHREQ_SUBJECT: msgID=78272.14, subject=com.nexy.assistant,
default	11:14:24.938633-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x93ad32700 at /Applications/Nexy.app
default	11:14:25.273693-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=78457.2, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=78431, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.google.Chrome, pid=78457, auid=501, euid=501, binary_path=/Applications/Google Chrome.app/Contents/MacOS/Google Chrome}, },
default	11:14:25.281203-0500	tccd	AUTHREQ_SUBJECT: msgID=78457.2, subject=com.nexy.assistant,
default	11:14:25.282270-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb2ed5de00 at /Applications/Nexy.app
default	11:14:25.304124-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=78457.3, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=78431, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.google.Chrome, pid=78457, auid=501, euid=501, binary_path=/Applications/Google Chrome.app/Contents/MacOS/Google Chrome}, },
default	11:14:25.305383-0500	tccd	AUTHREQ_SUBJECT: msgID=78457.3, subject=com.nexy.assistant,
default	11:14:25.306087-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb2ed5de00 at /Applications/Nexy.app
error	11:14:25.320882-0500	tccd	Prompting policy for hardened runtime; service: kTCCServiceCamera requires entitlement com.apple.security.device.camera but it is missing for responsible={TCCDProcess: identifier=com.nexy.assistant, pid=78431, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.google.Chrome, pid=78457, auid=501, euid=501, binary_path=/Applications/Google Chrome.app/Contents/MacOS/Google Chrome},
default	11:14:25.321732-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=78457.4, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=78431, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.google.Chrome, pid=78457, auid=501, euid=501, binary_path=/Applications/Google Chrome.app/Contents/MacOS/Google Chrome}, },
default	11:14:25.322981-0500	tccd	AUTHREQ_SUBJECT: msgID=78457.4, subject=com.nexy.assistant,
default	11:14:25.323673-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb2ed5de00 at /Applications/Nexy.app
error	11:14:25.338628-0500	tccd	Prompting policy for hardened runtime; service: kTCCServiceCamera requires entitlement com.apple.security.device.camera but it is missing for responsible={TCCDProcess: identifier=com.nexy.assistant, pid=78431, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.google.Chrome, pid=78457, auid=501, euid=501, binary_path=/Applications/Google Chrome.app/Contents/MacOS/Google Chrome},
default	11:14:25.339865-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=78457.5, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=78431, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.google.Chrome, pid=78457, auid=501, euid=501, binary_path=/Applications/Google Chrome.app/Contents/MacOS/Google Chrome}, },
default	11:14:25.341080-0500	tccd	AUTHREQ_SUBJECT: msgID=78457.5, subject=com.nexy.assistant,
default	11:14:25.341834-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x93ad33600 at /Applications/Nexy.app
default	11:14:25.775227-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=78473.1, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=78431, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.google.Chrome.framework.AlertNotificationService, pid=78473, auid=501, euid=501, binary_path=/Applications/Google Chrome.app/Contents/Frameworks/Google Chrome Framework.framework/Versions/144.0.7559.133/Helpers/Google Chrome Helper (Alerts).app/Contents/MacOS/Google Chrome Helper (Alerts)}, },
default	11:14:25.777821-0500	tccd	AUTHREQ_SUBJECT: msgID=78473.1, subject=com.nexy.assistant,
default	11:14:25.778985-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x93ad33600 at /Applications/Nexy.app
default	11:14:25.820446-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=78457.6, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=78431, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.google.Chrome, pid=78457, auid=501, euid=501, binary_path=/Applications/Google Chrome.app/Contents/MacOS/Google Chrome}, },
default	11:14:25.822227-0500	tccd	AUTHREQ_SUBJECT: msgID=78457.6, subject=com.nexy.assistant,
default	11:14:25.823023-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb2ed5de00 at /Applications/Nexy.app
error	11:14:25.840279-0500	tccd	Prompting policy for hardened runtime; service: kTCCServiceCamera requires entitlement com.apple.security.device.camera but it is missing for responsible={TCCDProcess: identifier=com.nexy.assistant, pid=78431, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.google.Chrome, pid=78457, auid=501, euid=501, binary_path=/Applications/Google Chrome.app/Contents/MacOS/Google Chrome},
default	11:14:25.841367-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=78457.7, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=78431, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.google.Chrome, pid=78457, auid=501, euid=501, binary_path=/Applications/Google Chrome.app/Contents/MacOS/Google Chrome}, },
default	11:14:25.842792-0500	tccd	AUTHREQ_SUBJECT: msgID=78457.7, subject=com.nexy.assistant,
default	11:14:25.843552-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=387.1700, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=78431, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.google.Chrome.framework.AlertNotificationService, pid=78473, auid=501, euid=501, binary_path=/Applications/Google Chrome.app/Contents/Frameworks/Google Chrome Framework.framework/Versions/144.0.7559.133/Helpers/Google Chrome Helper (Alerts).app/Contents/MacOS/Google Chrome Helper (Alerts)}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=387, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	11:14:25.843807-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb2ed5de00 at /Applications/Nexy.app
default	11:14:25.845006-0500	tccd	AUTHREQ_SUBJECT: msgID=387.1700, subject=com.nexy.assistant,
default	11:14:25.846179-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x93ad33600 at /Applications/Nexy.app
error	11:14:25.860133-0500	tccd	Prompting policy for hardened runtime; service: kTCCServiceCamera requires entitlement com.apple.security.device.camera but it is missing for responsible={TCCDProcess: identifier=com.nexy.assistant, pid=78431, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.google.Chrome, pid=78457, auid=501, euid=501, binary_path=/Applications/Google Chrome.app/Contents/MacOS/Google Chrome},
default	11:14:25.861552-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=78457.8, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=78431, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.google.Chrome, pid=78457, auid=501, euid=501, binary_path=/Applications/Google Chrome.app/Contents/MacOS/Google Chrome}, },
default	11:14:25.862721-0500	tccd	AUTHREQ_SUBJECT: msgID=78457.8, subject=com.nexy.assistant,
default	11:14:25.863390-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb2ed5de00 at /Applications/Nexy.app
error	11:14:25.880824-0500	tccd	Prompting policy for hardened runtime; service: kTCCServiceCamera requires entitlement com.apple.security.device.camera but it is missing for responsible={TCCDProcess: identifier=com.nexy.assistant, pid=78431, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.google.Chrome, pid=78457, auid=501, euid=501, binary_path=/Applications/Google Chrome.app/Contents/MacOS/Google Chrome},
default	11:14:25.881664-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=78457.9, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=78431, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.google.Chrome, pid=78457, auid=501, euid=501, binary_path=/Applications/Google Chrome.app/Contents/MacOS/Google Chrome}, },
default	11:14:25.882846-0500	tccd	AUTHREQ_SUBJECT: msgID=78457.9, subject=com.nexy.assistant,
default	11:14:25.883512-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb2ed5de00 at /Applications/Nexy.app
error	11:14:25.900224-0500	tccd	Prompting policy for hardened runtime; service: kTCCServiceCamera requires entitlement com.apple.security.device.camera but it is missing for responsible={TCCDProcess: identifier=com.nexy.assistant, pid=78431, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.google.Chrome, pid=78457, auid=501, euid=501, binary_path=/Applications/Google Chrome.app/Contents/MacOS/Google Chrome},
default	11:14:25.901458-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=78457.10, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=78431, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.google.Chrome, pid=78457, auid=501, euid=501, binary_path=/Applications/Google Chrome.app/Contents/MacOS/Google Chrome}, },
default	11:14:25.903475-0500	tccd	AUTHREQ_SUBJECT: msgID=78457.10, subject=com.nexy.assistant,
default	11:14:25.904795-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb2ed5de00 at /Applications/Nexy.app
default	11:14:26.217849-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 201
default	11:14:26.242433-0500	Nexy	NotifyToken::RegisterDispatch(user.uid.501.com.apple.LaunchServices.database) fired for session key <private>
default	11:14:26.260128-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=387.1701, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=78431, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.google.Chrome.helper, pid=78470, auid=501, euid=501, binary_path=/Applications/Google Chrome.app/Contents/Frameworks/Google Chrome Framework.framework/Versions/144.0.7559.133/Helpers/Google Chrome Helper.app/Contents/MacOS/Google Chrome Helper}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=387, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	11:14:26.265106-0500	tccd	AUTHREQ_SUBJECT: msgID=387.1701, subject=com.nexy.assistant,
default	11:14:26.267352-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x93ad31e00 at /Applications/Nexy.app
default	11:14:26.335917-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x93ad33000 at /Applications/Nexy.app
default	11:14:26.454972-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 201
error	11:14:26.454989-0500	audioaccessoryd	Updating local audio category 301 -> 201 app com.nexy.assistant
error	11:14:26.456058-0500	audioaccessoryd	Relaying via 24B92680-715A-E821-B5AF-358E78C2DAF9 inWxAddress 1C:77:54:18:C8:A3 to 88:20:0D:45:06:51 with options {
    "playingApp" : "com.nexy.assistant",
    "hostStreamingState" : "YES",
    "btAddress" : "A0:9A:8E:0D:58:86",
    "btName" : "Mac",
    "otherDeviceAudioCategory" : 201,
}
default	11:14:26.456609-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.nexy.assistant
default	11:14:27.323964-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=78457.12, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=78431, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.google.Chrome, pid=78457, auid=501, euid=501, binary_path=/Applications/Google Chrome.app/Contents/MacOS/Google Chrome}, },
default	11:14:27.282591-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Bluetooth App com.nexy.assistant, Score 201, Remote 100 NumofApp 1
default	11:14:27.328900-0500	tccd	AUTHREQ_SUBJECT: msgID=78457.12, subject=com.nexy.assistant,
default	11:14:27.331006-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb2ed5de00 at /Applications/Nexy.app
error	11:14:27.361989-0500	tccd	Prompting policy for hardened runtime; service: kTCCServiceCamera requires entitlement com.apple.security.device.camera but it is missing for responsible={TCCDProcess: identifier=com.nexy.assistant, pid=78431, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.google.Chrome, pid=78457, auid=501, euid=501, binary_path=/Applications/Google Chrome.app/Contents/MacOS/Google Chrome},
default	11:14:27.366950-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb2ed5de00 at /Applications/Nexy.app
error	11:14:27.388051-0500	tccd	Prompting policy for hardened runtime; service: kTCCServiceCamera requires entitlement com.apple.security.device.camera but it is missing for responsible={TCCDProcess: identifier=com.nexy.assistant, pid=78431, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.google.Chrome, pid=78457, auid=501, euid=501, binary_path=/Applications/Google Chrome.app/Contents/MacOS/Google Chrome},
default	11:14:27.396732-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=78457.14, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=78431, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.google.Chrome, pid=78457, auid=501, euid=501, binary_path=/Applications/Google Chrome.app/Contents/MacOS/Google Chrome}, },
default	11:14:27.398714-0500	tccd	AUTHREQ_SUBJECT: msgID=78457.14, subject=com.nexy.assistant,
default	11:14:27.399938-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb2ed5de00 at /Applications/Nexy.app
default	11:14:27.594734-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=78457.15, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=78431, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.google.Chrome, pid=78457, auid=501, euid=501, binary_path=/Applications/Google Chrome.app/Contents/MacOS/Google Chrome}, },
default	11:14:27.597147-0500	tccd	AUTHREQ_SUBJECT: msgID=78457.15, subject=com.nexy.assistant,
default	11:14:27.602919-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=387.1704, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=78431, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.SafariPlatformSupport.Helper, pid=78481, auid=501, euid=501, binary_path=/System/Volumes/Preboot/Cryptexes/OS/System/Library/PrivateFrameworks/SafariPlatformSupport.framework/Versions/A/XPCServices/com.apple.SafariPlatformSupport.Helper.xpc/Contents/MacOS/com.apple.SafariPlatformSupport.Helper}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=387, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	11:14:28.027070-0500	tccd	AUTHREQ_SUBJECT: msgID=78457.17, subject=com.nexy.assistant,
error	11:14:28.062107-0500	tccd	Prompting policy for hardened runtime; service: kTCCServiceCamera requires entitlement com.apple.security.device.camera but it is missing for responsible={TCCDProcess: identifier=com.nexy.assistant, pid=78431, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.google.Chrome, pid=78457, auid=501, euid=501, binary_path=/Applications/Google Chrome.app/Contents/MacOS/Google Chrome},
default	11:14:28.102978-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found 2 different sessions firstSession={clientName:'sid:0x1ee003, Browser Helper(1622), 'prim'', displayID:'company.thebrowser.browser.helper'}, secondSession={clientName:'sid:0x1ee029, Nexy(78431), 'prim'', displayID:'com.nexy.assistant'} but will use session={clientName:'(null)', displayID:'(null)'}
default	11:14:28.342165-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 201
default	11:14:28.422812-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=78481.2, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=78431, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.SafariPlatformSupport.Helper, pid=78481, auid=501, euid=501, binary_path=/System/Volumes/Preboot/Cryptexes/OS/System/Library/PrivateFrameworks/SafariPlatformSupport.framework/Versions/A/XPCServices/com.apple.SafariPlatformSupport.Helper.xpc/Contents/MacOS/com.apple.SafariPlatformSupport.Helper}, },
default	11:14:28.764537-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x93ad32a00 at /Applications/Nexy.app
default	11:14:28.882989-0500	Nexy	nw_path_libinfo_path_check [C1C4720C-A6C3-4261-BD74-6B9556A3E3D4 Hostname#59d04d8f:443 tcp, legacy-socket, attribution: developer]
	libinfo check path: <private>
default	11:14:28.883444-0500	mDNSResponder	[R45790] DNSServiceQueryRecord START -- qname: <mask.hash: 'c0NLQgvTESgYd1ms6HkuHg=='>, qtype: A, flags: 0x1D000, interface index: 0, client pid: 78431 (Nexy), name hash: d5fa343
default	11:14:28.885339-0500	mDNSResponder	[R45791] DNSServiceQueryRecord START -- qname: <mask.hash: 'c0NLQgvTESgYd1ms6HkuHg=='>, qtype: AAAA, flags: 0x1D000, interface index: 0, client pid: 78431 (Nexy), name hash: d5fa343
default	11:14:28.903837-0500	kernel	SK[6]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 1981D146-ED9F-4F21-95F5-69FC059C83D9 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.54781,dst=<IPv4-redacted>.443,proto=0x06 mask=0x0000003f,hash=0x9439f392 tp_proto=0x06"
default	11:14:28.904047-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:54781<-><IPv4-redacted>:443] interface: en0 (skipped: 0)
so_gencnt: 718934 t_state: SYN_SENT process: Nexy:78431 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 4 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x8ad9f90c
default	11:14:28.909583-0500	kernel	tcp connected: [<IPv4-redacted>:54781<-><IPv4-redacted>:443] interface: en0 (skipped: 0)
so_gencnt: 718934 t_state: ESTABLISHED process: Nexy:78431 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 4 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x8ad9f90c
default	11:14:28.913429-0500	symptomsd	Note coalition name com.nexy.assistant for uuid 4C4C4462-5555-3144-A167-AE19E6304731
default	11:14:29.259381-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=78481.3, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=78431, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.SafariPlatformSupport.Helper, pid=78481, auid=501, euid=501, binary_path=/System/Volumes/Preboot/Cryptexes/OS/System/Library/PrivateFrameworks/SafariPlatformSupport.framework/Versions/A/XPCServices/com.apple.SafariPlatformSupport.Helper.xpc/Contents/MacOS/com.apple.SafariPlatformSupport.Helper}, },
default	11:14:29.270502-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=78481.4, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=78431, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.SafariPlatformSupport.Helper, pid=78481, auid=501, euid=501, binary_path=/System/Volumes/Preboot/Cryptexes/OS/System/Library/PrivateFrameworks/SafariPlatformSupport.framework/Versions/A/XPCServices/com.apple.SafariPlatformSupport.Helper.xpc/Contents/MacOS/com.apple.SafariPlatformSupport.Helper}, },
default	11:14:29.377532-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=78481.5, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=78431, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.SafariPlatformSupport.Helper, pid=78481, auid=501, euid=501, binary_path=/System/Volumes/Preboot/Cryptexes/OS/System/Library/PrivateFrameworks/SafariPlatformSupport.framework/Versions/A/XPCServices/com.apple.SafariPlatformSupport.Helper.xpc/Contents/MacOS/com.apple.SafariPlatformSupport.Helper}, },
default	11:14:29.418751-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=12844.2794, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=78431, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.SafariPlatformSupport.Helper, pid=78481, auid=501, euid=501, binary_path=/System/Volumes/Preboot/Cryptexes/OS/System/Library/PrivateFrameworks/SafariPlatformSupport.framework/Versions/A/XPCServices/com.apple.SafariPlatformSupport.Helper.xpc/Contents/MacOS/com.apple.SafariPlatformSupport.Helper}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=12844, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	11:14:29.424242-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=12844.2795, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=78431, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.SafariPlatformSupport.Helper, pid=78481, auid=501, euid=501, binary_path=/System/Volumes/Preboot/Cryptexes/OS/System/Library/PrivateFrameworks/SafariPlatformSupport.framework/Versions/A/XPCServices/com.apple.SafariPlatformSupport.Helper.xpc/Contents/MacOS/com.apple.SafariPlatformSupport.Helper}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=12844, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	11:14:29.427834-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=12844.2796, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=78431, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.SafariPlatformSupport.Helper, pid=78481, auid=501, euid=501, binary_path=/System/Volumes/Preboot/Cryptexes/OS/System/Library/PrivateFrameworks/SafariPlatformSupport.framework/Versions/A/XPCServices/com.apple.SafariPlatformSupport.Helper.xpc/Contents/MacOS/com.apple.SafariPlatformSupport.Helper}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=12844, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	11:14:29.431698-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=12844.2797, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=78431, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.SafariPlatformSupport.Helper, pid=78481, auid=501, euid=501, binary_path=/System/Volumes/Preboot/Cryptexes/OS/System/Library/PrivateFrameworks/SafariPlatformSupport.framework/Versions/A/XPCServices/com.apple.SafariPlatformSupport.Helper.xpc/Contents/MacOS/com.apple.SafariPlatformSupport.Helper}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=12844, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	11:14:29.447105-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=12844.2798, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=78431, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.SafariPlatformSupport.Helper, pid=78481, auid=501, euid=501, binary_path=/System/Volumes/Preboot/Cryptexes/OS/System/Library/PrivateFrameworks/SafariPlatformSupport.framework/Versions/A/XPCServices/com.apple.SafariPlatformSupport.Helper.xpc/Contents/MacOS/com.apple.SafariPlatformSupport.Helper}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=12844, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	11:14:29.451462-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=12844.2799, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=78431, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.SafariPlatformSupport.Helper, pid=78481, auid=501, euid=501, binary_path=/System/Volumes/Preboot/Cryptexes/OS/System/Library/PrivateFrameworks/SafariPlatformSupport.framework/Versions/A/XPCServices/com.apple.SafariPlatformSupport.Helper.xpc/Contents/MacOS/com.apple.SafariPlatformSupport.Helper}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=12844, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	11:14:29.455442-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=12844.2800, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=78431, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.SafariPlatformSupport.Helper, pid=78481, auid=501, euid=501, binary_path=/System/Volumes/Preboot/Cryptexes/OS/System/Library/PrivateFrameworks/SafariPlatformSupport.framework/Versions/A/XPCServices/com.apple.SafariPlatformSupport.Helper.xpc/Contents/MacOS/com.apple.SafariPlatformSupport.Helper}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=12844, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	11:14:29.458230-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=12844.2801, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=78431, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.SafariPlatformSupport.Helper, pid=78481, auid=501, euid=501, binary_path=/System/Volumes/Preboot/Cryptexes/OS/System/Library/PrivateFrameworks/SafariPlatformSupport.framework/Versions/A/XPCServices/com.apple.SafariPlatformSupport.Helper.xpc/Contents/MacOS/com.apple.SafariPlatformSupport.Helper}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=12844, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	11:14:29.481453-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=12844.2802, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=78431, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.SafariPlatformSupport.Helper, pid=78481, auid=501, euid=501, binary_path=/System/Volumes/Preboot/Cryptexes/OS/System/Library/PrivateFrameworks/SafariPlatformSupport.framework/Versions/A/XPCServices/com.apple.SafariPlatformSupport.Helper.xpc/Contents/MacOS/com.apple.SafariPlatformSupport.Helper}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=12844, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	11:14:29.485111-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=12844.2803, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=78431, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.SafariPlatformSupport.Helper, pid=78481, auid=501, euid=501, binary_path=/System/Volumes/Preboot/Cryptexes/OS/System/Library/PrivateFrameworks/SafariPlatformSupport.framework/Versions/A/XPCServices/com.apple.SafariPlatformSupport.Helper.xpc/Contents/MacOS/com.apple.SafariPlatformSupport.Helper}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=12844, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	11:14:29.489423-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=12844.2804, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=78431, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.SafariPlatformSupport.Helper, pid=78481, auid=501, euid=501, binary_path=/System/Volumes/Preboot/Cryptexes/OS/System/Library/PrivateFrameworks/SafariPlatformSupport.framework/Versions/A/XPCServices/com.apple.SafariPlatformSupport.Helper.xpc/Contents/MacOS/com.apple.SafariPlatformSupport.Helper}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=12844, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	11:14:29.493891-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=12844.2805, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=78431, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.SafariPlatformSupport.Helper, pid=78481, auid=501, euid=501, binary_path=/System/Volumes/Preboot/Cryptexes/OS/System/Library/PrivateFrameworks/SafariPlatformSupport.framework/Versions/A/XPCServices/com.apple.SafariPlatformSupport.Helper.xpc/Contents/MacOS/com.apple.SafariPlatformSupport.Helper}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=12844, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	11:14:29.508238-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=12844.2806, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=78431, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.SafariPlatformSupport.Helper, pid=78481, auid=501, euid=501, binary_path=/System/Volumes/Preboot/Cryptexes/OS/System/Library/PrivateFrameworks/SafariPlatformSupport.framework/Versions/A/XPCServices/com.apple.SafariPlatformSupport.Helper.xpc/Contents/MacOS/com.apple.SafariPlatformSupport.Helper}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=12844, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	11:14:29.513545-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=12844.2807, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=78431, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.SafariPlatformSupport.Helper, pid=78481, auid=501, euid=501, binary_path=/System/Volumes/Preboot/Cryptexes/OS/System/Library/PrivateFrameworks/SafariPlatformSupport.framework/Versions/A/XPCServices/com.apple.SafariPlatformSupport.Helper.xpc/Contents/MacOS/com.apple.SafariPlatformSupport.Helper}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=12844, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	11:14:29.521759-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=12844.2808, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=78431, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.SafariPlatformSupport.Helper, pid=78481, auid=501, euid=501, binary_path=/System/Volumes/Preboot/Cryptexes/OS/System/Library/PrivateFrameworks/SafariPlatformSupport.framework/Versions/A/XPCServices/com.apple.SafariPlatformSupport.Helper.xpc/Contents/MacOS/com.apple.SafariPlatformSupport.Helper}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=12844, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	11:14:29.525897-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=12844.2809, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=78431, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.SafariPlatformSupport.Helper, pid=78481, auid=501, euid=501, binary_path=/System/Volumes/Preboot/Cryptexes/OS/System/Library/PrivateFrameworks/SafariPlatformSupport.framework/Versions/A/XPCServices/com.apple.SafariPlatformSupport.Helper.xpc/Contents/MacOS/com.apple.SafariPlatformSupport.Helper}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=12844, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	11:14:29.558216-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=12844.2810, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=78431, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.SafariPlatformSupport.Helper, pid=78481, auid=501, euid=501, binary_path=/System/Volumes/Preboot/Cryptexes/OS/System/Library/PrivateFrameworks/SafariPlatformSupport.framework/Versions/A/XPCServices/com.apple.SafariPlatformSupport.Helper.xpc/Contents/MacOS/com.apple.SafariPlatformSupport.Helper}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=12844, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	11:14:29.560267-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=12844.2811, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=78431, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.SafariPlatformSupport.Helper, pid=78481, auid=501, euid=501, binary_path=/System/Volumes/Preboot/Cryptexes/OS/System/Library/PrivateFrameworks/SafariPlatformSupport.framework/Versions/A/XPCServices/com.apple.SafariPlatformSupport.Helper.xpc/Contents/MacOS/com.apple.SafariPlatformSupport.Helper}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=12844, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	11:14:30.739567-0500	Nexy	nw_path_libinfo_path_check [3F0D8587-49C7-4999-9324-4B3A667AF239 Hostname#666bfe9f:443 tcp, legacy-socket, attribution: developer]
	libinfo check path: <private>
default	11:14:30.739706-0500	mDNSResponder	[R45792] DNSServiceQueryRecord START -- qname: <mask.hash: 'Uu8vLvOa37OJ2ARbwtbdCg=='>, qtype: A, flags: 0x1D000, interface index: 0, client pid: 78431 (Nexy), name hash: 705d4768
default	11:14:30.740220-0500	mDNSResponder	[R45793] DNSServiceQueryRecord START -- qname: <mask.hash: 'Uu8vLvOa37OJ2ARbwtbdCg=='>, qtype: AAAA, flags: 0x1D000, interface index: 0, client pid: 78431 (Nexy), name hash: 705d4768
default	11:14:30.749964-0500	kernel	SK[6]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 9DF3488A-384D-43E0-94F0-19E67C80B138 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.54782,dst=<IPv4-redacted>.443,proto=0x06 mask=0x0000003f,hash=0x8216ce40 tp_proto=0x06"
default	11:14:30.750037-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:54782<-><IPv4-redacted>:443] interface: en0 (skipped: 0)
so_gencnt: 718993 t_state: SYN_SENT process: Nexy:78431 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xb2fdfec0
default	11:14:30.865061-0500	kernel	tcp connected: [<IPv4-redacted>:54782<-><IPv4-redacted>:443] interface: en0 (skipped: 0)
so_gencnt: 718993 t_state: ESTABLISHED process: Nexy:78431 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xb2fdfec0
default	11:14:34.352216-0500	ControlCenter	Recent activity attributions changed to ["scr:com.nexy.assistant"]
default	11:14:42.966360-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.53053210.53053219(501)>:78431] from originator [osservice<com.apple.controlcenter(501)>:626] with description <RBSAssertionDescriptor| "FBWorkspace (BG-Active[40])" ID:394-626-35104 target:78431 attributes:[
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableLPRunReason-Suspend" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableRole-NonUI" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableJetsamPriority-Active" sourceEnvironment:"(null)">
	]>
default	11:14:42.966547-0500	runningboardd	Assertion 394-626-35104 (target:[app<application.com.nexy.assistant.53053210.53053219(501)>:78431]) will be created as active
default	11:14:42.966744-0500	ControlCenter	[app<application.com.nexy.assistant.53053210.53053219>:78431] Workspace state did change: XX-None[0] --> BG-Active[40] (assertion acquired).
default	11:14:42.967241-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78431] Ignoring jetsam update because this process is not memory-managed
default	11:14:42.967261-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78431] Ignoring suspend because this process is not lifecycle managed
default	11:14:42.967274-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78431] Ignoring GPU update because this process is not GPU managed
default	11:14:42.967668-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78431] Ignoring memory limit update because this process is not memory-managed
default	11:14:42.973436-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.53053210.53053219(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	11:14:42.974592-0500	ControlCenter	Received state update for 78431 (app<application.com.nexy.assistant.53053210.53053219(501)>, running-active-NotVisible
default	11:14:42.975826-0500	gamepolicyd	Received state update for 78431 (app<application.com.nexy.assistant.53053210.53053219(501)>, running-active-NotVisible
default	11:14:43.072393-0500	ControlCenter	[app<application.com.nexy.assistant.53053210.53053219>:78431] Workspace state did change: BG-Active[40] --> XX-None[0] (assertion dropped).
default	11:14:43.072599-0500	runningboardd	Invalidating assertion 394-626-35104 (target:[app<application.com.nexy.assistant.53053210.53053219(501)>:78431]) from originator [osservice<com.apple.controlcenter(501)>:626]
default	11:14:43.183290-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78431] Ignoring jetsam update because this process is not memory-managed
default	11:14:43.183301-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78431] Ignoring suspend because this process is not lifecycle managed
default	11:14:43.183327-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78431] Ignoring GPU update because this process is not GPU managed
default	11:14:43.183373-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78431] Ignoring memory limit update because this process is not memory-managed
default	11:14:43.187832-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.53053210.53053219(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	11:14:43.188114-0500	ControlCenter	Received state update for 78431 (app<application.com.nexy.assistant.53053210.53053219(501)>, running-active-NotVisible
default	11:14:43.189397-0500	gamepolicyd	Received state update for 78431 (app<application.com.nexy.assistant.53053210.53053219(501)>, running-active-NotVisible
default	11:14:43.466140-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=387.1706, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=78431, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.google.Chrome, pid=78457, auid=501, euid=501, binary_path=/Applications/Google Chrome.app/Contents/MacOS/Google Chrome}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=387, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	11:14:43.469238-0500	tccd	AUTHREQ_SUBJECT: msgID=387.1706, subject=com.nexy.assistant,
default	11:14:43.470221-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x93ad31b00 at /Applications/Nexy.app
default	11:14:44.119296-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.53053210.53053219(501)>:78431] from originator [osservice<com.apple.controlcenter(501)>:626] with description <RBSAssertionDescriptor| "FBWorkspace (BG-Active[40])" ID:394-626-35131 target:78431 attributes:[
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableLPRunReason-Suspend" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableRole-NonUI" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableJetsamPriority-Active" sourceEnvironment:"(null)">
	]>
default	11:14:44.119468-0500	runningboardd	Assertion 394-626-35131 (target:[app<application.com.nexy.assistant.53053210.53053219(501)>:78431]) will be created as active
default	11:14:44.119724-0500	ControlCenter	[app<application.com.nexy.assistant.53053210.53053219>:78431] Workspace state did change: XX-None[0] --> BG-Active[40] (assertion acquired).
default	11:14:44.126368-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78431] Ignoring jetsam update because this process is not memory-managed
default	11:14:44.126382-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78431] Ignoring suspend because this process is not lifecycle managed
default	11:14:44.126393-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78431] Ignoring GPU update because this process is not GPU managed
default	11:14:44.126526-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78431] Ignoring memory limit update because this process is not memory-managed
default	11:14:44.131782-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.53053210.53053219(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	11:14:44.139758-0500	ControlCenter	Received state update for 78431 (app<application.com.nexy.assistant.53053210.53053219(501)>, running-active-NotVisible
default	11:14:44.225724-0500	ControlCenter	[app<application.com.nexy.assistant.53053210.53053219>:78431] Workspace state did change: BG-Active[40] --> XX-None[0] (assertion dropped).
default	11:14:44.225858-0500	runningboardd	Invalidating assertion 394-626-35131 (target:[app<application.com.nexy.assistant.53053210.53053219(501)>:78431]) from originator [osservice<com.apple.controlcenter(501)>:626]
default	11:14:44.333044-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78431] Ignoring jetsam update because this process is not memory-managed
default	11:14:44.333071-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78431] Ignoring suspend because this process is not lifecycle managed
default	11:14:44.333097-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78431] Ignoring GPU update because this process is not GPU managed
default	11:14:44.333144-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78431] Ignoring memory limit update because this process is not memory-managed
default	11:14:44.336858-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.53053210.53053219(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	11:14:44.337230-0500	ControlCenter	Received state update for 78431 (app<application.com.nexy.assistant.53053210.53053219(501)>, running-active-NotVisible
default	11:14:44.337753-0500	gamepolicyd	Received state update for 78431 (app<application.com.nexy.assistant.53053210.53053219(501)>, running-active-NotVisible
default	11:15:01.112958-0500	kernel	tcp_connection_summary (tcp_usrclosed:3220)[<IPv4-redacted>:54781<-><IPv4-redacted>:443] interface: en0 (skipped: 0)
so_gencnt: 718934 t_state: LAST_ACK process: Nexy:78431 Duration: 32.209 sec Conn_Time: 0.006 sec bytes in/out: 10139/189432 pkts in/out: 12/21 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 5.562 ms rttvar: 0.687 ms base rtt: 4 ms so_error: 0 svc/tc: 0 flow: 0x8ad9f90c
default	11:15:01.112977-0500	kernel	tcp_connection_summary [<IPv4-redacted>:54781<-><IPv4-redacted>:443] interface: en0 (skipped: 0)
so_gencnt: 718934 t_state: LAST_ACK process: Nexy:78431 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 1/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	11:15:04.950063-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.53053210.53053219(501)>:78431] from originator [osservice<com.apple.controlcenter(501)>:626] with description <RBSAssertionDescriptor| "FBWorkspace (BG-Active[40])" ID:394-626-35148 target:78431 attributes:[
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableLPRunReason-Suspend" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableRole-NonUI" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableJetsamPriority-Active" sourceEnvironment:"(null)">
	]>
default	11:15:04.950417-0500	runningboardd	Assertion 394-626-35148 (target:[app<application.com.nexy.assistant.53053210.53053219(501)>:78431]) will be created as active
default	11:15:04.950691-0500	ControlCenter	[app<application.com.nexy.assistant.53053210.53053219>:78431] Workspace state did change: XX-None[0] --> BG-Active[40] (assertion acquired).
default	11:15:04.951152-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78431] Ignoring jetsam update because this process is not memory-managed
default	11:15:04.951169-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78431] Ignoring suspend because this process is not lifecycle managed
default	11:15:04.951181-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78431] Ignoring GPU update because this process is not GPU managed
default	11:15:04.951210-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78431] Ignoring memory limit update because this process is not memory-managed
default	11:15:04.955162-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.53053210.53053219(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	11:15:04.956306-0500	ControlCenter	Received state update for 78431 (app<application.com.nexy.assistant.53053210.53053219(501)>, running-active-NotVisible
default	11:15:04.956726-0500	gamepolicyd	Received state update for 78431 (app<application.com.nexy.assistant.53053210.53053219(501)>, running-active-NotVisible
default	11:15:05.056068-0500	ControlCenter	[app<application.com.nexy.assistant.53053210.53053219>:78431] Workspace state did change: BG-Active[40] --> XX-None[0] (assertion dropped).
default	11:15:05.056276-0500	runningboardd	Invalidating assertion 394-626-35148 (target:[app<application.com.nexy.assistant.53053210.53053219(501)>:78431]) from originator [osservice<com.apple.controlcenter(501)>:626]
default	11:15:05.169054-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78431] Ignoring jetsam update because this process is not memory-managed
default	11:15:05.169065-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78431] Ignoring suspend because this process is not lifecycle managed
default	11:15:05.169092-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78431] Ignoring GPU update because this process is not GPU managed
default	11:15:05.169137-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78431] Ignoring memory limit update because this process is not memory-managed
default	11:15:05.173244-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.53053210.53053219(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	11:15:05.173476-0500	ControlCenter	Received state update for 78431 (app<application.com.nexy.assistant.53053210.53053219(501)>, running-active-NotVisible
default	11:15:05.174277-0500	gamepolicyd	Received state update for 78431 (app<application.com.nexy.assistant.53053210.53053219(501)>, running-active-NotVisible
default	11:15:11.294305-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.53053210.53053219(501)>:78431] from originator [osservice<com.apple.controlcenter(501)>:626] with description <RBSAssertionDescriptor| "FBWorkspace (BG-Active[40])" ID:394-626-35232 target:78431 attributes:[
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableLPRunReason-Suspend" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableRole-NonUI" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableJetsamPriority-Active" sourceEnvironment:"(null)">
	]>
default	11:15:11.294476-0500	runningboardd	Assertion 394-626-35232 (target:[app<application.com.nexy.assistant.53053210.53053219(501)>:78431]) will be created as active
default	11:15:11.295454-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78431] Ignoring jetsam update because this process is not memory-managed
default	11:15:11.295501-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78431] Ignoring suspend because this process is not lifecycle managed
default	11:15:11.294668-0500	ControlCenter	[app<application.com.nexy.assistant.53053210.53053219>:78431] Workspace state did change: XX-None[0] --> BG-Active[40] (assertion acquired).
default	11:15:11.295536-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78431] Ignoring GPU update because this process is not GPU managed
default	11:15:11.295795-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78431] Ignoring memory limit update because this process is not memory-managed
default	11:15:11.301322-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.53053210.53053219(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	11:15:11.310672-0500	ControlCenter	Received state update for 78431 (app<application.com.nexy.assistant.53053210.53053219(501)>, running-active-NotVisible
default	11:15:11.312484-0500	gamepolicyd	Received state update for 78431 (app<application.com.nexy.assistant.53053210.53053219(501)>, running-active-NotVisible
default	11:15:11.400662-0500	ControlCenter	[app<application.com.nexy.assistant.53053210.53053219>:78431] Workspace state did change: BG-Active[40] --> XX-None[0] (assertion dropped).
default	11:15:11.400962-0500	runningboardd	Invalidating assertion 394-626-35232 (target:[app<application.com.nexy.assistant.53053210.53053219(501)>:78431]) from originator [osservice<com.apple.controlcenter(501)>:626]
default	11:15:11.507750-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78431] Ignoring jetsam update because this process is not memory-managed
default	11:15:11.507774-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78431] Ignoring suspend because this process is not lifecycle managed
default	11:15:11.507803-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78431] Ignoring GPU update because this process is not GPU managed
default	11:15:11.507867-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78431] Ignoring memory limit update because this process is not memory-managed
default	11:15:11.511708-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.53053210.53053219(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	11:15:11.512068-0500	ControlCenter	Received state update for 78431 (app<application.com.nexy.assistant.53053210.53053219(501)>, running-active-NotVisible
default	11:15:11.512929-0500	gamepolicyd	Received state update for 78431 (app<application.com.nexy.assistant.53053210.53053219(501)>, running-active-NotVisible
default	11:15:14.518893-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=387.1714, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=78431, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=387, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	11:15:14.518933-0500	tccd	requestor: TCCDProcess: identifier=com.apple.WindowServer, pid=387, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=78431, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	11:15:14.521284-0500	tccd	AUTHREQ_SUBJECT: msgID=387.1714, subject=com.nexy.assistant,
default	11:15:14.522496-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x93ad31b00 at /Applications/Nexy.app
default	11:15:14.668617-0500	WindowServer	1244af[StealKeyFocusReturningID]: [DeferringManager] Updating policy {
    advicePolicy: .keyThief;
    frontmostProcess: 0x0-0x2b32b3 (Google Chrome) mainConnectionID: B6CFB;
    keyThiefConnectionID: 1244AF;
} for reason: key thief updated 1244af 0x0-0x2af2af (Nexy)
default	11:15:14.668656-0500	WindowServer	<BSCompoundAssertion:0x96f011400> (com.apple.backboard.hid.delivery.localDelivery.preventFlushing) acquire for reason:key thief updated 1244af 0x0-0x2af2af (Nexy) <1850> acq:0x96dd07420 count:1
default	11:15:14.721925-0500	Nexy	[com.apple.controlcenter:3102C5D7-32AB-4033-A1B7-0E582F2556E7] Sending action(s) in update: NSSceneFenceAction
default	11:15:14.753077-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.53053210.53053219(501)>:78431] from originator [osservice<com.apple.WindowServer(88)>:387] with description <RBSAssertionDescriptor| "AppVisible" ID:394-387-35240 target:78431 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"AppVisible" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	11:15:14.753164-0500	runningboardd	Assertion 394-387-35240 (target:[app<application.com.nexy.assistant.53053210.53053219(501)>:78431]) will be created as active
default	11:15:14.753642-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78431] Ignoring jetsam update because this process is not memory-managed
default	11:15:14.753659-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78431] Ignoring suspend because this process is not lifecycle managed
default	11:15:14.753669-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78431] Ignoring GPU update because this process is not GPU managed
default	11:15:14.753690-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78431] Ignoring memory limit update because this process is not memory-managed
default	11:15:14.757157-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.53053210.53053219(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	11:15:14.757901-0500	ControlCenter	Received state update for 78431 (app<application.com.nexy.assistant.53053210.53053219(501)>, running-active-NotVisible
default	11:15:14.758079-0500	gamepolicyd	Received state update for 78431 (app<application.com.nexy.assistant.53053210.53053219(501)>, running-active-NotVisible
default	11:15:14.780908-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.53053210.53053219(501)>:78431] from originator [osservice<com.apple.WindowServer(88)>:387] with description <RBSAssertionDescriptor| "FUSBProcessWindowState: visible" ID:394-387-35241 target:78431 attributes:[
	<RBSDomainAttribute| domain:"com.apple.fuseboard" name:"Visible" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	11:15:14.781002-0500	runningboardd	Assertion 394-387-35241 (target:[app<application.com.nexy.assistant.53053210.53053219(501)>:78431]) will be created as active
default	11:15:14.781460-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78431] Ignoring jetsam update because this process is not memory-managed
default	11:15:14.781472-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78431] Ignoring suspend because this process is not lifecycle managed
default	11:15:14.781482-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78431] Ignoring GPU update because this process is not GPU managed
default	11:15:14.781502-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78431] Ignoring memory limit update because this process is not memory-managed
default	11:15:14.781529-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78431] visiblity is yes
default	11:15:14.784455-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.53053210.53053219(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	11:15:14.785089-0500	ControlCenter	Received state update for 78431 (app<application.com.nexy.assistant.53053210.53053219(501)>, running-active-NotVisible
default	11:15:14.785182-0500	gamepolicyd	Received state update for 78431 (app<application.com.nexy.assistant.53053210.53053219(501)>, running-active-NotVisible
default	11:15:15.944147-0500	Nexy	[C:3] Alloc com.apple.backboard.hid-services.xpc
default	11:15:15.944192-0500	Nexy	[0xb72053200] activating connection: mach=false listener=false peer=false name=(anonymous)
error	11:15:15.944772-0500	Nexy	Unable to obtain a task name port right for pid 387: (os/kern) failure (0x5)
default	11:15:15.945053-0500	Nexy	BKSHIDEventDeliveryManager - connection activation
default	11:15:15.948054-0500	Nexy	terminate:
default	11:15:15.948066-0500	Nexy	void _NSDisableAutomaticTerminationAndLog(NSString *) Terminating
default	11:15:15.948080-0500	Nexy	-[NSApplication _pushPersistentStateTerminationGeneration] sPersistentStateTerminateStackHeight -> 1
default	11:15:15.948163-0500	Nexy	Attempting sudden termination (1st attempt)
default	11:15:15.948174-0500	Nexy	Checking whether app should terminate
default	11:15:15.948246-0500	Nexy	Asking app delegate whether applicationShouldTerminate:
default	11:15:15.948267-0500	Nexy	replyToApplicationShouldTerminate:YES
default	11:15:15.948340-0500	Nexy	App termination approved
default	11:15:15.948353-0500	Nexy	Termination commencing
default	11:15:15.948365-0500	Nexy	Attempting sudden termination (2nd attempt)
default	11:15:15.949516-0500	Nexy	Termination complete. Exiting without sudden termination.
default	11:15:15.951531-0500	Nexy	[0xb72053340] activating connection: mach=true listener=false peer=false name=com.apple.powerlog.plxpclogger.xpc
default	11:15:15.952430-0500	Nexy	Entering exit handler.
default	11:15:15.952502-0500	Nexy	Queueing exit procedure onto XPC queue. Any further messages sent will be discarded. activeSendTransactions=0
default	11:15:15.954710-0500	audiomxd	  ServerSessionManager.mm:478   { "action":"destroy_session", "session":{"ID":"0x1ee029","name":"Nexy(78431)"}, "details":null }
default	11:15:15.954791-0500	audiomxd	AudioApplicationInfoImpl.mm:690   Successfully removed session 0x1ee029 from AudioApp, recording state unchanged (app: {"name":"[implicit] Nexy","pid":78431})
default	11:15:15.954806-0500	audiomxd	  ServerSessionManager.mm:1086  destroy audio app instance since was created implicitly by session creation and all sessions now gone (audio app: {"name":"[implicit] Nexy","pid":78431})
default	11:15:15.955437-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsPlaying:]: MXCoreSession com.nexy.assistant with category/mode MediaPlayback/Default and coreSessionID = 42 stopping playing
default	11:15:15.953314-0500	WindowServer	0[outside of RPC]: Process death: 0x0-0x2af2af (Nexy) connectionID: 1244AF pid: 78431 in session 0x101
default	11:15:15.954446-0500	WindowManager	Connection invalidated | (78431) Nexy
default	11:15:15.953344-0500	WindowServer	<BSCompoundAssertion:0x96f011540> ([FocusManager:257]-deferringPolicyEvaluationSuppression) acquire for reason:process death - 0x0-0x2af2af (Nexy) acq:0x96dd04e00 count:1
default	11:15:15.955611-0500	audiomxd	-MXCoreSession- -[MXCoreSession endInterruption:]: Session <ID: 42, PID = 78431, Name = sid:0x1ee029, Nexy(78431), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> is going inactive
default	11:15:15.955751-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 42, PID = 78431, Name = sid:0x1ee029, Nexy(78431), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	11:15:15.955984-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 42, PID = 78431, Name = sid:0x1ee029, Nexy(78431), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	11:15:15.957171-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	11:15:15.957232-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	11:15:15.957254-0500	audioaccessoryd	AudioStateChanged: Removed audio session app com.nexy.assistant 201 count 2
default	11:15:15.957269-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	11:15:15.955183-0500	ControlCenter	[app<application.com.nexy.assistant.53053210.53053219>:78431] Workspace connection invalidated.
default	11:15:15.955857-0500	ControlCenter	[app<application.com.nexy.assistant.53053210.53053219>:78431] Now flagged as pending exit for reason: workspace client connection invalidated
default	11:15:15.957492-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	11:15:15.952866-0500	Nexy	Cancelling XPC connection. Any further reply handler invocations will not retry messages
default	11:15:15.952905-0500	Nexy	[0xb72050000] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	11:15:15.952928-0500	Nexy	Exiting exit handler.
default	11:15:15.956824-0500	audiomxd	UpdateAudioState CID 0x45550001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	11:15:15.957014-0500	audiomxd	UpdateAudioState CID 0x45550001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	11:15:15.961014-0500	WindowServer	0[outside of RPC]: [FocusManager:257] update to deferring policy requested for reason: permitted list updated - 0x0-0x2af2af removed - but we are suppressing evaluation for reasons: {(
    "process death - 0x0-0x2af2af (Nexy)"
)}
default	11:15:15.961318-0500	WindowServer	0[outside of RPC]: [FocusManager:257] update to deferring policy requested for reason: permitted list updated - 0x1-0x1325f removed - but we are suppressing evaluation for reasons: {(
    "process death - 0x0-0x2af2af (Nexy)"
)}
default	11:15:15.963247-0500	runningboardd	Invalidating assertion 394-387-35241 (target:[app<application.com.nexy.assistant.53053210.53053219(501)>:78431]) from originator [osservice<com.apple.WindowServer(88)>:387]
default	11:15:15.963334-0500	runningboardd	XPC connection invalidated: [app<application.com.nexy.assistant.53053210.53053219(501)>:78431]
default	11:15:15.963489-0500	runningboardd	Invalidating assertion 394-387-35240 (target:[app<application.com.nexy.assistant.53053210.53053219(501)>:78431]) from originator [osservice<com.apple.WindowServer(88)>:387]
default	11:15:15.967962-0500	runningboardd	Invalidating assertion 394-328-35068 (target:[app<application.com.nexy.assistant.53053210.53053219(501)>:78431]) from originator [osservice<com.apple.powerd>:328]
default	11:15:15.969955-0500	coreaudiod	Sending message. { reporterID=336858579992578, category=IO, type=error, message=["scheduler_latency": Optional(14916), "multi_cycle_io_page_faults": Optional(0), "wg_external_wakeups": Optional(0), "io_cycle": Optional(5777), "safety_violation_sample_gap": Optional(0), "input_device_uid_list": Optional(), "io_buffer_size": Optional(480), "reporting_latency": Optional(14026333), "anchor_sample_time": Optional(23300), "overload_type": Optional(ClientTimeoutStart), "num_continuous_nonzero_io_cycles": Optional(0), "careporting_timestamp": 1770394515.969215, "safety_violation_time_gap": Optional(0), "wg_system_time_mach": Optional(529), "cause": Optional(ClientTimeout), "other_active_clients": Optional([ { HostApplicationDisplayID_other_client: company.thebrowser.browser.helper, sample_rate_other_client: 48000.000000, io_buffer_size_other_client: 480 } ]), "io_page_faults_duration": Optional(0), "HostApplicationDisplayID": Optional(com.nexy.assistant), "wg_instructions": Optional(44040), "is_prewarming": Optional(0), "sample_rate": Optional(48000), "out<…> }
default	11:15:15.970335-0500	coreaudiod	>>> NEGOTIATE [com.nexy.assistant]
default	11:15:15.970658-0500	coreaudiod	<<< NEGOTIATE [com.nexy.assistant]
default	11:15:15.979070-0500	coreaudiod	Sending message. { reporterID=0, category=IO, type=error, message=["scheduler_latency": Optional(15208), "multi_cycle_io_page_faults": Optional(0), "wg_external_wakeups": Optional(0), "io_cycle": Optional(5778), "safety_violation_sample_gap": Optional(0), "input_device_uid_list": Optional(), "io_buffer_size": Optional(480), "reporting_latency": Optional(12701625), "anchor_sample_time": Optional(23300), "overload_type": Optional(ClientTimeoutEnd), "num_continuous_nonzero_io_cycles": Optional(0), "careporting_timestamp": 1770394515.978018, "safety_violation_time_gap": Optional(0), "wg_system_time_mach": Optional(1413), "cause": Optional(ClientTimeout), "other_active_clients": Optional([ { HostApplicationDisplayID_other_client: company.thebrowser.browser.helper, sample_rate_other_client: 48000.000000, io_buffer_size_other_client: 480 } ]), "io_page_faults_duration": Optional(0), "HostApplicationDisplayID": Optional(com.nexy.assistant), "wg_instructions": Optional(78239), "is_prewarming": Optional(0), "sample_rate": Optional(48000), "outp<…> }
default	11:15:15.982059-0500	coreaudiod	IssueReporting.cpp:492   RTAID [ use_case=Generic report_type=RMS Generic Chain clientID=ADM node=ADM::com.nexy.assistant_2302.2212.0_airpods noise suppression studio::out-0 issue_detected_sample_time=92640.000000 ] -- [ rms:[-17.433037], peaks:[-0.287694] ]
default	11:15:15.982084-0500	coreaudiod	IssueReporting.cpp:492   RTAID [ use_case=Generic report_type=RMS Generic Chain clientID=ADM node=ADM::com.nexy.assistant_2302.2212.0_airpods noise suppression studio::in-0 issue_detected_sample_time=0.000000 ] -- [ rms:[-21.833525], peaks:[-4.796985] ]
default	11:15:15.994853-0500	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:54782<-><IPv4-redacted>:443] interface: en0 (skipped: 0)
so_gencnt: 718993 t_state: FIN_WAIT_1 process: Nexy:78431 Duration: 45.245 sec Conn_Time: 0.115 sec bytes in/out: 4920/29278 pkts in/out: 4/17 pkt rxmit: 9 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 115.562 ms rttvar: 8.625 ms base rtt: 113 ms so_error: 0 svc/tc: 0 flow: 0xb2fdfec0
default	11:15:15.994874-0500	kernel	tcp_connection_summary [<IPv4-redacted>:54782<-><IPv4-redacted>:443] interface: en0 (skipped: 0)
so_gencnt: 718993 t_state: FIN_WAIT_1 process: Nexy:78431 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	11:15:15.995104-0500	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:54692<-><IPv4-redacted>:443] interface: en0 (skipped: 0)
so_gencnt: 718401 t_state: FIN_WAIT_1 process: Nexy:78431 Duration: 73.972 sec Conn_Time: 0.015 sec bytes in/out: 4463/877 pkts in/out: 4/4 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 14.468 ms rttvar: 4.000 ms base rtt: 13 ms so_error: 0 svc/tc: 0 flow: 0x84ce1da3
default	11:15:15.995116-0500	kernel	tcp_connection_summary [<IPv4-redacted>:54692<-><IPv4-redacted>:443] interface: en0 (skipped: 0)
so_gencnt: 718401 t_state: FIN_WAIT_1 process: Nexy:78431 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	11:15:15.995203-0500	mDNSResponder	[R45780] DNSServiceCreateConnection STOP PID[78431](Nexy)
default	11:15:15.996911-0500	runningboardd	[app<application.com.nexy.assistant.53053210.53053219(501)>:78431] termination reported by launchd (0, 0, 0)
default	11:15:15.996978-0500	runningboardd	Removing process: [app<application.com.nexy.assistant.53053210.53053219(501)>:78431]
default	11:15:15.997268-0500	runningboardd	Removing launch job for: [app<application.com.nexy.assistant.53053210.53053219(501)>:78431]
default	11:15:15.997606-0500	runningboardd	Removed job for [app<application.com.nexy.assistant.53053210.53053219(501)>:78431]
default	11:15:15.997659-0500	runningboardd	Removing assertions for terminated process: [app<application.com.nexy.assistant.53053210.53053219(501)>:78431]
default	11:15:15.997709-0500	runningboardd	Removed last relative-start-date-defining assertion for process app<application.com.nexy.assistant.53053210.53053219(501)>
default	11:15:16.006311-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.53053210.53053219(501)>: none (role: None) (endowments: (null))
default	11:15:16.006679-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.53053210.53053219(501)>: none (role: None) (endowments: (null))
default	11:15:16.006829-0500	audiomxd	  ServerSessionManager.mm:1327  Monitored process died, pid = 78431, name = Nexy
default	11:15:16.006779-0500	ControlCenter	[app<application.com.nexy.assistant.53053210.53053219>:78431] Process exited: <RBSProcessExitContext| voluntary>.
default	11:15:16.006833-0500	ControlCenter	[app<application.com.nexy.assistant.53053210.53053219>:78431] Setting process task state to: Not Running
default	11:15:16.006880-0500	ControlCenter	[app<application.com.nexy.assistant.53053210.53053219>:78431] Setting process visibility to: Unknown
default	11:15:16.006964-0500	ControlCenter	[app<application.com.nexy.assistant.53053210.53053219>:78431] Invalidating workspace.
default	11:15:16.007025-0500	ControlCenter	Removing source registration for processHandle: [app<application.com.nexy.assistant.53053210.53053219(501)>:78431]
default	11:15:16.006829-0500	ControlCenter	Received state update for 78431 (app<application.com.nexy.assistant.53053210.53053219(501)>, none-NotVisible
default	11:15:16.007375-0500	ControlCenter	Received state update for 78431 (app<application.com.nexy.assistant.53053210.53053219(501)>, none-NotVisible
default	11:15:16.008008-0500	gamepolicyd	Received state update for 78431 (app<application.com.nexy.assistant.53053210.53053219(501)>, none-NotVisible
default	11:15:16.008249-0500	gamepolicyd	Received state update for 78431 (app<application.com.nexy.assistant.53053210.53053219(501)>, none-NotVisible
default	11:15:16.008304-0500	launchservicesd	Hit the server for a process handle 1dfb6c450001325f that resolved to: [app<application.com.nexy.assistant.53053210.53053219(501)>:78431]
default	11:15:16.010047-0500	ControlCenter	Removing: <FBApplicationProcess: 0xb081c7900; app<application.com.nexy.assistant.53053210.53053219>:78431(v919FF)>
default	11:15:16.011683-0500	loginwindow	-[ApplicationManager handleCASEvent:withData:] | CAS notification for appDeath for com.nexy.assistant with asn: LSASN:{hi=0x0;lo=0x2af2af} for bundle path: /Applications/Nexy.app with URL: file:///Applications/Nexy.app/
default	11:15:16.011795-0500	loginwindow	-[Application setState:] | enter: <Application: 0x8b953cd20: Nexy> state 3
default	11:15:16.011842-0500	loginwindow	-[PersistentAppsSupport applicationQuit:] | for app:Nexy, _appTrackingState = 2
default	11:15:16.018052-0500	ControlCenter	Stopping tracking for host; (bid:com.nexy.assistant-Item-0-78431)
default	11:15:16.018913-0500	loginwindow	-[Application setState:] | enter: <Application: 0x8b953cd20: Nexy> state 4
default	11:15:16.018934-0500	loginwindow	-[PersistentAppsSupport applicationQuit:] | for app:Nexy, _appTrackingState = 2
default	11:15:16.023375-0500	ControlCenter	Removing ephemeral displayable instance DisplayableId(EB23AC06) from menu bar. No corresponding host (bid:com.nexy.assistant-Item-0-78431)
default	11:15:16.023586-0500	ControlCenter	Removing displayables [DisplayableAppStatusItem(EB23AC06, (bid:com.nexy.assistant-Item-0-78431))]
error	11:15:16.161390-0500	runningboardd	RBSStateCapture remove item called for untracked item 394-387-35241 (target:[app<application.com.nexy.assistant.53053210.53053219(501)>:78431])
error	11:15:16.161405-0500	runningboardd	RBSStateCapture remove item called for untracked item 394-328-35068 (target:[app<application.com.nexy.assistant.53053210.53053219(501)>:78431])
error	11:15:16.161417-0500	runningboardd	RBSStateCapture remove item called for untracked item 394-387-35240 (target:[app<application.com.nexy.assistant.53053210.53053219(501)>:78431])
