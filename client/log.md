default	13:16:03.734846-0500	lsd	com.nexy.assistant/Unknown Persona:5:5:1:1:Building bundle record for app
default	13:16:03.735080-0500	lsd	com.nexy.assistant/Unknown Persona:5:5:2:1:Built bundle record for app
default	13:16:03.738053-0500	lsd	com.nexy.assistant/Unknown Persona:5:4:2:1:_LSServerRegisterItemInfo result = 0
default	13:16:03.753087-0500	runningboardd	Launch request for app<application.com.nexy.assistant.41851965.41851974(501)>[0] is using uid 501 (divined from auid 501 euid 501)
default	13:16:03.753217-0500	runningboardd	Acquiring assertion targeting app<application.com.nexy.assistant.41851965.41851974(501)> from originator [osservice<com.apple.coreservices.uiagent(501)>:99327] with description <RBSAssertionDescriptor| "LS launch com.nexy.assistant" ID:394-99327-1287756 target:app<application.com.nexy.assistant.41851965.41851974(501)> attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"LaunchRoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	13:16:03.753340-0500	runningboardd	Assertion 394-99327-1287756 (target:app<application.com.nexy.assistant.41851965.41851974(501)>) will be created as active
default	13:16:03.758338-0500	runningboardd	Checking PreventLaunch: global:0 exPath:/Applications/Nexy.app/Contents/MacOS/Nexy predicates:(null) allow:(null)
default	13:16:03.758387-0500	runningboardd	Creating and launching job for: app<application.com.nexy.assistant.41851965.41851974(501)>
default	13:16:03.758402-0500	runningboardd	_mutateContextIfNeeded called for com.nexy.assistant
default	13:16:03.758575-0500	runningboardd	app<application.com.nexy.assistant.41851965.41851974(501)>: -[RBPersonaManager personaForIdentity:context:personaUID:personaUniqueString:] required 0.001073 ms (wallclock); resolved to {4294967295, (null)}
default	13:16:03.828660-0500	dmd	Received xpc stream event (distributed notification matching) with name: com.apple.LaunchServices.applicationRegistered user info: {
    CFBundleDisplayName = Nexy;
    bundleIDs =     (
        "com.nexy.assistant"
    );
    isPlaceholder = 0;
}
default	13:16:03.842998-0500	runningboardd	[app<application.com.nexy.assistant.41851965.41851974(501)>:3734] is not RunningBoard jetsam managed.
default	13:16:03.843017-0500	runningboardd	[app<application.com.nexy.assistant.41851965.41851974(501)>:3734] This process will not be managed.
default	13:16:03.843027-0500	runningboardd	Now tracking process: [app<application.com.nexy.assistant.41851965.41851974(501)>:3734]
default	13:16:03.843185-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.41851965.41851974(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	13:16:03.844402-0500	gamepolicyd	Hit the server for a process handle 1f41d70100000e96 that resolved to: [app<application.com.nexy.assistant.41851965.41851974(501)>:3734]
default	13:16:03.844718-0500	gamepolicyd	Received state update for 3734 (app<application.com.nexy.assistant.41851965.41851974(501)>, running-active-NotVisible
default	13:16:03.852072-0500	runningboardd	Using default underlying assertion for app: [app<application.com.nexy.assistant.41851965.41851974(501)>:3734]
default	13:16:03.852190-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.41851965.41851974(501)>:3734] from originator [app<application.com.nexy.assistant.41851965.41851974(501)>:3734] with description <RBSAssertionDescriptor| "RB Underlying Assertion" ID:394-394-1287757 target:3734 attributes:[
	<RBSDomainAttribute| domain:"com.apple.underlying" name:"defaultUnderlyingAppAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	13:16:03.852379-0500	runningboardd	Assertion 394-394-1287757 (target:[app<application.com.nexy.assistant.41851965.41851974(501)>:3734]) will be created as active
default	13:16:03.852623-0500	runningboardd	[app<application.com.nexy.assistant.41851965.41851974(501)>:3734] Ignoring jetsam update because this process is not memory-managed
default	13:16:03.852643-0500	runningboardd	[app<application.com.nexy.assistant.41851965.41851974(501)>:3734] Ignoring suspend because this process is not lifecycle managed
default	13:16:03.852667-0500	runningboardd	[app<application.com.nexy.assistant.41851965.41851974(501)>:3734] Set darwin role to: UserInteractive
default	13:16:03.852713-0500	runningboardd	[app<application.com.nexy.assistant.41851965.41851974(501)>:3734] Ignoring GPU update because this process is not GPU managed
default	13:16:03.852773-0500	runningboardd	[app<application.com.nexy.assistant.41851965.41851974(501)>:3734] Ignoring memory limit update because this process is not memory-managed
default	13:16:03.852855-0500	runningboardd	[app<application.com.nexy.assistant.41851965.41851974(501)>:3734] reported to RB as running
default	13:16:03.855247-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.41851965.41851974(501)>:3734] from originator [osservice<com.apple.coreservices.launchservicesd>:357] with description <RBSAssertionDescriptor| "uielement:3734" ID:394-357-1287758 target:3734 attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"RoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	13:16:03.855412-0500	runningboardd	Assertion 394-357-1287758 (target:[app<application.com.nexy.assistant.41851965.41851974(501)>:3734]) will be created as active
default	13:16:03.855626-0500	CoreServicesUIAgent	LAUNCH: 0x0-0x17aa7a9 com.nexy.assistant starting stopped process.
default	13:16:03.857393-0500	runningboardd	[app<application.com.nexy.assistant.41851965.41851974(501)>:3734] Ignoring jetsam update because this process is not memory-managed
default	13:16:03.857455-0500	runningboardd	[app<application.com.nexy.assistant.41851965.41851974(501)>:3734] Ignoring suspend because this process is not lifecycle managed
default	13:16:03.857497-0500	runningboardd	[app<application.com.nexy.assistant.41851965.41851974(501)>:3734] Ignoring GPU update because this process is not GPU managed
default	13:16:03.857629-0500	runningboardd	[app<application.com.nexy.assistant.41851965.41851974(501)>:3734] Ignoring memory limit update because this process is not memory-managed
default	13:16:03.857829-0500	runningboardd	Successfully acquired underlying assertion for [app<application.com.nexy.assistant.41851965.41851974(501)>:3734]
default	13:16:03.858084-0500	loginwindow	-[Application _updateInformationInternal] | Got App URL: file:///Applications/Nexy.app/
default	13:16:03.860964-0500	loginwindow	-[Application setState:] | enter: <Application: 0x96aadb2a0: Nexy> state 2
default	13:16:03.861006-0500	loginwindow	-[ApplicationManager checkInAppContext:eventData:] | ApplicationManager: Checked in app : Nexy
default	13:16:03.862149-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.41851965.41851974(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	13:16:03.862478-0500	runningboardd	Invalidating assertion 394-99327-1287756 (target:app<application.com.nexy.assistant.41851965.41851974(501)>) from originator [osservice<com.apple.coreservices.uiagent(501)>:99327]
default	13:16:03.862524-0500	runningboardd	[app<application.com.nexy.assistant.41851965.41851974(501)>:3734] Ignoring jetsam update because this process is not memory-managed
default	13:16:03.862632-0500	runningboardd	[app<application.com.nexy.assistant.41851965.41851974(501)>:3734] Ignoring suspend because this process is not lifecycle managed
default	13:16:03.862711-0500	runningboardd	[app<application.com.nexy.assistant.41851965.41851974(501)>:3734] Ignoring GPU update because this process is not GPU managed
default	13:16:03.862834-0500	runningboardd	[app<application.com.nexy.assistant.41851965.41851974(501)>:3734] Ignoring memory limit update because this process is not memory-managed
default	13:16:03.863152-0500	gamepolicyd	Received state update for 3734 (app<application.com.nexy.assistant.41851965.41851974(501)>, running-active-NotVisible
default	13:16:03.870553-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.41851965.41851974(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	13:16:03.965833-0500	runningboardd	[app<application.com.nexy.assistant.41851965.41851974(501)>:3734] Ignoring jetsam update because this process is not memory-managed
default	13:16:03.965884-0500	runningboardd	[app<application.com.nexy.assistant.41851965.41851974(501)>:3734] Ignoring suspend because this process is not lifecycle managed
default	13:16:03.965904-0500	runningboardd	[app<application.com.nexy.assistant.41851965.41851974(501)>:3734] Ignoring GPU update because this process is not GPU managed
default	13:16:03.965992-0500	runningboardd	[app<application.com.nexy.assistant.41851965.41851974(501)>:3734] Ignoring memory limit update because this process is not memory-managed
default	13:16:03.966474-0500	gamepolicyd	Received state update for 3734 (app<application.com.nexy.assistant.41851965.41851974(501)>, running-active-NotVisible
default	13:16:03.970067-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.41851965.41851974(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	13:16:03.970761-0500	gamepolicyd	Received state update for 3734 (app<application.com.nexy.assistant.41851965.41851974(501)>, running-active-NotVisible
default	13:16:04.096643-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=489.73, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=3734, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.syspolicyd, pid=489, auid=0, euid=0, binary_path=/usr/libexec/syspolicyd}, },
default	13:16:04.106333-0500	tccd	AUTHREQ_SUBJECT: msgID=489.73, subject=com.nexy.assistant,
default	13:16:04.129808-0500	syspolicyd	Found provenance data on target: TA(c1427ed62e916d1d, 2), PST: (path: a2cffff67b96be6e), (team: 5NKLL2CLB9), (id: com.nexy.assistant), (bundle_id: (null))
default	13:16:04.144903-0500	kernel	Nexy[3734] triggered unnest of range 0x1fc000000->0x1fe000000 of DYLD shared region in VM map 0x954fe9625cb94c89. While not abnormal for debuggers, this increases system memory footprint until the target exits.
default	13:16:04.144926-0500	kernel	Nexy[3734] triggered unnest of range 0x1fe000000->0x200000000 of DYLD shared region in VM map 0x954fe9625cb94c89. While not abnormal for debuggers, this increases system memory footprint until the target exits.
error	13:16:04.648313-0500	Nexy	dlsym cannot find symbol NSMakeRect in CFBundle 0x10610db80 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	13:16:04.648624-0500	Nexy	dlsym cannot find symbol NSMakePoint in CFBundle 0x10610db80 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	13:16:04.648873-0500	Nexy	dlsym cannot find symbol NSMakeSize in CFBundle 0x10610db80 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	13:16:04.649117-0500	Nexy	dlsym cannot find symbol NSMakeRange in CFBundle 0x10610db80 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
default	13:16:04.650913-0500	Nexy	[0x106128490] activating connection: mach=true listener=false peer=false name=com.apple.coreservices.launchservicesd
default	13:16:04.651885-0500	Nexy	[0x7dab60000] activating connection: mach=true listener=false peer=false name=com.apple.analyticsd
default	13:16:04.652386-0500	Nexy	[0x7dab60140] activating connection: mach=true listener=false peer=false name=com.apple.pasteboard.1
default	13:16:04.653008-0500	Nexy	[0x7dab60280] activating connection: mach=true listener=false peer=false name=com.apple.distributed_notifications@Uv3
default	13:16:04.655529-0500	Nexy	void _NSDisableAutomaticTerminationAndLog(NSString *) No windows open yet
default	13:16:04.657675-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=3734.1, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=3734, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	13:16:04.656594-0500	Nexy	[0x7dab603c0] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	13:16:04.660948-0500	tccd	AUTHREQ_SUBJECT: msgID=3734.1, subject=com.nexy.assistant,
default	13:16:04.662561-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21255e00 at /Applications/Nexy.app
default	13:16:04.678180-0500	Nexy	Received configuration update from daemon (initial)
default	13:16:04.679714-0500	Nexy	[0x7dab603c0] invalidated after the last release of the connection object
default	13:16:04.684916-0500	Nexy	server port 0x0000350b, session port 0x0000350b
default	13:16:04.686064-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=387.11093, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=3734, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=387, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	13:16:04.686096-0500	tccd	requestor: TCCDProcess: identifier=com.apple.WindowServer, pid=387, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=3734, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	13:16:04.687880-0500	tccd	AUTHREQ_SUBJECT: msgID=387.11093, subject=com.nexy.assistant,
default	13:16:04.689148-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21255e00 at /Applications/Nexy.app
default	13:16:04.712552-0500	Nexy	CHECKIN: pid=3734
default	13:16:04.724303-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.41851965.41851974(501)>:3734] from originator [osservice<com.apple.coreservices.launchservicesd>:357] with description <RBSAssertionDescriptor| "uielement:3734" ID:394-357-1287766 target:3734 attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"RoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	13:16:04.724414-0500	runningboardd	Assertion 394-357-1287766 (target:[app<application.com.nexy.assistant.41851965.41851974(501)>:3734]) will be created as active
default	13:16:04.724378-0500	Nexy	CHECKEDIN: pid=3734 asn=0x0-0x17aa7a9 foreground=0
default	13:16:04.724235-0500	launchservicesd	CHECKIN:0x0-0x17aa7a9 3734 com.nexy.assistant
default	13:16:04.724834-0500	runningboardd	Invalidating assertion 394-357-1287758 (target:[app<application.com.nexy.assistant.41851965.41851974(501)>:3734]) from originator [osservice<com.apple.coreservices.launchservicesd>:357]
default	13:16:04.727966-0500	Nexy	[0x7dab60500] activating connection: mach=true listener=false peer=false name=com.apple.lsd.mapdb
default	13:16:04.732523-0500	Nexy	No persisted cache on this platform.
default	13:16:04.733930-0500	Nexy	Current system appearance, (HLTB: 1), (SLS: 0)
default	13:16:04.734607-0500	Nexy	Post-registration system appearance: (HLTB: 1)
default	13:16:04.738032-0500	Nexy	FBSWorkspace: endpoint monitoring is disabled.
default	13:16:04.738043-0500	Nexy	FBSWorkspace: default shell endpoint is disabled.
default	13:16:04.738116-0500	Nexy	Initializing connection
default	13:16:04.738162-0500	Nexy	Removing all cached process handles
default	13:16:04.738188-0500	Nexy	Sending handshake request attempt #1 to server
default	13:16:04.738198-0500	Nexy	Creating connection to com.apple.runningboard
default	13:16:04.738207-0500	Nexy	[0x7dab60640] activating connection: mach=true listener=false peer=false name=com.apple.runningboard
default	13:16:04.738759-0500	runningboardd	Setting client for [app<application.com.nexy.assistant.41851965.41851974(501)>:3734] as ready
default	13:16:04.739516-0500	Nexy	Handshake succeeded
default	13:16:04.739537-0500	Nexy	Identity resolved as app<application.com.nexy.assistant.41851965.41851974(501)>
default	13:16:04.740156-0500	Nexy	[0x7dab603c0] Connection returned listener port: 0x4403
default	13:16:04.743932-0500	Nexy	[0x7dab603c0] Connection returned listener port: 0x4403
default	13:16:04.748137-0500	Nexy	Created a new Process Instance Registry XPC connection (inactive)
default	13:16:04.748163-0500	Nexy	[0x7dab608c0] activating connection: mach=true listener=false peer=false name=com.apple.linkd.autoShortcut
default	13:16:04.748276-0500	Nexy	Activated connection to com.apple.linkd.autoShortcut (ApplicationService)
default	13:16:04.748327-0500	Nexy	[0x7dab60a00] activating connection: mach=false listener=true peer=false name=(anonymous)
default	13:16:06.113719-0500	kernel	SK[9]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid D092502B-F69B-4010-983B-F6ACDB23720F flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.57630,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0x3792c7d7 tp_proto=0x06"
default	13:16:06.113779-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:57630<-><IPv4-redacted>:53] interface: utun4 (skipped: 23977)
so_gencnt: 7004519 t_state: SYN_SENT process: Nexy:3734 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 1 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x837e5457
default	13:16:06.114267-0500	kernel	tcp connected: [<IPv4-redacted>:57630<-><IPv4-redacted>:53] interface: utun4 (skipped: 23977)
so_gencnt: 7004519 t_state: ESTABLISHED process: Nexy:3734 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 1 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x837e5457
default	13:16:06.114546-0500	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:57630<-><IPv4-redacted>:53] interface: utun4 (skipped: 23977)
so_gencnt: 7004519 t_state: FIN_WAIT_1 process: Nexy:3734 Duration: 0.001 sec Conn_Time: 0.000 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 1.000 ms rttvar: 0.500 ms base rtt: 1 ms so_error: 0 svc/tc: 0 flow: 0x837e5457
default	13:16:06.114556-0500	kernel	tcp_connection_summary [<IPv4-redacted>:57630<-><IPv4-redacted>:53] interface: utun4 (skipped: 23977)
so_gencnt: 7004519 t_state: FIN_WAIT_1 process: Nexy:3734 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	13:16:06.216787-0500	Nexy	  AVAudioSession_MacOS.mm:1021  initForMacOS
default	13:16:06.218247-0500	Nexy	[0x7dab60c80] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioSession
default	13:16:06.220438-0500	audiomxd	  ServerSessionManager.mm:315   { "action":"create_session", "session":{"ID":"0x1f482f","name":"Nexy(3734)"}, "details":{"PID":3734,"session_type":"Primary"} }
default	13:16:06.220550-0500	audiomxd	AudioApplicationInfoImpl.mm:250   Setting initial isRecording state: 0 for newly-created AudioApp
	app: {"name":"[implicit] Nexy","pid":3734}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1f482f, sessionType: 'prim', isRecording: false }, 
]
default	13:16:06.221767-0500	audiomxd	  ServerSessionManager.mm:1322  Start process monitoring, pid = 3734, name = Nexy
default	13:16:06.222224-0500	Nexy	    SessionCore_Create.mm:99    Created session 0x7db88b9c0 with ID: 0x1f482f
default	13:16:06.222915-0500	Nexy	Registered notify signal com.apple.caulk.alloc.rtdump (0)
default	13:16:06.224483-0500	Nexy	System_Input_Processing_Notification_Handler.mm:456   System_Input_Processing_Notification_Handler::is_vi_available(): Voice isolation DSP is available for client with bundle id com.nexy.assistant (AVFoundation is available, application is not in client deny list, application is not FaceTime variant)
default	13:16:06.227444-0500	Nexy	[0x7dab60dc0] activating connection: mach=true listener=false peer=false name=com.apple.cmio.registerassistantservice.system-extensions
fault	13:16:06.230930-0500	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.41851965.41851974 AUID=501> and <type=Application identifier=application.com.nexy.assistant.41851965.41851974>
default	13:16:06.237288-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOInitializeListenersForBundleID: for <private> -> <private>
default	13:16:06.239702-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> vpio_preferenceChangedListener: new value ((null)) for key AUVoiceIOClients/com-nexy-assistant/AUVoiceIOChatFlavor, translatedBundleID com.nexy.assistant, bundleIDs {(
    "com.nexy.assistant"
)}
default	13:16:06.239892-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> vpio_preferenceChangedListener: new value ((null)) for key AUVoiceIOClients/com-nexy-assistant/AUVoiceIOIsAutoChatFlavorEnabled, translatedBundleID com.nexy.assistant, bundleIDs {(
    "com.nexy.assistant"
)}
default	13:16:06.240092-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetSupportedChatFlavorsForBundleID: <private>-><private> get supported chat flavors: <private>
default	13:16:06.240102-0500	Nexy	            HALSystem.cpp:134    Enabling HAL Voice Isolation support
default	13:16:06.240140-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetHiddenChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	13:16:06.240283-0500	Nexy	[0x7dab60f00] activating connection: mach=true listener=false peer=false name=com.apple.tccd
default	13:16:06.240845-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=3734.2, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=3734, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	13:16:06.240979-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOHiddenChatFlavors newValue: (
    1
)
default	13:16:06.248051-0500	tccd	AUTHREQ_SUBJECT: msgID=3734.2, subject=com.nexy.assistant,
default	13:16:06.248783-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x7d1158000 at /Applications/Nexy.app
default	13:16:06.261928-0500	Nexy	[0x7dab60f00] invalidated after the last release of the connection object
default	13:16:06.261992-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetSupportedChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	13:16:06.265573-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOSupportedChatFlavors newValue: (
)
default	13:16:06.267081-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=395.9240, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=3734, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	13:16:06.268205-0500	tccd	AUTHREQ_SUBJECT: msgID=395.9240, subject=com.nexy.assistant,
default	13:16:06.268805-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x7d1158000 at /Applications/Nexy.app
error	13:16:06.282565-0500	tccd	Request message contains a target_token to accessing_process (TCCDProcess: identifier=com.nexy.assistant, pid=3734, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy) but TCCDProcess: identifier=com.apple.audio.coreaudiod, pid=395, auid=202, euid=202, binary_path=/usr/sbin/coreaudiod is not a TCC manager for service: kTCCServiceScreenCapture.
default	13:16:06.283528-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=395.9242, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=3734, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	13:16:06.284646-0500	tccd	AUTHREQ_SUBJECT: msgID=395.9242, subject=com.nexy.assistant,
default	13:16:06.285228-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x7d1158000 at /Applications/Nexy.app
default	13:16:06.305828-0500	Nexy	  HALPlugInManagement.cpp:440    HALPlugInManagement::RegisterPlugIns: skipping in-process plug-ins
error	13:16:06.306169-0500	Nexy	AddInstanceForFactory: No factory registered for id <CFUUID 0x7d95d81c0> F8BB1C28-BAE8-11D6-9C31-00039315CD46
default	13:16:06.335689-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	13:16:06.335840-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	13:16:06.342566-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetPreferredChatFlavorForBundleID: <private>-><private> get value: 0
default	13:16:06.344237-0500	Nexy	[0x7dab60f00] activating connection: mach=true listener=false peer=false name=com.apple.audioanalyticsd
error	13:16:06.344662-0500	Nexy	Reporter disconnected. { function=sendMessage, reporterID=16037407883265 }
default	13:16:06.345105-0500	Nexy	       AggregateDevice.mm:887   Creating DefaultDeviceAggregate
default	13:16:06.345366-0500	Nexy	       AggregateDevice.mm:914   fetched default output device, ID = 83
default	13:16:06.345405-0500	Nexy	       AggregateDevice.mm:914   fetched default input device, ID = 89
default	13:16:06.366753-0500	Nexy	       AggregateDevice.mm:688   Built valid aggregate 125
default	13:16:06.376954-0500	Nexy	  AVAudioSession_MacOS.mm:507   Setting category: AVAudioSessionCategoryPlayback, requires reconfiguration?: NO
default	13:16:06.376980-0500	Nexy	  AVAudioSession_MacOS.mm:883   Activating session
default	13:16:06.902678-0500	Nexy	                AUHAL.cpp:420   AUHAL: (0x7db984040) Selecting device 83 from constructor
default	13:16:06.902693-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0x7db984040)
default	13:16:06.902700-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0x7db984040) not already running
default	13:16:06.902944-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0x7db984040) nothing to teardown
default	13:16:06.902950-0500	Nexy	                AUHAL.cpp:762   SelectDevice: (0x7db984040) connecting device 83
default	13:16:06.903107-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0x7db984040) Device ID: 83 (Input:No | Output:Yes): true
default	13:16:06.903229-0500	Nexy	                AUHAL.cpp:774   SelectDevice: (0x7db984040) created ioproc 0xa for device 83
default	13:16:06.903361-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x7db984040) adding 7 device listeners to device 83
default	13:16:06.903563-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x7db984040) adding 0 device delegate listeners to device 83
default	13:16:06.903573-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x7db984040)
default	13:16:06.903656-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x54]:  2 ch,  48000 Hz, Float32, interleaved
default	13:16:06.903665-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	13:16:06.903671-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	13:16:06.903687-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	13:16:06.903700-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	13:16:06.903798-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x7db984040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	13:16:06.903809-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x7db984040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	13:16:06.903815-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	13:16:06.903820-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x7db984040) removing 0 device listeners from device 0
default	13:16:06.903825-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x7db984040) removing 0 device delegate listeners from device 0
default	13:16:06.903831-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0x7db984040)
default	13:16:06.903901-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is DISABLED
default	13:16:06.904365-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:16:06.906189-0500	Nexy	       ACv2Workarounds.mm:51    com.nexy.assistant: fix84702776_86723525_86479548_89800354_SinglePacketDesc: false
default	13:16:06.906270-0500	Nexy	Registered notify signal com.apple.caulk.alloc.audiodump (0)
default	13:16:06.906511-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0x7d9f18120, from  2 ch,  44100 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	13:16:06.906569-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:16:06.909246-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:16:06.909619-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:16:06.915239-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:16:06.915571-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:16:06.917798-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0x7d9f1ed60, from  2 ch,  44100 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	13:16:06.917819-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:16:06.918309-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:16:06.919042-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0x7d9f1eee0, from  2 ch,  48000 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	13:16:06.919056-0500	Nexy	       AudioConverter.cpp:1317  AudioConverter -> 0x7d9f1eee0: The in-process GetProperty call returned 1886547824 for property 1886546285 with size 8.
default	13:16:06.919063-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:16:06.919064-0500	Nexy	AudioConverter -> 0x7d9f1eee0: The in-process SetProperty call returned 1886547824 for property 1936876385 with size 4.
default	13:16:06.919075-0500	Nexy	AudioConverter -> 0x7d9f1eee0: The in-process SetProperty call returned 1886547824 for property 1936876401 with size 4.
default	13:16:06.919081-0500	Nexy	AudioConverter -> 0x7d9f1eee0: The in-process SetProperty call returned 1886547824 for property 1886547309 with size 4.
default	13:16:06.919836-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0x7d9f1eee0, from  2 ch,  48000 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	13:16:06.919842-0500	Nexy	       AudioConverter.cpp:1317  AudioConverter -> 0x7d9f1eee0: The in-process GetProperty call returned 1886547824 for property 1886546285 with size 8.
default	13:16:06.919847-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:16:06.919848-0500	Nexy	AudioConverter -> 0x7d9f1eee0: The in-process SetProperty call returned 1886547824 for property 1936876385 with size 4.
default	13:16:06.919857-0500	Nexy	AudioConverter -> 0x7d9f1eee0: The in-process SetProperty call returned 1886547824 for property 1936876401 with size 4.
default	13:16:06.919862-0500	Nexy	AudioConverter -> 0x7d9f1eee0: The in-process SetProperty call returned 1886547824 for property 1886547309 with size 4.
default	13:16:06.920011-0500	Nexy	       AudioConverter.cpp:1317  AudioConverter -> 0x7d9f1eee0: The in-process GetProperty call returned 1886547824 for property 1886546285 with size 8.
default	13:16:07.004142-0500	Nexy	                AUHAL.cpp:420   AUHAL: (0x7db985540) Selecting device 83 from constructor
default	13:16:07.004151-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0x7db985540)
default	13:16:07.004159-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0x7db985540) not already running
default	13:16:07.004163-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0x7db985540) nothing to teardown
default	13:16:07.004167-0500	Nexy	                AUHAL.cpp:762   SelectDevice: (0x7db985540) connecting device 83
default	13:16:07.004245-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0x7db985540) Device ID: 83 (Input:No | Output:Yes): true
default	13:16:07.004340-0500	Nexy	                AUHAL.cpp:774   SelectDevice: (0x7db985540) created ioproc 0xb for device 83
default	13:16:07.004437-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x7db985540) adding 7 device listeners to device 83
default	13:16:07.004592-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x7db985540) adding 0 device delegate listeners to device 83
default	13:16:07.004601-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x7db985540)
default	13:16:07.004671-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x54]:  2 ch,  48000 Hz, Float32, interleaved
default	13:16:07.004678-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	13:16:07.004683-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	13:16:07.004688-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	13:16:07.004697-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	13:16:07.004786-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x7db985540) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	13:16:07.004796-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x7db985540) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	13:16:07.004801-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	13:16:07.004806-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x7db985540) removing 0 device listeners from device 0
default	13:16:07.004808-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x7db985540) removing 0 device delegate listeners from device 0
default	13:16:07.004816-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0x7db985540)
default	13:16:07.004827-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is DISABLED
default	13:16:07.004878-0500	Nexy	                AUHAL.cpp:2303  SetProperty: (0x7db985540) caller requesting device change from 83 to 89
default	13:16:07.004885-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0x7db985540)
default	13:16:07.004893-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0x7db985540) not already running
default	13:16:07.004897-0500	Nexy	                AUHAL.cpp:687   SelectDevice: (0x7db985540) disconnecting device 83
default	13:16:07.004903-0500	Nexy	                AUHAL.cpp:751   SelectDevice: (0x7db985540) destroying ioproc 0xb for device 83
default	13:16:07.004964-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped Unknown {1C-77-54-18-C8-A3:output, 0xb}
default	13:16:07.005031-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	13:16:07.005104-0500	Nexy	                AUHAL.cpp:762   SelectDevice: (0x7db985540) connecting device 89
default	13:16:07.005173-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0x7db985540) Device ID: 89 (Input:Yes | Output:No): true
default	13:16:07.006658-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=395.9243, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=3734, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	13:16:07.008012-0500	tccd	AUTHREQ_SUBJECT: msgID=395.9243, subject=com.nexy.assistant,
default	13:16:07.008682-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x7d1158000 at /Applications/Nexy.app
default	13:16:07.027357-0500	tccd	AUTHREQ_PROMPTING: msgID=395.9243, service=kTCCServiceMicrophone, subject=Sub:{com.nexy.assistant}Resp:{TCCDProcess: identifier=com.nexy.assistant, pid=3734, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy},
default	13:16:08.405725-0500	tccd	Publishing <TCCDEvent: type=Create, service=kTCCServiceMicrophone, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 3 subscribers: {
    474 = "<TCCDEventSubscriber: token=474, state=Passed, csid=com.apple.photolibraryd>";
    472 = "<TCCDEventSubscriber: token=472, state=Passed, csid=com.apple.chronod>";
    37 = "<TCCDEventSubscriber: token=37, state=Initial, csid=(null)>";
}
default	13:16:08.408555-0500	chronod	[appAuth:com.nexy.assistant] tcc authorization(s) changed
default	13:16:08.408710-0500	Nexy	                AUHAL.cpp:774   SelectDevice: (0x7db985540) created ioproc 0xa for device 89
default	13:16:08.408926-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x7db985540) adding 7 device listeners to device 89
default	13:16:08.409193-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x7db985540) adding 0 device delegate listeners to device 89
default	13:16:08.409208-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x7db985540)
default	13:16:08.409220-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 output streams; not all mono
default	13:16:08.409236-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	13:16:08.409490-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  input stream 0 [0x5a]:  1 ch,  24000 Hz, Float32
default	13:16:08.409499-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 input streams; all mono
default	13:16:08.409507-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  1 ch,  24000 Hz, Float32
default	13:16:08.409636-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x7db985540) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	13:16:08.409652-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x7db985540) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	13:16:08.409660-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	13:16:08.409665-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x7db985540) removing 7 device listeners from device 83
default	13:16:08.409903-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x7db985540) removing 0 device delegate listeners from device 83
default	13:16:08.409915-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0x7db985540)
default	13:16:08.410532-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	13:16:08.412218-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=395.9244, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=3734, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	13:16:08.413983-0500	tccd	AUTHREQ_SUBJECT: msgID=395.9244, subject=com.nexy.assistant,
default	13:16:08.415102-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x7d1158000 at /Applications/Nexy.app
default	13:16:08.439400-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0x7d9f1f330, from  1 ch,  24000 Hz, Float32 to  1 ch,  16000 Hz, Float32
default	13:16:08.439676-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	13:16:08.440901-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=395.9245, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=3734, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	13:16:08.442138-0500	tccd	AUTHREQ_SUBJECT: msgID=395.9245, subject=com.nexy.assistant,
default	13:16:08.442830-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x7d1158000 at /Applications/Nexy.app
default	13:16:08.464452-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=395.9246, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=3734, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	13:16:08.465647-0500	tccd	AUTHREQ_SUBJECT: msgID=395.9246, subject=com.nexy.assistant,
default	13:16:08.466304-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x7d1158000 at /Applications/Nexy.app
default	13:16:08.497324-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetPreferredChatFlavorForBundleID: <private>-><private> get value: 0
default	13:16:08.497797-0500	coreaudiod	>>> NEGOTIATE [com.nexy.assistant]
default	13:16:08.497950-0500	coreaudiod	<<< NEGOTIATE [com.nexy.assistant]
default	13:16:08.499635-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetSupportedChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	13:16:08.499723-0500	coreaudiod	>>> ADAPT [com.nexy.assistant]
default	13:16:08.502134-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0x87e3f6d00] Created node ADM::com.nexy.assistant_52570.52454.0_airpods noise suppression studio::in-0 with nodeID 0 - reporting period = 10.000000, sample rate = 24000.000000
default	13:16:08.502199-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0x87e3f6d00] Created node ADM::com.nexy.assistant_52570.52454.0_airpods noise suppression studio::out-0 with nodeID 1 - reporting period = 10.000000, sample rate = 24000.000000
default	13:16:08.502432-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOSupportedChatFlavors newValue: (
    0,
    2
)
default	13:16:08.591490-0500	coreaudiod	<<< ADAPT [com.nexy.assistant]
default	13:16:08.596329-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:52570 called from <private>
default	13:16:08.596349-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Input {1C-77-54-18-C8-A3:input, 0xa}
default	13:16:08.596585-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(52569)
default	13:16:08.596586-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(52577)
default	13:16:08.596616-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:52569 called from <private>
default	13:16:08.598963-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1f482f","name":"Nexy(3734)"}, "details":{"deviceUIDs":["1C-77-54-18-C8-A3:input"],"implicit_category":"Record","input_running":true,"output_running":false} }
default	13:16:08.599296-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 2093, PID = 3734, Name = sid:0x1f482f, Nexy(3734), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	13:16:08.600675-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 2093, PID = 3734, Name = sid:0x1f482f, Nexy(3734), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	13:16:08.601994-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 2093, PID = 3734, Name = sid:0x1f482f, Nexy(3734), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	13:16:08.602521-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 2093, PID = 3734, Name = sid:0x1f482f, Nexy(3734), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	13:16:08.602817-0500	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 2093, PID = 3734, Name = sid:0x1f482f, Nexy(3734), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> is going active
default	13:16:08.602857-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1f482f, Nexy(3734), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 2093 starting recording
default	13:16:08.603686-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 2093, PID = 3734, Name = sid:0x1f482f, Nexy(3734), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	13:16:08.596620-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:52577 called from <private>
default	13:16:08.598097-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:52570 called from <private>
default	13:16:08.598382-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:52577 called from <private>
default	13:16:08.604229-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.41851965.41851974(501)>:3734] from originator [osservice<com.apple.powerd>:328] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:394-328-1287794 target:3734 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	13:16:08.603977-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 2093, PID = 3734, Name = sid:0x1f482f, Nexy(3734), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	13:16:08.604357-0500	runningboardd	Assertion 394-328-1287794 (target:[app<application.com.nexy.assistant.41851965.41851974(501)>:3734]) will be created as active
default	13:16:08.604778-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	13:16:08.596622-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:52569 called from <private>
default	13:16:08.598541-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(52570)
default	13:16:08.604152-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1f482f, Nexy(3734), 'prim'', displayID:'com.nexy.assistant'}
default	13:16:08.598556-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:52570 called from <private>
default	13:16:08.602724-0500	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1f482f, Nexy(3734), 'prim'', AudioCategory changed to 'Record_WithBluetooth'
default	13:16:08.605395-0500	runningboardd	[app<application.com.nexy.assistant.41851965.41851974(501)>:3734] Ignoring jetsam update because this process is not memory-managed
default	13:16:08.598673-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:52570 called from <private>
default	13:16:08.605801-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	13:16:08.605561-0500	runningboardd	[app<application.com.nexy.assistant.41851965.41851974(501)>:3734] Ignoring suspend because this process is not lifecycle managed
default	13:16:08.605978-0500	runningboardd	[app<application.com.nexy.assistant.41851965.41851974(501)>:3734] Ignoring GPU update because this process is not GPU managed
default	13:16:08.604173-0500	audiomxd	UpdateAudioState CID 0x72200001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:16:08.604383-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [1, 0]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:input"
)}
default	13:16:08.604574-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	13:16:08.606532-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(52570)
default	13:16:08.606554-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(52577)
default	13:16:08.606580-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(52570)
default	13:16:08.606622-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:52577 called from <private>
default	13:16:08.606622-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(52570)
default	13:16:08.607093-0500	runningboardd	[app<application.com.nexy.assistant.41851965.41851974(501)>:3734] Ignoring memory limit update because this process is not memory-managed
default	13:16:08.606657-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:52577 called from <private>
default	13:16:08.606693-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(52570)
default	13:16:08.606806-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(52570)
default	13:16:08.606823-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:52570 called from <private>
default	13:16:08.606863-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(52570)
default	13:16:08.606889-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:52570 called from <private>
default	13:16:08.606937-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:52570 called from <private>
default	13:16:08.607327-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:52570 called from <private>
default	13:16:08.607363-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:52570 called from <private>
default	13:16:08.607410-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:52570 called from <private>
default	13:16:08.607474-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:52570 called from <private>
default	13:16:08.607506-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:52570 called from <private>
default	13:16:08.607544-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:52570 called from <private>
default	13:16:08.607575-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:52570 called from <private>
default	13:16:08.604881-0500	audiomxd	UpdateAudioState CID 0x72200001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:16:08.607619-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:52570 called from <private>
default	13:16:08.607650-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:52570 called from <private>
default	13:16:08.607686-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:52570 called from <private>
default	13:16:08.605742-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	13:16:08.607738-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:52570 called from <private>
default	13:16:08.604985-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:16:08.605753-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:16:08.612077-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:52569 called from <private>
default	13:16:08.612092-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:52569 called from <private>
default	13:16:08.612183-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(52569)
default	13:16:08.612198-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:52569 called from <private>
default	13:16:08.612204-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:52569 called from <private>
default	13:16:08.615900-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(52569)
default	13:16:08.616312-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:52569 called from <private>
default	13:16:08.616341-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:52569 called from <private>
default	13:16:08.620685-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.41851965.41851974(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	13:16:08.616491-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:52569 called from <private>
default	13:16:08.616545-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:52569 called from <private>
default	13:16:08.617203-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:52569 called from <private>
default	13:16:08.617244-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:52569 called from <private>
default	13:16:08.617387-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(52569)
default	13:16:08.617453-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:52569 called from <private>
default	13:16:08.617651-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:52569 called from <private>
default	13:16:08.622616-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(52569)
default	13:16:08.622680-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:52569 called from <private>
default	13:16:08.622744-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(52569)
default	13:16:08.622782-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:52569 called from <private>
default	13:16:08.622842-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:52569 called from <private>
default	13:16:08.622885-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:52569 called from <private>
default	13:16:08.623935-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(52569)
default	13:16:08.624758-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(52569)
default	13:16:08.625432-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(52569)
default	13:16:08.627798-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:52569 called from <private>
default	13:16:08.621869-0500	runningboardd	Invalidating assertion 394-328-1287794 (target:[app<application.com.nexy.assistant.41851965.41851974(501)>:3734]) from originator [osservice<com.apple.powerd>:328]
default	13:16:08.627847-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:52569 called from <private>
default	13:16:08.640074-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:52577 called from <private>
default	13:16:08.640301-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(52577)
default	13:16:08.640429-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(52569)
default	13:16:08.640443-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:52569 called from <private>
default	13:16:08.640449-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:52569 called from <private>
default	13:16:08.641247-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(52577)
default	13:16:08.645179-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:52577 called from <private>
default	13:16:08.645205-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:52577 called from <private>
default	13:16:08.646940-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=395.9247, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=3734, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	13:16:08.645241-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:52577 called from <private>
default	13:16:08.645268-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:52577 called from <private>
default	13:16:08.664618-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x7db984040)
default	13:16:08.673194-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:16:08.674091-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x7db984040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	13:16:08.669981-0500	tccd	AUTHREQ_SUBJECT: msgID=395.9247, subject=com.nexy.assistant,
default	13:16:08.674103-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x7db984040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	13:16:08.674110-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	13:16:08.675451-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0x7db984040) Device ID: 83 (Input:No | Output:Yes): true
default	13:16:08.676229-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:16:08.675463-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x7db984040)
default	13:16:08.675584-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x54]:  2 ch,  24000 Hz, Float32, interleaved
default	13:16:08.675594-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	13:16:08.675601-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  24000 Hz, Float32, interleaved
default	13:16:08.675648-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	13:16:08.675712-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	13:16:08.676316-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
error	13:16:08.683190-0500	audioaccessoryd	Relaying via 24B92680-715A-E821-B5AF-358E78C2DAF9 inWxAddress 1C:77:54:18:C8:A3 to 88:20:0D:45:06:51 with options {
    "playingApp" : "com.nexy.assistant",
    "hostStreamingState" : "NO",
    "btAddress" : "A0:9A:8E:0D:58:86",
    "btName" : "Mac",
    "otherDeviceAudioCategory" : 200,
}
default	13:16:08.683326-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	13:16:08.681771-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(52577)
default	13:16:08.682034-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:52569 called from <private>
default	13:16:08.695151-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:52569 called from <private>
default	13:16:08.695157-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:52569 called from <private>
default	13:16:08.695523-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0x7d9f1f390, from  2 ch,  48000 Hz, Float32, deinterleaved to  2 ch,  24000 Hz, Float32, interleaved
default	13:16:08.695615-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:16:08.710611-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:16:08.710627-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:16:08.710645-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:16:08.710653-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:16:08.710660-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:16:08.710666-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	13:16:08.711075-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	13:16:08.711102-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:16:08.711127-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:16:08.711154-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:16:08.711186-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:16:08.711338-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:16:08.711359-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	13:16:08.721432-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:16:08.721446-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:16:08.721457-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:16:08.721462-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:16:08.721470-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:16:08.721476-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	13:16:08.721637-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	13:16:08.729233-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:52570 called from <private>
default	13:16:08.741688-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.41851965.41851974(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	13:16:08.742069-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	13:16:08.742136-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	13:16:08.742180-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	13:16:08.748328-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	13:16:08.749735-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=395.9248, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=3734, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	13:16:08.786323-0500	coreaudiod	>>> ADAPT [com.nexy.assistant]
default	13:16:08.789413-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0x87e3f6d00] Created node ADM::com.nexy.assistant_52570.52454.0_airpods noise suppression studio::out-0 with nodeID 1 - reporting period = 10.000000, sample rate = 24000.000000
default	13:16:08.797199-0500	Nexy	         AVAudioEngine.mm:1437  Engine@0x7dabc0630: iounit configuration changed > posting notification
default	13:16:08.828680-0500	coreaudiod	<<< ADAPT [com.nexy.assistant]
default	13:16:08.830120-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.41851965.41851974(501)>:3734] from originator [osservice<com.apple.powerd>:328] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:394-328-1287800 target:3734 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	13:16:08.830207-0500	runningboardd	Assertion 394-328-1287800 (target:[app<application.com.nexy.assistant.41851965.41851974(501)>:3734]) will be created as active
default	13:16:08.836740-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	13:16:08.837198-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(52570)
default	13:16:08.837587-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:52570 called from <private>
default	13:16:08.837599-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:52570 called from <private>
default	13:16:08.837611-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:52570 called from <private>
default	13:16:08.844214-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x7d1158000 at /Applications/Nexy.app
default	13:16:08.845294-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	13:16:08.845395-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	13:16:08.845487-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	13:16:08.848500-0500	runningboardd	[app<application.com.nexy.assistant.41851965.41851974(501)>:3734] Ignoring jetsam update because this process is not memory-managed
default	13:16:08.848516-0500	runningboardd	[app<application.com.nexy.assistant.41851965.41851974(501)>:3734] Ignoring suspend because this process is not lifecycle managed
default	13:16:08.848531-0500	runningboardd	[app<application.com.nexy.assistant.41851965.41851974(501)>:3734] Ignoring GPU update because this process is not GPU managed
default	13:16:08.848731-0500	runningboardd	[app<application.com.nexy.assistant.41851965.41851974(501)>:3734] Ignoring memory limit update because this process is not memory-managed
default	13:16:08.852926-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.41851965.41851974(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	13:16:08.853334-0500	gamepolicyd	Received state update for 3734 (app<application.com.nexy.assistant.41851965.41851974(501)>, running-active-NotVisible
default	13:16:08.869875-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.41851965.41851974(501)>:3734] from originator [osservice<com.apple.powerd>:328] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:394-328-1287801 target:3734 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	13:16:08.869947-0500	runningboardd	Assertion 394-328-1287801 (target:[app<application.com.nexy.assistant.41851965.41851974(501)>:3734]) will be created as active
default	13:16:08.880738-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	13:16:08.880863-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	13:16:08.880964-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	13:16:08.881347-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:16:08.881361-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:16:08.881372-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:16:08.881381-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:16:08.881390-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:16:08.881397-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	13:16:08.881417-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:16:08.881428-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:16:08.881437-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:16:08.881443-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:16:08.881450-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:16:08.881457-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	13:16:08.881655-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	13:16:08.963227-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xa}
default	13:16:08.963521-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1f482f","name":"Nexy(3734)"}, "details":{"deviceUIDs":[],"implicit_category":"","input_running":false,"output_running":false} }
default	13:16:08.963623-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 2093, PID = 3734, Name = sid:0x1f482f, Nexy(3734), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	13:16:08.963679-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 2093, PID = 3734, Name = sid:0x1f482f, Nexy(3734), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	13:16:08.963710-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1f482f, Nexy(3734), 'prim'', displayID:'com.nexy.assistant'}
default	13:16:08.963759-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1f482f, Nexy(3734), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 2093 stopping recording
default	13:16:08.963787-0500	audiomxd	-MXCoreSession- -[MXCoreSession endInterruption:]: Session <ID: 2093, PID = 3734, Name = sid:0x1f482f, Nexy(3734), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> is going inactive
default	13:16:08.963787-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	13:16:08.963819-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 2093, PID = 3734, Name = sid:0x1f482f, Nexy(3734), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	13:16:08.963857-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 2093, PID = 3734, Name = sid:0x1f482f, Nexy(3734), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	13:16:08.963989-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 0]. BT device UIDS: {(
)}
default	13:16:08.964009-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	13:16:08.964068-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 200 flag 0x1 < Hijack > app com.nexy.assistant CID 0x72200001 category Not set
default	13:16:08.964283-0500	audiomxd	UpdateAudioState CID 0x72200001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	13:16:08.964323-0500	audiomxd	UpdateAudioState CID 0x72200001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:16:08.964360-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	13:16:08.964399-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	13:16:08.964435-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	13:16:08.964459-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:16:08.964518-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	13:16:08.964528-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:16:08.964538-0500	audioaccessoryd	AudioStateChanged: Removed audio session app com.nexy.assistant 201 count 0
default	13:16:08.966042-0500	runningboardd	Invalidating assertion 394-328-1287801 (target:[app<application.com.nexy.assistant.41851965.41851974(501)>:3734]) from originator [osservice<com.apple.powerd>:328]
default	13:16:08.967382-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	13:16:08.968797-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:16:08.968842-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:16:08.968852-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:16:08.968857-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:16:08.968863-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:16:08.968868-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	13:16:08.968930-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	13:16:09.064573-0500	Nexy	                AUHAL.cpp:473   ~AUHAL: (0x7db985540) Selecting device 0 from destructor
default	13:16:09.064588-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0x7db985540)
default	13:16:09.064594-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0x7db985540) not already running
default	13:16:09.064600-0500	Nexy	                AUHAL.cpp:687   SelectDevice: (0x7db985540) disconnecting device 89
default	13:16:09.064608-0500	Nexy	                AUHAL.cpp:751   SelectDevice: (0x7db985540) destroying ioproc 0xa for device 89
default	13:16:09.064651-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xa}
default	13:16:09.064692-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	13:16:09.064882-0500	Nexy	                AUHAL.cpp:853   SelectDevice: (0x7db985540) nothing to setup
default	13:16:09.064896-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x7db985540) adding 0 device listeners to device 0
default	13:16:09.064903-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x7db985540) adding 0 device delegate listeners to device 0
default	13:16:09.064909-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x7db985540) removing 7 device listeners from device 89
default	13:16:09.065144-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x7db985540) removing 0 device delegate listeners from device 89
default	13:16:09.065162-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0x7db985540)
default	13:16:09.070425-0500	Nexy	[0x7dab61400] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
error	13:16:09.071470-0500	tccd	TCCDProcess: identifier=com.nexy.assistant, pid=3734, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy attempted to call TCCAccessRequest for kTCCServiceAccessibility without the recommended com.apple.private.tcc.manager.check-by-audit-token entitlement
default	13:16:09.071763-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=3734.3, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=3734, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.nexy.assistant, pid=3734, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	13:16:09.073379-0500	runningboardd	[app<application.com.nexy.assistant.41851965.41851974(501)>:3734] Ignoring jetsam update because this process is not memory-managed
default	13:16:09.073395-0500	runningboardd	[app<application.com.nexy.assistant.41851965.41851974(501)>:3734] Ignoring suspend because this process is not lifecycle managed
default	13:16:09.073453-0500	tccd	AUTHREQ_SUBJECT: msgID=3734.3, subject=com.nexy.assistant,
default	13:16:09.073406-0500	runningboardd	[app<application.com.nexy.assistant.41851965.41851974(501)>:3734] Ignoring GPU update because this process is not GPU managed
default	13:16:09.073426-0500	runningboardd	[app<application.com.nexy.assistant.41851965.41851974(501)>:3734] Ignoring memory limit update because this process is not memory-managed
default	13:16:09.074534-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21255200 at /Applications/Nexy.app
default	13:16:09.076878-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.41851965.41851974(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	13:16:09.077568-0500	gamepolicyd	Received state update for 3734 (app<application.com.nexy.assistant.41851965.41851974(501)>, running-active-NotVisible
default	13:16:09.093915-0500	Nexy	[0x7dab61400] invalidated after the last release of the connection object
default	13:16:09.094036-0500	Nexy	[0x7dab61400] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
error	13:16:09.094558-0500	tccd	TCCDProcess: identifier=com.nexy.assistant, pid=3734, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy attempted to call TCCAccessRequest for kTCCServiceAccessibility without the recommended com.apple.private.tcc.manager.check-by-audit-token entitlement
default	13:16:09.094772-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=3734.4, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=3734, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.nexy.assistant, pid=3734, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	13:16:09.096029-0500	tccd	AUTHREQ_SUBJECT: msgID=3734.4, subject=com.nexy.assistant,
default	13:16:09.096872-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21255200 at /Applications/Nexy.app
default	13:16:09.111736-0500	Nexy	[0x7dab61400] invalidated after the last release of the connection object
default	13:16:09.111840-0500	Nexy	[0x7dab61400] activating connection: mach=true listener=false peer=false name=com.apple.universalaccessAuthWarn
default	13:16:09.111982-0500	Nexy	[0x7dab61400] invalidated after the last release of the connection object
default	13:16:09.230977-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21255e00 at /Applications/Nexy.app
default	13:16:09.259857-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21254300 at /Applications/Nexy.app
default	13:16:09.266345-0500	tccd	Publishing <TCCDEvent: type=Modify, service=kTCCServiceAccessibility, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 0 subscribers: {
}
default	13:16:09.420078-0500	tccd	AUTHREQ_SUBJECT: msgID=3750.1, subject=com.nexy.assistant,
default	13:16:09.421302-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21255200 at /Applications/Nexy.app
default	13:16:09.449975-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=387.11102, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=3734, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.osascript, pid=3750, auid=501, euid=501, binary_path=/usr/bin/osascript}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=387, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	13:16:09.451095-0500	tccd	AUTHREQ_SUBJECT: msgID=387.11102, subject=com.nexy.assistant,
default	13:16:09.451859-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21255200 at /Applications/Nexy.app
default	13:16:09.512028-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21254300 at /Applications/Nexy.app
default	13:16:09.671408-0500	System Events	TCCAccessRequestIndirect: TCCAccessRequestIndirect with pid 3752: target_identity: {
    kTCCCodeIdentityAuditToken = {length = 32, bytes = 0xf5010000 f5010000 14000000 f5010000 ... b7860100 4e0a3600 };
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
default	13:16:09.685561-0500	tccd	target_executable_path_URL: file:///Applications/Nexy.app/Contents/MacOS/Nexy
default	13:16:09.694396-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x7d1158300 at /Applications/Nexy.app
default	13:16:09.710989-0500	tccd	Prompting for access to indirect object System Events by Nexy
default	13:16:10.132883-0500	Nexy	[0x7dab61540] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	13:16:10.134193-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=3734.5, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=3734, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	13:16:10.135823-0500	tccd	AUTHREQ_SUBJECT: msgID=3734.5, subject=com.nexy.assistant,
default	13:16:10.136817-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21255200 at /Applications/Nexy.app
default	13:16:10.158175-0500	Nexy	[0x7dab61540] invalidated after the last release of the connection object
default	13:16:10.259603-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=3754.1, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=3734, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.osascript, pid=3754, auid=501, euid=501, binary_path=/usr/bin/osascript}, },
default	13:16:10.261212-0500	tccd	AUTHREQ_SUBJECT: msgID=3754.1, subject=com.nexy.assistant,
default	13:16:10.261993-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21255200 at /Applications/Nexy.app
default	13:16:10.282594-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=387.11108, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=3734, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.osascript, pid=3754, auid=501, euid=501, binary_path=/usr/bin/osascript}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=387, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	13:16:10.283436-0500	tccd	AUTHREQ_SUBJECT: msgID=387.11108, subject=com.nexy.assistant,
default	13:16:10.284126-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21255200 at /Applications/Nexy.app
default	13:16:10.324549-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21254300 at /Applications/Nexy.app
default	13:16:10.970000-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x7d1158900 at /Applications/Nexy.app
default	13:16:10.979558-0500	System Events	TCCAccessRequestIndirect: TCCAccessRequestIndirect with pid 3752: target_identity: {
    kTCCCodeIdentityAuditToken = {length = 32, bytes = 0xf5010000 f5010000 14000000 f5010000 ... b7860100 590a3600 };
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
default	13:16:10.978862-0500	tccd	Publishing <TCCDEvent: type=Create, service=kTCCServiceAppleEvents, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 3 subscribers: {
    474 = "<TCCDEventSubscriber: token=474, state=Passed, csid=com.apple.photolibraryd>";
    472 = "<TCCDEventSubscriber: token=472, state=Passed, csid=com.apple.chronod>";
    37 = "<TCCDEventSubscriber: token=37, state=Initial, csid=(null)>";
}
default	13:16:10.981473-0500	chronod	[appAuth:com.nexy.assistant] tcc authorization(s) changed
default	13:16:10.994687-0500	tccd	target_executable_path_URL: file:///Applications/Nexy.app/Contents/MacOS/Nexy
default	13:16:11.133327-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=3755.1, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=3734, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.osascript, pid=3755, auid=501, euid=501, binary_path=/usr/bin/osascript}, },
default	13:16:11.134648-0500	tccd	AUTHREQ_SUBJECT: msgID=3755.1, subject=com.nexy.assistant,
default	13:16:11.135348-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21255200 at /Applications/Nexy.app
default	13:16:11.154500-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=387.11113, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=3734, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.osascript, pid=3755, auid=501, euid=501, binary_path=/usr/bin/osascript}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=387, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	13:16:11.155345-0500	tccd	AUTHREQ_SUBJECT: msgID=387.11113, subject=com.nexy.assistant,
default	13:16:11.156006-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21255200 at /Applications/Nexy.app
default	13:16:11.203054-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21254300 at /Applications/Nexy.app
default	13:16:11.236057-0500	System Events	TCCAccessRequestIndirect: TCCAccessRequestIndirect with pid 3752: target_identity: {
    kTCCCodeIdentityAuditToken = {length = 32, bytes = 0xf5010000 f5010000 14000000 f5010000 ... b7860100 5b0a3600 };
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
default	13:16:11.251609-0500	tccd	target_executable_path_URL: file:///Applications/Nexy.app/Contents/MacOS/Nexy
default	13:16:11.441231-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(52577)
default	13:16:11.441319-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:52577 called from <private>
default	13:16:11.441329-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:52577 called from <private>
default	13:16:11.442255-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(52569)
default	13:16:11.442286-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:52569 called from <private>
default	13:16:11.442295-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:52569 called from <private>
default	13:16:11.443649-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(52577)
default	13:16:11.443679-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(52570)
default	13:16:11.443883-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:52577 called from <private>
default	13:16:11.444051-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:52570 called from <private>
default	13:16:11.444072-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:52577 called from <private>
default	13:16:11.444093-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:52570 called from <private>
default	13:16:11.457046-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:52569 called from <private>
default	13:16:11.457091-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:52569 called from <private>
default	13:16:11.457954-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(52569)
default	13:16:11.457986-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:52569 called from <private>
default	13:16:11.457993-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:52569 called from <private>
default	13:16:11.460011-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(52569)
default	13:16:11.460159-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(52569)
default	13:16:11.460174-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(52569)
default	13:16:11.463196-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:52569 called from <private>
default	13:16:11.463231-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:52569 called from <private>
default	13:16:11.463248-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:52569 called from <private>
default	13:16:11.463259-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:52569 called from <private>
default	13:16:11.463280-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:52569 called from <private>
default	13:16:11.463289-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:52569 called from <private>
default	13:16:11.463294-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:52569 called from <private>
default	13:16:11.463320-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:52569 called from <private>
default	13:16:11.475213-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:52577 called from <private>
default	13:16:11.475248-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:52577 called from <private>
default	13:16:11.475557-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(52577)
default	13:16:11.475589-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(52570)
default	13:16:11.475605-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:52570 called from <private>
default	13:16:11.475610-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:52570 called from <private>
default	13:16:11.476212-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(52577)
default	13:16:11.476428-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:52569 called from <private>
default	13:16:11.476439-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:52569 called from <private>
default	13:16:11.476744-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(52569)
default	13:16:11.476767-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:52569 called from <private>
default	13:16:11.476773-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:52569 called from <private>
default	13:16:11.478598-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(52569)
default	13:16:11.478878-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:52569 called from <private>
default	13:16:11.478890-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:52569 called from <private>
default	13:16:11.478924-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:52569 called from <private>
default	13:16:11.478935-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:52569 called from <private>
default	13:16:11.479742-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	13:16:11.480055-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	13:16:11.481281-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(52577)
default	13:16:11.481304-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(52569)
default	13:16:11.481321-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(52577)
default	13:16:11.481328-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(52569)
default	13:16:11.481338-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:52569 called from <private>
default	13:16:11.481345-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:52569 called from <private>
default	13:16:11.481353-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:52569 called from <private>
default	13:16:11.481498-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:52569 called from <private>
default	13:16:11.481618-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:52577 called from <private>
default	13:16:11.481630-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:52577 called from <private>
default	13:16:11.481762-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:52577 called from <private>
default	13:16:11.481843-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(52569)
default	13:16:11.481975-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:52577 called from <private>
default	13:16:11.482004-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:52577 called from <private>
default	13:16:11.482027-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:52577 called from <private>
default	13:16:11.482088-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:52577 called from <private>
default	13:16:11.482120-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:52577 called from <private>
default	13:16:11.482182-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:52577 called from <private>
default	13:16:11.482369-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:52577 called from <private>
default	13:16:11.496486-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:52569 called from <private>
default	13:16:11.496520-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:52569 called from <private>
default	13:16:11.496670-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(52569)
default	13:16:11.499675-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(52569)
default	13:16:11.499988-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:52569 called from <private>
default	13:16:11.499998-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:52569 called from <private>
default	13:16:11.500053-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:52569 called from <private>
default	13:16:11.500061-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:52569 called from <private>
default	13:16:11.500068-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:52569 called from <private>
default	13:16:11.500076-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:52569 called from <private>
default	13:16:11.500106-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:52569 called from <private>
default	13:16:11.500138-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:52569 called from <private>
default	13:16:11.500299-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0x7db984040) Device ID: 83 (Input:No | Output:Yes): true
default	13:16:11.500315-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x7db984040)
default	13:16:11.500614-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x54]:  2 ch,  48000 Hz, Float32, interleaved
default	13:16:11.500626-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	13:16:11.500653-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	13:16:11.500850-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	13:16:11.500941-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	13:16:11.501902-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0x7d9f18240, from  2 ch,  48000 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	13:16:11.502049-0500	Nexy	       AudioConverter.cpp:1317  AudioConverter -> 0x7d9f18240: The in-process GetProperty call returned 1886547824 for property 1886546285 with size 8.
default	13:16:11.502113-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:16:11.502233-0500	Nexy	AudioConverter -> 0x7d9f18240: The in-process SetProperty call returned 1886547824 for property 1936876385 with size 4.
default	13:16:11.502506-0500	Nexy	AudioConverter -> 0x7d9f18240: The in-process SetProperty call returned 1886547824 for property 1936876401 with size 4.
default	13:16:11.502518-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x7db984040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	13:16:11.502578-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x7db984040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	13:16:11.502666-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	13:16:11.502532-0500	Nexy	AudioConverter -> 0x7d9f18240: The in-process SetProperty call returned 1886547824 for property 1886547309 with size 4.
default	13:16:11.505459-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0x7db984040) Device ID: 83 (Input:No | Output:Yes): true
default	13:16:11.505482-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x7db984040)
default	13:16:11.506175-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x54]:  2 ch,  48000 Hz, Float32, interleaved
default	13:16:11.506186-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	13:16:11.506234-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	13:16:11.506289-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	13:16:11.506346-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	13:16:11.508672-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0x7d9f182a0, from  2 ch,  48000 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	13:16:11.508827-0500	Nexy	       AudioConverter.cpp:1317  AudioConverter -> 0x7d9f182a0: The in-process GetProperty call returned 1886547824 for property 1886546285 with size 8.
default	13:16:11.508938-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:16:11.509797-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x7db984040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	13:16:11.509948-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x7db984040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	13:16:11.510070-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	13:16:11.509325-0500	Nexy	AudioConverter -> 0x7d9f182a0: The in-process SetProperty call returned 1886547824 for property 1936876385 with size 4.
default	13:16:11.510786-0500	Nexy	AudioConverter -> 0x7d9f182a0: The in-process SetProperty call returned 1886547824 for property 1936876401 with size 4.
default	13:16:11.510823-0500	Nexy	AudioConverter -> 0x7d9f182a0: The in-process SetProperty call returned 1886547824 for property 1886547309 with size 4.
default	13:16:11.622749-0500	Nexy	         AVAudioEngine.mm:1437  Engine@0x7dabc0630: iounit configuration changed > posting notification
default	13:16:11.705960-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=3756.1, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=3734, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.osascript, pid=3756, auid=501, euid=501, binary_path=/usr/bin/osascript}, },
default	13:16:11.707858-0500	tccd	AUTHREQ_SUBJECT: msgID=3756.1, subject=com.nexy.assistant,
default	13:16:11.708719-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21255200 at /Applications/Nexy.app
default	13:16:11.730941-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=387.11114, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=3734, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.osascript, pid=3756, auid=501, euid=501, binary_path=/usr/bin/osascript}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=387, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	13:16:11.732022-0500	tccd	AUTHREQ_SUBJECT: msgID=387.11114, subject=com.nexy.assistant,
default	13:16:11.732799-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21255200 at /Applications/Nexy.app
default	13:16:11.776509-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21254300 at /Applications/Nexy.app
default	13:16:11.805286-0500	System Events	TCCAccessRequestIndirect: TCCAccessRequestIndirect with pid 3752: target_identity: {
    kTCCCodeIdentityAuditToken = {length = 32, bytes = 0xf5010000 f5010000 14000000 f5010000 ... b7860100 5d0a3600 };
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
default	13:16:11.819921-0500	tccd	target_executable_path_URL: file:///Applications/Nexy.app/Contents/MacOS/Nexy
default	13:16:11.873260-0500	Nexy	[0x7dab61680] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	13:16:11.873835-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=3734.6, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=3734, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	13:16:11.875232-0500	tccd	AUTHREQ_SUBJECT: msgID=3734.6, subject=com.nexy.assistant,
default	13:16:11.876149-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21255200 at /Applications/Nexy.app
default	13:16:11.890136-0500	tccd	Notifying for access  kTCCServiceScreenCapture for target PID[3734], responsiblePID[3734], responsiblePath: /Applications/Nexy.app to UID: 501
default	13:16:11.890381-0500	Nexy	[0x7dab61680] invalidated after the last release of the connection object
default	13:16:11.944761-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21255e00 at /Applications/Nexy.app
default	13:16:11.968240-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21254300 at /Applications/Nexy.app
default	13:16:11.972462-0500	tccd	Publishing <TCCDEvent: type=Modify, service=kTCCServiceScreenCapture, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 0 subscribers: {
}
default	13:16:14.428844-0500	Nexy	NotifyToken::RegisterDispatch(user.uid.501.com.apple.LaunchServices.database) fired for session key <private>
error	13:16:14.785124-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAccessibility com.nexy.assistant none
error	13:16:14.860857-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAppleEvents com.nexy.assistant full
error	13:16:14.860858-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAppleEvents com.nexy.assistant full
error	13:16:14.864324-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceMicrophone com.nexy.assistant full
default	13:16:14.924438-0500	nehelper	Received an apps uninstalled notification with bundle IDs (
    "com.nexy.assistant"
)
default	13:16:15.522703-0500	nehelper	Removing UUIDs for (
    "com.nexy.assistant"
)
default	13:16:15.525374-0500	nehelper	Handling an apps uninstalled notification with bundle IDs (
    "com.nexy.assistant"
)
default	13:16:15.538567-0500	nehelper	com.apple.preferences.networkprivacy-F67B3EA9-90A6-470B-B321-9BBD719C692B: Populating the cache with 2 UUID(s) for com.nexy.assistant
default	13:16:15.737165-0500	Nexy	LSExceptions shared instance invalidated for timeout.
default	13:16:18.654608-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21255e00 at /Applications/Nexy.app
default	13:16:18.676975-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21254300 at /Applications/Nexy.app
default	13:16:18.686424-0500	tccd	Publishing <TCCDEvent: type=Modify, service=kTCCServiceScreenCapture, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 0 subscribers: {
}
error	13:16:18.805726-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAccessibility com.nexy.assistant none
error	13:16:18.806385-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceScreenCapture com.nexy.assistant full
error	13:16:18.807751-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAccessibility com.nexy.assistant none
error	13:16:18.807975-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceScreenCapture com.nexy.assistant full
error	13:16:18.841351-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAppleEvents com.nexy.assistant full
error	13:16:18.841717-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAppleEvents com.nexy.assistant full
error	13:16:18.842298-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceMicrophone com.nexy.assistant full
error	13:16:18.842858-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceMicrophone com.nexy.assistant full
default	13:16:26.913882-0500	Nexy	[0x7dab61680] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	13:16:26.915612-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=3734.7, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=3734, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	13:16:26.919960-0500	tccd	AUTHREQ_SUBJECT: msgID=3734.7, subject=com.nexy.assistant,
default	13:16:26.921452-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21255200 at /Applications/Nexy.app
default	13:16:26.948880-0500	Nexy	[0x7dab61680] invalidated after the last release of the connection object
default	13:16:42.094289-0500	Nexy	                AUHAL.cpp:420   AUHAL: (0x7db985540) Selecting device 83 from constructor
default	13:16:42.094331-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0x7db985540)
default	13:16:42.094351-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0x7db985540) not already running
default	13:16:42.094367-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0x7db985540) nothing to teardown
default	13:16:42.094379-0500	Nexy	                AUHAL.cpp:762   SelectDevice: (0x7db985540) connecting device 83
default	13:16:42.094669-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0x7db985540) Device ID: 83 (Input:No | Output:Yes): true
default	13:16:42.095057-0500	Nexy	                AUHAL.cpp:774   SelectDevice: (0x7db985540) created ioproc 0xc for device 83
default	13:16:42.095416-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x7db985540) adding 7 device listeners to device 83
default	13:16:42.095794-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x7db985540) adding 0 device delegate listeners to device 83
default	13:16:42.095810-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x7db985540)
default	13:16:42.095976-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x54]:  2 ch,  48000 Hz, Float32, interleaved
default	13:16:42.095995-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	13:16:42.096008-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	13:16:42.096021-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	13:16:42.096035-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	13:16:42.096229-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x7db985540) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	13:16:42.096251-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x7db985540) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	13:16:42.096261-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	13:16:42.096270-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x7db985540) removing 0 device listeners from device 0
default	13:16:42.096276-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x7db985540) removing 0 device delegate listeners from device 0
default	13:16:42.096286-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0x7db985540)
default	13:16:42.096317-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is DISABLED
default	13:16:42.096421-0500	Nexy	                AUHAL.cpp:2303  SetProperty: (0x7db985540) caller requesting device change from 83 to 89
default	13:16:42.096435-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0x7db985540)
default	13:16:42.096443-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0x7db985540) not already running
default	13:16:42.096451-0500	Nexy	                AUHAL.cpp:687   SelectDevice: (0x7db985540) disconnecting device 83
default	13:16:42.096458-0500	Nexy	                AUHAL.cpp:751   SelectDevice: (0x7db985540) destroying ioproc 0xc for device 83
default	13:16:42.096498-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped Unknown {1C-77-54-18-C8-A3:output, 0xc}
default	13:16:42.096560-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	13:16:42.096709-0500	Nexy	                AUHAL.cpp:762   SelectDevice: (0x7db985540) connecting device 89
default	13:16:42.096851-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0x7db985540) Device ID: 89 (Input:Yes | Output:No): true
default	13:16:42.100352-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=395.9250, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=3734, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	13:16:42.103637-0500	tccd	AUTHREQ_SUBJECT: msgID=395.9250, subject=com.nexy.assistant,
default	13:16:42.104842-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x7d1158000 at /Applications/Nexy.app
default	13:16:42.131686-0500	Nexy	                AUHAL.cpp:774   SelectDevice: (0x7db985540) created ioproc 0xb for device 89
default	13:16:42.131860-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x7db985540) adding 7 device listeners to device 89
default	13:16:42.132040-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x7db985540) adding 0 device delegate listeners to device 89
default	13:16:42.132050-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x7db985540)
default	13:16:42.132066-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 output streams; not all mono
default	13:16:42.132081-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	13:16:42.132211-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  input stream 0 [0x5a]:  1 ch,  24000 Hz, Float32
default	13:16:42.132219-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 input streams; all mono
default	13:16:42.132225-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  1 ch,  24000 Hz, Float32
default	13:16:42.132325-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x7db985540) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	13:16:42.132334-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x7db985540) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	13:16:42.132339-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	13:16:42.132344-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x7db985540) removing 7 device listeners from device 83
default	13:16:42.132493-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x7db985540) removing 0 device delegate listeners from device 83
default	13:16:42.132500-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0x7db985540)
default	13:16:42.132519-0500	Nexy	AudioHardware-mac-imp.cpp:1306   AudioObjectAddPropertyListener: listener was already added
default	13:16:42.132864-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	13:16:42.134175-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=395.9251, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=3734, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	13:16:42.135364-0500	tccd	AUTHREQ_SUBJECT: msgID=395.9251, subject=com.nexy.assistant,
default	13:16:42.135996-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x7d1158000 at /Applications/Nexy.app
default	13:16:42.152772-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0x7d9f1f360, from  1 ch,  24000 Hz, Float32 to  1 ch,  16000 Hz, Float32
default	13:16:42.153028-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	13:16:42.154017-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=395.9252, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=3734, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	13:16:42.155095-0500	tccd	AUTHREQ_SUBJECT: msgID=395.9252, subject=com.nexy.assistant,
default	13:16:42.155715-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x7d1158000 at /Applications/Nexy.app
default	13:16:42.173394-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=395.9253, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=3734, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	13:16:42.174348-0500	tccd	AUTHREQ_SUBJECT: msgID=395.9253, subject=com.nexy.assistant,
default	13:16:42.174923-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x7d1158000 at /Applications/Nexy.app
default	13:16:42.192421-0500	coreaudiod	>>> NEGOTIATE [com.nexy.assistant]
default	13:16:42.192756-0500	coreaudiod	<<< NEGOTIATE [com.nexy.assistant]
default	13:16:42.195257-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:52570 called from <private>
default	13:16:42.195333-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Input {1C-77-54-18-C8-A3:input, 0xb}
default	13:16:42.195369-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	13:16:42.197484-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:52570 called from <private>
default	13:16:42.197736-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(52577)
default	13:16:42.197761-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:52577 called from <private>
default	13:16:42.197767-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:52577 called from <private>
default	13:16:42.197794-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(52569)
default	13:16:42.198338-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:52569 called from <private>
default	13:16:42.198837-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:52569 called from <private>
default	13:16:42.199677-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(52570)
default	13:16:42.199700-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:52570 called from <private>
default	13:16:42.199709-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:52570 called from <private>
default	13:16:42.204592-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(52577)
default	13:16:42.204610-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:52577 called from <private>
default	13:16:42.204617-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:52577 called from <private>
default	13:16:42.209916-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	13:16:42.210621-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	13:16:42.213475-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(52570)
default	13:16:42.213515-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(52570)
default	13:16:42.213531-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(52570)
default	13:16:42.213542-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(52570)
default	13:16:42.214716-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:52570 called from <private>
default	13:16:42.214725-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:52570 called from <private>
default	13:16:42.214747-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:52570 called from <private>
default	13:16:42.214757-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:52570 called from <private>
default	13:16:42.216555-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1f482f","name":"Nexy(3734)"}, "details":{"deviceUIDs":["1C-77-54-18-C8-A3:input"],"implicit_category":"Record","input_running":true,"output_running":false} }
default	13:16:42.216661-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 2093, PID = 3734, Name = sid:0x1f482f, Nexy(3734), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	13:16:42.216705-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Category/Mode changed -- The score for sid:0x1f482f, Nexy(3734), 'prim'/com.nexy.assistant was not correct. Old score = 201
default	13:16:42.216733-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 2093, PID = 3734, Name = sid:0x1f482f, Nexy(3734), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	13:16:42.217067-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 2093, PID = 3734, Name = sid:0x1f482f, Nexy(3734), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	13:16:42.217256-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 2093, PID = 3734, Name = sid:0x1f482f, Nexy(3734), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	13:16:42.214765-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:52570 called from <private>
default	13:16:42.216517-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.41851965.41851974(501)>:3734] from originator [osservice<com.apple.powerd>:328] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:394-328-1287946 target:3734 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	13:16:42.214824-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:52570 called from <private>
default	13:16:42.215513-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:52570 called from <private>
default	13:16:42.215565-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:52570 called from <private>
default	13:16:42.216886-0500	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1f482f, Nexy(3734), 'prim'', AudioCategory changed to 'Record_WithBluetooth'
default	13:16:42.215677-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:52570 called from <private>
default	13:16:42.217499-0500	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 2093, PID = 3734, Name = sid:0x1f482f, Nexy(3734), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> is going active
default	13:16:42.217536-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1f482f, Nexy(3734), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 2093 starting recording
default	13:16:42.218261-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 2093, PID = 3734, Name = sid:0x1f482f, Nexy(3734), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	13:16:42.215840-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:52570 called from <private>
default	13:16:42.217637-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:52569 called from <private>
default	13:16:42.216897-0500	runningboardd	Assertion 394-328-1287946 (target:[app<application.com.nexy.assistant.41851965.41851974(501)>:3734]) will be created as active
default	13:16:42.217722-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:52569 called from <private>
default	13:16:42.218491-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 2093, PID = 3734, Name = sid:0x1f482f, Nexy(3734), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	13:16:42.217957-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(52569)
default	13:16:42.218110-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:52569 called from <private>
default	13:16:42.218228-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:52569 called from <private>
default	13:16:42.220485-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1f482f, Nexy(3734), 'prim'', displayID:'com.nexy.assistant'}
default	13:16:42.217736-0500	audiomxd	UpdateAudioState CID 0x72200001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:16:42.221384-0500	audiomxd	UpdateAudioState CID 0x72200001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:16:42.224431-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	13:16:42.223428-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:16:42.220916-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [1, 0]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:input"
)}
default	13:16:42.224303-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:16:42.220968-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	13:16:42.223963-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(52569)
default	13:16:42.235037-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:52569 called from <private>
default	13:16:42.235049-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:52569 called from <private>
default	13:16:42.235058-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:52569 called from <private>
default	13:16:42.235069-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:52569 called from <private>
default	13:16:42.237930-0500	runningboardd	[app<application.com.nexy.assistant.41851965.41851974(501)>:3734] Ignoring jetsam update because this process is not memory-managed
default	13:16:42.238043-0500	runningboardd	[app<application.com.nexy.assistant.41851965.41851974(501)>:3734] Ignoring suspend because this process is not lifecycle managed
default	13:16:42.238105-0500	runningboardd	[app<application.com.nexy.assistant.41851965.41851974(501)>:3734] Ignoring GPU update because this process is not GPU managed
default	13:16:42.238218-0500	runningboardd	[app<application.com.nexy.assistant.41851965.41851974(501)>:3734] Ignoring memory limit update because this process is not memory-managed
default	13:16:42.247268-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(52569)
default	13:16:42.247287-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:52569 called from <private>
default	13:16:42.247292-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:52569 called from <private>
default	13:16:42.247376-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(52577)
default	13:16:42.247400-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(52570)
default	13:16:42.247416-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(52569)
default	13:16:42.247426-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:52570 called from <private>
default	13:16:42.247438-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:52569 called from <private>
default	13:16:42.247813-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:52569 called from <private>
default	13:16:42.247931-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:52569 called from <private>
default	13:16:42.247989-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:52569 called from <private>
default	13:16:42.248146-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(52569)
default	13:16:42.248203-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:52569 called from <private>
default	13:16:42.248292-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:52569 called from <private>
default	13:16:42.248307-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(52577)
default	13:16:42.248538-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:52577 called from <private>
default	13:16:42.248691-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(52569)
default	13:16:42.248976-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:52569 called from <private>
default	13:16:42.249083-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(52569)
default	13:16:42.249166-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:52569 called from <private>
default	13:16:42.248944-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:52577 called from <private>
default	13:16:42.252854-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:52577 called from <private>
default	13:16:42.252859-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:52577 called from <private>
default	13:16:42.252862-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:52577 called from <private>
default	13:16:42.252896-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:52577 called from <private>
default	13:16:42.252934-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:52577 called from <private>
default	13:16:42.254122-0500	tccd	AUTHREQ_SUBJECT: msgID=395.9254, subject=com.nexy.assistant,
default	13:16:42.254333-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	13:16:42.254718-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	13:16:42.254807-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	13:16:42.261014-0500	gamepolicyd	Received state update for 3734 (app<application.com.nexy.assistant.41851965.41851974(501)>, running-active-NotVisible
default	13:16:42.271364-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0x7d9f1f330, from  2 ch,  48000 Hz, Float32, deinterleaved to  2 ch,  24000 Hz, Float32, interleaved
default	13:16:42.276396-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:16:42.276612-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:16:42.276669-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:16:42.276724-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:16:42.276820-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:16:42.278237-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:16:42.278496-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x7db984040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	13:16:42.278529-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x7db984040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	13:16:42.278537-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	13:16:42.292589-0500	coreaudiod	>>> NEGOTIATE [com.nexy.assistant]
default	13:16:42.299329-0500	runningboardd	Invalidating assertion 394-328-1287947 (target:[app<application.com.nexy.assistant.41851965.41851974(501)>:3734]) from originator [osservice<com.apple.powerd>:328]
default	13:16:42.298808-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(52570)
default	13:16:42.298821-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:52570 called from <private>
default	13:16:42.298827-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:52570 called from <private>
default	13:16:42.300237-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(52570)
default	13:16:42.300714-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:52570 called from <private>
default	13:16:42.300725-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:52570 called from <private>
default	13:16:42.300767-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:52570 called from <private>
default	13:16:42.302841-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=395.9255, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=3734, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	13:16:42.306904-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x7d1158000 at /Applications/Nexy.app
default	13:16:42.309344-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	13:16:42.309400-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	13:16:42.327841-0500	coreaudiod	>>> ADAPT [com.nexy.assistant]
default	13:16:42.329485-0500	coreaudiod	IssueReporting.cpp:492   RTAID [ use_case=Generic report_type=RMS Generic Chain clientID=ADM node=ADM::com.nexy.assistant_52570.52454.0_airpods noise suppression studio::out-0 issue_detected_sample_time=2160.000000 ] -- [ rms:[-120.000000], peaks:[-240.000000] ]
default	13:16:42.329503-0500	coreaudiod	IssueReporting.cpp:492   RTAID [ use_case=Generic report_type=RMS Generic Chain clientID=ADM node=ADM::com.nexy.assistant_52570.52454.0_airpods noise suppression studio::in-0 issue_detected_sample_time=0.000000 ] -- [ rms:[-120.000000], peaks:[-240.000000] ]
default	13:16:42.329797-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0x87e3f6d00] Created node ADM::com.nexy.assistant_52570.52454.0_airpods noise suppression studio::in-0 with nodeID 0 - reporting period = 10.000000, sample rate = 24000.000000
default	13:16:42.329857-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0x87e3f6d00] Created node ADM::com.nexy.assistant_52570.52454.0_airpods noise suppression studio::out-0 with nodeID 1 - reporting period = 10.000000, sample rate = 24000.000000
default	13:16:42.340564-0500	runningboardd	[app<application.com.nexy.assistant.41851965.41851974(501)>:3734] Ignoring jetsam update because this process is not memory-managed
default	13:16:42.340580-0500	runningboardd	[app<application.com.nexy.assistant.41851965.41851974(501)>:3734] Ignoring suspend because this process is not lifecycle managed
default	13:16:42.340590-0500	runningboardd	[app<application.com.nexy.assistant.41851965.41851974(501)>:3734] Ignoring GPU update because this process is not GPU managed
default	13:16:42.340610-0500	runningboardd	[app<application.com.nexy.assistant.41851965.41851974(501)>:3734] Ignoring memory limit update because this process is not memory-managed
default	13:16:42.343369-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.41851965.41851974(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	13:16:42.348797-0500	gamepolicyd	Received state update for 3734 (app<application.com.nexy.assistant.41851965.41851974(501)>, running-active-NotVisible
default	13:16:42.382915-0500	Nexy	         AVAudioEngine.mm:1437  Engine@0x7dabc0630: iounit configuration changed > posting notification
default	13:16:42.395767-0500	coreaudiod	<<< ADAPT [com.nexy.assistant]
default	13:16:42.398793-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:52570 called from <private>
default	13:16:42.398824-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:52570 called from <private>
default	13:16:42.400876-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	13:16:42.401776-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:52570 called from <private>
default	13:16:42.401885-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.41851965.41851974(501)>:3734] from originator [osservice<com.apple.powerd>:328] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:394-328-1287948 target:3734 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	13:16:42.401905-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(52570)
default	13:16:42.401928-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:52570 called from <private>
default	13:16:42.401936-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:52570 called from <private>
default	13:16:42.402003-0500	runningboardd	Assertion 394-328-1287948 (target:[app<application.com.nexy.assistant.41851965.41851974(501)>:3734]) will be created as active
default	13:16:42.402390-0500	runningboardd	[app<application.com.nexy.assistant.41851965.41851974(501)>:3734] Ignoring jetsam update because this process is not memory-managed
default	13:16:42.402406-0500	runningboardd	[app<application.com.nexy.assistant.41851965.41851974(501)>:3734] Ignoring suspend because this process is not lifecycle managed
default	13:16:42.402422-0500	runningboardd	[app<application.com.nexy.assistant.41851965.41851974(501)>:3734] Ignoring GPU update because this process is not GPU managed
default	13:16:42.402487-0500	runningboardd	[app<application.com.nexy.assistant.41851965.41851974(501)>:3734] Ignoring memory limit update because this process is not memory-managed
default	13:16:42.402939-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	13:16:42.403213-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	13:16:42.403698-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(52570)
default	13:16:42.404181-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:52570 called from <private>
default	13:16:42.404192-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:52570 called from <private>
default	13:16:42.404203-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:52570 called from <private>
default	13:16:42.405430-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=395.9256, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=3734, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	13:16:42.407038-0500	tccd	AUTHREQ_SUBJECT: msgID=395.9256, subject=com.nexy.assistant,
default	13:16:42.407958-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x7d1158000 at /Applications/Nexy.app
default	13:16:42.409071-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.41851965.41851974(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	13:16:42.409493-0500	gamepolicyd	Received state update for 3734 (app<application.com.nexy.assistant.41851965.41851974(501)>, running-active-NotVisible
default	13:16:42.409431-0500	runningboardd	Invalidating assertion 394-328-1287948 (target:[app<application.com.nexy.assistant.41851965.41851974(501)>:3734]) from originator [osservice<com.apple.powerd>:328]
default	13:16:42.410099-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	13:16:42.410156-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	13:16:42.410203-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	13:16:42.410403-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	13:16:42.414602-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:16:42.414612-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:16:42.414623-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:16:42.414628-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:16:42.414649-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:16:42.414659-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	13:16:42.415756-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	13:16:42.419182-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:16:42.419189-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:16:42.419197-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:16:42.419203-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:16:42.419209-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:16:42.419215-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	13:16:42.419312-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	13:16:42.429491-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.41851965.41851974(501)>:3734] from originator [osservice<com.apple.powerd>:328] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:394-328-1287950 target:3734 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	13:16:42.429549-0500	runningboardd	Assertion 394-328-1287950 (target:[app<application.com.nexy.assistant.41851965.41851974(501)>:3734]) will be created as active
default	13:16:42.430201-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:52570 called from <private>
default	13:16:42.438221-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	13:16:42.438268-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	13:16:42.438302-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	13:16:42.438550-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:16:42.438564-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:16:42.438574-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:16:42.438585-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:16:42.438594-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:16:42.438601-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	13:16:42.438657-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:16:42.438671-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:16:42.438698-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:16:42.438705-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:16:42.438713-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:16:42.438719-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	13:16:42.438817-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	13:16:42.439038-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:16:42.439050-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:16:42.439073-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:16:42.439091-0500	ControlCenter	Navigating to new application [com.nexy.assistant]
default	13:16:42.439083-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:16:42.439102-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:16:42.439127-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	13:16:42.522970-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xb}
default	13:16:42.523227-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1f482f","name":"Nexy(3734)"}, "details":{"deviceUIDs":[],"implicit_category":"","input_running":false,"output_running":false} }
default	13:16:42.523314-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 2093, PID = 3734, Name = sid:0x1f482f, Nexy(3734), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	13:16:42.523360-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 2093, PID = 3734, Name = sid:0x1f482f, Nexy(3734), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	13:16:42.523389-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1f482f, Nexy(3734), 'prim'', displayID:'com.nexy.assistant'}
default	13:16:42.523441-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1f482f, Nexy(3734), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 2093 stopping recording
default	13:16:42.523463-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	13:16:42.523466-0500	audiomxd	-MXCoreSession- -[MXCoreSession endInterruption:]: Session <ID: 2093, PID = 3734, Name = sid:0x1f482f, Nexy(3734), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> is going inactive
default	13:16:42.523565-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 2093, PID = 3734, Name = sid:0x1f482f, Nexy(3734), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	13:16:42.523772-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 200 flag 0x1 < Hijack > app com.nexy.assistant CID 0x72200001 category Not set
default	13:16:42.523796-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 0]. BT device UIDS: {(
)}
default	13:16:42.523638-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 2093, PID = 3734, Name = sid:0x1f482f, Nexy(3734), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	13:16:42.523814-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	13:16:42.523983-0500	audiomxd	UpdateAudioState CID 0x72200001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	13:16:42.524022-0500	audiomxd	UpdateAudioState CID 0x72200001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:16:42.524065-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	13:16:42.524111-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	13:16:42.524148-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:16:42.524172-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	13:16:42.524218-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	13:16:42.524228-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:16:42.524236-0500	audioaccessoryd	AudioStateChanged: Removed audio session app com.nexy.assistant 201 count 0
default	13:16:42.525533-0500	runningboardd	Invalidating assertion 394-328-1287950 (target:[app<application.com.nexy.assistant.41851965.41851974(501)>:3734]) from originator [osservice<com.apple.powerd>:328]
default	13:16:42.527220-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	13:16:42.529082-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:16:42.529095-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:16:42.529108-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:16:42.529114-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	13:16:42.529128-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	13:16:42.529134-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	13:16:42.529218-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	13:16:42.624891-0500	Nexy	                AUHAL.cpp:473   ~AUHAL: (0x7db985540) Selecting device 0 from destructor
default	13:16:42.624905-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0x7db985540)
default	13:16:42.624913-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0x7db985540) not already running
default	13:16:42.624918-0500	Nexy	                AUHAL.cpp:687   SelectDevice: (0x7db985540) disconnecting device 89
default	13:16:42.624927-0500	Nexy	                AUHAL.cpp:751   SelectDevice: (0x7db985540) destroying ioproc 0xb for device 89
default	13:16:42.624973-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xb}
default	13:16:42.625027-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	13:16:42.625217-0500	Nexy	                AUHAL.cpp:853   SelectDevice: (0x7db985540) nothing to setup
default	13:16:42.625236-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x7db985540) adding 0 device listeners to device 0
default	13:16:42.625242-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x7db985540) adding 0 device delegate listeners to device 0
default	13:16:42.625251-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x7db985540) removing 7 device listeners from device 89
default	13:16:42.625492-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x7db985540) removing 0 device delegate listeners from device 89
default	13:16:42.625521-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0x7db985540)
default	13:16:42.631078-0500	runningboardd	[app<application.com.nexy.assistant.41851965.41851974(501)>:3734] Ignoring jetsam update because this process is not memory-managed
default	13:16:42.631095-0500	runningboardd	[app<application.com.nexy.assistant.41851965.41851974(501)>:3734] Ignoring suspend because this process is not lifecycle managed
default	13:16:42.631105-0500	runningboardd	[app<application.com.nexy.assistant.41851965.41851974(501)>:3734] Ignoring GPU update because this process is not GPU managed
default	13:16:42.631125-0500	runningboardd	[app<application.com.nexy.assistant.41851965.41851974(501)>:3734] Ignoring memory limit update because this process is not memory-managed
default	13:16:42.633996-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.41851965.41851974(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	13:16:42.634669-0500	gamepolicyd	Received state update for 3734 (app<application.com.nexy.assistant.41851965.41851974(501)>, running-active-NotVisible
default	13:16:42.729217-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=3796.1, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=3734, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.osascript, pid=3796, auid=501, euid=501, binary_path=/usr/bin/osascript}, },
default	13:16:42.730838-0500	tccd	AUTHREQ_SUBJECT: msgID=3796.1, subject=com.nexy.assistant,
default	13:16:42.731600-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21255200 at /Applications/Nexy.app
default	13:16:42.754280-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=387.11130, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=3734, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.osascript, pid=3796, auid=501, euid=501, binary_path=/usr/bin/osascript}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=387, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	13:16:42.755176-0500	tccd	AUTHREQ_SUBJECT: msgID=387.11130, subject=com.nexy.assistant,
default	13:16:42.755867-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21255200 at /Applications/Nexy.app
default	13:16:42.801100-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21254300 at /Applications/Nexy.app
default	13:16:42.834191-0500	System Events	TCCAccessRequestIndirect: TCCAccessRequestIndirect with pid 3752: target_identity: {
    kTCCCodeIdentityAuditToken = {length = 32, bytes = 0xf5010000 f5010000 14000000 f5010000 ... b7860100 d10a3600 };
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
default	13:16:42.856229-0500	tccd	target_executable_path_URL: file:///Applications/Nexy.app/Contents/MacOS/Nexy
default	13:16:43.914551-0500	WindowServer	0[outside of RPC]: Process death: 0x0-0x17aa7a9 (Nexy) connectionID: 1D0AB3 pid: 3734 in session 0x101
default	13:16:43.914599-0500	WindowServer	<BSCompoundAssertion:0xb6cc11540> ([FocusManager:257]-deferringPolicyEvaluationSuppression) acquire for reason:process death - 0x0-0x17aa7a9 (Nexy) acq:0xb6cea9720 count:1
default	13:16:43.914958-0500	audiomxd	  ServerSessionManager.mm:478   { "action":"destroy_session", "session":{"ID":"0x1f482f","name":"Nexy(3734)"}, "details":null }
default	13:16:43.914994-0500	audiomxd	AudioApplicationInfoImpl.mm:690   Successfully removed session 0x1f482f from AudioApp, recording state unchanged (app: {"name":"[implicit] Nexy","pid":3734})
default	13:16:43.915007-0500	audiomxd	  ServerSessionManager.mm:1086  destroy audio app instance since was created implicitly by session creation and all sessions now gone (audio app: {"name":"[implicit] Nexy","pid":3734})
default	13:16:43.915280-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 2093, PID = 3734, Name = sid:0x1f482f, Nexy(3734), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	13:16:43.915456-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 2093, PID = 3734, Name = sid:0x1f482f, Nexy(3734), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	13:16:43.915633-0500	audiomxd	UpdateAudioState CID 0x72200001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:16:43.915842-0500	audiomxd	UpdateAudioState CID 0x72200001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:16:43.915720-0500	WindowServer	0[outside of RPC]: [FocusManager:257] update to deferring policy requested for reason: permitted list updated - 0x0-0x17aa7a9 removed - but we are suppressing evaluation for reasons: {(
    "process death - 0x0-0x17aa7a9 (Nexy)"
)}
default	13:16:43.915936-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:16:43.916044-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:16:43.916084-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:16:43.916230-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	13:16:43.916506-0500	WindowServer	0[outside of RPC]: [FocusManager:257] update to deferring policy requested for reason: permitted list updated - 0x1-0xe96 removed - but we are suppressing evaluation for reasons: {(
    "process death - 0x0-0x17aa7a9 (Nexy)"
)}
default	13:16:43.921353-0500	runningboardd	XPC connection invalidated: [app<application.com.nexy.assistant.41851965.41851974(501)>:3734]
default	13:16:43.927962-0500	coreaudiod	>>> NEGOTIATE [com.nexy.assistant]
default	13:16:43.928216-0500	coreaudiod	<<< NEGOTIATE [com.nexy.assistant]
default	13:16:43.932617-0500	coreaudiod	IssueReporting.cpp:492   RTAID [ use_case=Generic report_type=RMS Generic Chain clientID=ADM node=ADM::com.nexy.assistant_52570.52454.0_airpods noise suppression studio::out-0 issue_detected_sample_time=2160.000000 ] -- [ rms:[-120.000000], peaks:[-240.000000] ]
default	13:16:43.932656-0500	coreaudiod	IssueReporting.cpp:492   RTAID [ use_case=Generic report_type=RMS Generic Chain clientID=ADM node=ADM::com.nexy.assistant_52570.52454.0_airpods noise suppression studio::in-0 issue_detected_sample_time=0.000000 ] -- [ rms:[-120.000000], peaks:[-240.000000] ]
default	13:16:43.937762-0500	runningboardd	[app<application.com.nexy.assistant.41851965.41851974(501)>:3734] termination reported by launchd (0, 0, 0)
default	13:16:43.937819-0500	runningboardd	Removing process: [app<application.com.nexy.assistant.41851965.41851974(501)>:3734]
default	13:16:43.938134-0500	runningboardd	Removing launch job for: [app<application.com.nexy.assistant.41851965.41851974(501)>:3734]
default	13:16:43.938355-0500	runningboardd	Removed job for [app<application.com.nexy.assistant.41851965.41851974(501)>:3734]
default	13:16:43.938400-0500	runningboardd	Removing assertions for terminated process: [app<application.com.nexy.assistant.41851965.41851974(501)>:3734]
default	13:16:43.943754-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.41851965.41851974(501)>: none (role: None) (endowments: (null))
default	13:16:43.943907-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.41851965.41851974(501)>: none (role: None) (endowments: (null))
default	13:16:43.944004-0500	audiomxd	  ServerSessionManager.mm:1327  Monitored process died, pid = 3734, name = Nexy
default	13:16:43.944401-0500	launchservicesd	Hit the server for a process handle 1f41d70100000e96 that resolved to: [app<application.com.nexy.assistant.41851965.41851974(501)>:3734]
default	13:16:43.944432-0500	gamepolicyd	Received state update for 3734 (app<application.com.nexy.assistant.41851965.41851974(501)>, none-NotVisible
default	13:16:43.946429-0500	loginwindow	-[ApplicationManager handleCASEvent:withData:] | CAS notification for appDeath for com.nexy.assistant with asn: LSASN:{hi=0x0;lo=0x17aa7a9} for bundle path: /Applications/Nexy.app with URL: file:///Applications/Nexy.app/
default	13:16:43.946455-0500	loginwindow	-[Application setState:] | enter: <Application: 0x96aadb2a0: Nexy> state 3
default	13:16:43.946465-0500	loginwindow	-[PersistentAppsSupport applicationQuit:] | for app:Nexy, _appTrackingState = 2
default	13:16:43.947992-0500	loginwindow	-[Application setState:] | enter: <Application: 0x96aadb2a0: Nexy> state 4
default	13:16:43.948002-0500	loginwindow	-[PersistentAppsSupport applicationQuit:] | for app:Nexy, _appTrackingState = 2
default	13:16:47.004271-0500	logger	launching: /usr/bin/open -n -a /Applications/Nexy.app
default	13:16:47.101552-0500	lsd	com.nexy.assistant/Unknown Persona:5:5:1:1:Building bundle record for app
default	13:16:47.101713-0500	lsd	com.nexy.assistant/Unknown Persona:5:5:2:1:Built bundle record for app
default	13:16:47.103744-0500	lsd	com.nexy.assistant/Unknown Persona:5:4:2:1:_LSServerRegisterItemInfo result = 0
default	13:16:47.110961-0500	runningboardd	Launch request for app<application.com.nexy.assistant.41851965.41851974.E07E1E6A-F99F-44EE-AA0C-BCFC3DC26379(501)>[0] is using uid 501 (divined from auid 501 euid 501)
default	13:16:47.111036-0500	runningboardd	Acquiring assertion targeting app<application.com.nexy.assistant.41851965.41851974.E07E1E6A-F99F-44EE-AA0C-BCFC3DC26379(501)> from originator [osservice<com.apple.coreservices.uiagent(501)>:99327] with description <RBSAssertionDescriptor| "LS launch com.nexy.assistant" ID:394-99327-1287963 target:app<application.com.nexy.assistant.41851965.41851974.E07E1E6A-F99F-44EE-AA0C-BCFC3DC26379(501)> attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"LaunchRoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	13:16:47.111116-0500	runningboardd	Assertion 394-99327-1287963 (target:app<application.com.nexy.assistant.41851965.41851974.E07E1E6A-F99F-44EE-AA0C-BCFC3DC26379(501)>) will be created as active
default	13:16:47.110651-0500	dmd	Received xpc stream event (distributed notification matching) with name: com.apple.LaunchServices.applicationRegistered user info: {
    CFBundleDisplayName = Nexy;
    bundleIDs =     (
        "com.nexy.assistant"
    );
    isPlaceholder = 0;
}
default	13:16:47.113985-0500	runningboardd	Checking PreventLaunch: global:0 exPath:/Applications/Nexy.app/Contents/MacOS/Nexy predicates:(null) allow:(null)
default	13:16:47.114013-0500	runningboardd	Creating and launching job for: app<application.com.nexy.assistant.41851965.41851974.E07E1E6A-F99F-44EE-AA0C-BCFC3DC26379(501)>
default	13:16:47.114031-0500	runningboardd	_mutateContextIfNeeded called for com.nexy.assistant
default	13:16:47.114094-0500	runningboardd	app<application.com.nexy.assistant.41851965.41851974.E07E1E6A-F99F-44EE-AA0C-BCFC3DC26379(501)>: -[RBPersonaManager personaForIdentity:context:personaUID:personaUniqueString:] required 0.000000 ms (wallclock); resolved to {4294967295, (null)}
default	13:16:47.125099-0500	runningboardd	[app<application.com.nexy.assistant.41851965.41851974.E07E1E6A-F99F-44EE-AA0C-BCFC3DC26379(501)>:3817] is not RunningBoard jetsam managed.
default	13:16:47.125117-0500	runningboardd	[app<application.com.nexy.assistant.41851965.41851974.E07E1E6A-F99F-44EE-AA0C-BCFC3DC26379(501)>:3817] This process will not be managed.
default	13:16:47.125128-0500	runningboardd	Now tracking process: [app<application.com.nexy.assistant.41851965.41851974.E07E1E6A-F99F-44EE-AA0C-BCFC3DC26379(501)>:3817]
default	13:16:47.125308-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.41851965.41851974.E07E1E6A-F99F-44EE-AA0C-BCFC3DC26379(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	13:16:47.125951-0500	gamepolicyd	Hit the server for a process handle 1a5597b100000ee9 that resolved to: [app<application.com.nexy.assistant.41851965.41851974.E07E1E6A-F99F-44EE-AA0C-BCFC3DC26379(501)>:3817]
default	13:16:47.125991-0500	gamepolicyd	Received state update for 3817 (app<application.com.nexy.assistant.41851965.41851974.E07E1E6A-F99F-44EE-AA0C-BCFC3DC26379(501)>, running-active-NotVisible
default	13:16:47.128360-0500	runningboardd	Using default underlying assertion for app: [app<application.com.nexy.assistant.41851965.41851974.E07E1E6A-F99F-44EE-AA0C-BCFC3DC26379(501)>:3817]
default	13:16:47.128422-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.41851965.41851974.E07E1E6A-F99F-44EE-AA0C-BCFC3DC26379(501)>:3817] from originator [app<application.com.nexy.assistant.41851965.41851974.E07E1E6A-F99F-44EE-AA0C-BCFC3DC26379(501)>:3817] with description <RBSAssertionDescriptor| "RB Underlying Assertion" ID:394-394-1287964 target:3817 attributes:[
	<RBSDomainAttribute| domain:"com.apple.underlying" name:"defaultUnderlyingAppAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	13:16:47.128551-0500	runningboardd	Assertion 394-394-1287964 (target:[app<application.com.nexy.assistant.41851965.41851974.E07E1E6A-F99F-44EE-AA0C-BCFC3DC26379(501)>:3817]) will be created as active
default	13:16:47.128760-0500	runningboardd	[app<application.com.nexy.assistant.41851965.41851974.E07E1E6A-F99F-44EE-AA0C-BCFC3DC26379(501)>:3817] Ignoring jetsam update because this process is not memory-managed
default	13:16:47.128778-0500	runningboardd	[app<application.com.nexy.assistant.41851965.41851974.E07E1E6A-F99F-44EE-AA0C-BCFC3DC26379(501)>:3817] Ignoring suspend because this process is not lifecycle managed
default	13:16:47.128798-0500	runningboardd	[app<application.com.nexy.assistant.41851965.41851974.E07E1E6A-F99F-44EE-AA0C-BCFC3DC26379(501)>:3817] Set darwin role to: UserInteractive
default	13:16:47.128813-0500	runningboardd	[app<application.com.nexy.assistant.41851965.41851974.E07E1E6A-F99F-44EE-AA0C-BCFC3DC26379(501)>:3817] Ignoring GPU update because this process is not GPU managed
default	13:16:47.128843-0500	runningboardd	[app<application.com.nexy.assistant.41851965.41851974.E07E1E6A-F99F-44EE-AA0C-BCFC3DC26379(501)>:3817] Ignoring memory limit update because this process is not memory-managed
default	13:16:47.128900-0500	runningboardd	[app<application.com.nexy.assistant.41851965.41851974.E07E1E6A-F99F-44EE-AA0C-BCFC3DC26379(501)>:3817] reported to RB as running
default	13:16:47.130377-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.41851965.41851974.E07E1E6A-F99F-44EE-AA0C-BCFC3DC26379(501)>:3817] from originator [osservice<com.apple.coreservices.launchservicesd>:357] with description <RBSAssertionDescriptor| "uielement:3817" ID:394-357-1287965 target:3817 attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"RoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	13:16:47.130503-0500	runningboardd	Assertion 394-357-1287965 (target:[app<application.com.nexy.assistant.41851965.41851974.E07E1E6A-F99F-44EE-AA0C-BCFC3DC26379(501)>:3817]) will be created as active
default	13:16:47.130553-0500	CoreServicesUIAgent	LAUNCH: 0x0-0x17b67b5 com.nexy.assistant starting stopped process.
default	13:16:47.131787-0500	loginwindow	-[Application _updateInformationInternal] | Got App URL: file:///Applications/Nexy.app/
default	13:16:47.131969-0500	loginwindow	-[Application setState:] | enter: <Application: 0x96aadb2a0: Nexy> state 2
default	13:16:47.131992-0500	loginwindow	-[ApplicationManager checkInAppContext:eventData:] | ApplicationManager: Checked in app : Nexy
default	13:16:47.132435-0500	runningboardd	[app<application.com.nexy.assistant.41851965.41851974.E07E1E6A-F99F-44EE-AA0C-BCFC3DC26379(501)>:3817] Ignoring jetsam update because this process is not memory-managed
default	13:16:47.132460-0500	runningboardd	[app<application.com.nexy.assistant.41851965.41851974.E07E1E6A-F99F-44EE-AA0C-BCFC3DC26379(501)>:3817] Ignoring suspend because this process is not lifecycle managed
default	13:16:47.132472-0500	runningboardd	[app<application.com.nexy.assistant.41851965.41851974.E07E1E6A-F99F-44EE-AA0C-BCFC3DC26379(501)>:3817] Ignoring GPU update because this process is not GPU managed
default	13:16:47.132520-0500	runningboardd	[app<application.com.nexy.assistant.41851965.41851974.E07E1E6A-F99F-44EE-AA0C-BCFC3DC26379(501)>:3817] Ignoring memory limit update because this process is not memory-managed
default	13:16:47.132603-0500	runningboardd	Successfully acquired underlying assertion for [app<application.com.nexy.assistant.41851965.41851974.E07E1E6A-F99F-44EE-AA0C-BCFC3DC26379(501)>:3817]
default	13:16:47.132704-0500	kernel	Nexy[3817] triggered unnest of range 0x1fc000000->0x1fe000000 of DYLD shared region in VM map 0x3f8ff10a34b3b9b5. While not abnormal for debuggers, this increases system memory footprint until the target exits.
default	13:16:47.132724-0500	kernel	Nexy[3817] triggered unnest of range 0x1fe000000->0x200000000 of DYLD shared region in VM map 0x3f8ff10a34b3b9b5. While not abnormal for debuggers, this increases system memory footprint until the target exits.
default	13:16:47.133662-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.41851965.41851974.E07E1E6A-F99F-44EE-AA0C-BCFC3DC26379(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	13:16:47.133950-0500	runningboardd	Invalidating assertion 394-99327-1287963 (target:app<application.com.nexy.assistant.41851965.41851974.E07E1E6A-F99F-44EE-AA0C-BCFC3DC26379(501)>) from originator [osservice<com.apple.coreservices.uiagent(501)>:99327]
default	13:16:47.133982-0500	runningboardd	[app<application.com.nexy.assistant.41851965.41851974.E07E1E6A-F99F-44EE-AA0C-BCFC3DC26379(501)>:3817] Ignoring jetsam update because this process is not memory-managed
default	13:16:47.134033-0500	runningboardd	[app<application.com.nexy.assistant.41851965.41851974.E07E1E6A-F99F-44EE-AA0C-BCFC3DC26379(501)>:3817] Ignoring suspend because this process is not lifecycle managed
default	13:16:47.134066-0500	runningboardd	[app<application.com.nexy.assistant.41851965.41851974.E07E1E6A-F99F-44EE-AA0C-BCFC3DC26379(501)>:3817] Ignoring GPU update because this process is not GPU managed
default	13:16:47.134073-0500	gamepolicyd	Received state update for 3817 (app<application.com.nexy.assistant.41851965.41851974.E07E1E6A-F99F-44EE-AA0C-BCFC3DC26379(501)>, running-active-NotVisible
default	13:16:47.134160-0500	runningboardd	[app<application.com.nexy.assistant.41851965.41851974.E07E1E6A-F99F-44EE-AA0C-BCFC3DC26379(501)>:3817] Ignoring memory limit update because this process is not memory-managed
default	13:16:47.136718-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.41851965.41851974.E07E1E6A-F99F-44EE-AA0C-BCFC3DC26379(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	13:16:47.144761-0500	logger	verifying new process for /Applications/Nexy.app/Contents/MacOS/Nexy
default	13:16:47.183612-0500	logger	detected new pid 3817 for /Applications/Nexy.app/Contents/MacOS/Nexy
default	13:16:47.208134-0500	Nexy	[0x101dd07c0] activating connection: mach=true listener=false peer=false name=com.apple.cfprefsd.daemon
default	13:16:47.208209-0500	Nexy	[0x101dd0d80] activating connection: mach=true listener=false peer=false name=com.apple.cfprefsd.agent
default	13:16:47.239490-0500	gamepolicyd	Received state update for 3817 (app<application.com.nexy.assistant.41851965.41851974.E07E1E6A-F99F-44EE-AA0C-BCFC3DC26379(501)>, running-active-NotVisible
default	13:16:47.241591-0500	runningboardd	[app<application.com.nexy.assistant.41851965.41851974.E07E1E6A-F99F-44EE-AA0C-BCFC3DC26379(501)>:3817] Ignoring jetsam update because this process is not memory-managed
default	13:16:47.241611-0500	runningboardd	[app<application.com.nexy.assistant.41851965.41851974.E07E1E6A-F99F-44EE-AA0C-BCFC3DC26379(501)>:3817] Ignoring suspend because this process is not lifecycle managed
default	13:16:47.241631-0500	runningboardd	[app<application.com.nexy.assistant.41851965.41851974.E07E1E6A-F99F-44EE-AA0C-BCFC3DC26379(501)>:3817] Ignoring GPU update because this process is not GPU managed
default	13:16:47.241698-0500	runningboardd	[app<application.com.nexy.assistant.41851965.41851974.E07E1E6A-F99F-44EE-AA0C-BCFC3DC26379(501)>:3817] Ignoring memory limit update because this process is not memory-managed
default	13:16:47.244554-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.41851965.41851974.E07E1E6A-F99F-44EE-AA0C-BCFC3DC26379(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	13:16:47.250307-0500	gamepolicyd	Received state update for 3817 (app<application.com.nexy.assistant.41851965.41851974.E07E1E6A-F99F-44EE-AA0C-BCFC3DC26379(501)>, running-active-NotVisible
error	13:16:47.324052-0500	Nexy	dlsym cannot find symbol NSMakeRect in CFBundle 0x101dc1980 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	13:16:47.324280-0500	Nexy	dlsym cannot find symbol NSMakePoint in CFBundle 0x101dc1980 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	13:16:47.324486-0500	Nexy	dlsym cannot find symbol NSMakeSize in CFBundle 0x101dc1980 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	13:16:47.324687-0500	Nexy	dlsym cannot find symbol NSMakeRange in CFBundle 0x101dc1980 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
default	13:16:47.325980-0500	Nexy	[0x101dc0800] activating connection: mach=true listener=false peer=false name=com.apple.coreservices.launchservicesd
default	13:16:47.326731-0500	Nexy	[0xa305f4000] activating connection: mach=true listener=false peer=false name=com.apple.analyticsd
default	13:16:47.327086-0500	Nexy	[0xa305f4140] activating connection: mach=true listener=false peer=false name=com.apple.pasteboard.1
default	13:16:47.327480-0500	Nexy	[0xa305f4280] activating connection: mach=true listener=false peer=false name=com.apple.distributed_notifications@Uv3
default	13:16:47.329555-0500	Nexy	void _NSDisableAutomaticTerminationAndLog(NSString *) No windows open yet
default	13:16:47.329931-0500	Nexy	[0xa305f43c0] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	13:16:47.330662-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=3817.1, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=3817, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	13:16:47.332312-0500	tccd	AUTHREQ_SUBJECT: msgID=3817.1, subject=com.nexy.assistant,
default	13:16:47.333059-0500	Nexy	Received configuration update from daemon (initial)
default	13:16:47.333101-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21255200 at /Applications/Nexy.app
default	13:16:47.352890-0500	Nexy	[0xa305f43c0] invalidated after the last release of the connection object
default	13:16:47.353239-0500	Nexy	server port 0x00003507, session port 0x00003507
default	13:16:47.354307-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=387.11131, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=3817, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=387, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	13:16:47.354336-0500	tccd	requestor: TCCDProcess: identifier=com.apple.WindowServer, pid=387, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=3817, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	13:16:47.355264-0500	tccd	AUTHREQ_SUBJECT: msgID=387.11131, subject=com.nexy.assistant,
default	13:16:47.355990-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21255200 at /Applications/Nexy.app
default	13:16:47.380582-0500	Nexy	New connection 0x15ffe3 main
default	13:16:47.383290-0500	Nexy	CHECKIN: pid=3817
default	13:16:47.391809-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.41851965.41851974.E07E1E6A-F99F-44EE-AA0C-BCFC3DC26379(501)>:3817] from originator [osservice<com.apple.coreservices.launchservicesd>:357] with description <RBSAssertionDescriptor| "uielement:3817" ID:394-357-1287968 target:3817 attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"RoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	13:16:47.391910-0500	runningboardd	Assertion 394-357-1287968 (target:[app<application.com.nexy.assistant.41851965.41851974.E07E1E6A-F99F-44EE-AA0C-BCFC3DC26379(501)>:3817]) will be created as active
default	13:16:47.392437-0500	runningboardd	Invalidating assertion 394-357-1287965 (target:[app<application.com.nexy.assistant.41851965.41851974.E07E1E6A-F99F-44EE-AA0C-BCFC3DC26379(501)>:3817]) from originator [osservice<com.apple.coreservices.launchservicesd>:357]
default	13:16:47.392448-0500	Nexy	CHECKEDIN: pid=3817 asn=0x0-0x17b67b5 foreground=0
default	13:16:47.392290-0500	launchservicesd	CHECKIN:0x0-0x17b67b5 3817 com.nexy.assistant
default	13:16:47.392476-0500	loginwindow	-[Application _updateInformationInternal] | Got App URL: file:///Applications/Nexy.app/
default	13:16:47.392621-0500	loginwindow	-[ApplicationManager checkInAppContext:eventData:] | ApplicationManager: Checked in app : Nexy
default	13:16:47.392708-0500	Nexy	[0xa305f43c0] activating connection: mach=false listener=true peer=false name=(anonymous)
default	13:16:47.392740-0500	Nexy	[0xa305f43c0] Connection returned listener port: 0x4f03
default	13:16:47.393287-0500	Nexy	[0xa31758300] activating connection: mach=false listener=false peer=true name=com.apple.xpc.anonymous.0xa305f43c0.peer[357].0xa31758300
default	13:16:47.395612-0500	Nexy	FRONTLOGGING: version 1
default	13:16:47.395682-0500	Nexy	Registered, pid=3817 ASN=0x0,0x17b67b5
default	13:16:47.396155-0500	WindowServer	15ffe3[CreateApplication]: Process creation: 0x0-0x17b67b5 (Nexy) connectionID: 15FFE3 pid: 3817 in session 0x101
default	13:16:47.396656-0500	Nexy	[0xa305f4500] activating connection: mach=true listener=false peer=false name=com.apple.lsd.mapdb
default	13:16:47.398416-0500	Nexy	[0xa305f43c0] Connection returned listener port: 0x4f03
default	13:16:47.400171-0500	Nexy	BringForward: pid=3817 asn=0x0-0x17b67b5 bringForward=0 foreground=0 uiElement=1 launchedByLS=1 modifiersCount=1 allDisabled=0
default	13:16:47.400737-0500	Nexy	BringFrontModifier: pid=3817 asn=0x0-0x17b67b5 Modifier 0 hideAfter=0 hideOthers=0 dontMakeFrontmost=0 mouseDown=0/0 seed=0/0
default	13:16:47.401556-0500	Nexy	Current system appearance, (HLTB: 1), (SLS: 0)
default	13:16:47.406724-0500	Nexy	Post-registration system appearance: (HLTB: 1)
default	13:16:47.411525-0500	Nexy	Handshake succeeded
default	13:16:47.411540-0500	Nexy	Identity resolved as app<application.com.nexy.assistant.41851965.41851974.E07E1E6A-F99F-44EE-AA0C-BCFC3DC26379(501)>
default	13:16:47.411921-0500	Nexy	[0xa305f43c0] Connection returned listener port: 0x4f03
default	13:16:47.415731-0500	Nexy	[0xa305f43c0] Connection returned listener port: 0x4f03
default	13:16:47.420871-0500	Nexy	Created a new Process Instance Registry XPC connection (inactive)
default	13:16:48.246381-0500	kernel	SK[7]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 36989EE2-FE8F-4780-AF9A-44787EBD821F flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.57694,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0x701b2a8b tp_proto=0x06"
default	13:16:48.246462-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:57694<-><IPv4-redacted>:53] interface: utun4 (skipped: 23977)
so_gencnt: 7004991 t_state: SYN_SENT process: Nexy:3817 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 1 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x91b19f9e
default	13:16:48.247018-0500	kernel	tcp connected: [<IPv4-redacted>:57694<-><IPv4-redacted>:53] interface: utun4 (skipped: 23977)
so_gencnt: 7004991 t_state: ESTABLISHED process: Nexy:3817 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 1 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x91b19f9e
default	13:16:48.247277-0500	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:57694<-><IPv4-redacted>:53] interface: utun4 (skipped: 23977)
so_gencnt: 7004991 t_state: FIN_WAIT_1 process: Nexy:3817 Duration: 0.001 sec Conn_Time: 0.001 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 1.000 ms rttvar: 0.500 ms base rtt: 1 ms so_error: 0 svc/tc: 0 flow: 0x91b19f9e
default	13:16:48.247286-0500	kernel	tcp_connection_summary [<IPv4-redacted>:57694<-><IPv4-redacted>:53] interface: utun4 (skipped: 23977)
so_gencnt: 7004991 t_state: FIN_WAIT_1 process: Nexy:3817 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	13:16:48.285567-0500	Nexy	  AVAudioSession_MacOS.mm:1021  initForMacOS
default	13:16:48.286204-0500	Nexy	[0xa305f4c80] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioSession
default	13:16:48.287308-0500	audiomxd	  ServerSessionManager.mm:315   { "action":"create_session", "session":{"ID":"0x1f4830","name":"Nexy(3817)"}, "details":{"PID":3817,"session_type":"Primary"} }
default	13:16:48.287395-0500	audiomxd	AudioApplicationInfoImpl.mm:250   Setting initial isRecording state: 0 for newly-created AudioApp
	app: {"name":"[implicit] Nexy","pid":3817}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1f4830, sessionType: 'prim', isRecording: false }, 
]
default	13:16:48.288172-0500	audiomxd	  ServerSessionManager.mm:1322  Start process monitoring, pid = 3817, name = Nexy
default	13:16:48.288527-0500	Nexy	    SessionCore_Create.mm:99    Created session 0xa317970e0 with ID: 0x1f4830
default	13:16:48.288830-0500	Nexy	Registered notify signal com.apple.caulk.alloc.rtdump (0)
default	13:16:48.289830-0500	Nexy	System_Input_Processing_Notification_Handler.mm:456   System_Input_Processing_Notification_Handler::is_vi_available(): Voice isolation DSP is available for client with bundle id com.nexy.assistant (AVFoundation is available, application is not in client deny list, application is not FaceTime variant)
default	13:16:48.291400-0500	Nexy	[0xa305f4dc0] activating connection: mach=true listener=false peer=false name=com.apple.cmio.registerassistantservice.system-extensions
fault	13:16:48.293863-0500	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.41851965.41851974.E07E1E6A-F99F-44EE-AA0C-BCFC3DC26379 AUID=501> and <type=Application identifier=application.com.nexy.assistant.41851965.41851974.E07E1E6A-F99F-44EE-AA0C-BCFC3DC26379>
default	13:16:48.298182-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOInitializeListenersForBundleID: for <private> -> <private>
default	13:16:48.299770-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> vpio_preferenceChangedListener: new value ((null)) for key AUVoiceIOClients/com-nexy-assistant/AUVoiceIOChatFlavor, translatedBundleID com.nexy.assistant, bundleIDs {(
    "com.nexy.assistant"
)}
default	13:16:48.299958-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> vpio_preferenceChangedListener: new value ((null)) for key AUVoiceIOClients/com-nexy-assistant/AUVoiceIOIsAutoChatFlavorEnabled, translatedBundleID com.nexy.assistant, bundleIDs {(
    "com.nexy.assistant"
)}
default	13:16:48.300116-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetSupportedChatFlavorsForBundleID: <private>-><private> get supported chat flavors: <private>
default	13:16:48.300127-0500	Nexy	            HALSystem.cpp:134    Enabling HAL Voice Isolation support
default	13:16:48.300158-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetHiddenChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	13:16:48.300291-0500	Nexy	[0xa305f4f00] activating connection: mach=true listener=false peer=false name=com.apple.tccd
default	13:16:48.300437-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOHiddenChatFlavors newValue: (
    1
)
default	13:16:48.301469-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=3817.2, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=3817, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	13:16:48.312212-0500	tccd	AUTHREQ_SUBJECT: msgID=3817.2, subject=com.nexy.assistant,
default	13:16:48.312849-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x7d1158000 at /Applications/Nexy.app
default	13:16:48.330705-0500	Nexy	[0xa305f4f00] invalidated after the last release of the connection object
default	13:16:48.330842-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetPreferredChatFlavorForBundleID: <private>-><private> get value: 0
default	13:16:48.330882-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetSupportedChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	13:16:48.331083-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOSupportedChatFlavors newValue: (
    0,
    2
)
default	13:16:48.332123-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=395.9257, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=3817, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	13:16:48.333080-0500	tccd	AUTHREQ_SUBJECT: msgID=395.9257, subject=com.nexy.assistant,
default	13:16:48.333632-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x7d1158000 at /Applications/Nexy.app
error	13:16:48.349234-0500	tccd	Request message contains a target_token to accessing_process (TCCDProcess: identifier=com.nexy.assistant, pid=3817, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy) but TCCDProcess: identifier=com.apple.audio.coreaudiod, pid=395, auid=202, euid=202, binary_path=/usr/sbin/coreaudiod is not a TCC manager for service: kTCCServiceScreenCapture.
default	13:16:48.350142-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=395.9259, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=3817, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=388, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	13:16:48.351102-0500	tccd	AUTHREQ_SUBJECT: msgID=395.9259, subject=com.nexy.assistant,
default	13:16:48.351665-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x7d1158000 at /Applications/Nexy.app
default	13:16:48.367913-0500	Nexy	  HALPlugInManagement.cpp:440    HALPlugInManagement::RegisterPlugIns: skipping in-process plug-ins
error	13:16:48.367932-0500	Nexy	AddInstanceForFactory: No factory registered for id <CFUUID 0xa305afee0> F8BB1C28-BAE8-11D6-9C31-00039315CD46
error	13:16:48.388103-0500	Nexy	         HALC_ProxyObjectMap.cpp:174   HALC_ProxyObjectMap::_CopyObjectByObjectID: failed to create the local object
error	13:16:48.388113-0500	Nexy	            HALC_ShellDevice.cpp:2673  HALC_ShellDevice::RebuildControlList: couldn't find the control object
default	13:16:48.391150-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	13:16:48.391288-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	13:16:48.397239-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetPreferredChatFlavorForBundleID: <private>-><private> get value: 0
default	13:16:48.398288-0500	Nexy	[0xa305f4f00] activating connection: mach=true listener=false peer=false name=com.apple.audioanalyticsd
error	13:16:48.398622-0500	Nexy	Reporter disconnected. { function=sendMessage, reporterID=16393890168833 }
default	13:16:48.398700-0500	Nexy	       AggregateDevice.mm:887   Creating DefaultDeviceAggregate
default	13:16:48.398744-0500	Nexy	       AggregateDevice.mm:914   fetched default output device, ID = 83
default	13:16:48.398778-0500	Nexy	       AggregateDevice.mm:914   fetched default input device, ID = 89
default	13:16:48.409501-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	13:16:48.409631-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	13:16:48.414324-0500	Nexy	       AggregateDevice.mm:688   Built valid aggregate 125
default	13:16:48.421449-0500	Nexy	  AVAudioSession_MacOS.mm:507   Setting category: AVAudioSessionCategoryPlayback, requires reconfiguration?: NO
default	13:16:48.421472-0500	Nexy	  AVAudioSession_MacOS.mm:883   Activating session
default	13:16:48.425146-0500	Nexy	[0xa305f5040] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioComponentRegistrar
default	13:16:48.433988-0500	Nexy	                AUHAL.cpp:420   AUHAL: (0xa31130e40) Selecting device 83 from constructor
default	13:16:48.434752-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is DISABLED
default	13:16:48.435090-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:16:48.436085-0500	Nexy	       ACv2Workarounds.mm:51    com.nexy.assistant: fix84702776_86723525_86479548_89800354_SinglePacketDesc: false
default	13:16:48.436125-0500	Nexy	Registered notify signal com.apple.caulk.alloc.audiodump (0)
default	13:16:48.436243-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0xa30c57390, from  2 ch,  44100 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	13:16:48.436261-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:16:48.437407-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:16:48.437628-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:16:48.439183-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:16:48.439430-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:16:48.440397-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0xa30c57420, from  2 ch,  44100 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	13:16:48.440411-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:16:48.440745-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:16:48.441400-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0xa30c573f0, from  2 ch,  48000 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	13:16:48.441409-0500	Nexy	       AudioConverter.cpp:1317  AudioConverter -> 0xa30c573f0: The in-process GetProperty call returned 1886547824 for property 1886546285 with size 8.
default	13:16:48.441414-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:16:48.441415-0500	Nexy	AudioConverter -> 0xa30c573f0: The in-process SetProperty call returned 1886547824 for property 1936876385 with size 4.
default	13:16:48.441422-0500	Nexy	AudioConverter -> 0xa30c573f0: The in-process SetProperty call returned 1886547824 for property 1936876401 with size 4.
default	13:16:48.441426-0500	Nexy	AudioConverter -> 0xa30c573f0: The in-process SetProperty call returned 1886547824 for property 1886547309 with size 4.
default	13:16:48.442153-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0xa30c573f0, from  2 ch,  48000 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	13:16:48.442162-0500	Nexy	       AudioConverter.cpp:1317  AudioConverter -> 0xa30c573f0: The in-process GetProperty call returned 1886547824 for property 1886546285 with size 8.
default	13:16:48.442167-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	13:16:48.442167-0500	Nexy	AudioConverter -> 0xa30c573f0: The in-process SetProperty call returned 1886547824 for property 1936876385 with size 4.
default	13:16:48.442177-0500	Nexy	AudioConverter -> 0xa30c573f0: The in-process SetProperty call returned 1886547824 for property 1936876401 with size 4.
default	13:16:48.442181-0500	Nexy	AudioConverter -> 0xa30c573f0: The in-process SetProperty call returned 1886547824 for property 1886547309 with size 4.
default	13:16:48.442315-0500	Nexy	       AudioConverter.cpp:1317  AudioConverter -> 0xa30c573f0: The in-process GetProperty call returned 1886547824 for property 1886546285 with size 8.
default	13:16:48.463835-0500	Nexy	[0xa305f5400] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
error	13:16:48.464298-0500	tccd	TCCDProcess: identifier=com.nexy.assistant, pid=3817, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy attempted to call TCCAccessRequest for kTCCServiceAccessibility without the recommended com.apple.private.tcc.manager.check-by-audit-token entitlement
default	13:16:48.464468-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=3817.3, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=3817, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.nexy.assistant, pid=3817, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	13:16:48.465379-0500	tccd	AUTHREQ_SUBJECT: msgID=3817.3, subject=com.nexy.assistant,
default	13:16:48.465998-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21255200 at /Applications/Nexy.app
default	13:16:48.484478-0500	Nexy	[0xa305f5400] invalidated after the last release of the connection object
default	13:16:48.484559-0500	Nexy	[0xa305f5400] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
error	13:16:48.484894-0500	tccd	TCCDProcess: identifier=com.nexy.assistant, pid=3817, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy attempted to call TCCAccessRequest for kTCCServiceAccessibility without the recommended com.apple.private.tcc.manager.check-by-audit-token entitlement
default	13:16:48.485047-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=3817.4, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=3817, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.nexy.assistant, pid=3817, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	13:16:48.485754-0500	tccd	AUTHREQ_SUBJECT: msgID=3817.4, subject=com.nexy.assistant,
default	13:16:48.503520-0500	Nexy	[0xa305f5400] invalidated after the last release of the connection object
default	13:16:48.503573-0500	Nexy	[0xa305f5400] activating connection: mach=true listener=false peer=false name=com.apple.universalaccessAuthWarn
default	13:16:48.503655-0500	Nexy	[0xa305f5400] invalidated after the last release of the connection object
default	13:16:48.579319-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=3828.1, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=3817, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.osascript, pid=3828, auid=501, euid=501, binary_path=/usr/bin/osascript}, },
default	13:16:48.601017-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=387.11132, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=3817, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.osascript, pid=3828, auid=501, euid=501, binary_path=/usr/bin/osascript}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=387, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	13:16:48.602422-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21255200 at /Applications/Nexy.app
default	13:16:48.667968-0500	System Events	TCCAccessRequestIndirect: TCCAccessRequestIndirect with pid 3752: target_identity: {
    kTCCCodeIdentityAuditToken = {length = 32, bytes = 0xf5010000 f5010000 14000000 f5010000 ... b7860100 0d0b3600 };
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
default	13:16:48.681983-0500	tccd	target_executable_path_URL: file:///Applications/Nexy.app/Contents/MacOS/Nexy
default	13:16:48.758553-0500	Nexy	[0xa305f5540] invalidated after the last release of the connection object
default	13:16:52.309129-0500	runningboardd	Assertion did invalidate due to timeout: 394-394-1287964 (target:[app<application.com.nexy.assistant.41851965.41851974.E07E1E6A-F99F-44EE-AA0C-BCFC3DC26379(501)>:3817])
default	13:16:52.506356-0500	runningboardd	[app<application.com.nexy.assistant.41851965.41851974.E07E1E6A-F99F-44EE-AA0C-BCFC3DC26379(501)>:3817] Ignoring jetsam update because this process is not memory-managed
default	13:16:52.506381-0500	runningboardd	[app<application.com.nexy.assistant.41851965.41851974.E07E1E6A-F99F-44EE-AA0C-BCFC3DC26379(501)>:3817] Ignoring suspend because this process is not lifecycle managed
default	13:16:52.506402-0500	runningboardd	[app<application.com.nexy.assistant.41851965.41851974.E07E1E6A-F99F-44EE-AA0C-BCFC3DC26379(501)>:3817] Ignoring GPU update because this process is not GPU managed
default	13:16:52.506449-0500	runningboardd	[app<application.com.nexy.assistant.41851965.41851974.E07E1E6A-F99F-44EE-AA0C-BCFC3DC26379(501)>:3817] Ignoring memory limit update because this process is not memory-managed
default	13:16:52.510221-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.41851965.41851974.E07E1E6A-F99F-44EE-AA0C-BCFC3DC26379(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	13:16:52.510801-0500	gamepolicyd	Received state update for 3817 (app<application.com.nexy.assistant.41851965.41851974.E07E1E6A-F99F-44EE-AA0C-BCFC3DC26379(501)>, running-active-NotVisible
default	13:16:57.794182-0500	Nexy	NotifyToken::RegisterDispatch(user.uid.501.com.apple.LaunchServices.database) fired for session key <private>
default	13:16:58.405855-0500	Nexy	LSExceptions shared instance invalidated for timeout.
default	13:17:04.017169-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=3833.1, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=3817, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.osascript, pid=3833, auid=501, euid=501, binary_path=/usr/bin/osascript}, },
default	13:17:04.019006-0500	tccd	AUTHREQ_SUBJECT: msgID=3833.1, subject=com.nexy.assistant,
default	13:17:04.019820-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21255200 at /Applications/Nexy.app
default	13:17:04.042742-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=387.11134, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=3817, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.osascript, pid=3833, auid=501, euid=501, binary_path=/usr/bin/osascript}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=387, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	13:17:04.043667-0500	tccd	AUTHREQ_SUBJECT: msgID=387.11134, subject=com.nexy.assistant,
default	13:17:04.044395-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21255200 at /Applications/Nexy.app
default	13:17:04.082823-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21254300 at /Applications/Nexy.app
default	13:17:04.109071-0500	System Events	TCCAccessRequestIndirect: TCCAccessRequestIndirect with pid 3752: target_identity: {
    kTCCCodeIdentityAuditToken = {length = 32, bytes = 0xf5010000 f5010000 14000000 f5010000 ... b7860100 1b0b3600 };
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
default	13:17:04.124581-0500	tccd	target_executable_path_URL: file:///Applications/Nexy.app/Contents/MacOS/Nexy
default	13:17:04.190396-0500	Nexy	[0xa305f5900] activating connection: mach=true listener=false peer=false name=com.apple.iconservices
default	13:17:04.191279-0500	Nexy	[0xa305f5a40] activating connection: mach=true listener=false peer=false name=com.apple.iconservices.store
default	13:17:04.194062-0500	Nexy	[0xa305f5b80] activating connection: mach=true listener=false peer=false name=com.apple.fonts
default	13:17:04.209553-0500	Nexy	[0xa305f6940] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	13:17:04.210297-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=3817.6, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=3817, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	13:17:04.211492-0500	tccd	AUTHREQ_SUBJECT: msgID=3817.6, subject=com.nexy.assistant,
default	13:17:04.212254-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21255200 at /Applications/Nexy.app
default	13:17:04.231297-0500	Nexy	[0xa305f6940] invalidated after the last release of the connection object
default	13:17:04.231441-0500	Nexy	server port 0x00013f13, session port 0x00003507
default	13:17:04.232163-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=387.11135, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=3817, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=387, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	13:17:04.232192-0500	tccd	requestor: TCCDProcess: identifier=com.apple.WindowServer, pid=387, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=3817, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	13:17:04.233721-0500	tccd	AUTHREQ_SUBJECT: msgID=387.11135, subject=com.nexy.assistant,
default	13:17:04.234658-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21255200 at /Applications/Nexy.app
default	13:17:04.252573-0500	Nexy	server port 0x00013f23, session port 0x00003507
default	13:17:04.256795-0500	kernel	SK[8]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 82674152-2A5D-4112-BC6C-8C3846B8BE0D flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.57711,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0x481a699a tp_proto=0x06"
default	13:17:04.256839-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:57711<-><IPv4-redacted>:53] interface: utun4 (skipped: 23977)
so_gencnt: 7005063 t_state: SYN_SENT process: Nexy:3817 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 1 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x91743cea
default	13:17:04.257138-0500	kernel	tcp connected: [<IPv4-redacted>:57711<-><IPv4-redacted>:53] interface: utun4 (skipped: 23977)
so_gencnt: 7005063 t_state: ESTABLISHED process: Nexy:3817 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 1 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x91743cea
default	13:17:04.257919-0500	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:57711<-><IPv4-redacted>:53] interface: utun4 (skipped: 23977)
so_gencnt: 7005063 t_state: FIN_WAIT_1 process: Nexy:3817 Duration: 0.001 sec Conn_Time: 0.000 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 1.000 ms rttvar: 0.500 ms base rtt: 1 ms so_error: 0 svc/tc: 0 flow: 0x91743cea
default	13:17:04.257927-0500	kernel	tcp_connection_summary [<IPv4-redacted>:57711<-><IPv4-redacted>:53] interface: utun4 (skipped: 23977)
so_gencnt: 7005063 t_state: FIN_WAIT_1 process: Nexy:3817 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	13:17:04.260771-0500	kernel	SK[8]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 2ADAE091-037D-4EC5-9CAC-DEBD72637808 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.57712,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0xece21395 tp_proto=0x06"
default	13:17:04.260787-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:57712<-><IPv4-redacted>:53] interface: utun4 (skipped: 23977)
so_gencnt: 7005064 t_state: SYN_SENT process: Nexy:3817 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 1 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xa383fd5a
default	13:17:04.260906-0500	kernel	tcp connected: [<IPv4-redacted>:57712<-><IPv4-redacted>:53] interface: utun4 (skipped: 23977)
so_gencnt: 7005064 t_state: ESTABLISHED process: Nexy:3817 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 1 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xa383fd5a
default	13:17:04.262089-0500	Nexy	networkd_settings_read_from_file initialized networkd settings by reading plist directly
default	13:17:04.262130-0500	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:57712<-><IPv4-redacted>:53] interface: utun4 (skipped: 23977)
so_gencnt: 7005064 t_state: FIN_WAIT_1 process: Nexy:3817 Duration: 0.001 sec Conn_Time: 0.000 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 1.000 ms rttvar: 0.500 ms base rtt: 1 ms so_error: 0 svc/tc: 0 flow: 0xa383fd5a
default	13:17:04.262139-0500	kernel	tcp_connection_summary [<IPv4-redacted>:57712<-><IPv4-redacted>:53] interface: utun4 (skipped: 23977)
so_gencnt: 7005064 t_state: FIN_WAIT_1 process: Nexy:3817 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	13:17:04.262239-0500	Nexy	networkd_settings_read_from_file initialized networkd settings by reading plist directly
default	13:17:04.262886-0500	Nexy	nw_path_libinfo_path_check [A20E34C3-0565-47CE-B8D4-0BB30F180574 IPv4#ff704912:443 tcp, legacy-socket, attribution: developer]
	libinfo check path: <private>
default	13:17:04.263324-0500	kernel	SK[7]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 6B0BB5FC-B3EF-4897-A257-0A6675E83A39 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.57713,dst=<IPv4-redacted>.443,proto=0x06 mask=0x0000003f,hash=0x12070362 tp_proto=0x06"
default	13:17:04.263349-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:57713<-><IPv4-redacted>:443] interface: utun4 (skipped: 23977)
so_gencnt: 7005067 t_state: SYN_SENT process: Nexy:3817 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x893c1d1f
default	13:17:04.263458-0500	kernel	tcp connected: [<IPv4-redacted>:57713<-><IPv4-redacted>:443] interface: utun4 (skipped: 23977)
so_gencnt: 7005067 t_state: ESTABLISHED process: Nexy:3817 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x893c1d1f
default	13:17:04.272202-0500	kernel	udp connect: [<IPv4-redacted>:56739<-><IPv4-redacted>:443] interface:  (skipped: 4450)
so_gencnt: 7005068 so_state: 0x0002 process: Nexy:3817 bytes in/out: 0/0 pkts in/out: 0/0 error: 0 so_error: 0 svc/tc: 0 flow: 0x9efebefe
default	13:17:04.272213-0500	kernel	udp_connection_summary [<IPv4-redacted>:56739<-><IPv4-redacted>:443] interface:  (skipped: 4450)
so_gencnt: 7005068 so_state: 0x0002 process: Nexy:3817 Duration: 0.000 sec Conn_Time: 0.000 sec bytes in/out: 0/0 pkts in/out: 0/0 rxnospace pkts/bytes: 0/0 so_error: 0 svc/tc: 0 flow: 0x9efebefe flowctl: 0us (0x)
default	13:17:04.275582-0500	kernel	SK[8]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 9203E7AA-7380-4D22-A61A-F6094D97CC21 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.57715,dst=<IPv4-redacted>.443,proto=0x06 mask=0x0000003f,hash=0xd1229453 tp_proto=0x06"
default	13:17:04.275609-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:57715<-><IPv4-redacted>:443] interface: utun4 (skipped: 23977)
so_gencnt: 7005070 t_state: SYN_SENT process: Nexy:3817 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 1 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x9d9735ed
default	13:17:04.275867-0500	kernel	tcp connected: [<IPv4-redacted>:57715<-><IPv4-redacted>:443] interface: utun4 (skipped: 23977)
so_gencnt: 7005070 t_state: ESTABLISHED process: Nexy:3817 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 1 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x9d9735ed
default	13:17:04.279723-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=3834.1, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=3817, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.osascript, pid=3834, auid=501, euid=501, binary_path=/usr/bin/osascript}, },
default	13:17:04.280947-0500	tccd	AUTHREQ_SUBJECT: msgID=3834.1, subject=com.nexy.assistant,
default	13:17:04.281584-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21255200 at /Applications/Nexy.app
default	13:17:04.299971-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=387.11136, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=3817, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.osascript, pid=3834, auid=501, euid=501, binary_path=/usr/bin/osascript}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=387, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	13:17:04.300676-0500	tccd	AUTHREQ_SUBJECT: msgID=387.11136, subject=com.nexy.assistant,
default	13:17:04.301270-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21255200 at /Applications/Nexy.app
default	13:17:04.333806-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21254300 at /Applications/Nexy.app
default	13:17:04.356416-0500	System Events	TCCAccessRequestIndirect: TCCAccessRequestIndirect with pid 3752: target_identity: {
    kTCCCodeIdentityAuditToken = {length = 32, bytes = 0xf5010000 f5010000 14000000 f5010000 ... b7860100 1d0b3600 };
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
default	13:17:04.368026-0500	tccd	target_executable_path_URL: file:///Applications/Nexy.app/Contents/MacOS/Nexy
default	13:17:04.470499-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=3835.1, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=3817, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.osascript, pid=3835, auid=501, euid=501, binary_path=/usr/bin/osascript}, },
default	13:17:04.471713-0500	tccd	AUTHREQ_SUBJECT: msgID=3835.1, subject=com.nexy.assistant,
default	13:17:04.472373-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21255200 at /Applications/Nexy.app
default	13:17:04.492517-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=387.11137, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=3817, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.osascript, pid=3835, auid=501, euid=501, binary_path=/usr/bin/osascript}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=387, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	13:17:04.493232-0500	tccd	AUTHREQ_SUBJECT: msgID=387.11137, subject=com.nexy.assistant,
default	13:17:04.493829-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21255200 at /Applications/Nexy.app
default	13:17:04.525386-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21254300 at /Applications/Nexy.app
default	13:17:04.549098-0500	System Events	TCCAccessRequestIndirect: TCCAccessRequestIndirect with pid 3752: target_identity: {
    kTCCCodeIdentityAuditToken = {length = 32, bytes = 0xf5010000 f5010000 14000000 f5010000 ... b7860100 1f0b3600 };
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
default	13:17:04.560097-0500	tccd	target_executable_path_URL: file:///Applications/Nexy.app/Contents/MacOS/Nexy
default	13:17:04.685605-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=3837.1, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=3817, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.osascript, pid=3837, auid=501, euid=501, binary_path=/usr/bin/osascript}, },
default	13:17:04.687019-0500	tccd	AUTHREQ_SUBJECT: msgID=3837.1, subject=com.nexy.assistant,
default	13:17:04.687756-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21255200 at /Applications/Nexy.app
default	13:17:04.707880-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=387.11138, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=3817, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.osascript, pid=3837, auid=501, euid=501, binary_path=/usr/bin/osascript}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=387, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	13:17:04.708777-0500	tccd	AUTHREQ_SUBJECT: msgID=387.11138, subject=com.nexy.assistant,
default	13:17:04.709475-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21255200 at /Applications/Nexy.app
default	13:17:04.749155-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21254300 at /Applications/Nexy.app
default	13:17:04.776340-0500	System Events	TCCAccessRequestIndirect: TCCAccessRequestIndirect with pid 3752: target_identity: {
    kTCCCodeIdentityAuditToken = {length = 32, bytes = 0xf5010000 f5010000 14000000 f5010000 ... b7860100 230b3600 };
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
default	13:17:04.789380-0500	tccd	target_executable_path_URL: file:///Applications/Nexy.app/Contents/MacOS/Nexy
default	13:17:05.009156-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=3839.1, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=3817, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.osascript, pid=3839, auid=501, euid=501, binary_path=/usr/bin/osascript}, },
default	13:17:05.010453-0500	tccd	AUTHREQ_SUBJECT: msgID=3839.1, subject=com.nexy.assistant,
default	13:17:05.011106-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21255200 at /Applications/Nexy.app
default	13:17:05.030917-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=387.11139, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=3817, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.osascript, pid=3839, auid=501, euid=501, binary_path=/usr/bin/osascript}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=387, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	13:17:05.031697-0500	tccd	AUTHREQ_SUBJECT: msgID=387.11139, subject=com.nexy.assistant,
default	13:17:05.032367-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21255200 at /Applications/Nexy.app
default	13:17:05.068193-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21254300 at /Applications/Nexy.app
default	13:17:05.094074-0500	System Events	TCCAccessRequestIndirect: TCCAccessRequestIndirect with pid 3752: target_identity: {
    kTCCCodeIdentityAuditToken = {length = 32, bytes = 0xf5010000 f5010000 14000000 f5010000 ... b7860100 280b3600 };
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
default	13:17:05.106787-0500	tccd	target_executable_path_URL: file:///Applications/Nexy.app/Contents/MacOS/Nexy
default	13:17:05.239993-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=3840.1, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=3817, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.osascript, pid=3840, auid=501, euid=501, binary_path=/usr/bin/osascript}, },
default	13:17:05.241498-0500	tccd	AUTHREQ_SUBJECT: msgID=3840.1, subject=com.nexy.assistant,
default	13:17:05.242255-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21255200 at /Applications/Nexy.app
default	13:17:05.262770-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=387.11140, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=3817, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.osascript, pid=3840, auid=501, euid=501, binary_path=/usr/bin/osascript}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=387, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	13:17:05.263617-0500	tccd	AUTHREQ_SUBJECT: msgID=387.11140, subject=com.nexy.assistant,
default	13:17:05.264291-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21255200 at /Applications/Nexy.app
default	13:17:05.304852-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21254300 at /Applications/Nexy.app
default	13:17:05.330410-0500	System Events	TCCAccessRequestIndirect: TCCAccessRequestIndirect with pid 3752: target_identity: {
    kTCCCodeIdentityAuditToken = {length = 32, bytes = 0xf5010000 f5010000 14000000 f5010000 ... b7860100 2a0b3600 };
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
default	13:17:05.343450-0500	tccd	target_executable_path_URL: file:///Applications/Nexy.app/Contents/MacOS/Nexy
default	13:17:05.415977-0500	Nexy	[0xa305f6e40] activating connection: mach=true listener=false peer=false name=com.apple.usernoted.client
default	13:17:05.425986-0500	usernoted	Connection com.nexy.assistant with path: /Applications/Nexy.app
default	13:17:05.426770-0500	distnoted	register name: com.apple.nsquiet_safe_quit_give_reason object: com.nexy.assistant token: 2400000020 pid: 3817
default	13:17:05.437298-0500	Nexy	NSApp cache appearance:
-NSRequiresAquaSystemAppearance: 0
-appearance: (null)
-effectiveAppearance: <NSCompositeAppearance: 0xa3051c780
 (
    "<NSAquaAppearance: 0xa3051c640>",
    "<NSSystemAppearance: 0xa3051c6e0>"
)>
default	13:17:05.445789-0500	Nexy	[0xa305f7340] activating connection: mach=true listener=false peer=false name=com.apple.dock.fullscreen
default	13:17:05.446645-0500	Nexy	(<private>) deleteSearchableItemsWithDomainIdentifiers, protectionClass:(null), domainIdentifiers number:1
default	13:17:05.446964-0500	Nexy	sConnectionName: com.apple.spotlight.IndexAgent
default	13:17:05.446983-0500	Nexy	Start service name com.apple.spotlight.IndexAgent
default	13:17:05.447021-0500	Nexy	[0xa305f7480] activating connection: mach=true listener=false peer=false name=com.apple.spotlight.IndexAgent
default	13:17:05.447088-0500	Nexy	[C:1] Alloc com.apple.controlcenter.statusitems
default	13:17:05.447165-0500	Nexy	[0xa305f75c0] activating connection: mach=false listener=false peer=false name=(anonymous)
default	13:17:05.447232-0500	Nexy	FBSWorkspace registering source: <private>
default	13:17:05.448188-0500	suggestd	SGDSpotlightReceiver: deleting 1 domain identifiers (1 after removing overlaps) for com.nexy.assistant: <private>
default	13:17:05.448925-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	13:17:05.449294-0500	Nexy	<FBSWorkspaceScenesClient:0xa3051f700 <private>> attempting immediate handshake from activate
default	13:17:05.449647-0500	Nexy	<FBSWorkspaceScenesClient:0xa3051f700 <private>> sent handshake
default	13:17:05.449760-0500	Nexy	Realizing settings extension __NSStatusItemSceneHostSettings__ on FBSSceneSettings
default	13:17:05.450412-0500	Nexy	Realizing settings extension __NSStatusItemSceneClientSettings__ on FBSSceneClientSettings
default	13:17:05.450921-0500	ControlCenter	Asked to bootstrap a new process for handle: [app<application.com.nexy.assistant.41851965.41851974.E07E1E6A-F99F-44EE-AA0C-BCFC3DC26379(501)>:3817]
default	13:17:05.451464-0500	ControlCenter	Creating process (sync=true) for handle: [app<application.com.nexy.assistant.41851965.41851974.E07E1E6A-F99F-44EE-AA0C-BCFC3DC26379(501)>:3817]
default	13:17:05.451790-0500	Nexy	Realizing settings extension FBSSceneSettingsCore on FBSSceneSettings
default	13:17:05.452284-0500	ControlCenter	[app<application.com.nexy.assistant.41851965.41851974.E07E1E6A-F99F-44EE-AA0C-BCFC3DC26379>:3817] Registering event dispatcher at init
default	13:17:05.452752-0500	ControlCenter	Created <FBWorkspace: 0x8e6ef6bc0; <FBApplicationProcess: 0x8e3783480; app<application.com.nexy.assistant.41851965.41851974.E07E1E6A-F99F-44EE-AA0C-BCFC3DC26379>:3817(v360AF9)>>
default	13:17:05.452778-0500	ControlCenter	Bootstrapping app<application.com.nexy.assistant.41851965.41851974.E07E1E6A-F99F-44EE-AA0C-BCFC3DC26379> with intent background
default	13:17:05.453207-0500	Nexy	Realizing settings extension FBSSceneClientSettingsCore on FBSSceneClientSettings
default	13:17:05.453244-0500	runningboardd	Launch request for app<application.com.nexy.assistant.41851965.41851974.E07E1E6A-F99F-44EE-AA0C-BCFC3DC26379(501)>[0] is using uid 501 (divined from auid 501 euid 501)
default	13:17:05.453398-0500	runningboardd	Acquiring assertion targeting app<application.com.nexy.assistant.41851965.41851974.E07E1E6A-F99F-44EE-AA0C-BCFC3DC26379(501)> from originator [osservice<com.apple.controlcenter(501)>:638] with description <RBSAssertionDescriptor| "FBApplicationProcess" ID:394-638-1288041 target:app<application.com.nexy.assistant.41851965.41851974.E07E1E6A-F99F-44EE-AA0C-BCFC3DC26379(501)> attributes:[
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableLPRunReason-Suspend" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableRole-NonUI" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableJetsamPriority-Active" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableBootstrapping" sourceEnvironment:"(null)">
	]>
default	13:17:05.453572-0500	runningboardd	Assertion 394-638-1288041 (target:app<application.com.nexy.assistant.41851965.41851974.E07E1E6A-F99F-44EE-AA0C-BCFC3DC26379(501)>) will be created as active
default	13:17:05.453604-0500	runningboardd	setting abstract target for <RBSAssertionDescriptor| "FBApplicationProcess" ID:394-638-1288041 target:app<application.com.nexy.assistant.41851965.41851974.E07E1E6A-F99F-44EE-AA0C-BCFC3DC26379(501)> attributes:[
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableLPRunReason-Suspend" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableRole-NonUI" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableJetsamPriority-Active" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableBootstrapping" sourceEnvironment:"(null)">
	]> to [app<application.com.nexy.assistant.41851965.41851974.E07E1E6A-F99F-44EE-AA0C-BCFC3DC26379(501)>:3817]
default	13:17:05.453974-0500	runningboardd	[app<application.com.nexy.assistant.41851965.41851974.E07E1E6A-F99F-44EE-AA0C-BCFC3DC26379(501)>:3817] Ignoring jetsam update because this process is not memory-managed
default	13:17:05.453984-0500	runningboardd	[app<application.com.nexy.assistant.41851965.41851974.E07E1E6A-F99F-44EE-AA0C-BCFC3DC26379(501)>:3817] Ignoring suspend because this process is not lifecycle managed
default	13:17:05.453995-0500	runningboardd	[app<application.com.nexy.assistant.41851965.41851974.E07E1E6A-F99F-44EE-AA0C-BCFC3DC26379(501)>:3817] Ignoring GPU update because this process is not GPU managed
default	13:17:05.454014-0500	runningboardd	[app<application.com.nexy.assistant.41851965.41851974.E07E1E6A-F99F-44EE-AA0C-BCFC3DC26379(501)>:3817] Ignoring memory limit update because this process is not memory-managed
default	13:17:05.454185-0500	Nexy	Requesting scene <FBSScene: 0xa3051fa20; com.apple.controlcenter:4C955EBC-E598-4C97-ADE7-FDAC6EEE3402> from com.apple.controlcenter.statusitems
default	13:17:05.456713-0500	Nexy	Request for <FBSScene: 0xa3051fa20; com.apple.controlcenter:4C955EBC-E598-4C97-ADE7-FDAC6EEE3402> complete!
default	13:17:05.456815-0500	Nexy	Realizing settings extension FBSSceneTransitionContextCore on FBSSceneTransitionContext
default	13:17:05.457228-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.41851965.41851974.E07E1E6A-F99F-44EE-AA0C-BCFC3DC26379(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	13:17:05.458555-0500	Nexy	Realizing settings extension __NSHostedViewSceneSettings__ on FBSSceneSettings
default	13:17:05.458810-0500	Nexy	Realizing settings extension __NSClientHostedViewSceneSettings__ on FBSSceneClientSettings
default	13:17:05.459070-0500	Nexy	Realizing settings extension __NSStatusItemAuxiliaryViewSceneSettings__ on FBSSceneSettings
default	13:17:05.459105-0500	Nexy	Realizing settings extension __NSClientStatusItemAuxiliaryViewSceneSettings__ on FBSSceneClientSettings
default	13:17:05.459357-0500	gamepolicyd	Received state update for 3817 (app<application.com.nexy.assistant.41851965.41851974.E07E1E6A-F99F-44EE-AA0C-BCFC3DC26379(501)>, running-active-NotVisible
default	13:17:05.459391-0500	Nexy	Requesting scene <FBSScene: 0xa3051fac0; com.apple.controlcenter:4C955EBC-E598-4C97-ADE7-FDAC6EEE3402-Aux[1]-NSStatusItemView> from com.apple.controlcenter.statusitems
default	13:17:05.460099-0500	Nexy	Request for <FBSScene: 0xa3051fac0; com.apple.controlcenter:4C955EBC-E598-4C97-ADE7-FDAC6EEE3402-Aux[1]-NSStatusItemView> complete!
default	13:17:05.461905-0500	ControlCenter	[app<application.com.nexy.assistant.41851965.41851974.E07E1E6A-F99F-44EE-AA0C-BCFC3DC26379>:3817] Bootstrap success!
default	13:17:05.462673-0500	ControlCenter	[app<application.com.nexy.assistant.41851965.41851974.E07E1E6A-F99F-44EE-AA0C-BCFC3DC26379>:3817] Setting process visibility to: Background
default	13:17:05.462759-0500	ControlCenter	[app<application.com.nexy.assistant.41851965.41851974.E07E1E6A-F99F-44EE-AA0C-BCFC3DC26379>:3817] No launch watchdog for this process, dropping initial assertion in 2.0s
default	13:17:05.463210-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.41851965.41851974.E07E1E6A-F99F-44EE-AA0C-BCFC3DC26379(501)>:3817] from originator [osservice<com.apple.controlcenter(501)>:638] with description <RBSAssertionDescriptor| "FBWorkspaceDomain: injecting saved endowment" ID:394-638-1288042 target:3817 attributes:[
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"WorkspaceEndpointInjection" sourceEnvironment:"(null)">
	]>
default	13:17:05.463308-0500	runningboardd	Assertion 394-638-1288042 (target:[app<application.com.nexy.assistant.41851965.41851974.E07E1E6A-F99F-44EE-AA0C-BCFC3DC26379(501)>:3817]) will be created as active
default	13:17:05.463445-0500	Nexy	[com.apple.controlcenter:4C955EBC-E598-4C97-ADE7-FDAC6EEE3402-Aux[1]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
default	13:17:05.463463-0500	Nexy	[com.apple.controlcenter:4C955EBC-E598-4C97-ADE7-FDAC6EEE3402-Aux[1]-NSStatusItemView] Dropping transition context because the scene is reconnecting
default	13:17:05.463726-0500	runningboardd	[app<application.com.nexy.assistant.41851965.41851974.E07E1E6A-F99F-44EE-AA0C-BCFC3DC26379(501)>:3817] Ignoring jetsam update because this process is not memory-managed
default	13:17:05.463737-0500	runningboardd	[app<application.com.nexy.assistant.41851965.41851974.E07E1E6A-F99F-44EE-AA0C-BCFC3DC26379(501)>:3817] Ignoring suspend because this process is not lifecycle managed
default	13:17:05.463747-0500	runningboardd	[app<application.com.nexy.assistant.41851965.41851974.E07E1E6A-F99F-44EE-AA0C-BCFC3DC26379(501)>:3817] Ignoring GPU update because this process is not GPU managed
default	13:17:05.463882-0500	runningboardd	[app<application.com.nexy.assistant.41851965.41851974.E07E1E6A-F99F-44EE-AA0C-BCFC3DC26379(501)>:3817] Ignoring memory limit update because this process is not memory-managed
default	13:17:05.466590-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.41851965.41851974.E07E1E6A-F99F-44EE-AA0C-BCFC3DC26379(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	13:17:05.467253-0500	ControlCenter	Adding: <FBApplicationProcess: 0x8e3783480; app<application.com.nexy.assistant.41851965.41851974.E07E1E6A-F99F-44EE-AA0C-BCFC3DC26379>:3817(v360AF9)>
default	13:17:05.467592-0500	gamepolicyd	Received state update for 3817 (app<application.com.nexy.assistant.41851965.41851974.E07E1E6A-F99F-44EE-AA0C-BCFC3DC26379(501)>, running-active-NotVisible
default	13:17:05.467811-0500	Nexy	[com.apple.controlcenter:4C955EBC-E598-4C97-ADE7-FDAC6EEE3402-Aux[1]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
default	13:17:05.467830-0500	Nexy	[com.apple.controlcenter:4C955EBC-E598-4C97-ADE7-FDAC6EEE3402-Aux[1]-NSStatusItemView] Dropping transition context because the scene is reconnecting
default	13:17:05.467952-0500	Nexy	Warning: the app is using `-[NSStatusBarButton setHighlightsBy:]` to set the highlight behavior. Instead, consider removing that setting. That will enable macOS to highlight the status bar button as appropriate for all configurations (e.g., light, dark, and increased contrast modes).
default	13:17:05.467977-0500	ControlCenter	[app<application.com.nexy.assistant.41851965.41851974.E07E1E6A-F99F-44EE-AA0C-BCFC3DC26379>:3817] Connection established.
default	13:17:05.468125-0500	ControlCenter	[app<application.com.nexy.assistant.41851965.41851974.E07E1E6A-F99F-44EE-AA0C-BCFC3DC26379>:3817] created proxy of <BSXPCServiceConnectionProxy<FBSWorkspaceServiceServerInterface>: 0x8e889cf50>
default	13:17:05.468195-0500	ControlCenter	[app<application.com.nexy.assistant.41851965.41851974.E07E1E6A-F99F-44EE-AA0C-BCFC3DC26379>:3817] Connection to remote process established!
default	13:17:05.468308-0500	ControlCenter	Received state update for 3817 (app<application.com.nexy.assistant.41851965.41851974.E07E1E6A-F99F-44EE-AA0C-BCFC3DC26379(501)>, running-active-NotVisible
default	13:17:05.484038-0500	ControlCenter	Asked to bootstrap a new process for handle: [app<application.com.nexy.assistant.41851965.41851974.E07E1E6A-F99F-44EE-AA0C-BCFC3DC26379(501)>:3817]
default	13:17:05.484062-0500	ControlCenter	A process already exists for this handle: <FBApplicationProcess: 0x8e3783480; app<application.com.nexy.assistant.41851965.41851974.E07E1E6A-F99F-44EE-AA0C-BCFC3DC26379>:3817(v360AF9)>
default	13:17:05.484232-0500	ControlCenter	[app<application.com.nexy.assistant.41851965.41851974.E07E1E6A-F99F-44EE-AA0C-BCFC3DC26379>:3817] Registered new scene: <FBWorkspaceScene: 0x8e4ae2340; com.apple.controlcenter:4C955EBC-E598-4C97-ADE7-FDAC6EEE3402> (fromRemnant = 0)
default	13:17:05.484285-0500	ControlCenter	[app<application.com.nexy.assistant.41851965.41851974.E07E1E6A-F99F-44EE-AA0C-BCFC3DC26379>:3817] Workspace interruption policy did change: reconnect
default	13:17:05.484693-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.41851965.41851974.E07E1E6A-F99F-44EE-AA0C-BCFC3DC26379(501)>:3817] from originator [osservice<com.apple.controlcenter(501)>:638] with description <RBSAssertionDescriptor| "com.apple.frontboard.after-life.interrupted" ID:394-638-1288043 target:3817 attributes:[
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"AfterLife-Interrupted" sourceEnvironment:"(null)">
	]>
default	13:17:05.484806-0500	runningboardd	Assertion 394-638-1288043 (target:[app<application.com.nexy.assistant.41851965.41851974.E07E1E6A-F99F-44EE-AA0C-BCFC3DC26379(501)>:3817]) will be created as inactive as originator process has not exited
default	13:17:05.485078-0500	Nexy	Request for <FBSScene: 0xa3051fa20; com.apple.controlcenter:4C955EBC-E598-4C97-ADE7-FDAC6EEE3402> complete!
default	13:17:05.485071-0500	ControlCenter	[com.apple.controlcenter:4C955EBC-E598-4C97-ADE7-FDAC6EEE3402] Client process connected: [app<application.com.nexy.assistant.41851965.41851974.E07E1E6A-F99F-44EE-AA0C-BCFC3DC26379(501)>:3817]
default	13:17:05.487891-0500	ControlCenter	Asked to bootstrap a new process for handle: [app<application.com.nexy.assistant.41851965.41851974.E07E1E6A-F99F-44EE-AA0C-BCFC3DC26379(501)>:3817]
default	13:17:05.488015-0500	ControlCenter	A process already exists for this handle: <FBApplicationProcess: 0x8e3783480; app<application.com.nexy.assistant.41851965.41851974.E07E1E6A-F99F-44EE-AA0C-BCFC3DC26379>:3817(v360AF9)>
default	13:17:05.487925-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.41851965.41851974.E07E1E6A-F99F-44EE-AA0C-BCFC3DC26379(501)>:3817] from originator [osservice<com.apple.controlcenter(501)>:638] with description <RBSAssertionDescriptor| "FBWorkspace (BG-Active[40])" ID:394-638-1288044 target:3817 attributes:[
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableLPRunReason-Suspend" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableRole-NonUI" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableJetsamPriority-Active" sourceEnvironment:"(null)">
	]>
default	13:17:05.488100-0500	runningboardd	Assertion 394-638-1288044 (target:[app<application.com.nexy.assistant.41851965.41851974.E07E1E6A-F99F-44EE-AA0C-BCFC3DC26379(501)>:3817]) will be created as active
default	13:17:05.488110-0500	ControlCenter	[app<application.com.nexy.assistant.41851965.41851974.E07E1E6A-F99F-44EE-AA0C-BCFC3DC26379>:3817] Registered new scene: <FBWorkspaceScene: 0x8e4ae0e40; com.apple.controlcenter:4C955EBC-E598-4C97-ADE7-FDAC6EEE3402-Aux[1]-NSStatusItemView> (fromRemnant = 0)
default	13:17:05.488534-0500	Nexy	Request for <FBSScene: 0xa3051fac0; com.apple.controlcenter:4C955EBC-E598-4C97-ADE7-FDAC6EEE3402-Aux[1]-NSStatusItemView> complete!
default	13:17:05.488215-0500	ControlCenter	[app<application.com.nexy.assistant.41851965.41851974.E07E1E6A-F99F-44EE-AA0C-BCFC3DC26379>:3817] Workspace state did change: XX-None[0] --> BG-Active[40] (assertion acquired).
default	13:17:05.488538-0500	ControlCenter	[com.apple.controlcenter:4C955EBC-E598-4C97-ADE7-FDAC6EEE3402-Aux[1]-NSStatusItemView] Client process connected: [app<application.com.nexy.assistant.41851965.41851974.E07E1E6A-F99F-44EE-AA0C-BCFC3DC26379(501)>:3817]
default	13:17:05.488589-0500	runningboardd	[app<application.com.nexy.assistant.41851965.41851974.E07E1E6A-F99F-44EE-AA0C-BCFC3DC26379(501)>:3817] Ignoring jetsam update because this process is not memory-managed
default	13:17:05.488658-0500	runningboardd	[app<application.com.nexy.assistant.41851965.41851974.E07E1E6A-F99F-44EE-AA0C-BCFC3DC26379(501)>:3817] Ignoring suspend because this process is not lifecycle managed
default	13:17:05.488750-0500	runningboardd	[app<application.com.nexy.assistant.41851965.41851974.E07E1E6A-F99F-44EE-AA0C-BCFC3DC26379(501)>:3817] Ignoring GPU update because this process is not GPU managed
default	13:17:05.488966-0500	Nexy	<FBSWorkspaceScenesClient:0xa3051f700 <private>> Reconnecting scene com.apple.controlcenter:4C955EBC-E598-4C97-ADE7-FDAC6EEE3402
default	13:17:05.488867-0500	runningboardd	[app<application.com.nexy.assistant.41851965.41851974.E07E1E6A-F99F-44EE-AA0C-BCFC3DC26379(501)>:3817] Ignoring memory limit update because this process is not memory-managed
default	13:17:05.489290-0500	Nexy	<FBSWorkspaceScenesClient:0xa3051f700 <private>> Reconnecting scene com.apple.controlcenter:4C955EBC-E598-4C97-ADE7-FDAC6EEE3402-Aux[1]-NSStatusItemView
default	13:17:05.492582-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.41851965.41851974.E07E1E6A-F99F-44EE-AA0C-BCFC3DC26379(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	13:17:05.493221-0500	ControlCenter	Received state update for 3817 (app<application.com.nexy.assistant.41851965.41851974.E07E1E6A-F99F-44EE-AA0C-BCFC3DC26379(501)>, running-active-NotVisible
default	13:17:05.493846-0500	gamepolicyd	Received state update for 3817 (app<application.com.nexy.assistant.41851965.41851974.E07E1E6A-F99F-44EE-AA0C-BCFC3DC26379(501)>, running-active-NotVisible
default	13:17:05.494990-0500	Nexy	Registering for test daemon availability notify post.
default	13:17:05.495212-0500	Nexy	notify_get_state check indicated test daemon not ready.
default	13:17:05.495363-0500	Nexy	notify_get_state check indicated test daemon not ready.
default	13:17:05.495474-0500	Nexy	notify_get_state check indicated test daemon not ready.
default	13:17:05.511214-0500	Nexy	registering darwin observer for name: com.apple.gms.availability.notification
default	13:17:05.511245-0500	Nexy	registering darwin observer for name: com.apple.os-eligibility-domain.change.greymatter
default	13:17:05.511276-0500	Nexy	registering darwin observer for name: com.apple.language.changed
default	13:17:05.511311-0500	Nexy	isAvailable value changed: isMDMAllowed = true, gmAvailable (current) = true
default	13:17:05.514570-0500	Nexy	[0xa305f7980] activating connection: mach=true listener=false peer=false name=com.apple.coreservices.appleevents
default	13:17:05.518594-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xb21255200 at /Applications/Nexy.app
default	13:17:05.525693-0500	Nexy	[0xa305f43c0] Connection returned listener port: 0x4f03
default	13:17:05.526284-0500	Nexy	SignalReady: pid=3817 asn=0x0-0x17b67b5
default	13:17:05.526809-0500	Nexy	SIGNAL: pid=3817 asn=0x0x-0x17b67b5
default	13:17:05.527772-0500	loginwindow	-[Application _updateInformationInternal] | Got App URL: file:///Applications/Nexy.app/
default	13:17:05.538203-0500	Nexy	[com.apple.controlcenter:4C955EBC-E598-4C97-ADE7-FDAC6EEE3402-Aux[1]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
default	13:17:05.544913-0500	Nexy	[com.apple.controlcenter:4C955EBC-E598-4C97-ADE7-FDAC6EEE3402-Aux[1]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
default	13:17:05.548213-0500	Nexy	void _NSDisableAutomaticTerminationAndLog(NSString *) Restoring windows
default	13:17:05.548223-0500	Nexy	-[NSApplication _reopenWindowsAsNecessaryIncludingRestorableState:withFullFidelity:completionHandler:] shouldRestoreState=1 hasPersistentStateToRestore=0 shouldStillRestoreStateAfterPrompting=0
default	13:17:05.548249-0500	Nexy	[0xa305f6a80] activating connection: mach=true listener=false peer=false name=com.apple.window_proxies
default	13:17:05.548360-0500	Nexy	[0xa305f6a80] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	13:17:05.549796-0500	Nexy	void _NSEnableAutomaticTerminationAndLog(NSString *) Restoring windows
default	13:17:05.552395-0500	Nexy	[C:2] Alloc <private>
default	13:17:05.552445-0500	Nexy	[0xa305f6a80] activating connection: mach=false listener=false peer=false name=(anonymous)
default	13:17:05.554496-0500	WindowManager	Connection activated | (3817) Nexy
default	13:17:05.554676-0500	ControlCenter	Host properties initialized; (bid:com.nexy.assistant-Item-0-3817). State(applicationItem: true, clientRequestsVisibility: true, neverClip: false)
default	13:17:05.556305-0500	ControlCenter	Starting to track host; (bid:com.nexy.assistant-Item-0-3817)
default	13:17:05.557362-0500	ControlCenter	Created new displayable type DisplayableAppStatusItemType(8036A47A, (bid:com.nexy.assistant-Item-0-3817)) for (bid:com.nexy.assistant-Item-0-3817)
default	13:17:05.558315-0500	ControlCenter	Adding displayable items for status items; [(bid:com.nexy.assistant-Item-0-3817)]
default	13:17:05.559124-0500	ControlCenter	Created instance DisplayableId(ED2A13F1) in .menuBar for DisplayableAppStatusItemType(8036A47A, (bid:com.nexy.assistant-Item-0-3817)) .menuBar
default	13:17:05.560200-0500	Nexy	[com.apple.controlcenter:4C955EBC-E598-4C97-ADE7-FDAC6EEE3402-Aux[1]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
default	13:17:05.561340-0500	Nexy	[com.apple.controlcenter:4C955EBC-E598-4C97-ADE7-FDAC6EEE3402] Sending action(s) in update: NSSceneFenceAction
default	13:17:05.567451-0500	Nexy	[0xa305f5540] activating connection: mach=false listener=false peer=false name=com.apple.ImageIOXPCService
default	13:17:05.569371-0500	ControlCenter	Created ephemaral instance DisplayableId(ED2A13F1) for (bid:com.nexy.assistant-Item-0-3817) with positioning .ephemeral
default	13:17:05.618758-0500	Nexy	[com.apple.controlcenter:4C955EBC-E598-4C97-ADE7-FDAC6EEE3402-Aux[1]-NSStatusItemView] Received action(s) in scene-update: NSSceneFenceAction
default	13:17:05.625992-0500	Nexy	[com.apple.controlcenter:4C955EBC-E598-4C97-ADE7-FDAC6EEE3402-Aux[1]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
default	13:17:05.629067-0500	Nexy	[com.apple.controlcenter:4C955EBC-E598-4C97-ADE7-FDAC6EEE3402-Aux[1]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
default	13:17:05.629600-0500	Nexy	[com.apple.controlcenter:4C955EBC-E598-4C97-ADE7-FDAC6EEE3402] Sending action(s) in update: NSSceneFenceAction
default	13:17:05.781372-0500	Nexy	*warn* MailCS ======%%% _setMailMessageAttributes skip:1
default	13:17:05.788006-0500	Nexy	Start service name com.apple.spotlightknowledged
default	13:17:05.788913-0500	Nexy	[GMS] availability notification token 92
default	13:17:05.831533-0500	ControlCenter	[app<application.com.nexy.assistant.41851965.41851974.E07E1E6A-F99F-44EE-AA0C-BCFC3DC26379>:3817] Workspace state did change: BG-Active[40] --> XX-None[0] (assertion dropped).
default	13:17:05.831726-0500	runningboardd	Invalidating assertion 394-638-1288044 (target:[app<application.com.nexy.assistant.41851965.41851974.E07E1E6A-F99F-44EE-AA0C-BCFC3DC26379(501)>:3817]) from originator [osservice<com.apple.controlcenter(501)>:638]
default	13:17:05.933870-0500	runningboardd	[app<application.com.nexy.assistant.41851965.41851974.E07E1E6A-F99F-44EE-AA0C-BCFC3DC26379(501)>:3817] Ignoring jetsam update because this process is not memory-managed
default	13:17:05.933912-0500	runningboardd	[app<application.com.nexy.assistant.41851965.41851974.E07E1E6A-F99F-44EE-AA0C-BCFC3DC26379(501)>:3817] Ignoring suspend because this process is not lifecycle managed
default	13:17:05.933937-0500	runningboardd	[app<application.com.nexy.assistant.41851965.41851974.E07E1E6A-F99F-44EE-AA0C-BCFC3DC26379(501)>:3817] Ignoring GPU update because this process is not GPU managed
default	13:17:05.934003-0500	runningboardd	[app<application.com.nexy.assistant.41851965.41851974.E07E1E6A-F99F-44EE-AA0C-BCFC3DC26379(501)>:3817] Ignoring memory limit update because this process is not memory-managed
default	13:17:05.939798-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.41851965.41851974.E07E1E6A-F99F-44EE-AA0C-BCFC3DC26379(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	13:17:05.940376-0500	ControlCenter	Received state update for 3817 (app<application.com.nexy.assistant.41851965.41851974.E07E1E6A-F99F-44EE-AA0C-BCFC3DC26379(501)>, running-active-NotVisible
default	13:17:05.940474-0500	gamepolicyd	Received state update for 3817 (app<application.com.nexy.assistant.41851965.41851974.E07E1E6A-F99F-44EE-AA0C-BCFC3DC26379(501)>, running-active-NotVisible
default	13:17:06.045253-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.41851965.41851974.E07E1E6A-F99F-44EE-AA0C-BCFC3DC26379(501)>:3817] from originator [osservice<com.apple.WindowServer(88)>:387] with description <RBSAssertionDescriptor| "AppDrawing" ID:394-387-1288047 target:3817 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"AppDrawing" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	13:17:06.045368-0500	runningboardd	Assertion 394-387-1288047 (target:[app<application.com.nexy.assistant.41851965.41851974.E07E1E6A-F99F-44EE-AA0C-BCFC3DC26379(501)>:3817]) will be created as active
default	13:17:06.045795-0500	runningboardd	[app<application.com.nexy.assistant.41851965.41851974.E07E1E6A-F99F-44EE-AA0C-BCFC3DC26379(501)>:3817] Ignoring jetsam update because this process is not memory-managed
default	13:17:06.045808-0500	runningboardd	[app<application.com.nexy.assistant.41851965.41851974.E07E1E6A-F99F-44EE-AA0C-BCFC3DC26379(501)>:3817] Ignoring suspend because this process is not lifecycle managed
default	13:17:06.045818-0500	runningboardd	[app<application.com.nexy.assistant.41851965.41851974.E07E1E6A-F99F-44EE-AA0C-BCFC3DC26379(501)>:3817] Ignoring GPU update because this process is not GPU managed
default	13:17:06.045838-0500	runningboardd	[app<application.com.nexy.assistant.41851965.41851974.E07E1E6A-F99F-44EE-AA0C-BCFC3DC26379(501)>:3817] Ignoring memory limit update because this process is not memory-managed
default	13:17:06.048871-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.41851965.41851974.E07E1E6A-F99F-44EE-AA0C-BCFC3DC26379(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	13:17:06.049376-0500	ControlCenter	Received state update for 3817 (app<application.com.nexy.assistant.41851965.41851974.E07E1E6A-F99F-44EE-AA0C-BCFC3DC26379(501)>, running-active-NotVisible
default	13:17:06.049424-0500	gamepolicyd	Received state update for 3817 (app<application.com.nexy.assistant.41851965.41851974.E07E1E6A-F99F-44EE-AA0C-BCFC3DC26379(501)>, running-active-NotVisible
default	13:17:07.560589-0500	runningboardd	Invalidating assertion 394-638-1288041 (target:app<application.com.nexy.assistant.41851965.41851974.E07E1E6A-F99F-44EE-AA0C-BCFC3DC26379(501)>) from originator [osservice<com.apple.controlcenter(501)>:638]
default	13:17:07.663650-0500	runningboardd	Removed last relative-start-date-defining assertion for process app<application.com.nexy.assistant.41851965.41851974.E07E1E6A-F99F-44EE-AA0C-BCFC3DC26379(501)>
default	13:17:07.664494-0500	runningboardd	[app<application.com.nexy.assistant.41851965.41851974.E07E1E6A-F99F-44EE-AA0C-BCFC3DC26379(501)>:3817] Ignoring jetsam update because this process is not memory-managed
default	13:17:07.664506-0500	runningboardd	[app<application.com.nexy.assistant.41851965.41851974.E07E1E6A-F99F-44EE-AA0C-BCFC3DC26379(501)>:3817] Ignoring suspend because this process is not lifecycle managed
default	13:17:07.664520-0500	runningboardd	[app<application.com.nexy.assistant.41851965.41851974.E07E1E6A-F99F-44EE-AA0C-BCFC3DC26379(501)>:3817] Ignoring GPU update because this process is not GPU managed
default	13:17:07.664550-0500	runningboardd	[app<application.com.nexy.assistant.41851965.41851974.E07E1E6A-F99F-44EE-AA0C-BCFC3DC26379(501)>:3817] Ignoring memory limit update because this process is not memory-managed
default	13:17:07.667897-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.41851965.41851974.E07E1E6A-F99F-44EE-AA0C-BCFC3DC26379(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	13:17:07.673029-0500	ControlCenter	Received state update for 3817 (app<application.com.nexy.assistant.41851965.41851974.E07E1E6A-F99F-44EE-AA0C-BCFC3DC26379(501)>, running-active-NotVisible
default	13:17:07.673244-0500	gamepolicyd	Received state update for 3817 (app<application.com.nexy.assistant.41851965.41851974.E07E1E6A-F99F-44EE-AA0C-BCFC3DC26379(501)>, running-active-NotVisible
default	13:17:10.429151-0500	Nexy	void _updateToReflectAutomaticTerminationState(void) Setting _kLSApplicationWouldBeTerminatedByTALKey=1
default	13:17:16.423841-0500	Nexy	LSExceptions shared instance invalidated for timeout.
