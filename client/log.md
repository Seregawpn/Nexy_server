default	17:21:39.308733-0500	dmd	Received xpc stream event (distributed notification matching) with name: com.apple.LaunchServices.applicationRegistered user info: {
    CFBundleDisplayName = Nexy;
    bundleIDs =     (
        "com.nexy.assistant"
    );
    isPlaceholder = 0;
}
default	17:21:39.316425-0500	runningboardd	Launch request for app<application.com.nexy.assistant.54878181.54878190(501)>[0] is using uid 501 (divined from auid 501 euid 501)
default	17:21:39.316495-0500	runningboardd	Acquiring assertion targeting app<application.com.nexy.assistant.54878181.54878190(501)> from originator [osservice<com.apple.coreservices.uiagent(501)>:99676] with description <RBSAssertionDescriptor| "LS launch com.nexy.assistant" ID:400-99676-16843 target:app<application.com.nexy.assistant.54878181.54878190(501)> attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"LaunchRoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	17:21:39.316566-0500	runningboardd	Assertion 400-99676-16843 (target:app<application.com.nexy.assistant.54878181.54878190(501)>) will be created as active
default	17:21:39.369074-0500	runningboardd	[app<application.com.nexy.assistant.54878181.54878190(501)>:21340] is not RunningBoard jetsam managed.
default	17:21:39.369087-0500	runningboardd	[app<application.com.nexy.assistant.54878181.54878190(501)>:21340] This process will not be managed.
default	17:21:39.369096-0500	runningboardd	Now tracking process: [app<application.com.nexy.assistant.54878181.54878190(501)>:21340]
default	17:21:39.369229-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.54878181.54878190(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	17:21:39.369714-0500	gamepolicyd	Hit the server for a process handle 1c2fa5b30000535c that resolved to: [app<application.com.nexy.assistant.54878181.54878190(501)>:21340]
default	17:21:39.369738-0500	gamepolicyd	Received state update for 21340 (app<application.com.nexy.assistant.54878181.54878190(501)>, running-active-NotVisible
default	17:21:39.373193-0500	runningboardd	Using default underlying assertion for app: [app<application.com.nexy.assistant.54878181.54878190(501)>:21340]
default	17:21:39.373234-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.54878181.54878190(501)>:21340] from originator [app<application.com.nexy.assistant.54878181.54878190(501)>:21340] with description <RBSAssertionDescriptor| "RB Underlying Assertion" ID:400-400-16844 target:21340 attributes:[
	<RBSDomainAttribute| domain:"com.apple.underlying" name:"defaultUnderlyingAppAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	17:21:39.373306-0500	runningboardd	Assertion 400-400-16844 (target:[app<application.com.nexy.assistant.54878181.54878190(501)>:21340]) will be created as active
default	17:21:39.373414-0500	runningboardd	[app<application.com.nexy.assistant.54878181.54878190(501)>:21340] Ignoring jetsam update because this process is not memory-managed
default	17:21:39.373428-0500	runningboardd	[app<application.com.nexy.assistant.54878181.54878190(501)>:21340] Ignoring suspend because this process is not lifecycle managed
default	17:21:39.373446-0500	runningboardd	[app<application.com.nexy.assistant.54878181.54878190(501)>:21340] Set darwin role to: UserInteractive
default	17:21:39.373482-0500	runningboardd	[app<application.com.nexy.assistant.54878181.54878190(501)>:21340] Ignoring GPU update because this process is not GPU managed
default	17:21:39.373505-0500	runningboardd	[app<application.com.nexy.assistant.54878181.54878190(501)>:21340] reported to RB as running
default	17:21:39.373560-0500	runningboardd	[app<application.com.nexy.assistant.54878181.54878190(501)>:21340] Ignoring memory limit update because this process is not memory-managed
default	17:21:39.374722-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.54878181.54878190(501)>:21340] from originator [osservice<com.apple.coreservices.launchservicesd>:361] with description <RBSAssertionDescriptor| "uielement:21340" ID:400-361-16845 target:21340 attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"RoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	17:21:39.374883-0500	runningboardd	Assertion 400-361-16845 (target:[app<application.com.nexy.assistant.54878181.54878190(501)>:21340]) will be created as active
default	17:21:39.374905-0500	CoreServicesUIAgent	LAUNCH: 0x0-0x1eb1eb com.nexy.assistant starting stopped process.
default	17:21:39.376192-0500	loginwindow	-[Application _updateInformationInternal] | Got App URL: file:///Applications/Nexy.app/
default	17:21:39.376347-0500	loginwindow	-[Application setState:] | enter: <Application: 0xc01219400: Nexy> state 2
default	17:21:39.376365-0500	loginwindow	-[ApplicationManager checkInAppContext:eventData:] | ApplicationManager: Checked in app : Nexy
default	17:21:39.376970-0500	runningboardd	[app<application.com.nexy.assistant.54878181.54878190(501)>:21340] Ignoring jetsam update because this process is not memory-managed
default	17:21:39.376991-0500	runningboardd	[app<application.com.nexy.assistant.54878181.54878190(501)>:21340] Ignoring suspend because this process is not lifecycle managed
default	17:21:39.377022-0500	runningboardd	[app<application.com.nexy.assistant.54878181.54878190(501)>:21340] Ignoring GPU update because this process is not GPU managed
default	17:21:39.377074-0500	runningboardd	[app<application.com.nexy.assistant.54878181.54878190(501)>:21340] Ignoring memory limit update because this process is not memory-managed
default	17:21:39.377160-0500	runningboardd	Successfully acquired underlying assertion for [app<application.com.nexy.assistant.54878181.54878190(501)>:21340]
default	17:21:39.379241-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.54878181.54878190(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	17:21:39.379463-0500	runningboardd	Invalidating assertion 400-99676-16843 (target:app<application.com.nexy.assistant.54878181.54878190(501)>) from originator [osservice<com.apple.coreservices.uiagent(501)>:99676]
default	17:21:39.379487-0500	runningboardd	[app<application.com.nexy.assistant.54878181.54878190(501)>:21340] Ignoring jetsam update because this process is not memory-managed
default	17:21:39.379483-0500	gamepolicyd	Received state update for 21340 (app<application.com.nexy.assistant.54878181.54878190(501)>, running-active-NotVisible
default	17:21:39.379518-0500	runningboardd	[app<application.com.nexy.assistant.54878181.54878190(501)>:21340] Ignoring suspend because this process is not lifecycle managed
default	17:21:39.379551-0500	runningboardd	[app<application.com.nexy.assistant.54878181.54878190(501)>:21340] Ignoring GPU update because this process is not GPU managed
default	17:21:39.379652-0500	runningboardd	[app<application.com.nexy.assistant.54878181.54878190(501)>:21340] Ignoring memory limit update because this process is not memory-managed
default	17:21:39.382380-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.54878181.54878190(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	17:21:39.382458-0500	runningboardd	[app<application.com.nexy.assistant.54878181.54878190(501)>:21340] Ignoring jetsam update because this process is not memory-managed
default	17:21:39.382469-0500	runningboardd	[app<application.com.nexy.assistant.54878181.54878190(501)>:21340] Ignoring suspend because this process is not lifecycle managed
default	17:21:39.382478-0500	runningboardd	[app<application.com.nexy.assistant.54878181.54878190(501)>:21340] Ignoring GPU update because this process is not GPU managed
default	17:21:39.382520-0500	runningboardd	[app<application.com.nexy.assistant.54878181.54878190(501)>:21340] Ignoring memory limit update because this process is not memory-managed
default	17:21:39.385801-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.54878181.54878190(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	17:21:39.486445-0500	gamepolicyd	Received state update for 21340 (app<application.com.nexy.assistant.54878181.54878190(501)>, running-active-NotVisible
default	17:21:39.666814-0500	syspolicyd	GK evaluateScanResult: 3, PST: (path: a2cffff67b96be6e), (team: 5NKLL2CLB9), (id: com.nexy.assistant), (bundle_id: (null)), 0, 0, 1, 0, 9, 4, 1
default	17:21:39.667571-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=508.20, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=21340, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.syspolicyd, pid=508, auid=0, euid=0, binary_path=/usr/libexec/syspolicyd}, },
default	17:21:39.670680-0500	tccd	AUTHREQ_SUBJECT: msgID=508.20, subject=com.nexy.assistant,
default	17:21:39.671089-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b5167600 at /Applications/Nexy.app
default	17:21:39.678395-0500	syspolicyd	Found provenance data on target: TA(c1427ed62e916d1d, 2), PST: (path: a2cffff67b96be6e), (team: 5NKLL2CLB9), (id: com.nexy.assistant), (bundle_id: (null))
default	17:21:39.683708-0500	kernel	Nexy[21340] triggered unnest of range 0x1f8000000->0x1fa000000 of DYLD shared region in VM map 0x136dd6400a074891. While not abnormal for debuggers, this increases system memory footprint until the target exits.
default	17:21:39.683723-0500	kernel	Nexy[21340] triggered unnest of range 0x1fa000000->0x1fc000000 of DYLD shared region in VM map 0x136dd6400a074891. While not abnormal for debuggers, this increases system memory footprint until the target exits.
default	17:21:39.805676-0500	Nexy	[0x102f34f00] activating connection: mach=true listener=false peer=false name=com.apple.cfprefsd.daemon
default	17:21:39.805713-0500	Nexy	[0x102f35440] activating connection: mach=true listener=false peer=false name=com.apple.cfprefsd.agent
error	17:21:39.913836-0500	Nexy	dlsym cannot find symbol NSMakeRect in CFBundle 0x102f3e660 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	17:21:39.913959-0500	Nexy	dlsym cannot find symbol NSMakePoint in CFBundle 0x102f3e660 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	17:21:39.914072-0500	Nexy	dlsym cannot find symbol NSMakeSize in CFBundle 0x102f3e660 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	17:21:39.914191-0500	Nexy	dlsym cannot find symbol NSMakeRange in CFBundle 0x102f3e660 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
default	17:21:39.914776-0500	Nexy	[0x102f3faa0] activating connection: mach=true listener=false peer=false name=com.apple.coreservices.launchservicesd
default	17:21:39.915148-0500	Nexy	[0x82cb14000] activating connection: mach=true listener=false peer=false name=com.apple.analyticsd
default	17:21:39.915292-0500	Nexy	[0x82cb14140] activating connection: mach=true listener=false peer=false name=com.apple.pasteboard.1
default	17:21:39.915491-0500	Nexy	[0x82cb14280] activating connection: mach=true listener=false peer=false name=com.apple.distributed_notifications@Uv3
default	17:21:39.915832-0500	Nexy	Received configuration update from daemon (initial)
default	17:21:39.916467-0500	Nexy	void _NSDisableAutomaticTerminationAndLog(NSString *) No windows open yet
default	17:21:39.916637-0500	Nexy	[0x82cb143c0] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	17:21:39.916970-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=21340.1, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=21340, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	17:21:39.917747-0500	tccd	AUTHREQ_SUBJECT: msgID=21340.1, subject=com.nexy.assistant,
default	17:21:39.918171-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b5164f00 at /Applications/Nexy.app
default	17:21:39.925092-0500	Nexy	[0x82cb143c0] invalidated after the last release of the connection object
default	17:21:39.925911-0500	Nexy	server port 0x0000370b, session port 0x0000370b
default	17:21:39.926485-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=391.809, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=21340, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=391, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	17:21:39.926500-0500	tccd	requestor: TCCDProcess: identifier=com.apple.WindowServer, pid=391, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=21340, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	17:21:39.926959-0500	tccd	AUTHREQ_SUBJECT: msgID=391.809, subject=com.nexy.assistant,
default	17:21:39.927350-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b5164f00 at /Applications/Nexy.app
default	17:21:39.936548-0500	Nexy	New connection 0xfe583 main
default	17:21:39.937856-0500	Nexy	CHECKIN: pid=21340
default	17:21:39.942245-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.54878181.54878190(501)>:21340] from originator [osservice<com.apple.coreservices.launchservicesd>:361] with description <RBSAssertionDescriptor| "uielement:21340" ID:400-361-16846 target:21340 attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"RoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	17:21:39.942292-0500	runningboardd	Assertion 400-361-16846 (target:[app<application.com.nexy.assistant.54878181.54878190(501)>:21340]) will be created as active
default	17:21:39.942603-0500	runningboardd	Invalidating assertion 400-361-16845 (target:[app<application.com.nexy.assistant.54878181.54878190(501)>:21340]) from originator [osservice<com.apple.coreservices.launchservicesd>:361]
default	17:21:39.942718-0500	Nexy	CHECKEDIN: pid=21340 asn=0x0-0x1eb1eb foreground=0
default	17:21:39.942589-0500	launchservicesd	CHECKIN:0x0-0x1eb1eb 21340 com.nexy.assistant
default	17:21:39.942862-0500	Nexy	[0x82cb143c0] activating connection: mach=false listener=true peer=false name=(anonymous)
default	17:21:39.943383-0500	loginwindow	-[Application _updateInformationInternal] | Got App URL: file:///Applications/Nexy.app/
default	17:21:39.942866-0500	Nexy	[0x82cb143c0] Connection returned listener port: 0x5103
default	17:21:39.943474-0500	loginwindow	-[ApplicationManager checkInAppContext:eventData:] | ApplicationManager: Checked in app : Nexy
default	17:21:39.943082-0500	Nexy	[0x82db14300] activating connection: mach=false listener=false peer=true name=com.apple.xpc.anonymous.0x82cb143c0.peer[361].0x82db14300
default	17:21:39.944830-0500	Nexy	FRONTLOGGING: version 1
default	17:21:39.944871-0500	Nexy	Registered, pid=21340 ASN=0x0,0x1eb1eb
default	17:21:39.945118-0500	WindowServer	fe583[CreateApplication]: Process creation: 0x0-0x1eb1eb (Nexy) connectionID: FE583 pid: 21340 in session 0x101
default	17:21:39.945242-0500	Nexy	[0x82cb14500] activating connection: mach=true listener=false peer=false name=com.apple.lsd.mapdb
default	17:21:39.946377-0500	Nexy	[0x82cb143c0] Connection returned listener port: 0x5103
default	17:21:39.947156-0500	Nexy	BringForward: pid=21340 asn=0x0-0x1eb1eb bringForward=0 foreground=0 uiElement=1 launchedByLS=1 modifiersCount=1 allDisabled=0
default	17:21:39.947427-0500	Nexy	BringFrontModifier: pid=21340 asn=0x0-0x1eb1eb Modifier 0 hideAfter=0 hideOthers=0 dontMakeFrontmost=0 mouseDown=0/0 seed=0/0
default	17:21:39.947968-0500	Nexy	Current system appearance, (HLTB: 1), (SLS: 0)
default	17:21:39.948600-0500	Nexy	No persisted cache on this platform.
default	17:21:39.949214-0500	Nexy	Current system appearance, (HLTB: 1), (SLS: 0)
default	17:21:39.949522-0500	Nexy	Post-registration system appearance: (HLTB: 1)
default	17:21:39.950999-0500	Nexy	FBSWorkspace: endpoint monitoring is disabled.
default	17:21:39.951004-0500	Nexy	FBSWorkspace: default shell endpoint is disabled.
default	17:21:39.951036-0500	Nexy	Initializing connection
default	17:21:39.951062-0500	Nexy	Removing all cached process handles
default	17:21:39.951077-0500	Nexy	Sending handshake request attempt #1 to server
default	17:21:39.951085-0500	Nexy	Creating connection to com.apple.runningboard
default	17:21:39.951090-0500	Nexy	[0x82cb14640] activating connection: mach=true listener=false peer=false name=com.apple.runningboard
default	17:21:39.951355-0500	runningboardd	Setting client for [app<application.com.nexy.assistant.54878181.54878190(501)>:21340] as ready
default	17:21:39.951746-0500	Nexy	Handshake succeeded
default	17:21:39.951756-0500	Nexy	Identity resolved as app<application.com.nexy.assistant.54878181.54878190(501)>
default	17:21:39.951935-0500	Nexy	[0x82cb143c0] Connection returned listener port: 0x5103
default	17:21:39.952965-0500	distnoted	register name: com.apple.xctest.FakeForceTouchDevice object: com.nexy.assistant token: 1e0000001d pid: 21340
default	17:21:39.957534-0500	Nexy	[0x82cb143c0] Connection returned listener port: 0x5103
default	17:21:39.959638-0500	Nexy	Created a new Process Instance Registry XPC connection (inactive)
default	17:21:39.959651-0500	Nexy	[0x82cb148c0] activating connection: mach=true listener=false peer=false name=com.apple.linkd.autoShortcut
default	17:21:39.959698-0500	Nexy	Activated connection to com.apple.linkd.autoShortcut (ApplicationService)
default	17:21:39.959723-0500	Nexy	[0x82cb14a00] activating connection: mach=false listener=true peer=false name=(anonymous)
default	17:21:39.960417-0500	Nexy	[0x82cb14a00] Connection returned listener port: 0x6703
default	17:21:39.960917-0500	Nexy	Registered process with identifier 21340-7977529
default	17:21:40.733161-0500	kernel	SK[9]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid BFE2565A-1A1C-45FF-99BE-349FC8BAC5D9 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.55118,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0x4604ac27 tp_proto=0x06"
default	17:21:40.733212-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:55118<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 5933824 t_state: SYN_SENT process: Nexy:21340 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x9a57fb44
default	17:21:40.771955-0500	kernel	tcp connected: [<IPv4-redacted>:55118<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 5933824 t_state: ESTABLISHED process: Nexy:21340 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x9a57fb44
default	17:21:40.772242-0500	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:55118<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 5933824 t_state: FIN_WAIT_1 process: Nexy:21340 Duration: 0.039 sec Conn_Time: 0.039 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 39.000 ms rttvar: 19.500 ms base rtt: 39 ms so_error: 0 svc/tc: 0 flow: 0x9a57fb44
default	17:21:40.772248-0500	kernel	tcp_connection_summary [<IPv4-redacted>:55118<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 5933824 t_state: FIN_WAIT_1 process: Nexy:21340 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	17:21:41.329152-0500	Nexy	Registered notify signal com.apple.caulk.alloc.rtdump (0)
default	17:21:41.330120-0500	Nexy	System_Input_Processing_Notification_Handler.mm:456   System_Input_Processing_Notification_Handler::is_vi_available(): Voice isolation DSP is available for client with bundle id com.nexy.assistant (AVFoundation is available, application is not in client deny list, application is not FaceTime variant)
default	17:21:41.331093-0500	Nexy	[0x82cb14dc0] activating connection: mach=true listener=false peer=false name=com.apple.cmio.registerassistantservice.system-extensions
fault	17:21:41.332324-0500	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.54878181.54878190 AUID=501> and <type=Application identifier=application.com.nexy.assistant.54878181.54878190>
default	17:21:41.333966-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOInitializeListenersForBundleID: for <private> -> <private>
default	17:21:41.334728-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> vpio_preferenceChangedListener: new value ((null)) for key AUVoiceIOClients/com-nexy-assistant/AUVoiceIOChatFlavor, translatedBundleID com.nexy.assistant, bundleIDs {(
    "com.nexy.assistant"
)}
default	17:21:41.334803-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> vpio_preferenceChangedListener: new value ((null)) for key AUVoiceIOClients/com-nexy-assistant/AUVoiceIOIsAutoChatFlavorEnabled, translatedBundleID com.nexy.assistant, bundleIDs {(
    "com.nexy.assistant"
)}
default	17:21:41.334868-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetSupportedChatFlavorsForBundleID: <private>-><private> get supported chat flavors: <private>
default	17:21:41.334873-0500	Nexy	            HALSystem.cpp:134    Enabling HAL Voice Isolation support
default	17:21:41.334891-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetHiddenChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	17:21:41.334950-0500	Nexy	[0x82cb14f00] activating connection: mach=true listener=false peer=false name=com.apple.tccd
default	17:21:41.335220-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=21340.2, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=21340, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	17:21:41.338812-0500	tccd	AUTHREQ_SUBJECT: msgID=21340.2, subject=com.nexy.assistant,
default	17:21:41.339118-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x722e70300 at /Applications/Nexy.app
default	17:21:41.345287-0500	Nexy	[0x82cb14f00] invalidated after the last release of the connection object
default	17:21:41.345316-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetSupportedChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	17:21:41.347659-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.954, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=21340, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=392, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	17:21:41.348186-0500	tccd	AUTHREQ_SUBJECT: msgID=401.954, subject=com.nexy.assistant,
default	17:21:41.348498-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x722e70300 at /Applications/Nexy.app
error	17:21:41.354933-0500	tccd	Request message contains a target_token to accessing_process (TCCDProcess: identifier=com.nexy.assistant, pid=21340, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy) but TCCDProcess: identifier=com.apple.audio.coreaudiod, pid=401, auid=202, euid=202, binary_path=/usr/sbin/coreaudiod is not a TCC manager for service: kTCCServiceScreenCapture.
default	17:21:41.355460-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.956, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=21340, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=392, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	17:21:41.356081-0500	tccd	AUTHREQ_SUBJECT: msgID=401.956, subject=com.nexy.assistant,
default	17:21:41.356379-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x722e70300 at /Applications/Nexy.app
default	17:21:41.364005-0500	Nexy	  HALPlugInManagement.cpp:440    HALPlugInManagement::RegisterPlugIns: skipping in-process plug-ins
error	17:21:41.364012-0500	Nexy	AddInstanceForFactory: No factory registered for id <CFUUID 0x82f843980> F8BB1C28-BAE8-11D6-9C31-00039315CD46
default	17:21:41.372021-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetPreferredChatFlavorForBundleID: <private>-><private> get value: 0
default	17:21:41.374465-0500	Nexy	[0x82cb14f00] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioComponentRegistrar
default	17:21:41.805468-0500	Nexy	                AUHAL.cpp:420   AUHAL: (0x82f29b140) Selecting device 71 from constructor
default	17:21:41.805479-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0x82f29b140)
default	17:21:41.805486-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0x82f29b140) not already running
default	17:21:41.805494-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0x82f29b140) nothing to teardown
default	17:21:41.805500-0500	Nexy	                AUHAL.cpp:762   SelectDevice: (0x82f29b140) connecting device 71
default	17:21:41.805614-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0x82f29b140) Device ID: 71 (Input:No | Output:Yes): true
default	17:21:41.805712-0500	Nexy	                AUHAL.cpp:774   SelectDevice: (0x82f29b140) created ioproc 0xa for device 71
default	17:21:41.805845-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x82f29b140) adding 7 device listeners to device 71
default	17:21:41.806072-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x82f29b140) adding 0 device delegate listeners to device 71
default	17:21:41.806082-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x82f29b140)
default	17:21:41.806163-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x48]:  2 ch,  48000 Hz, Float32, interleaved
default	17:21:41.806173-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	17:21:41.806180-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	17:21:41.806189-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	17:21:41.806199-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	17:21:41.806308-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x82f29b140) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	17:21:41.806320-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x82f29b140) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	17:21:41.806329-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	17:21:41.806334-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x82f29b140) removing 0 device listeners from device 0
default	17:21:41.806339-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x82f29b140) removing 0 device delegate listeners from device 0
default	17:21:41.806349-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0x82f29b140)
default	17:21:41.806364-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is DISABLED
default	17:21:41.806437-0500	Nexy	                AUHAL.cpp:2303  SetProperty: (0x82f29b140) caller requesting device change from 71 to 78
default	17:21:41.806448-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0x82f29b140)
default	17:21:41.806454-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0x82f29b140) not already running
default	17:21:41.806459-0500	Nexy	                AUHAL.cpp:687   SelectDevice: (0x82f29b140) disconnecting device 71
default	17:21:41.806464-0500	Nexy	                AUHAL.cpp:751   SelectDevice: (0x82f29b140) destroying ioproc 0xa for device 71
default	17:21:41.806509-0500	Nexy	  AVAudioSession_MacOS.mm:1021  initForMacOS
default	17:21:41.807799-0500	Nexy	[0x82cb15180] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioSession
default	17:21:41.808624-0500	audiomxd	  ServerSessionManager.mm:315   { "action":"create_session", "session":{"ID":"0x1f4029","name":"Nexy(21340)"}, "details":{"PID":21340,"session_type":"Primary"} }
default	17:21:41.808706-0500	audiomxd	AudioApplicationInfoImpl.mm:250   Setting initial isRecording state: 0 for newly-created AudioApp
	app: {"name":"[implicit] Nexy","pid":21340}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1f4029, sessionType: 'prim', isRecording: false }, 
]
default	17:21:41.809350-0500	audiomxd	  ServerSessionManager.mm:1322  Start process monitoring, pid = 21340, name = Nexy
default	17:21:41.809597-0500	Nexy	    SessionCore_Create.mm:99    Created session 0x82cb5d000 with ID: 0x1f4029
default	17:21:41.810472-0500	Nexy	[0x82cb152c0] activating connection: mach=true listener=false peer=false name=com.apple.audioanalyticsd
error	17:21:41.810784-0500	Nexy	Reporter disconnected. { function=sendMessage, reporterID=91654602096641 }
default	17:21:41.810796-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped Unknown {BuiltInSpeakerDevice, 0xa}
default	17:21:41.810851-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	17:21:41.810940-0500	Nexy	                AUHAL.cpp:762   SelectDevice: (0x82f29b140) connecting device 78
default	17:21:41.811027-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0x82f29b140) Device ID: 78 (Input:Yes | Output:No): true
default	17:21:41.812174-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.957, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=21340, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=392, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	17:21:41.813416-0500	tccd	AUTHREQ_SUBJECT: msgID=401.957, subject=com.nexy.assistant,
default	17:21:41.814079-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x722e70300 at /Applications/Nexy.app
default	17:21:41.829485-0500	tccd	AUTHREQ_PROMPTING: msgID=401.957, service=kTCCServiceMicrophone, subject=Sub:{com.nexy.assistant}Resp:{TCCDProcess: identifier=com.nexy.assistant, pid=21340, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy},
default	17:21:43.288549-0500	tccd	Publishing <TCCDEvent: type=Create, service=kTCCServiceMicrophone, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 3 subscribers: {
    39 = "<TCCDEventSubscriber: token=39, state=Passed, csid=com.apple.chronod>";
    38 = "<TCCDEventSubscriber: token=38, state=Initial, csid=(null)>";
    41 = "<TCCDEventSubscriber: token=41, state=Passed, csid=com.apple.photolibraryd>";
}
default	17:21:43.289510-0500	Nexy	                AUHAL.cpp:774   SelectDevice: (0x82f29b140) created ioproc 0xa for device 78
default	17:21:43.289741-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x82f29b140) adding 7 device listeners to device 78
default	17:21:43.290106-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x82f29b140) adding 0 device delegate listeners to device 78
default	17:21:43.290122-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x82f29b140)
default	17:21:43.290138-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 output streams; not all mono
default	17:21:43.290157-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	17:21:43.290072-0500	chronod	[appAuth:com.nexy.assistant] tcc authorization(s) changed
default	17:21:43.290390-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  input stream 0 [0x4f]:  1 ch,  44100 Hz, Float32
default	17:21:43.290405-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 input streams; all mono
default	17:21:43.290416-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  1 ch,  44100 Hz, Float32
default	17:21:43.290554-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x82f29b140) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	17:21:43.290579-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x82f29b140) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	17:21:43.290586-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	17:21:43.290595-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x82f29b140) removing 7 device listeners from device 71
default	17:21:43.290862-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x82f29b140) removing 0 device delegate listeners from device 71
default	17:21:43.290879-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0x82f29b140)
default	17:21:43.291526-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	17:21:43.293325-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.958, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=21340, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=392, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	17:21:43.295185-0500	tccd	AUTHREQ_SUBJECT: msgID=401.958, subject=com.nexy.assistant,
default	17:21:43.296367-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x722e70300 at /Applications/Nexy.app
default	17:21:43.317650-0500	Nexy	       ACv2Workarounds.mm:51    com.nexy.assistant: fix84702776_86723525_86479548_89800354_SinglePacketDesc: false
default	17:21:43.317718-0500	Nexy	Registered notify signal com.apple.caulk.alloc.audiodump (0)
default	17:21:43.317874-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0x82ba454d0, from  1 ch,  44100 Hz, Float32 to  1 ch,  16000 Hz, Float32
default	17:21:43.318301-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	17:21:43.319470-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.959, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=21340, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=392, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	17:21:43.321316-0500	tccd	AUTHREQ_SUBJECT: msgID=401.959, subject=com.nexy.assistant,
default	17:21:43.321893-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x722e70300 at /Applications/Nexy.app
default	17:21:43.337851-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.960, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=21340, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=392, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	17:21:43.338604-0500	tccd	AUTHREQ_SUBJECT: msgID=401.960, subject=com.nexy.assistant,
default	17:21:43.339032-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x722e70900 at /Applications/Nexy.app
default	17:21:43.350881-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetPreferredChatFlavorForBundleID: <private>-><private> get value: 0
default	17:21:43.351191-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetSupportedChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	17:21:43.351735-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.54878181.54878190(501)>:21340] from originator [osservice<com.apple.powerd>:332] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:400-332-16853 target:21340 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	17:21:43.351794-0500	runningboardd	Assertion 400-332-16853 (target:[app<application.com.nexy.assistant.54878181.54878190(501)>:21340]) will be created as active
default	17:21:43.352046-0500	runningboardd	[app<application.com.nexy.assistant.54878181.54878190(501)>:21340] Ignoring jetsam update because this process is not memory-managed
default	17:21:43.352082-0500	runningboardd	[app<application.com.nexy.assistant.54878181.54878190(501)>:21340] Ignoring suspend because this process is not lifecycle managed
default	17:21:43.352190-0500	runningboardd	[app<application.com.nexy.assistant.54878181.54878190(501)>:21340] Ignoring GPU update because this process is not GPU managed
default	17:21:43.352255-0500	runningboardd	[app<application.com.nexy.assistant.54878181.54878190(501)>:21340] Ignoring memory limit update because this process is not memory-managed
default	17:21:43.355386-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.54878181.54878190(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	17:21:43.356161-0500	gamepolicyd	Received state update for 21340 (app<application.com.nexy.assistant.54878181.54878190(501)>, running-active-NotVisible
default	17:21:43.376403-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Input {BuiltInMicrophoneDevice, 0xa}
default	17:21:43.377115-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1f4029","name":"Nexy(21340)"}, "details":{"deviceUIDs":[],"implicit_category":"Record","input_running":true,"output_running":false} }
default	17:21:43.377165-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 42, PID = 21340, Name = sid:0x1f4029, Nexy(21340), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	17:21:43.377192-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 42, PID = 21340, Name = sid:0x1f4029, Nexy(21340), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	17:21:43.377377-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	17:21:43.377396-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	17:21:43.377244-0500	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1f4029, Nexy(21340), 'prim'', AudioCategory changed to 'Record_WithBluetooth'
default	17:21:43.377307-0500	audiomxd	UpdateAudioState CID 0x91550001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	17:21:43.377305-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 42, PID = 21340, Name = sid:0x1f4029, Nexy(21340), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	17:21:43.377394-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 42, PID = 21340, Name = sid:0x1f4029, Nexy(21340), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	17:21:43.377567-0500	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 42, PID = 21340, Name = sid:0x1f4029, Nexy(21340), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> is going active
default	17:21:43.377572-0500	audiomxd	UpdateAudioState CID 0x91550001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	17:21:43.377599-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1f4029, Nexy(21340), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 42 starting recording
default	17:21:43.377850-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 42, PID = 21340, Name = sid:0x1f4029, Nexy(21340), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	17:21:43.377671-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	17:21:43.377692-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	17:21:43.378010-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [1, 0]. BT device UIDS: {(
)}
default	17:21:43.378093-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	17:21:43.378017-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	17:21:43.378103-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	17:21:43.377902-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 42, PID = 21340, Name = sid:0x1f4029, Nexy(21340), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
fault	17:21:43.377872-0500	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.54878181.54878190 AUID=501> and <type=Application identifier=application.com.nexy.assistant.54878181.54878190>
default	17:21:43.378108-0500	audioaccessoryd	AudioStateChanged: Added audio session app com.nexy.assistant NULL -> 200 count 1
default	17:21:43.378150-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	17:21:43.377928-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1f4029, Nexy(21340), 'prim'', displayID:'com.nexy.assistant'}
error	17:21:43.378190-0500	audioaccessoryd	Updating local audio category 100 -> 200 app com.nexy.assistant
default	17:21:43.378348-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	17:21:43.378279-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	17:21:43.378027-0500	audiomxd	UpdateAudioState CID 0x91550001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
fault	17:21:43.379199-0500	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.54878181.54878190 AUID=501> and <type=Application identifier=application.com.nexy.assistant.54878181.54878190>
default	17:21:43.382504-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {BuiltInMicrophoneDevice, 0xa}
default	17:21:43.382755-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1f4029","name":"Nexy(21340)"}, "details":{"deviceUIDs":[],"implicit_category":"","input_running":false,"output_running":false} }
default	17:21:43.382816-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 42, PID = 21340, Name = sid:0x1f4029, Nexy(21340), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	17:21:43.382848-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 42, PID = 21340, Name = sid:0x1f4029, Nexy(21340), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	17:21:43.382919-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1f4029, Nexy(21340), 'prim'', displayID:'com.nexy.assistant'}
default	17:21:43.383086-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1f4029, Nexy(21340), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 42 stopping recording
default	17:21:43.383135-0500	audiomxd	-MXCoreSession- -[MXCoreSession endInterruption:]: Session <ID: 42, PID = 21340, Name = sid:0x1f4029, Nexy(21340), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> is going inactive
default	17:21:43.383152-0500	audiomxd	UpdateAudioState CID 0x91550001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	17:21:43.383202-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 42, PID = 21340, Name = sid:0x1f4029, Nexy(21340), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	17:21:43.383275-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 42, PID = 21340, Name = sid:0x1f4029, Nexy(21340), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	17:21:43.383265-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	17:21:43.383425-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 0]. BT device UIDS: {(
)}
default	17:21:43.383430-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	17:21:43.383276-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	17:21:43.383281-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	17:21:43.383295-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	17:21:43.383563-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	17:21:43.383572-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	17:21:43.383074-0500	runningboardd	Invalidating assertion 400-332-16853 (target:[app<application.com.nexy.assistant.54878181.54878190(501)>:21340]) from originator [osservice<com.apple.powerd>:332]
default	17:21:43.383697-0500	audioaccessoryd	AudioStateChanged: Removed audio session app com.nexy.assistant 201 count 0
default	17:21:43.383451-0500	audiomxd	UpdateAudioState CID 0x91550001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	17:21:43.392162-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	17:21:43.392234-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	17:21:43.392258-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	17:21:43.392777-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	17:21:43.394638-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	17:21:43.395304-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	17:21:43.397969-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:videoeffects/com-nexy-assistant/centerstage-controlmode newValue: (null)
default	17:21:43.398236-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:videoeffects/com-nexy-assistant/centerstage-enabled newValue: (null)
default	17:21:43.398446-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:videoeffects/com-nexy-assistant/centerstage-unavailablereasons newValue: (null)
default	17:21:43.398771-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:videoeffects/com-nexy-assistant/portraiteffect-controlmode newValue: (null)
default	17:21:43.399051-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:videoeffects/com-nexy-assistant/portraiteffect-enabled newValue: (null)
default	17:21:43.399193-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:videoeffects/com-nexy-assistant/portraiteffect-unavailablereasons newValue: (null)
default	17:21:43.399379-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:videoeffects/com-nexy-assistant/portraiteffect-aperture newValue: (null)
default	17:21:43.399527-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:videoeffects/com-nexy-assistant/studiolighting-controlmode newValue: (null)
default	17:21:43.399698-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:videoeffects/com-nexy-assistant/studiolighting-enabled newValue: (null)
default	17:21:43.399939-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:videoeffects/com-nexy-assistant/studiolighting-unavailablereasons newValue: (null)
default	17:21:43.400150-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:videoeffects/com-nexy-assistant/studiolighting-intensity newValue: (null)
default	17:21:43.400312-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:videoeffects/com-nexy-assistant/reactions-enabled newValue: 1
default	17:21:43.400435-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:videoeffects/com-nexy-assistant/gestures-enabled newValue: (null)
default	17:21:43.400810-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:videoeffects/com-nexy-assistant/background-replacement-enabled newValue: (null)
default	17:21:43.400959-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:videoeffects/com-nexy-assistant/background-replacement-unavailablereasons newValue: 0
default	17:21:43.401109-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:videoeffects/com-nexy-assistant/background-replacement-url-bookmark newValue: (null)
default	17:21:43.401293-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:global/videoeffects/ringlight-supported newValue: (null)
default	17:21:43.401730-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:global/videoeffects/ringlight-enabled newValue: (null)
default	17:21:43.401881-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:global/videoeffects/ringlight-active newValue: (null)
default	17:21:43.402072-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:global/videoeffects/ringlight-bias newValue: (null)
default	17:21:43.402148-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:global/videoeffects/ringlight-screennitsfloor newValue: (null)
default	17:21:43.402281-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:global/videoeffects/ringlight-width newValue: (null)
default	17:21:43.402426-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:global/videoeffects/ringlight-color newValue: (null)
default	17:21:43.402573-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:global/videoeffects/ringlight-autocolorenabled newValue: (null)
default	17:21:43.402717-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:global/videoeffects/ringlight-recommendedcolor newValue: (null)
default	17:21:43.402811-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:global/videoeffects/ringlight-autosupported newValue: (null)
default	17:21:43.402947-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:global/videoeffects/ringlight-mode newValue: (null)
default	17:21:43.403017-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:global/videoeffects/ringlight-onboarding-state newValue: (null)
default	17:21:43.403158-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:global/videoeffects/ringlight-onboarding-strikecount newValue: (null)
default	17:21:43.403297-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:global/videoeffects/ringlight-onboarding-previoustiptimestamp newValue: (null)
default	17:21:43.403512-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOBypassVoiceProcessing newValue: (null)
default	17:21:43.403716-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOChatFlavor newValue: (null)
default	17:21:43.403835-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOActiveChatFlavor newValue: (null)
default	17:21:43.404001-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOSupportedChatFlavors newValue: (
    0,
    2
)
default	17:21:43.404136-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOHiddenChatFlavors newValue: (
    1
)
default	17:21:43.404258-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOIsAutoChatFlavorEnabled newValue: (null)
default	17:21:43.404350-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	17:21:43.404361-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	17:21:43.404373-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	17:21:43.404381-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	17:21:43.404453-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	17:21:43.404485-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	17:21:43.404493-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	17:21:43.404500-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	17:21:43.404508-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	17:21:43.404515-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	17:21:43.404520-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	17:21:43.404611-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	17:21:43.404637-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	17:21:43.404654-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	17:21:43.404676-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	17:21:43.404716-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	17:21:43.404753-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	17:21:43.404778-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	17:21:43.404907-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	17:21:43.421591-0500	runningboardd	[app<application.com.nexy.assistant.54878181.54878190(501)>:21340] Ignoring jetsam update because this process is not memory-managed
default	17:21:43.421605-0500	runningboardd	[app<application.com.nexy.assistant.54878181.54878190(501)>:21340] Ignoring suspend because this process is not lifecycle managed
default	17:21:43.421616-0500	runningboardd	[app<application.com.nexy.assistant.54878181.54878190(501)>:21340] Ignoring GPU update because this process is not GPU managed
default	17:21:43.421633-0500	runningboardd	[app<application.com.nexy.assistant.54878181.54878190(501)>:21340] Ignoring memory limit update because this process is not memory-managed
default	17:21:43.424582-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.54878181.54878190(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	17:21:43.425008-0500	gamepolicyd	Received state update for 21340 (app<application.com.nexy.assistant.54878181.54878190(501)>, running-active-NotVisible
default	17:21:43.485269-0500	Nexy	                AUHAL.cpp:473   ~AUHAL: (0x82f29b140) Selecting device 0 from destructor
default	17:21:43.485277-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0x82f29b140)
default	17:21:43.485285-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0x82f29b140) not already running
default	17:21:43.485290-0500	Nexy	                AUHAL.cpp:687   SelectDevice: (0x82f29b140) disconnecting device 78
default	17:21:43.485296-0500	Nexy	                AUHAL.cpp:751   SelectDevice: (0x82f29b140) destroying ioproc 0xa for device 78
default	17:21:43.485313-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {BuiltInMicrophoneDevice, 0xa}
default	17:21:43.485337-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	17:21:43.485455-0500	Nexy	                AUHAL.cpp:853   SelectDevice: (0x82f29b140) nothing to setup
default	17:21:43.485469-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x82f29b140) adding 0 device listeners to device 0
default	17:21:43.485476-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x82f29b140) adding 0 device delegate listeners to device 0
default	17:21:43.485481-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x82f29b140) removing 7 device listeners from device 78
default	17:21:43.485712-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x82f29b140) removing 0 device delegate listeners from device 78
default	17:21:43.485726-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0x82f29b140)
default	17:21:45.319545-0500	runningboardd	Assertion did invalidate due to timeout: 400-400-16844 (target:[app<application.com.nexy.assistant.54878181.54878190(501)>:21340])
default	17:21:45.519953-0500	runningboardd	[app<application.com.nexy.assistant.54878181.54878190(501)>:21340] Ignoring jetsam update because this process is not memory-managed
default	17:21:45.519979-0500	runningboardd	[app<application.com.nexy.assistant.54878181.54878190(501)>:21340] Ignoring suspend because this process is not lifecycle managed
default	17:21:45.519995-0500	runningboardd	[app<application.com.nexy.assistant.54878181.54878190(501)>:21340] Ignoring GPU update because this process is not GPU managed
default	17:21:45.520020-0500	runningboardd	[app<application.com.nexy.assistant.54878181.54878190(501)>:21340] Ignoring memory limit update because this process is not memory-managed
default	17:21:45.523849-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.54878181.54878190(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	17:21:45.524321-0500	gamepolicyd	Received state update for 21340 (app<application.com.nexy.assistant.54878181.54878190(501)>, running-active-NotVisible
default	17:21:49.999274-0500	Nexy	NotifyToken::RegisterDispatch(user.uid.501.com.apple.LaunchServices.database) fired for session key <private>
default	17:21:50.947865-0500	Nexy	LSExceptions shared instance invalidated for timeout.
default	17:21:56.491115-0500	Nexy	                AUHAL.cpp:420   AUHAL: (0x82f29b140) Selecting device 71 from constructor
default	17:21:56.491157-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0x82f29b140)
default	17:21:56.491174-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0x82f29b140) not already running
default	17:21:56.491192-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0x82f29b140) nothing to teardown
default	17:21:56.491203-0500	Nexy	                AUHAL.cpp:762   SelectDevice: (0x82f29b140) connecting device 71
default	17:21:56.491519-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0x82f29b140) Device ID: 71 (Input:No | Output:Yes): true
default	17:21:56.491990-0500	Nexy	                AUHAL.cpp:774   SelectDevice: (0x82f29b140) created ioproc 0xb for device 71
default	17:21:56.492327-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x82f29b140) adding 7 device listeners to device 71
default	17:21:56.492866-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x82f29b140) adding 0 device delegate listeners to device 71
default	17:21:56.492893-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x82f29b140)
default	17:21:56.493104-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x48]:  2 ch,  48000 Hz, Float32, interleaved
default	17:21:56.493139-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	17:21:56.493158-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	17:21:56.493177-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	17:21:56.493200-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	17:21:56.493452-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x82f29b140) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	17:21:56.493480-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x82f29b140) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	17:21:56.493509-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	17:21:56.493525-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x82f29b140) removing 0 device listeners from device 0
default	17:21:56.493537-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x82f29b140) removing 0 device delegate listeners from device 0
default	17:21:56.493550-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0x82f29b140)
default	17:21:56.493582-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is DISABLED
default	17:21:56.493750-0500	Nexy	                AUHAL.cpp:2303  SetProperty: (0x82f29b140) caller requesting device change from 71 to 78
default	17:21:56.493774-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0x82f29b140)
default	17:21:56.493788-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0x82f29b140) not already running
default	17:21:56.493802-0500	Nexy	                AUHAL.cpp:687   SelectDevice: (0x82f29b140) disconnecting device 71
default	17:21:56.493813-0500	Nexy	                AUHAL.cpp:751   SelectDevice: (0x82f29b140) destroying ioproc 0xb for device 71
default	17:21:56.493916-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped Unknown {BuiltInSpeakerDevice, 0xb}
default	17:21:56.494039-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	17:21:56.494230-0500	Nexy	                AUHAL.cpp:762   SelectDevice: (0x82f29b140) connecting device 78
default	17:21:56.494441-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0x82f29b140) Device ID: 78 (Input:Yes | Output:No): true
default	17:21:56.497648-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.961, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=21340, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=392, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	17:21:56.501929-0500	tccd	AUTHREQ_SUBJECT: msgID=401.961, subject=com.nexy.assistant,
default	17:21:56.503283-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x722e70300 at /Applications/Nexy.app
default	17:21:56.530069-0500	Nexy	                AUHAL.cpp:774   SelectDevice: (0x82f29b140) created ioproc 0xb for device 78
default	17:21:56.530237-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x82f29b140) adding 7 device listeners to device 78
default	17:21:56.530471-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x82f29b140) adding 0 device delegate listeners to device 78
default	17:21:56.530479-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x82f29b140)
default	17:21:56.530491-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 output streams; not all mono
default	17:21:56.530502-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	17:21:56.530663-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  input stream 0 [0x4f]:  1 ch,  44100 Hz, Float32
default	17:21:56.530670-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 input streams; all mono
default	17:21:56.530675-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  1 ch,  44100 Hz, Float32
default	17:21:56.530766-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x82f29b140) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	17:21:56.530782-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x82f29b140) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	17:21:56.530788-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	17:21:56.530793-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x82f29b140) removing 7 device listeners from device 71
default	17:21:56.530976-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x82f29b140) removing 0 device delegate listeners from device 71
default	17:21:56.530983-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0x82f29b140)
default	17:21:56.530993-0500	Nexy	AudioHardware-mac-imp.cpp:1306   AudioObjectAddPropertyListener: listener was already added
default	17:21:56.531702-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	17:21:56.532949-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.962, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=21340, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=392, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	17:21:56.534226-0500	tccd	AUTHREQ_SUBJECT: msgID=401.962, subject=com.nexy.assistant,
default	17:21:56.534903-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x722e70300 at /Applications/Nexy.app
default	17:21:56.549501-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0x82ba454d0, from  1 ch,  44100 Hz, Float32 to  1 ch,  16000 Hz, Float32
default	17:21:56.549752-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	17:21:56.550590-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.963, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=21340, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=392, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	17:21:56.551448-0500	tccd	AUTHREQ_SUBJECT: msgID=401.963, subject=com.nexy.assistant,
default	17:21:56.551920-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x722e70300 at /Applications/Nexy.app
default	17:21:56.563759-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.964, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=21340, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=392, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	17:21:56.564369-0500	tccd	AUTHREQ_SUBJECT: msgID=401.964, subject=com.nexy.assistant,
default	17:21:56.564743-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x722e70300 at /Applications/Nexy.app
default	17:21:56.575879-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.54878181.54878190(501)>:21340] from originator [osservice<com.apple.powerd>:332] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:400-332-16855 target:21340 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	17:21:56.575998-0500	runningboardd	Assertion 400-332-16855 (target:[app<application.com.nexy.assistant.54878181.54878190(501)>:21340]) will be created as active
default	17:21:56.576450-0500	runningboardd	[app<application.com.nexy.assistant.54878181.54878190(501)>:21340] Ignoring jetsam update because this process is not memory-managed
default	17:21:56.576467-0500	runningboardd	[app<application.com.nexy.assistant.54878181.54878190(501)>:21340] Ignoring suspend because this process is not lifecycle managed
default	17:21:56.576483-0500	runningboardd	[app<application.com.nexy.assistant.54878181.54878190(501)>:21340] Ignoring GPU update because this process is not GPU managed
default	17:21:56.576514-0500	runningboardd	[app<application.com.nexy.assistant.54878181.54878190(501)>:21340] Ignoring memory limit update because this process is not memory-managed
default	17:21:56.581859-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.54878181.54878190(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	17:21:56.582447-0500	gamepolicyd	Received state update for 21340 (app<application.com.nexy.assistant.54878181.54878190(501)>, running-active-NotVisible
default	17:21:56.600713-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Input {BuiltInMicrophoneDevice, 0xb}
default	17:21:56.601186-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1f4029","name":"Nexy(21340)"}, "details":{"deviceUIDs":[],"implicit_category":"Record","input_running":true,"output_running":false} }
default	17:21:56.601249-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 42, PID = 21340, Name = sid:0x1f4029, Nexy(21340), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	17:21:56.601270-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Category/Mode changed -- The score for sid:0x1f4029, Nexy(21340), 'prim'/com.nexy.assistant was not correct. Old score = 201
default	17:21:56.601289-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 42, PID = 21340, Name = sid:0x1f4029, Nexy(21340), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	17:21:56.601337-0500	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1f4029, Nexy(21340), 'prim'', AudioCategory changed to 'Record_WithBluetooth'
default	17:21:56.601363-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 42, PID = 21340, Name = sid:0x1f4029, Nexy(21340), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	17:21:56.601382-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 42, PID = 21340, Name = sid:0x1f4029, Nexy(21340), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	17:21:56.601381-0500	audiomxd	UpdateAudioState CID 0x91550001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	17:21:56.601509-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	17:21:56.601460-0500	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 42, PID = 21340, Name = sid:0x1f4029, Nexy(21340), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> is going active
default	17:21:56.601533-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	17:21:56.601473-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1f4029, Nexy(21340), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 42 starting recording
default	17:21:56.601483-0500	audiomxd	UpdateAudioState CID 0x91550001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	17:21:56.601561-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	17:21:56.601579-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	17:21:56.601666-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 42, PID = 21340, Name = sid:0x1f4029, Nexy(21340), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	17:21:56.601749-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 42, PID = 21340, Name = sid:0x1f4029, Nexy(21340), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	17:21:56.601830-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1f4029, Nexy(21340), 'prim'', displayID:'com.nexy.assistant'}
default	17:21:56.601881-0500	audiomxd	UpdateAudioState CID 0x91550001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	17:21:56.601897-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [1, 0]. BT device UIDS: {(
)}
default	17:21:56.601902-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	17:21:56.601939-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	17:21:56.601953-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	17:21:56.601960-0500	audioaccessoryd	AudioStateChanged: Added audio session app com.nexy.assistant NULL -> 200 count 1
default	17:21:56.601965-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
error	17:21:56.601970-0500	audioaccessoryd	Updating local audio category 100 -> 200 app com.nexy.assistant
default	17:21:56.601991-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	17:21:56.608093-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	17:21:56.608167-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	17:21:56.608217-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	17:21:56.609049-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	17:21:56.609066-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	17:21:56.609082-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	17:21:56.609092-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	17:21:56.609102-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	17:21:56.609112-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	17:21:56.609128-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	17:21:56.609146-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	17:21:56.609158-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	17:21:56.609168-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	17:21:56.609177-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	17:21:56.609246-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	17:21:56.609441-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	17:21:56.610610-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	17:21:56.610625-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	17:21:56.610639-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	17:21:56.610646-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	17:21:56.610663-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	17:21:56.610672-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	17:21:56.610721-0500	ControlCenter	Navigating to new application [com.nexy.assistant]
default	17:21:56.704801-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {BuiltInMicrophoneDevice, 0xb}
default	17:21:56.704992-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1f4029","name":"Nexy(21340)"}, "details":{"deviceUIDs":[],"implicit_category":"","input_running":false,"output_running":false} }
default	17:21:56.705105-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 42, PID = 21340, Name = sid:0x1f4029, Nexy(21340), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	17:21:56.705158-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 42, PID = 21340, Name = sid:0x1f4029, Nexy(21340), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	17:21:56.705190-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1f4029, Nexy(21340), 'prim'', displayID:'com.nexy.assistant'}
default	17:21:56.705246-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1f4029, Nexy(21340), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 42 stopping recording
default	17:21:56.705250-0500	audiomxd	UpdateAudioState CID 0x91550001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	17:21:56.705271-0500	audiomxd	-MXCoreSession- -[MXCoreSession endInterruption:]: Session <ID: 42, PID = 21340, Name = sid:0x1f4029, Nexy(21340), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> is going inactive
default	17:21:56.705298-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 42, PID = 21340, Name = sid:0x1f4029, Nexy(21340), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	17:21:56.705332-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 42, PID = 21340, Name = sid:0x1f4029, Nexy(21340), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	17:21:56.705391-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	17:21:56.705430-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 0]. BT device UIDS: {(
)}
default	17:21:56.705439-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	17:21:56.705447-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	17:21:56.705467-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	17:21:56.705482-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	17:21:56.705538-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	17:21:56.705562-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	17:21:56.705574-0500	audioaccessoryd	AudioStateChanged: Removed audio session app com.nexy.assistant 201 count 0
default	17:21:56.705382-0500	audiomxd	UpdateAudioState CID 0x91550001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	17:21:56.710500-0500	runningboardd	Invalidating assertion 400-332-16855 (target:[app<application.com.nexy.assistant.54878181.54878190(501)>:21340]) from originator [osservice<com.apple.powerd>:332]
default	17:21:56.711484-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	17:21:56.713641-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	17:21:56.713661-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	17:21:56.713680-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	17:21:56.713694-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	17:21:56.713706-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	17:21:56.713718-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	17:21:56.713905-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	17:21:56.806052-0500	Nexy	                AUHAL.cpp:473   ~AUHAL: (0x82f29b140) Selecting device 0 from destructor
default	17:21:56.806072-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0x82f29b140)
default	17:21:56.806082-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0x82f29b140) not already running
default	17:21:56.806090-0500	Nexy	                AUHAL.cpp:687   SelectDevice: (0x82f29b140) disconnecting device 78
default	17:21:56.806098-0500	Nexy	                AUHAL.cpp:751   SelectDevice: (0x82f29b140) destroying ioproc 0xb for device 78
default	17:21:56.806144-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {BuiltInMicrophoneDevice, 0xb}
default	17:21:56.806191-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	17:21:56.806413-0500	Nexy	                AUHAL.cpp:853   SelectDevice: (0x82f29b140) nothing to setup
default	17:21:56.806430-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x82f29b140) adding 0 device listeners to device 0
default	17:21:56.806437-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x82f29b140) adding 0 device delegate listeners to device 0
default	17:21:56.806446-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x82f29b140) removing 7 device listeners from device 78
default	17:21:56.806750-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x82f29b140) removing 0 device delegate listeners from device 78
default	17:21:56.806771-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0x82f29b140)
default	17:21:56.811734-0500	runningboardd	[app<application.com.nexy.assistant.54878181.54878190(501)>:21340] Ignoring jetsam update because this process is not memory-managed
default	17:21:56.811752-0500	runningboardd	[app<application.com.nexy.assistant.54878181.54878190(501)>:21340] Ignoring suspend because this process is not lifecycle managed
default	17:21:56.811768-0500	runningboardd	[app<application.com.nexy.assistant.54878181.54878190(501)>:21340] Ignoring GPU update because this process is not GPU managed
default	17:21:56.811790-0500	runningboardd	[app<application.com.nexy.assistant.54878181.54878190(501)>:21340] Ignoring memory limit update because this process is not memory-managed
default	17:21:56.815916-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.54878181.54878190(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	17:21:56.816582-0500	gamepolicyd	Received state update for 21340 (app<application.com.nexy.assistant.54878181.54878190(501)>, running-active-NotVisible
default	17:21:59.815433-0500	Nexy	[0x82cb15680] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	17:21:59.816656-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=21340.3, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=21340, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	17:21:59.818645-0500	tccd	AUTHREQ_SUBJECT: msgID=21340.3, subject=com.nexy.assistant,
default	17:21:59.819694-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b5164f00 at /Applications/Nexy.app
default	17:21:59.841635-0500	tccd	Notifying for access  kTCCServiceScreenCapture for target PID[21340], responsiblePID[21340], responsiblePath: /Applications/Nexy.app to UID: 501
default	17:21:59.842130-0500	Nexy	[0x82cb15680] invalidated after the last release of the connection object
default	17:22:00.068578-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b5164600 at /Applications/Nexy.app
default	17:22:00.083940-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b5167600 at /Applications/Nexy.app
default	17:22:00.084192-0500	nehelper	Received an apps uninstalled notification with bundle IDs (
    "com.nexy.assistant"
)
default	17:22:00.086298-0500	tccd	Publishing <TCCDEvent: type=Modify, service=kTCCServiceScreenCapture, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 0 subscribers: {
}
default	17:22:00.677840-0500	nehelper	Removing UUIDs for (
    "com.nexy.assistant"
)
default	17:22:00.682796-0500	nehelper	Handling an apps uninstalled notification with bundle IDs (
    "com.nexy.assistant"
)
default	17:22:00.705390-0500	nehelper	com.apple.preferences.networkprivacy-F67B3EA9-90A6-470B-B321-9BBD719C692B: Populating the cache with 2 UUID(s) for com.nexy.assistant
error	17:22:02.481281-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceScreenCapture com.nexy.assistant none
error	17:22:02.483937-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceScreenCapture com.nexy.assistant none
error	17:22:02.548994-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceMicrophone com.nexy.assistant full
default	17:22:08.232302-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b5165b00 at /Applications/Nexy.app
default	17:22:08.246438-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b5164900 at /Applications/Nexy.app
default	17:22:08.252372-0500	tccd	Publishing <TCCDEvent: type=Modify, service=kTCCServiceScreenCapture, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 0 subscribers: {
}
error	17:22:08.340778-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceScreenCapture com.nexy.assistant full
error	17:22:08.344800-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceScreenCapture com.nexy.assistant full
error	17:22:08.366417-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceMicrophone com.nexy.assistant full
error	17:22:08.372241-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceMicrophone com.nexy.assistant full
error	17:22:11.063620-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceScreenCapture com.nexy.assistant full
error	17:22:11.067131-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceScreenCapture com.nexy.assistant full
error	17:22:11.086034-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceMicrophone com.nexy.assistant full
error	17:22:11.088532-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceMicrophone com.nexy.assistant full
default	17:22:12.850236-0500	Nexy	[0x82cb15540] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	17:22:12.852097-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=21340.4, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=21340, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	17:22:12.855012-0500	tccd	AUTHREQ_SUBJECT: msgID=21340.4, subject=com.nexy.assistant,
default	17:22:12.857127-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b5165800 at /Applications/Nexy.app
default	17:22:12.886773-0500	Nexy	[0x82cb15540] invalidated after the last release of the connection object
default	17:22:12.888963-0500	Nexy	 [INFO] SLSWindowListCreateImageProxying:84 request: <private>
default	17:22:12.891313-0500	Nexy	[0x82cb15540] activating connection: mach=true listener=false peer=false name=com.apple.replayd
default	17:22:12.891453-0500	Nexy	 [INFO] -[RPDaemonProxy consumeSandboxExtension:processNewConnection:]:568
default	17:22:12.891541-0500	Nexy	 [INFO] -[RPDaemonProxy proxyCoreGraphicsWithMethodType:config:machPort:completionHandler:]:1493
default	17:22:12.899449-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=21333.2, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=21340, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.replayd, pid=21333, auid=501, euid=501, binary_path=/usr/libexec/replayd}, },
default	17:22:12.899472-0500	tccd	requestor: TCCDProcess: identifier=com.apple.replayd, pid=21333, auid=501, euid=501, binary_path=/usr/libexec/replayd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=21340, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	17:22:12.900393-0500	tccd	AUTHREQ_SUBJECT: msgID=21333.2, subject=com.nexy.assistant,
default	17:22:12.901024-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b5165800 at /Applications/Nexy.app
default	17:22:12.920103-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=391.837, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=21340, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=391, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	17:22:12.920120-0500	tccd	requestor: TCCDProcess: identifier=com.apple.WindowServer, pid=391, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=21340, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	17:22:12.920655-0500	tccd	AUTHREQ_SUBJECT: msgID=391.837, subject=com.nexy.assistant,
default	17:22:12.921071-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b5165800 at /Applications/Nexy.app
default	17:22:12.934511-0500	Nexy	 [INFO] SLSWindowListCreateImageProxying_block_invoke:116 request: <private>, error: (null), output: <private>
default	17:22:12.962675-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	17:22:12.962804-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant)]
default	17:22:12.962857-0500	ControlCenter	Active activity attributions changed to ["scr:com.nexy.assistant"]
default	17:22:12.964528-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	17:22:12.964543-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	17:22:12.964559-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	17:22:12.964567-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	17:22:12.964582-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	17:22:12.964591-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	17:22:12.964714-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	17:22:15.941812-0500	kernel	udp connect: [<IPv4-redacted>:59860<-><IPv4-redacted>:80] interface:  (skipped: 0)
so_gencnt: 5934221 so_state: 0x0102 process: Nexy:21340 bytes in/out: 0/0 pkts in/out: 0/0 error: 0 so_error: 0 svc/tc: 0 flow: 0x926b2333
default	17:22:15.942055-0500	kernel	udp_connection_summary [<IPv4-redacted>:59860<-><IPv4-redacted>:80] interface: en0 (skipped: 0)
so_gencnt: 5934221 so_state: 0x0102 process: Nexy:21340 Duration: 0.000 sec Conn_Time: 0.000 sec bytes in/out: 0/18 pkts in/out: 0/1 rxnospace pkts/bytes: 0/0 so_error: 0 svc/tc: 0 flow: 0x926b2333 flowctl: 0us (0x)
default	17:22:15.945183-0500	Nexy	networkd_settings_read_from_file initialized networkd settings by reading plist directly
default	17:22:15.945565-0500	Nexy	networkd_settings_read_from_file initialized networkd settings by reading plist directly
default	17:22:15.948043-0500	Nexy	nw_path_libinfo_path_check [ED28B698-3978-4AA3-B780-0CFD41746527 IPv4#80252384:53 tcp, legacy-socket, attribution: developer]
	libinfo check path: <private>
default	17:22:15.949687-0500	kernel	SK[1]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 084DA601-AAB7-44EC-A174-68D7DE87435E flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.55136,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0xc63b38df tp_proto=0x06"
default	17:22:15.949816-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:55136<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 5934222 t_state: SYN_SENT process: Nexy:21340 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 21 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xabce67a5
default	17:22:15.970921-0500	kernel	tcp connected: [<IPv4-redacted>:55136<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 5934222 t_state: ESTABLISHED process: Nexy:21340 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 21 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xabce67a5
default	17:22:15.971050-0500	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:55136<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 5934222 t_state: FIN_WAIT_1 process: Nexy:21340 Duration: 0.021 sec Conn_Time: 0.021 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 21.000 ms rttvar: 10.500 ms base rtt: 21 ms so_error: 0 svc/tc: 0 flow: 0xabce67a5
default	17:22:15.971069-0500	kernel	tcp_connection_summary [<IPv4-redacted>:55136<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 5934222 t_state: FIN_WAIT_1 process: Nexy:21340 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	17:22:15.971745-0500	kernel	tcp listen: [<IPv4-redacted>:55137<-><IPv4-redacted>:0] interface:  (skipped: 0)
so_gencnt: 5934223 t_state: LISTEN process: Nexy:21340 so_qlimit: 0 error: 0 so_error: 0 svc/tc: 0
default	17:22:15.971976-0500	kernel	tcp_connection_summary (tcp_close:1797)[<IPv4-redacted>:55137<-><IPv4-redacted>:0] interface:  (skipped: 0)
so_gencnt: 5934223 t_state: LISTEN process: Nexy:21340 Duration: 0.000 sec Conn_Time: 0.000 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 0.000 ms rttvar: 250.000 ms base rtt: 0 ms so_error: 0 svc/tc: 0 flow: 0x0
default	17:22:15.971997-0500	kernel	tcp_connection_summary [<IPv4-redacted>:55137<-><IPv4-redacted>:0] interface:  (skipped: 0)
so_gencnt: 5934223 t_state: LISTEN process: Nexy:21340 flowctl: 0us (0x) SYN in/out: 0/0 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	17:22:16.954567-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	17:22:16.954674-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant)]
default	17:22:19.024512-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	17:22:19.024616-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant)]
default	17:22:23.037077-0500	ControlCenter	Recent activity attributions changed to ["scr:com.nexy.assistant"]
default	17:22:28.978921-0500	Nexy	nw_path_libinfo_path_check [0C2043EB-6210-4A53-9FFA-767DFA26162E IPv4#80252384:53 tcp, legacy-socket, attribution: developer]
	libinfo check path: <private>
default	17:22:28.979619-0500	kernel	SK[3]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 6C2F6384-101E-45F0-B02F-9657AE5E4C7E flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.55138,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0x0979f86d tp_proto=0x06"
default	17:22:28.979768-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:55138<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 5934287 t_state: SYN_SENT process: Nexy:21340 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 21 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x87fba33c
default	17:22:29.000149-0500	kernel	tcp connected: [<IPv4-redacted>:55138<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 5934287 t_state: ESTABLISHED process: Nexy:21340 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 21 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x87fba33c
default	17:22:29.000238-0500	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:55138<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 5934287 t_state: FIN_WAIT_1 process: Nexy:21340 Duration: 0.020 sec Conn_Time: 0.020 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 20.000 ms rttvar: 10.000 ms base rtt: 20 ms so_error: 0 svc/tc: 0 flow: 0x87fba33c
default	17:22:29.000262-0500	kernel	tcp_connection_summary [<IPv4-redacted>:55138<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 5934287 t_state: FIN_WAIT_1 process: Nexy:21340 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	17:22:32.031965-0500	Nexy	[0x82cb15680] activating connection: mach=true listener=false peer=false name=com.apple.tccd
default	17:22:32.032532-0500	Nexy	[0x82cb157c0] activating connection: mach=true listener=false peer=false name=com.apple.tccd
default	17:22:32.032973-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=21340.5, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=21340, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	17:22:32.033004-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=21340.6, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=21340, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	17:22:32.034787-0500	tccd	AUTHREQ_SUBJECT: msgID=21340.6, subject=com.nexy.assistant,
default	17:22:32.034790-0500	tccd	AUTHREQ_SUBJECT: msgID=21340.5, subject=com.nexy.assistant,
default	17:22:32.035650-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x722e70600 at /Applications/Nexy.app
default	17:22:32.035696-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x722e70900 at /Applications/Nexy.app
default	17:22:32.052911-0500	Nexy	[0x82cb157c0] invalidated after the last release of the connection object
default	17:22:32.053090-0500	Nexy	Adding shared photo decorator (includeSharedPhotoContacts=YES)
default	17:22:32.054411-0500	Nexy	[0x82cb157c0] activating connection: mach=true listener=false peer=false name=com.apple.tccd
default	17:22:32.055006-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=21340.7, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=21340, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	17:22:32.056301-0500	tccd	AUTHREQ_SUBJECT: msgID=21340.7, subject=com.nexy.assistant,
default	17:22:32.056991-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x722e70900 at /Applications/Nexy.app
default	17:22:32.057629-0500	Nexy	[0x82cb15680] invalidated after the last release of the connection object
default	17:22:32.070875-0500	tccd	AUTHREQ_PROMPTING: msgID=21340.7, service=kTCCServiceAddressBook, subject=Sub:{com.nexy.assistant}Resp:{TCCDProcess: identifier=com.nexy.assistant, pid=21340, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy},
default	17:22:33.836437-0500	tccd	Publishing <TCCDEvent: type=Create, service=kTCCServiceAddressBook, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 3 subscribers: {
    39 = "<TCCDEventSubscriber: token=39, state=Passed, csid=com.apple.chronod>";
    38 = "<TCCDEventSubscriber: token=38, state=Initial, csid=(null)>";
    41 = "<TCCDEventSubscriber: token=41, state=Passed, csid=com.apple.photolibraryd>";
}
default	17:22:33.836973-0500	Nexy	[0x82cb157c0] invalidated after the last release of the connection object
default	17:22:33.837888-0500	chronod	[appAuth:com.nexy.assistant] tcc authorization(s) changed
default	17:22:33.840696-0500	Nexy	[0x82cb157c0] activating connection: mach=true listener=false peer=false name=com.apple.AddressBook.ContactsAccountsService
default	17:22:33.842300-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=53693.60, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=21340, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.sandboxd, pid=53693, auid=0, euid=0, binary_path=/usr/libexec/sandboxd}, },
default	17:22:33.845959-0500	tccd	AUTHREQ_SUBJECT: msgID=53693.60, subject=com.nexy.assistant,
default	17:22:33.847093-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x722e70900 at /Applications/Nexy.app
default	17:22:33.873394-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=53693.61, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=21340, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.sandboxd, pid=53693, auid=0, euid=0, binary_path=/usr/libexec/sandboxd}, },
default	17:22:33.874216-0500	tccd	AUTHREQ_SUBJECT: msgID=53693.61, subject=com.nexy.assistant,
default	17:22:33.874676-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x722e70900 at /Applications/Nexy.app
default	17:22:33.891428-0500	Nexy	[0x82cb15680] activating connection: mach=true listener=false peer=false name=com.apple.accountsd.accountmanager
fault	17:22:33.892894-0500	Nexy	Attempted to register account monitor for types client is not authorized to access: <private>
error	17:22:33.892941-0500	Nexy	<private> 0x82cb64800: Store registration failed: Error Domain=com.apple.accounts Code=7 "(null)"
error	17:22:33.892976-0500	Nexy	<private> 0x82cb64800: Update event received, but store registration failed. This event will be handled, but the behavior is undefined.
default	17:22:33.893898-0500	Nexy	Adding shared photo decorator (includeSharedPhotoContacts=YES)
default	17:22:33.907741-0500	Nexy	[0x82cb15900] activating connection: mach=true listener=false peer=false name=com.apple.AddressBook.ContactsAccountsService
default	17:22:33.908428-0500	Nexy	[0x82cb15900] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	17:22:33.908499-0500	Nexy	Will add prepared store without migration (path: file:///Users/sergiyzasorin/Library/Application%20Support/AddressBook/AddressBook-v22.abcddb)
default	17:22:33.908721-0500	Nexy	Will add XPC store with options: <private> <private>
default	17:22:33.911401-0500	Nexy	[0x82cd9c3c0] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	17:22:33.912355-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=53435.1457, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=21340, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=53435, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	17:22:33.912389-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=53435, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=21340, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	17:22:33.913847-0500	tccd	AUTHREQ_SUBJECT: msgID=53435.1457, subject=com.nexy.assistant,
default	17:22:33.914836-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x722e70600 at /Applications/Nexy.app
default	17:22:33.935020-0500	Nexy	[0x82cd9c3c0] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	17:22:33.935107-0500	Nexy	[0x82cd9c3c0] activating connection: mach=false listener=false peer=false name=(anonymous)
default	17:22:33.935192-0500	Nexy	[0x82cd9c500] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	17:22:33.935956-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=53435.1458, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=21340, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=53435, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	17:22:33.935995-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=53435, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=21340, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	17:22:33.937221-0500	tccd	AUTHREQ_SUBJECT: msgID=53435.1458, subject=com.nexy.assistant,
default	17:22:33.937992-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x722e70600 at /Applications/Nexy.app
default	17:22:33.961369-0500	Nexy	[0x82cd9c500] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	17:22:33.961451-0500	Nexy	[0x82cd9c500] activating connection: mach=false listener=false peer=false name=(anonymous)
default	17:22:33.961500-0500	Nexy	[0x82cd9c640] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	17:22:33.962407-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=53435.1459, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=21340, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=53435, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	17:22:33.962527-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=53435, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=21340, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	17:22:33.964051-0500	tccd	AUTHREQ_SUBJECT: msgID=53435.1459, subject=com.nexy.assistant,
default	17:22:33.964864-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x722e70600 at /Applications/Nexy.app
default	17:22:33.987205-0500	Nexy	[0x82cd9c640] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	17:22:33.987292-0500	Nexy	[0x82cd9c640] activating connection: mach=false listener=false peer=false name=(anonymous)
default	17:22:33.987346-0500	Nexy	[0x82cd9c780] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	17:22:33.989623-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=53435.1460, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=21340, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=53435, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	17:22:33.989655-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=53435, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=21340, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	17:22:33.991118-0500	tccd	AUTHREQ_SUBJECT: msgID=53435.1460, subject=com.nexy.assistant,
default	17:22:33.992050-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x722e70600 at /Applications/Nexy.app
default	17:22:34.016629-0500	Nexy	[0x82cd9c780] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	17:22:34.016683-0500	Nexy	[0x82cd9c780] activating connection: mach=false listener=false peer=false name=(anonymous)
default	17:22:34.030172-0500	Nexy	Did add XPC store
default	17:22:34.030185-0500	Nexy	Did add prepared store without migration (path: file:///Users/sergiyzasorin/Library/Application%20Support/AddressBook/AddressBook-v22.abcddb)
default	17:22:34.032274-0500	Nexy	0x82cb5c660: Using cached account information
default	17:22:34.033118-0500	Nexy	[0x82cb3b5c0] Session created.
default	17:22:34.033126-0500	Nexy	[0x82cb3b5c0] Session created with Mach Service: <private>
default	17:22:34.033134-0500	Nexy	[0x82cd9cdc0] activating connection: mach=true listener=false peer=false name=com.apple.contacts.account-caching
default	17:22:34.033241-0500	Nexy	[0x82cb3b5c0] Session activated
default	17:22:34.035116-0500	Nexy	[0x82cd9cdc0] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	17:22:34.035123-0500	Nexy	[0x82cb3b5c0] Session canceled.
default	17:22:34.035131-0500	Nexy	[0x82cb3b5c0] Disposing of session
default	17:22:34.035393-0500	Nexy	[0x82cd9cdc0] activating connection: mach=true listener=false peer=false name=com.apple.AddressBook.ContactsAccountsService
default	17:22:34.035849-0500	Nexy	[0x82cd9cdc0] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	17:22:34.035866-0500	Nexy	Will add prepared store without migration (path: file:///Users/sergiyzasorin/Library/Application%20Support/AddressBook/Sources/4437DACA-BE14-412E-B504-7A2DD2E9DC7D/AddressBook-v22.abcddb)
default	17:22:34.035881-0500	Nexy	Will add XPC store with options: <private> <private>
default	17:22:34.039727-0500	Nexy	[0x82cd9f840] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	17:22:34.040703-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=53435.1461, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=21340, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=53435, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	17:22:34.040740-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=53435, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=21340, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	17:22:34.042196-0500	tccd	AUTHREQ_SUBJECT: msgID=53435.1461, subject=com.nexy.assistant,
default	17:22:34.043081-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x722e70600 at /Applications/Nexy.app
default	17:22:34.070425-0500	Nexy	[0x82cd9f840] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	17:22:34.070483-0500	Nexy	[0x82cd9f840] activating connection: mach=false listener=false peer=false name=(anonymous)
default	17:22:34.070535-0500	Nexy	[0x82cd9f980] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	17:22:34.071414-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=53435.1462, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=21340, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=53435, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	17:22:34.071449-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=53435, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=21340, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	17:22:34.072886-0500	tccd	AUTHREQ_SUBJECT: msgID=53435.1462, subject=com.nexy.assistant,
default	17:22:34.073858-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x722e70600 at /Applications/Nexy.app
default	17:22:34.099363-0500	Nexy	[0x82cd9f980] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	17:22:34.099426-0500	Nexy	[0x82cd9f980] activating connection: mach=false listener=false peer=false name=(anonymous)
default	17:22:34.099483-0500	Nexy	[0x82cd9fac0] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	17:22:34.100548-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=53435.1463, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=21340, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=53435, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	17:22:34.100583-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=53435, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=21340, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	17:22:34.102030-0500	tccd	AUTHREQ_SUBJECT: msgID=53435.1463, subject=com.nexy.assistant,
default	17:22:34.102888-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x722e70600 at /Applications/Nexy.app
default	17:22:34.127388-0500	Nexy	[0x82cd9fac0] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	17:22:34.127479-0500	Nexy	[0x82cd9fac0] activating connection: mach=false listener=false peer=false name=(anonymous)
default	17:22:34.127547-0500	Nexy	[0x82cd9fc00] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	17:22:34.128613-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=53435.1464, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=21340, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=53435, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	17:22:34.128652-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=53435, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=21340, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	17:22:34.130146-0500	tccd	AUTHREQ_SUBJECT: msgID=53435.1464, subject=com.nexy.assistant,
default	17:22:34.130928-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x722e70600 at /Applications/Nexy.app
default	17:22:34.153049-0500	Nexy	[0x82cd9fc00] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	17:22:34.153112-0500	Nexy	[0x82cd9fc00] activating connection: mach=false listener=false peer=false name=(anonymous)
default	17:22:34.165282-0500	Nexy	Did add XPC store
default	17:22:34.165309-0500	Nexy	Did add prepared store without migration (path: file:///Users/sergiyzasorin/Library/Application%20Support/AddressBook/Sources/4437DACA-BE14-412E-B504-7A2DD2E9DC7D/AddressBook-v22.abcddb)
default	17:22:34.165421-0500	Nexy	[0x82cd9fe80] activating connection: mach=true listener=false peer=false name=com.apple.AddressBook.ContactsAccountsService
default	17:22:34.165915-0500	Nexy	[0x82cd9fe80] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	17:22:34.165930-0500	Nexy	Will add prepared store without migration (path: file:///Users/sergiyzasorin/Library/Application%20Support/AddressBook/AddressBook-v22.abcddb)
default	17:22:34.165946-0500	Nexy	Will add XPC store with options: <private> <private>
default	17:22:34.169528-0500	Nexy	[0x82cdd6940] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	17:22:34.170433-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=53435.1465, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=21340, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=53435, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	17:22:34.170466-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=53435, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=21340, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	17:22:34.171844-0500	tccd	AUTHREQ_SUBJECT: msgID=53435.1465, subject=com.nexy.assistant,
default	17:22:34.172552-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x722e70600 at /Applications/Nexy.app
default	17:22:34.198317-0500	Nexy	[0x82cdd6940] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	17:22:34.198390-0500	Nexy	[0x82cdd6940] activating connection: mach=false listener=false peer=false name=(anonymous)
default	17:22:34.198447-0500	Nexy	[0x82cdd6a80] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	17:22:34.199368-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=53435.1466, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=21340, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=53435, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	17:22:34.199409-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=53435, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=21340, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	17:22:34.200668-0500	tccd	AUTHREQ_SUBJECT: msgID=53435.1466, subject=com.nexy.assistant,
default	17:22:34.201364-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x722e70600 at /Applications/Nexy.app
default	17:22:34.224451-0500	Nexy	[0x82cdd6a80] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	17:22:34.224531-0500	Nexy	[0x82cdd6a80] activating connection: mach=false listener=false peer=false name=(anonymous)
default	17:22:34.224598-0500	Nexy	[0x82cdd6bc0] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	17:22:34.225573-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=53435.1467, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=21340, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=53435, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	17:22:34.225606-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=53435, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=21340, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	17:22:34.226978-0500	tccd	AUTHREQ_SUBJECT: msgID=53435.1467, subject=com.nexy.assistant,
default	17:22:34.227722-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x722e70600 at /Applications/Nexy.app
default	17:22:34.252808-0500	Nexy	[0x82cdd6bc0] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	17:22:34.252932-0500	Nexy	[0x82cdd6bc0] activating connection: mach=false listener=false peer=false name=(anonymous)
default	17:22:34.253020-0500	Nexy	[0x82cdd6d00] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	17:22:34.254225-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=53435.1468, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=21340, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=53435, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	17:22:34.254265-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=53435, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=21340, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	17:22:34.256035-0500	tccd	AUTHREQ_SUBJECT: msgID=53435.1468, subject=com.nexy.assistant,
default	17:22:34.256933-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x722e70600 at /Applications/Nexy.app
default	17:22:34.289769-0500	Nexy	[0x82cdd6d00] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	17:22:34.289879-0500	Nexy	[0x82cdd6d00] activating connection: mach=false listener=false peer=false name=(anonymous)
default	17:22:34.291790-0500	Nexy	Did add XPC store
default	17:22:34.291836-0500	Nexy	Did add prepared store without migration (path: file:///Users/sergiyzasorin/Library/Application%20Support/AddressBook/AddressBook-v22.abcddb)
default	17:22:34.324263-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=53435.1469, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=21340, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=53435, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	17:22:34.324302-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=53435, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=21340, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	17:22:34.326190-0500	tccd	AUTHREQ_SUBJECT: msgID=53435.1469, subject=com.nexy.assistant,
default	17:22:34.327040-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x722e70600 at /Applications/Nexy.app
default	17:22:34.355328-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=53435.1470, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=21340, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=53435, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	17:22:34.355370-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=53435, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=21340, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	17:22:34.357085-0500	tccd	AUTHREQ_SUBJECT: msgID=53435.1470, subject=com.nexy.assistant,
default	17:22:34.357970-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x722e70600 at /Applications/Nexy.app
default	17:22:34.400330-0500	Nexy	"ACMonitoredAccountStore: Fetching accounts of account type com.apple.account.CardDAV..."
default	17:22:34.416832-0500	Nexy	"ACMonitoredAccountStore: Fetched Accounts"
default	17:22:34.416877-0500	Nexy	"ACMonitoredAccountStore: account was added: <private>"
error	17:22:34.416949-0500	Nexy	<private> 0x82cb64800: Update event received, but store registration failed. This event will be handled, but the behavior is undefined.
default	17:22:34.421632-0500	Nexy	Removing cached PSC for file:///Users/sergiyzasorin/Library/Application%20Support/AddressBook/ because accounts changed
default	17:22:34.421724-0500	Nexy	[0x82cd9c780] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	17:22:34.421737-0500	Nexy	[0x82cd9c640] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	17:22:34.421768-0500	Nexy	[0x82cd9c500] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	17:22:34.421782-0500	Nexy	[0x82cd9c3c0] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	17:22:36.654969-0500	Nexy	[0x82cdd70c0] activating connection: mach=true listener=false peer=false name=com.apple.system.opendirectoryd.api
default	17:22:48.418792-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=21393.1, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=21340, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.osascript, pid=21393, auid=501, euid=501, binary_path=/usr/bin/osascript}, },
default	17:22:48.420454-0500	tccd	AUTHREQ_SUBJECT: msgID=21393.1, subject=com.nexy.assistant,
default	17:22:48.421339-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b5165800 at /Applications/Nexy.app
default	17:22:48.439522-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=391.848, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=21340, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.osascript, pid=21393, auid=501, euid=501, binary_path=/usr/bin/osascript}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=391, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	17:22:48.440613-0500	tccd	AUTHREQ_SUBJECT: msgID=391.848, subject=com.nexy.assistant,
default	17:22:48.441438-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b5165800 at /Applications/Nexy.app
default	17:22:48.473721-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b5164900 at /Applications/Nexy.app
default	17:22:48.721191-0500	Messages	TCCAccessRequestIndirect: TCCAccessRequestIndirect with pid 21394: target_identity: {
    kTCCCodeIdentityAuditToken = {length = 32, bytes = 0xf5010000 f5010000 14000000 f5010000 ... b7860100 d3ba7900 };
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
default	17:22:48.729758-0500	tccd	target_executable_path_URL: file:///Applications/Nexy.app/Contents/MacOS/Nexy
default	17:22:48.736227-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x722e70900 at /Applications/Nexy.app
default	17:22:48.746817-0500	tccd	Prompting for access to indirect object Messages by Nexy
default	17:22:50.054142-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x722e70300 at /Applications/Nexy.app
default	17:22:50.060653-0500	tccd	Publishing <TCCDEvent: type=Create, service=kTCCServiceAppleEvents, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 3 subscribers: {
    39 = "<TCCDEventSubscriber: token=39, state=Passed, csid=com.apple.chronod>";
    38 = "<TCCDEventSubscriber: token=38, state=Initial, csid=(null)>";
    41 = "<TCCDEventSubscriber: token=41, state=Passed, csid=com.apple.photolibraryd>";
}
default	17:22:50.061151-0500	chronod	[appAuth:com.nexy.assistant] tcc authorization(s) changed
default	17:23:01.174909-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=21404.1, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=21340, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.osascript, pid=21404, auid=501, euid=501, binary_path=/usr/bin/osascript}, },
default	17:23:01.175896-0500	tccd	AUTHREQ_SUBJECT: msgID=21404.1, subject=com.nexy.assistant,
default	17:23:01.176331-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b5165800 at /Applications/Nexy.app
default	17:23:01.185607-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=391.851, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=21340, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.osascript, pid=21404, auid=501, euid=501, binary_path=/usr/bin/osascript}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=391, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	17:23:01.186048-0500	tccd	AUTHREQ_SUBJECT: msgID=391.851, subject=com.nexy.assistant,
default	17:23:01.186408-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b5165800 at /Applications/Nexy.app
default	17:23:01.214059-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b5164900 at /Applications/Nexy.app
default	17:23:01.236793-0500	Messages	TCCAccessRequestIndirect: TCCAccessRequestIndirect with pid 21394: target_identity: {
    kTCCCodeIdentityAuditToken = {length = 32, bytes = 0xf5010000 f5010000 14000000 f5010000 ... b7860100 f2ba7900 };
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
default	17:23:01.251169-0500	tccd	target_executable_path_URL: file:///Applications/Nexy.app/Contents/MacOS/Nexy
default	17:23:04.265008-0500	Nexy	[0x82cdd7200] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	17:23:04.267060-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=21340.8, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=21340, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	17:23:04.269515-0500	tccd	AUTHREQ_SUBJECT: msgID=21340.8, subject=com.nexy.assistant,
default	17:23:04.271164-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b5165800 at /Applications/Nexy.app
default	17:23:04.293908-0500	tccd	Notifying for access  kTCCServiceListenEvent for target PID[21340], responsiblePID[21340], responsiblePath: /Applications/Nexy.app to UID: 501
default	17:23:04.294373-0500	Nexy	[0x82cdd7200] invalidated after the last release of the connection object
default	17:23:04.336817-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b5165b00 at /Applications/Nexy.app
default	17:23:04.354748-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b5164900 at /Applications/Nexy.app
default	17:23:04.358027-0500	tccd	Publishing <TCCDEvent: type=Modify, service=kTCCServiceListenEvent, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 0 subscribers: {
}
default	17:23:06.031950-0500	Nexy	"ACMonitoredAccountStore: Fetching accounts of account type com.apple.account.CardDAV..."
default	17:23:06.044687-0500	Nexy	"ACMonitoredAccountStore: Fetched Accounts"
error	17:23:06.436167-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceScreenCapture com.nexy.assistant full
error	17:23:06.436331-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceListenEvent com.nexy.assistant none
error	17:23:06.437788-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceListenEvent com.nexy.assistant none
error	17:23:06.437920-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceScreenCapture com.nexy.assistant full
error	17:23:06.468362-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAddressBook com.nexy.assistant full
error	17:23:06.468399-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAddressBook com.nexy.assistant full
error	17:23:06.468792-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAppleEvents com.nexy.assistant full
error	17:23:06.468903-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAppleEvents com.nexy.assistant full
error	17:23:06.470536-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceMicrophone com.nexy.assistant full
error	17:23:06.470606-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceMicrophone com.nexy.assistant full
default	17:23:06.725156-0500	Nexy	"ACMonitoredAccountStore: Fetched Accounts"
default	17:23:10.296519-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b5165b00 at /Applications/Nexy.app
default	17:23:10.313801-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b5167600 at /Applications/Nexy.app
default	17:23:10.321110-0500	tccd	Publishing <TCCDEvent: type=Modify, service=kTCCServiceListenEvent, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 0 subscribers: {
}
error	17:23:10.407260-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceScreenCapture com.nexy.assistant full
error	17:23:10.407391-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceListenEvent com.nexy.assistant full
error	17:23:10.410331-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceListenEvent com.nexy.assistant full
error	17:23:10.410479-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceScreenCapture com.nexy.assistant full
error	17:23:10.430941-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAddressBook com.nexy.assistant full
error	17:23:10.431121-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAppleEvents com.nexy.assistant full
error	17:23:10.431863-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceMicrophone com.nexy.assistant full
error	17:23:10.434227-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAddressBook com.nexy.assistant full
error	17:23:10.434395-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAppleEvents com.nexy.assistant full
error	17:23:10.435060-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceMicrophone com.nexy.assistant full
default	17:23:17.303684-0500	Nexy	server port 0x00014e33, session port 0x0000370b
default	17:23:17.306317-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=391.869, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=21340, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=391, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	17:23:17.306391-0500	tccd	requestor: TCCDProcess: identifier=com.apple.WindowServer, pid=391, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=21340, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	17:23:17.310549-0500	tccd	AUTHREQ_SUBJECT: msgID=391.869, subject=com.nexy.assistant,
default	17:23:17.312000-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b5164600 at /Applications/Nexy.app
default	17:23:20.350474-0500	Nexy	[0x82cdd7200] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	17:23:20.351979-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=21340.9, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=21340, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	17:23:20.354370-0500	tccd	AUTHREQ_SUBJECT: msgID=21340.9, subject=com.nexy.assistant,
default	17:23:20.356014-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b5164600 at /Applications/Nexy.app
default	17:23:20.380822-0500	tccd	Notifying for access  kTCCServicePostEvent for target PID[21340], responsiblePID[21340], responsiblePath: /Applications/Nexy.app to UID: 501
default	17:23:20.381200-0500	Nexy	[0x82cdd7200] invalidated after the last release of the connection object
default	17:23:20.420653-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b5165b00 at /Applications/Nexy.app
default	17:23:20.440032-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b5167600 at /Applications/Nexy.app
default	17:23:20.443386-0500	tccd	Publishing <TCCDEvent: type=Modify, service=kTCCServicePostEvent, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 0 subscribers: {
}
default	17:23:25.749314-0500	Nexy	"ACMonitoredAccountStore: Fetching accounts of account type com.apple.account.CardDAV..."
default	17:23:25.768404-0500	Nexy	"ACMonitoredAccountStore: Fetched Accounts"
error	17:23:26.054796-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceListenEvent com.nexy.assistant full
error	17:23:26.057810-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceScreenCapture com.nexy.assistant full
error	17:23:26.058265-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAccessibility com.nexy.assistant none
error	17:23:26.062134-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceScreenCapture com.nexy.assistant full
error	17:23:26.124162-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAddressBook com.nexy.assistant full
error	17:23:26.127115-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceMicrophone com.nexy.assistant full
default	17:23:29.234463-0500	Nexy	"ACMonitoredAccountStore: Fetching accounts of account type com.apple.account.CardDAV..."
default	17:23:29.288805-0500	Nexy	"ACMonitoredAccountStore: Fetched Accounts"
default	17:23:29.328815-0500	Nexy	"ACMonitoredAccountStore: Fetching accounts of account type com.apple.account.CardDAV..."
default	17:23:29.394404-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b5164600 at /Applications/Nexy.app
default	17:23:29.425120-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b5165b00 at /Applications/Nexy.app
default	17:23:29.347898-0500	Nexy	"ACMonitoredAccountStore: Fetched Accounts"
default	17:23:29.456238-0500	tccd	Publishing <TCCDEvent: type=Modify, service=kTCCServiceAccessibility, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 0 subscribers: {
}
default	17:23:29.488277-0500	Nexy	"ACMonitoredAccountStore: Fetching accounts of account type com.apple.account.CardDAV..."
error	17:23:29.540739-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAccessibility com.nexy.assistant full
error	17:23:29.541285-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceListenEvent com.nexy.assistant full
error	17:23:29.543054-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceScreenCapture com.nexy.assistant full
error	17:23:29.545450-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAccessibility com.nexy.assistant full
error	17:23:29.548933-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAccessibility com.nexy.assistant full
error	17:23:29.557898-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceListenEvent com.nexy.assistant full
error	17:23:29.558371-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceScreenCapture com.nexy.assistant full
error	17:23:29.559665-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAccessibility com.nexy.assistant full
default	17:23:29.548778-0500	Nexy	"ACMonitoredAccountStore: Fetched Accounts"
error	17:23:29.612505-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAddressBook com.nexy.assistant full
error	17:23:29.613285-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAppleEvents com.nexy.assistant full
error	17:23:29.614295-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAddressBook com.nexy.assistant full
error	17:23:29.615329-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAppleEvents com.nexy.assistant full
error	17:23:29.616144-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceMicrophone com.nexy.assistant full
error	17:23:29.617347-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceMicrophone com.nexy.assistant full
default	17:23:33.456044-0500	Nexy	[0x82cdd7340] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
error	17:23:33.456495-0500	tccd	TCCDProcess: identifier=com.nexy.assistant, pid=21340, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy attempted to call TCCAccessRequest for kTCCServiceAccessibility without the recommended com.apple.private.tcc.manager.check-by-audit-token entitlement
default	17:23:33.456626-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=21340.10, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=21340, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.nexy.assistant, pid=21340, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	17:23:33.457416-0500	tccd	AUTHREQ_SUBJECT: msgID=21340.10, subject=com.nexy.assistant,
default	17:23:33.458126-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b5167600 at /Applications/Nexy.app
default	17:23:33.470527-0500	Nexy	[0x82cdd7340] invalidated after the last release of the connection object
default	17:23:36.475413-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=53693.63, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=21340, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.sandboxd, pid=53693, auid=0, euid=0, binary_path=/usr/libexec/sandboxd}, },
default	17:23:36.483397-0500	tccd	AUTHREQ_SUBJECT: msgID=53693.63, subject=com.nexy.assistant,
default	17:23:36.484256-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b5165b00 at /Applications/Nexy.app
default	17:23:36.505899-0500	tccd	Publishing <TCCDEvent: type=Create, service=kTCCServiceSystemPolicyAllFiles, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 0 subscribers: {
}
default	17:23:36.571144-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b5165b00 at /Applications/Nexy.app
default	17:23:36.996258-0500	Nexy	"ACMonitoredAccountStore: Fetched Accounts"
default	17:23:37.359088-0500	Nexy	"ACMonitoredAccountStore: Fetching accounts of account type com.apple.account.CardDAV..."
error	17:23:37.445892-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAccessibility com.nexy.assistant full
error	17:23:37.447156-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceListenEvent com.nexy.assistant full
error	17:23:37.448411-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceScreenCapture com.nexy.assistant full
error	17:23:37.448820-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAccessibility com.nexy.assistant full
error	17:23:37.449286-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceScreenCapture com.nexy.assistant full
error	17:23:37.449847-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceSystemPolicyAllFiles com.nexy.assistant none
error	17:23:37.450300-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceSystemPolicyAllFiles com.nexy.assistant none
error	17:23:37.450470-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAccessibility com.nexy.assistant full
error	17:23:37.450602-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceListenEvent com.nexy.assistant full
error	17:23:37.450943-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAccessibility com.nexy.assistant full
default	17:23:37.449142-0500	Nexy	"ACMonitoredAccountStore: Fetched Accounts"
error	17:23:37.507935-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAddressBook com.nexy.assistant full
error	17:23:37.508693-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAppleEvents com.nexy.assistant full
error	17:23:37.508802-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAddressBook com.nexy.assistant full
error	17:23:37.510159-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAppleEvents com.nexy.assistant full
error	17:23:37.512316-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceMicrophone com.nexy.assistant full
error	17:23:37.513071-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceMicrophone com.nexy.assistant full
default	17:23:40.936868-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b5167000 at /Applications/Nexy.app
default	17:23:40.966404-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b5167600 at /Applications/Nexy.app
default	17:23:40.971853-0500	tccd	Publishing <TCCDEvent: type=Modify, service=kTCCServiceSystemPolicyAllFiles, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 0 subscribers: {
}
error	17:23:41.058429-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAccessibility com.nexy.assistant full
error	17:23:41.058572-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceListenEvent com.nexy.assistant full
error	17:23:41.058692-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceScreenCapture com.nexy.assistant full
error	17:23:41.059279-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceSystemPolicyAllFiles com.nexy.assistant full
error	17:23:41.059386-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAccessibility com.nexy.assistant full
error	17:23:41.060188-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAccessibility com.nexy.assistant full
error	17:23:41.060355-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceScreenCapture com.nexy.assistant full
error	17:23:41.060605-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceSystemPolicyAllFiles com.nexy.assistant full
error	17:23:41.060734-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceListenEvent com.nexy.assistant full
error	17:23:41.060802-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAccessibility com.nexy.assistant full
error	17:23:41.081552-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAddressBook com.nexy.assistant full
error	17:23:41.081763-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAppleEvents com.nexy.assistant full
error	17:23:41.082545-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceMicrophone com.nexy.assistant full
error	17:23:41.088695-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAddressBook com.nexy.assistant full
error	17:23:41.088860-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAppleEvents com.nexy.assistant full
error	17:23:41.089648-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceMicrophone com.nexy.assistant full
default	17:23:49.621423-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=53693.64, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=21340, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.sandboxd, pid=53693, auid=0, euid=0, binary_path=/usr/libexec/sandboxd}, },
default	17:23:49.624406-0500	tccd	AUTHREQ_SUBJECT: msgID=53693.64, subject=com.nexy.assistant,
default	17:23:49.626880-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b5165200 at /Applications/Nexy.app
default	17:23:52.670939-0500	Nexy	  AVAudioSession_MacOS.mm:507   Setting category: AVAudioSessionCategoryPlayback, requires reconfiguration?: NO
default	17:23:52.671053-0500	Nexy	  AVAudioSession_MacOS.mm:883   Activating session
default	17:23:52.671736-0500	Nexy	       AggregateDevice.mm:887   Creating DefaultDeviceAggregate
default	17:23:52.672511-0500	Nexy	       AggregateDevice.mm:914   fetched default output device, ID = 71
default	17:23:52.672594-0500	Nexy	       AggregateDevice.mm:914   fetched default input device, ID = 78
default	17:23:52.695538-0500	Nexy	       AggregateDevice.mm:688   Built valid aggregate 110
default	17:23:52.701116-0500	Nexy	[0x82cdd7200] activating connection: mach=true listener=false peer=false name=com.apple.SystemConfiguration.DNSConfiguration
default	17:23:52.703895-0500	Nexy	[0x82cdd7200] invalidated after the last release of the connection object
default	17:23:52.706518-0500	kernel	udp connect: [<IPv6-redacted>:62662<-><IPv6-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 5934847 so_state: 0x0102 process: Nexy:21340 bytes in/out: 0/0 pkts in/out: 0/0 error: 0 so_error: 0 svc/tc: 0 flow: 0xad668470
default	17:23:52.718796-0500	Nexy	                AUHAL.cpp:420   AUHAL: (0x82f29b840) Selecting device 71 from constructor
default	17:23:52.718810-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0x82f29b840)
default	17:23:52.718817-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0x82f29b840) not already running
default	17:23:52.718822-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0x82f29b840) nothing to teardown
default	17:23:52.718827-0500	Nexy	                AUHAL.cpp:762   SelectDevice: (0x82f29b840) connecting device 71
default	17:23:52.718941-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0x82f29b840) Device ID: 71 (Input:No | Output:Yes): true
default	17:23:52.719084-0500	Nexy	                AUHAL.cpp:774   SelectDevice: (0x82f29b840) created ioproc 0xc for device 71
default	17:23:52.719202-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x82f29b840) adding 7 device listeners to device 71
default	17:23:52.719417-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x82f29b840) adding 0 device delegate listeners to device 71
default	17:23:52.719429-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x82f29b840)
default	17:23:52.719507-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x48]:  2 ch,  48000 Hz, Float32, interleaved
default	17:23:52.719517-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	17:23:52.719523-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	17:23:52.719531-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	17:23:52.719538-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	17:23:52.719654-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x82f29b840) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	17:23:52.719671-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x82f29b840) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	17:23:52.719676-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	17:23:52.719679-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x82f29b840) removing 0 device listeners from device 0
default	17:23:52.719681-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x82f29b840) removing 0 device delegate listeners from device 0
default	17:23:52.719683-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0x82f29b840)
default	17:23:52.719741-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is DISABLED
default	17:23:52.720103-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	17:23:52.721484-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0x82ba47360, from  2 ch,  44100 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	17:23:52.721518-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	17:23:52.723773-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	17:23:52.724030-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	17:23:52.732822-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	17:23:52.733238-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	17:23:52.735137-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0x82ba47450, from  2 ch,  44100 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	17:23:52.735148-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	17:23:52.735435-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	17:23:52.735939-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0x82ba47450, from  2 ch,  48000 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	17:23:52.735945-0500	Nexy	       AudioConverter.cpp:1317  AudioConverter -> 0x82ba47450: The in-process GetProperty call returned 1886547824 for property 1886546285 with size 8.
default	17:23:52.735949-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	17:23:52.735949-0500	Nexy	AudioConverter -> 0x82ba47450: The in-process SetProperty call returned 1886547824 for property 1936876385 with size 4.
default	17:23:52.736006-0500	Nexy	AudioConverter -> 0x82ba47450: The in-process SetProperty call returned 1886547824 for property 1936876401 with size 4.
default	17:23:52.736088-0500	Nexy	AudioConverter -> 0x82ba47450: The in-process SetProperty call returned 1886547824 for property 1886547309 with size 4.
default	17:23:52.736735-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0x82ba47510, from  2 ch,  48000 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	17:23:52.736741-0500	Nexy	       AudioConverter.cpp:1317  AudioConverter -> 0x82ba47510: The in-process GetProperty call returned 1886547824 for property 1886546285 with size 8.
default	17:23:52.736742-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	17:23:52.736743-0500	Nexy	AudioConverter -> 0x82ba47510: The in-process SetProperty call returned 1886547824 for property 1936876385 with size 4.
default	17:23:52.736747-0500	Nexy	AudioConverter -> 0x82ba47510: The in-process SetProperty call returned 1886547824 for property 1936876401 with size 4.
default	17:23:52.736749-0500	Nexy	AudioConverter -> 0x82ba47510: The in-process SetProperty call returned 1886547824 for property 1886547309 with size 4.
default	17:23:52.736848-0500	Nexy	       AudioConverter.cpp:1317  AudioConverter -> 0x82ba47510: The in-process GetProperty call returned 1886547824 for property 1886546285 with size 8.
default	17:23:52.778047-0500	kernel	udp connect: [<IPv4-redacted>:0<-><IPv4-redacted>:0] interface:  (skipped: 0)
so_gencnt: 5934850 so_state: 0x0000 process: Nexy:21340 bytes in/out: 0/0 pkts in/out: 0/0 error: 49 so_error: 0 svc/tc: 0 flow: 0x0
default	17:23:52.778081-0500	kernel	udp_connection_summary [<IPv4-redacted>:0<-><IPv4-redacted>:0] interface:  (skipped: 0)
so_gencnt: 5934850 so_state: 0x0000 process: Nexy:21340 Duration: 0.000 sec Conn_Time: 0.000 sec bytes in/out: 0/0 pkts in/out: 0/0 rxnospace pkts/bytes: 0/0 so_error: 0 svc/tc: 0 flow: 0x0 flowctl: 0us (0x)
default	17:23:52.778196-0500	kernel	udp connect: [<IPv4-redacted>:53532<-><IPv4-redacted>:443] interface:  (skipped: 0)
so_gencnt: 5934851 so_state: 0x0002 process: Nexy:21340 bytes in/out: 0/0 pkts in/out: 0/0 error: 0 so_error: 0 svc/tc: 0 flow: 0xa716d711
default	17:23:52.778203-0500	kernel	udp_connection_summary [<IPv4-redacted>:53532<-><IPv4-redacted>:443] interface:  (skipped: 0)
so_gencnt: 5934851 so_state: 0x0002 process: Nexy:21340 Duration: 0.000 sec Conn_Time: 0.000 sec bytes in/out: 0/0 pkts in/out: 0/0 rxnospace pkts/bytes: 0/0 so_error: 0 svc/tc: 0 flow: 0xa716d711 flowctl: 0us (0x)
default	17:23:52.778431-0500	kernel	udp_connection_summary [<IPv6-redacted>:62662<-><IPv6-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 5934847 so_state: 0x0132 process: Nexy:21340 Duration: 0.072 sec Conn_Time: 0.071 sec bytes in/out: 355/194 pkts in/out: 3/3 rxnospace pkts/bytes: 0/0 so_error: 0 svc/tc: 0 flow: 0xad668470 flowctl: 0us (0x)
default	17:23:52.781485-0500	kernel	SK[4]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 6F456BC6-C8AC-4D70-AF8A-AB6C10A0B1A7 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.55162,dst=<IPv4-redacted>.443,proto=0x06 mask=0x0000003f,hash=0x05ce2037 tp_proto=0x06"
default	17:23:52.781578-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:55162<-><IPv4-redacted>:443] interface: en0 (skipped: 0)
so_gencnt: 5934852 t_state: SYN_SENT process: Nexy:21340 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x9bd16c2a
default	17:23:52.825151-0500	kernel	tcp connected: [<IPv4-redacted>:55162<-><IPv4-redacted>:443] interface: en0 (skipped: 0)
so_gencnt: 5934852 t_state: ESTABLISHED process: Nexy:21340 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x9bd16c2a
default	17:23:53.745810-0500	Nexy	[0x82cdd7480] activating connection: mach=true listener=false peer=false name=com.apple.usernoted.client
default	17:23:53.758198-0500	usernoted	Connection com.nexy.assistant with path: /Applications/Nexy.app
default	17:23:53.759712-0500	distnoted	register name: com.apple.nsquiet_safe_quit_give_reason object: com.nexy.assistant token: 3000000033 pid: 21340
default	17:23:53.767903-0500	Nexy	NSApp cache appearance:
-NSRequiresAquaSystemAppearance: 0
-appearance: (null)
-effectiveAppearance: <NSCompositeAppearance: 0x82d9dc640
 (
    "<NSAquaAppearance: 0x82d9dc6e0>",
    "<NSSystemAppearance: 0x82d9dc780>"
)>
default	17:23:53.772047-0500	Nexy	[0x82cdd7980] activating connection: mach=true listener=false peer=false name=com.apple.dock.fullscreen
default	17:23:53.772732-0500	Nexy	[0x82cdd7ac0] activating connection: mach=true listener=false peer=false name=com.apple.fonts
default	17:23:53.774907-0500	Nexy	(<private>) deleteSearchableItemsWithDomainIdentifiers, protectionClass:(null), domainIdentifiers number:1
default	17:23:53.775085-0500	Nexy	sConnectionName: com.apple.spotlight.IndexAgent
default	17:23:53.775094-0500	Nexy	Start service name com.apple.spotlight.IndexAgent
default	17:23:53.775114-0500	Nexy	[0x82cdd7c00] activating connection: mach=true listener=false peer=false name=com.apple.spotlight.IndexAgent
default	17:23:53.775136-0500	Nexy	[C:1] Alloc com.apple.controlcenter.statusitems
default	17:23:53.775178-0500	Nexy	[0x82cdd7d40] activating connection: mach=false listener=false peer=false name=(anonymous)
default	17:23:53.775224-0500	Nexy	FBSWorkspace registering source: <private>
default	17:23:53.775732-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	17:23:53.775775-0500	Nexy	<FBSWorkspaceScenesClient:0x8300caee0 <private>> attempting immediate handshake from activate
default	17:23:53.775804-0500	Nexy	<FBSWorkspaceScenesClient:0x8300caee0 <private>> sent handshake
default	17:23:53.775870-0500	Nexy	Realizing settings extension __NSStatusItemSceneHostSettings__ on FBSSceneSettings
default	17:23:53.775774-0500	suggestd	SGDSpotlightReceiver: deleting 1 domain identifiers (1 after removing overlaps) for com.nexy.assistant: <private>
default	17:23:53.776268-0500	ControlCenter	Asked to bootstrap a new process for handle: [app<application.com.nexy.assistant.54878181.54878190(501)>:21340]
default	17:23:53.776293-0500	ControlCenter	Creating process (sync=true) for handle: [app<application.com.nexy.assistant.54878181.54878190(501)>:21340]
default	17:23:53.776364-0500	ControlCenter	[app<application.com.nexy.assistant.54878181.54878190>:21340] Registering event dispatcher at init
default	17:23:53.776310-0500	Nexy	Realizing settings extension __NSStatusItemSceneClientSettings__ on FBSSceneClientSettings
default	17:23:53.776433-0500	ControlCenter	Created <FBWorkspace: 0xc31cf4aa0; <FBApplicationProcess: 0xc32033000; app<application.com.nexy.assistant.54878181.54878190>:21340(v79BA39)>>
default	17:23:53.776452-0500	ControlCenter	Bootstrapping app<application.com.nexy.assistant.54878181.54878190> with intent background
default	17:23:53.776710-0500	runningboardd	Launch request for app<application.com.nexy.assistant.54878181.54878190(501)>[0] is using uid 501 (divined from auid 501 euid 501)
default	17:23:53.776808-0500	runningboardd	Acquiring assertion targeting app<application.com.nexy.assistant.54878181.54878190(501)> from originator [osservice<com.apple.controlcenter(501)>:615] with description <RBSAssertionDescriptor| "FBApplicationProcess" ID:400-615-17231 target:app<application.com.nexy.assistant.54878181.54878190(501)> attributes:[
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableLPRunReason-Suspend" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableRole-NonUI" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableJetsamPriority-Active" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableBootstrapping" sourceEnvironment:"(null)">
	]>
default	17:23:53.776941-0500	runningboardd	Assertion 400-615-17231 (target:app<application.com.nexy.assistant.54878181.54878190(501)>) will be created as active
default	17:23:53.776973-0500	runningboardd	setting abstract target for <RBSAssertionDescriptor| "FBApplicationProcess" ID:400-615-17231 target:app<application.com.nexy.assistant.54878181.54878190(501)> attributes:[
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableLPRunReason-Suspend" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableRole-NonUI" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableJetsamPriority-Active" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableBootstrapping" sourceEnvironment:"(null)">
	]> to [app<application.com.nexy.assistant.54878181.54878190(501)>:21340]
default	17:23:53.777290-0500	runningboardd	[app<application.com.nexy.assistant.54878181.54878190(501)>:21340] Ignoring jetsam update because this process is not memory-managed
default	17:23:53.777301-0500	runningboardd	[app<application.com.nexy.assistant.54878181.54878190(501)>:21340] Ignoring suspend because this process is not lifecycle managed
default	17:23:53.777626-0500	Nexy	Realizing settings extension FBSSceneSettingsCore on FBSSceneSettings
default	17:23:53.777309-0500	runningboardd	[app<application.com.nexy.assistant.54878181.54878190(501)>:21340] Ignoring GPU update because this process is not GPU managed
default	17:23:53.778476-0500	Nexy	Realizing settings extension FBSSceneClientSettingsCore on FBSSceneClientSettings
default	17:23:53.778968-0500	Nexy	Requesting scene <FBSScene: 0x8300cb480; com.apple.controlcenter:A99A00FE-4E63-4F18-9369-39457B8ACFF3> from com.apple.controlcenter.statusitems
default	17:23:53.779180-0500	Nexy	Request for <FBSScene: 0x8300cb480; com.apple.controlcenter:A99A00FE-4E63-4F18-9369-39457B8ACFF3> complete!
default	17:23:53.778219-0500	runningboardd	[app<application.com.nexy.assistant.54878181.54878190(501)>:21340] Ignoring memory limit update because this process is not memory-managed
default	17:23:53.779231-0500	Nexy	Realizing settings extension FBSSceneTransitionContextCore on FBSSceneTransitionContext
default	17:23:53.780400-0500	Nexy	Realizing settings extension __NSHostedViewSceneSettings__ on FBSSceneSettings
default	17:23:53.780643-0500	Nexy	Realizing settings extension __NSClientHostedViewSceneSettings__ on FBSSceneClientSettings
default	17:23:53.780834-0500	Nexy	Realizing settings extension __NSStatusItemAuxiliaryViewSceneSettings__ on FBSSceneSettings
default	17:23:53.780860-0500	Nexy	Realizing settings extension __NSClientStatusItemAuxiliaryViewSceneSettings__ on FBSSceneClientSettings
default	17:23:53.781085-0500	Nexy	Requesting scene <FBSScene: 0x8300cb340; com.apple.controlcenter:A99A00FE-4E63-4F18-9369-39457B8ACFF3-Aux[1]-NSStatusItemView> from com.apple.controlcenter.statusitems
default	17:23:53.781198-0500	Nexy	Request for <FBSScene: 0x8300cb340; com.apple.controlcenter:A99A00FE-4E63-4F18-9369-39457B8ACFF3-Aux[1]-NSStatusItemView> complete!
default	17:23:53.782382-0500	Nexy	[com.apple.controlcenter:A99A00FE-4E63-4F18-9369-39457B8ACFF3-Aux[1]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
default	17:23:53.782393-0500	Nexy	[com.apple.controlcenter:A99A00FE-4E63-4F18-9369-39457B8ACFF3-Aux[1]-NSStatusItemView] Dropping transition context because the scene is reconnecting
default	17:23:53.783814-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.54878181.54878190(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	17:23:53.784427-0500	gamepolicyd	Received state update for 21340 (app<application.com.nexy.assistant.54878181.54878190(501)>, running-active-NotVisible
default	17:23:53.784574-0500	ControlCenter	[app<application.com.nexy.assistant.54878181.54878190>:21340] Bootstrap success!
default	17:23:53.784883-0500	ControlCenter	[app<application.com.nexy.assistant.54878181.54878190>:21340] Setting process visibility to: Background
default	17:23:53.784931-0500	ControlCenter	[app<application.com.nexy.assistant.54878181.54878190>:21340] No launch watchdog for this process, dropping initial assertion in 2.0s
default	17:23:53.785135-0500	Nexy	[com.apple.controlcenter:A99A00FE-4E63-4F18-9369-39457B8ACFF3-Aux[1]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
default	17:23:53.785146-0500	Nexy	[com.apple.controlcenter:A99A00FE-4E63-4F18-9369-39457B8ACFF3-Aux[1]-NSStatusItemView] Dropping transition context because the scene is reconnecting
default	17:23:53.785145-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.54878181.54878190(501)>:21340] from originator [osservice<com.apple.controlcenter(501)>:615] with description <RBSAssertionDescriptor| "FBWorkspaceDomain: injecting saved endowment" ID:400-615-17232 target:21340 attributes:[
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"WorkspaceEndpointInjection" sourceEnvironment:"(null)">
	]>
default	17:23:53.785197-0500	runningboardd	Assertion 400-615-17232 (target:[app<application.com.nexy.assistant.54878181.54878190(501)>:21340]) will be created as active
default	17:23:53.785207-0500	Nexy	Warning: the app is using `-[NSStatusBarButton setHighlightsBy:]` to set the highlight behavior. Instead, consider removing that setting. That will enable macOS to highlight the status bar button as appropriate for all configurations (e.g., light, dark, and increased contrast modes).
default	17:23:53.785480-0500	runningboardd	[app<application.com.nexy.assistant.54878181.54878190(501)>:21340] Ignoring jetsam update because this process is not memory-managed
default	17:23:53.785490-0500	runningboardd	[app<application.com.nexy.assistant.54878181.54878190(501)>:21340] Ignoring suspend because this process is not lifecycle managed
default	17:23:53.785500-0500	runningboardd	[app<application.com.nexy.assistant.54878181.54878190(501)>:21340] Ignoring GPU update because this process is not GPU managed
default	17:23:53.785516-0500	runningboardd	[app<application.com.nexy.assistant.54878181.54878190(501)>:21340] Ignoring memory limit update because this process is not memory-managed
default	17:23:53.788000-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.54878181.54878190(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	17:23:53.788336-0500	ControlCenter	Adding: <FBApplicationProcess: 0xc32033000; app<application.com.nexy.assistant.54878181.54878190>:21340(v79BA39)>
default	17:23:53.788505-0500	gamepolicyd	Received state update for 21340 (app<application.com.nexy.assistant.54878181.54878190(501)>, running-active-NotVisible
default	17:23:53.788747-0500	ControlCenter	[app<application.com.nexy.assistant.54878181.54878190>:21340] Connection established.
default	17:23:53.788800-0500	ControlCenter	[app<application.com.nexy.assistant.54878181.54878190>:21340] created proxy of <BSXPCServiceConnectionProxy<FBSWorkspaceServiceServerInterface>: 0xc34a15b20>
default	17:23:53.788821-0500	ControlCenter	[app<application.com.nexy.assistant.54878181.54878190>:21340] Connection to remote process established!
default	17:23:53.788826-0500	ControlCenter	Received state update for 21340 (app<application.com.nexy.assistant.54878181.54878190(501)>, running-active-NotVisible
default	17:23:53.793837-0500	Nexy	Registering for test daemon availability notify post.
default	17:23:53.793932-0500	Nexy	notify_get_state check indicated test daemon not ready.
default	17:23:53.793992-0500	Nexy	notify_get_state check indicated test daemon not ready.
default	17:23:53.794043-0500	Nexy	notify_get_state check indicated test daemon not ready.
default	17:23:53.794836-0500	Nexy	[0x82cb17d40] activating connection: mach=true listener=false peer=false name=com.apple.coreservices.appleevents
default	17:23:53.795262-0500	ControlCenter	Asked to bootstrap a new process for handle: [app<application.com.nexy.assistant.54878181.54878190(501)>:21340]
default	17:23:53.795285-0500	ControlCenter	A process already exists for this handle: <FBApplicationProcess: 0xc32033000; app<application.com.nexy.assistant.54878181.54878190>:21340(v79BA39)>
default	17:23:53.795401-0500	ControlCenter	[app<application.com.nexy.assistant.54878181.54878190>:21340] Registered new scene: <FBWorkspaceScene: 0xc346c4900; com.apple.controlcenter:A99A00FE-4E63-4F18-9369-39457B8ACFF3> (fromRemnant = 0)
default	17:23:53.795439-0500	ControlCenter	[app<application.com.nexy.assistant.54878181.54878190>:21340] Workspace interruption policy did change: reconnect
default	17:23:53.795610-0500	Nexy	Request for <FBSScene: 0x8300cb480; com.apple.controlcenter:A99A00FE-4E63-4F18-9369-39457B8ACFF3> complete!
default	17:23:53.795613-0500	ControlCenter	[com.apple.controlcenter:A99A00FE-4E63-4F18-9369-39457B8ACFF3] Client process connected: [app<application.com.nexy.assistant.54878181.54878190(501)>:21340]
default	17:23:53.795694-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.54878181.54878190(501)>:21340] from originator [osservice<com.apple.controlcenter(501)>:615] with description <RBSAssertionDescriptor| "com.apple.frontboard.after-life.interrupted" ID:400-615-17233 target:21340 attributes:[
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"AfterLife-Interrupted" sourceEnvironment:"(null)">
	]>
default	17:23:53.795770-0500	runningboardd	Assertion 400-615-17233 (target:[app<application.com.nexy.assistant.54878181.54878190(501)>:21340]) will be created as inactive as originator process has not exited
default	17:23:53.796119-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.54878181.54878190(501)>:21340] from originator [osservice<com.apple.controlcenter(501)>:615] with description <RBSAssertionDescriptor| "FBWorkspace (BG-Active[40])" ID:400-615-17234 target:21340 attributes:[
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableLPRunReason-Suspend" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableRole-NonUI" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableJetsamPriority-Active" sourceEnvironment:"(null)">
	]>
default	17:23:53.796217-0500	runningboardd	Assertion 400-615-17234 (target:[app<application.com.nexy.assistant.54878181.54878190(501)>:21340]) will be created as active
default	17:23:53.796247-0500	ControlCenter	Asked to bootstrap a new process for handle: [app<application.com.nexy.assistant.54878181.54878190(501)>:21340]
default	17:23:53.796264-0500	ControlCenter	A process already exists for this handle: <FBApplicationProcess: 0xc32033000; app<application.com.nexy.assistant.54878181.54878190>:21340(v79BA39)>
default	17:23:53.796298-0500	ControlCenter	[app<application.com.nexy.assistant.54878181.54878190>:21340] Workspace state did change: XX-None[0] --> BG-Active[40] (assertion acquired).
default	17:23:53.796323-0500	ControlCenter	[app<application.com.nexy.assistant.54878181.54878190>:21340] Registered new scene: <FBWorkspaceScene: 0xc346c5440; com.apple.controlcenter:A99A00FE-4E63-4F18-9369-39457B8ACFF3-Aux[1]-NSStatusItemView> (fromRemnant = 0)
default	17:23:53.796458-0500	runningboardd	[app<application.com.nexy.assistant.54878181.54878190(501)>:21340] Ignoring jetsam update because this process is not memory-managed
default	17:23:53.796452-0500	Nexy	Request for <FBSScene: 0x8300cb340; com.apple.controlcenter:A99A00FE-4E63-4F18-9369-39457B8ACFF3-Aux[1]-NSStatusItemView> complete!
default	17:23:53.796461-0500	ControlCenter	[com.apple.controlcenter:A99A00FE-4E63-4F18-9369-39457B8ACFF3-Aux[1]-NSStatusItemView] Client process connected: [app<application.com.nexy.assistant.54878181.54878190(501)>:21340]
default	17:23:53.796469-0500	runningboardd	[app<application.com.nexy.assistant.54878181.54878190(501)>:21340] Ignoring suspend because this process is not lifecycle managed
default	17:23:53.796478-0500	runningboardd	[app<application.com.nexy.assistant.54878181.54878190(501)>:21340] Ignoring GPU update because this process is not GPU managed
default	17:23:53.796515-0500	runningboardd	[app<application.com.nexy.assistant.54878181.54878190(501)>:21340] Ignoring memory limit update because this process is not memory-managed
default	17:23:53.796783-0500	Nexy	<FBSWorkspaceScenesClient:0x8300caee0 <private>> Reconnecting scene com.apple.controlcenter:A99A00FE-4E63-4F18-9369-39457B8ACFF3
default	17:23:53.796964-0500	Nexy	<FBSWorkspaceScenesClient:0x8300caee0 <private>> Reconnecting scene com.apple.controlcenter:A99A00FE-4E63-4F18-9369-39457B8ACFF3-Aux[1]-NSStatusItemView
default	17:23:53.798356-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b5165200 at /Applications/Nexy.app
default	17:23:53.799118-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.54878181.54878190(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	17:23:53.799525-0500	ControlCenter	Received state update for 21340 (app<application.com.nexy.assistant.54878181.54878190(501)>, running-active-NotVisible
default	17:23:53.799590-0500	Nexy	[0x82cb143c0] Connection returned listener port: 0x5103
default	17:23:53.799686-0500	gamepolicyd	Received state update for 21340 (app<application.com.nexy.assistant.54878181.54878190(501)>, running-active-NotVisible
default	17:23:53.799870-0500	Nexy	SignalReady: pid=21340 asn=0x0-0x1eb1eb
default	17:23:53.800507-0500	Nexy	SIGNAL: pid=21340 asn=0x0x-0x1eb1eb
default	17:23:53.800956-0500	loginwindow	-[Application _updateInformationInternal] | Got App URL: file:///Applications/Nexy.app/
default	17:23:53.807003-0500	Nexy	0x82cb64680: Posting CNCDContactStoreDidChangeNotification because accounts changed
default	17:23:53.807010-0500	Nexy	0x82d00a520: Updating using cached account information
default	17:23:53.810381-0500	Nexy	[com.apple.controlcenter:A99A00FE-4E63-4F18-9369-39457B8ACFF3-Aux[1]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
default	17:23:53.812133-0500	Nexy	[com.apple.controlcenter:A99A00FE-4E63-4F18-9369-39457B8ACFF3-Aux[1]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
default	17:23:53.813416-0500	Nexy	void _NSDisableAutomaticTerminationAndLog(NSString *) Restoring windows
default	17:23:53.813426-0500	Nexy	-[NSApplication _reopenWindowsAsNecessaryIncludingRestorableState:withFullFidelity:completionHandler:] shouldRestoreState=1 hasPersistentStateToRestore=0 shouldStillRestoreStateAfterPrompting=0
default	17:23:53.813458-0500	Nexy	[0x82cb15400] activating connection: mach=true listener=false peer=false name=com.apple.window_proxies
default	17:23:53.813514-0500	Nexy	[0x82cb15400] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	17:23:53.814203-0500	Nexy	void _NSEnableAutomaticTerminationAndLog(NSString *) Restoring windows
default	17:23:53.817055-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.54878181.54878190(501)>:21340] from originator [app<application.com.nexy.assistant.54878181.54878190(501)>:21340] with description <RBSAssertionDescriptor| "AudioHAL" ID:400-21340-17235 target:21340 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	17:23:53.817092-0500	runningboardd	Assertion 400-21340-17235 (target:[app<application.com.nexy.assistant.54878181.54878190(501)>:21340]) will be created as active
default	17:23:53.817306-0500	runningboardd	Invalidating assertion 400-21340-17235 (target:[app<application.com.nexy.assistant.54878181.54878190(501)>:21340]) from originator [app<application.com.nexy.assistant.54878181.54878190(501)>:21340]
default	17:23:53.817347-0500	runningboardd	[app<application.com.nexy.assistant.54878181.54878190(501)>:21340] Ignoring jetsam update because this process is not memory-managed
default	17:23:53.817372-0500	runningboardd	[app<application.com.nexy.assistant.54878181.54878190(501)>:21340] Ignoring suspend because this process is not lifecycle managed
default	17:23:53.817379-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.54878181.54878190(501)>:21340] from originator [app<application.com.nexy.assistant.54878181.54878190(501)>:21340] with description <RBSAssertionDescriptor| "AudioHAL" ID:400-21340-17236 target:21340 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	17:23:53.817395-0500	runningboardd	[app<application.com.nexy.assistant.54878181.54878190(501)>:21340] Ignoring GPU update because this process is not GPU managed
default	17:23:53.817452-0500	runningboardd	Assertion 400-21340-17236 (target:[app<application.com.nexy.assistant.54878181.54878190(501)>:21340]) will be created as active
default	17:23:53.817465-0500	runningboardd	[app<application.com.nexy.assistant.54878181.54878190(501)>:21340] Ignoring memory limit update because this process is not memory-managed
default	17:23:53.817833-0500	ControlCenter	Host properties initialized; (bid:com.nexy.assistant-Item-0-21340). State(applicationItem: true, clientRequestsVisibility: true, neverClip: false)
default	17:23:53.819351-0500	ControlCenter	Starting to track host; (bid:com.nexy.assistant-Item-0-21340)
default	17:23:53.819875-0500	ControlCenter	Created new displayable type DisplayableAppStatusItemType(3DE6819B, (bid:com.nexy.assistant-Item-0-21340)) for (bid:com.nexy.assistant-Item-0-21340)
default	17:23:53.820116-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.54878181.54878190(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	17:23:53.820358-0500	runningboardd	Invalidating assertion 400-21340-17236 (target:[app<application.com.nexy.assistant.54878181.54878190(501)>:21340]) from originator [app<application.com.nexy.assistant.54878181.54878190(501)>:21340]
default	17:23:53.820441-0500	ControlCenter	Adding displayable items for status items; [(bid:com.nexy.assistant-Item-0-21340)]
default	17:23:53.820533-0500	ControlCenter	Received state update for 21340 (app<application.com.nexy.assistant.54878181.54878190(501)>, running-active-NotVisible
default	17:23:53.820704-0500	gamepolicyd	Received state update for 21340 (app<application.com.nexy.assistant.54878181.54878190(501)>, running-active-NotVisible
default	17:23:53.820801-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=53435.1938, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=21340, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=53435, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	17:23:53.820981-0500	Nexy	[com.apple.controlcenter:A99A00FE-4E63-4F18-9369-39457B8ACFF3-Aux[1]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
default	17:23:53.820868-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=53435, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=21340, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	17:23:53.821044-0500	Nexy	[0x82cb15400] activating connection: mach=true listener=false peer=false name=com.apple.AddressBook.ContactsAccountsService
default	17:23:53.821156-0500	ControlCenter	Created instance DisplayableId(91EE63C4) in .menuBar for DisplayableAppStatusItemType(3DE6819B, (bid:com.nexy.assistant-Item-0-21340)) .menuBar
default	17:23:53.821386-0500	Nexy	[0x82cb15400] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	17:23:53.821391-0500	Nexy	[com.apple.controlcenter:A99A00FE-4E63-4F18-9369-39457B8ACFF3] Sending action(s) in update: NSSceneFenceAction
default	17:23:53.821399-0500	Nexy	Will add prepared store without migration (path: file:///Users/sergiyzasorin/Library/Application%20Support/AddressBook/Sources/4437DACA-BE14-412E-B504-7A2DD2E9DC7D/AddressBook-v22.abcddb)
default	17:23:53.821444-0500	Nexy	Will add XPC store with options: <private> <private>
default	17:23:53.821885-0500	tccd	AUTHREQ_SUBJECT: msgID=53435.1938, subject=com.nexy.assistant,
default	17:23:53.822458-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x722e70300 at /Applications/Nexy.app
default	17:23:53.822701-0500	Nexy	[0x82cd9c3c0] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	17:23:53.823054-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=53435.1939, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=21340, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=53435, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	17:23:53.823071-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=53435, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=21340, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	17:23:53.823596-0500	tccd	AUTHREQ_SUBJECT: msgID=53435.1939, subject=com.nexy.assistant,
default	17:23:53.823914-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x722e70900 at /Applications/Nexy.app
default	17:23:53.825532-0500	Nexy	[C:2] Alloc <private>
default	17:23:53.825551-0500	Nexy	[0x82cd9c500] activating connection: mach=false listener=false peer=false name=(anonymous)
default	17:23:53.826085-0500	Nexy	[com.apple.controlcenter:A99A00FE-4E63-4F18-9369-39457B8ACFF3-Aux[1]-NSStatusItemView] Received action(s) in scene-update: NSSceneFenceAction
default	17:23:53.826267-0500	ControlCenter	Created ephemaral instance DisplayableId(91EE63C4) for (bid:com.nexy.assistant-Item-0-21340) with positioning .ephemeral
default	17:23:53.826735-0500	WindowManager	Connection activated | (21340) Nexy
default	17:23:53.829011-0500	Nexy	[com.apple.controlcenter:A99A00FE-4E63-4F18-9369-39457B8ACFF3-Aux[1]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
default	17:23:53.835521-0500	Nexy	[0x82cd9c3c0] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	17:23:53.835546-0500	Nexy	[0x82cd9c640] activating connection: mach=false listener=false peer=false name=(anonymous)
default	17:23:53.835587-0500	Nexy	[0x82cd9c3c0] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	17:23:53.836173-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=53435.1940, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=21340, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=53435, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	17:23:53.836210-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=53435, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=21340, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
error	17:23:53.836345-0500	Nexy	It's not legal to call -layoutSubtreeIfNeeded on a view which is already being laid out.  If you are implementing the view's -layout method, you can call -[super layout] instead.  Break on void _NSDetectedLayoutRecursion(void) to debug.  This will be logged only once.  This may break in the future.
default	17:23:53.836410-0500	Nexy	[com.apple.controlcenter:A99A00FE-4E63-4F18-9369-39457B8ACFF3-Aux[1]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
default	17:23:53.837445-0500	tccd	AUTHREQ_SUBJECT: msgID=53435.1940, subject=com.nexy.assistant,
default	17:23:53.838037-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x722e70900 at /Applications/Nexy.app
default	17:23:53.838187-0500	Nexy	Defaultable: persistentAccounts: <private>
default	17:23:53.838206-0500	Nexy	Defaultable: Rejecting account <ABAccount: 0x8300ca800: identifier=_acceptedIntroductions, name=Other Known, baseURL=(nil), dsid=(nil)> because it can't become default
default	17:23:53.838212-0500	Nexy	Defaultable: Rejecting account <ABAccount: 0x8300ca760: identifier=_directoryServices, name=Directory Services, baseURL=(nil), dsid=(nil)> because it can't become default
default	17:23:53.838727-0500	Nexy	[com.apple.controlcenter:A99A00FE-4E63-4F18-9369-39457B8ACFF3] Sending action(s) in update: NSSceneFenceAction
default	17:23:53.838891-0500	Nexy	-awakeFromLoad
default	17:23:53.838951-0500	Nexy	-setServername: <private>  Parsed into scheme: https  host: <private>  port: 0  path: <private>
default	17:23:53.838982-0500	Nexy	-initWithUID:persistence: called on thread: <private>
default	17:23:53.839119-0500	Nexy	-clearPrincipalProperties
default	17:23:53.839131-0500	Nexy	-clearHomeContainers
default	17:23:53.839451-0500	Nexy	Defaultable: Final list: <private>
default	17:23:53.839459-0500	Nexy	New account should become the default account
default	17:23:53.839576-0500	Nexy	0x82cb64680: Posting CNCDContactStoreDidChangeNotification because accounts changed
default	17:23:53.839596-0500	Nexy	0x82d00a520: Updating using cached account information
default	17:23:53.847383-0500	Nexy	[0x82cd9c3c0] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	17:23:53.847404-0500	Nexy	[0x82cd9c3c0] activating connection: mach=false listener=false peer=false name=(anonymous)
default	17:23:53.847428-0500	Nexy	[0x82b6c4000] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	17:23:53.847819-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=53435.1941, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=21340, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=53435, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	17:23:53.847840-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=53435, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=21340, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	17:23:53.848467-0500	tccd	AUTHREQ_SUBJECT: msgID=53435.1941, subject=com.nexy.assistant,
default	17:23:53.848802-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x722e70900 at /Applications/Nexy.app
default	17:23:53.857831-0500	Nexy	[0x82b6c4000] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	17:23:53.857850-0500	Nexy	[0x82b6c4140] activating connection: mach=false listener=false peer=false name=(anonymous)
default	17:23:53.857872-0500	Nexy	[0x82b6c4000] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	17:23:53.858215-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=53435.1942, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=21340, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=53435, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	17:23:53.858230-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=53435, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=21340, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	17:23:53.858738-0500	tccd	AUTHREQ_SUBJECT: msgID=53435.1942, subject=com.nexy.assistant,
default	17:23:53.859081-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x722e70900 at /Applications/Nexy.app
default	17:23:53.868038-0500	Nexy	[0x82b6c4000] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	17:23:53.868060-0500	Nexy	[0x82b6c4000] activating connection: mach=false listener=false peer=false name=(anonymous)
default	17:23:53.868712-0500	Nexy	Did add XPC store
default	17:23:53.868724-0500	Nexy	Did add prepared store without migration (path: file:///Users/sergiyzasorin/Library/Application%20Support/AddressBook/Sources/4437DACA-BE14-412E-B504-7A2DD2E9DC7D/AddressBook-v22.abcddb)
default	17:23:53.868758-0500	Nexy	[0x82b6c4780] activating connection: mach=true listener=false peer=false name=com.apple.AddressBook.ContactsAccountsService
default	17:23:53.868983-0500	Nexy	[0x82b6c4780] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	17:23:53.868995-0500	Nexy	Will add prepared store without migration (path: file:///Users/sergiyzasorin/Library/Application%20Support/AddressBook/AddressBook-v22.abcddb)
default	17:23:53.869016-0500	Nexy	Will add XPC store with options: <private> <private>
default	17:23:53.870100-0500	Nexy	[0x82b6c7200] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	17:23:53.870441-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=53435.1943, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=21340, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=53435, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	17:23:53.870455-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=53435, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=21340, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	17:23:53.870933-0500	tccd	AUTHREQ_SUBJECT: msgID=53435.1943, subject=com.nexy.assistant,
default	17:23:53.871243-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x722e70900 at /Applications/Nexy.app
default	17:23:53.879944-0500	Nexy	[0x82b6c7200] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	17:23:53.879966-0500	Nexy	[0x82b6c7200] activating connection: mach=false listener=false peer=false name=(anonymous)
default	17:23:53.879986-0500	Nexy	[0x82b6c7340] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	17:23:53.880347-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=53435.1944, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=21340, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=53435, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	17:23:53.880371-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=53435, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=21340, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	17:23:53.880930-0500	tccd	AUTHREQ_SUBJECT: msgID=53435.1944, subject=com.nexy.assistant,
default	17:23:53.881228-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x722e70900 at /Applications/Nexy.app
default	17:23:53.889924-0500	Nexy	[0x82b6c7340] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	17:23:53.889944-0500	Nexy	[0x82b6c7340] activating connection: mach=false listener=false peer=false name=(anonymous)
default	17:23:53.889961-0500	Nexy	[0x82b6c7480] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	17:23:53.890297-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=53435.1945, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=21340, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=53435, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	17:23:53.890311-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=53435, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=21340, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	17:23:53.890763-0500	tccd	AUTHREQ_SUBJECT: msgID=53435.1945, subject=com.nexy.assistant,
default	17:23:53.891048-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x722e70900 at /Applications/Nexy.app
default	17:23:53.900268-0500	Nexy	[0x82b6c7480] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	17:23:53.900290-0500	Nexy	[0x82b6c7480] activating connection: mach=false listener=false peer=false name=(anonymous)
default	17:23:53.900305-0500	Nexy	[0x82b6c75c0] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	17:23:53.900655-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=53435.1946, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=21340, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=53435, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	17:23:53.900667-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=53435, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=21340, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	17:23:53.901113-0500	tccd	AUTHREQ_SUBJECT: msgID=53435.1946, subject=com.nexy.assistant,
default	17:23:53.901395-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x722e70900 at /Applications/Nexy.app
default	17:23:53.910913-0500	Nexy	[0x82b6c75c0] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	17:23:53.910934-0500	Nexy	[0x82b6c75c0] activating connection: mach=false listener=false peer=false name=(anonymous)
default	17:23:53.911372-0500	Nexy	Did add XPC store
default	17:23:53.911380-0500	Nexy	Did add prepared store without migration (path: file:///Users/sergiyzasorin/Library/Application%20Support/AddressBook/AddressBook-v22.abcddb)
default	17:23:53.914932-0500	Nexy	Client change history token is invalid: <private>, current token: <private>, error: Error Domain=NSCocoaErrorDomain Code=134501 UserInfo={NSLocalizedFailureReason=<private>}
error	17:23:53.915520-0500	Nexy	Failed to fetch change history: Error Domain=CNErrorDomain Code=1006 "Full Sync Required" UserInfo={NSLocalizedFailureReason=A full sync is required., NSLocalizedDescription=Full Sync Required, NSUnderlyingError=0x83023c0f0 {Error Domain=CNErrorDomain Code=604 "Invalid Change History Anchor" UserInfo={NSLocalizedDescription=Invalid Change History Anchor, NSLocalizedFailureReason=The change history anchor is invalid.}}}
default	17:23:53.915674-0500	Nexy	0000 BEGIN: Will execute fetch for request: <private>
default	17:23:53.915682-0500	Nexy	0000 Entry point: executeFetchRequest:error:
default	17:23:53.915684-0500	Nexy	0000 Predicate: (null) <private>
default	17:23:53.918776-0500	Nexy	*warn* MailCS ======%%% _setMailMessageAttributes skip:1
default	17:23:53.920229-0500	Nexy	Start service name com.apple.spotlightknowledged
default	17:23:53.920646-0500	Nexy	[GMS] availability notification token 123
default	17:23:53.922461-0500	Nexy	App is linked against Fall 2022 SDK or later
default	17:23:53.922467-0500	Nexy	Note access is not granted, so Notes are inaccessible
fault	17:23:53.922521-0500	Nexy	Attempt to read notes by an unentitled app
default	17:23:53.923300-0500	runningboardd	[app<application.com.nexy.assistant.54878181.54878190(501)>:21340] Ignoring jetsam update because this process is not memory-managed
default	17:23:53.923310-0500	runningboardd	[app<application.com.nexy.assistant.54878181.54878190(501)>:21340] Ignoring suspend because this process is not lifecycle managed
default	17:23:53.923320-0500	runningboardd	[app<application.com.nexy.assistant.54878181.54878190(501)>:21340] Ignoring GPU update because this process is not GPU managed
default	17:23:53.923336-0500	runningboardd	[app<application.com.nexy.assistant.54878181.54878190(501)>:21340] Ignoring memory limit update because this process is not memory-managed
default	17:23:53.925862-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.54878181.54878190(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	17:23:53.926212-0500	ControlCenter	Received state update for 21340 (app<application.com.nexy.assistant.54878181.54878190(501)>, running-active-NotVisible
default	17:23:53.926243-0500	gamepolicyd	Received state update for 21340 (app<application.com.nexy.assistant.54878181.54878190(501)>, running-active-NotVisible
default	17:23:53.926646-0500	Nexy	0000 History anchor returned to client: <CNChangeHistoryAnchor: 0x82b7095e0: version=2, token=<NSPersistentHistoryToken - {
    "121C6BBC-8A11-4E34-B252-321D0995C010" = 6;
    "CE445509-54F5-473C-9A96-89025D6F9355" = 4846;
}>>
default	17:23:53.926691-0500	Nexy	0000 Contact: 3EE990C2-437C-497A-B4CF-4787E78B5D0C:ABPerson
default	17:23:53.926696-0500	Nexy	0000 Contact: 2645688D-4F81-4C23-847F-96DEA47CCE6D:ABPerson
default	17:23:53.926697-0500	Nexy	0000 Contact: C822EB31-1F0F-41F6-9120-A322A5874983:ABPerson
default	17:23:53.926702-0500	Nexy	0000 Contact: 50AD2AD1-9340-4D1D-8702-DB033FCB2397:ABPerson
default	17:23:53.926704-0500	Nexy	0000 Contact: EDB979D3-287A-47DC-BC6D-006167336515:ABPerson
default	17:23:53.926707-0500	Nexy	0000 Contact: 9595A838-850C-49DB-8998-80F19667F619:ABPerson
default	17:23:53.926709-0500	Nexy	0000 Contact: 9891AB4D-DDC3-49D3-8FAA-45BFB1995A79:ABPerson
default	17:23:53.926712-0500	Nexy	0000 Contact: 34B7C886-745F-477F-BAF4-C6494310C1C1:ABPerson
default	17:23:53.926714-0500	Nexy	0000 Contact: 3426C1A4-CACA-42EF-8793-7312DCEE5E69:ABPerson
default	17:23:53.926718-0500	Nexy	0000 Contact: AFFBAE3D-BA02-4D6F-AE25-87E55C2E4CD9:ABPerson
default	17:23:53.926722-0500	Nexy	0000 Contact: 55C7A0C2-9163-43BC-95A9-A92E4F5427BD:ABPerson
default	17:23:53.926724-0500	Nexy	0000 Contact: CBAABC59-9B06-47EE-9311-0823CE3EE179:ABPerson
default	17:23:53.926728-0500	Nexy	0000 Contact: FF2BD9DD-8A6D-4E97-BB7D-7B1A5C4FAC0F:ABPerson
default	17:23:53.926731-0500	Nexy	0000 Contact: F6E944AE-3E32-4C0C-BA60-EE94D9402DA7:ABPerson
default	17:23:53.926736-0500	Nexy	0000 Contact: 0E222C4B-C87D-403F-A824-B8B8EAABF29D:ABPerson
default	17:23:53.926743-0500	Nexy	0000 Contact: 160B58EE-E9AF-4BBE-B484-7D4E18CA0CD4:ABPerson
default	17:23:53.926745-0500	Nexy	0000 Contact: D6931A27-6BBA-4ABF-AB86-AA94288C8731:ABPerson
default	17:23:53.926748-0500	Nexy	0000 Contact: 04E7F59A-3D30-4CF9-8395-AE8737EE1154:ABPerson
default	17:23:53.926753-0500	Nexy	0000 Contact: 863252FB-26EB-421B-9B96-91673ED81D35:ABPerson
default	17:23:53.926755-0500	Nexy	0000 Contact: 742C7DAC-D2A9-4D1C-A93D-DC71F37722B9:ABPerson
default	17:23:53.926763-0500	Nexy	0000 Contact: 99649BEC-0C02-4588-9CCA-09103FDC430C:ABPerson
default	17:23:53.926765-0500	Nexy	0000 Contact: 8898FA76-8C7B-4917-B353-30B4A337A32B:ABPerson
default	17:23:53.926769-0500	Nexy	0000 Contact: 75C5C7DD-DD9E-437F-91B9-34AFD56C5A14:ABPerson
default	17:23:53.926775-0500	Nexy	0000 Contact: DDC41FDC-94BF-4147-9863-5AFCC485C4BA:ABPerson
default	17:23:53.926778-0500	Nexy	0000 Contact: B6D0B979-BBDF-4FF5-93A8-0974C5AE45C7:ABPerson
default	17:23:53.926781-0500	Nexy	0000 Contact: B7A8ADD0-A952-45B0-B7A2-D15A3D34A898:ABPerson
default	17:23:53.926786-0500	Nexy	0000 Contact: 35894E4A-BF98-44E4-85B9-33C2A0A01944:ABPerson
default	17:23:53.926793-0500	Nexy	0000 Contact: 67B532BB-C394-4D14-B2E6-C1B93DE930E4:ABPerson
default	17:23:53.926795-0500	Nexy	0000 Contact: A71518ED-EC1D-4740-9D8C-2C5F81C71467:ABPerson
default	17:23:53.926800-0500	Nexy	0000 Contact: EE1E04AC-AF03-428A-97EF-6E8851A86066:ABPerson
default	17:23:53.926805-0500	Nexy	0000 Contact: 54E381BF-247A-4AB7-81FD-8C78CBB93296:ABPerson
default	17:23:53.926810-0500	Nexy	0000 Contact: A5DB19AB-C77E-44EC-87A4-8459DA494E7B:ABPerson
default	17:23:53.926815-0500	Nexy	0000 Contact: FC26680D-B85F-4E40-812F-4F169185AE50:ABPerson
default	17:23:53.926819-0500	Nexy	0000 Contact: E36EA0A4-41F7-4C3F-AAF9-A93099626D77:ABPerson
default	17:23:53.926825-0500	Nexy	0000 Contact: 37E2B276-263E-40A5-BF81-1628796DB605:ABPerson
default	17:23:53.926827-0500	Nexy	0000 Contact: D989E37A-D5DC-4A68-8D47-AD8FEE0B37BA:ABPerson
default	17:23:53.926834-0500	Nexy	0000 Contact: 204F2E81-2324-4937-9859-E8732482C902:ABPerson
default	17:23:53.926839-0500	Nexy	0000 Contact: C4831F25-FE6F-4217-92D2-C4D6C01013BC:ABPerson
default	17:23:53.926843-0500	Nexy	0000 Contact: 4FD77C47-1199-46DF-B186-25C3BB8E54C4:ABPerson
default	17:23:53.926846-0500	Nexy	0000 Contact: 16FA5BBF-AADB-4362-83EB-09668C0C6A84:ABPerson
default	17:23:53.926851-0500	Nexy	0000 Contact: D9A061DB-8A77-472E-A6B3-AF6A4A6727A9:ABPerson
default	17:23:53.926855-0500	Nexy	0000 Contact: 62AC02AD-E5FE-4F18-8DEB-151D2FFD50D2:ABPerson
default	17:23:53.926860-0500	Nexy	0000 Contact: 9D4856E4-4610-4169-9460-115522478752:ABPerson
default	17:23:53.926862-0500	Nexy	0000 Contact: 8038DF9A-4503-4464-BA80-1A8B28F523E6:ABPerson
default	17:23:53.926868-0500	Nexy	0000 Contact: DE31B769-37E8-406B-BC5C-FC44F37A37D1:ABPerson
default	17:23:53.926875-0500	Nexy	0000 Contact: B2E8FADF-3954-4D05-B047-C43474BF8E54:ABPerson
default	17:23:53.926877-0500	Nexy	0000 Contact: 5C30DD83-8C53-4FB6-943A-DF0CED6109D6:ABPerson
default	17:23:53.926882-0500	Nexy	0000 Contact: 16A1EC92-AB39-4C1E-8E16-706B5F47397C:ABPerson
default	17:23:53.926887-0500	Nexy	0000 Contact: 36994EED-FC81-46EF-86F8-8B3217234A98:ABPerson
default	17:23:53.926893-0500	Nexy	0000 Contact: D0D31CD7-6F0F-4030-A30D-197CE5187EED:ABPerson
default	17:23:53.926897-0500	Nexy	0000 Contact: F5676762-711F-4325-8A7A-FCB211127327:ABPerson
default	17:23:53.926903-0500	Nexy	0000 Contact: 99378C4C-7187-4A49-A938-AF1E4D9750E9:ABPerson
default	17:23:53.926911-0500	Nexy	0000 Contact: FE93F61D-6DD6-4CF7-9D17-F972815C60EB:ABPerson
default	17:23:53.926917-0500	Nexy	0000 Contact: E7CCA41A-8A2E-4351-852A-A5CFB6BD2AF5:ABPerson
default	17:23:53.926920-0500	Nexy	0000 Contact: EC41AC6A-1CB5-41D5-B70A-D7D261B5F6B3:ABPerson
default	17:23:53.926923-0500	Nexy	0000 Contact: 2A13AE99-82FE-4A26-A768-1B8C4A11C6C3:ABPerson
default	17:23:53.926925-0500	Nexy	0000 Contact: D5B5277E-F18A-48C2-B93C-E578CEB16C34:ABPerson
default	17:23:53.926928-0500	Nexy	0000 Contact: 1148E024-6D8F-4279-921E-7936B62EB2B8:ABPerson
default	17:23:53.926930-0500	Nexy	0000 Contact: FAF205FC-E995-4261-90F7-336A4D237F48:ABPerson
default	17:23:53.926937-0500	Nexy	0000 Contact: 88E161CA-F779-4608-BE32-D15726C295C6:ABPerson
default	17:23:53.926939-0500	Nexy	0000 Contact: BE244260-8495-47EA-9EFA-A4A129388623:ABPerson
default	17:23:53.926945-0500	Nexy	0000 Contact: FC34E363-0467-4B9C-95B0-F8C585C41741:ABPerson
default	17:23:53.926950-0500	Nexy	0000 Contact: F244F65D-0A57-4A3C-B8B8-9E1C389A5E77:ABPerson
default	17:23:53.926954-0500	Nexy	0000 Contact: 9DE56935-FB3E-470E-9878-89DB593E2DFE:ABPerson
default	17:23:53.926960-0500	Nexy	0000 Contact: 51D61586-1A8A-4EC4-8568-45B5296B1751:ABPerson
default	17:23:53.926965-0500	Nexy	0000 Contact: F34A454E-F1D3-4849-9368-950A6FFA8DD1:ABPerson
default	17:23:53.926970-0500	Nexy	0000 Contact: 5E09571D-9D8E-4D12-8480-F04FD91A55C4:ABPerson
default	17:23:53.926975-0500	Nexy	0000 Contact: 997D7D2F-4504-4C65-A31D-535219B806F5:ABPerson
default	17:23:53.926980-0500	Nexy	0000 Contact: F4D5E6E8-6B00-4329-94DC-82661F45DDB5:ABPerson
default	17:23:53.926985-0500	Nexy	0000 Contact: B3F91E16-48C2-4383-BFDA-F39E45D698A9:ABPerson
default	17:23:53.927047-0500	Nexy	0000 Contact: 972B1CC5-A00E-409A-A1C8-1035B67228F2:ABPerson
default	17:23:53.927062-0500	Nexy	0000 Contact: C9342200-2A80-485B-8777-A59F252176D4:ABPerson
default	17:23:53.927074-0500	Nexy	0000 Contact: FCD5548B-6E7B-4B57-9097-496095F0C27B:ABPerson
default	17:23:53.927087-0500	Nexy	0000 Contact: 32E90B79-BC48-4AFC-A5CE-495011FBE68F:ABPerson
default	17:23:53.927098-0500	Nexy	0000 Contact: 799B442D-0C1B-41A7-982A-5A795CF5AC7E:ABPerson
default	17:23:53.927112-0500	Nexy	0000 Contact: 4BC8FD3A-601A-4905-B4F0-AAEE2EA51FFC:ABPerson
default	17:23:53.927124-0500	Nexy	0000 Contact: EB01D8DC-AD35-4332-B52D-021C69F834F5:ABPerson
default	17:23:53.927135-0500	Nexy	0000 Contact: 34439B56-399C-41AE-8A94-926BE1F059E3:ABPerson
default	17:23:53.927148-0500	Nexy	0000 Contact: 5B2AA695-5EAB-4F85-9EA7-0F11FEE7BF7E:ABPerson
default	17:23:53.927160-0500	Nexy	0000 Contact: 680613B6-43E0-4C77-8B2B-0F21D4D6F558:ABPerson
default	17:23:53.927172-0500	Nexy	0000 Contact: FEFADE95-1917-4F12-AF5F-E9AF0F50E039:ABPerson
default	17:23:53.927185-0500	Nexy	0000 Contact: 1CED5FB1-D054-43C6-BF35-E035DFF16C75:ABPerson
default	17:23:53.927197-0500	Nexy	0000 Contact: 4D6A09F3-71D7-4E04-83FD-9BB5EF7442CF:ABPerson
default	17:23:53.927210-0500	Nexy	0000 Contact: 03F9DBA8-764B-4F5E-AFB8-4FE555600768:ABPerson
default	17:23:53.927221-0500	Nexy	0000 Contact: 33E6AEE6-78CC-42D7-80DA-478EDE698964:ABPerson
default	17:23:53.927242-0500	Nexy	0000 Contact: 2B720652-555E-462B-8C74-277B5F6F5F59:ABPerson
default	17:23:53.927257-0500	Nexy	0000 Contact: D8AB7561-7ABC-404E-A1AD-D9765D7DD983:ABPerson
default	17:23:53.927268-0500	Nexy	0000 Contact: 8256DD81-94E0-404F-BE4E-E6831011073C:ABPerson
default	17:23:53.927282-0500	Nexy	0000 Contact: 260C090E-52D7-4D15-AE22-6804C72C9DBF:ABPerson
default	17:23:53.927314-0500	Nexy	0000 Contact: F5703214-DEA8-429F-ADBF-5465A9AFE1BC:ABPerson
default	17:23:53.927341-0500	Nexy	0000 Contact: 1FBE32BC-B2F2-4B98-8BA8-04A4E25A4F0E:ABPerson
default	17:23:53.927355-0500	Nexy	0000 Contact: 2285EC2D-05CF-42C3-8C59-C4930AD792E3:ABPerson
default	17:23:53.927366-0500	Nexy	0000 Contact: 96E50230-0A5E-4B64-A2E9-A2F57018F4EA:ABPerson
default	17:23:53.927392-0500	Nexy	0000 Contact: 1D80A41C-48FF-40D8-A1F7-EB1FCAF019EC:ABPerson
default	17:23:53.927403-0500	Nexy	0000 Contact: 3C49D81F-04DC-4318-93D4-B25373EDFE30:ABPerson
default	17:23:53.927416-0500	Nexy	0000 Contact: 5B4B2182-FBEA-48F0-B9C7-742552BF6CF6:ABPerson
default	17:23:53.927443-0500	Nexy	0000 Contact: 697396C6-6DF5-4A8D-BBC1-7CFB8C26B531:ABPerson
default	17:23:53.927457-0500	Nexy	0000 Contact: BC83C14B-9BF3-4E6D-A5BD-1252B3AF3A72:ABPerson
default	17:23:53.927469-0500	Nexy	0000 Contact: 29B138C5-7412-4C36-A514-72D80434AC26:ABPerson
default	17:23:53.927484-0500	Nexy	0000 Contact: 93438337-7E2C-4A3D-99F8-28AECEE7A491:ABPerson
default	17:23:53.927498-0500	Nexy	0000 Contact: BEEDDC1A-71AD-4FBD-9241-9F6B4669022C:ABPerson
default	17:23:53.927510-0500	Nexy	0000 Contact: 516FCDD2-D694-4336-9C5C-B3F9398876E3:ABPerson
default	17:23:53.927522-0500	Nexy	0000 Contact: CB798F66-5E15-419F-8CB1-A22A10034846:ABPerson
default	17:23:53.927536-0500	Nexy	0000 Contact: 9BE2908B-57F8-42EB-85AB-E556B53D5008:ABPerson
default	17:23:53.927560-0500	Nexy	0000 Contact: 74E5D1E4-D560-47F5-800D-2B15C8F128ED:ABPerson
default	17:23:53.927580-0500	Nexy	0000 Contact: 73FA4D96-88CD-4E81-B755-D3C151251CB2:ABPerson
default	17:23:53.927594-0500	Nexy	0000 Contact: A159EB30-CDD4-4876-B3EB-7A251E5003A1:ABPerson
default	17:23:53.927607-0500	Nexy	0000 Contact: 2E020885-F8C2-47BB-AEE3-DD7CF66B13B4:ABPerson
default	17:23:53.927619-0500	Nexy	0000 Contact: 05A17C92-D301-4B09-A90C-D64806C4CA53:ABPerson
default	17:23:53.927643-0500	Nexy	0000 Contact: AD733A8E-1D66-4608-811D-8B3CC382D864:ABPerson
default	17:23:53.927658-0500	Nexy	0000 Contact: E567A65A-A157-4ABD-B1FD-82CC549DEDED:ABPerson
default	17:23:53.927669-0500	Nexy	0000 Contact: 7F0336C8-01E0-47A7-A79A-9400EBF86D9C:ABPerson
default	17:23:53.927680-0500	Nexy	0000 Contact: 46F95F55-6525-42E6-A4B3-332AB9ECB6C9:ABPerson
default	17:23:53.927691-0500	Nexy	0000 Contact: 0BF7B2D3-D0E4-4CF5-A2E5-BBAB2F74860F:ABPerson
default	17:23:53.927702-0500	Nexy	0000 Contact: 889A4ED3-ACDE-4D87-9718-586CF8A5A3CC:ABPerson
default	17:23:53.927715-0500	Nexy	0000 Contact: DF05522B-2972-4CAB-8C0F-9FDECE2E3D80:ABPerson
default	17:23:53.927728-0500	Nexy	0000 Contact: 32C28665-F08E-4EE8-AFEB-487908D24319:ABPerson
default	17:23:53.927742-0500	Nexy	0000 Contact: 23512481-0DEF-42CA-8985-3D92A24DC0D9:ABPerson
default	17:23:53.927752-0500	Nexy	0000 Contact: C799BC2E-8783-42B8-BE80-6B9329212F7F:ABPerson
default	17:23:53.927764-0500	Nexy	0000 Contact: AF84B174-40F6-4E9C-A51A-D3FACA6CD75E:ABPerson
default	17:23:53.927776-0500	Nexy	0000 Contact: D41F250E-DF7F-4F9C-9D25-DC402CAC6533:ABPerson
default	17:23:53.927788-0500	Nexy	0000 Contact: E5E58063-920E-46E6-8939-C1A7ACCF23F0:ABPerson
default	17:23:53.927802-0500	Nexy	0000 Contact: F48B9D39-03E0-45D0-AA05-14488FC68C6F:ABPerson
default	17:23:53.927813-0500	Nexy	0000 Contact: B599DEB9-C4DF-472F-9B9E-67C3935077CD:ABPerson
default	17:23:53.927828-0500	Nexy	0000 Contact: CD1D19AA-FC19-4C03-9DC9-C147E8C245D1:ABPerson
default	17:23:53.927839-0500	Nexy	0000 Contact: 4F833F31-870E-4630-825C-0F532CBA3D39:ABPerson
default	17:23:53.927850-0500	Nexy	0000 Contact: BD409DD5-797E-41A8-B955-2CC4520A8769:ABPerson
default	17:23:53.927862-0500	Nexy	0000 Contact: 8A88B309-DB9A-4B6A-B1D9-CD6910D5845B:ABPerson
default	17:23:53.927874-0500	Nexy	0000 Contact: 18BDFAAD-5A5F-42D6-890A-2C5AEA9201D4:ABPerson
default	17:23:53.927885-0500	Nexy	0000 Contact: 96309E07-28A0-4C3F-8B27-7224031FF6EB:ABPerson
default	17:23:53.927896-0500	Nexy	0000 Contact: BF324B31-1F91-4723-87BC-8FE02890D85F:ABPerson
default	17:23:53.927907-0500	Nexy	0000 Contact: A0DA1AD3-5F0A-4625-8A45-AEE2662B5DF7:ABPerson
default	17:23:53.927918-0500	Nexy	0000 Contact: 76DEED21-9E22-4327-83F8-C1C1DDF67DEE:ABPerson
default	17:23:53.927930-0500	Nexy	0000 Contact: 7C25BC81-A7AB-4059-A199-45F36EBE02EB:ABPerson
default	17:23:53.927942-0500	Nexy	0000 Contact: 919E5AE9-2160-41DC-8E41-9C2536932C86:ABPerson
default	17:23:53.927953-0500	Nexy	0000 Contact: 8FC46F73-8C76-4F4F-A480-86AD43FB3197:ABPerson
default	17:23:53.927964-0500	Nexy	0000 Contact: 758B39F6-7626-4392-A342-2F56B6D94427:ABPerson
default	17:23:53.927975-0500	Nexy	0000 Contact: 8A6084C7-9664-4FCF-BD0E-DF7B4AE169BC:ABPerson
default	17:23:53.927988-0500	Nexy	0000 Contact: 51857A1F-41AD-4ABC-BC2E-82377C39162B:ABPerson
default	17:23:53.927999-0500	Nexy	0000 Contact: 0145E52B-5388-4DF4-9BA6-041E2688EA53:ABPerson
default	17:23:53.928010-0500	Nexy	0000 Contact: 7C58562E-BF30-4BE5-AC33-E0A88F42AB76:ABPerson
default	17:23:53.928021-0500	Nexy	0000 Contact: C7C8564C-DF73-4360-B286-BB2CF4C72F17:ABPerson
default	17:23:53.928034-0500	Nexy	0000 Contact: F9EE7585-B534-46B5-848E-58FFD7152121:ABPerson
default	17:23:53.928045-0500	Nexy	0000 Contact: DABCF335-B625-47DD-918B-704381FD587D:ABPerson
default	17:23:53.928056-0500	Nexy	0000 Contact: A68807CD-0A21-4F90-BE39-09BAF83835E8:ABPerson
default	17:23:53.928067-0500	Nexy	0000 Contact: 3B7F983F-D8F3-400C-8462-CA84B84968A4:ABPerson
default	17:23:53.928080-0500	Nexy	0000 Contact: BE53EA52-E9F8-4C18-8446-4FA2489ADE02:ABPerson
default	17:23:53.928091-0500	Nexy	0000 Contact: A804F4AE-3921-4E55-83D8-094B7C4F17A3:ABPerson
default	17:23:53.928102-0500	Nexy	0000 Contact: 489A6364-6AEC-4FC5-8F52-FC08E5527BA0:ABPerson
default	17:23:53.928113-0500	Nexy	0000 Contact: B43BC68C-E9BB-48C1-98C3-A32A09C9A802:ABPerson
default	17:23:53.928124-0500	Nexy	0000 Contact: 05518C4D-4F67-4CD6-83D7-85AA7F2525A5:ABPerson
default	17:23:53.928137-0500	Nexy	0000 Contact: 955CE160-9CC8-4013-829C-A68FD99C7595:ABPerson
default	17:23:53.928149-0500	Nexy	0000 Contact: C13FF96F-DEF6-4C53-83DE-4B45963DD9AF:ABPerson
default	17:23:53.928159-0500	Nexy	0000 Contact: AE65B570-135A-4B14-BA64-EC538224DA56:ABPerson
default	17:23:53.928172-0500	Nexy	0000 Contact: C2132A98-A61A-4358-A681-AF1A1DA20915:ABPerson
default	17:23:53.928183-0500	Nexy	0000 Contact: C3CC1CBC-2410-4DA6-A83E-0477D239E755:ABPerson
default	17:23:53.928194-0500	Nexy	0000 Contact: 0FB60F1D-91EC-4396-A66A-69F15AF14BC5:ABPerson
default	17:23:53.928205-0500	Nexy	0000 Contact: FC6CD704-B936-454E-9EBD-E1701A5DE7D8:ABPerson
default	17:23:53.928215-0500	Nexy	0000 Contact: ED88C6F4-1641-473F-A5BC-DA8C11FCE9D2:ABPerson
default	17:23:53.928231-0500	Nexy	0000 Contact: 88083F13-CF73-4821-896D-8C9EDB5E9029:ABPerson
default	17:23:53.928237-0500	Nexy	0000 Contact: C5BAA4A8-B489-4A59-9400-5C0DFDAA91CA:ABPerson
default	17:23:53.928251-0500	Nexy	0000 Contact: F0187322-8BFE-4EE7-BA9E-BF7D7A056616:ABPerson
default	17:23:53.928263-0500	Nexy	0000 Contact: BA26FE3B-CB6A-471A-8E10-5000CF5332C2:ABPerson
default	17:23:53.928276-0500	Nexy	0000 Contact: DB250DFB-C87D-447B-B125-220B6E3DA663:ABPerson
default	17:23:53.928287-0500	Nexy	0000 Contact: B436BB91-BBBB-49E7-9C6A-93DDDD421478:ABPerson
default	17:23:53.928302-0500	Nexy	0000 Contact: DFCC4D11-6BC3-4ACD-B8C6-F8C46F7C8369:ABPerson
default	17:23:53.928313-0500	Nexy	0000 Contact: 0B435818-E34A-41BF-8808-417BCB956E97:ABPerson
default	17:23:53.928323-0500	Nexy	0000 Contact: E336CBFC-CF06-4672-BEF7-926884FB9BC8:ABPerson
default	17:23:53.928333-0500	Nexy	0000 Contact: A04F02F1-D5E5-4B3E-B5D0-287A46E6DB37:ABPerson
default	17:23:53.928345-0500	Nexy	0000 Contact: 274D78AE-37CF-4B30-B57D-D218F7D433BC:ABPerson
default	17:23:53.928356-0500	Nexy	0000 Contact: AFC75DDF-9D56-451F-8FFA-33CEF512BC9E:ABPerson
default	17:23:53.928368-0500	Nexy	0000 Contact: 36B84A8B-DD90-4609-9407-3BED73397C90:ABPerson
default	17:23:53.928380-0500	Nexy	0000 Contact: 25B2E948-39F0-4DA0-984A-6EAAFC4452BF:ABPerson
default	17:23:53.928390-0500	Nexy	0000 Contact: FD3874CC-9147-45D7-9635-BA7057F1E4CE:ABPerson
default	17:23:53.928401-0500	Nexy	0000 Contact: 93C427E1-DE52-48BF-AFC1-082EC9E9EDA0:ABPerson
default	17:23:53.928412-0500	Nexy	0000 Contact: 0ADD2D08-B0E0-4789-8BA5-3036146B6B78:ABPerson
default	17:23:53.928425-0500	Nexy	0000 Contact: C1626763-A8D5-4907-A0D9-325529F3E7B5:ABPerson
default	17:23:53.928436-0500	Nexy	0000 Contact: A691F96E-80C3-406D-A1F3-443C491D30D0:ABPerson
default	17:23:53.928448-0500	Nexy	0000 Contact: 331AE8C5-F99D-4F0A-B33F-36D558A607C3:ABPerson
default	17:23:53.928462-0500	Nexy	0000 Contact: 5C041266-AB76-41D1-BBBA-5FE4A4792084:ABPerson
default	17:23:53.928472-0500	Nexy	0000 Contact: F3BDC31E-20AF-4198-B696-F389C8F31C9F:ABPerson
default	17:23:53.928482-0500	Nexy	0000 Contact: 0CC4651C-3FC4-4644-BAB9-41107FBFF900:ABPerson
default	17:23:53.928493-0500	Nexy	0000 Contact: 9C0BE147-A58C-44D2-9C4A-FC7DFE653F3E:ABPerson
default	17:23:53.928504-0500	Nexy	0000 Contact: 0C5D18DF-0E63-4D12-AB19-70F9449BFDD3:ABPerson
default	17:23:53.928515-0500	Nexy	0000 Contact: 1EB1F958-3A33-4C17-AEFC-E59EA17F5D5B:ABPerson
default	17:23:53.928525-0500	Nexy	0000 Contact: E9510B2D-16FE-4F94-BBBE-BFACDEEF0759:ABPerson
default	17:23:53.928538-0500	Nexy	0000 Contact: 5D99F42B-5A12-4DD2-9DA9-063C524A30C7:ABPerson
default	17:23:53.928549-0500	Nexy	0000 Contact: 7C44FDAA-3756-43F4-B87F-DDA61E480B1C:ABPerson
default	17:23:53.928560-0500	Nexy	0000 Contact: DFDA976C-6D05-4677-AAA2-604A3688988F:ABPerson
default	17:23:53.928570-0500	Nexy	0000 Contact: 91B8C6A6-858C-4158-B742-E97BCFF7F054:ABPerson
default	17:23:53.928582-0500	Nexy	0000 Contact: 2A16F554-F4B5-4D1A-84FF-1B1B9CD41A6F:ABPerson
default	17:23:53.928592-0500	Nexy	0000 Contact: 51FDBD11-7239-4140-9605-7B2CFF1426E4:ABPerson
default	17:23:53.928603-0500	Nexy	0000 Contact: 2F813EA9-9EFC-409F-A1C4-64F820E4D179:ABPerson
default	17:23:53.928615-0500	Nexy	0000 Contact: 6B7D950D-D374-429D-91CE-A6E1B5D41AAA:ABPerson
default	17:23:53.928627-0500	Nexy	0000 Contact: F7679D0A-6363-40EC-A12A-63E9F2C28321:ABPerson
default	17:23:53.928637-0500	Nexy	0000 Contact: 6703F826-C4D7-43ED-83B5-77B3CBF74E39:ABPerson
default	17:23:53.928649-0500	Nexy	0000 Contact: ED036238-8F1A-4104-98CA-4C44E9BC5990:ABPerson
default	17:23:53.928661-0500	Nexy	0000 Contact: 00F2C374-C9A3-4DD0-B92B-E70CEFC1C968:ABPerson
default	17:23:53.928672-0500	Nexy	0000 Contact: E984A144-E505-46AA-AA38-1CF1EE5DF265:ABPerson
default	17:23:53.928683-0500	Nexy	0000 Contact: 444D762E-7CC5-479E-B3C7-D5172CE8F56B:ABPerson
default	17:23:53.928694-0500	Nexy	0000 Contact: D7D2F3A4-5125-4F75-8CA2-19A18318ABBB:ABPerson
default	17:23:53.928704-0500	Nexy	0000 Contact: AA3A68CB-8A4B-4BAD-94D4-F0B1FDEF6AD2:ABPerson
default	17:23:53.928715-0500	Nexy	0000 Contact: B729AB23-719C-4993-99D4-97F17990CA6E:ABPerson
default	17:23:53.928726-0500	Nexy	0000 Contact: DDD6C0A5-9D08-4756-BB6E-06612386E694:ABPerson
default	17:23:53.928738-0500	Nexy	0000 Contact: DAA81742-1BAC-4E0A-86AB-1805922F5BFB:ABPerson
default	17:23:53.928749-0500	Nexy	0000 Contact: CCCE8074-7CFC-4765-87C4-3DA3398ED5E3:ABPerson
default	17:23:53.928761-0500	Nexy	0000 Contact: B3126A39-DB1F-4EB9-BA9E-057A701FEADB:ABPerson
default	17:23:53.928772-0500	Nexy	0000 Contact: D7A6F43C-FFAB-4219-B325-4345A3EBA5B5:ABPerson
default	17:23:53.928785-0500	Nexy	0000 Contact: F3959633-1472-4370-AE25-6C163A86F28A:ABPerson
default	17:23:53.928795-0500	Nexy	0000 Contact: 818A8D3F-5A2E-44CA-B4CF-47B295DB8C98:ABPerson
default	17:23:53.928806-0500	Nexy	0000 Contact: 228410FA-14BD-488B-A385-35C7112B9635:ABPerson
default	17:23:53.928817-0500	Nexy	0000 Contact: 1A2FDBB3-F370-4D0F-8C9A-34D9C191D7E3:ABPerson
default	17:23:53.928827-0500	Nexy	0000 Contact: 5FDB4463-1088-4EF5-9E20-48795D669908:ABPerson
default	17:23:53.928838-0500	Nexy	0000 Contact: 241E5174-F04C-45D2-BB1E-C4295A53CA80:ABPerson
default	17:23:53.928848-0500	Nexy	0000 Contact: 135FEF8F-5A69-49C6-97E1-E218FAD43A7E:ABPerson
default	17:23:53.928859-0500	Nexy	0000 Contact: F7BF6E9A-A1DE-4F0A-B9FE-DD0E61EBC464:ABPerson
default	17:23:53.928870-0500	Nexy	0000 Contact: F4DA25ED-6C3C-44D5-8A9B-87F14829E713:ABPerson
default	17:23:53.928881-0500	Nexy	0000 Contact: 95FF7EB7-87CC-416D-8811-B8DCC6FE7621:ABPerson
default	17:23:53.928891-0500	Nexy	0000 Contact: 751FAE5C-98A6-414E-B107-317AF0CBED37:ABPerson
default	17:23:53.928903-0500	Nexy	0000 Contact: 5465ECDD-A832-402B-BB73-FDF36810C6E0:ABPerson
default	17:23:53.928914-0500	Nexy	0000 Contact: 52FD2EC7-BEF6-4D05-BCAC-73FBAA131CDF:ABPerson
default	17:23:53.928924-0500	Nexy	0000 Contact: 9D848D63-FDF8-461C-9756-F8AAC3070EFF:ABPerson
default	17:23:53.928936-0500	Nexy	0000 Contact: D6BF6AC9-65CA-41BE-AFA2-C3071A2539F5:ABPerson
default	17:23:53.928946-0500	Nexy	0000 Contact: 4E4C0E62-3EE9-4F23-A226-025907D6882D:ABPerson
default	17:23:53.928957-0500	Nexy	0000 Contact: 1006869C-954C-4394-BFE9-09E9CE09AFB5:ABPerson
default	17:23:53.928968-0500	Nexy	0000 Contact: 339B0201-420C-414B-96CB-1D8150AEF6BB:ABPerson
default	17:23:53.928981-0500	Nexy	0000 Contact: 6A713058-BCB2-4635-BC21-577F0261940C:ABPerson
default	17:23:53.928992-0500	Nexy	0000 Contact: 8B61AAC1-DF6F-440A-B5AC-33331AF930E1:ABPerson
default	17:23:53.929002-0500	Nexy	0000 Contact: B5C0C11D-6F8A-4CCE-872A-DEC086F666A6:ABPerson
default	17:23:53.929013-0500	Nexy	0000 Contact: D17EDFE8-D58A-41FF-B738-D480ED1B54BB:ABPerson
default	17:23:53.929024-0500	Nexy	0000 Contact: 8D969F0D-4878-45C3-A329-14C8F1B9A1C4:ABPerson
default	17:23:53.929035-0500	Nexy	0000 Contact: 4DC763F6-4288-4A25-AE37-52DAC0E54434:ABPerson
default	17:23:53.929047-0500	Nexy	0000 Contact: BB62CE57-7037-4156-BE7F-D1E84FA0B46F:ABPerson
default	17:23:53.929058-0500	Nexy	0000 Contact: 32598CF7-ABA5-4AF8-B60C-8B3F9BB79824:ABPerson
default	17:23:53.929069-0500	Nexy	0000 Contact: 4C93D59E-2641-437E-8D5E-6E5135B4B9D7:ABPerson
default	17:23:53.929080-0500	Nexy	0000 Contact: 95C0601A-0362-4E71-9B56-8E66BA6334DB:ABPerson
default	17:23:53.929090-0500	Nexy	0000 Contact: F23EFEDD-DB9E-4EEE-86A8-A0BB0B161DCE:ABPerson
default	17:23:53.929101-0500	Nexy	0000 Contact: A25C8DA8-E066-47BE-A228-BA3A79122649:ABPerson
default	17:23:53.929112-0500	Nexy	0000 Contact: 7709CB5C-F45D-4130-AFCC-F66EB248B381:ABPerson
default	17:23:53.929124-0500	Nexy	0000 Contact: A95901C1-18E2-412B-9429-B9A87D46EEF1:ABPerson
default	17:23:53.929136-0500	Nexy	0000 Contact: 90CCE3F7-7CB8-44CE-8E3B-0E1FEE5B8574:ABPerson
default	17:23:53.929148-0500	Nexy	0000 Contact: D21F44BE-5C0B-49C1-ACBC-50C7FDD0E574:ABPerson
default	17:23:53.929160-0500	Nexy	0000 Contact: 9A341135-6F8F-42C6-A5D8-776E0F0EF424:ABPerson
default	17:23:53.929172-0500	Nexy	0000 Contact: 60C9F9CC-1758-4215-94FA-79E8E5591D0D:ABPerson
default	17:23:53.929184-0500	Nexy	0000 Contact: 7A0D8FED-170A-4F26-B868-532276E4BDF6:ABPerson
default	17:23:53.929194-0500	Nexy	0000 Contact: 791662EB-B4C3-41EA-8207-065A1C9F0AA0:ABPerson
default	17:23:53.929205-0500	Nexy	0000 Contact: D5AB1F03-8C06-438F-8713-DCCBBCD76892:ABPerson
default	17:23:53.929218-0500	Nexy	0000 Contact: 96EC0E50-9CC0-4769-8082-E7C877889553:ABPerson
default	17:23:53.929229-0500	Nexy	0000 Contact: 33394098-1926-4C5F-AA29-7B8610A5C7E6:ABPerson
default	17:23:53.929243-0500	Nexy	0000 Contact: B5956767-6E1D-49F2-8708-69E0D16EC786:ABPerson
default	17:23:53.929255-0500	Nexy	0000 Contact: 918AF5E7-EDE6-400D-A786-261C7B3BC323:ABPerson
default	17:23:53.929267-0500	Nexy	0000 Contact: 78374AF4-D2CF-4636-B824-5922E7BCDAA7:ABPerson
default	17:23:53.929279-0500	Nexy	0000 Contact: E1E5926D-F19D-45D4-9FFE-12E3198D0E67:ABPerson
default	17:23:53.929290-0500	Nexy	0000 Contact: DB957E68-3771-4194-AB47-1B347BE66F63:ABPerson
default	17:23:53.929301-0500	Nexy	0000 Contact: 2112C6EB-840A-49FE-B03E-5DDBFE2F6992:ABPerson
default	17:23:53.929311-0500	Nexy	0000 Contact: 3E8DAA1B-0AD6-465E-BDAB-A68A5FD23D3E:ABPerson
default	17:23:53.929322-0500	Nexy	0000 Contact: 5B8A6BDC-5927-4718-B89F-674DCC70DA16:ABPerson
default	17:23:53.929332-0500	Nexy	0000 Contact: 44BFDAD7-D780-4604-8369-CD3317F7F3FB:ABPerson
default	17:23:53.929343-0500	Nexy	0000 Contact: DD452BC2-AA0F-4E55-9417-30946834E7D9:ABPerson
default	17:23:53.929354-0500	Nexy	0000 Contact: A79E1C58-6726-4518-9160-5833FD1D9E85:ABPerson
default	17:23:53.929366-0500	Nexy	0000 Contact: EEDB6E81-803C-4D9E-9479-23840064FF07:ABPerson
default	17:23:53.929377-0500	Nexy	0000 Contact: E8BAA178-7C7C-4B0C-837F-07B80E6A8155:ABPerson
default	17:23:53.929387-0500	Nexy	0000 Contact: A8C84C99-FF9C-48DF-A603-CEB3050F0BC6:ABPerson
default	17:23:53.929398-0500	Nexy	0000 Contact: 0FD65269-7801-440C-A119-71EBE23C4E70:ABPerson
default	17:23:53.929409-0500	Nexy	0000 Contact: 0A4FEAE5-C426-4926-8B49-A5260D97B9E6:ABPerson
default	17:23:53.929421-0500	Nexy	0000 Contact: CA81313F-6121-4FF6-B60C-EEE869ECF990:ABPerson
default	17:23:53.929433-0500	Nexy	0000 Contact: EA9B96E2-2F87-4EB2-AD12-46F37DFF0EC9:ABPerson
default	17:23:53.929445-0500	Nexy	0000 Contact: 7A89C56B-6D06-419B-A08D-00F14B94AA1C:ABPerson
default	17:23:53.929455-0500	Nexy	0000 Contact: 660A1E96-3CA3-48B5-B94A-96D6D35A72E6:ABPerson
default	17:23:53.929466-0500	Nexy	0000 Contact: 3F5D85F3-9B89-4AD7-A353-FEFEA5DA1C36:ABPerson
default	17:23:53.929476-0500	Nexy	0000 Contact: 8F99EACB-5E71-4F4C-9899-AE7E1FF5280E:ABPerson
default	17:23:53.929491-0500	Nexy	0000 Contact: 9E8B52AD-B9B2-41CA-8134-7861A90F9A02:ABPerson
default	17:23:53.929502-0500	Nexy	0000 Contact: 98237DEC-70B4-4CA5-A4B8-FEE401C3F3C4:ABPerson
default	17:23:53.929512-0500	Nexy	0000 Contact: BD690A56-23D5-4941-B041-50C06351C977:ABPerson
default	17:23:53.929523-0500	Nexy	0000 Contact: D191A589-BA65-49F2-86A3-08D90FB284FD:ABPerson
default	17:23:53.929534-0500	Nexy	0000 Contact: AAF5FE8A-214C-4B65-9B4F-C2578C97C51D:ABPerson
default	17:23:53.929546-0500	Nexy	0000 Contact: 3D737248-8F03-4732-8B3A-8CDA2D45B5AA:ABPerson
default	17:23:53.929558-0500	Nexy	0000 Contact: E120A189-E8F5-4B5F-A2A2-B1A60E6DF145:ABPerson
default	17:23:53.929569-0500	Nexy	0000 Contact: 46187B48-32E0-4B21-B7CE-D3B44766EEEC:ABPerson
default	17:23:53.929580-0500	Nexy	0000 Contact: B72ACD21-62D9-4BC2-8F5A-F33464EEEED5:ABPerson
default	17:23:53.929591-0500	Nexy	0000 Contact: 1D1B1CB1-D316-4BC5-B11C-BC2D4D437605:ABPerson
default	17:23:53.929603-0500	Nexy	0000 Contact: EEC7F987-F555-4025-8B35-10CBE93E26D7:ABPerson
default	17:23:53.929615-0500	Nexy	0000 Contact: A4F96105-C3FC-4D3D-842F-E729A3F28760:ABPerson
default	17:23:53.929626-0500	Nexy	0000 Contact: F0613D78-6887-4B13-AC52-703B5D1A7060:ABPerson
default	17:23:53.929637-0500	Nexy	0000 Contact: BDD5E012-4C2D-4949-9778-80672887C0EC:ABPerson
default	17:23:53.929650-0500	Nexy	0000 Contact: E03CBC1C-C4D5-476B-A9AE-20A246A5FE73:ABPerson
default	17:23:53.929660-0500	Nexy	0000 Contact: A9567605-C983-4D5B-9877-2D3BC5D341CF:ABPerson
default	17:23:53.929670-0500	Nexy	0000 Contact: 378D10F9-7887-44F8-B0A5-9683F2AF012D:ABPerson
default	17:23:53.929682-0500	Nexy	0000 Contact: 29F7EE25-03CA-4DEA-AB4C-5E84B0046094:ABPerson
default	17:23:53.929692-0500	Nexy	0000 Contact: 6045438B-32EF-4240-BCDE-3A83DD6098C1:ABPerson
default	17:23:53.929704-0500	Nexy	0000 Contact: CC00B3CB-4536-414F-8E8F-116901AAAB66:ABPerson
default	17:23:53.929716-0500	Nexy	0000 Contact: CDF1FCD3-669F-4B16-9D7A-07091B53B43E:ABPerson
default	17:23:53.929730-0500	Nexy	0000 Contact: 1C7A8AAA-2853-4C56-892C-93832C406B2F:ABPerson
default	17:23:53.929742-0500	Nexy	0000 Contact: 5FA233B8-A72C-468F-8344-138CB3A320AD:ABPerson
default	17:23:53.929753-0500	Nexy	0000 Contact: CC42A082-921C-4A2F-9B2A-20AD5E63DE26:ABPerson
default	17:23:53.929764-0500	Nexy	0000 Contact: 4D22B39B-A7C9-4F71-B531-0D0A75E819DC:ABPerson
default	17:23:53.929775-0500	Nexy	0000 Contact: 10DA5D0D-F87E-40C2-A2FB-1B4E18ADEED7:ABPerson
default	17:23:53.929788-0500	Nexy	0000 Contact: 1020F64F-877A-46EF-A85B-0B7B4702F30A:ABPerson
default	17:23:53.929800-0500	Nexy	0000 Contact: 7A3258A0-4EF6-4C07-8BAC-DE67AFC5BF0F:ABPerson
default	17:23:53.929828-0500	Nexy	0000 Contact: D8BF88A0-50CD-408B-91AC-FABB6153F0E7:ABPerson
default	17:23:53.929843-0500	Nexy	0000 Contact: F96FB111-3581-4F57-A0DB-8D18E0A5CE3D:ABPerson
default	17:23:53.929856-0500	Nexy	0000 Contact: F8DEA06B-2666-4B7C-AB2B-2D1C7121121A:ABPerson
default	17:23:53.929867-0500	Nexy	0000 Contact: 2DD46A4A-00EA-4AF2-BED6-A0E4704A401E:ABPerson
default	17:23:53.929878-0500	Nexy	0000 Contact: E75A43A8-9126-46AD-BDE0-2F09D8195FCE:ABPerson
default	17:23:53.929893-0500	Nexy	0000 Contact: 0CE70590-2C7E-400D-AAC3-E2AB83B20E6D:ABPerson
default	17:23:53.929904-0500	Nexy	0000 Contact: C93B2BF3-4882-418D-A785-20AABA5900CA:ABPerson
default	17:23:53.929917-0500	Nexy	0000 Contact: 72A79220-BD0A-4F38-A644-7891B8D6D08C:ABPerson
default	17:23:53.929929-0500	Nexy	0000 Contact: 5168F235-33BF-487B-9C88-9A0977EF3D96:ABPerson
default	17:23:53.929939-0500	Nexy	0000 Contact: EF5D8980-C0E4-4FBD-8942-AC7EC9F886BE:ABPerson
default	17:23:53.929950-0500	Nexy	0000 Contact: 8335160D-3EFF-4C7A-B500-08D4AAF9D6C4:ABPerson
default	17:23:53.929963-0500	Nexy	0000 Contact: F30C415E-480E-47D7-A697-2DDF78C62B78:ABPerson
default	17:23:53.929975-0500	Nexy	0000 Contact: 4B86EE6B-7192-4DEC-9A5D-DB2A68A29544:ABPerson
default	17:23:53.929986-0500	Nexy	0000 Contact: 7028A821-E1BB-4996-9F0A-B483955BBD46:ABPerson
default	17:23:53.929999-0500	Nexy	0000 Contact: 7C930844-C857-4F62-B795-A317F57982E7:ABPerson
default	17:23:53.930011-0500	Nexy	0000 Contact: 2958D2B1-193E-4859-97A7-E9D0A6DDAC5B:ABPerson
default	17:23:53.930022-0500	Nexy	0000 Contact: CF7AC9E0-68F2-4C92-A7E7-2F56630F8B8B:ABPerson
default	17:23:53.930032-0500	Nexy	0000 Contact: ADDCC376-3417-4952-A610-3D53B96EC2BD:ABPerson
default	17:23:53.930043-0500	Nexy	0000 Contact: 19855E2F-023D-4999-A9F8-0515B5257D6F:ABPerson
default	17:23:53.930056-0500	Nexy	0000 Contact: 2BAB4AEF-3D51-42E4-BBCA-4587A6EF5B42:ABPerson
default	17:23:53.930067-0500	Nexy	0000 Contact: B68F306A-9F87-4675-9C7C-73ADAC3CF928:ABPerson
default	17:23:53.930078-0500	Nexy	0000 Contact: EBEFEBC5-E9A8-48CB-B48D-DE0E2C3AE2B9:ABPerson
default	17:23:53.930088-0500	Nexy	0000 Contact: C1E29AB3-927E-4614-A170-469712D37DE0:ABPerson
default	17:23:53.930100-0500	Nexy	0000 Contact: 1E18829A-DFA4-4A9A-AEBA-FFF85B2D3E00:ABPerson
default	17:23:53.930111-0500	Nexy	0000 Contact: 41E94FCB-1477-45AF-AB50-6AF7C4651D76:ABPerson
default	17:23:53.930123-0500	Nexy	0000 Contact: 55D05EF1-7380-43F3-9CCC-FCCBB0A382A9:ABPerson
default	17:23:53.930135-0500	Nexy	0000 Contact: 88B8B688-3607-4FD1-BE7E-73F6DAA20674:ABPerson
default	17:23:53.930147-0500	Nexy	0000 Contact: 6A7FA276-678E-44BC-A5CD-1E7AB887CD37:ABPerson
default	17:23:53.930159-0500	Nexy	0000 Contact: A6FD2708-9CD8-45E0-9E88-5BE836285468:ABPerson
default	17:23:53.930171-0500	Nexy	0000 Contact: FFBA4F3C-8FF6-4FC6-9CB6-F62755FFB90C:ABPerson
default	17:23:53.930181-0500	Nexy	0000 Contact: F5A10DB4-BCD8-4342-9435-C976615D2367:ABPerson
default	17:23:53.930192-0500	Nexy	0000 Contact: 1C210F17-EE8F-4513-8100-4877479969F3:ABPerson
default	17:23:53.930203-0500	Nexy	0000 Contact: E6ACEB4F-3D7F-4D37-8463-568D34A3D393:ABPerson
default	17:23:53.930217-0500	Nexy	0000 Contact: 05B170A2-D739-4BCB-A7A9-927DAAC7B3FD:ABPerson
default	17:23:53.930229-0500	Nexy	0000 Contact: 791F5495-5017-4DBF-ABB6-4220285C8A7F:ABPerson
default	17:23:53.930242-0500	Nexy	0000 Contact: DFA3FE46-B8CF-41EC-B2E6-04C798B63209:ABPerson
default	17:23:53.930255-0500	Nexy	0000 Contact: 09772BD5-23E2-45C0-8579-EAA3F5DFAA04:ABPerson
default	17:23:53.930269-0500	Nexy	0000 Contact: 21D1D25A-A332-455E-BF6D-219DAED4CF2E:ABPerson
default	17:23:53.930282-0500	Nexy	0000 Contact: 85CBC919-29F4-4481-90E8-91811DF04251:ABPerson
default	17:23:53.930293-0500	Nexy	0000 Contact: 7D4E6C00-B562-4BD3-84B2-BE3484A218DC:ABPerson
default	17:23:53.930305-0500	Nexy	0000 Contact: 7CEA1D92-BD70-4661-A995-FC9C088765E4:ABPerson
default	17:23:53.930318-0500	Nexy	0000 Contact: 5BC153A8-ECD2-4153-8199-62D228ED9EFF:ABPerson
default	17:23:53.930329-0500	Nexy	0000 Contact: 539E00F6-4B11-4899-9B48-833F1C83B1AF:ABPerson
default	17:23:53.930341-0500	Nexy	0000 Contact: 480BDC40-266E-44A2-A7F0-81FF207F9107:ABPerson
default	17:23:53.930352-0500	Nexy	0000 Contact: AD76EC2F-309C-4663-88AB-5380B537AD21:ABPerson
default	17:23:53.930363-0500	Nexy	0000 Contact: E8D00EFB-149F-4D70-9E53-DCC37B11CA41:ABPerson
default	17:23:53.930375-0500	Nexy	0000 Contact: F1AC5DD9-2463-40B4-A31D-D698D4A81A07:ABPerson
default	17:23:53.930391-0500	Nexy	0000 Contact: 5CC4AD9E-AFA2-4D91-93BB-A2AEE0287CA1:ABPerson
default	17:23:53.930402-0500	Nexy	0000 Contact: 82273310-7E56-45DD-8F38-49E6EFB991AF:ABPerson
default	17:23:53.930428-0500	Nexy	0000 Contact: 52C4710F-7736-48E9-81CB-BFB715D2471F:ABPerson
default	17:23:53.930459-0500	Nexy	0000 Contact: 3DAF2C1D-E01A-4ECE-88B6-7A1FEC8F43AC:ABPerson
default	17:23:53.930470-0500	Nexy	0000 Contact: C66A3203-5558-449A-90CB-DECEC564C830:ABPerson
default	17:23:53.930483-0500	Nexy	0000 Contact: 1587F0BD-924E-4B7A-B625-9C3C29B7D02B:ABPerson
default	17:23:53.930495-0500	Nexy	0000 Contact: 8E669F37-64D4-4FCD-83DF-C7AB7025BAED:ABPerson
default	17:23:53.930507-0500	Nexy	0000 Contact: 42E8C30D-1FB0-42FC-833E-588AB5BBE3DB:ABPerson
default	17:23:53.930517-0500	Nexy	0000 Contact: EAE3066F-0C4F-41A6-8DBE-F68459786EC0:ABPerson
default	17:23:53.930531-0500	Nexy	0000 Contact: 2AF16E0B-3963-42BF-9826-D9FEA11B3CCA:ABPerson
default	17:23:53.930541-0500	Nexy	0000 Contact: 319E891D-32E9-49AF-B4E4-B5BAE8155200:ABPerson
default	17:23:53.930568-0500	Nexy	0000 Contact: 1594CB17-7E0F-473A-929D-C52CB3C2ADF4:ABPerson
default	17:23:53.930594-0500	Nexy	0000 Contact: 77010702-80A2-4E97-B0A7-B2EE441BFF58:ABPerson
default	17:23:53.930605-0500	Nexy	0000 Contact: 878309A1-31D9-4B89-8226-32C4BFA85E5A:ABPerson
default	17:23:53.930655-0500	Nexy	0000 Contact: 8C53459B-D709-4754-8779-C759C5D30623:ABPerson
default	17:23:53.930666-0500	Nexy	0000 Contact: 2D7A7BAB-3BDE-4E62-9336-46D7687262C6:ABPerson
default	17:23:53.930692-0500	Nexy	0000 Contact: ADE039BB-356A-4FF6-9B48-11643C1A74A3:ABPerson
default	17:23:53.930704-0500	Nexy	0000 Contact: 1DAA78BA-EBAD-4BF6-B582-A4DE8A4A1F60:ABPerson
default	17:23:53.930746-0500	Nexy	0000 Contact: E3B3AD82-9DE2-41D8-BAB4-955DF431F0D7:ABPerson
default	17:23:53.930756-0500	Nexy	0000 Contact: 4EA7F008-36E8-457A-AB52-5E92AB655707:ABPerson
default	17:23:53.930779-0500	Nexy	0000 Contact: 2EE1FF46-FBE2-4A40-8CE4-EC8C163406A8:ABPerson
default	17:23:53.930794-0500	Nexy	0000 Contact: 4749FF87-CDF6-4765-A605-FBF954CEC3DD:ABPerson
default	17:23:53.930805-0500	Nexy	0000 Contact: 78533628-5040-45D4-907C-06311D0B83C8:ABPerson
default	17:23:53.930818-0500	Nexy	0000 Contact: 55ED3DE3-FD66-4A5E-995C-7174A0F57355:ABPerson
default	17:23:53.930829-0500	Nexy	0000 Contact: 1EB3E13D-C8C2-40B4-B5C1-95672F5BB775:ABPerson
default	17:23:53.930840-0500	Nexy	0000 Contact: F83287C3-CE0B-407B-88A2-A5B43CAB98EC:ABPerson
default	17:23:53.930850-0500	Nexy	0000 Contact: 2D1AC54F-1C05-415F-803B-EB84B4DE155C:ABPerson
default	17:23:53.930862-0500	Nexy	0000 Contact: C8633A15-35F4-4ABC-9A2A-82EBF1A6767D:ABPerson
default	17:23:53.930874-0500	Nexy	0000 Contact: D62A5235-E401-4A9F-AC82-61328161530D:ABPerson
default	17:23:53.930885-0500	Nexy	0000 Contact: C80DE5B6-E12E-4835-863B-E63D84C0DEB5:ABPerson
default	17:23:53.930896-0500	Nexy	0000 Contact: 922530A8-0D72-4067-AAC0-1FF5C4ABE1BA:ABPerson
default	17:23:53.930907-0500	Nexy	0000 Contact: A66AB62E-7C4B-489D-A5AC-97BE240AF07B:ABPerson
default	17:23:53.930917-0500	Nexy	0000 Contact: C42862EB-E49A-4500-B5A0-744247A93DC0:ABPerson
default	17:23:53.930928-0500	Nexy	0000 Contact: 3608E376-1FDF-4DA6-94BE-B39CF8F32D25:ABPerson
default	17:23:53.930941-0500	Nexy	0000 Contact: 3D44B959-62DC-41CB-825F-C0FB5D231322:ABPerson
default	17:23:53.930952-0500	Nexy	0000 Contact: 47FCBCE3-65D3-44A4-8283-4C1AF6654C9F:ABPerson
default	17:23:53.930963-0500	Nexy	0000 Contact: 93BAC1B1-3857-40CA-A143-09E6F7A990EF:ABPerson
default	17:23:53.930974-0500	Nexy	0000 Contact: F1B433EB-BB39-4CD7-A784-1E41309B908C:ABPerson
default	17:23:53.930985-0500	Nexy	0000 Contact: A52B8A51-99C7-427A-BD9F-97EC5E9F7EA8:ABPerson
default	17:23:53.930998-0500	Nexy	0000 Contact: 0191E2F5-DF4D-441F-A40B-BBEE1682877B:ABPerson
default	17:23:53.931009-0500	Nexy	0000 Contact: 0697FA50-06C8-4FDB-A5D3-B10F8A859674:ABPerson
default	17:23:53.931021-0500	Nexy	0000 Contact: 093F142A-458F-4ACF-BEEE-FAB7BA5E520A:ABPerson
default	17:23:53.931032-0500	Nexy	0000 Contact: 98F95301-000C-4EF9-91DF-E637EF0C27F4:ABPerson
default	17:23:53.931045-0500	Nexy	0000 Contact: 720814F5-D603-40AE-A834-D49467F3A7FD:ABPerson
default	17:23:53.931056-0500	Nexy	0000 Contact: 40CDB1E4-DC18-4D79-AE2F-6242CCF62978:ABPerson
default	17:23:53.931067-0500	Nexy	0000 Contact: A8D9C348-1926-49B7-98C2-A2C917FB651B:ABPerson
default	17:23:53.931078-0500	Nexy	0000 Contact: 7656FBDF-5810-4382-9538-529EC1E5EF83:ABPerson
default	17:23:53.931092-0500	Nexy	0000 Contact: 8F442B0B-AFC7-4087-AEFC-FDC987F28E2C:ABPerson
default	17:23:53.931106-0500	Nexy	0000 Contact: DE96F2D0-DA7E-4742-AD3E-6D43BC32C213:ABPerson
default	17:23:53.931116-0500	Nexy	0000 Contact: DA1B14DD-D92B-4633-BF3C-0CCCE7117BE4:ABPerson
default	17:23:53.931128-0500	Nexy	0000 Contact: 0134E272-51ED-44B6-AC46-4C34642F56AA:ABPerson
default	17:23:53.931138-0500	Nexy	0000 Contact: FA551EE7-6781-4874-B9EA-0B6893B3293F:ABPerson
default	17:23:53.931149-0500	Nexy	0000 Contact: A88C8AF6-EF10-48E8-9C60-3709424155EB:ABPerson
default	17:23:53.931160-0500	Nexy	0000 Contact: C00692B4-EC26-459C-A690-D23F5BCEF621:ABPerson
default	17:23:53.931171-0500	Nexy	0000 Contact: 652921DA-B2DA-4539-A7F6-6B5A80149E2C:ABPerson
default	17:23:53.931185-0500	Nexy	0000 Contact: 88DED267-1D14-49FB-B0EA-D61FEEEA7475:ABPerson
default	17:23:53.931196-0500	Nexy	0000 Contact: CEB05018-C421-4234-BE90-56F8041F2286:ABPerson
default	17:23:53.931207-0500	Nexy	0000 Contact: DFB23C20-7349-4617-9A20-48014D8D844F:ABPerson
default	17:23:53.931216-0500	Nexy	0000 Contact: 9AC48DA6-FEAA-4630-AD56-EF041D62524A:ABPerson
default	17:23:53.931229-0500	Nexy	0000 Contact: 936230C2-1597-4A80-898D-31476BAE0C72:ABPerson
default	17:23:53.931241-0500	Nexy	0000 Contact: E99AC935-51E8-4AC2-9D90-C3ED9A41CF89:ABPerson
default	17:23:53.931253-0500	Nexy	0000 Contact: 1041C9F3-A247-4866-BCE3-A908919C3641:ABPerson
default	17:23:53.931266-0500	Nexy	0000 Contact: AA55B04C-AA66-4E4C-BE73-FCD01D057FF4:ABPerson
default	17:23:53.931277-0500	Nexy	0000 Contact: 8E1DE28A-250A-438D-ADCC-EC00B09AFDCF:ABPerson
default	17:23:53.931288-0500	Nexy	0000 Contact: 9D974937-BC35-459C-9596-7F3C287A39DE:ABPerson
default	17:23:53.931298-0500	Nexy	0000 Contact: 7A52455B-63F6-4500-850D-4CD4CAEE7CDA:ABPerson
default	17:23:53.931310-0500	Nexy	0000 Contact: BB0E685F-E844-4A51-8837-01C68FCCEECD:ABPerson
default	17:23:53.931324-0500	Nexy	0000 Contact: 958F31A6-1E1B-4833-99AC-EC3D8191CACE:ABPerson
default	17:23:53.931334-0500	Nexy	0000 Contact: 88212F02-02C2-4E0B-AD31-33A4F57D97C3:ABPerson
default	17:23:53.931346-0500	Nexy	0000 Contact: 060A07B0-DE54-4CA0-82F9-C5E7D642FE04:ABPerson
default	17:23:53.931356-0500	Nexy	0000 Contact: 84FD0E15-D8B4-4C4A-AF3F-ECACC4D7D2AB:ABPerson
default	17:23:53.931368-0500	Nexy	0000 Contact: E03C33D7-9B66-41CC-9823-13495C0F1BFF:ABPerson
default	17:23:53.931379-0500	Nexy	0000 Contact: 4F05D0EB-A7C7-4CE9-8BBE-252CDE0913B6:ABPerson
default	17:23:53.931390-0500	Nexy	0000 Contact: 0D4D94BE-BE27-4924-B1EF-D18DBC8CB9CB:ABPerson
default	17:23:53.931401-0500	Nexy	0000 Contact: DE3244DE-AA8B-42BE-9E6B-D93D5F072FC8:ABPerson
default	17:23:53.931413-0500	Nexy	0000 Contact: D2349093-8AC3-493E-A63B-2FDDBF010597:ABPerson
default	17:23:53.931423-0500	Nexy	0000 Contact: 582B6770-D754-4F28-BE23-DE8B912C1D70:ABPerson
default	17:23:53.931435-0500	Nexy	0000 Contact: 7230DAA8-42F7-4810-9E64-7E0576DEC21F:ABPerson
default	17:23:53.931446-0500	Nexy	0000 Contact: A044BEEF-238E-4A88-9B39-26B87097EDBA:ABPerson
default	17:23:53.931457-0500	Nexy	0000 Contact: 37C10F00-3A36-4D68-A9FE-F7CBB93250AA:ABPerson
default	17:23:53.931468-0500	Nexy	0000 Contact: BF90E79B-597F-4512-8E44-EA4CE870BBE2:ABPerson
default	17:23:53.931479-0500	Nexy	0000 Contact: BC75C771-F624-4E3A-AD7C-60B2F270D59D:ABPerson
default	17:23:53.931490-0500	Nexy	0000 Contact: C9795424-7E48-45EA-BBDF-4E008BDD9978:ABPerson
default	17:23:53.931502-0500	Nexy	0000 Contact: 40A1ED53-5876-46E0-B311-D54958985F34:ABPerson
default	17:23:53.931514-0500	Nexy	0000 Contact: 7E4C40BE-99FF-4182-ACF1-5DF8D2DDBE83:ABPerson
default	17:23:53.931524-0500	Nexy	0000 Contact: 6E048310-6707-4D3C-BD0B-81F080042AD6:ABPerson
default	17:23:53.931536-0500	Nexy	0000 Contact: 7268EB56-C8B9-4982-99B0-A40D08B65BA9:ABPerson
default	17:23:53.931549-0500	Nexy	0000 Contact: 0E2D5908-AAC6-40CB-BFB1-0CE7506D0A99:ABPerson
default	17:23:53.931560-0500	Nexy	0000 Contact: D2628142-CF91-46B0-A289-5CA32977E44D:ABPerson
default	17:23:53.931571-0500	Nexy	0000 Contact: 914E27F4-B07C-487A-BF66-F3CA485B9275:ABPerson
default	17:23:53.931582-0500	Nexy	0000 Contact: D014DC3B-188A-4277-A1D5-FBE211695D60:ABPerson
default	17:23:53.931593-0500	Nexy	0000 Contact: 48C9CC87-0557-4A05-B9B6-9FC3799AA710:ABPerson
default	17:23:53.931607-0500	Nexy	0000 Contact: D19BADAB-1850-4DC5-BEEF-B4D77FFCF312:ABPerson
default	17:23:53.931621-0500	Nexy	0000 Contact: 5F52D0B4-4801-47FD-A2E8-E1EC4C2CFBF7:ABPerson
default	17:23:53.931632-0500	Nexy	0000 Contact: F8F59880-57E4-410D-B266-90532EAA85ED:ABPerson
default	17:23:53.931643-0500	Nexy	0000 Contact: 894EBF35-6AF8-4262-8E87-8394A0235AEA:ABPerson
default	17:23:53.931654-0500	Nexy	0000 Contact: 57AEA313-D5E2-4575-AA16-1A5115913CC7:ABPerson
default	17:23:53.931667-0500	Nexy	0000 Contact: F89D0C36-26A8-41DC-83C9-B4FBE705654B:ABPerson
default	17:23:53.931679-0500	Nexy	0000 Contact: 1B9D8EA6-9499-4BFC-8492-1342D6A1460A:ABPerson
default	17:23:53.931689-0500	Nexy	0000 Contact: 35990211-93E2-4128-9887-673DB78EB237:ABPerson
default	17:23:53.931700-0500	Nexy	0000 Contact: E09D3D05-8D17-403A-BB6D-AE0A7DAC6A91:ABPerson
default	17:23:53.931714-0500	Nexy	0000 Contact: 6947AB19-73BD-4633-9B74-8444F2D5EB48:ABPerson
default	17:23:53.931725-0500	Nexy	0000 Contact: 327524E2-8EE7-43AD-A10C-4D95E5236B33:ABPerson
default	17:23:53.931736-0500	Nexy	0000 Contact: 5C927C23-EC97-4E44-979D-C91168A0225F:ABPerson
default	17:23:53.931747-0500	Nexy	0000 Contact: 3E96739C-79E5-47F2-8D58-297DAFFED273:ABPerson
default	17:23:53.931760-0500	Nexy	0000 Contact: 923B5225-B958-47B8-A994-56D2C6594BC3:ABPerson
default	17:23:53.931771-0500	Nexy	0000 Contact: 71E3945F-552E-4A87-81E7-3B4F6B837FB0:ABPerson
default	17:23:53.931782-0500	Nexy	0000 Contact: 98BB4D37-BA08-403B-863B-EA841E79DDEC:ABPerson
default	17:23:53.931793-0500	Nexy	0000 Contact: 3C958CB9-9822-42CE-908D-E1263845615F:ABPerson
default	17:23:53.931804-0500	Nexy	0000 Contact: 99F6FF83-6AC8-4BB2-A7FB-0E45BF397CE1:ABPerson
default	17:23:53.931816-0500	Nexy	0000 Contact: ECEB9C46-3E9A-4B07-BA0A-83A9F5AC9BD8:ABPerson
default	17:23:53.931828-0500	Nexy	0000 Contact: 2D8CF878-704D-4216-A869-2AA3CE40DC8B:ABPerson
default	17:23:53.931839-0500	Nexy	0000 Contact: D6E1C189-3EE0-4001-BBD7-BA1BAA052DCD:ABPerson
default	17:23:53.931850-0500	Nexy	0000 Contact: 0FB6D688-1124-496D-8A74-936908325AC4:ABPerson
default	17:23:53.931862-0500	Nexy	0000 Contact: 8E63BF2D-7068-4689-AA89-3F14A6D447C7:ABPerson
default	17:23:53.931873-0500	Nexy	0000 Contact: A6A438A5-EBCC-4387-AE2C-974496DF3475:ABPerson
default	17:23:53.931884-0500	Nexy	0000 Contact: A7980BCA-3250-42B1-9819-B7F094FC4046:ABPerson
default	17:23:53.931895-0500	Nexy	0000 Contact: 4C6A56D0-B520-49E0-8E8E-16BA4BC6CC20:ABPerson
default	17:23:53.931906-0500	Nexy	0000 Contact: C0FC9CF3-3693-4D44-981C-6047B6AEE5AB:ABPerson
default	17:23:53.931919-0500	Nexy	0000 Contact: 9436B5EC-36D3-4607-B5EB-7EF577DAA4E1:ABPerson
default	17:23:53.931931-0500	Nexy	0000 Contact: FC8D2904-8F71-4E20-8978-D780134A1143:ABPerson
default	17:23:53.931941-0500	Nexy	0000 Contact: 8E15809F-EDFE-43EB-A729-82985D40BEDD:ABPerson
default	17:23:53.931952-0500	Nexy	0000 Contact: 4CFCE671-0922-422E-84D2-7E3D755B9AA0:ABPerson
default	17:23:53.931965-0500	Nexy	0000 Contact: 97F9A37A-8704-4049-B22E-5464D3555283:ABPerson
default	17:23:53.931976-0500	Nexy	0000 Contact: 5EAB76EB-1518-4AB1-A60F-6440D4E97C67:ABPerson
default	17:23:53.931988-0500	Nexy	0000 Contact: 66AA346D-AFEA-46E3-AB76-B76AB73EEFE6:ABPerson
default	17:23:53.931998-0500	Nexy	0000 Contact: A94FA9D0-8D8F-482E-A1FA-415674AAE3CD:ABPerson
default	17:23:53.932010-0500	Nexy	0000 Contact: E26AEFB0-1D2D-4ED3-B1E2-B7D352747749:ABPerson
default	17:23:53.932023-0500	Nexy	0000 Contact: AE956307-DB6F-4D84-8479-F99A334DD9D9:ABPerson
default	17:23:53.932034-0500	Nexy	0000 Contact: D85CE9F6-4FD9-4FE4-BAC1-3B143BBF015B:ABPerson
default	17:23:53.932044-0500	Nexy	0000 Contact: D86C98C7-EA2A-4783-9D89-B5CCC7F3F76F:ABPerson
default	17:23:53.932056-0500	Nexy	0000 Contact: 9BD95D2C-57F9-41BC-82A1-01276B837DE5:ABPerson
default	17:23:53.932068-0500	Nexy	0000 Contact: D73A9313-DE0F-415F-AEB6-A3064AD4E8D4:ABPerson
default	17:23:53.932079-0500	Nexy	0000 Contact: 0D652AFC-47EC-4A75-8D39-2C5235F7B2D8:ABPerson
default	17:23:53.932090-0500	Nexy	0000 Contact: ACA1A5BD-6656-45E2-BD86-154568B82D42:ABPerson
default	17:23:53.932101-0500	Nexy	0000 Contact: 4EEB39AF-CB99-4D4F-99E0-813379D86B51:ABPerson
default	17:23:53.932111-0500	Nexy	0000 Contact: 37348E4E-8173-4E70-B552-CB72B6A9AF42:ABPerson
default	17:23:53.932123-0500	Nexy	0000 Contact: 3D23A662-D7CC-4235-A90D-B25C77F75FB1:ABPerson
default	17:23:53.932135-0500	Nexy	0000 Contact: F5DA0315-4AD8-41C4-B7CF-81A2E12E2691:ABPerson
default	17:23:53.932147-0500	Nexy	0000 Contact: 61773524-5763-4829-81ED-9B3EFF5744C8:ABPerson
default	17:23:53.932158-0500	Nexy	0000 Contact: 3A8DC04F-FBB6-495A-8E75-D22B3ACFD775:ABPerson
default	17:23:53.932169-0500	Nexy	0000 Contact: 8E1B53A0-CE9F-4B5A-BCD2-6FCBB2FE03C1:ABPerson
default	17:23:53.932182-0500	Nexy	0000 Contact: 927F81A1-D726-4969-8419-5DAAAB376B20:ABPerson
default	17:23:53.932193-0500	Nexy	0000 Contact: 499571CA-8847-4A36-8AFD-700D10BA01B6:ABPerson
default	17:23:53.932204-0500	Nexy	0000 Contact: 687940D3-01D3-4EE6-8DF6-B77137DF4358:ABPerson
default	17:23:53.932214-0500	Nexy	0000 Contact: AC2B4231-8E18-49D2-A6E0-4DAD10C52F8E:ABPerson
default	17:23:53.932225-0500	Nexy	0000 Contact: B9C8A612-D08C-4C98-AFEC-7B492BFFCF09:ABPerson
default	17:23:53.932236-0500	Nexy	0000 Contact: 4DE12C0D-88F3-46EA-AE7A-52A8C97B2642:ABPerson
default	17:23:53.932249-0500	Nexy	0000 Contact: 74E71AB9-12C3-492C-8D90-44002E96E279:ABPerson
default	17:23:53.932264-0500	Nexy	0000 Contact: F06E384F-51AB-4945-8C9A-CDDA3D1F1726:ABPerson
default	17:23:53.932275-0500	Nexy	0000 Contact: B4392798-7C17-4630-9433-A03FD74A67B6:ABPerson
default	17:23:53.932286-0500	Nexy	0000 Contact: 81B63730-E89B-4309-B937-6526BC363BE9:ABPerson
default	17:23:53.932297-0500	Nexy	0000 Contact: 67260B0D-B185-469D-A099-1F276E9003E9:ABPerson
default	17:23:53.932311-0500	Nexy	0000 Contact: 523939B5-07BC-4BA9-8827-8E5DE74ABD59:ABPerson
default	17:23:53.932324-0500	Nexy	0000 Contact: 448593D9-FFE0-4A5E-85CF-951EBD64FD34:ABPerson
default	17:23:53.932336-0500	Nexy	0000 Contact: 39E0059F-CE32-4A7F-8412-CBB5B8512D91:ABPerson
default	17:23:53.932348-0500	Nexy	0000 Contact: BD79F9BE-48FE-4B17-A966-4900444CB4BE:ABPerson
default	17:23:53.932358-0500	Nexy	0000 Contact: CB117BD9-26BB-482F-BE1D-474050D4F877:ABPerson
default	17:23:53.932369-0500	Nexy	0000 Contact: 1BE44750-F897-4471-B2BB-23F1750F6052:ABPerson
default	17:23:53.932380-0500	Nexy	0000 Contact: F521BF7D-BEA0-4970-8ABB-0D36D0C55CFB:ABPerson
default	17:23:53.932391-0500	Nexy	0000 Contact: B31F68AA-132A-4764-BF9C-07AFF1DFEBE9:ABPerson
default	17:23:53.932403-0500	Nexy	0000 Contact: BFC74FBC-8459-4E5C-926D-CA8CB584E493:ABPerson
default	17:23:53.932415-0500	Nexy	0000 Contact: 513D3922-7269-4052-92B9-A5DDC7F20D85:ABPerson
default	17:23:53.932429-0500	Nexy	0000 Contact: 1680643C-880B-4F66-A23A-54553511F91E:ABPerson
default	17:23:53.932440-0500	Nexy	0000 Contact: AC09AA75-399F-4388-B06D-B36195539921:ABPerson
default	17:23:53.932462-0500	Nexy	0000 Contact: 905AEE60-BF17-4861-8B9D-D8A7C93CA851:ABPerson
default	17:23:53.932476-0500	Nexy	0000 Contact: 605EC366-1BE6-4728-AF4F-35065DDE105E:ABPerson
default	17:23:53.932487-0500	Nexy	0000 Contact: 2E5AC2EB-1D50-48E4-A733-1565B7FBD9B0:ABPerson
default	17:23:53.932498-0500	Nexy	0000 Contact: 8DBBC6C7-2A3B-452A-A683-96B213129365:ABPerson
default	17:23:53.932509-0500	Nexy	0000 Contact: D1ABDE8F-AB3A-4A78-B366-8122520E469C:ABPerson
default	17:23:53.932522-0500	Nexy	0000 Contact: 2BBC7823-B462-47BC-97A1-FAF56A6CD6D4:ABPerson
default	17:23:53.932533-0500	Nexy	0000 Contact: CBBBAAFD-0C8A-4928-B6C5-104BD483B756:ABPerson
default	17:23:53.932543-0500	Nexy	0000 Contact: 7B546412-E513-4FAC-8F04-5B93F8284CD9:ABPerson
default	17:23:53.932558-0500	Nexy	0000 Contact: BEDFD270-E6D5-4BD4-9396-F461E76A3D6D:ABPerson
default	17:23:53.932569-0500	Nexy	0000 Contact: DFF04280-7038-4F29-96DF-CE1264E33F45:ABPerson
default	17:23:53.932580-0500	Nexy	0000 Contact: DA723208-FBEF-435F-9D7D-AF23C3292A04:ABPerson
default	17:23:53.932591-0500	Nexy	0000 Contact: 689B7484-1008-4903-8E58-C16D6135D1BE:ABPerson
default	17:23:53.932602-0500	Nexy	0000 Contact: 2EBB3BBB-AA1B-44AB-AEB2-507047DFB1BF:ABPerson
default	17:23:53.932614-0500	Nexy	0000 Contact: 2C4816A3-74B3-44EE-8613-D4A9EA487364:ABPerson
default	17:23:53.932625-0500	Nexy	0000 Contact: 327FE41D-07EB-426D-B40A-C41E6414A032:ABPerson
default	17:23:53.932636-0500	Nexy	0000 Contact: 661E42B6-4641-42DC-ADAD-F2F4F64E9A7F:ABPerson
default	17:23:53.932647-0500	Nexy	0000 Contact: 5B3F5B1B-AEB4-49F2-9295-98A6D2E90DF3:ABPerson
default	17:23:53.932658-0500	Nexy	0000 Contact: 3B9A0F65-3862-4239-9B4C-22A3937CB3E3:ABPerson
default	17:23:53.932671-0500	Nexy	0000 Contact: 1F5296B1-D8A8-4DEE-A3AC-4F6FF8EB8592:ABPerson
default	17:23:53.932682-0500	Nexy	0000 Contact: 83367917-4C48-420D-BED6-953D5D799BA3:ABPerson
default	17:23:53.932693-0500	Nexy	0000 Contact: CB81A645-AA3F-4E01-A5E8-7FFB1DE784B8:ABPerson
default	17:23:53.932704-0500	Nexy	0000 Contact: 76C1E860-76F6-46A7-AE8B-0B8D533979A1:ABPerson
default	17:23:53.932715-0500	Nexy	0000 Contact: 38D87E84-8FFA-4644-89BB-3B2C64683F25:ABPerson
default	17:23:53.932727-0500	Nexy	0000 Contact: BFC89011-6208-402B-902D-227391CF84D7:ABPerson
default	17:23:53.932738-0500	Nexy	0000 Contact: AE1E272C-12CF-4D37-AA16-321C66EB1922:ABPerson
default	17:23:53.932749-0500	Nexy	0000 Contact: 37AF5276-1B9C-4873-9D80-6BD7C5AE160B:ABPerson
default	17:23:53.932760-0500	Nexy	0000 Contact: 873FBA93-2932-4885-9ABA-B766E56EF823:ABPerson
default	17:23:53.932771-0500	Nexy	0000 Contact: DA14AB47-A56B-4F79-A505-4A5F3CF9709B:ABPerson
default	17:23:53.932784-0500	Nexy	0000 Contact: 5DBDC986-75E3-45D5-BDAC-840F64A095F3:ABPerson
default	17:23:53.932795-0500	Nexy	0000 Contact: 7E2E667C-A7D1-4A88-9C92-C2F38557DF00:ABPerson
default	17:23:53.932807-0500	Nexy	0000 Contact: 5307FC68-117A-42FB-92AA-DFB24F94E71D:ABPerson
default	17:23:53.932817-0500	Nexy	0000 Contact: 5F493737-ED28-4B1F-8903-5BA4CE98E525:ABPerson
default	17:23:53.932832-0500	Nexy	0000 Contact: 581AB38B-88DC-4442-B96C-20827400BCDB:ABPerson
default	17:23:53.932842-0500	Nexy	0000 Contact: E7A269EB-3583-4C11-9FA2-A805E372821C:ABPerson
default	17:23:53.932853-0500	Nexy	0000 Contact: 17A33554-E561-4BBD-9CEB-2A42D78570CB:ABPerson
default	17:23:53.932864-0500	Nexy	0000 Contact: B6294A95-D955-4DE1-981A-1C81A88B3C77:ABPerson
default	17:23:53.932876-0500	Nexy	0000 Contact: 2775B95B-E344-4E6E-860A-2E7C048D2F1D:ABPerson
default	17:23:53.932889-0500	Nexy	0000 Contact: C811339F-FA52-4CA4-B33E-D0F308EB497B:ABPerson
default	17:23:53.932900-0500	Nexy	0000 Contact: 3EBCE39A-CFA0-4AE5-A027-E77300906D8C:ABPerson
default	17:23:53.932913-0500	Nexy	0000 Contact: EE34E8D6-8FA8-43EA-956D-B93BBAEE1A85:ABPerson
default	17:23:53.932924-0500	Nexy	0000 Contact: 9502BE8E-CE6C-45C1-B06E-06F25C1B2DB2:ABPerson
default	17:23:53.932934-0500	Nexy	0000 Contact: CB72BAE7-75D4-4B69-B8B1-6F54BA25195A:ABPerson
default	17:23:53.932946-0500	Nexy	0000 Contact: 8ABDA833-5BB8-43D2-9DD4-D9977041708F:ABPerson
default	17:23:53.932957-0500	Nexy	0000 Contact: BC7FC3F8-6E58-42C6-8D38-58B4E05E74D8:ABPerson
default	17:23:53.932969-0500	Nexy	0000 Contact: 8C9E4B42-EDDD-4DA5-8291-79608D7118FD:ABPerson
default	17:23:53.932980-0500	Nexy	0000 Contact: 88A354D2-628D-4BBD-A9D2-4025114C2B74:ABPerson
default	17:23:53.932991-0500	Nexy	0000 Contact: D671E4A8-5C78-48DB-9F39-C9F55D0773F0:ABPerson
default	17:23:53.933002-0500	Nexy	0000 Contact: B55652C2-FF9A-492E-9E74-59BF77FF7657:ABPerson
default	17:23:53.933015-0500	Nexy	0000 Contact: D40BEEF6-659C-4640-8883-A886679E7683:ABPerson
default	17:23:53.933026-0500	Nexy	0000 Contact: AC0B1878-D813-4721-AF37-E5AD5DF1D1F6:ABPerson
default	17:23:53.933037-0500	Nexy	0000 Contact: 2501625C-D3F0-448F-BE59-758CB4781991:ABPerson
default	17:23:53.933048-0500	Nexy	0000 Contact: 95793C06-46A7-463F-B79D-BD4828AA82E5:ABPerson
default	17:23:53.933059-0500	Nexy	0000 Contact: 39FB6543-CE8F-4850-B087-CB9BC9D83CD1:ABPerson
default	17:23:53.933072-0500	Nexy	0000 Contact: 4899EBC6-6B1B-4110-ACC0-42C6281F11F0:ABPerson
default	17:23:53.933082-0500	Nexy	0000 Contact: 2152007E-EC7F-40ED-A920-334BFEE05F62:ABPerson
default	17:23:53.933094-0500	Nexy	0000 Contact: E5FB73BD-A112-4CB1-A44C-4AE9AA8A7FD9:ABPerson
default	17:23:53.933106-0500	Nexy	0000 Contact: 9DF4B53B-8E66-438F-A541-31A6AC43028E:ABPerson
default	17:23:53.933119-0500	Nexy	0000 Contact: ED52C6FA-B011-454D-BF73-CD97015FEDF8:ABPerson
default	17:23:53.933130-0500	Nexy	0000 Contact: 637D6BED-2C4A-4F5E-9BF9-E5A8854E4DF1:ABPerson
default	17:23:53.933140-0500	Nexy	0000 Contact: 763CD797-4630-439F-982D-34ACFA2E7238:ABPerson
default	17:23:53.933151-0500	Nexy	0000 Contact: DE4A7BAA-4835-447E-9B59-F863ACBFA092:ABPerson
default	17:23:53.933162-0500	Nexy	0000 Contact: FE3ED792-5C16-4CA6-AD68-BBDFDF93EAC3:ABPerson
default	17:23:53.933175-0500	Nexy	0000 Contact: F5F336E5-374B-4E45-B851-690629571134:ABPerson
default	17:23:53.933186-0500	Nexy	0000 Contact: 00E52FC0-B1F1-47C4-A4E2-351A2927B2AC:ABPerson
default	17:23:53.933202-0500	Nexy	0000 Contact: 5AA6919D-04C9-470A-99B9-9FB0D437DA6A:ABPerson
default	17:23:53.933209-0500	Nexy	0000 Contact: 1FC22462-8E84-43E6-8F68-5D141CC903D6:ABPerson
default	17:23:53.933222-0500	Nexy	0000 Contact: 379EEF06-D880-4C4C-81B4-19232497B238:ABPerson
default	17:23:53.933233-0500	Nexy	0000 Contact: 9AA12C79-AC0F-40D8-82D4-7D1D1B6024D4:ABPerson
default	17:23:53.933243-0500	Nexy	0000 Contact: B584C21D-4B54-4F37-A1B1-B5EF3AEC170C:ABPerson
default	17:23:53.933254-0500	Nexy	0000 Contact: D2940461-BB6C-4224-8218-88019B5DB07D:ABPerson
default	17:23:53.933267-0500	Nexy	0000 Contact: 734CE2EC-7CFA-4475-B601-8F5A0EDC5AFC:ABPerson
default	17:23:53.933278-0500	Nexy	0000 Contact: 693CFFC7-F57A-478E-BBA2-CB65EB6C5425:ABPerson
default	17:23:53.933289-0500	Nexy	0000 Contact: 522D9347-0C39-4479-9A87-99551E9F992C:ABPerson
default	17:23:53.933301-0500	Nexy	0000 Contact: BC6A800E-2E2E-4B39-B37E-6639FBEE75EF:ABPerson
default	17:23:53.933312-0500	Nexy	0000 Contact: 4B6CD270-FA88-4F64-9F96-22BB79CBD541:ABPerson
default	17:23:53.933322-0500	Nexy	0000 Contact: 77ED343F-8BF8-4BFD-A0F9-901367A608BC:ABPerson
default	17:23:53.933334-0500	Nexy	0000 Contact: 37D2B9B0-053A-474C-BE44-09B4453D4050:ABPerson
default	17:23:53.933346-0500	Nexy	0000 Contact: 62B0EB86-C5BA-495C-9E28-535D2EF0354A:ABPerson
default	17:23:53.933357-0500	Nexy	0000 Contact: 670ECAAE-6CD8-4A3A-8EA6-614A11174BD6:ABPerson
default	17:23:53.933367-0500	Nexy	0000 Contact: A45DAD74-F719-4D46-9EA6-6DFEEF650375:ABPerson
default	17:23:53.933381-0500	Nexy	0000 Contact: B7008B2E-FA86-42D5-8656-CE248026D27E:ABPerson
default	17:23:53.933393-0500	Nexy	0000 Contact: 66B98153-BD62-4141-BD1F-DADC79D75A4F:ABPerson
default	17:23:53.933404-0500	Nexy	0000 Contact: FA38B842-F2F3-4FED-B33D-A5010D4304B0:ABPerson
default	17:23:53.933415-0500	Nexy	0000 Contact: 14743D61-F4A1-4392-9E1B-26918104BF14:ABPerson
default	17:23:53.933428-0500	Nexy	0000 Contact: B2D8BD53-113A-4BF0-91CA-D5DEB28674B5:ABPerson
default	17:23:53.933439-0500	Nexy	0000 Contact: 64B8389E-447B-4C35-B14E-8146CA91B47B:ABPerson
default	17:23:53.933449-0500	Nexy	0000 Contact: 3FF7B769-C140-4D4C-B32F-6B8F440DE2D8:ABPerson
default	17:23:53.933460-0500	Nexy	0000 Contact: 1F6916A9-1A84-48F4-B955-59E227D8C9DF:ABPerson
default	17:23:53.933471-0500	Nexy	0000 Contact: F334D708-4AFD-4933-99D2-F8F1D76176A9:ABPerson
default	17:23:53.933482-0500	Nexy	0000 Contact: 626EC525-A04F-4FBF-8FEE-BA93D0436808:ABPerson
default	17:23:53.933492-0500	Nexy	0000 Contact: A4D2F572-E7C4-45EE-AE51-345CC039C259:ABPerson
default	17:23:53.933506-0500	Nexy	0000 Contact: 014698F9-DA96-407C-A1B8-DEC6B51A33F6:ABPerson
default	17:23:53.933517-0500	Nexy	0000 Contact: F5B2550B-7B88-4DCE-A7A3-1B10271953FC:ABPerson
default	17:23:53.933527-0500	Nexy	0000 Contact: 1EAD0F34-5228-476C-B4EB-ACD91782DD85:ABPerson
default	17:23:53.933538-0500	Nexy	0000 Contact: F7E0D308-2E0A-49CC-849B-C883B6F8730F:ABPerson
default	17:23:53.933551-0500	Nexy	0000 Contact: 145A9F4B-B827-49A2-B108-81359AEE2B8F:ABPerson
default	17:23:53.933562-0500	Nexy	0000 Contact: 0AA46F26-7B70-4230-AC5B-AFDC6D2DD22B:ABPerson
default	17:23:53.933573-0500	Nexy	0000 Contact: AE79C4EC-990E-4BA3-913E-7C842EB653EF:ABPerson
default	17:23:53.933583-0500	Nexy	0000 Contact: C05B9998-16AE-4F34-8E4F-817C3D9B8EC6:ABPerson
default	17:23:53.933594-0500	Nexy	0000 Contact: 7F27B5B3-D0F5-483F-89C6-8B9931845E1F:ABPerson
default	17:23:53.933604-0500	Nexy	0000 Contact: 84E58627-BCB4-42D0-BDFA-EE699F5FBDD8:ABPerson
default	17:23:53.933615-0500	Nexy	0000 Contact: 2513C61B-7EFC-4A92-88AB-DF9479B99E6A:ABPerson
default	17:23:53.933626-0500	Nexy	0000 Contact: 84CFF237-6D8B-4620-9181-D1B4BB0809EE:ABPerson
default	17:23:53.933638-0500	Nexy	0000 Contact: 0BFD29DC-60C9-4B71-9D65-4ADA47472277:ABPerson
default	17:23:53.933648-0500	Nexy	0000 Contact: 69998C87-7B1A-45AA-ABB3-2D84128DD9EE:ABPerson
default	17:23:53.933660-0500	Nexy	0000 Contact: A7C3EEE8-11F8-4C0C-848D-3AC49C688578:ABPerson
default	17:23:53.933672-0500	Nexy	0000 Contact: A64A1E7E-C301-454E-A9A9-D685C82EF693:ABPerson
default	17:23:53.933682-0500	Nexy	0000 Contact: 91C379A3-DE9D-456A-A6AD-0F1F963582E7:ABPerson
default	17:23:53.933696-0500	Nexy	0000 Contact: 6ACE0F8B-171F-450C-83E2-081B5F26881E:ABPerson
default	17:23:53.933706-0500	Nexy	0000 Contact: AC074808-2D0D-48F8-8B23-3F0CA6D51D26:ABPerson
default	17:23:53.933717-0500	Nexy	0000 Contact: F4F5D7A0-BC90-4C27-BBCE-BE969384F1C0:ABPerson
default	17:23:53.933727-0500	Nexy	0000 Contact: 1ABDAACE-D0B1-4F9B-96D1-DC2C524CE1C6:ABPerson
default	17:23:53.933739-0500	Nexy	0000 Contact: 43585BE0-779A-4596-A518-8D5E4ADB3D19:ABPerson
default	17:23:53.933751-0500	Nexy	0000 Contact: 67051D02-C728-4665-B5FC-4F1B269F02BD:ABPerson
default	17:23:53.933763-0500	Nexy	0000 Contact: 4473A678-C9E7-4D62-84E0-753DF60913D1:ABPerson
default	17:23:53.933773-0500	Nexy	0000 Contact: D56AB0C8-7D93-4C12-B5B5-95E0DC8F2240:ABPerson
default	17:23:53.933784-0500	Nexy	0000 Contact: 9579BC4C-AF0F-4D50-A15C-319AACBFC2A5:ABPerson
default	17:23:53.933795-0500	Nexy	0000 Contact: 4BE75408-838B-4CDE-A088-588AE1E78C84:ABPerson
default	17:23:53.933808-0500	Nexy	0000 Contact: C87BCEEB-0D99-4BCD-B837-B1790FEF5A35:ABPerson
default	17:23:53.933820-0500	Nexy	0000 Contact: 11C070CC-DE86-43A2-AC2E-BD5D0E666C75:ABPerson
default	17:23:53.933831-0500	Nexy	0000 Contact: 1BC6C401-C80C-443B-86A1-DE142581F385:ABPerson
default	17:23:53.933842-0500	Nexy	0000 Contact: 0A5F3B64-AC92-4AC6-A80F-C08A85FC26AF:ABPerson
default	17:23:53.933854-0500	Nexy	0000 Contact: 87E03F74-07D8-4C64-9DA7-D99DC9CA7445:ABPerson
default	17:23:53.933865-0500	Nexy	0000 Contact: 94F55698-438B-4D8C-9CA0-71DDFD6367D5:ABPerson
default	17:23:53.933876-0500	Nexy	0000 Contact: 15748416-FFAD-4D4B-B4AF-076BF4C1B672:ABPerson
default	17:23:53.933887-0500	Nexy	0000 Contact: 74B3EEDB-C36E-4B91-AAF8-A7D433556574:ABPerson
default	17:23:53.933901-0500	Nexy	0000 Contact: 951A73EB-D920-4420-8258-81B51426DEF7:ABPerson
default	17:23:53.933912-0500	Nexy	0000 Contact: 6B194999-7994-412B-8F16-25AB9317AAB4:ABPerson
default	17:23:53.933923-0500	Nexy	0000 Contact: 2EC20223-DCBF-406A-9D39-5F1D770A8BC4:ABPerson
default	17:23:53.933934-0500	Nexy	0000 Contact: 1562F9E4-94A8-48AB-BF2B-C1EB0C1BE5A4:ABPerson
default	17:23:53.933945-0500	Nexy	0000 Contact: F6C3B173-427B-4C46-AA87-E8AA5B4E4C47:ABPerson
default	17:23:53.933957-0500	Nexy	0000 Contact: 5340250A-2C48-4FA9-9A43-1E9438F76204:ABPerson
default	17:23:53.933968-0500	Nexy	0000 Contact: 910FA8BF-611B-4C75-9EB0-5F2EFD716C1F:ABPerson
default	17:23:53.933979-0500	Nexy	0000 Contact: 08B0DE06-259B-449C-B66B-FFBA5AB8D812:ABPerson
default	17:23:53.933990-0500	Nexy	0000 Contact: 3C20B58D-2CA5-485E-A9A6-F77768532665:ABPerson
default	17:23:53.934001-0500	Nexy	0000 Contact: 6524FEA4-C209-419D-8A29-C534C9D1627C:ABPerson
default	17:23:53.934012-0500	Nexy	0000 Contact: 9A063C74-04C9-4AD8-AB36-6C8734D43E2D:ABPerson
default	17:23:53.934025-0500	Nexy	0000 Contact: AEAB4360-3F45-4F6B-9F79-B5D0B38B9A81:ABPerson
default	17:23:53.934036-0500	Nexy	0000 Contact: 044C1B1D-1FA6-46AA-B69A-444A8B442B7C:ABPerson
default	17:23:53.934047-0500	Nexy	0000 Contact: 67E45E85-4716-4AD1-9FE5-0DD5A68A6D7E:ABPerson
default	17:23:53.934058-0500	Nexy	0000 Contact: 4ADAEDF0-6C5E-4C06-9C0A-B8594FF82BDA:ABPerson
default	17:23:53.934070-0500	Nexy	0000 Contact: DA46038B-56C6-4414-9F21-077B66E8C91C:ABPerson
default	17:23:53.934082-0500	Nexy	0000 Contact: 75FADFA1-F7C3-437C-8B58-DAA8A4B54442:ABPerson
default	17:23:53.934092-0500	Nexy	0000 Contact: B6E3347E-7AC5-41E7-ACA5-D2CEF067A1CA:ABPerson
default	17:23:53.934104-0500	Nexy	0000 Contact: 4EFFE145-11B7-42A5-822C-A4BAB5D83906:ABPerson
default	17:23:53.934114-0500	Nexy	0000 Contact: EAB298D5-435C-4D40-83A7-2C55723A0BFD:ABPerson
default	17:23:53.934127-0500	Nexy	0000 Contact: B0D78C24-E588-4901-88A7-6B1BB429B840:ABPerson
default	17:23:53.934138-0500	Nexy	0000 Contact: 1CB20B90-D9D5-4C8F-9AB0-DAA44D00BDD4:ABPerson
default	17:23:53.934149-0500	Nexy	0000 Contact: 527699A5-81B2-4D67-AEED-D6EED43F9044:ABPerson
default	17:23:53.934159-0500	Nexy	0000 Contact: CB5E53D4-5C8B-43F5-94AF-6B7D8BA543FD:ABPerson
default	17:23:53.934173-0500	Nexy	0000 Contact: 04598613-6173-4B93-B8E7-285BC4F3D8E8:ABPerson
default	17:23:53.934182-0500	Nexy	0000 Contact: ADD86E64-7CF0-4510-AD39-66BD6BD079BC:ABPerson
default	17:23:53.934195-0500	Nexy	0000 Contact: 32788248-0C60-4FEA-85E7-FA758B61DD1D:ABPerson
default	17:23:53.934206-0500	Nexy	0000 Contact: AA1A4C67-F155-4EE5-9010-31149EE1E39C:ABPerson
default	17:23:53.934216-0500	Nexy	0000 Contact: 961DCC0E-AAAD-4D01-9678-0A7621D2AFB0:ABPerson
default	17:23:53.934227-0500	Nexy	0000 Contact: 66B11FA1-1DE3-48ED-A067-665E7467482A:ABPerson
default	17:23:53.934238-0500	Nexy	0000 Contact: F5182AF8-32D2-40E6-993D-C0489EBC89E4:ABPerson
default	17:23:53.934250-0500	Nexy	0000 Contact: 0D60E67B-3CE2-4AA5-A3A7-78022070A092:ABPerson
default	17:23:53.934261-0500	Nexy	0000 Contact: 3AAC52F8-BF6B-4AF2-BB6D-03A1310B24E5:ABPerson
default	17:23:53.934272-0500	Nexy	0000 Contact: CE41D8E9-94C5-4D35-9B34-26811B12C410:ABPerson
default	17:23:53.934283-0500	Nexy	0000 Contact: F13294CA-A587-43D6-B693-775C43EE2187:ABPerson
default	17:23:53.934297-0500	Nexy	0000 Contact: 89FE41AC-035D-4508-9B13-A7A61A86A77D:ABPerson
default	17:23:53.934308-0500	Nexy	0000 Contact: 31E21B40-260C-42C1-9677-7C97CC1B201D:ABPerson
default	17:23:53.934319-0500	Nexy	0000 Contact: F0D80C37-667F-495B-83CE-9F5BF918C730:ABPerson
default	17:23:53.934330-0500	Nexy	0000 Contact: 06259E4E-E4B7-4654-BF6B-33F4F0FCB23A:ABPerson
default	17:23:53.934341-0500	Nexy	0000 Contact: 55FDAC9D-D436-4535-BE96-A71F62A0AF9E:ABPerson
default	17:23:53.934353-0500	Nexy	0000 Contact: F790FA9D-7B36-4AEA-8012-0BDEED54CF62:ABPerson
default	17:23:53.934365-0500	Nexy	0000 Contact: 276E4846-224E-4119-AB43-FE2E963D133E:ABPerson
default	17:23:53.934376-0500	Nexy	0000 Contact: DB25F4B4-E218-42CD-959A-C88098B61FD4:ABPerson
default	17:23:53.934386-0500	Nexy	0000 Contact: 7E8FC80C-607C-43E2-BF92-C5FCC8403326:ABPerson
default	17:23:53.934397-0500	Nexy	0000 Contact: 6BE779B6-7D7F-4DB2-A36A-3696730156FE:ABPerson
default	17:23:53.934408-0500	Nexy	0000 Contact: A45B54DD-B6FC-4653-84D5-0757EB2F2ED6:ABPerson
default	17:23:53.934422-0500	Nexy	0000 Contact: 8605C2C8-7153-4112-9036-FAA472B7FD44:ABPerson
default	17:23:53.934434-0500	Nexy	0000 Contact: CD272F42-E884-45F1-84C3-CFD3A0B1BF35:ABPerson
default	17:23:53.934446-0500	Nexy	0000 Contact: 4D2116D6-A645-48BB-B220-E9ED03C71748:ABPerson
default	17:23:53.934457-0500	Nexy	0000 Contact: B502B3DD-9E9D-4150-B4A9-4872364793EF:ABPerson
default	17:23:53.934468-0500	Nexy	0000 Contact: 0C360F68-EDE2-457E-AC4B-ACE762AD5BD0:ABPerson
default	17:23:53.934478-0500	Nexy	0000 Contact: FF4175C6-26DF-47BC-BF00-2E75EEE8B1FD:ABPerson
default	17:23:53.934489-0500	Nexy	0000 Contact: 09A457F3-A9F4-4F24-9B11-9FA58D4C1508:ABPerson
default	17:23:53.934503-0500	Nexy	0000 Contact: B89DEF47-D413-46AD-BAEA-7D496DD46FB1:ABPerson
default	17:23:53.934514-0500	Nexy	0000 Contact: 3598E3CB-8A76-4D70-AC49-D3EB37CA2029:ABPerson
default	17:23:53.934525-0500	Nexy	0000 Contact: AA991FC9-EB3D-43B4-8CBD-8E604A09B637:ABPerson
default	17:23:53.934537-0500	Nexy	0000 Contact: CC5195D6-422A-4FB7-B9EE-A2A04E601EC0:ABPerson
default	17:23:53.934550-0500	Nexy	0000 Contact: B569062E-A03D-4DD9-A53C-5D2D8D57CB4B:ABPerson
default	17:23:53.934561-0500	Nexy	0000 Contact: 73B6BD20-2014-4F01-90D9-4428F13B690A:ABPerson
default	17:23:53.934571-0500	Nexy	0000 Contact: AA3A3E50-90A8-4525-8DAA-B8B4FADD18DA:ABPerson
default	17:23:53.934582-0500	Nexy	0000 Contact: 3BAE7091-1579-47D0-B90D-0D3CF681C569:ABPerson
default	17:23:53.934595-0500	Nexy	0000 Contact: 56A226DF-9ECE-4143-BA65-8AD0B646C7CB:ABPerson
default	17:23:53.934607-0500	Nexy	0000 Contact: 50F1ED96-0C6B-4F81-AA14-43DC6EBECD59:ABPerson
default	17:23:53.934636-0500	Nexy	0000 Contact: 5A494BDA-3B74-4B7B-92A5-ADDBE7FB8C87:ABPerson
default	17:23:53.934663-0500	Nexy	0000 Contact: 6BD609FD-5007-4D59-A4EF-493CADDB85B2:ABPerson
default	17:23:53.934678-0500	Nexy	0000 Contact: 7E64D4B3-BC6D-4959-B7A0-E823B049142C:ABPerson
default	17:23:53.934691-0500	Nexy	0000 Contact: 621AF0D1-3352-4F82-9C69-D6B0F8D4F5A9:ABPerson
default	17:23:53.934704-0500	Nexy	0000 Contact: 4E051A3F-F33F-42F6-A635-4F6B6FEFCFB2:ABPerson
default	17:23:53.934715-0500	Nexy	0000 Contact: 30F7C290-B84E-45EF-8777-D14EBB9D4BB1:ABPerson
default	17:23:53.934726-0500	Nexy	0000 Contact: B489EA28-72B0-4D87-8E65-2FCC5266CCBB:ABPerson
default	17:23:53.934737-0500	Nexy	0000 Contact: E5C00A28-C49D-4782-B544-D726CFE29EF0:ABPerson
default	17:23:53.934750-0500	Nexy	0000 Contact: DA65C871-7E16-4359-B34C-C5906692C623:ABPerson
default	17:23:53.934761-0500	Nexy	0000 Contact: 5BAFBA23-8FAE-41B7-86D6-A6B3DB070404:ABPerson
default	17:23:53.934773-0500	Nexy	0000 Contact: EA0D316B-758E-4C59-B0A6-6FFB7AD3E09F:ABPerson
default	17:23:53.934786-0500	Nexy	0000 Contact: 9BD347CB-8966-4118-92F7-D6D42F5F8C7C:ABPerson
default	17:23:53.934824-0500	Nexy	0000 Contact: 018F45A5-C534-4FC0-871A-DB5567A8D78E:ABPerson
default	17:23:53.934839-0500	Nexy	0000 Contact: 9FC18618-FB9D-4960-8474-07F6A0D062F8:ABPerson
default	17:23:53.934850-0500	Nexy	0000 Contact: C8BDDDAE-C009-4DB9-B3FC-01F3B16C6D25:ABPerson
default	17:23:53.934863-0500	Nexy	0000 Contact: 1D0198ED-A6C3-4B64-AA1A-2E8A8C4A0172:ABPerson
default	17:23:53.934875-0500	Nexy	0000 Contact: 3BD67570-1034-422C-85A2-6F28BE24C33A:ABPerson
default	17:23:53.934887-0500	Nexy	0000 Contact: D75A5B27-BD0C-4D34-AC6B-FC2822769519:ABPerson
default	17:23:53.934900-0500	Nexy	0000 Contact: 6B5F7DDD-1E04-453D-8539-4B54A251117A:ABPerson
default	17:23:53.934911-0500	Nexy	0000 Contact: 49E369CD-B10E-4CD5-B030-5393AB2ADE18:ABPerson
default	17:23:53.934923-0500	Nexy	0000 Contact: A9AB0613-621A-427C-9150-83893BA072C5:ABPerson
default	17:23:53.934936-0500	Nexy	0000 Contact: 9B8281D5-C780-436F-988A-96C01722B038:ABPerson
default	17:23:53.934957-0500	Nexy	0000 FINISH (19.3 ms)
default	17:23:54.035454-0500	ControlCenter	[app<application.com.nexy.assistant.54878181.54878190>:21340] Workspace state did change: BG-Active[40] --> XX-None[0] (assertion dropped).
default	17:23:54.035552-0500	runningboardd	Invalidating assertion 400-615-17234 (target:[app<application.com.nexy.assistant.54878181.54878190(501)>:21340]) from originator [osservice<com.apple.controlcenter(501)>:615]
default	17:23:54.136710-0500	runningboardd	[app<application.com.nexy.assistant.54878181.54878190(501)>:21340] Ignoring jetsam update because this process is not memory-managed
default	17:23:54.136722-0500	runningboardd	[app<application.com.nexy.assistant.54878181.54878190(501)>:21340] Ignoring suspend because this process is not lifecycle managed
default	17:23:54.136733-0500	runningboardd	[app<application.com.nexy.assistant.54878181.54878190(501)>:21340] Ignoring GPU update because this process is not GPU managed
default	17:23:54.136754-0500	runningboardd	[app<application.com.nexy.assistant.54878181.54878190(501)>:21340] Ignoring memory limit update because this process is not memory-managed
default	17:23:54.139830-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.54878181.54878190(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	17:23:54.140378-0500	ControlCenter	Received state update for 21340 (app<application.com.nexy.assistant.54878181.54878190(501)>, running-active-NotVisible
default	17:23:54.140893-0500	gamepolicyd	Received state update for 21340 (app<application.com.nexy.assistant.54878181.54878190(501)>, running-active-NotVisible
default	17:23:54.325587-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.54878181.54878190(501)>:21340] from originator [osservice<com.apple.WindowServer(88)>:391] with description <RBSAssertionDescriptor| "AppDrawing" ID:400-391-17238 target:21340 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"AppDrawing" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	17:23:54.325740-0500	runningboardd	Assertion 400-391-17238 (target:[app<application.com.nexy.assistant.54878181.54878190(501)>:21340]) will be created as active
default	17:23:54.326370-0500	runningboardd	[app<application.com.nexy.assistant.54878181.54878190(501)>:21340] Ignoring jetsam update because this process is not memory-managed
default	17:23:54.326390-0500	runningboardd	[app<application.com.nexy.assistant.54878181.54878190(501)>:21340] Ignoring suspend because this process is not lifecycle managed
default	17:23:54.326409-0500	runningboardd	[app<application.com.nexy.assistant.54878181.54878190(501)>:21340] Ignoring GPU update because this process is not GPU managed
default	17:23:54.326442-0500	runningboardd	[app<application.com.nexy.assistant.54878181.54878190(501)>:21340] Ignoring memory limit update because this process is not memory-managed
default	17:23:54.332716-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.54878181.54878190(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	17:23:54.333333-0500	ControlCenter	Received state update for 21340 (app<application.com.nexy.assistant.54878181.54878190(501)>, running-active-NotVisible
default	17:23:54.333575-0500	gamepolicyd	Received state update for 21340 (app<application.com.nexy.assistant.54878181.54878190(501)>, running-active-NotVisible
default	17:23:54.690903-0500	WindowServer	0[outside of RPC]: Process death: 0x0-0x1eb1eb (Nexy) connectionID: FE583 pid: 21340 in session 0x101
default	17:23:54.690980-0500	WindowServer	<BSCompoundAssertion:0x830c11580> ([FocusManager:257]-deferringPolicyEvaluationSuppression) acquire for reason:process death - 0x0-0x1eb1eb (Nexy) acq:0x8322fe6a0 count:1
default	17:23:54.692279-0500	audiomxd	  ServerSessionManager.mm:478   { "action":"destroy_session", "session":{"ID":"0x1f4029","name":"Nexy(21340)"}, "details":null }
default	17:23:54.692358-0500	audiomxd	AudioApplicationInfoImpl.mm:690   Successfully removed session 0x1f4029 from AudioApp, recording state unchanged (app: {"name":"[implicit] Nexy","pid":21340})
default	17:23:54.692384-0500	audiomxd	  ServerSessionManager.mm:1086  destroy audio app instance since was created implicitly by session creation and all sessions now gone (audio app: {"name":"[implicit] Nexy","pid":21340})
default	17:23:54.693077-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 42, PID = 21340, Name = sid:0x1f4029, Nexy(21340), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	17:23:54.693238-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 42, PID = 21340, Name = sid:0x1f4029, Nexy(21340), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	17:23:54.692588-0500	ControlCenter	[app<application.com.nexy.assistant.54878181.54878190>:21340] Workspace connection invalidated.
default	17:23:54.692666-0500	ControlCenter	[app<application.com.nexy.assistant.54878181.54878190>:21340] Now flagged as pending exit for reason: workspace client connection invalidated
default	17:23:54.692526-0500	WindowManager	Connection invalidated | (21340) Nexy
default	17:23:54.694004-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	17:23:54.694091-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	17:23:54.693438-0500	WindowServer	0[outside of RPC]: [FocusManager:257] update to deferring policy requested for reason: permitted list updated - 0x0-0x1eb1eb removed - but we are suppressing evaluation for reasons: {(
    "process death - 0x0-0x1eb1eb (Nexy)"
)}
default	17:23:54.694135-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	17:23:54.693608-0500	audiomxd	UpdateAudioState CID 0x91550001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	17:23:54.693799-0500	audiomxd	UpdateAudioState CID 0x91550001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	17:23:54.696028-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	17:23:54.697681-0500	WindowServer	0[outside of RPC]: [FocusManager:257] update to deferring policy requested for reason: permitted list updated - 0x1-0x535c removed - but we are suppressing evaluation for reasons: {(
    "process death - 0x0-0x1eb1eb (Nexy)"
)}
default	17:23:54.708065-0500	runningboardd	XPC connection invalidated: [app<application.com.nexy.assistant.54878181.54878190(501)>:21340]
default	17:23:54.723001-0500	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:55162<-><IPv4-redacted>:443] interface: en0 (skipped: 0)
so_gencnt: 5934852 t_state: FIN_WAIT_1 process: Nexy:21340 Duration: 1.941 sec Conn_Time: 0.043 sec bytes in/out: 2269/732 pkts in/out: 6/4 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 42.375 ms rttvar: 21.687 ms base rtt: 24 ms so_error: 0 svc/tc: 0 flow: 0x9bd16c2a
default	17:23:54.723017-0500	kernel	tcp_connection_summary [<IPv4-redacted>:55162<-><IPv4-redacted>:443] interface: en0 (skipped: 0)
so_gencnt: 5934852 t_state: FIN_WAIT_1 process: Nexy:21340 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	17:23:54.723882-0500	runningboardd	[app<application.com.nexy.assistant.54878181.54878190(501)>:21340] termination reported by launchd (0, 0, 0)
default	17:23:54.723939-0500	runningboardd	Removing process: [app<application.com.nexy.assistant.54878181.54878190(501)>:21340]
default	17:23:54.724186-0500	runningboardd	Removing launch job for: [app<application.com.nexy.assistant.54878181.54878190(501)>:21340]
default	17:23:54.724416-0500	runningboardd	Removed job for [app<application.com.nexy.assistant.54878181.54878190(501)>:21340]
default	17:23:54.724472-0500	runningboardd	Removing assertions for terminated process: [app<application.com.nexy.assistant.54878181.54878190(501)>:21340]
default	17:23:54.732450-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.54878181.54878190(501)>: none (role: NonUserInteractive) (endowments: (null))
default	17:23:54.732848-0500	ControlCenter	[app<application.com.nexy.assistant.54878181.54878190>:21340] Process exited: <RBSProcessExitContext| voluntary>.
default	17:23:54.732873-0500	ControlCenter	[app<application.com.nexy.assistant.54878181.54878190>:21340] Setting process task state to: Not Running
default	17:23:54.732887-0500	ControlCenter	[app<application.com.nexy.assistant.54878181.54878190>:21340] Setting process visibility to: Unknown
default	17:23:54.732778-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.54878181.54878190(501)>: none (role: NonUserInteractive) (endowments: (null))
default	17:23:54.732920-0500	ControlCenter	[app<application.com.nexy.assistant.54878181.54878190>:21340] Invalidating workspace.
default	17:23:54.732911-0500	ControlCenter	Received state update for 21340 (app<application.com.nexy.assistant.54878181.54878190(501)>, none-NotVisible
default	17:23:54.732968-0500	ControlCenter	Removing source registration for processHandle: [app<application.com.nexy.assistant.54878181.54878190(501)>:21340]
default	17:23:54.732897-0500	audiomxd	  ServerSessionManager.mm:1327  Monitored process died, pid = 21340, name = Nexy
default	17:23:54.733170-0500	ControlCenter	Received state update for 21340 (app<application.com.nexy.assistant.54878181.54878190(501)>, none-NotVisible
default	17:23:54.733454-0500	ControlCenter	Removing: <FBApplicationProcess: 0xc32033000; app<application.com.nexy.assistant.54878181.54878190>:21340(v79BA39)>
default	17:23:54.735141-0500	gamepolicyd	Received state update for 21340 (app<application.com.nexy.assistant.54878181.54878190(501)>, none-NotVisible
default	17:23:54.735482-0500	launchservicesd	Hit the server for a process handle 1c2fa5b30000535c that resolved to: [app<application.com.nexy.assistant.54878181.54878190(501)>:21340]
default	17:23:54.735726-0500	ControlCenter	Stopping tracking for host; (bid:com.nexy.assistant-Item-0-21340)
default	17:23:54.737906-0500	loginwindow	-[ApplicationManager handleCASEvent:withData:] | CAS notification for appDeath for com.nexy.assistant with asn: LSASN:{hi=0x0;lo=0x1eb1eb} for bundle path: /Applications/Nexy.app with URL: file:///Applications/Nexy.app/
default	17:23:54.737941-0500	loginwindow	-[Application setState:] | enter: <Application: 0xc01219400: Nexy> state 3
default	17:23:54.737962-0500	loginwindow	-[PersistentAppsSupport applicationQuit:] | for app:Nexy, _appTrackingState = 2
default	17:23:54.738543-0500	ControlCenter	Removing ephemeral displayable instance DisplayableId(91EE63C4) from menu bar. No corresponding host (bid:com.nexy.assistant-Item-0-21340)
default	17:23:54.738615-0500	ControlCenter	Removing displayables [DisplayableAppStatusItem(91EE63C4, (bid:com.nexy.assistant-Item-0-21340))]
default	17:23:54.743371-0500	loginwindow	-[Application setState:] | enter: <Application: 0xc01219400: Nexy> state 4
default	17:23:54.743388-0500	loginwindow	-[PersistentAppsSupport applicationQuit:] | for app:Nexy, _appTrackingState = 2
default	17:23:55.872287-0500	runningboardd	Invalidating assertion 400-615-17231 (target:app<application.com.nexy.assistant.54878181.54878190(501)>) from originator [osservice<com.apple.controlcenter(501)>:615]
default	17:23:55.975394-0500	runningboardd	Removed last relative-start-date-defining assertion for process app<application.com.nexy.assistant.54878181.54878190(501)>
default	17:23:55.981467-0500	gamepolicyd	Received state update for -1 (app<application.com.nexy.assistant.54878181.54878190(501)>, none-NotVisible
default	17:23:57.818761-0500	logger	launching: /usr/bin/open -a /Applications/Nexy.app
default	17:23:57.899854-0500	lsd	com.nexy.assistant/Unknown Persona:5:5:1:1:Building bundle record for app
default	17:23:57.899964-0500	lsd	com.nexy.assistant/Unknown Persona:5:5:2:1:Built bundle record for app
default	17:23:57.901742-0500	lsd	com.nexy.assistant/Unknown Persona:5:4:2:1:_LSServerRegisterItemInfo result = 0
default	17:23:57.905340-0500	dmd	Received xpc stream event (distributed notification matching) with name: com.apple.LaunchServices.applicationRegistered user info: {
    CFBundleDisplayName = Nexy;
    bundleIDs =     (
        "com.nexy.assistant"
    );
    isPlaceholder = 0;
}
default	17:23:57.907433-0500	runningboardd	Launch request for app<application.com.nexy.assistant.54878181.54878190(501)>[0] is using uid 501 (divined from auid 501 euid 501)
default	17:23:57.907480-0500	runningboardd	Acquiring assertion targeting app<application.com.nexy.assistant.54878181.54878190(501)> from originator [osservice<com.apple.coreservices.uiagent(501)>:99676] with description <RBSAssertionDescriptor| "LS launch com.nexy.assistant" ID:400-99676-17239 target:app<application.com.nexy.assistant.54878181.54878190(501)> attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"LaunchRoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	17:23:57.907530-0500	runningboardd	Assertion 400-99676-17239 (target:app<application.com.nexy.assistant.54878181.54878190(501)>) will be created as active
default	17:23:57.910512-0500	runningboardd	Checking PreventLaunch: global:0 exPath:/Applications/Nexy.app/Contents/MacOS/Nexy predicates:(null) allow:(null)
default	17:23:57.910538-0500	runningboardd	Creating and launching job for: app<application.com.nexy.assistant.54878181.54878190(501)>
default	17:23:57.910550-0500	runningboardd	_mutateContextIfNeeded called for com.nexy.assistant
default	17:23:57.910610-0500	runningboardd	app<application.com.nexy.assistant.54878181.54878190(501)>: -[RBPersonaManager personaForIdentity:context:personaUID:personaUniqueString:] required 0.000000 ms (wallclock); resolved to {4294967295, (null)}
default	17:23:57.923630-0500	runningboardd	[app<application.com.nexy.assistant.54878181.54878190(501)>:21495] is not RunningBoard jetsam managed.
default	17:23:57.923640-0500	runningboardd	[app<application.com.nexy.assistant.54878181.54878190(501)>:21495] This process will not be managed.
default	17:23:57.923646-0500	runningboardd	Now tracking process: [app<application.com.nexy.assistant.54878181.54878190(501)>:21495]
default	17:23:57.923746-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.54878181.54878190(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	17:23:57.924321-0500	gamepolicyd	Hit the server for a process handle 4fa432c000053f7 that resolved to: [app<application.com.nexy.assistant.54878181.54878190(501)>:21495]
default	17:23:57.924343-0500	gamepolicyd	Received state update for 21495 (app<application.com.nexy.assistant.54878181.54878190(501)>, running-active-NotVisible
default	17:23:57.927205-0500	runningboardd	Using default underlying assertion for app: [app<application.com.nexy.assistant.54878181.54878190(501)>:21495]
default	17:23:57.927256-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.54878181.54878190(501)>:21495] from originator [app<application.com.nexy.assistant.54878181.54878190(501)>:21495] with description <RBSAssertionDescriptor| "RB Underlying Assertion" ID:400-400-17240 target:21495 attributes:[
	<RBSDomainAttribute| domain:"com.apple.underlying" name:"defaultUnderlyingAppAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	17:23:57.927355-0500	runningboardd	Assertion 400-400-17240 (target:[app<application.com.nexy.assistant.54878181.54878190(501)>:21495]) will be created as active
default	17:23:57.927484-0500	runningboardd	[app<application.com.nexy.assistant.54878181.54878190(501)>:21495] Ignoring jetsam update because this process is not memory-managed
default	17:23:57.927501-0500	runningboardd	[app<application.com.nexy.assistant.54878181.54878190(501)>:21495] Ignoring suspend because this process is not lifecycle managed
default	17:23:57.927517-0500	runningboardd	[app<application.com.nexy.assistant.54878181.54878190(501)>:21495] Set darwin role to: UserInteractive
default	17:23:57.927531-0500	runningboardd	[app<application.com.nexy.assistant.54878181.54878190(501)>:21495] Ignoring GPU update because this process is not GPU managed
default	17:23:57.927556-0500	runningboardd	[app<application.com.nexy.assistant.54878181.54878190(501)>:21495] Ignoring memory limit update because this process is not memory-managed
default	17:23:57.927591-0500	runningboardd	[app<application.com.nexy.assistant.54878181.54878190(501)>:21495] reported to RB as running
default	17:23:57.928596-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.54878181.54878190(501)>:21495] from originator [osservice<com.apple.coreservices.launchservicesd>:361] with description <RBSAssertionDescriptor| "uielement:21495" ID:400-361-17241 target:21495 attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"RoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	17:23:57.928668-0500	runningboardd	Assertion 400-361-17241 (target:[app<application.com.nexy.assistant.54878181.54878190(501)>:21495]) will be created as active
default	17:23:57.928793-0500	CoreServicesUIAgent	LAUNCH: 0x0-0x215215 com.nexy.assistant starting stopped process.
default	17:23:57.929508-0500	runningboardd	[app<application.com.nexy.assistant.54878181.54878190(501)>:21495] Ignoring jetsam update because this process is not memory-managed
default	17:23:57.929558-0500	runningboardd	[app<application.com.nexy.assistant.54878181.54878190(501)>:21495] Ignoring suspend because this process is not lifecycle managed
default	17:23:57.929729-0500	loginwindow	-[Application _updateInformationInternal] | Got App URL: file:///Applications/Nexy.app/
default	17:23:57.929584-0500	runningboardd	[app<application.com.nexy.assistant.54878181.54878190(501)>:21495] Ignoring GPU update because this process is not GPU managed
default	17:23:57.929701-0500	runningboardd	[app<application.com.nexy.assistant.54878181.54878190(501)>:21495] Ignoring memory limit update because this process is not memory-managed
default	17:23:57.929857-0500	loginwindow	-[Application setState:] | enter: <Application: 0xc01219400: Nexy> state 2
default	17:23:57.929881-0500	loginwindow	-[ApplicationManager checkInAppContext:eventData:] | ApplicationManager: Checked in app : Nexy
default	17:23:57.929796-0500	runningboardd	Successfully acquired underlying assertion for [app<application.com.nexy.assistant.54878181.54878190(501)>:21495]
default	17:23:57.932166-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.54878181.54878190(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	17:23:57.932404-0500	runningboardd	Invalidating assertion 400-99676-17239 (target:app<application.com.nexy.assistant.54878181.54878190(501)>) from originator [osservice<com.apple.coreservices.uiagent(501)>:99676]
default	17:23:57.932446-0500	runningboardd	[app<application.com.nexy.assistant.54878181.54878190(501)>:21495] Ignoring jetsam update because this process is not memory-managed
default	17:23:57.932476-0500	runningboardd	[app<application.com.nexy.assistant.54878181.54878190(501)>:21495] Ignoring suspend because this process is not lifecycle managed
default	17:23:57.932507-0500	runningboardd	[app<application.com.nexy.assistant.54878181.54878190(501)>:21495] Ignoring GPU update because this process is not GPU managed
default	17:23:57.932471-0500	gamepolicyd	Received state update for 21495 (app<application.com.nexy.assistant.54878181.54878190(501)>, running-active-NotVisible
default	17:23:57.932595-0500	runningboardd	[app<application.com.nexy.assistant.54878181.54878190(501)>:21495] Ignoring memory limit update because this process is not memory-managed
default	17:23:57.935170-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.54878181.54878190(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	17:23:57.940906-0500	logger	verifying new process for /Applications/Nexy.app/Contents/MacOS/Nexy
default	17:23:57.969490-0500	logger	detected new pid 21495 for /Applications/Nexy.app/Contents/MacOS/Nexy
default	17:23:57.989123-0500	Nexy	[0x106e97ba0] activating connection: mach=true listener=false peer=false name=com.apple.cfprefsd.daemon
default	17:23:57.989157-0500	Nexy	[0x106e97ce0] activating connection: mach=true listener=false peer=false name=com.apple.cfprefsd.agent
default	17:23:58.035615-0500	gamepolicyd	Received state update for 21495 (app<application.com.nexy.assistant.54878181.54878190(501)>, running-active-NotVisible
error	17:23:58.046128-0500	Nexy	dlsym cannot find symbol NSMakeRect in CFBundle 0x106e7c180 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	17:23:58.046247-0500	Nexy	dlsym cannot find symbol NSMakePoint in CFBundle 0x106e7c180 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	17:23:58.046355-0500	Nexy	dlsym cannot find symbol NSMakeSize in CFBundle 0x106e7c180 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	17:23:58.046463-0500	Nexy	dlsym cannot find symbol NSMakeRange in CFBundle 0x106e7c180 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
default	17:23:58.047276-0500	Nexy	[0x106e905e0] activating connection: mach=true listener=false peer=false name=com.apple.coreservices.launchservicesd
default	17:23:58.047631-0500	Nexy	[0x836ac0000] activating connection: mach=true listener=false peer=false name=com.apple.analyticsd
default	17:23:58.047794-0500	Nexy	[0x836ac0140] activating connection: mach=true listener=false peer=false name=com.apple.pasteboard.1
default	17:23:58.047974-0500	Nexy	[0x836ac0280] activating connection: mach=true listener=false peer=false name=com.apple.distributed_notifications@Uv3
default	17:23:58.048954-0500	Nexy	void _NSDisableAutomaticTerminationAndLog(NSString *) No windows open yet
default	17:23:58.049125-0500	Nexy	[0x836ac03c0] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	17:23:58.049401-0500	Nexy	Received configuration update from daemon (initial)
default	17:23:58.049402-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=21495.1, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=21495, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	17:23:58.050184-0500	tccd	AUTHREQ_SUBJECT: msgID=21495.1, subject=com.nexy.assistant,
default	17:23:58.050555-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b5165200 at /Applications/Nexy.app
default	17:23:58.060882-0500	Nexy	[0x836ac03c0] invalidated after the last release of the connection object
default	17:23:58.061048-0500	Nexy	server port 0x00003113, session port 0x00003113
default	17:23:58.061563-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=391.914, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=21495, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=391, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	17:23:58.061574-0500	tccd	requestor: TCCDProcess: identifier=com.apple.WindowServer, pid=391, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=21495, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	17:23:58.061995-0500	tccd	AUTHREQ_SUBJECT: msgID=391.914, subject=com.nexy.assistant,
default	17:23:58.062357-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b5164900 at /Applications/Nexy.app
default	17:23:58.074481-0500	Nexy	New connection 0xd58fb main
default	17:23:58.075738-0500	Nexy	CHECKIN: pid=21495
default	17:23:58.079891-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.54878181.54878190(501)>:21495] from originator [osservice<com.apple.coreservices.launchservicesd>:361] with description <RBSAssertionDescriptor| "uielement:21495" ID:400-361-17242 target:21495 attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"RoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	17:23:58.079935-0500	runningboardd	Assertion 400-361-17242 (target:[app<application.com.nexy.assistant.54878181.54878190(501)>:21495]) will be created as active
default	17:23:58.080353-0500	Nexy	CHECKEDIN: pid=21495 asn=0x0-0x215215 foreground=0
default	17:23:58.080548-0500	loginwindow	-[Application _updateInformationInternal] | Got App URL: file:///Applications/Nexy.app/
default	17:23:58.080250-0500	runningboardd	Invalidating assertion 400-361-17241 (target:[app<application.com.nexy.assistant.54878181.54878190(501)>:21495]) from originator [osservice<com.apple.coreservices.launchservicesd>:361]
default	17:23:58.080259-0500	launchservicesd	CHECKIN:0x0-0x215215 21495 com.nexy.assistant
default	17:23:58.080629-0500	loginwindow	-[ApplicationManager checkInAppContext:eventData:] | ApplicationManager: Checked in app : Nexy
default	17:23:58.080482-0500	Nexy	[0x836ac03c0] activating connection: mach=false listener=true peer=false name=(anonymous)
default	17:23:58.080487-0500	Nexy	[0x836ac03c0] Connection returned listener port: 0x4e03
default	17:23:58.081006-0500	Nexy	[0x837e6c300] activating connection: mach=false listener=false peer=true name=com.apple.xpc.anonymous.0x836ac03c0.peer[361].0x837e6c300
default	17:23:58.082093-0500	Nexy	FRONTLOGGING: version 1
default	17:23:58.082124-0500	Nexy	Registered, pid=21495 ASN=0x0,0x215215
default	17:23:58.082294-0500	Nexy	[0x836ac0500] activating connection: mach=true listener=false peer=false name=com.apple.lsd.mapdb
default	17:23:58.082335-0500	WindowServer	d58fb[CreateApplication]: Process creation: 0x0-0x215215 (Nexy) connectionID: D58FB pid: 21495 in session 0x101
default	17:23:58.084444-0500	Nexy	[0x836ac03c0] Connection returned listener port: 0x4e03
default	17:23:58.084913-0500	Nexy	BringForward: pid=21495 asn=0x0-0x215215 bringForward=0 foreground=0 uiElement=1 launchedByLS=1 modifiersCount=1 allDisabled=0
default	17:23:58.085087-0500	Nexy	BringFrontModifier: pid=21495 asn=0x0-0x215215 Modifier 0 hideAfter=0 hideOthers=0 dontMakeFrontmost=0 mouseDown=0/0 seed=0/0
default	17:23:58.085428-0500	Nexy	Current system appearance, (HLTB: 1), (SLS: 0)
default	17:23:58.086386-0500	Nexy	No persisted cache on this platform.
default	17:23:58.087153-0500	Nexy	Current system appearance, (HLTB: 1), (SLS: 0)
default	17:23:58.087660-0500	Nexy	Post-registration system appearance: (HLTB: 1)
default	17:23:58.089106-0500	Nexy	FBSWorkspace: endpoint monitoring is disabled.
default	17:23:58.089112-0500	Nexy	FBSWorkspace: default shell endpoint is disabled.
default	17:23:58.089145-0500	Nexy	Initializing connection
default	17:23:58.089167-0500	Nexy	Removing all cached process handles
default	17:23:58.089179-0500	Nexy	Sending handshake request attempt #1 to server
default	17:23:58.089184-0500	Nexy	Creating connection to com.apple.runningboard
default	17:23:58.089189-0500	Nexy	[0x836ac0640] activating connection: mach=true listener=false peer=false name=com.apple.runningboard
default	17:23:58.089449-0500	runningboardd	Setting client for [app<application.com.nexy.assistant.54878181.54878190(501)>:21495] as ready
default	17:23:58.089761-0500	Nexy	Handshake succeeded
default	17:23:58.089771-0500	Nexy	Identity resolved as app<application.com.nexy.assistant.54878181.54878190(501)>
default	17:23:58.089972-0500	Nexy	[0x836ac03c0] Connection returned listener port: 0x4e03
default	17:23:58.090506-0500	distnoted	register name: com.apple.xctest.FakeForceTouchDevice object: com.nexy.assistant token: 1e0000001d pid: 21495
default	17:23:58.091918-0500	Nexy	[0x836ac03c0] Connection returned listener port: 0x4e03
default	17:23:58.093630-0500	Nexy	Created a new Process Instance Registry XPC connection (inactive)
default	17:23:58.093641-0500	Nexy	[0x836ac0780] activating connection: mach=true listener=false peer=false name=com.apple.linkd.autoShortcut
default	17:23:58.093693-0500	Nexy	Activated connection to com.apple.linkd.autoShortcut (ApplicationService)
default	17:23:58.093730-0500	Nexy	[0x836ac0a00] activating connection: mach=false listener=true peer=false name=(anonymous)
default	17:23:58.094491-0500	Nexy	[0x836ac0a00] Connection returned listener port: 0x6a03
default	17:23:58.094834-0500	Nexy	Registered process with identifier 21495-7977954
default	17:23:58.124526-0500	runningboardd	[app<application.com.nexy.assistant.54878181.54878190(501)>:21495] Ignoring jetsam update because this process is not memory-managed
default	17:23:58.124533-0500	runningboardd	[app<application.com.nexy.assistant.54878181.54878190(501)>:21495] Ignoring suspend because this process is not lifecycle managed
default	17:23:58.124541-0500	runningboardd	[app<application.com.nexy.assistant.54878181.54878190(501)>:21495] Ignoring GPU update because this process is not GPU managed
default	17:23:58.124583-0500	runningboardd	[app<application.com.nexy.assistant.54878181.54878190(501)>:21495] Ignoring memory limit update because this process is not memory-managed
default	17:23:58.127016-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.54878181.54878190(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	17:23:58.127419-0500	gamepolicyd	Received state update for 21495 (app<application.com.nexy.assistant.54878181.54878190(501)>, running-active-NotVisible
default	17:23:58.567222-0500	kernel	SK[8]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 736ED8B5-06F3-494E-B1BA-E12CD76EBAA7 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.55168,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0xc697ce54 tp_proto=0x06"
default	17:23:58.567271-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:55168<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 5934976 t_state: SYN_SENT process: Nexy:21495 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 20 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x99015f21
default	17:23:58.584642-0500	kernel	tcp connected: [<IPv4-redacted>:55168<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 5934976 t_state: ESTABLISHED process: Nexy:21495 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 20 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x99015f21
default	17:23:58.584805-0500	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:55168<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 5934976 t_state: FIN_WAIT_1 process: Nexy:21495 Duration: 0.018 sec Conn_Time: 0.018 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 18.000 ms rttvar: 9.000 ms base rtt: 18 ms so_error: 0 svc/tc: 0 flow: 0x99015f21
default	17:23:58.584810-0500	kernel	tcp_connection_summary [<IPv4-redacted>:55168<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 5934976 t_state: FIN_WAIT_1 process: Nexy:21495 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	17:23:59.083385-0500	Nexy	server port 0x0000a903, session port 0x00003113
default	17:23:59.087630-0500	Nexy	  AVAudioSession_MacOS.mm:1021  initForMacOS
default	17:23:59.087929-0500	Nexy	[0x836ac0f00] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioSession
default	17:23:59.088362-0500	audiomxd	  ServerSessionManager.mm:315   { "action":"create_session", "session":{"ID":"0x1f402a","name":"Nexy(21495)"}, "details":{"PID":21495,"session_type":"Primary"} }
default	17:23:59.088403-0500	audiomxd	AudioApplicationInfoImpl.mm:250   Setting initial isRecording state: 0 for newly-created AudioApp
	app: {"name":"[implicit] Nexy","pid":21495}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1f402a, sessionType: 'prim', isRecording: false }, 
]
default	17:23:59.088762-0500	audiomxd	  ServerSessionManager.mm:1322  Start process monitoring, pid = 21495, name = Nexy
default	17:23:59.088927-0500	Nexy	    SessionCore_Create.mm:99    Created session 0x836980cc0 with ID: 0x1f402a
default	17:23:59.089055-0500	Nexy	Registered notify signal com.apple.caulk.alloc.rtdump (0)
default	17:23:59.089535-0500	Nexy	System_Input_Processing_Notification_Handler.mm:456   System_Input_Processing_Notification_Handler::is_vi_available(): Voice isolation DSP is available for client with bundle id com.nexy.assistant (AVFoundation is available, application is not in client deny list, application is not FaceTime variant)
default	17:23:59.090145-0500	Nexy	[0x836ac1040] activating connection: mach=true listener=false peer=false name=com.apple.cmio.registerassistantservice.system-extensions
fault	17:23:59.091365-0500	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.54878181.54878190 AUID=501> and <type=Application identifier=application.com.nexy.assistant.54878181.54878190>
default	17:23:59.095352-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOInitializeListenersForBundleID: for <private> -> <private>
default	17:23:59.096158-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> vpio_preferenceChangedListener: new value ((null)) for key AUVoiceIOClients/com-nexy-assistant/AUVoiceIOChatFlavor, translatedBundleID com.nexy.assistant, bundleIDs {(
    "com.nexy.assistant"
)}
default	17:23:59.096241-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> vpio_preferenceChangedListener: new value ((null)) for key AUVoiceIOClients/com-nexy-assistant/AUVoiceIOIsAutoChatFlavorEnabled, translatedBundleID com.nexy.assistant, bundleIDs {(
    "com.nexy.assistant"
)}
default	17:23:59.096303-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetSupportedChatFlavorsForBundleID: <private>-><private> get supported chat flavors: <private>
default	17:23:59.096308-0500	Nexy	            HALSystem.cpp:134    Enabling HAL Voice Isolation support
default	17:23:59.096326-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetHiddenChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	17:23:59.096384-0500	Nexy	[0x836ac1180] activating connection: mach=true listener=false peer=false name=com.apple.tccd
default	17:23:59.096501-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOHiddenChatFlavors newValue: (
    1
)
default	17:23:59.096631-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=21495.2, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=21495, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	17:23:59.101253-0500	tccd	AUTHREQ_SUBJECT: msgID=21495.2, subject=com.nexy.assistant,
default	17:23:59.101713-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x722e70900 at /Applications/Nexy.app
default	17:23:59.111783-0500	Nexy	[0x836ac1180] invalidated after the last release of the connection object
default	17:23:59.111877-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetPreferredChatFlavorForBundleID: <private>-><private> get value: 0
default	17:23:59.111902-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetSupportedChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	17:23:59.112057-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOSupportedChatFlavors newValue: (
    0,
    2
)
default	17:23:59.112679-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.965, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=21495, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=392, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	17:23:59.113240-0500	tccd	AUTHREQ_SUBJECT: msgID=401.965, subject=com.nexy.assistant,
default	17:23:59.113554-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x722e70900 at /Applications/Nexy.app
error	17:23:59.122380-0500	tccd	Request message contains a target_token to accessing_process (TCCDProcess: identifier=com.nexy.assistant, pid=21495, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy) but TCCDProcess: identifier=com.apple.audio.coreaudiod, pid=401, auid=202, euid=202, binary_path=/usr/sbin/coreaudiod is not a TCC manager for service: kTCCServiceScreenCapture.
default	17:23:59.122842-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.967, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=21495, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=392, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	17:23:59.123353-0500	tccd	AUTHREQ_SUBJECT: msgID=401.967, subject=com.nexy.assistant,
default	17:23:59.123718-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x722e70900 at /Applications/Nexy.app
default	17:23:59.131886-0500	Nexy	  HALPlugInManagement.cpp:440    HALPlugInManagement::RegisterPlugIns: skipping in-process plug-ins
error	17:23:59.131899-0500	Nexy	AddInstanceForFactory: No factory registered for id <CFUUID 0x839ea4c20> F8BB1C28-BAE8-11D6-9C31-00039315CD46
default	17:23:59.139561-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetPreferredChatFlavorForBundleID: <private>-><private> get value: 0
default	17:23:59.139996-0500	Nexy	[0x836ac1180] activating connection: mach=true listener=false peer=false name=com.apple.audioanalyticsd
error	17:23:59.140212-0500	Nexy	Reporter disconnected. { function=sendMessage, reporterID=92320322027521 }
default	17:23:59.140259-0500	Nexy	       AggregateDevice.mm:887   Creating DefaultDeviceAggregate
default	17:23:59.140280-0500	Nexy	       AggregateDevice.mm:914   fetched default output device, ID = 71
default	17:23:59.140295-0500	Nexy	       AggregateDevice.mm:914   fetched default input device, ID = 78
default	17:23:59.145207-0500	Nexy	       AggregateDevice.mm:688   Built valid aggregate 110
default	17:23:59.150732-0500	Nexy	  AVAudioSession_MacOS.mm:507   Setting category: AVAudioSessionCategoryPlayback, requires reconfiguration?: NO
default	17:23:59.150748-0500	Nexy	  AVAudioSession_MacOS.mm:883   Activating session
default	17:23:59.153155-0500	Nexy	[0x836ac12c0] activating connection: mach=true listener=false peer=false name=com.apple.SystemConfiguration.DNSConfiguration
default	17:23:59.153429-0500	Nexy	[0x836ac12c0] invalidated after the last release of the connection object
default	17:23:59.153454-0500	Nexy	[0x836ac1400] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioComponentRegistrar
default	17:23:59.153762-0500	kernel	udp connect: [<IPv6-redacted>:53341<-><IPv6-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 5935019 so_state: 0x0102 process: Nexy:21495 bytes in/out: 0/0 pkts in/out: 0/0 error: 0 so_error: 0 svc/tc: 0 flow: 0x90a13972
default	17:23:59.158741-0500	Nexy	                AUHAL.cpp:420   AUHAL: (0x839ebea40) Selecting device 71 from constructor
default	17:23:59.158746-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0x839ebea40)
default	17:23:59.158747-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0x839ebea40) not already running
default	17:23:59.158751-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0x839ebea40) nothing to teardown
default	17:23:59.158767-0500	Nexy	                AUHAL.cpp:762   SelectDevice: (0x839ebea40) connecting device 71
default	17:23:59.158840-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0x839ebea40) Device ID: 71 (Input:No | Output:Yes): true
default	17:23:59.158910-0500	Nexy	                AUHAL.cpp:774   SelectDevice: (0x839ebea40) created ioproc 0xa for device 71
default	17:23:59.158967-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x839ebea40) adding 7 device listeners to device 71
default	17:23:59.159073-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x839ebea40) adding 0 device delegate listeners to device 71
default	17:23:59.159076-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x839ebea40)
default	17:23:59.159120-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x48]:  2 ch,  48000 Hz, Float32, interleaved
default	17:23:59.160115-0500	Nexy	       ACv2Workarounds.mm:51    com.nexy.assistant: fix84702776_86723525_86479548_89800354_SinglePacketDesc: false
default	17:23:59.160142-0500	Nexy	Registered notify signal com.apple.caulk.alloc.audiodump (0)
default	17:23:59.160217-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0x83567e160, from  2 ch,  44100 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	17:23:59.160229-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	17:23:59.160983-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	17:23:59.161101-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	17:23:59.162748-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0x83567e190, from  2 ch,  44100 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	17:23:59.162758-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	17:23:59.162930-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	17:23:59.163388-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0x83567e190, from  2 ch,  48000 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	17:23:59.163394-0500	Nexy	       AudioConverter.cpp:1317  AudioConverter -> 0x83567e190: The in-process GetProperty call returned 1886547824 for property 1886546285 with size 8.
default	17:23:59.163398-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	17:23:59.163397-0500	Nexy	AudioConverter -> 0x83567e190: The in-process SetProperty call returned 1886547824 for property 1936876385 with size 4.
default	17:23:59.163402-0500	Nexy	AudioConverter -> 0x83567e190: The in-process SetProperty call returned 1886547824 for property 1936876401 with size 4.
default	17:23:59.163403-0500	Nexy	AudioConverter -> 0x83567e190: The in-process SetProperty call returned 1886547824 for property 1886547309 with size 4.
default	17:23:59.165050-0500	kernel	SK[6]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid F0B7CC8E-B3F0-470F-BA65-11343F5E308E flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.55174,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0xbbdb287c tp_proto=0x06"
default	17:23:59.165091-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:55174<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 5935020 t_state: SYN_SENT process: Nexy:21495 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 17 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xbc42d384
default	17:23:59.165280-0500	Nexy	networkd_settings_read_from_file initialized networkd settings by reading plist directly
default	17:23:59.165374-0500	Nexy	networkd_settings_read_from_file initialized networkd settings by reading plist directly
default	17:23:59.178488-0500	kernel	SK[6]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid CEDDF083-D304-45BA-B3AD-07F65C6BB0A0 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.55177,dst=<IPv4-redacted>.443,proto=0x06 mask=0x0000003f,hash=0x7454847d tp_proto=0x06"
default	17:23:59.178503-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:55177<-><IPv4-redacted>:443] interface: en0 (skipped: 0)
so_gencnt: 5935053 t_state: SYN_SENT process: Nexy:21495 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 24 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x831a8557
default	17:23:59.186892-0500	kernel	tcp connected: [<IPv4-redacted>:55174<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 5935020 t_state: ESTABLISHED process: Nexy:21495 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 17 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xbc42d384
default	17:23:59.187057-0500	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:55174<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 5935020 t_state: FIN_WAIT_1 process: Nexy:21495 Duration: 0.022 sec Conn_Time: 0.022 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 22.000 ms rttvar: 11.000 ms base rtt: 17 ms so_error: 0 svc/tc: 0 flow: 0xbc42d384
default	17:23:59.187062-0500	kernel	tcp_connection_summary [<IPv4-redacted>:55174<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 5935020 t_state: FIN_WAIT_1 process: Nexy:21495 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	17:23:59.187149-0500	kernel	SK[9]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 691A5B7B-931E-42CE-90FC-CADD88473BD8 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.55178,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0x7200b64b tp_proto=0x06"
default	17:23:59.187159-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:55178<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 5935054 t_state: SYN_SENT process: Nexy:21495 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 17 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x8d348528
default	17:23:59.207643-0500	kernel	tcp connected: [<IPv4-redacted>:55177<-><IPv4-redacted>:443] interface: en0 (skipped: 0)
so_gencnt: 5935053 t_state: ESTABLISHED process: Nexy:21495 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 24 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x831a8557
default	17:23:59.208950-0500	kernel	tcp connected: [<IPv4-redacted>:55178<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 5935054 t_state: ESTABLISHED process: Nexy:21495 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 17 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x8d348528
default	17:23:59.209093-0500	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:55178<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 5935054 t_state: FIN_WAIT_1 process: Nexy:21495 Duration: 0.022 sec Conn_Time: 0.022 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 22.000 ms rttvar: 11.000 ms base rtt: 17 ms so_error: 0 svc/tc: 0 flow: 0x8d348528
default	17:23:59.209099-0500	kernel	tcp_connection_summary [<IPv4-redacted>:55178<-><IPv4-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 5935054 t_state: FIN_WAIT_1 process: Nexy:21495 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	17:23:59.210766-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=21505.1, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=21495, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.osascript, pid=21505, auid=501, euid=501, binary_path=/usr/bin/osascript}, },
default	17:23:59.211853-0500	tccd	AUTHREQ_SUBJECT: msgID=21505.1, subject=com.nexy.assistant,
default	17:23:59.212821-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b5164900 at /Applications/Nexy.app
default	17:23:59.225492-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=391.916, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=21495, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.osascript, pid=21505, auid=501, euid=501, binary_path=/usr/bin/osascript}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=391, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	17:23:59.225994-0500	tccd	AUTHREQ_SUBJECT: msgID=391.916, subject=com.nexy.assistant,
default	17:23:59.226320-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b5164900 at /Applications/Nexy.app
default	17:23:59.250858-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b5164000 at /Applications/Nexy.app
default	17:23:59.284295-0500	kernel	udp connect: [<IPv4-redacted>:54564<-><IPv4-redacted>:443] interface:  (skipped: 0)
so_gencnt: 5935055 so_state: 0x0002 process: Nexy:21495 bytes in/out: 0/0 pkts in/out: 0/0 error: 0 so_error: 0 svc/tc: 0 flow: 0xa920e264
default	17:23:59.284303-0500	kernel	udp_connection_summary [<IPv4-redacted>:54564<-><IPv4-redacted>:443] interface:  (skipped: 0)
so_gencnt: 5935055 so_state: 0x0002 process: Nexy:21495 Duration: 0.000 sec Conn_Time: 0.000 sec bytes in/out: 0/0 pkts in/out: 0/0 rxnospace pkts/bytes: 0/0 so_error: 0 svc/tc: 0 flow: 0xa920e264 flowctl: 0us (0x)
default	17:23:59.284317-0500	kernel	udp_connection_summary [<IPv6-redacted>:53341<-><IPv6-redacted>:53] interface: en0 (skipped: 0)
so_gencnt: 5935019 so_state: 0x0132 process: Nexy:21495 Duration: 0.130 sec Conn_Time: 0.130 sec bytes in/out: 355/194 pkts in/out: 3/3 rxnospace pkts/bytes: 0/0 so_error: 0 svc/tc: 0 flow: 0x90a13972 flowctl: 0us (0x)
default	17:23:59.284514-0500	kernel	SK[6]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 5910E2C9-CD5D-4DEF-98A1-38BA92FFE866 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.55179,dst=<IPv4-redacted>.443,proto=0x06 mask=0x0000003f,hash=0x0d4b97a2 tp_proto=0x06"
default	17:23:59.284542-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:55179<-><IPv4-redacted>:443] interface: en0 (skipped: 0)
so_gencnt: 5935056 t_state: SYN_SENT process: Nexy:21495 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 24 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x997b93aa
default	17:23:59.305207-0500	kernel	tcp connected: [<IPv4-redacted>:55179<-><IPv4-redacted>:443] interface: en0 (skipped: 0)
so_gencnt: 5935056 t_state: ESTABLISHED process: Nexy:21495 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 24 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x997b93aa
default	17:23:59.342735-0500	System Events	TCCAccessRequestIndirect: TCCAccessRequestIndirect with pid 21506: target_identity: {
    kTCCCodeIdentityAuditToken = {length = 32, bytes = 0xf5010000 f5010000 14000000 f5010000 ... b7860100 f3bb7900 };
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
default	17:23:59.349280-0500	tccd	target_executable_path_URL: file:///Applications/Nexy.app/Contents/MacOS/Nexy
default	17:23:59.356245-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x722e70600 at /Applications/Nexy.app
default	17:23:59.365292-0500	tccd	Prompting for access to indirect object System Events by Nexy
default	17:24:01.175137-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x722e71200 at /Applications/Nexy.app
default	17:24:01.182100-0500	tccd	Publishing <TCCDEvent: type=Create, service=kTCCServiceAppleEvents, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 3 subscribers: {
    39 = "<TCCDEventSubscriber: token=39, state=Passed, csid=com.apple.chronod>";
    38 = "<TCCDEventSubscriber: token=38, state=Initial, csid=(null)>";
    41 = "<TCCDEventSubscriber: token=41, state=Passed, csid=com.apple.photolibraryd>";
}
default	17:24:01.187102-0500	chronod	[appAuth:com.nexy.assistant] tcc authorization(s) changed
default	17:24:03.266335-0500	Nexy	  AVAudioSession_MacOS.mm:883   Activating session
default	17:24:03.271991-0500	Nexy	         AVAudioEngine.mm:1182  Engine@0x836b305d0: start, was running 0
default	17:24:03.275639-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.54878181.54878190(501)>:21495] from originator [osservice<com.apple.powerd>:332] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:400-332-17257 target:21495 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	17:24:03.275763-0500	runningboardd	Assertion 400-332-17257 (target:[app<application.com.nexy.assistant.54878181.54878190(501)>:21495]) will be created as active
default	17:24:03.276180-0500	runningboardd	[app<application.com.nexy.assistant.54878181.54878190(501)>:21495] Ignoring jetsam update because this process is not memory-managed
default	17:24:03.276192-0500	runningboardd	[app<application.com.nexy.assistant.54878181.54878190(501)>:21495] Ignoring suspend because this process is not lifecycle managed
default	17:24:03.276202-0500	runningboardd	[app<application.com.nexy.assistant.54878181.54878190(501)>:21495] Ignoring GPU update because this process is not GPU managed
default	17:24:03.276226-0500	runningboardd	[app<application.com.nexy.assistant.54878181.54878190(501)>:21495] Ignoring memory limit update because this process is not memory-managed
default	17:24:03.280536-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.54878181.54878190(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	17:24:03.281610-0500	gamepolicyd	Received state update for 21495 (app<application.com.nexy.assistant.54878181.54878190(501)>, running-active-NotVisible
default	17:24:03.300744-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {BuiltInSpeakerDevice, 0xa}
default	17:24:03.302102-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1f402a","name":"Nexy(21495)"}, "details":{"deviceUIDs":[],"implicit_category":"MediaPlayback","input_running":false,"output_running":true} }
default	17:24:03.302244-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 43, PID = 21495, Name = sid:0x1f402a, Nexy(21495), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	17:24:03.302311-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 43, PID = 21495, Name = sid:0x1f402a, Nexy(21495), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	17:24:03.302361-0500	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1f402a, Nexy(21495), 'prim'', AudioCategory changed to 'MediaPlayback'
default	17:24:03.302393-0500	audiomxd	UpdateAudioState CID 0x91550001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	17:24:03.302454-0500	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 43, PID = 21495, Name = sid:0x1f402a, Nexy(21495), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO> is going active
default	17:24:03.302468-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsPlaying:]: MXCoreSession com.nexy.assistant with category/mode MediaPlayback/Default and coreSessionID = 43 starting playing
default	17:24:03.302550-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 43, PID = 21495, Name = sid:0x1f402a, Nexy(21495), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	17:24:03.302581-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 43, PID = 21495, Name = sid:0x1f402a, Nexy(21495), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO>
default	17:24:03.302606-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1f402a, Nexy(21495), 'prim'', displayID:'com.nexy.assistant'}
default	17:24:03.302586-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	17:24:03.302635-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	17:24:03.302628-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Will try to see if we can get the shared route for session = <ID: 43, PID = 21495, Name = sid:0x1f402a, Nexy(21495), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO>. Old (200) and New (201) scores.
default	17:24:03.302670-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 201, deviceID = <private>
default	17:24:03.302701-0500	audiomxd	AudioApplicationInfoImpl.mm:395   Successfully updated session 0x1f402a to isSessionRecording: 0
	app: {"name":"[implicit] Nexy","pid":21495}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1f402a, sessionType: 'prim', isRecording: false }, 
]
default	17:24:03.302866-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 1]. BT device UIDS: {(
)}
default	17:24:03.302881-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	17:24:03.304459-0500	audioaccessoryd	Routing request Wx NULL score 201 flag 0x1 < Hijack > app com.nexy.assistant CID 0x91550001 category Not set
default	17:24:03.304748-0500	audiomxd	UpdateAudioState CID 0x91550001 audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	17:24:03.304852-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 201,
}
default	17:24:03.304882-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	17:24:03.304898-0500	audioaccessoryd	AudioStateChanged: Added audio session app com.nexy.assistant NULL -> 201 count 1
default	17:24:03.304908-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 201
error	17:24:03.304920-0500	audioaccessoryd	Updating local audio category 100 -> 201 app com.nexy.assistant
default	17:24:03.304963-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.nexy.assistant
default	17:24:03.331186-0500	runningboardd	Assertion did invalidate due to timeout: 400-400-17240 (target:[app<application.com.nexy.assistant.54878181.54878190(501)>:21495])
default	17:24:03.358586-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 201
default	17:24:03.358608-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.nexy.assistant
default	17:24:03.358809-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 201
default	17:24:03.358823-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.nexy.assistant
default	17:24:03.359000-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 201
default	17:24:03.359013-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.nexy.assistant
default	17:24:03.395150-0500	Nexy	[0x836ac17c0] activating connection: mach=true listener=false peer=false name=com.apple.usernoted.client
default	17:24:03.405670-0500	usernoted	Connection com.nexy.assistant with path: /Applications/Nexy.app
default	17:24:03.411365-0500	distnoted	register name: com.apple.nsquiet_safe_quit_give_reason object: com.nexy.assistant token: 2300000021 pid: 21495
default	17:24:03.422111-0500	Nexy	NSApp cache appearance:
-NSRequiresAquaSystemAppearance: 0
-appearance: (null)
-effectiveAppearance: <NSCompositeAppearance: 0x837d68780
 (
    "<NSAquaAppearance: 0x837d685a0>",
    "<NSSystemAppearance: 0x837d686e0>"
)>
default	17:24:03.427252-0500	Nexy	[0x836ac1cc0] activating connection: mach=true listener=false peer=false name=com.apple.dock.fullscreen
default	17:24:03.427707-0500	Nexy	[0x836ac1e00] activating connection: mach=true listener=false peer=false name=com.apple.fonts
default	17:24:03.430143-0500	Nexy	(<private>) deleteSearchableItemsWithDomainIdentifiers, protectionClass:(null), domainIdentifiers number:1
default	17:24:03.430409-0500	Nexy	sConnectionName: com.apple.spotlight.IndexAgent
default	17:24:03.430418-0500	Nexy	Start service name com.apple.spotlight.IndexAgent
default	17:24:03.430445-0500	Nexy	[0x836ac1f40] activating connection: mach=true listener=false peer=false name=com.apple.spotlight.IndexAgent
default	17:24:03.430483-0500	Nexy	[C:1] Alloc com.apple.controlcenter.statusitems
default	17:24:03.430550-0500	Nexy	[0x836ac2080] activating connection: mach=false listener=false peer=false name=(anonymous)
default	17:24:03.430614-0500	Nexy	FBSWorkspace registering source: <private>
default	17:24:03.431099-0500	suggestd	SGDSpotlightReceiver: deleting 1 domain identifiers (1 after removing overlaps) for com.nexy.assistant: <private>
default	17:24:03.431335-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	17:24:03.431639-0500	Nexy	<FBSWorkspaceScenesClient:0x837d6a800 <private>> attempting immediate handshake from activate
default	17:24:03.431689-0500	Nexy	<FBSWorkspaceScenesClient:0x837d6a800 <private>> sent handshake
default	17:24:03.431777-0500	Nexy	Realizing settings extension __NSStatusItemSceneHostSettings__ on FBSSceneSettings
default	17:24:03.432090-0500	ControlCenter	Asked to bootstrap a new process for handle: [app<application.com.nexy.assistant.54878181.54878190(501)>:21495]
default	17:24:03.432116-0500	ControlCenter	Creating process (sync=true) for handle: [app<application.com.nexy.assistant.54878181.54878190(501)>:21495]
default	17:24:03.432183-0500	ControlCenter	[app<application.com.nexy.assistant.54878181.54878190>:21495] Registering event dispatcher at init
default	17:24:03.432241-0500	ControlCenter	Created <FBWorkspace: 0xc31cf7020; <FBApplicationProcess: 0xc32031f80; app<application.com.nexy.assistant.54878181.54878190>:21495(v79BBE2)>>
default	17:24:03.432255-0500	ControlCenter	Bootstrapping app<application.com.nexy.assistant.54878181.54878190> with intent background
default	17:24:03.432326-0500	Nexy	Realizing settings extension __NSStatusItemSceneClientSettings__ on FBSSceneClientSettings
default	17:24:03.432481-0500	runningboardd	Launch request for app<application.com.nexy.assistant.54878181.54878190(501)>[0] is using uid 501 (divined from auid 501 euid 501)
default	17:24:03.432586-0500	runningboardd	Acquiring assertion targeting app<application.com.nexy.assistant.54878181.54878190(501)> from originator [osservice<com.apple.controlcenter(501)>:615] with description <RBSAssertionDescriptor| "FBApplicationProcess" ID:400-615-17260 target:app<application.com.nexy.assistant.54878181.54878190(501)> attributes:[
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableLPRunReason-Suspend" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableRole-NonUI" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableJetsamPriority-Active" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableBootstrapping" sourceEnvironment:"(null)">
	]>
default	17:24:03.432724-0500	runningboardd	Assertion 400-615-17260 (target:app<application.com.nexy.assistant.54878181.54878190(501)>) will be created as active
default	17:24:03.432755-0500	runningboardd	setting abstract target for <RBSAssertionDescriptor| "FBApplicationProcess" ID:400-615-17260 target:app<application.com.nexy.assistant.54878181.54878190(501)> attributes:[
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableLPRunReason-Suspend" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableRole-NonUI" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableJetsamPriority-Active" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableBootstrapping" sourceEnvironment:"(null)">
	]> to [app<application.com.nexy.assistant.54878181.54878190(501)>:21495]
default	17:24:03.433088-0500	runningboardd	[app<application.com.nexy.assistant.54878181.54878190(501)>:21495] Ignoring jetsam update because this process is not memory-managed
default	17:24:03.433926-0500	Nexy	Realizing settings extension FBSSceneSettingsCore on FBSSceneSettings
default	17:24:03.433099-0500	runningboardd	[app<application.com.nexy.assistant.54878181.54878190(501)>:21495] Ignoring suspend because this process is not lifecycle managed
default	17:24:03.434652-0500	runningboardd	[app<application.com.nexy.assistant.54878181.54878190(501)>:21495] Ignoring GPU update because this process is not GPU managed
default	17:24:03.435015-0500	Nexy	Realizing settings extension FBSSceneClientSettingsCore on FBSSceneClientSettings
default	17:24:03.435199-0500	runningboardd	[app<application.com.nexy.assistant.54878181.54878190(501)>:21495] Ignoring memory limit update because this process is not memory-managed
default	17:24:03.435619-0500	Nexy	Requesting scene <FBSScene: 0x837d6ac60; com.apple.controlcenter:950C5067-8704-4062-917B-7F9E4958E32D> from com.apple.controlcenter.statusitems
default	17:24:03.435997-0500	Nexy	Request for <FBSScene: 0x837d6ac60; com.apple.controlcenter:950C5067-8704-4062-917B-7F9E4958E32D> complete!
default	17:24:03.436075-0500	Nexy	Realizing settings extension FBSSceneTransitionContextCore on FBSSceneTransitionContext
default	17:24:03.437650-0500	Nexy	Realizing settings extension __NSHostedViewSceneSettings__ on FBSSceneSettings
default	17:24:03.437946-0500	Nexy	Realizing settings extension __NSClientHostedViewSceneSettings__ on FBSSceneClientSettings
default	17:24:03.438234-0500	Nexy	Realizing settings extension __NSStatusItemAuxiliaryViewSceneSettings__ on FBSSceneSettings
default	17:24:03.438266-0500	Nexy	Realizing settings extension __NSClientStatusItemAuxiliaryViewSceneSettings__ on FBSSceneClientSettings
default	17:24:03.438587-0500	Nexy	Requesting scene <FBSScene: 0x837d6ab20; com.apple.controlcenter:950C5067-8704-4062-917B-7F9E4958E32D-Aux[1]-NSStatusItemView> from com.apple.controlcenter.statusitems
default	17:24:03.438747-0500	Nexy	Request for <FBSScene: 0x837d6ab20; com.apple.controlcenter:950C5067-8704-4062-917B-7F9E4958E32D-Aux[1]-NSStatusItemView> complete!
default	17:24:03.440354-0500	Nexy	[com.apple.controlcenter:950C5067-8704-4062-917B-7F9E4958E32D-Aux[1]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
default	17:24:03.440367-0500	Nexy	[com.apple.controlcenter:950C5067-8704-4062-917B-7F9E4958E32D-Aux[1]-NSStatusItemView] Dropping transition context because the scene is reconnecting
default	17:24:03.441170-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.54878181.54878190(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	17:24:03.441931-0500	gamepolicyd	Received state update for 21495 (app<application.com.nexy.assistant.54878181.54878190(501)>, running-active-NotVisible
default	17:24:03.441951-0500	ControlCenter	[app<application.com.nexy.assistant.54878181.54878190>:21495] Bootstrap success!
default	17:24:03.442368-0500	ControlCenter	[app<application.com.nexy.assistant.54878181.54878190>:21495] Setting process visibility to: Background
default	17:24:03.442425-0500	ControlCenter	[app<application.com.nexy.assistant.54878181.54878190>:21495] No launch watchdog for this process, dropping initial assertion in 2.0s
default	17:24:03.442682-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.54878181.54878190(501)>:21495] from originator [osservice<com.apple.controlcenter(501)>:615] with description <RBSAssertionDescriptor| "FBWorkspaceDomain: injecting saved endowment" ID:400-615-17261 target:21495 attributes:[
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"WorkspaceEndpointInjection" sourceEnvironment:"(null)">
	]>
default	17:24:03.442744-0500	runningboardd	Assertion 400-615-17261 (target:[app<application.com.nexy.assistant.54878181.54878190(501)>:21495]) will be created as active
default	17:24:03.443094-0500	runningboardd	[app<application.com.nexy.assistant.54878181.54878190(501)>:21495] Ignoring jetsam update because this process is not memory-managed
default	17:24:03.443104-0500	runningboardd	[app<application.com.nexy.assistant.54878181.54878190(501)>:21495] Ignoring suspend because this process is not lifecycle managed
default	17:24:03.443114-0500	runningboardd	[app<application.com.nexy.assistant.54878181.54878190(501)>:21495] Ignoring GPU update because this process is not GPU managed
default	17:24:03.443169-0500	runningboardd	[app<application.com.nexy.assistant.54878181.54878190(501)>:21495] Ignoring memory limit update because this process is not memory-managed
default	17:24:03.443564-0500	Nexy	[com.apple.controlcenter:950C5067-8704-4062-917B-7F9E4958E32D-Aux[1]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
default	17:24:03.443578-0500	Nexy	[com.apple.controlcenter:950C5067-8704-4062-917B-7F9E4958E32D-Aux[1]-NSStatusItemView] Dropping transition context because the scene is reconnecting
default	17:24:03.443650-0500	Nexy	Warning: the app is using `-[NSStatusBarButton setHighlightsBy:]` to set the highlight behavior. Instead, consider removing that setting. That will enable macOS to highlight the status bar button as appropriate for all configurations (e.g., light, dark, and increased contrast modes).
default	17:24:03.446064-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.54878181.54878190(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	17:24:03.446427-0500	ControlCenter	Adding: <FBApplicationProcess: 0xc32031f80; app<application.com.nexy.assistant.54878181.54878190>:21495(v79BBE2)>
default	17:24:03.446607-0500	gamepolicyd	Received state update for 21495 (app<application.com.nexy.assistant.54878181.54878190(501)>, running-active-NotVisible
default	17:24:03.446835-0500	ControlCenter	[app<application.com.nexy.assistant.54878181.54878190>:21495] Connection established.
default	17:24:03.446903-0500	ControlCenter	[app<application.com.nexy.assistant.54878181.54878190>:21495] created proxy of <BSXPCServiceConnectionProxy<FBSWorkspaceServiceServerInterface>: 0xc34a16ed0>
default	17:24:03.446973-0500	ControlCenter	[app<application.com.nexy.assistant.54878181.54878190>:21495] Connection to remote process established!
default	17:24:03.447072-0500	ControlCenter	Received state update for 21495 (app<application.com.nexy.assistant.54878181.54878190(501)>, running-active-NotVisible
default	17:24:03.448455-0500	Nexy	Registering for test daemon availability notify post.
default	17:24:03.448549-0500	Nexy	notify_get_state check indicated test daemon not ready.
default	17:24:03.448616-0500	Nexy	notify_get_state check indicated test daemon not ready.
default	17:24:03.448673-0500	Nexy	notify_get_state check indicated test daemon not ready.
default	17:24:03.449697-0500	Nexy	[0x836ac2440] activating connection: mach=true listener=false peer=false name=com.apple.coreservices.appleevents
default	17:24:03.451395-0500	ControlCenter	Asked to bootstrap a new process for handle: [app<application.com.nexy.assistant.54878181.54878190(501)>:21495]
default	17:24:03.451412-0500	ControlCenter	A process already exists for this handle: <FBApplicationProcess: 0xc32031f80; app<application.com.nexy.assistant.54878181.54878190>:21495(v79BBE2)>
default	17:24:03.451502-0500	ControlCenter	[app<application.com.nexy.assistant.54878181.54878190>:21495] Registered new scene: <FBWorkspaceScene: 0xc346c4900; com.apple.controlcenter:950C5067-8704-4062-917B-7F9E4958E32D> (fromRemnant = 0)
default	17:24:03.451538-0500	ControlCenter	[app<application.com.nexy.assistant.54878181.54878190>:21495] Workspace interruption policy did change: reconnect
default	17:24:03.451692-0500	Nexy	Request for <FBSScene: 0x837d6ac60; com.apple.controlcenter:950C5067-8704-4062-917B-7F9E4958E32D> complete!
default	17:24:03.451694-0500	ControlCenter	[com.apple.controlcenter:950C5067-8704-4062-917B-7F9E4958E32D] Client process connected: [app<application.com.nexy.assistant.54878181.54878190(501)>:21495]
default	17:24:03.451802-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.54878181.54878190(501)>:21495] from originator [osservice<com.apple.controlcenter(501)>:615] with description <RBSAssertionDescriptor| "com.apple.frontboard.after-life.interrupted" ID:400-615-17262 target:21495 attributes:[
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"AfterLife-Interrupted" sourceEnvironment:"(null)">
	]>
default	17:24:03.451885-0500	runningboardd	Assertion 400-615-17262 (target:[app<application.com.nexy.assistant.54878181.54878190(501)>:21495]) will be created as inactive as originator process has not exited
default	17:24:03.452274-0500	ControlCenter	Asked to bootstrap a new process for handle: [app<application.com.nexy.assistant.54878181.54878190(501)>:21495]
default	17:24:03.452272-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.54878181.54878190(501)>:21495] from originator [osservice<com.apple.controlcenter(501)>:615] with description <RBSAssertionDescriptor| "FBWorkspace (BG-Active[40])" ID:400-615-17263 target:21495 attributes:[
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableLPRunReason-Suspend" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableRole-NonUI" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableJetsamPriority-Active" sourceEnvironment:"(null)">
	]>
default	17:24:03.452291-0500	ControlCenter	A process already exists for this handle: <FBApplicationProcess: 0xc32031f80; app<application.com.nexy.assistant.54878181.54878190>:21495(v79BBE2)>
default	17:24:03.452349-0500	ControlCenter	[app<application.com.nexy.assistant.54878181.54878190>:21495] Registered new scene: <FBWorkspaceScene: 0xc346c5440; com.apple.controlcenter:950C5067-8704-4062-917B-7F9E4958E32D-Aux[1]-NSStatusItemView> (fromRemnant = 0)
default	17:24:03.452372-0500	runningboardd	Assertion 400-615-17263 (target:[app<application.com.nexy.assistant.54878181.54878190(501)>:21495]) will be created as active
default	17:24:03.452485-0500	Nexy	Request for <FBSScene: 0x837d6ab20; com.apple.controlcenter:950C5067-8704-4062-917B-7F9E4958E32D-Aux[1]-NSStatusItemView> complete!
default	17:24:03.452461-0500	ControlCenter	[app<application.com.nexy.assistant.54878181.54878190>:21495] Workspace state did change: XX-None[0] --> BG-Active[40] (assertion acquired).
default	17:24:03.452487-0500	ControlCenter	[com.apple.controlcenter:950C5067-8704-4062-917B-7F9E4958E32D-Aux[1]-NSStatusItemView] Client process connected: [app<application.com.nexy.assistant.54878181.54878190(501)>:21495]
default	17:24:03.452667-0500	runningboardd	[app<application.com.nexy.assistant.54878181.54878190(501)>:21495] Ignoring jetsam update because this process is not memory-managed
default	17:24:03.452903-0500	Nexy	<FBSWorkspaceScenesClient:0x837d6a800 <private>> Reconnecting scene com.apple.controlcenter:950C5067-8704-4062-917B-7F9E4958E32D
default	17:24:03.452716-0500	runningboardd	[app<application.com.nexy.assistant.54878181.54878190(501)>:21495] Ignoring suspend because this process is not lifecycle managed
default	17:24:03.452814-0500	runningboardd	[app<application.com.nexy.assistant.54878181.54878190(501)>:21495] Ignoring GPU update because this process is not GPU managed
default	17:24:03.452969-0500	runningboardd	[app<application.com.nexy.assistant.54878181.54878190(501)>:21495] Ignoring memory limit update because this process is not memory-managed
default	17:24:03.453201-0500	Nexy	<FBSWorkspaceScenesClient:0x837d6a800 <private>> Reconnecting scene com.apple.controlcenter:950C5067-8704-4062-917B-7F9E4958E32D-Aux[1]-NSStatusItemView
default	17:24:03.455866-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.54878181.54878190(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	17:24:03.456310-0500	ControlCenter	Received state update for 21495 (app<application.com.nexy.assistant.54878181.54878190(501)>, running-active-NotVisible
default	17:24:03.456460-0500	gamepolicyd	Received state update for 21495 (app<application.com.nexy.assistant.54878181.54878190(501)>, running-active-NotVisible
default	17:24:03.458039-0500	Nexy	[0x836ac03c0] Connection returned listener port: 0x4e03
default	17:24:03.458352-0500	Nexy	SignalReady: pid=21495 asn=0x0-0x215215
default	17:24:03.458647-0500	Nexy	SIGNAL: pid=21495 asn=0x0x-0x215215
default	17:24:03.459323-0500	loginwindow	-[Application _updateInformationInternal] | Got App URL: file:///Applications/Nexy.app/
default	17:24:03.461986-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b5164000 at /Applications/Nexy.app
default	17:24:03.464791-0500	Nexy	[com.apple.controlcenter:950C5067-8704-4062-917B-7F9E4958E32D-Aux[1]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
default	17:24:03.466265-0500	Nexy	[com.apple.controlcenter:950C5067-8704-4062-917B-7F9E4958E32D-Aux[1]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
default	17:24:03.467339-0500	Nexy	void _NSDisableAutomaticTerminationAndLog(NSString *) Restoring windows
default	17:24:03.467344-0500	Nexy	-[NSApplication _reopenWindowsAsNecessaryIncludingRestorableState:withFullFidelity:completionHandler:] shouldRestoreState=1 hasPersistentStateToRestore=0 shouldStillRestoreStateAfterPrompting=0
default	17:24:03.467353-0500	Nexy	[0x836ac12c0] activating connection: mach=true listener=false peer=false name=com.apple.window_proxies
default	17:24:03.467405-0500	Nexy	[0x836ac12c0] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	17:24:03.468097-0500	Nexy	void _NSEnableAutomaticTerminationAndLog(NSString *) Restoring windows
default	17:24:03.469619-0500	ControlCenter	Host properties initialized; (bid:com.nexy.assistant-Item-0-21495). State(applicationItem: true, clientRequestsVisibility: true, neverClip: false)
default	17:24:03.469835-0500	Nexy	[C:2] Alloc <private>
default	17:24:03.469852-0500	Nexy	[0x836ac12c0] activating connection: mach=false listener=false peer=false name=(anonymous)
default	17:24:03.470356-0500	ControlCenter	Starting to track host; (bid:com.nexy.assistant-Item-0-21495)
default	17:24:03.470396-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.54878181.54878190(501)>:21495] from originator [app<application.com.nexy.assistant.54878181.54878190(501)>:21495] with description <RBSAssertionDescriptor| "AudioHAL" ID:400-21495-17264 target:21495 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	17:24:03.470437-0500	runningboardd	Assertion 400-21495-17264 (target:[app<application.com.nexy.assistant.54878181.54878190(501)>:21495]) will be created as active
default	17:24:03.470448-0500	ControlCenter	Created new displayable type DisplayableAppStatusItemType(0D5C0513, (bid:com.nexy.assistant-Item-0-21495)) for (bid:com.nexy.assistant-Item-0-21495)
default	17:24:03.470706-0500	runningboardd	[app<application.com.nexy.assistant.54878181.54878190(501)>:21495] Ignoring jetsam update because this process is not memory-managed
default	17:24:03.470767-0500	runningboardd	[app<application.com.nexy.assistant.54878181.54878190(501)>:21495] Ignoring suspend because this process is not lifecycle managed
default	17:24:03.470824-0500	runningboardd	[app<application.com.nexy.assistant.54878181.54878190(501)>:21495] Ignoring GPU update because this process is not GPU managed
default	17:24:03.470990-0500	runningboardd	[app<application.com.nexy.assistant.54878181.54878190(501)>:21495] Ignoring memory limit update because this process is not memory-managed
default	17:24:03.470989-0500	ControlCenter	Adding displayable items for status items; [(bid:com.nexy.assistant-Item-0-21495)]
default	17:24:03.471043-0500	ControlCenter	Created instance DisplayableId(B14481AF) in .menuBar for DisplayableAppStatusItemType(0D5C0513, (bid:com.nexy.assistant-Item-0-21495)) .menuBar
default	17:24:03.470968-0500	WindowManager	Connection activated | (21495) Nexy
default	17:24:03.474714-0500	Nexy	[com.apple.controlcenter:950C5067-8704-4062-917B-7F9E4958E32D-Aux[1]-NSStatusItemView] Received action(s) in scene-update: NSSceneFenceAction
default	17:24:03.475337-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.54878181.54878190(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	17:24:03.475701-0500	ControlCenter	Created ephemaral instance DisplayableId(B14481AF) for (bid:com.nexy.assistant-Item-0-21495) with positioning .ephemeral
default	17:24:03.475740-0500	ControlCenter	Received state update for 21495 (app<application.com.nexy.assistant.54878181.54878190(501)>, running-active-NotVisible
default	17:24:03.475810-0500	gamepolicyd	Received state update for 21495 (app<application.com.nexy.assistant.54878181.54878190(501)>, running-active-NotVisible
default	17:24:03.475970-0500	Nexy	[com.apple.controlcenter:950C5067-8704-4062-917B-7F9E4958E32D-Aux[1]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
error	17:24:03.476242-0500	Nexy	It's not legal to call -layoutSubtreeIfNeeded on a view which is already being laid out.  If you are implementing the view's -layout method, you can call -[super layout] instead.  Break on void _NSDetectedLayoutRecursion(void) to debug.  This will be logged only once.  This may break in the future.
default	17:24:03.476313-0500	Nexy	[com.apple.controlcenter:950C5067-8704-4062-917B-7F9E4958E32D-Aux[1]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
default	17:24:03.496948-0500	Nexy	[com.apple.controlcenter:950C5067-8704-4062-917B-7F9E4958E32D] Sending action(s) in update: NSSceneFenceAction
default	17:24:03.529407-0500	runningboardd	[app<application.com.nexy.assistant.54878181.54878190(501)>:21495] Ignoring jetsam update because this process is not memory-managed
default	17:24:03.529417-0500	runningboardd	[app<application.com.nexy.assistant.54878181.54878190(501)>:21495] Ignoring suspend because this process is not lifecycle managed
default	17:24:03.529423-0500	runningboardd	[app<application.com.nexy.assistant.54878181.54878190(501)>:21495] Ignoring GPU update because this process is not GPU managed
default	17:24:03.529437-0500	runningboardd	[app<application.com.nexy.assistant.54878181.54878190(501)>:21495] Ignoring memory limit update because this process is not memory-managed
default	17:24:03.531905-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.54878181.54878190(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	17:24:03.532275-0500	ControlCenter	Received state update for 21495 (app<application.com.nexy.assistant.54878181.54878190(501)>, running-active-NotVisible
default	17:24:03.532396-0500	gamepolicyd	Received state update for 21495 (app<application.com.nexy.assistant.54878181.54878190(501)>, running-active-NotVisible
default	17:24:03.630253-0500	Nexy	*warn* MailCS ======%%% _setMailMessageAttributes skip:1
default	17:24:03.633713-0500	Nexy	Start service name com.apple.spotlightknowledged
default	17:24:03.634522-0500	Nexy	[GMS] availability notification token 86
default	17:24:03.682975-0500	ControlCenter	[app<application.com.nexy.assistant.54878181.54878190>:21495] Workspace state did change: BG-Active[40] --> XX-None[0] (assertion dropped).
default	17:24:03.683103-0500	runningboardd	Invalidating assertion 400-615-17263 (target:[app<application.com.nexy.assistant.54878181.54878190(501)>:21495]) from originator [osservice<com.apple.controlcenter(501)>:615]
default	17:24:03.787257-0500	runningboardd	[app<application.com.nexy.assistant.54878181.54878190(501)>:21495] Ignoring jetsam update because this process is not memory-managed
default	17:24:03.787286-0500	runningboardd	[app<application.com.nexy.assistant.54878181.54878190(501)>:21495] Ignoring suspend because this process is not lifecycle managed
default	17:24:03.787324-0500	runningboardd	[app<application.com.nexy.assistant.54878181.54878190(501)>:21495] Ignoring GPU update because this process is not GPU managed
default	17:24:03.787369-0500	runningboardd	[app<application.com.nexy.assistant.54878181.54878190(501)>:21495] Ignoring memory limit update because this process is not memory-managed
default	17:24:03.792728-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.54878181.54878190(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	17:24:03.793452-0500	ControlCenter	Received state update for 21495 (app<application.com.nexy.assistant.54878181.54878190(501)>, running-active-NotVisible
default	17:24:03.793709-0500	gamepolicyd	Received state update for 21495 (app<application.com.nexy.assistant.54878181.54878190(501)>, running-active-NotVisible
default	17:24:03.974169-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.54878181.54878190(501)>:21495] from originator [osservice<com.apple.WindowServer(88)>:391] with description <RBSAssertionDescriptor| "AppDrawing" ID:400-391-17265 target:21495 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"AppDrawing" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	17:24:03.974329-0500	runningboardd	Assertion 400-391-17265 (target:[app<application.com.nexy.assistant.54878181.54878190(501)>:21495]) will be created as active
default	17:24:03.974812-0500	runningboardd	[app<application.com.nexy.assistant.54878181.54878190(501)>:21495] Ignoring jetsam update because this process is not memory-managed
default	17:24:03.974826-0500	runningboardd	[app<application.com.nexy.assistant.54878181.54878190(501)>:21495] Ignoring suspend because this process is not lifecycle managed
default	17:24:03.974838-0500	runningboardd	[app<application.com.nexy.assistant.54878181.54878190(501)>:21495] Ignoring GPU update because this process is not GPU managed
default	17:24:03.974862-0500	runningboardd	[app<application.com.nexy.assistant.54878181.54878190(501)>:21495] Ignoring memory limit update because this process is not memory-managed
default	17:24:03.979393-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.54878181.54878190(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	17:24:03.980016-0500	ControlCenter	Received state update for 21495 (app<application.com.nexy.assistant.54878181.54878190(501)>, running-active-NotVisible
default	17:24:03.980242-0500	gamepolicyd	Received state update for 21495 (app<application.com.nexy.assistant.54878181.54878190(501)>, running-active-NotVisible
default	17:24:03.993669-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Speaker App com.nexy.assistant, Score 201, Remote -1 NumofApp 2
default	17:24:05.536062-0500	runningboardd	Invalidating assertion 400-615-17260 (target:app<application.com.nexy.assistant.54878181.54878190(501)>) from originator [osservice<com.apple.controlcenter(501)>:615]
default	17:24:05.637794-0500	runningboardd	Removed last relative-start-date-defining assertion for process app<application.com.nexy.assistant.54878181.54878190(501)>
default	17:24:05.638602-0500	runningboardd	[app<application.com.nexy.assistant.54878181.54878190(501)>:21495] Ignoring jetsam update because this process is not memory-managed
default	17:24:05.638617-0500	runningboardd	[app<application.com.nexy.assistant.54878181.54878190(501)>:21495] Ignoring suspend because this process is not lifecycle managed
default	17:24:05.638628-0500	runningboardd	[app<application.com.nexy.assistant.54878181.54878190(501)>:21495] Ignoring GPU update because this process is not GPU managed
default	17:24:05.638649-0500	runningboardd	[app<application.com.nexy.assistant.54878181.54878190(501)>:21495] Ignoring memory limit update because this process is not memory-managed
default	17:24:05.642173-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.54878181.54878190(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	17:24:05.648354-0500	ControlCenter	Received state update for 21495 (app<application.com.nexy.assistant.54878181.54878190(501)>, running-active-NotVisible
default	17:24:05.649504-0500	gamepolicyd	Received state update for 21495 (app<application.com.nexy.assistant.54878181.54878190(501)>, running-active-NotVisible
default	17:24:06.993602-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Speaker App com.nexy.assistant, Score 201, Remote -1 NumofApp 2
default	17:24:08.413085-0500	Nexy	void _updateToReflectAutomaticTerminationState(void) Setting _kLSApplicationWouldBeTerminatedByTALKey=1
default	17:24:08.587857-0500	Nexy	NotifyToken::RegisterDispatch(user.uid.501.com.apple.LaunchServices.database) fired for session key <private>
default	17:24:09.986824-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Speaker App com.nexy.assistant, Score 201, Remote -1 NumofApp 2
default	17:24:10.839970-0500	Nexy	  AVAudioSession_MacOS.mm:883   Activating session
default	17:24:10.841186-0500	Nexy	[com.apple.controlcenter:950C5067-8704-4062-917B-7F9E4958E32D] Sending action(s) in update: NSSceneFenceAction
default	17:24:10.841344-0500	Nexy	                AUHAL.cpp:420   AUHAL: (0x839f4c040) Selecting device 71 from constructor
default	17:24:10.841351-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0x839f4c040)
default	17:24:10.841355-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0x839f4c040) not already running
default	17:24:10.841357-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0x839f4c040) nothing to teardown
default	17:24:10.841360-0500	Nexy	                AUHAL.cpp:762   SelectDevice: (0x839f4c040) connecting device 71
default	17:24:10.841468-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0x839f4c040) Device ID: 71 (Input:No | Output:Yes): true
default	17:24:10.841634-0500	Nexy	                AUHAL.cpp:774   SelectDevice: (0x839f4c040) created ioproc 0xb for device 71
default	17:24:10.841762-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x839f4c040) adding 7 device listeners to device 71
default	17:24:10.841943-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x839f4c040) adding 0 device delegate listeners to device 71
default	17:24:10.841958-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x839f4c040)
default	17:24:10.842035-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x48]:  2 ch,  48000 Hz, Float32, interleaved
default	17:24:10.842041-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	17:24:10.842045-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	17:24:10.842048-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	17:24:10.842055-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	17:24:10.842137-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x839f4c040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	17:24:10.842144-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x839f4c040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	17:24:10.842334-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	17:24:10.842369-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x839f4c040) removing 0 device listeners from device 0
default	17:24:10.842397-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x839f4c040) removing 0 device delegate listeners from device 0
default	17:24:10.842446-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0x839f4c040)
default	17:24:10.842475-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is DISABLED
default	17:24:10.842521-0500	Nexy	                AUHAL.cpp:2303  SetProperty: (0x839f4c040) caller requesting device change from 71 to 78
default	17:24:10.842526-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0x839f4c040)
default	17:24:10.842530-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0x839f4c040) not already running
default	17:24:10.842559-0500	Nexy	                AUHAL.cpp:687   SelectDevice: (0x839f4c040) disconnecting device 71
default	17:24:10.842577-0500	Nexy	                AUHAL.cpp:751   SelectDevice: (0x839f4c040) destroying ioproc 0xb for device 71
default	17:24:10.842605-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped Unknown {BuiltInSpeakerDevice, 0xb}
default	17:24:10.842796-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 1]. BT device UIDS: {(
)} Server update was not required.
default	17:24:10.842901-0500	Nexy	                AUHAL.cpp:762   SelectDevice: (0x839f4c040) connecting device 78
default	17:24:10.842972-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0x839f4c040) Device ID: 78 (Input:Yes | Output:No): true
default	17:24:10.843920-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.970, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=21495, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=392, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	17:24:10.845299-0500	tccd	AUTHREQ_SUBJECT: msgID=401.970, subject=com.nexy.assistant,
default	17:24:10.845834-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x722e70900 at /Applications/Nexy.app
default	17:24:10.856754-0500	Nexy	[0x836ac26c0] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	17:24:10.857120-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=21495.3, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=21495, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	17:24:10.857803-0500	tccd	AUTHREQ_SUBJECT: msgID=21495.3, subject=com.nexy.assistant,
default	17:24:10.858254-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b5164900 at /Applications/Nexy.app
default	17:24:10.861152-0500	Nexy	                AUHAL.cpp:774   SelectDevice: (0x839f4c040) created ioproc 0xa for device 78
default	17:24:10.861227-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x839f4c040) adding 7 device listeners to device 78
default	17:24:10.861361-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x839f4c040) adding 0 device delegate listeners to device 78
default	17:24:10.861367-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x839f4c040)
default	17:24:10.861373-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 output streams; not all mono
default	17:24:10.861381-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	17:24:10.861460-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  input stream 0 [0x4f]:  1 ch,  44100 Hz, Float32
default	17:24:10.861466-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 input streams; all mono
default	17:24:10.861470-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  1 ch,  44100 Hz, Float32
default	17:24:10.861527-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x839f4c040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	17:24:10.861537-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x839f4c040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	17:24:10.861541-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	17:24:10.861545-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x839f4c040) removing 7 device listeners from device 71
default	17:24:10.861660-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x839f4c040) removing 0 device delegate listeners from device 71
default	17:24:10.861666-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0x839f4c040)
default	17:24:10.861942-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	17:24:10.862607-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.971, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=21495, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=392, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	17:24:10.863337-0500	tccd	AUTHREQ_SUBJECT: msgID=401.971, subject=com.nexy.assistant,
default	17:24:10.863769-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x722e70900 at /Applications/Nexy.app
default	17:24:10.872766-0500	Nexy	[0x836ac26c0] invalidated after the last release of the connection object
default	17:24:10.872903-0500	Nexy	[0x836ac2800] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	17:24:10.873205-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=21495.4, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=21495, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	17:24:10.873944-0500	tccd	AUTHREQ_SUBJECT: msgID=21495.4, subject=com.nexy.assistant,
default	17:24:10.874372-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b5164900 at /Applications/Nexy.app
default	17:24:10.875746-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	17:24:10.876341-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.972, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=21495, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=392, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	17:24:10.876928-0500	tccd	AUTHREQ_SUBJECT: msgID=401.972, subject=com.nexy.assistant,
default	17:24:10.877279-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x722e70900 at /Applications/Nexy.app
default	17:24:10.888551-0500	Nexy	[0x836ac2800] invalidated after the last release of the connection object
default	17:24:10.888576-0500	Nexy	 [INFO] SLSHWCaptureDesktopProxying:485 request: <private>
default	17:24:10.888593-0500	Nexy	 [INFO] SLSHWCaptureDesktopProxying:485 request: <private>
default	17:24:10.888848-0500	Nexy	[0x836ac2800] activating connection: mach=true listener=false peer=false name=com.apple.replayd
default	17:24:10.888911-0500	Nexy	 [INFO] -[RPDaemonProxy consumeSandboxExtension:processNewConnection:]:568
default	17:24:10.888969-0500	Nexy	 [INFO] -[RPDaemonProxy proxyCoreGraphicsWithMethodType:config:machPort:completionHandler:]:1493
default	17:24:10.888978-0500	Nexy	 [INFO] -[RPDaemonProxy proxyCoreGraphicsWithMethodType:config:machPort:completionHandler:]:1493
default	17:24:10.890191-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=21333.3, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=21495, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.replayd, pid=21333, auid=501, euid=501, binary_path=/usr/libexec/replayd}, },
default	17:24:10.890208-0500	tccd	requestor: TCCDProcess: identifier=com.apple.replayd, pid=21333, auid=501, euid=501, binary_path=/usr/libexec/replayd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=21495, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	17:24:10.890860-0500	tccd	AUTHREQ_SUBJECT: msgID=21333.3, subject=com.nexy.assistant,
default	17:24:10.891172-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.973, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=21495, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=392, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	17:24:10.891587-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b5164900 at /Applications/Nexy.app
default	17:24:10.891799-0500	tccd	AUTHREQ_SUBJECT: msgID=401.973, subject=com.nexy.assistant,
default	17:24:10.892138-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x722e70900 at /Applications/Nexy.app
default	17:24:10.906888-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=391.926, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=21495, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=391, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	17:24:10.906902-0500	tccd	requestor: TCCDProcess: identifier=com.apple.WindowServer, pid=391, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=21495, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	17:24:10.907332-0500	tccd	AUTHREQ_SUBJECT: msgID=391.926, subject=com.nexy.assistant,
default	17:24:10.908241-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b5164900 at /Applications/Nexy.app
default	17:24:10.929892-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Input {BuiltInMicrophoneDevice, 0xa}
default	17:24:10.930455-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1f402a","name":"Nexy(21495)"}, "details":{"deviceUIDs":[],"implicit_category":"PlayAndRecord","input_running":true,"output_running":true} }
default	17:24:10.930499-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 43, PID = 21495, Name = sid:0x1f402a, Nexy(21495), 'prim', BundleID = com.nexy.assistant, Category = PlayAndRecord_WithBluetooth, Mode = Default, Active = YES, Playing = YES, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	17:24:10.930512-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Category/Mode changed -- The score for sid:0x1f402a, Nexy(21495), 'prim'/com.nexy.assistant was not correct. Old score = 201
default	17:24:10.930527-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 43, PID = 21495, Name = sid:0x1f402a, Nexy(21495), 'prim', BundleID = com.nexy.assistant, Category = PlayAndRecord_WithBluetooth, Mode = Default, Active = YES, Playing = YES, Recording = NO>
default	17:24:10.930541-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1f402a, Nexy(21495), 'prim'', displayID:'com.nexy.assistant'}
default	17:24:10.930571-0500	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1f402a, Nexy(21495), 'prim'', AudioCategory changed to 'PlayAndRecord_WithBluetooth'
default	17:24:10.930737-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 201,
}
default	17:24:10.930620-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 43, PID = 21495, Name = sid:0x1f402a, Nexy(21495), 'prim', BundleID = com.nexy.assistant, Category = PlayAndRecord_WithBluetooth, Mode = Default, Active = YES, Playing = YES, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	17:24:10.930757-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	17:24:10.930630-0500	audiomxd	UpdateAudioState CID 0x91550001 audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	17:24:10.930771-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 201
default	17:24:10.930680-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 43, PID = 21495, Name = sid:0x1f402a, Nexy(21495), 'prim', BundleID = com.nexy.assistant, Category = PlayAndRecord_WithBluetooth, Mode = Default, Active = YES, Playing = YES, Recording = NO>
default	17:24:10.930789-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.nexy.assistant
default	17:24:10.930704-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1f402a, Nexy(21495), 'prim'', displayID:'com.nexy.assistant'}
default	17:24:10.930860-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 43, PID = 21495, Name = sid:0x1f402a, Nexy(21495), 'prim', BundleID = com.nexy.assistant, Category = PlayAndRecord_WithBluetooth, Mode = Default, Active = YES, Playing = YES, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	17:24:10.930876-0500	audiomxd	UpdateAudioState CID 0x91550001 audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	17:24:10.930978-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 201,
}
default	17:24:10.930927-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 43, PID = 21495, Name = sid:0x1f402a, Nexy(21495), 'prim', BundleID = com.nexy.assistant, Category = PlayAndRecord_WithBluetooth, Mode = Default, Active = YES, Playing = YES, Recording = NO>
default	17:24:10.930991-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	17:24:10.931006-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 201
default	17:24:10.930967-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1f402a, Nexy(21495), 'prim'', displayID:'com.nexy.assistant'}
default	17:24:10.931024-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.nexy.assistant
default	17:24:10.931061-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 201,
}
default	17:24:10.931071-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 201,
}
fault	17:24:10.931108-0500	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.54878181.54878190 AUID=501> and <type=Application identifier=application.com.nexy.assistant.54878181.54878190>
default	17:24:10.931082-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 201
default	17:24:10.931009-0500	audiomxd	UpdateAudioState CID 0x91550001 audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	17:24:10.931093-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.nexy.assistant
default	17:24:10.931010-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1f402a, Nexy(21495), 'prim' with category(PlayAndRecord_WithBluetooth)/mode(Default) and coreSessionID = 43 starting recording
default	17:24:10.931071-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: Bumping the mode to Voice chat for session as session started recording = <ID: 43, PID = 21495, Name = sid:0x1f402a, Nexy(21495), 'prim', BundleID = com.nexy.assistant, Category = PlayAndRecord_WithBluetooth, Mode = Default, Active = YES, Playing = YES, Recording = YES>
default	17:24:10.931126-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 43, PID = 21495, Name = sid:0x1f402a, Nexy(21495), 'prim', BundleID = com.nexy.assistant, Category = PlayAndRecord_WithBluetooth, Mode = VoiceChat, Active = YES, Playing = YES, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	17:24:10.931153-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Category/Mode changed -- The score for sid:0x1f402a, Nexy(21495), 'prim'/com.nexy.assistant was not correct. Old score = 201
default	17:24:10.931224-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 501 for session <ID: 43, PID = 21495, Name = sid:0x1f402a, Nexy(21495), 'prim', BundleID = com.nexy.assistant, Category = PlayAndRecord_WithBluetooth, Mode = VoiceChat, Active = YES, Playing = YES, Recording = YES>
default	17:24:10.931247-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1f402a, Nexy(21495), 'prim'', displayID:'com.nexy.assistant'}
default	17:24:10.931271-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Will try to see if we can get the shared route for session = <ID: 43, PID = 21495, Name = sid:0x1f402a, Nexy(21495), 'prim', BundleID = com.nexy.assistant, Category = PlayAndRecord_WithBluetooth, Mode = VoiceChat, Active = YES, Playing = YES, Recording = YES>. Old (201) and New (501) scores.
default	17:24:10.931337-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [1, 1]. BT device UIDS: {(
)}
default	17:24:10.931344-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	17:24:10.931318-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 501, deviceID = <private>
default	17:24:10.931432-0500	audioaccessoryd	Routing request Wx NULL score 501 flag 0x1 < Hijack > app com.nexy.assistant CID 0x91550001 category Not set
default	17:24:10.931523-0500	audiomxd	UpdateAudioState CID 0x91550001 audioState Start apps {
    "com.nexy.assistant" : 501,
}
default	17:24:10.931560-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 501,
}
default	17:24:10.931571-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 501,
}
default	17:24:10.931581-0500	audioaccessoryd	AudioStateChanged: Added audio session app com.nexy.assistant 201 -> 501 count 2
default	17:24:10.931587-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 501
error	17:24:10.931592-0500	audioaccessoryd	Updating local audio category 201 -> 501 app com.nexy.assistant
default	17:24:10.931607-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 501 App com.nexy.assistant
fault	17:24:10.932342-0500	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.54878181.54878190 AUID=501> and <type=Application identifier=application.com.nexy.assistant.54878181.54878190>
default	17:24:10.949008-0500	Nexy	 [INFO] SLSHWCaptureDesktopProxying_block_invoke:506 request: <private>, error: (null), windowInfo: (null)
default	17:24:10.949599-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=21333.4, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=21495, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.replayd, pid=21333, auid=501, euid=501, binary_path=/usr/libexec/replayd}, },
default	17:24:10.949613-0500	tccd	requestor: TCCDProcess: identifier=com.apple.replayd, pid=21333, auid=501, euid=501, binary_path=/usr/libexec/replayd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=21495, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	17:24:10.950195-0500	tccd	AUTHREQ_SUBJECT: msgID=21333.4, subject=com.nexy.assistant,
default	17:24:10.950797-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b5164900 at /Applications/Nexy.app
default	17:24:10.954690-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	17:24:10.954763-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	17:24:10.954801-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	17:24:10.955507-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	17:24:10.955517-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	17:24:10.955527-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	17:24:10.955533-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	17:24:10.955607-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	17:24:10.955663-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	17:24:10.956234-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	17:24:10.961512-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	17:24:10.961522-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	17:24:10.961533-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	17:24:10.961539-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	17:24:10.961545-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	17:24:10.961551-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	17:24:10.961621-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	17:24:10.961668-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	17:24:10.961678-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	17:24:10.961688-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	17:24:10.961694-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	17:24:10.961699-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	17:24:10.961705-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	17:24:10.961813-0500	ControlCenter	Navigating to new application [com.nexy.assistant]
default	17:24:10.964107-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	17:24:10.972930-0500	Nexy	 [INFO] SLSHWCaptureDesktopProxying_block_invoke:506 request: <private>, error: (null), windowInfo: (null)
default	17:24:10.973093-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	17:24:10.973227-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant), [scr] Nexy (com.nexy.assistant)]
default	17:24:10.973275-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant", "scr:com.nexy.assistant"]
default	17:24:10.987560-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	17:24:10.987572-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	17:24:10.987584-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	17:24:10.987591-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	17:24:10.987598-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	17:24:10.987606-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	17:24:10.987617-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	17:24:10.987628-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	17:24:10.987637-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	17:24:10.987644-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	17:24:10.987658-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	17:24:10.987664-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	17:24:10.987746-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	17:24:10.987864-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	17:24:10.987874-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	17:24:10.987881-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	17:24:10.987888-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	17:24:10.987895-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	17:24:10.987900-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	17:24:11.727005-0500	Nexy	[com.apple.controlcenter:950C5067-8704-4062-917B-7F9E4958E32D] Sending action(s) in update: NSSceneFenceAction
default	17:24:12.488303-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	17:24:12.495733-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {BuiltInMicrophoneDevice, 0xa}
default	17:24:12.497365-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1f402a","name":"Nexy(21495)"}, "details":{"deviceUIDs":[],"implicit_category":"MediaPlayback","input_running":false,"output_running":true} }
default	17:24:12.497559-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 43, PID = 21495, Name = sid:0x1f402a, Nexy(21495), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	17:24:12.497616-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Category/Mode changed -- The score for sid:0x1f402a, Nexy(21495), 'prim'/com.nexy.assistant was not correct. Old score = 501
default	17:24:12.497673-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 43, PID = 21495, Name = sid:0x1f402a, Nexy(21495), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = YES>
default	17:24:12.497724-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1f402a, Nexy(21495), 'prim'', displayID:'com.nexy.assistant'}
default	17:24:12.497795-0500	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1f402a, Nexy(21495), 'prim'', AudioCategory changed to 'MediaPlayback'
default	17:24:12.498063-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 43, PID = 21495, Name = sid:0x1f402a, Nexy(21495), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	17:24:12.498147-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 43, PID = 21495, Name = sid:0x1f402a, Nexy(21495), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = YES>
default	17:24:12.498270-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1f402a, Nexy(21495), 'prim'', displayID:'com.nexy.assistant'}
default	17:24:12.498549-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 43, PID = 21495, Name = sid:0x1f402a, Nexy(21495), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	17:24:12.498083-0500	audiomxd	UpdateAudioState CID 0x91550001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	17:24:12.498667-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 43, PID = 21495, Name = sid:0x1f402a, Nexy(21495), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = YES>
default	17:24:12.498769-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1f402a, Nexy(21495), 'prim'', displayID:'com.nexy.assistant'}
default	17:24:12.498907-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	17:24:12.498981-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	17:24:12.499011-0500	audioaccessoryd	AudioStateChanged: Added audio session app com.nexy.assistant 501 -> 200 count 2
default	17:24:12.498886-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1f402a, Nexy(21495), 'prim' with category(MediaPlayback)/mode(Default) and coreSessionID = 43 stopping recording
default	17:24:12.498905-0500	audiomxd	UpdateAudioState CID 0x91550001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	17:24:12.499043-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	17:24:12.499015-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 43, PID = 21495, Name = sid:0x1f402a, Nexy(21495), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
error	17:24:12.499068-0500	audioaccessoryd	Updating local audio category 501 -> 200 app com.nexy.assistant
default	17:24:12.499001-0500	audiomxd	UpdateAudioState CID 0x91550001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	17:24:12.499145-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 43, PID = 21495, Name = sid:0x1f402a, Nexy(21495), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO>
default	17:24:12.499099-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	17:24:12.499243-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	17:24:12.499286-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1f402a, Nexy(21495), 'prim'', displayID:'com.nexy.assistant'}
default	17:24:12.499274-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	17:24:12.499397-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	17:24:12.499428-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Will try to see if we can get the shared route for session = <ID: 43, PID = 21495, Name = sid:0x1f402a, Nexy(21495), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO>. Old (200) and New (201) scores.
default	17:24:12.499455-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	17:24:12.499484-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 201, deviceID = <private>
default	17:24:12.499538-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	17:24:12.499564-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	17:24:12.499943-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 1]. BT device UIDS: {(
)}
default	17:24:12.499634-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	17:24:12.499969-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	17:24:12.499912-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	17:24:12.499979-0500	audioaccessoryd	Routing request Wx NULL score 201 flag 0x1 < Hijack > app com.nexy.assistant CID 0x91550001 category Not set
default	17:24:12.500402-0500	audiomxd	UpdateAudioState CID 0x91550001 audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	17:24:12.500505-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 201,
}
default	17:24:12.500535-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	17:24:12.500550-0500	audioaccessoryd	AudioStateChanged: Added audio session app com.nexy.assistant 200 -> 201 count 2
default	17:24:12.500574-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 201
error	17:24:12.500585-0500	audioaccessoryd	Updating local audio category 200 -> 201 app com.nexy.assistant
default	17:24:12.500701-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.nexy.assistant
default	17:24:12.507621-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	17:24:12.507765-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant)]
default	17:24:12.507854-0500	ControlCenter	Active activity attributions changed to ["scr:com.nexy.assistant"]
default	17:24:12.507880-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	17:24:12.509061-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	17:24:12.509073-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	17:24:12.509087-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	17:24:12.509094-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	17:24:12.509103-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	17:24:12.509121-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	17:24:12.509232-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	17:24:12.509319-0500	Nexy	[com.apple.controlcenter:950C5067-8704-4062-917B-7F9E4958E32D] Sending action(s) in update: NSSceneFenceAction
default	17:24:12.602267-0500	Nexy	                AUHAL.cpp:473   ~AUHAL: (0x839f4c040) Selecting device 0 from destructor
default	17:24:12.602286-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0x839f4c040)
default	17:24:12.602308-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0x839f4c040) not already running
default	17:24:12.602314-0500	Nexy	                AUHAL.cpp:687   SelectDevice: (0x839f4c040) disconnecting device 78
default	17:24:12.602324-0500	Nexy	                AUHAL.cpp:751   SelectDevice: (0x839f4c040) destroying ioproc 0xa for device 78
default	17:24:12.602391-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {BuiltInMicrophoneDevice, 0xa}
default	17:24:12.602958-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 1]. BT device UIDS: {(
)} Server update was not required.
default	17:24:12.603152-0500	Nexy	                AUHAL.cpp:853   SelectDevice: (0x839f4c040) nothing to setup
default	17:24:12.603171-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x839f4c040) adding 0 device listeners to device 0
default	17:24:12.603178-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x839f4c040) adding 0 device delegate listeners to device 0
default	17:24:12.603185-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x839f4c040) removing 7 device listeners from device 78
default	17:24:12.603466-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x839f4c040) removing 0 device delegate listeners from device 78
default	17:24:12.603482-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0x839f4c040)
default	17:24:12.993532-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Speaker App com.nexy.assistant, Score 201, Remote -1 NumofApp 2
default	17:24:13.856476-0500	Nexy	                AUHAL.cpp:420   AUHAL: (0x83a050e40) Selecting device 71 from constructor
default	17:24:13.856542-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0x83a050e40)
default	17:24:13.856559-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0x83a050e40) not already running
default	17:24:13.856565-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0x83a050e40) nothing to teardown
default	17:24:13.856574-0500	Nexy	                AUHAL.cpp:762   SelectDevice: (0x83a050e40) connecting device 71
default	17:24:13.856729-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0x83a050e40) Device ID: 71 (Input:No | Output:Yes): true
default	17:24:13.857073-0500	Nexy	                AUHAL.cpp:774   SelectDevice: (0x83a050e40) created ioproc 0xc for device 71
default	17:24:13.857239-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x83a050e40) adding 7 device listeners to device 71
default	17:24:13.857244-0500	Nexy	 [INFO] SLSHWCaptureDesktopProxying:485 request: <private>
default	17:24:13.857305-0500	Nexy	 [INFO] -[RPDaemonProxy proxyCoreGraphicsWithMethodType:config:machPort:completionHandler:]:1493
default	17:24:13.857522-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x83a050e40) adding 0 device delegate listeners to device 71
default	17:24:13.857539-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x83a050e40)
default	17:24:13.857687-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x48]:  2 ch,  48000 Hz, Float32, interleaved
default	17:24:13.857703-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	17:24:13.857712-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	17:24:13.857722-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	17:24:13.857734-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	17:24:13.857872-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x83a050e40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	17:24:13.857914-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x83a050e40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	17:24:13.857923-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	17:24:13.857933-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x83a050e40) removing 0 device listeners from device 0
default	17:24:13.857942-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x83a050e40) removing 0 device delegate listeners from device 0
default	17:24:13.857949-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0x83a050e40)
default	17:24:13.858120-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is DISABLED
default	17:24:13.858243-0500	Nexy	                AUHAL.cpp:2303  SetProperty: (0x83a050e40) caller requesting device change from 71 to 78
default	17:24:13.858256-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0x83a050e40)
default	17:24:13.858280-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0x83a050e40) not already running
default	17:24:13.858285-0500	Nexy	                AUHAL.cpp:687   SelectDevice: (0x83a050e40) disconnecting device 71
default	17:24:13.858293-0500	Nexy	                AUHAL.cpp:751   SelectDevice: (0x83a050e40) destroying ioproc 0xc for device 71
default	17:24:13.858315-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped Unknown {BuiltInSpeakerDevice, 0xc}
default	17:24:13.858659-0500	Nexy	[com.apple.controlcenter:950C5067-8704-4062-917B-7F9E4958E32D] Sending action(s) in update: NSSceneFenceAction
default	17:24:13.858741-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 1]. BT device UIDS: {(
)} Server update was not required.
default	17:24:13.858978-0500	Nexy	                AUHAL.cpp:762   SelectDevice: (0x83a050e40) connecting device 78
default	17:24:13.859152-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0x83a050e40) Device ID: 78 (Input:Yes | Output:No): true
default	17:24:13.860029-0500	Nexy	LSExceptions shared instance invalidated for timeout.
default	17:24:13.860452-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=21333.5, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=21495, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.replayd, pid=21333, auid=501, euid=501, binary_path=/usr/libexec/replayd}, },
default	17:24:13.860657-0500	tccd	requestor: TCCDProcess: identifier=com.apple.replayd, pid=21333, auid=501, euid=501, binary_path=/usr/libexec/replayd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=21495, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	17:24:13.861449-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.974, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=21495, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=392, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	17:24:13.863131-0500	tccd	AUTHREQ_SUBJECT: msgID=21333.5, subject=com.nexy.assistant,
default	17:24:13.863568-0500	tccd	AUTHREQ_SUBJECT: msgID=401.974, subject=com.nexy.assistant,
default	17:24:13.864351-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b5164900 at /Applications/Nexy.app
default	17:24:13.864631-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x722e70900 at /Applications/Nexy.app
default	17:24:13.887129-0500	Nexy	                AUHAL.cpp:774   SelectDevice: (0x83a050e40) created ioproc 0xb for device 78
default	17:24:13.887265-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x83a050e40) adding 7 device listeners to device 78
default	17:24:13.887437-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x83a050e40) adding 0 device delegate listeners to device 78
default	17:24:13.887445-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x83a050e40)
default	17:24:13.887454-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 output streams; not all mono
default	17:24:13.887464-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	17:24:13.887579-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  input stream 0 [0x4f]:  1 ch,  44100 Hz, Float32
default	17:24:13.887588-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 input streams; all mono
default	17:24:13.887593-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  1 ch,  44100 Hz, Float32
default	17:24:13.887667-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x83a050e40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	17:24:13.887677-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x83a050e40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	17:24:13.887682-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	17:24:13.887687-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x83a050e40) removing 7 device listeners from device 71
default	17:24:13.887821-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x83a050e40) removing 0 device delegate listeners from device 71
default	17:24:13.887828-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0x83a050e40)
default	17:24:13.887835-0500	Nexy	AudioHardware-mac-imp.cpp:1306   AudioObjectAddPropertyListener: listener was already added
default	17:24:13.888115-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	17:24:13.889060-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.975, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=21495, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=392, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	17:24:13.889916-0500	tccd	AUTHREQ_SUBJECT: msgID=401.975, subject=com.nexy.assistant,
default	17:24:13.890443-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x722e70900 at /Applications/Nexy.app
default	17:24:13.893713-0500	Nexy	 [INFO] SLSHWCaptureDesktopProxying:485 request: <private>
default	17:24:13.893731-0500	Nexy	 [INFO] -[RPDaemonProxy proxyCoreGraphicsWithMethodType:config:machPort:completionHandler:]:1493
default	17:24:13.896265-0500	Nexy	 [INFO] SLSHWCaptureDesktopProxying_block_invoke:506 request: <private>, error: (null), windowInfo: (null)
default	17:24:13.896930-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=21333.6, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=21495, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.replayd, pid=21333, auid=501, euid=501, binary_path=/usr/libexec/replayd}, },
default	17:24:13.896949-0500	tccd	requestor: TCCDProcess: identifier=com.apple.replayd, pid=21333, auid=501, euid=501, binary_path=/usr/libexec/replayd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=21495, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	17:24:13.897612-0500	tccd	AUTHREQ_SUBJECT: msgID=21333.6, subject=com.nexy.assistant,
default	17:24:13.898118-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b5164900 at /Applications/Nexy.app
default	17:24:13.904777-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	17:24:13.905500-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.976, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=21495, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=392, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	17:24:13.906263-0500	tccd	AUTHREQ_SUBJECT: msgID=401.976, subject=com.nexy.assistant,
default	17:24:13.906668-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x722e70900 at /Applications/Nexy.app
default	17:24:13.918730-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.977, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=21495, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=392, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	17:24:13.919599-0500	tccd	AUTHREQ_SUBJECT: msgID=401.977, subject=com.nexy.assistant,
default	17:24:13.920201-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x722e70900 at /Applications/Nexy.app
default	17:24:13.920332-0500	Nexy	 [INFO] SLSHWCaptureDesktopProxying_block_invoke:506 request: <private>, error: (null), windowInfo: (null)
default	17:24:13.957618-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Input {BuiltInMicrophoneDevice, 0xb}
default	17:24:13.958179-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1f402a","name":"Nexy(21495)"}, "details":{"deviceUIDs":[],"implicit_category":"PlayAndRecord","input_running":true,"output_running":true} }
default	17:24:13.958225-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 43, PID = 21495, Name = sid:0x1f402a, Nexy(21495), 'prim', BundleID = com.nexy.assistant, Category = PlayAndRecord_WithBluetooth, Mode = Default, Active = YES, Playing = YES, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	17:24:13.958240-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Category/Mode changed -- The score for sid:0x1f402a, Nexy(21495), 'prim'/com.nexy.assistant was not correct. Old score = 201
default	17:24:13.958252-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 43, PID = 21495, Name = sid:0x1f402a, Nexy(21495), 'prim', BundleID = com.nexy.assistant, Category = PlayAndRecord_WithBluetooth, Mode = Default, Active = YES, Playing = YES, Recording = NO>
default	17:24:13.958270-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1f402a, Nexy(21495), 'prim'', displayID:'com.nexy.assistant'}
default	17:24:13.958308-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 43, PID = 21495, Name = sid:0x1f402a, Nexy(21495), 'prim', BundleID = com.nexy.assistant, Category = PlayAndRecord_WithBluetooth, Mode = Default, Active = YES, Playing = YES, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	17:24:13.958298-0500	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1f402a, Nexy(21495), 'prim'', AudioCategory changed to 'PlayAndRecord_WithBluetooth'
default	17:24:13.958360-0500	audiomxd	UpdateAudioState CID 0x91550001 audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	17:24:13.958394-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 43, PID = 21495, Name = sid:0x1f402a, Nexy(21495), 'prim', BundleID = com.nexy.assistant, Category = PlayAndRecord_WithBluetooth, Mode = Default, Active = YES, Playing = YES, Recording = NO>
default	17:24:13.958463-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 201,
}
default	17:24:13.958417-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1f402a, Nexy(21495), 'prim'', displayID:'com.nexy.assistant'}
default	17:24:13.958502-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	17:24:13.958540-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 201
default	17:24:13.958559-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 201,
}
default	17:24:13.958457-0500	audiomxd	UpdateAudioState CID 0x91550001 audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	17:24:13.958595-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.nexy.assistant
default	17:24:13.958496-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 43, PID = 21495, Name = sid:0x1f402a, Nexy(21495), 'prim', BundleID = com.nexy.assistant, Category = PlayAndRecord_WithBluetooth, Mode = Default, Active = YES, Playing = YES, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	17:24:13.958602-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	17:24:13.958561-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 43, PID = 21495, Name = sid:0x1f402a, Nexy(21495), 'prim', BundleID = com.nexy.assistant, Category = PlayAndRecord_WithBluetooth, Mode = Default, Active = YES, Playing = YES, Recording = NO>
default	17:24:13.958611-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 201
default	17:24:13.958642-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1f402a, Nexy(21495), 'prim'', displayID:'com.nexy.assistant'}
default	17:24:13.958658-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.nexy.assistant
default	17:24:13.958862-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 201,
}
default	17:24:13.958874-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	17:24:13.958775-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1f402a, Nexy(21495), 'prim' with category(PlayAndRecord_WithBluetooth)/mode(Default) and coreSessionID = 43 starting recording
default	17:24:13.958887-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 201
default	17:24:13.958728-0500	audiomxd	UpdateAudioState CID 0x91550001 audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	17:24:13.958899-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.nexy.assistant
default	17:24:13.958856-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: Bumping the mode to Voice chat for session as session started recording = <ID: 43, PID = 21495, Name = sid:0x1f402a, Nexy(21495), 'prim', BundleID = com.nexy.assistant, Category = PlayAndRecord_WithBluetooth, Mode = Default, Active = YES, Playing = YES, Recording = YES>
default	17:24:13.958900-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 43, PID = 21495, Name = sid:0x1f402a, Nexy(21495), 'prim', BundleID = com.nexy.assistant, Category = PlayAndRecord_WithBluetooth, Mode = VoiceChat, Active = YES, Playing = YES, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	17:24:13.958918-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Category/Mode changed -- The score for sid:0x1f402a, Nexy(21495), 'prim'/com.nexy.assistant was not correct. Old score = 201
default	17:24:13.958940-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 501 for session <ID: 43, PID = 21495, Name = sid:0x1f402a, Nexy(21495), 'prim', BundleID = com.nexy.assistant, Category = PlayAndRecord_WithBluetooth, Mode = VoiceChat, Active = YES, Playing = YES, Recording = YES>
default	17:24:13.958961-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1f402a, Nexy(21495), 'prim'', displayID:'com.nexy.assistant'}
default	17:24:13.958981-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Will try to see if we can get the shared route for session = <ID: 43, PID = 21495, Name = sid:0x1f402a, Nexy(21495), 'prim', BundleID = com.nexy.assistant, Category = PlayAndRecord_WithBluetooth, Mode = VoiceChat, Active = YES, Playing = YES, Recording = YES>. Old (201) and New (501) scores.
default	17:24:13.959059-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [1, 1]. BT device UIDS: {(
)}
default	17:24:13.959019-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 501, deviceID = <private>
default	17:24:13.959067-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	17:24:13.959132-0500	audioaccessoryd	Routing request Wx NULL score 501 flag 0x1 < Hijack > app com.nexy.assistant CID 0x91550001 category Not set
default	17:24:13.959256-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 501,
}
default	17:24:13.959219-0500	audiomxd	UpdateAudioState CID 0x91550001 audioState Start apps {
    "com.nexy.assistant" : 501,
}
default	17:24:13.959270-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 501,
}
default	17:24:13.959278-0500	audioaccessoryd	AudioStateChanged: Added audio session app com.nexy.assistant 201 -> 501 count 2
default	17:24:13.959285-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 501
error	17:24:13.959290-0500	audioaccessoryd	Updating local audio category 201 -> 501 app com.nexy.assistant
default	17:24:13.959301-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 501 App com.nexy.assistant
default	17:24:13.963006-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	17:24:13.966413-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	17:24:13.966474-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant), [mic] Nexy (com.nexy.assistant)]
default	17:24:13.966514-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant", "scr:com.nexy.assistant"]
default	17:24:13.967108-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	17:24:13.967118-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	17:24:13.967130-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	17:24:13.967139-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	17:24:13.967164-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	17:24:13.967176-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	17:24:13.967205-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	17:24:13.967215-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	17:24:13.967286-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	17:24:13.967314-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	17:24:13.967344-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	17:24:13.967398-0500	ControlCenter	Navigating to new application [com.nexy.assistant]
default	17:24:13.967391-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	17:24:13.967458-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	17:24:13.967479-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	17:24:13.967514-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	17:24:13.967641-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	17:24:13.967678-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	17:24:13.967709-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	17:24:13.967732-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	17:24:14.745393-0500	Nexy	[com.apple.controlcenter:950C5067-8704-4062-917B-7F9E4958E32D] Sending action(s) in update: NSSceneFenceAction
default	17:24:15.563107-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	17:24:15.577821-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {BuiltInMicrophoneDevice, 0xb}
default	17:24:15.580154-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1f402a","name":"Nexy(21495)"}, "details":{"deviceUIDs":[],"implicit_category":"MediaPlayback","input_running":false,"output_running":true} }
default	17:24:15.580321-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 43, PID = 21495, Name = sid:0x1f402a, Nexy(21495), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	17:24:15.580365-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Category/Mode changed -- The score for sid:0x1f402a, Nexy(21495), 'prim'/com.nexy.assistant was not correct. Old score = 501
default	17:24:15.580405-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 43, PID = 21495, Name = sid:0x1f402a, Nexy(21495), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = YES>
default	17:24:15.580420-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	17:24:15.580442-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1f402a, Nexy(21495), 'prim'', displayID:'com.nexy.assistant'}
default	17:24:15.580495-0500	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1f402a, Nexy(21495), 'prim'', AudioCategory changed to 'MediaPlayback'
default	17:24:15.580529-0500	audiomxd	UpdateAudioState CID 0x91550001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	17:24:15.580535-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 43, PID = 21495, Name = sid:0x1f402a, Nexy(21495), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	17:24:15.580600-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant)]
default	17:24:15.580579-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 43, PID = 21495, Name = sid:0x1f402a, Nexy(21495), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = YES>
default	17:24:15.580602-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1f402a, Nexy(21495), 'prim'', displayID:'com.nexy.assistant'}
default	17:24:15.580709-0500	ControlCenter	Active activity attributions changed to ["scr:com.nexy.assistant"]
default	17:24:15.580662-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 43, PID = 21495, Name = sid:0x1f402a, Nexy(21495), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	17:24:15.580734-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	17:24:15.580682-0500	audiomxd	UpdateAudioState CID 0x91550001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	17:24:15.580729-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 43, PID = 21495, Name = sid:0x1f402a, Nexy(21495), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = YES>
default	17:24:15.580764-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1f402a, Nexy(21495), 'prim'', displayID:'com.nexy.assistant'}
default	17:24:15.580771-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	17:24:15.580827-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	17:24:15.580848-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	17:24:15.580876-0500	audioaccessoryd	AudioStateChanged: Added audio session app com.nexy.assistant 501 -> 200 count 2
default	17:24:15.580812-0500	audiomxd	UpdateAudioState CID 0x91550001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	17:24:15.580837-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1f402a, Nexy(21495), 'prim' with category(MediaPlayback)/mode(Default) and coreSessionID = 43 stopping recording
default	17:24:15.580907-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	17:24:15.580924-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	17:24:15.580869-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 43, PID = 21495, Name = sid:0x1f402a, Nexy(21495), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
error	17:24:15.580941-0500	audioaccessoryd	Updating local audio category 501 -> 200 app com.nexy.assistant
default	17:24:15.580921-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 43, PID = 21495, Name = sid:0x1f402a, Nexy(21495), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO>
default	17:24:15.581002-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	17:24:15.581017-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	17:24:15.580971-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1f402a, Nexy(21495), 'prim'', displayID:'com.nexy.assistant'}
default	17:24:15.581037-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	17:24:15.580996-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Will try to see if we can get the shared route for session = <ID: 43, PID = 21495, Name = sid:0x1f402a, Nexy(21495), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO>. Old (200) and New (201) scores.
default	17:24:15.581064-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	17:24:15.581075-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	17:24:15.581032-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 201, deviceID = <private>
default	17:24:15.581094-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	17:24:15.581135-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 1]. BT device UIDS: {(
)}
default	17:24:15.581160-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	17:24:15.581119-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	17:24:15.581219-0500	audioaccessoryd	Routing request Wx NULL score 201 flag 0x1 < Hijack > app com.nexy.assistant CID 0x91550001 category Not set
default	17:24:15.581413-0500	audiomxd	UpdateAudioState CID 0x91550001 audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	17:24:15.581496-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 201,
}
default	17:24:15.581523-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	17:24:15.581538-0500	audioaccessoryd	AudioStateChanged: Added audio session app com.nexy.assistant 200 -> 201 count 2
default	17:24:15.581556-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 201
error	17:24:15.581564-0500	audioaccessoryd	Updating local audio category 200 -> 201 app com.nexy.assistant
default	17:24:15.581527-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	17:24:15.581542-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	17:24:15.581595-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.nexy.assistant
default	17:24:15.581554-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	17:24:15.581562-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	17:24:15.581569-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	17:24:15.581577-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	17:24:15.581729-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	17:24:15.605181-0500	Nexy	nw_path_libinfo_path_check [B5951BBD-726D-4ABE-ACD8-F151CE3F50E9 Hostname#2f11c8a7:80 tcp, legacy-socket, attribution: developer]
	libinfo check path: <private>
default	17:24:15.605340-0500	mDNSResponder	[R16007] DNSServiceQueryRecord START -- qname: <mask.hash: 'WYUTXafykb7b/ZdEN+VCdQ=='>, qtype: A, flags: 0x1D000, interface index: 0, client pid: 21495 (Nexy), name hash: b360ab20
default	17:24:15.606126-0500	mDNSResponder	[R16008] DNSServiceQueryRecord START -- qname: <mask.hash: 'WYUTXafykb7b/ZdEN+VCdQ=='>, qtype: AAAA, flags: 0x1D000, interface index: 0, client pid: 21495 (Nexy), name hash: b360ab20
default	17:24:15.635360-0500	kernel	SK[6]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 4043F98E-46B5-4D77-84F7-63FD81822BCF flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=96,src=<IPv6-redacted>.55186,dst=<IPv6-redacted>.80,proto=0x06 mask=0x0000003f,hash=0x6448ad17 tp_proto=0x06"
default	17:24:15.635473-0500	kernel	tcp connect outgoing: [<IPv6-redacted>:55186<-><IPv6-redacted>:80] interface: en0 (skipped: 0)
so_gencnt: 5935300 t_state: SYN_SENT process: Nexy:21495 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xa895f3d4
default	17:24:15.651081-0500	kernel	tcp connected: [<IPv6-redacted>:55186<-><IPv6-redacted>:80] interface: en0 (skipped: 0)
so_gencnt: 5935300 t_state: ESTABLISHED process: Nexy:21495 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xa895f3d4
default	17:24:15.682537-0500	Nexy	                AUHAL.cpp:473   ~AUHAL: (0x83a050e40) Selecting device 0 from destructor
default	17:24:15.682549-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0x83a050e40)
default	17:24:15.682557-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0x83a050e40) not already running
default	17:24:15.682563-0500	Nexy	                AUHAL.cpp:687   SelectDevice: (0x83a050e40) disconnecting device 78
default	17:24:15.682571-0500	Nexy	                AUHAL.cpp:751   SelectDevice: (0x83a050e40) destroying ioproc 0xb for device 78
default	17:24:15.682617-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {BuiltInMicrophoneDevice, 0xb}
default	17:24:15.683094-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 1]. BT device UIDS: {(
)} Server update was not required.
default	17:24:15.683265-0500	Nexy	                AUHAL.cpp:853   SelectDevice: (0x83a050e40) nothing to setup
default	17:24:15.683279-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x83a050e40) adding 0 device listeners to device 0
default	17:24:15.683286-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x83a050e40) adding 0 device delegate listeners to device 0
default	17:24:15.683293-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x83a050e40) removing 7 device listeners from device 78
default	17:24:15.683502-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x83a050e40) removing 0 device delegate listeners from device 78
default	17:24:15.683515-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0x83a050e40)
default	17:24:15.893325-0500	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv6-redacted>:55186<-><IPv6-redacted>:80] interface: en0 (skipped: 0)
so_gencnt: 5935300 t_state: FIN_WAIT_1 process: Nexy:21495 Duration: 0.258 sec Conn_Time: 0.015 sec bytes in/out: 398/28694 pkts in/out: 2/12 pkt rxmit: 1 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 18.406 ms rttvar: 6.500 ms base rtt: 14 ms so_error: 0 svc/tc: 0 flow: 0xa895f3d4
default	17:24:15.893359-0500	kernel	tcp_connection_summary [<IPv6-redacted>:55186<-><IPv6-redacted>:80] interface: en0 (skipped: 0)
so_gencnt: 5935300 t_state: FIN_WAIT_1 process: Nexy:21495 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	17:24:15.916073-0500	Nexy	[com.apple.controlcenter:950C5067-8704-4062-917B-7F9E4958E32D] Sending action(s) in update: NSSceneFenceAction
default	17:24:15.993509-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Speaker App com.nexy.assistant, Score 201, Remote -1 NumofApp 2
default	17:24:16.764506-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	17:24:16.764631-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant)]
default	17:24:18.995783-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Speaker App com.nexy.assistant, Score 201, Remote -1 NumofApp 2
default	17:24:21.990375-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Speaker App com.nexy.assistant, Score 201, Remote -1 NumofApp 2
default	17:24:23.658447-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	17:24:23.658602-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant)]
default	17:24:24.993483-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Speaker App com.nexy.assistant, Score 201, Remote -1 NumofApp 2
default	17:24:27.993424-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Speaker App com.nexy.assistant, Score 201, Remote -1 NumofApp 2
default	17:24:30.993385-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Speaker App com.nexy.assistant, Score 201, Remote -1 NumofApp 2
default	17:24:31.112493-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant", "scr:com.nexy.assistant"]
default	17:24:31.114346-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	17:24:31.114378-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	17:24:31.114408-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	17:24:31.114424-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	17:24:31.114444-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	17:24:31.114459-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	17:24:31.114815-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	17:24:33.541352-0500	Nexy	System appearance change
default	17:24:33.541582-0500	Nexy	Current system appearance, (HLTB: 1), (SLS: 0)
default	17:24:33.552215-0500	Nexy	Invalidate NSApp effectiveAppearance
default	17:24:33.553632-0500	Nexy	Current system appearance, (HLTB: 1), (SLS: 0)
default	17:24:33.993278-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Speaker App com.nexy.assistant, Score 201, Remote -1 NumofApp 2
error	17:24:34.870073-0500	tccd	TCCDProcess: identifier=com.nexy.assistant, pid=21495, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy attempted to call TCCAccessRequest for kTCCServiceAccessibility without the recommended com.apple.private.tcc.manager.check-by-audit-token entitlement
default	17:24:34.869438-0500	Nexy	[0x836ac26c0] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	17:24:34.870224-0500	Nexy	[0x836ac26c0] invalidated after the last release of the connection object
default	17:24:34.875665-0500	Nexy	void _NSDisableAutomaticTerminationAndLog(NSString *) NSAccessibility Request Received
default	17:24:35.732716-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 201
default	17:24:35.732743-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.nexy.assistant
default	17:24:35.732901-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found 2 different sessions firstSession={clientName:'sid:0x1f402a, Nexy(21495), 'prim'', displayID:'com.nexy.assistant'}, secondSession={clientName:'sid:0x1f402b, VoiceOver(21533), 'prim'', displayID:'com.apple.VoiceOver'} but will use session={clientName:'(null)', displayID:'(null)'}
default	17:24:35.733429-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 201
default	17:24:35.810789-0500	Nexy	AudioComponentPluginMgr.mm:1117  component registrations changed
default	17:24:38.318099-0500	Nexy	                AUHAL.cpp:420   AUHAL: (0x83a050e40) Selecting device 71 from constructor
default	17:24:38.318120-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0x83a050e40)
default	17:24:38.318126-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0x83a050e40) not already running
default	17:24:38.318133-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0x83a050e40) nothing to teardown
default	17:24:38.318137-0500	Nexy	                AUHAL.cpp:762   SelectDevice: (0x83a050e40) connecting device 71
default	17:24:38.318244-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0x83a050e40) Device ID: 71 (Input:No | Output:Yes): true
default	17:24:38.318551-0500	Nexy	                AUHAL.cpp:774   SelectDevice: (0x83a050e40) created ioproc 0xd for device 71
default	17:24:38.318763-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x83a050e40) adding 7 device listeners to device 71
default	17:24:38.318944-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x83a050e40) adding 0 device delegate listeners to device 71
default	17:24:38.318957-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x83a050e40)
default	17:24:38.319084-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x48]:  2 ch,  48000 Hz, Float32, interleaved
default	17:24:38.319098-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	17:24:38.319107-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	17:24:38.319133-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	17:24:38.319144-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	17:24:38.319262-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x83a050e40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	17:24:38.319281-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x83a050e40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	17:24:38.319291-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	17:24:38.319297-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x83a050e40) removing 0 device listeners from device 0
default	17:24:38.319302-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x83a050e40) removing 0 device delegate listeners from device 0
default	17:24:38.319307-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0x83a050e40)
default	17:24:38.319330-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is DISABLED
default	17:24:38.319422-0500	Nexy	                AUHAL.cpp:2303  SetProperty: (0x83a050e40) caller requesting device change from 71 to 78
default	17:24:38.319432-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0x83a050e40)
default	17:24:38.319437-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0x83a050e40) not already running
default	17:24:38.319442-0500	Nexy	                AUHAL.cpp:687   SelectDevice: (0x83a050e40) disconnecting device 71
default	17:24:38.319448-0500	Nexy	                AUHAL.cpp:751   SelectDevice: (0x83a050e40) destroying ioproc 0xd for device 71
default	17:24:38.319489-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped Unknown {BuiltInSpeakerDevice, 0xd}
default	17:24:38.320030-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 1]. BT device UIDS: {(
)} Server update was not required.
default	17:24:38.320291-0500	Nexy	                AUHAL.cpp:762   SelectDevice: (0x83a050e40) connecting device 78
default	17:24:38.320400-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0x83a050e40) Device ID: 78 (Input:Yes | Output:No): true
default	17:24:38.321793-0500	Nexy	 [INFO] SLSHWCaptureDesktopProxying:485 request: <private>
default	17:24:38.321846-0500	Nexy	 [INFO] -[RPDaemonProxy proxyCoreGraphicsWithMethodType:config:machPort:completionHandler:]:1493
default	17:24:38.322379-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.984, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=21495, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=392, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	17:24:38.323813-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=21333.7, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=21495, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.replayd, pid=21333, auid=501, euid=501, binary_path=/usr/libexec/replayd}, },
default	17:24:38.323843-0500	tccd	requestor: TCCDProcess: identifier=com.apple.replayd, pid=21333, auid=501, euid=501, binary_path=/usr/libexec/replayd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=21495, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	17:24:38.323923-0500	Nexy	[com.apple.controlcenter:950C5067-8704-4062-917B-7F9E4958E32D] Sending action(s) in update: NSSceneFenceAction
default	17:24:38.324620-0500	tccd	AUTHREQ_SUBJECT: msgID=401.984, subject=com.nexy.assistant,
default	17:24:38.325083-0500	tccd	AUTHREQ_SUBJECT: msgID=21333.7, subject=com.nexy.assistant,
default	17:24:38.325947-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x722e70c00 at /Applications/Nexy.app
default	17:24:38.326152-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b5164000 at /Applications/Nexy.app
default	17:24:38.348867-0500	Nexy	                AUHAL.cpp:774   SelectDevice: (0x83a050e40) created ioproc 0xc for device 78
default	17:24:38.349014-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x83a050e40) adding 7 device listeners to device 78
default	17:24:38.349232-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x83a050e40) adding 0 device delegate listeners to device 78
default	17:24:38.349252-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x83a050e40)
default	17:24:38.349261-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 output streams; not all mono
default	17:24:38.349270-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	17:24:38.349442-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  input stream 0 [0x4f]:  1 ch,  44100 Hz, Float32
default	17:24:38.349448-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 input streams; all mono
default	17:24:38.349453-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  1 ch,  44100 Hz, Float32
default	17:24:38.349592-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x83a050e40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	17:24:38.349600-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x83a050e40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	17:24:38.349603-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	17:24:38.349610-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x83a050e40) removing 7 device listeners from device 71
default	17:24:38.349834-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x83a050e40) removing 0 device delegate listeners from device 71
default	17:24:38.349848-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0x83a050e40)
default	17:24:38.349855-0500	Nexy	AudioHardware-mac-imp.cpp:1306   AudioObjectAddPropertyListener: listener was already added
default	17:24:38.350270-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	17:24:38.351061-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.985, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=21495, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=392, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	17:24:38.351819-0500	tccd	AUTHREQ_SUBJECT: msgID=401.985, subject=com.nexy.assistant,
default	17:24:38.352272-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x722e70c00 at /Applications/Nexy.app
default	17:24:38.362826-0500	Nexy	 [INFO] SLSHWCaptureDesktopProxying_block_invoke:506 request: <private>, error: (null), windowInfo: (null)
default	17:24:38.364038-0500	Nexy	 [INFO] SLSHWCaptureDesktopProxying:485 request: <private>
default	17:24:38.364078-0500	Nexy	 [INFO] -[RPDaemonProxy proxyCoreGraphicsWithMethodType:config:machPort:completionHandler:]:1493
default	17:24:38.366929-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=21333.8, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=21495, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.replayd, pid=21333, auid=501, euid=501, binary_path=/usr/libexec/replayd}, },
default	17:24:38.367059-0500	tccd	requestor: TCCDProcess: identifier=com.apple.replayd, pid=21333, auid=501, euid=501, binary_path=/usr/libexec/replayd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=21495, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	17:24:38.367969-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	17:24:38.368482-0500	tccd	AUTHREQ_SUBJECT: msgID=21333.8, subject=com.nexy.assistant,
default	17:24:38.368906-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.986, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=21495, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=392, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	17:24:38.369405-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b5164000 at /Applications/Nexy.app
default	17:24:38.371871-0500	tccd	AUTHREQ_SUBJECT: msgID=401.986, subject=com.nexy.assistant,
default	17:24:38.372427-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x722e70c00 at /Applications/Nexy.app
default	17:24:38.380511-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	17:24:38.380614-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant)]
default	17:24:38.380702-0500	ControlCenter	Active activity attributions changed to ["scr:com.nexy.assistant"]
default	17:24:38.390047-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.987, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=21495, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=392, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	17:24:38.390821-0500	tccd	AUTHREQ_SUBJECT: msgID=401.987, subject=com.nexy.assistant,
default	17:24:38.391258-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x722e70c00 at /Applications/Nexy.app
default	17:24:38.397706-0500	Nexy	 [INFO] SLSHWCaptureDesktopProxying_block_invoke:506 request: <private>, error: (null), windowInfo: (null)
default	17:24:38.428294-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Input {BuiltInMicrophoneDevice, 0xc}
default	17:24:38.430397-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1f402a","name":"Nexy(21495)"}, "details":{"deviceUIDs":[],"implicit_category":"PlayAndRecord","input_running":true,"output_running":true} }
default	17:24:38.430588-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 43, PID = 21495, Name = sid:0x1f402a, Nexy(21495), 'prim', BundleID = com.nexy.assistant, Category = PlayAndRecord_WithBluetooth, Mode = Default, Active = YES, Playing = YES, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	17:24:38.430747-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Category/Mode changed -- The score for sid:0x1f402a, Nexy(21495), 'prim'/com.nexy.assistant was not correct. Old score = 201
default	17:24:38.430773-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 43, PID = 21495, Name = sid:0x1f402a, Nexy(21495), 'prim', BundleID = com.nexy.assistant, Category = PlayAndRecord_WithBluetooth, Mode = Default, Active = YES, Playing = YES, Recording = NO>
default	17:24:38.430788-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found 2 different sessions firstSession={clientName:'sid:0x1f402a, Nexy(21495), 'prim'', displayID:'com.nexy.assistant'}, secondSession={clientName:'sid:0x1f402b, VoiceOver(21533), 'prim'', displayID:'com.apple.VoiceOver'} but will use session={clientName:'(null)', displayID:'(null)'}
default	17:24:38.430815-0500	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1f402a, Nexy(21495), 'prim'', AudioCategory changed to 'PlayAndRecord_WithBluetooth'
default	17:24:38.430836-0500	audiomxd	UpdateAudioState CID 0x91550001 audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	17:24:38.430890-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 43, PID = 21495, Name = sid:0x1f402a, Nexy(21495), 'prim', BundleID = com.nexy.assistant, Category = PlayAndRecord_WithBluetooth, Mode = Default, Active = YES, Playing = YES, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	17:24:38.430934-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 43, PID = 21495, Name = sid:0x1f402a, Nexy(21495), 'prim', BundleID = com.nexy.assistant, Category = PlayAndRecord_WithBluetooth, Mode = Default, Active = YES, Playing = YES, Recording = NO>
default	17:24:38.430965-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found 2 different sessions firstSession={clientName:'sid:0x1f402a, Nexy(21495), 'prim'', displayID:'com.nexy.assistant'}, secondSession={clientName:'sid:0x1f402b, VoiceOver(21533), 'prim'', displayID:'com.apple.VoiceOver'} but will use session={clientName:'(null)', displayID:'(null)'}
default	17:24:38.431123-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 43, PID = 21495, Name = sid:0x1f402a, Nexy(21495), 'prim', BundleID = com.nexy.assistant, Category = PlayAndRecord_WithBluetooth, Mode = Default, Active = YES, Playing = YES, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	17:24:38.431123-0500	audiomxd	UpdateAudioState CID 0x91550001 audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	17:24:38.431143-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 43, PID = 21495, Name = sid:0x1f402a, Nexy(21495), 'prim', BundleID = com.nexy.assistant, Category = PlayAndRecord_WithBluetooth, Mode = Default, Active = YES, Playing = YES, Recording = NO>
default	17:24:38.431155-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found 2 different sessions firstSession={clientName:'sid:0x1f402a, Nexy(21495), 'prim'', displayID:'com.nexy.assistant'}, secondSession={clientName:'sid:0x1f402b, VoiceOver(21533), 'prim'', displayID:'com.apple.VoiceOver'} but will use session={clientName:'(null)', displayID:'(null)'}
default	17:24:38.431173-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1f402a, Nexy(21495), 'prim' with category(PlayAndRecord_WithBluetooth)/mode(Default) and coreSessionID = 43 starting recording
default	17:24:38.431236-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: Bumping the mode to Voice chat for session as session started recording = <ID: 43, PID = 21495, Name = sid:0x1f402a, Nexy(21495), 'prim', BundleID = com.nexy.assistant, Category = PlayAndRecord_WithBluetooth, Mode = Default, Active = YES, Playing = YES, Recording = YES>
default	17:24:38.431260-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 43, PID = 21495, Name = sid:0x1f402a, Nexy(21495), 'prim', BundleID = com.nexy.assistant, Category = PlayAndRecord_WithBluetooth, Mode = VoiceChat, Active = YES, Playing = YES, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	17:24:38.431277-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Category/Mode changed -- The score for sid:0x1f402a, Nexy(21495), 'prim'/com.nexy.assistant was not correct. Old score = 201
default	17:24:38.431325-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 201,
}
default	17:24:38.431349-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	17:24:38.431305-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 501 for session <ID: 43, PID = 21495, Name = sid:0x1f402a, Nexy(21495), 'prim', BundleID = com.nexy.assistant, Category = PlayAndRecord_WithBluetooth, Mode = VoiceChat, Active = YES, Playing = YES, Recording = YES>
default	17:24:38.431330-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found 2 different sessions firstSession={clientName:'sid:0x1f402a, Nexy(21495), 'prim'', displayID:'com.nexy.assistant'}, secondSession={clientName:'sid:0x1f402b, VoiceOver(21533), 'prim'', displayID:'com.apple.VoiceOver'} but will use session={clientName:'(null)', displayID:'(null)'}
default	17:24:38.431365-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 201
default	17:24:38.431453-0500	audiomxd	UpdateAudioState CID 0x91550001 audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	17:24:38.431583-0500	audiomxd	UpdateAudioState CID 0x91550001 audioState Start apps {
    "com.nexy.assistant" : 501,
}
default	17:24:38.431585-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 201,
}
default	17:24:38.431615-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	17:24:38.431660-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 201
default	17:24:38.431694-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 201,
}
default	17:24:38.431745-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	17:24:38.431654-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [1, 1]. BT device UIDS: {(
)}
default	17:24:38.431866-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 201
default	17:24:38.431849-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	17:24:38.431926-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 501,
}
default	17:24:38.431991-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 501,
}
default	17:24:38.432019-0500	audioaccessoryd	AudioStateChanged: Added audio session app com.nexy.assistant 201 -> 501 count 3
default	17:24:38.432190-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 501
error	17:24:38.432255-0500	audioaccessoryd	Updating local audio category 201 -> 501 app com.nexy.assistant
default	17:24:38.432367-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 501 App com.nexy.assistant
default	17:24:38.435996-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	17:24:38.440628-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	17:24:38.440702-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant), [mic] Nexy (com.nexy.assistant)]
default	17:24:38.440732-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant", "scr:com.nexy.assistant"]
default	17:24:38.441139-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	17:24:38.441162-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	17:24:38.441179-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	17:24:38.441186-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	17:24:38.441194-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	17:24:38.441200-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	17:24:38.441365-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	17:24:38.444384-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	17:24:38.444396-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	17:24:38.444407-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	17:24:38.444415-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	17:24:38.444422-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	17:24:38.444428-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	17:24:38.444497-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	17:24:38.444571-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	17:24:38.444582-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	17:24:38.444592-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	17:24:38.444600-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	17:24:38.444607-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	17:24:38.444617-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	17:24:38.444722-0500	ControlCenter	Navigating to new application [com.nexy.assistant]
default	17:24:39.993310-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Speaker App com.nexy.assistant, Score 501, Remote -1 NumofApp 3
default	17:24:40.325401-0500	Nexy	[com.apple.controlcenter:950C5067-8704-4062-917B-7F9E4958E32D] Sending action(s) in update: NSSceneFenceAction
default	17:24:41.369702-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	17:24:41.376429-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	17:24:41.376569-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant), [scr] Nexy (com.nexy.assistant)]
default	17:24:42.217988-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	17:24:42.234143-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {BuiltInMicrophoneDevice, 0xc}
default	17:24:42.235049-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	17:24:42.235150-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant)]
default	17:24:42.235224-0500	ControlCenter	Active activity attributions changed to ["scr:com.nexy.assistant"]
default	17:24:42.235244-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	17:24:42.236037-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1f402a","name":"Nexy(21495)"}, "details":{"deviceUIDs":[],"implicit_category":"MediaPlayback","input_running":false,"output_running":true} }
default	17:24:42.236197-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 43, PID = 21495, Name = sid:0x1f402a, Nexy(21495), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	17:24:42.236248-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Category/Mode changed -- The score for sid:0x1f402a, Nexy(21495), 'prim'/com.nexy.assistant was not correct. Old score = 501
default	17:24:42.236289-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 43, PID = 21495, Name = sid:0x1f402a, Nexy(21495), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = YES>
default	17:24:42.236325-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found 2 different sessions firstSession={clientName:'sid:0x1f402a, Nexy(21495), 'prim'', displayID:'com.nexy.assistant'}, secondSession={clientName:'sid:0x1f402b, VoiceOver(21533), 'prim'', displayID:'com.apple.VoiceOver'} but will use session={clientName:'(null)', displayID:'(null)'}
default	17:24:42.236382-0500	audiomxd	UpdateAudioState CID 0x91550001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	17:24:42.236443-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 43, PID = 21495, Name = sid:0x1f402a, Nexy(21495), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	17:24:42.236522-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 43, PID = 21495, Name = sid:0x1f402a, Nexy(21495), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = YES>
default	17:24:42.236392-0500	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1f402a, Nexy(21495), 'prim'', AudioCategory changed to 'MediaPlayback'
default	17:24:42.236553-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found 2 different sessions firstSession={clientName:'sid:0x1f402a, Nexy(21495), 'prim'', displayID:'com.nexy.assistant'}, secondSession={clientName:'sid:0x1f402b, VoiceOver(21533), 'prim'', displayID:'com.apple.VoiceOver'} but will use session={clientName:'(null)', displayID:'(null)'}
default	17:24:42.236571-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	17:24:42.236633-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	17:24:42.236670-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 43, PID = 21495, Name = sid:0x1f402a, Nexy(21495), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	17:24:42.236732-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	17:24:42.236675-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	17:24:42.236746-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	17:24:42.236692-0500	audioaccessoryd	AudioStateChanged: Added audio session app com.nexy.assistant 501 -> 200 count 3
default	17:24:42.236746-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 43, PID = 21495, Name = sid:0x1f402a, Nexy(21495), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = YES>
default	17:24:42.236752-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	17:24:42.236751-0500	audiomxd	UpdateAudioState CID 0x91550001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	17:24:42.236848-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	17:24:42.236804-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found 2 different sessions firstSession={clientName:'sid:0x1f402a, Nexy(21495), 'prim'', displayID:'com.nexy.assistant'}, secondSession={clientName:'sid:0x1f402b, VoiceOver(21533), 'prim'', displayID:'com.apple.VoiceOver'} but will use session={clientName:'(null)', displayID:'(null)'}
default	17:24:42.236860-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	17:24:42.236910-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1f402a, Nexy(21495), 'prim' with category(MediaPlayback)/mode(Default) and coreSessionID = 43 stopping recording
default	17:24:42.236721-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	17:24:42.236994-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 43, PID = 21495, Name = sid:0x1f402a, Nexy(21495), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	17:24:42.236953-0500	audiomxd	UpdateAudioState CID 0x91550001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	17:24:42.237004-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	17:24:42.237055-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	17:24:42.237190-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	17:24:42.237293-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	17:24:42.237385-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	17:24:42.237071-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 43, PID = 21495, Name = sid:0x1f402a, Nexy(21495), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO>
default	17:24:42.237637-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 1]. BT device UIDS: {(
)}
default	17:24:42.237682-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	17:24:42.237478-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	17:24:42.237149-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found 2 different sessions firstSession={clientName:'sid:0x1f402a, Nexy(21495), 'prim'', displayID:'com.nexy.assistant'}, secondSession={clientName:'sid:0x1f402b, VoiceOver(21533), 'prim'', displayID:'com.apple.VoiceOver'} but will use session={clientName:'(null)', displayID:'(null)'}
default	17:24:42.237559-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 201,
}
default	17:24:42.237251-0500	audiomxd	UpdateAudioState CID 0x91550001 audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	17:24:42.237518-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	17:24:42.237623-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	17:24:42.237682-0500	audioaccessoryd	AudioStateChanged: Added audio session app com.nexy.assistant 200 -> 201 count 3
default	17:24:42.237818-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 201
default	17:24:42.251281-0500	Nexy	nw_path_libinfo_path_check [57FD26F1-82B4-47E0-9BCC-8EF1073A3D99 Hostname#2f11c8a7:80 tcp, legacy-socket, attribution: developer]
	libinfo check path: <private>
default	17:24:42.251434-0500	mDNSResponder	[R16041] DNSServiceQueryRecord START -- qname: <mask.hash: 'WYUTXafykb7b/ZdEN+VCdQ=='>, qtype: A, flags: 0x1D000, interface index: 0, client pid: 21495 (Nexy), name hash: b360ab20
default	17:24:42.252397-0500	mDNSResponder	[R16042] DNSServiceQueryRecord START -- qname: <mask.hash: 'WYUTXafykb7b/ZdEN+VCdQ=='>, qtype: AAAA, flags: 0x1D000, interface index: 0, client pid: 21495 (Nexy), name hash: b360ab20
default	17:24:42.280483-0500	kernel	SK[5]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid B7A34155-71E2-4D70-AE3E-E8A95392136E flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=96,src=<IPv6-redacted>.55187,dst=<IPv6-redacted>.80,proto=0x06 mask=0x0000003f,hash=0x99bd2c5e tp_proto=0x06"
default	17:24:42.280632-0500	kernel	tcp connect outgoing: [<IPv6-redacted>:55187<-><IPv6-redacted>:80] interface: en0 (skipped: 0)
so_gencnt: 5935417 t_state: SYN_SENT process: Nexy:21495 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xb0202c2c
default	17:24:42.304816-0500	kernel	tcp connected: [<IPv6-redacted>:55187<-><IPv6-redacted>:80] interface: en0 (skipped: 0)
so_gencnt: 5935417 t_state: ESTABLISHED process: Nexy:21495 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xb0202c2c
default	17:24:42.344109-0500	Nexy	                AUHAL.cpp:473   ~AUHAL: (0x83a050e40) Selecting device 0 from destructor
default	17:24:42.344135-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0x83a050e40)
default	17:24:42.344150-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0x83a050e40) not already running
default	17:24:42.344161-0500	Nexy	                AUHAL.cpp:687   SelectDevice: (0x83a050e40) disconnecting device 78
default	17:24:42.344183-0500	Nexy	                AUHAL.cpp:751   SelectDevice: (0x83a050e40) destroying ioproc 0xc for device 78
default	17:24:42.344244-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {BuiltInMicrophoneDevice, 0xc}
default	17:24:42.345186-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 1]. BT device UIDS: {(
)} Server update was not required.
default	17:24:42.345495-0500	Nexy	                AUHAL.cpp:853   SelectDevice: (0x83a050e40) nothing to setup
default	17:24:42.345525-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x83a050e40) adding 0 device listeners to device 0
default	17:24:42.345541-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x83a050e40) adding 0 device delegate listeners to device 0
default	17:24:42.345556-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x83a050e40) removing 7 device listeners from device 78
default	17:24:42.346050-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x83a050e40) removing 0 device delegate listeners from device 78
default	17:24:42.346080-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0x83a050e40)
default	17:24:42.721985-0500	kernel	tcp_connection_summary (tcp_usrclosed:3220)[<IPv6-redacted>:55187<-><IPv6-redacted>:80] interface: en0 (skipped: 0)
so_gencnt: 5935417 t_state: LAST_ACK process: Nexy:21495 Duration: 0.441 sec Conn_Time: 0.024 sec bytes in/out: 584/98837 pkts in/out: 4/36 pkt rxmit: 3 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 24.843 ms rttvar: 5.750 ms base rtt: 16 ms so_error: 0 svc/tc: 0 flow: 0xb0202c2c
default	17:24:42.722052-0500	kernel	tcp_connection_summary [<IPv6-redacted>:55187<-><IPv6-redacted>:80] interface: en0 (skipped: 0)
so_gencnt: 5935417 t_state: LAST_ACK process: Nexy:21495 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 1/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	17:24:49.777746-0500	Nexy	[com.apple.controlcenter:950C5067-8704-4062-917B-7F9E4958E32D] Sending action(s) in update: NSSceneFenceAction
default	17:24:50.392858-0500	Nexy	  AVAudioSession_MacOS.mm:883   Activating session
default	17:24:50.395284-0500	Nexy	[com.apple.controlcenter:950C5067-8704-4062-917B-7F9E4958E32D] Sending action(s) in update: NSSceneFenceAction
default	17:24:50.395493-0500	Nexy	                AUHAL.cpp:420   AUHAL: (0x83a050e40) Selecting device 71 from constructor
default	17:24:50.395514-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0x83a050e40)
default	17:24:50.395523-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0x83a050e40) not already running
default	17:24:50.395529-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0x83a050e40) nothing to teardown
default	17:24:50.395534-0500	Nexy	                AUHAL.cpp:762   SelectDevice: (0x83a050e40) connecting device 71
default	17:24:50.395663-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0x83a050e40) Device ID: 71 (Input:No | Output:Yes): true
default	17:24:50.395977-0500	Nexy	                AUHAL.cpp:774   SelectDevice: (0x83a050e40) created ioproc 0xe for device 71
default	17:24:50.396100-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x83a050e40) adding 7 device listeners to device 71
default	17:24:50.396332-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x83a050e40) adding 0 device delegate listeners to device 71
default	17:24:50.396346-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x83a050e40)
default	17:24:50.396449-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x48]:  2 ch,  48000 Hz, Float32, interleaved
default	17:24:50.396462-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	17:24:50.396470-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	17:24:50.396480-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	17:24:50.396502-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	17:24:50.396622-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x83a050e40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	17:24:50.396640-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x83a050e40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	17:24:50.396647-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	17:24:50.396655-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x83a050e40) removing 0 device listeners from device 0
default	17:24:50.396661-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x83a050e40) removing 0 device delegate listeners from device 0
default	17:24:50.396666-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0x83a050e40)
default	17:24:50.396686-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is DISABLED
default	17:24:50.396755-0500	Nexy	                AUHAL.cpp:2303  SetProperty: (0x83a050e40) caller requesting device change from 71 to 78
default	17:24:50.396768-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0x83a050e40)
default	17:24:50.396775-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0x83a050e40) not already running
default	17:24:50.396780-0500	Nexy	                AUHAL.cpp:687   SelectDevice: (0x83a050e40) disconnecting device 71
default	17:24:50.396785-0500	Nexy	                AUHAL.cpp:751   SelectDevice: (0x83a050e40) destroying ioproc 0xe for device 71
default	17:24:50.396806-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped Unknown {BuiltInSpeakerDevice, 0xe}
default	17:24:50.397202-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 1]. BT device UIDS: {(
)} Server update was not required.
default	17:24:50.397486-0500	Nexy	                AUHAL.cpp:762   SelectDevice: (0x83a050e40) connecting device 78
default	17:24:50.397595-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0x83a050e40) Device ID: 78 (Input:Yes | Output:No): true
default	17:24:50.399723-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.988, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=21495, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=392, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	17:24:50.401820-0500	tccd	AUTHREQ_SUBJECT: msgID=401.988, subject=com.nexy.assistant,
default	17:24:50.402945-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x722e70c00 at /Applications/Nexy.app
default	17:24:50.407812-0500	Nexy	 [INFO] SLSHWCaptureDesktopProxying:485 request: <private>
default	17:24:50.407860-0500	Nexy	 [INFO] -[RPDaemonProxy proxyCoreGraphicsWithMethodType:config:machPort:completionHandler:]:1493
default	17:24:50.409895-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=21333.9, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=21495, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.replayd, pid=21333, auid=501, euid=501, binary_path=/usr/libexec/replayd}, },
default	17:24:50.409929-0500	tccd	requestor: TCCDProcess: identifier=com.apple.replayd, pid=21333, auid=501, euid=501, binary_path=/usr/libexec/replayd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=21495, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	17:24:50.411551-0500	tccd	AUTHREQ_SUBJECT: msgID=21333.9, subject=com.nexy.assistant,
default	17:24:50.412669-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b5164000 at /Applications/Nexy.app
default	17:24:50.425729-0500	Nexy	                AUHAL.cpp:774   SelectDevice: (0x83a050e40) created ioproc 0xd for device 78
default	17:24:50.425921-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x83a050e40) adding 7 device listeners to device 78
default	17:24:50.426158-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x83a050e40) adding 0 device delegate listeners to device 78
default	17:24:50.426168-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x83a050e40)
default	17:24:50.426181-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 output streams; not all mono
default	17:24:50.426192-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	17:24:50.426337-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  input stream 0 [0x4f]:  1 ch,  44100 Hz, Float32
default	17:24:50.426345-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 input streams; all mono
default	17:24:50.426353-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  1 ch,  44100 Hz, Float32
default	17:24:50.426454-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x83a050e40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	17:24:50.426465-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x83a050e40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	17:24:50.426470-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	17:24:50.426522-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x83a050e40) removing 7 device listeners from device 71
default	17:24:50.426726-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x83a050e40) removing 0 device delegate listeners from device 71
default	17:24:50.426732-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0x83a050e40)
default	17:24:50.426740-0500	Nexy	AudioHardware-mac-imp.cpp:1306   AudioObjectAddPropertyListener: listener was already added
default	17:24:50.427082-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	17:24:50.428240-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.989, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=21495, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=392, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	17:24:50.429382-0500	tccd	AUTHREQ_SUBJECT: msgID=401.989, subject=com.nexy.assistant,
default	17:24:50.429974-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x722e70c00 at /Applications/Nexy.app
default	17:24:50.437279-0500	Nexy	 [INFO] SLSHWCaptureDesktopProxying:485 request: <private>
default	17:24:50.437311-0500	Nexy	 [INFO] -[RPDaemonProxy proxyCoreGraphicsWithMethodType:config:machPort:completionHandler:]:1493
default	17:24:50.444329-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	17:24:50.445229-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.990, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=21495, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=392, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	17:24:50.445940-0500	tccd	AUTHREQ_SUBJECT: msgID=401.990, subject=com.nexy.assistant,
default	17:24:50.446362-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x722e70c00 at /Applications/Nexy.app
default	17:24:50.447478-0500	Nexy	 [INFO] SLSHWCaptureDesktopProxying_block_invoke:506 request: <private>, error: (null), windowInfo: (null)
default	17:24:50.448087-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=21333.10, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=21495, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.replayd, pid=21333, auid=501, euid=501, binary_path=/usr/libexec/replayd}, },
default	17:24:50.448108-0500	tccd	requestor: TCCDProcess: identifier=com.apple.replayd, pid=21333, auid=501, euid=501, binary_path=/usr/libexec/replayd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=21495, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	17:24:50.448755-0500	tccd	AUTHREQ_SUBJECT: msgID=21333.10, subject=com.nexy.assistant,
default	17:24:50.449232-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b5164000 at /Applications/Nexy.app
default	17:24:50.459104-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.991, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=21495, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=392, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	17:24:50.459764-0500	tccd	AUTHREQ_SUBJECT: msgID=401.991, subject=com.nexy.assistant,
default	17:24:50.460226-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x722e70c00 at /Applications/Nexy.app
default	17:24:50.477025-0500	Nexy	 [INFO] SLSHWCaptureDesktopProxying_block_invoke:506 request: <private>, error: (null), windowInfo: (null)
default	17:24:50.497927-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Input {BuiltInMicrophoneDevice, 0xd}
default	17:24:50.498517-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1f402a","name":"Nexy(21495)"}, "details":{"deviceUIDs":[],"implicit_category":"PlayAndRecord","input_running":true,"output_running":true} }
default	17:24:50.498564-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 43, PID = 21495, Name = sid:0x1f402a, Nexy(21495), 'prim', BundleID = com.nexy.assistant, Category = PlayAndRecord_WithBluetooth, Mode = Default, Active = YES, Playing = YES, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	17:24:50.498583-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Category/Mode changed -- The score for sid:0x1f402a, Nexy(21495), 'prim'/com.nexy.assistant was not correct. Old score = 201
default	17:24:50.498598-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 43, PID = 21495, Name = sid:0x1f402a, Nexy(21495), 'prim', BundleID = com.nexy.assistant, Category = PlayAndRecord_WithBluetooth, Mode = Default, Active = YES, Playing = YES, Recording = NO>
default	17:24:50.498611-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found 2 different sessions firstSession={clientName:'sid:0x1f402a, Nexy(21495), 'prim'', displayID:'com.nexy.assistant'}, secondSession={clientName:'sid:0x1f402b, VoiceOver(21533), 'prim'', displayID:'com.apple.VoiceOver'} but will use session={clientName:'(null)', displayID:'(null)'}
default	17:24:50.498648-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 43, PID = 21495, Name = sid:0x1f402a, Nexy(21495), 'prim', BundleID = com.nexy.assistant, Category = PlayAndRecord_WithBluetooth, Mode = Default, Active = YES, Playing = YES, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	17:24:50.498644-0500	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1f402a, Nexy(21495), 'prim'', AudioCategory changed to 'PlayAndRecord_WithBluetooth'
default	17:24:50.498670-0500	audiomxd	UpdateAudioState CID 0x91550001 audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	17:24:50.498744-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 43, PID = 21495, Name = sid:0x1f402a, Nexy(21495), 'prim', BundleID = com.nexy.assistant, Category = PlayAndRecord_WithBluetooth, Mode = Default, Active = YES, Playing = YES, Recording = NO>
default	17:24:50.498785-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 201,
}
default	17:24:50.498804-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	17:24:50.498771-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found 2 different sessions firstSession={clientName:'sid:0x1f402a, Nexy(21495), 'prim'', displayID:'com.nexy.assistant'}, secondSession={clientName:'sid:0x1f402b, VoiceOver(21533), 'prim'', displayID:'com.apple.VoiceOver'} but will use session={clientName:'(null)', displayID:'(null)'}
default	17:24:50.498822-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 201
default	17:24:50.498805-0500	audiomxd	UpdateAudioState CID 0x91550001 audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	17:24:50.498827-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 43, PID = 21495, Name = sid:0x1f402a, Nexy(21495), 'prim', BundleID = com.nexy.assistant, Category = PlayAndRecord_WithBluetooth, Mode = Default, Active = YES, Playing = YES, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	17:24:50.498884-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 43, PID = 21495, Name = sid:0x1f402a, Nexy(21495), 'prim', BundleID = com.nexy.assistant, Category = PlayAndRecord_WithBluetooth, Mode = Default, Active = YES, Playing = YES, Recording = NO>
default	17:24:50.498861-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 201,
}
default	17:24:50.498876-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	17:24:50.498929-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found 2 different sessions firstSession={clientName:'sid:0x1f402a, Nexy(21495), 'prim'', displayID:'com.nexy.assistant'}, secondSession={clientName:'sid:0x1f402b, VoiceOver(21533), 'prim'', displayID:'com.apple.VoiceOver'} but will use session={clientName:'(null)', displayID:'(null)'}
default	17:24:50.498936-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 201
default	17:24:50.498963-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1f402a, Nexy(21495), 'prim' with category(PlayAndRecord_WithBluetooth)/mode(Default) and coreSessionID = 43 starting recording
default	17:24:50.498975-0500	audiomxd	UpdateAudioState CID 0x91550001 audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	17:24:50.499068-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 201,
}
default	17:24:50.499037-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: Bumping the mode to Voice chat for session as session started recording = <ID: 43, PID = 21495, Name = sid:0x1f402a, Nexy(21495), 'prim', BundleID = com.nexy.assistant, Category = PlayAndRecord_WithBluetooth, Mode = Default, Active = YES, Playing = YES, Recording = YES>
default	17:24:50.499084-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	17:24:50.499094-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 43, PID = 21495, Name = sid:0x1f402a, Nexy(21495), 'prim', BundleID = com.nexy.assistant, Category = PlayAndRecord_WithBluetooth, Mode = VoiceChat, Active = YES, Playing = YES, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	17:24:50.499129-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Category/Mode changed -- The score for sid:0x1f402a, Nexy(21495), 'prim'/com.nexy.assistant was not correct. Old score = 201
default	17:24:50.499145-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 201
default	17:24:50.499190-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 501 for session <ID: 43, PID = 21495, Name = sid:0x1f402a, Nexy(21495), 'prim', BundleID = com.nexy.assistant, Category = PlayAndRecord_WithBluetooth, Mode = VoiceChat, Active = YES, Playing = YES, Recording = YES>
default	17:24:50.499310-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [1, 1]. BT device UIDS: {(
)}
default	17:24:50.499317-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	17:24:50.499411-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 501,
}
default	17:24:50.499250-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found 2 different sessions firstSession={clientName:'sid:0x1f402a, Nexy(21495), 'prim'', displayID:'com.nexy.assistant'}, secondSession={clientName:'sid:0x1f402b, VoiceOver(21533), 'prim'', displayID:'com.apple.VoiceOver'} but will use session={clientName:'(null)', displayID:'(null)'}
default	17:24:50.499422-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 501,
}
default	17:24:50.499428-0500	audioaccessoryd	AudioStateChanged: Added audio session app com.nexy.assistant 201 -> 501 count 3
default	17:24:50.499334-0500	audiomxd	UpdateAudioState CID 0x91550001 audioState Start apps {
    "com.nexy.assistant" : 501,
}
default	17:24:50.499438-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 501
error	17:24:50.499443-0500	audioaccessoryd	Updating local audio category 201 -> 501 app com.nexy.assistant
default	17:24:50.499533-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 501 App com.nexy.assistant
default	17:24:50.504532-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	17:24:50.508531-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	17:24:50.508590-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant), [mic] Nexy (com.nexy.assistant)]
default	17:24:50.508632-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant", "scr:com.nexy.assistant"]
default	17:24:50.509201-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	17:24:50.509213-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	17:24:50.509229-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	17:24:50.509239-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	17:24:50.509248-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	17:24:50.509253-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	17:24:50.509270-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	17:24:50.509282-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	17:24:50.509290-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	17:24:50.509298-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	17:24:50.509305-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	17:24:50.509311-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	17:24:50.509321-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	17:24:50.509341-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	17:24:50.509387-0500	ControlCenter	Navigating to new application [com.nexy.assistant]
default	17:24:50.509377-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	17:24:50.509414-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	17:24:50.509443-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	17:24:50.509459-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	17:24:50.509462-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	17:24:51.495829-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	17:24:51.502477-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	17:24:51.502590-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant), [scr] Nexy (com.nexy.assistant)]
default	17:24:51.993347-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Speaker App com.nexy.assistant, Score 501, Remote -1 NumofApp 3
default	17:24:52.839633-0500	Nexy	[com.apple.controlcenter:950C5067-8704-4062-917B-7F9E4958E32D] Sending action(s) in update: NSSceneFenceAction
default	17:24:54.639569-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	17:24:54.657843-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	17:24:54.657958-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant)]
default	17:24:54.658039-0500	ControlCenter	Active activity attributions changed to ["scr:com.nexy.assistant"]
default	17:24:54.658062-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	17:24:54.658742-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	17:24:54.658757-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	17:24:54.658776-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	17:24:54.658785-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	17:24:54.658796-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	17:24:54.658804-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	17:24:54.658942-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	17:24:54.659440-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {BuiltInMicrophoneDevice, 0xd}
default	17:24:54.662807-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1f402a","name":"Nexy(21495)"}, "details":{"deviceUIDs":[],"implicit_category":"MediaPlayback","input_running":false,"output_running":true} }
default	17:24:54.662985-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 43, PID = 21495, Name = sid:0x1f402a, Nexy(21495), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	17:24:54.663039-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Category/Mode changed -- The score for sid:0x1f402a, Nexy(21495), 'prim'/com.nexy.assistant was not correct. Old score = 501
default	17:24:54.663085-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 43, PID = 21495, Name = sid:0x1f402a, Nexy(21495), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = YES>
default	17:24:54.663130-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found 2 different sessions firstSession={clientName:'sid:0x1f402a, Nexy(21495), 'prim'', displayID:'com.nexy.assistant'}, secondSession={clientName:'sid:0x1f402b, VoiceOver(21533), 'prim'', displayID:'com.apple.VoiceOver'} but will use session={clientName:'(null)', displayID:'(null)'}
default	17:24:54.663175-0500	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1f402a, Nexy(21495), 'prim'', AudioCategory changed to 'MediaPlayback'
default	17:24:54.663211-0500	audiomxd	UpdateAudioState CID 0x91550001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	17:24:54.663228-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 43, PID = 21495, Name = sid:0x1f402a, Nexy(21495), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	17:24:54.663295-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 43, PID = 21495, Name = sid:0x1f402a, Nexy(21495), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = YES>
default	17:24:54.663347-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found 2 different sessions firstSession={clientName:'sid:0x1f402a, Nexy(21495), 'prim'', displayID:'com.nexy.assistant'}, secondSession={clientName:'sid:0x1f402b, VoiceOver(21533), 'prim'', displayID:'com.apple.VoiceOver'} but will use session={clientName:'(null)', displayID:'(null)'}
default	17:24:54.663402-0500	audiomxd	UpdateAudioState CID 0x91550001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	17:24:54.663429-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 43, PID = 21495, Name = sid:0x1f402a, Nexy(21495), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	17:24:54.663465-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 43, PID = 21495, Name = sid:0x1f402a, Nexy(21495), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = YES>
default	17:24:54.663495-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found 2 different sessions firstSession={clientName:'sid:0x1f402a, Nexy(21495), 'prim'', displayID:'com.nexy.assistant'}, secondSession={clientName:'sid:0x1f402b, VoiceOver(21533), 'prim'', displayID:'com.apple.VoiceOver'} but will use session={clientName:'(null)', displayID:'(null)'}
default	17:24:54.663428-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	17:24:54.663494-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	17:24:54.663537-0500	audiomxd	UpdateAudioState CID 0x91550001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	17:24:54.663538-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1f402a, Nexy(21495), 'prim' with category(MediaPlayback)/mode(Default) and coreSessionID = 43 stopping recording
default	17:24:54.663522-0500	audioaccessoryd	AudioStateChanged: Added audio session app com.nexy.assistant 501 -> 200 count 3
default	17:24:54.663578-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 43, PID = 21495, Name = sid:0x1f402a, Nexy(21495), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	17:24:54.663569-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	17:24:54.663614-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 43, PID = 21495, Name = sid:0x1f402a, Nexy(21495), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO>
default	17:24:54.663620-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	17:24:54.663703-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	17:24:54.663695-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found 2 different sessions firstSession={clientName:'sid:0x1f402a, Nexy(21495), 'prim'', displayID:'com.nexy.assistant'}, secondSession={clientName:'sid:0x1f402b, VoiceOver(21533), 'prim'', displayID:'com.apple.VoiceOver'} but will use session={clientName:'(null)', displayID:'(null)'}
default	17:24:54.663789-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	17:24:54.663919-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 1]. BT device UIDS: {(
)}
default	17:24:54.663738-0500	audiomxd	UpdateAudioState CID 0x91550001 audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	17:24:54.663948-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	17:24:54.663889-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	17:24:54.663980-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 201,
}
default	17:24:54.664014-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	17:24:54.664104-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	17:24:54.664149-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	17:24:54.664159-0500	audioaccessoryd	AudioStateChanged: Added audio session app com.nexy.assistant 200 -> 201 count 3
default	17:24:54.664186-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 201
default	17:24:54.676096-0500	Nexy	nw_path_libinfo_path_check [5CBD92FD-6720-4E8C-BD7E-3B38AECB85D3 Hostname#2f11c8a7:80 tcp, legacy-socket, attribution: developer]
	libinfo check path: <private>
default	17:24:54.676256-0500	mDNSResponder	[R16043] DNSServiceQueryRecord START -- qname: <mask.hash: 'WYUTXafykb7b/ZdEN+VCdQ=='>, qtype: A, flags: 0x1D000, interface index: 0, client pid: 21495 (Nexy), name hash: b360ab20
default	17:24:54.677042-0500	mDNSResponder	[R16044] DNSServiceQueryRecord START -- qname: <mask.hash: 'WYUTXafykb7b/ZdEN+VCdQ=='>, qtype: AAAA, flags: 0x1D000, interface index: 0, client pid: 21495 (Nexy), name hash: b360ab20
default	17:24:54.677823-0500	kernel	SK[6]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 43399222-0B3F-4524-B445-31EA4EE2BCAD flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=96,src=<IPv6-redacted>.55189,dst=<IPv6-redacted>.80,proto=0x06 mask=0x0000003f,hash=0x609e9c1a tp_proto=0x06"
default	17:24:54.677942-0500	kernel	tcp connect outgoing: [<IPv6-redacted>:55189<-><IPv6-redacted>:80] interface: en0 (skipped: 0)
so_gencnt: 5935455 t_state: SYN_SENT process: Nexy:21495 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 16 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x9ea5048e
default	17:24:54.721890-0500	kernel	tcp connected: [<IPv6-redacted>:55189<-><IPv6-redacted>:80] interface: en0 (skipped: 0)
so_gencnt: 5935455 t_state: ESTABLISHED process: Nexy:21495 SYN in/out: 1/2 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 16 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x9ea5048e
default	17:24:54.765700-0500	Nexy	                AUHAL.cpp:473   ~AUHAL: (0x83a050e40) Selecting device 0 from destructor
default	17:24:54.765717-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0x83a050e40)
default	17:24:54.765727-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0x83a050e40) not already running
default	17:24:54.765734-0500	Nexy	                AUHAL.cpp:687   SelectDevice: (0x83a050e40) disconnecting device 78
default	17:24:54.765752-0500	Nexy	                AUHAL.cpp:751   SelectDevice: (0x83a050e40) destroying ioproc 0xd for device 78
default	17:24:54.765800-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {BuiltInMicrophoneDevice, 0xd}
default	17:24:54.766423-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 1]. BT device UIDS: {(
)} Server update was not required.
default	17:24:54.766633-0500	Nexy	                AUHAL.cpp:853   SelectDevice: (0x83a050e40) nothing to setup
default	17:24:54.766650-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x83a050e40) adding 0 device listeners to device 0
default	17:24:54.766659-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x83a050e40) adding 0 device delegate listeners to device 0
default	17:24:54.766669-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x83a050e40) removing 7 device listeners from device 78
default	17:24:54.766973-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x83a050e40) removing 0 device delegate listeners from device 78
default	17:24:54.766993-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0x83a050e40)
default	17:24:55.352718-0500	kernel	tcp_connection_summary (tcp_usrclosed:3220)[<IPv6-redacted>:55189<-><IPv6-redacted>:80] interface: en0 (skipped: 0)
so_gencnt: 5935455 t_state: LAST_ACK process: Nexy:21495 Duration: 0.675 sec Conn_Time: 0.044 sec bytes in/out: 867/100398 pkts in/out: 4/27 pkt rxmit: 0 ooo pkts: 1 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 54.375 ms rttvar: 12.500 ms base rtt: 16 ms so_error: 0 svc/tc: 0 flow: 0x9ea5048e
default	17:24:55.352732-0500	kernel	tcp_connection_summary [<IPv6-redacted>:55189<-><IPv6-redacted>:80] interface: en0 (skipped: 0)
so_gencnt: 5935455 t_state: LAST_ACK process: Nexy:21495 flowctl: 0us (0x) SYN in/out: 2/2 FIN in/out: 1/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	17:24:56.840611-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 201
default	17:24:56.840708-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.nexy.assistant
default	17:24:57.951467-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Speaker App com.nexy.assistant, Score 201, Remote -1 NumofApp 2
default	17:24:59.355626-0500	find_contacts_by_name_swift	[0x100aacb20] activating connection: mach=true listener=false peer=false name=com.apple.tccd
default	17:24:59.356318-0500	find_contacts_by_name_swift	[0x100aada30] activating connection: mach=true listener=false peer=false name=com.apple.cfprefsd.daemon
default	17:24:59.356398-0500	find_contacts_by_name_swift	[0x100aadf70] activating connection: mach=true listener=false peer=false name=com.apple.cfprefsd.agent
default	17:24:59.356944-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=21554.1, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=21495, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=find_contacts_by_name_swift, pid=21554, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift}, },
default	17:24:59.358431-0500	find_contacts_by_name_swift	[0x100aad360] activating connection: mach=true listener=false peer=false name=com.apple.distributed_notifications@Uv3
default	17:24:59.358712-0500	find_contacts_by_name_swift	[0xa37034000] activating connection: mach=true listener=false peer=false name=com.apple.tccd
default	17:24:59.359255-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=21554.2, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=21495, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=find_contacts_by_name_swift, pid=21554, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift}, },
default	17:24:59.387278-0500	tccd	AUTHREQ_SUBJECT: msgID=21554.2, subject=com.nexy.assistant,
default	17:24:59.391058-0500	find_contacts_by_name_swift	[0xa37034000] invalidated after the last release of the connection object
default	17:24:59.391141-0500	find_contacts_by_name_swift	Adding shared photo decorator (includeSharedPhotoContacts=YES)
default	17:24:59.392781-0500	tccd	AUTHREQ_SUBJECT: msgID=21554.1, subject=com.nexy.assistant,
default	17:24:59.395934-0500	find_contacts_by_name_swift	[0x100aacb20] invalidated after the last release of the connection object
default	17:24:59.395948-0500	find_contacts_by_name_swift	[0xa37034000] activating connection: mach=true listener=false peer=false name=com.apple.tccd
default	17:24:59.396047-0500	find_contacts_by_name_swift	No persisted cache on this platform.
default	17:24:59.396183-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=21554.3, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=21495, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=find_contacts_by_name_swift, pid=21554, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift}, },
default	17:24:59.396238-0500	find_contacts_by_name_swift	[0xa37034140] activating connection: mach=true listener=false peer=false name=com.apple.tccd
default	17:24:59.396739-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=21554.4, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=21495, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=find_contacts_by_name_swift, pid=21554, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift}, },
default	17:24:59.396794-0500	tccd	AUTHREQ_SUBJECT: msgID=21554.3, subject=com.nexy.assistant,
default	17:24:59.397207-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x722e70f00 at /Applications/Nexy.app
default	17:24:59.398142-0500	tccd	AUTHREQ_SUBJECT: msgID=21554.4, subject=com.nexy.assistant,
default	17:24:59.399049-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x722e70c00 at /Applications/Nexy.app
default	17:24:59.408148-0500	find_contacts_by_name_swift	[0xa37034000] invalidated after the last release of the connection object
default	17:24:59.410413-0500	find_contacts_by_name_swift	[0xa37034140] invalidated after the last release of the connection object
default	17:24:59.410542-0500	find_contacts_by_name_swift	0000 BEGIN: Will execute fetch for request: <private>
default	17:24:59.410552-0500	find_contacts_by_name_swift	0000 Entry point: enumerateContactsWithFetchRequest:error:usingBlock:
default	17:24:59.410561-0500	find_contacts_by_name_swift	0000 Predicate: CNCDContactWithNamePredicate <private>
default	17:24:59.411468-0500	find_contacts_by_name_swift	[0xa37034000] activating connection: mach=true listener=false peer=false name=com.apple.AddressBook.ContactsAccountsService
default	17:24:59.412349-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=53693.69, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=21495, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=find_contacts_by_name_swift, pid=21554, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift}, requesting={TCCDProcess: identifier=com.apple.sandboxd, pid=53693, auid=0, euid=0, binary_path=/usr/libexec/sandboxd}, },
default	17:24:59.413640-0500	tccd	AUTHREQ_SUBJECT: msgID=53693.69, subject=com.nexy.assistant,
default	17:24:59.414385-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x722e70c00 at /Applications/Nexy.app
default	17:24:59.441905-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=53693.70, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=21495, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=find_contacts_by_name_swift, pid=21554, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift}, requesting={TCCDProcess: identifier=com.apple.sandboxd, pid=53693, auid=0, euid=0, binary_path=/usr/libexec/sandboxd}, },
default	17:24:59.443396-0500	tccd	AUTHREQ_SUBJECT: msgID=53693.70, subject=com.nexy.assistant,
default	17:24:59.443856-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x722e70c00 at /Applications/Nexy.app
default	17:24:59.488075-0500	find_contacts_by_name_swift	[0xa37034140] activating connection: mach=true listener=false peer=false name=com.apple.accountsd.accountmanager
fault	17:24:59.489078-0500	find_contacts_by_name_swift	Attempted to register account monitor for types client is not authorized to access: <private>
error	17:24:59.489114-0500	find_contacts_by_name_swift	<private> 0xa36c48640: Store registration failed: Error Domain=com.apple.accounts Code=7 "(null)"
error	17:24:59.489130-0500	find_contacts_by_name_swift	<private> 0xa36c48640: Update event received, but store registration failed. This event will be handled, but the behavior is undefined.
default	17:24:59.489820-0500	find_contacts_by_name_swift	[0xa37034280] activating connection: mach=true listener=false peer=false name=com.apple.tccd
default	17:24:59.490241-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=21554.5, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=21495, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=find_contacts_by_name_swift, pid=21554, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift}, },
default	17:24:59.491213-0500	tccd	AUTHREQ_SUBJECT: msgID=21554.5, subject=com.nexy.assistant,
default	17:24:59.491739-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x722e70c00 at /Applications/Nexy.app
default	17:24:59.510848-0500	find_contacts_by_name_swift	[0xa37034280] invalidated after the last release of the connection object
default	17:24:59.510888-0500	find_contacts_by_name_swift	Adding shared photo decorator (includeSharedPhotoContacts=YES)
default	17:24:59.514990-0500	find_contacts_by_name_swift	[0xa37034280] activating connection: mach=true listener=false peer=false name=com.apple.AddressBook.ContactsAccountsService
default	17:24:59.515394-0500	find_contacts_by_name_swift	[0xa37034280] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	17:24:59.515424-0500	find_contacts_by_name_swift	Will add prepared store without migration (path: file:///Users/sergiyzasorin/Library/Application%20Support/AddressBook/AddressBook-v22.abcddb)
default	17:24:59.515527-0500	find_contacts_by_name_swift	Will add XPC store with options: <private> <private>
default	17:24:59.517036-0500	find_contacts_by_name_swift	[0xa37036d00] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	17:24:59.517534-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=53435.2057, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=21495, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=find_contacts_by_name_swift, pid=21554, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=53435, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	17:24:59.517558-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=53435, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=find_contacts_by_name_swift, pid=21554, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift
default	17:24:59.518281-0500	tccd	AUTHREQ_SUBJECT: msgID=53435.2057, subject=com.nexy.assistant,
default	17:24:59.519205-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x722e70c00 at /Applications/Nexy.app
default	17:24:59.536020-0500	find_contacts_by_name_swift	[0xa37036d00] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	17:24:59.536072-0500	find_contacts_by_name_swift	[0xa37036d00] activating connection: mach=false listener=false peer=false name=(anonymous)
default	17:24:59.536113-0500	find_contacts_by_name_swift	[0xa37036e40] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	17:24:59.536644-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=53435.2058, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=21495, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=find_contacts_by_name_swift, pid=21554, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=53435, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	17:24:59.536659-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=53435, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=find_contacts_by_name_swift, pid=21554, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift
default	17:24:59.537296-0500	tccd	AUTHREQ_SUBJECT: msgID=53435.2058, subject=com.nexy.assistant,
default	17:24:59.537626-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x722e70c00 at /Applications/Nexy.app
default	17:24:59.547720-0500	find_contacts_by_name_swift	[0xa37036e40] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	17:24:59.547754-0500	find_contacts_by_name_swift	[0xa37036f80] activating connection: mach=false listener=false peer=false name=(anonymous)
default	17:24:59.547784-0500	find_contacts_by_name_swift	[0xa37036e40] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	17:24:59.548213-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=53435.2059, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=21495, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=find_contacts_by_name_swift, pid=21554, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=53435, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	17:24:59.548227-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=53435, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=find_contacts_by_name_swift, pid=21554, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift
default	17:24:59.548842-0500	tccd	AUTHREQ_SUBJECT: msgID=53435.2059, subject=com.nexy.assistant,
default	17:24:59.549170-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x722e70c00 at /Applications/Nexy.app
default	17:24:59.571557-0500	find_contacts_by_name_swift	[0xa37036e40] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	17:24:59.571587-0500	find_contacts_by_name_swift	[0xa37036e40] activating connection: mach=false listener=false peer=false name=(anonymous)
default	17:24:59.571613-0500	find_contacts_by_name_swift	[0xa370370c0] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	17:24:59.572026-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=53435.2060, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=21495, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=find_contacts_by_name_swift, pid=21554, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=53435, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	17:24:59.572047-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=53435, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=find_contacts_by_name_swift, pid=21554, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift
default	17:24:59.572603-0500	tccd	AUTHREQ_SUBJECT: msgID=53435.2060, subject=com.nexy.assistant,
default	17:24:59.572909-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x722e70c00 at /Applications/Nexy.app
default	17:24:59.582181-0500	find_contacts_by_name_swift	[0xa370370c0] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	17:24:59.582204-0500	find_contacts_by_name_swift	[0xa370370c0] activating connection: mach=false listener=false peer=false name=(anonymous)
default	17:24:59.585339-0500	find_contacts_by_name_swift	Did add XPC store
default	17:24:59.585346-0500	find_contacts_by_name_swift	Did add prepared store without migration (path: file:///Users/sergiyzasorin/Library/Application%20Support/AddressBook/AddressBook-v22.abcddb)
default	17:24:59.585411-0500	find_contacts_by_name_swift	[0xa37037700] activating connection: mach=true listener=false peer=false name=com.apple.analyticsd
default	17:24:59.586009-0500	find_contacts_by_name_swift	Received configuration update from daemon (initial)
default	17:24:59.586082-0500	find_contacts_by_name_swift	0xa370385e0: Using cached account information
default	17:24:59.586191-0500	find_contacts_by_name_swift	[0xa370653b0] Session created.
default	17:24:59.586194-0500	find_contacts_by_name_swift	[0xa370653b0] Session created with Mach Service: <private>
default	17:24:59.586199-0500	find_contacts_by_name_swift	[0xa37037840] activating connection: mach=true listener=false peer=false name=com.apple.contacts.account-caching
default	17:24:59.586229-0500	find_contacts_by_name_swift	[0xa370653b0] Session activated
default	17:24:59.587119-0500	find_contacts_by_name_swift	[0xa37037840] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	17:24:59.587121-0500	find_contacts_by_name_swift	[0xa370653b0] Session canceled.
default	17:24:59.587130-0500	find_contacts_by_name_swift	[0xa370653b0] Disposing of session
default	17:24:59.587238-0500	find_contacts_by_name_swift	[0xa37037840] activating connection: mach=true listener=false peer=false name=com.apple.AddressBook.ContactsAccountsService
default	17:24:59.587451-0500	find_contacts_by_name_swift	[0xa37037840] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	17:24:59.587461-0500	find_contacts_by_name_swift	Will add prepared store without migration (path: file:///Users/sergiyzasorin/Library/Application%20Support/AddressBook/Sources/4437DACA-BE14-412E-B504-7A2DD2E9DC7D/AddressBook-v22.abcddb)
default	17:24:59.587472-0500	find_contacts_by_name_swift	Will add XPC store with options: <private> <private>
default	17:24:59.588582-0500	find_contacts_by_name_swift	[0xa371ca300] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	17:24:59.588948-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=53435.2061, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=21495, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=find_contacts_by_name_swift, pid=21554, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=53435, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	17:24:59.588962-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=53435, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=find_contacts_by_name_swift, pid=21554, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift
default	17:24:59.589549-0500	tccd	AUTHREQ_SUBJECT: msgID=53435.2061, subject=com.nexy.assistant,
default	17:24:59.589874-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x722e70c00 at /Applications/Nexy.app
default	17:24:59.598889-0500	find_contacts_by_name_swift	[0xa371ca300] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	17:24:59.598907-0500	find_contacts_by_name_swift	[0xa371ca300] activating connection: mach=false listener=false peer=false name=(anonymous)
default	17:24:59.598927-0500	find_contacts_by_name_swift	[0xa371ca440] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	17:24:59.599276-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=53435.2062, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=21495, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=find_contacts_by_name_swift, pid=21554, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=53435, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	17:24:59.599292-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=53435, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=find_contacts_by_name_swift, pid=21554, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift
default	17:24:59.599809-0500	tccd	AUTHREQ_SUBJECT: msgID=53435.2062, subject=com.nexy.assistant,
default	17:24:59.600166-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x722e70c00 at /Applications/Nexy.app
default	17:24:59.611216-0500	find_contacts_by_name_swift	[0xa371ca440] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	17:24:59.611257-0500	find_contacts_by_name_swift	[0xa371ca580] activating connection: mach=false listener=false peer=false name=(anonymous)
default	17:24:59.611290-0500	find_contacts_by_name_swift	[0xa371ca440] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	17:24:59.611766-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=53435.2063, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=21495, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=find_contacts_by_name_swift, pid=21554, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=53435, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	17:24:59.611785-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=53435, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=find_contacts_by_name_swift, pid=21554, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift
default	17:24:59.612751-0500	tccd	AUTHREQ_SUBJECT: msgID=53435.2063, subject=com.nexy.assistant,
default	17:24:59.613873-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x722e70c00 at /Applications/Nexy.app
default	17:24:59.629712-0500	find_contacts_by_name_swift	[0xa371ca440] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	17:24:59.629743-0500	find_contacts_by_name_swift	[0xa371ca440] activating connection: mach=false listener=false peer=false name=(anonymous)
default	17:24:59.629767-0500	find_contacts_by_name_swift	[0xa371ca6c0] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	17:24:59.630362-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=53435.2064, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=21495, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=find_contacts_by_name_swift, pid=21554, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=53435, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	17:24:59.630378-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=53435, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=find_contacts_by_name_swift, pid=21554, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift
default	17:24:59.631278-0500	tccd	AUTHREQ_SUBJECT: msgID=53435.2064, subject=com.nexy.assistant,
default	17:24:59.631690-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x722e70c00 at /Applications/Nexy.app
default	17:24:59.647371-0500	find_contacts_by_name_swift	[0xa371ca6c0] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	17:24:59.647397-0500	find_contacts_by_name_swift	[0xa371ca6c0] activating connection: mach=false listener=false peer=false name=(anonymous)
default	17:24:59.650964-0500	find_contacts_by_name_swift	Did add XPC store
default	17:24:59.650978-0500	find_contacts_by_name_swift	Did add prepared store without migration (path: file:///Users/sergiyzasorin/Library/Application%20Support/AddressBook/Sources/4437DACA-BE14-412E-B504-7A2DD2E9DC7D/AddressBook-v22.abcddb)
default	17:24:59.651015-0500	find_contacts_by_name_swift	[0xa371ca940] activating connection: mach=true listener=false peer=false name=com.apple.AddressBook.ContactsAccountsService
default	17:24:59.651336-0500	find_contacts_by_name_swift	[0xa371ca940] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	17:24:59.651345-0500	find_contacts_by_name_swift	Will add prepared store without migration (path: file:///Users/sergiyzasorin/Library/Application%20Support/AddressBook/AddressBook-v22.abcddb)
default	17:24:59.651351-0500	find_contacts_by_name_swift	Will add XPC store with options: <private> <private>
default	17:24:59.652450-0500	find_contacts_by_name_swift	[0xa371e9400] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	17:24:59.653166-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=53435.2065, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=21495, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=find_contacts_by_name_swift, pid=21554, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=53435, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	17:24:59.653181-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=53435, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=find_contacts_by_name_swift, pid=21554, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift
default	17:24:59.653769-0500	tccd	AUTHREQ_SUBJECT: msgID=53435.2065, subject=com.nexy.assistant,
default	17:24:59.654066-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x722e70c00 at /Applications/Nexy.app
default	17:24:59.664195-0500	find_contacts_by_name_swift	[0xa371e9400] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	17:24:59.664217-0500	find_contacts_by_name_swift	[0xa371e9400] activating connection: mach=false listener=false peer=false name=(anonymous)
default	17:24:59.664238-0500	find_contacts_by_name_swift	[0xa371e9540] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	17:24:59.664632-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=53435.2066, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=21495, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=find_contacts_by_name_swift, pid=21554, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=53435, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	17:24:59.664650-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=53435, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=find_contacts_by_name_swift, pid=21554, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift
default	17:24:59.665230-0500	tccd	AUTHREQ_SUBJECT: msgID=53435.2066, subject=com.nexy.assistant,
default	17:24:59.665750-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x722e70c00 at /Applications/Nexy.app
default	17:24:59.675077-0500	find_contacts_by_name_swift	[0xa371e9540] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	17:24:59.675103-0500	find_contacts_by_name_swift	[0xa371e9680] activating connection: mach=false listener=false peer=false name=(anonymous)
default	17:24:59.675133-0500	find_contacts_by_name_swift	[0xa371e9540] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	17:24:59.675559-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=53435.2067, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=21495, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=find_contacts_by_name_swift, pid=21554, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=53435, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	17:24:59.675576-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=53435, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=find_contacts_by_name_swift, pid=21554, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift
default	17:24:59.676196-0500	tccd	AUTHREQ_SUBJECT: msgID=53435.2067, subject=com.nexy.assistant,
default	17:24:59.676532-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x722e70c00 at /Applications/Nexy.app
default	17:24:59.688785-0500	find_contacts_by_name_swift	[0xa371e9540] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	17:24:59.688801-0500	find_contacts_by_name_swift	[0xa371e97c0] activating connection: mach=false listener=false peer=false name=(anonymous)
default	17:24:59.688817-0500	find_contacts_by_name_swift	[0xa371e9540] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	17:24:59.689140-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=53435.2068, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=21495, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=find_contacts_by_name_swift, pid=21554, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=53435, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	17:24:59.689156-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=53435, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=find_contacts_by_name_swift, pid=21554, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift
default	17:24:59.689655-0500	tccd	AUTHREQ_SUBJECT: msgID=53435.2068, subject=com.nexy.assistant,
default	17:24:59.690148-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x722e70c00 at /Applications/Nexy.app
default	17:24:59.702986-0500	find_contacts_by_name_swift	[0xa371e9540] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	17:24:59.703016-0500	find_contacts_by_name_swift	[0xa371e9540] activating connection: mach=false listener=false peer=false name=(anonymous)
default	17:24:59.703505-0500	find_contacts_by_name_swift	Did add XPC store
default	17:24:59.703516-0500	find_contacts_by_name_swift	Did add prepared store without migration (path: file:///Users/sergiyzasorin/Library/Application%20Support/AddressBook/AddressBook-v22.abcddb)
default	17:24:59.708758-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=53435.2069, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=21495, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=find_contacts_by_name_swift, pid=21554, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=53435, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	17:24:59.708777-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=53435, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=find_contacts_by_name_swift, pid=21554, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift
default	17:24:59.709332-0500	tccd	AUTHREQ_SUBJECT: msgID=53435.2069, subject=com.nexy.assistant,
default	17:24:59.709836-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x722e70c00 at /Applications/Nexy.app
default	17:24:59.722266-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=53435.2070, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=21495, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=find_contacts_by_name_swift, pid=21554, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=53435, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	17:24:59.722280-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=53435, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=find_contacts_by_name_swift, pid=21554, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/Frameworks/modules/messages/find_contacts_by_name_swift
default	17:24:59.722763-0500	tccd	AUTHREQ_SUBJECT: msgID=53435.2070, subject=com.nexy.assistant,
default	17:24:59.723074-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x722e70c00 at /Applications/Nexy.app
default	17:24:59.734972-0500	find_contacts_by_name_swift	"ACMonitoredAccountStore: Fetching accounts of account type com.apple.account.CardDAV..."
error	17:24:59.740434-0500	find_contacts_by_name_swift	"Error returned from daemon: Error Domain=com.apple.accounts Code=7"
error	17:24:59.740467-0500	find_contacts_by_name_swift	"ACMonitoredAccountStore: Failed to fetch accounts: Error Domain=com.apple.accounts Code=7"
default	17:24:59.743334-0500	find_contacts_by_name_swift	0xa36c482c0: Posting CNCDContactStoreDidChangeNotification because accounts changed
default	17:24:59.743350-0500	find_contacts_by_name_swift	0xa370253e0: Updating using cached account information
default	17:24:59.763953-0500	find_contacts_by_name_swift	App is linked against Fall 2022 SDK or later
default	17:24:59.763962-0500	find_contacts_by_name_swift	Note access is not granted, so Notes are inaccessible
fault	17:24:59.764019-0500	find_contacts_by_name_swift	Attempt to read notes by an unentitled app
default	17:24:59.768446-0500	find_contacts_by_name_swift	decoratedContacts called with 1 contacts
default	17:24:59.768457-0500	find_contacts_by_name_swift	Validating keys for 7 descriptors
default	17:24:59.768469-0500	find_contacts_by_name_swift	Final keysToFetchVector: <private>
default	17:24:59.768471-0500	find_contacts_by_name_swift	Contains wallpaper key: 0
default	17:24:59.768475-0500	find_contacts_by_name_swift	Skipping: required keys missing
default	17:24:59.768481-0500	find_contacts_by_name_swift	0000 Contact: AC0B1878-D813-4721-AF37-E5AD5DF1D1F6:ABPerson
default	17:24:59.768547-0500	find_contacts_by_name_swift	0000 All results have been returned to the client
default	17:24:59.768568-0500	find_contacts_by_name_swift	0000 Time spent in client code: 56.0 µs
default	17:24:59.768578-0500	find_contacts_by_name_swift	0000 FINISH (358 ms)
default	17:24:59.768637-0500	find_contacts_by_name_swift	Entering exit handler.
default	17:24:59.768644-0500	find_contacts_by_name_swift	Queueing exit procedure onto XPC queue. Any further messages sent will be discarded. activeSendTransactions=0
default	17:24:59.768662-0500	find_contacts_by_name_swift	Cancelling XPC connection. Any further reply handler invocations will not retry messages
default	17:24:59.768666-0500	find_contacts_by_name_swift	[0xa37037700] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	17:24:59.768671-0500	find_contacts_by_name_swift	Exiting exit handler.
default	17:24:59.768682-0500	find_contacts_by_name_swift	XPC connection invalidated (daemon unloaded/disabled)
default	17:24:59.820302-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=21556.1, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=21495, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.osascript, pid=21556, auid=501, euid=501, binary_path=/usr/bin/osascript}, },
default	17:24:59.821017-0500	tccd	AUTHREQ_SUBJECT: msgID=21556.1, subject=com.nexy.assistant,
default	17:24:59.821338-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b5164000 at /Applications/Nexy.app
default	17:24:59.831675-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=391.947, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=21495, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.osascript, pid=21556, auid=501, euid=501, binary_path=/usr/bin/osascript}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=391, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	17:24:59.832134-0500	tccd	AUTHREQ_SUBJECT: msgID=391.947, subject=com.nexy.assistant,
default	17:24:59.832462-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b5164000 at /Applications/Nexy.app
default	17:24:59.859925-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b5165200 at /Applications/Nexy.app
default	17:24:59.882575-0500	Messages	TCCAccessRequestIndirect: TCCAccessRequestIndirect with pid 21394: target_identity: {
    kTCCCodeIdentityAuditToken = {length = 32, bytes = 0xf5010000 f5010000 14000000 f5010000 ... b7860100 83bc7900 };
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
default	17:24:59.896325-0500	tccd	target_executable_path_URL: file:///Applications/Nexy.app/Contents/MacOS/Nexy
default	17:25:00.991101-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Speaker App com.nexy.assistant, Score 201, Remote -1 NumofApp 2
default	17:25:03.993232-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Speaker App com.nexy.assistant, Score 201, Remote -1 NumofApp 2
default	17:25:05.594178-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	17:25:05.594353-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant)]
default	17:25:06.607352-0500	Nexy	[com.apple.controlcenter:950C5067-8704-4062-917B-7F9E4958E32D] Sending action(s) in update: NSSceneFenceAction
default	17:25:06.979955-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Speaker App com.nexy.assistant, Score 201, Remote -1 NumofApp 2
default	17:25:08.659389-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant", "scr:com.nexy.assistant"]
default	17:25:08.661230-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	17:25:08.661261-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	17:25:08.661298-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	17:25:08.661330-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	17:25:08.661350-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	17:25:08.661365-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	17:25:08.661716-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	17:25:09.993139-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Speaker App com.nexy.assistant, Score 201, Remote -1 NumofApp 2
default	17:25:11.436180-0500	Nexy	System appearance change
default	17:25:11.436237-0500	Nexy	Current system appearance, (HLTB: 1), (SLS: 0)
default	17:25:11.441472-0500	Nexy	Invalidate NSApp effectiveAppearance
default	17:25:11.442161-0500	Nexy	Current system appearance, (HLTB: 1), (SLS: 0)
default	17:25:11.603791-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found 2 different sessions firstSession={clientName:'sid:0x1f402a, Nexy(21495), 'prim'', displayID:'com.nexy.assistant'}, secondSession={clientName:'sid:0x1f402b, VoiceOver(21533), 'prim'', displayID:'com.apple.VoiceOver'} but will use session={clientName:'(null)', displayID:'(null)'}
default	17:25:11.604130-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 201
default	17:25:14.209187-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 201
default	17:25:14.209245-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.nexy.assistant
default	17:25:14.209280-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 201
default	17:25:14.209315-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.nexy.assistant
default	17:25:14.659482-0500	ControlCenter	Recent activity attributions changed to ["scr:com.nexy.assistant"]
default	17:25:15.993141-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Speaker App com.nexy.assistant, Score 201, Remote -1 NumofApp 2
default	17:25:16.274288-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.54878181.54878190(501)>:21495] from originator [osservice<com.apple.controlcenter(501)>:615] with description <RBSAssertionDescriptor| "FBWorkspace (BG-Active[40])" ID:400-615-17435 target:21495 attributes:[
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableLPRunReason-Suspend" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableRole-NonUI" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableJetsamPriority-Active" sourceEnvironment:"(null)">
	]>
default	17:25:16.274451-0500	runningboardd	Assertion 400-615-17435 (target:[app<application.com.nexy.assistant.54878181.54878190(501)>:21495]) will be created as active
default	17:25:16.274681-0500	ControlCenter	[app<application.com.nexy.assistant.54878181.54878190>:21495] Workspace state did change: XX-None[0] --> BG-Active[40] (assertion acquired).
default	17:25:16.274842-0500	runningboardd	[app<application.com.nexy.assistant.54878181.54878190(501)>:21495] Ignoring jetsam update because this process is not memory-managed
default	17:25:16.274856-0500	runningboardd	[app<application.com.nexy.assistant.54878181.54878190(501)>:21495] Ignoring suspend because this process is not lifecycle managed
default	17:25:16.274864-0500	runningboardd	[app<application.com.nexy.assistant.54878181.54878190(501)>:21495] Ignoring GPU update because this process is not GPU managed
default	17:25:16.274938-0500	runningboardd	[app<application.com.nexy.assistant.54878181.54878190(501)>:21495] Ignoring memory limit update because this process is not memory-managed
default	17:25:16.277930-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.54878181.54878190(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	17:25:16.278572-0500	ControlCenter	Received state update for 21495 (app<application.com.nexy.assistant.54878181.54878190(501)>, running-active-NotVisible
default	17:25:16.279073-0500	gamepolicyd	Received state update for 21495 (app<application.com.nexy.assistant.54878181.54878190(501)>, running-active-NotVisible
default	17:25:16.377399-0500	ControlCenter	[app<application.com.nexy.assistant.54878181.54878190>:21495] Workspace state did change: BG-Active[40] --> XX-None[0] (assertion dropped).
default	17:25:16.377521-0500	runningboardd	Invalidating assertion 400-615-17435 (target:[app<application.com.nexy.assistant.54878181.54878190(501)>:21495]) from originator [osservice<com.apple.controlcenter(501)>:615]
default	17:25:16.487324-0500	runningboardd	[app<application.com.nexy.assistant.54878181.54878190(501)>:21495] Ignoring jetsam update because this process is not memory-managed
default	17:25:16.487339-0500	runningboardd	[app<application.com.nexy.assistant.54878181.54878190(501)>:21495] Ignoring suspend because this process is not lifecycle managed
default	17:25:16.487375-0500	runningboardd	[app<application.com.nexy.assistant.54878181.54878190(501)>:21495] Ignoring GPU update because this process is not GPU managed
default	17:25:16.487423-0500	runningboardd	[app<application.com.nexy.assistant.54878181.54878190(501)>:21495] Ignoring memory limit update because this process is not memory-managed
default	17:25:16.491903-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.54878181.54878190(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	17:25:16.492178-0500	ControlCenter	Received state update for 21495 (app<application.com.nexy.assistant.54878181.54878190(501)>, running-active-NotVisible
default	17:25:16.495619-0500	gamepolicyd	Received state update for 21495 (app<application.com.nexy.assistant.54878181.54878190(501)>, running-active-NotVisible
default	17:25:18.546552-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.54878181.54878190(501)>:21495] from originator [osservice<com.apple.controlcenter(501)>:615] with description <RBSAssertionDescriptor| "FBWorkspace (BG-Active[40])" ID:400-615-17457 target:21495 attributes:[
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableLPRunReason-Suspend" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableRole-NonUI" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableJetsamPriority-Active" sourceEnvironment:"(null)">
	]>
default	17:25:18.546679-0500	runningboardd	Assertion 400-615-17457 (target:[app<application.com.nexy.assistant.54878181.54878190(501)>:21495]) will be created as active
default	17:25:18.549499-0500	runningboardd	[app<application.com.nexy.assistant.54878181.54878190(501)>:21495] Ignoring jetsam update because this process is not memory-managed
default	17:25:18.549612-0500	runningboardd	[app<application.com.nexy.assistant.54878181.54878190(501)>:21495] Ignoring suspend because this process is not lifecycle managed
default	17:25:18.550184-0500	runningboardd	[app<application.com.nexy.assistant.54878181.54878190(501)>:21495] Ignoring GPU update because this process is not GPU managed
default	17:25:18.550431-0500	runningboardd	[app<application.com.nexy.assistant.54878181.54878190(501)>:21495] Ignoring memory limit update because this process is not memory-managed
default	17:25:18.549320-0500	ControlCenter	[app<application.com.nexy.assistant.54878181.54878190>:21495] Workspace state did change: XX-None[0] --> BG-Active[40] (assertion acquired).
default	17:25:18.553632-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.54878181.54878190(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	17:25:18.554385-0500	ControlCenter	Received state update for 21495 (app<application.com.nexy.assistant.54878181.54878190(501)>, running-active-NotVisible
default	17:25:18.555119-0500	gamepolicyd	Received state update for 21495 (app<application.com.nexy.assistant.54878181.54878190(501)>, running-active-NotVisible
default	17:25:18.653448-0500	ControlCenter	[app<application.com.nexy.assistant.54878181.54878190>:21495] Workspace state did change: BG-Active[40] --> XX-None[0] (assertion dropped).
default	17:25:18.653548-0500	runningboardd	Invalidating assertion 400-615-17457 (target:[app<application.com.nexy.assistant.54878181.54878190(501)>:21495]) from originator [osservice<com.apple.controlcenter(501)>:615]
default	17:25:18.762213-0500	runningboardd	[app<application.com.nexy.assistant.54878181.54878190(501)>:21495] Ignoring jetsam update because this process is not memory-managed
default	17:25:18.762244-0500	runningboardd	[app<application.com.nexy.assistant.54878181.54878190(501)>:21495] Ignoring suspend because this process is not lifecycle managed
default	17:25:18.762269-0500	runningboardd	[app<application.com.nexy.assistant.54878181.54878190(501)>:21495] Ignoring GPU update because this process is not GPU managed
default	17:25:18.762324-0500	runningboardd	[app<application.com.nexy.assistant.54878181.54878190(501)>:21495] Ignoring memory limit update because this process is not memory-managed
default	17:25:18.765914-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.54878181.54878190(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	17:25:18.766170-0500	ControlCenter	Received state update for 21495 (app<application.com.nexy.assistant.54878181.54878190(501)>, running-active-NotVisible
default	17:25:18.767066-0500	gamepolicyd	Received state update for 21495 (app<application.com.nexy.assistant.54878181.54878190(501)>, running-active-NotVisible
default	17:25:18.996340-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Speaker App com.nexy.assistant, Score 201, Remote -1 NumofApp 2
default	17:25:19.339667-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=391.952, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=21495, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=391, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	17:25:19.339704-0500	tccd	requestor: TCCDProcess: identifier=com.apple.WindowServer, pid=391, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=21495, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	17:25:19.341845-0500	tccd	AUTHREQ_SUBJECT: msgID=391.952, subject=com.nexy.assistant,
default	17:25:19.343179-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b5164000 at /Applications/Nexy.app
default	17:25:19.779303-0500	WindowServer	d58fb[StealKeyFocusReturningID]: [DeferringManager] Updating policy {
    advicePolicy: .keyThief;
    frontmostProcess: 0x0-0xb70b7 (Arc) mainConnectionID: 8FBFF;
    keyThiefConnectionID: D58FB;
} for reason: key thief updated d58fb 0x0-0x215215 (Nexy)
default	17:25:19.779351-0500	WindowServer	<BSCompoundAssertion:0x830c11400> (com.apple.backboard.hid.delivery.localDelivery.preventFlushing) acquire for reason:key thief updated d58fb 0x0-0x215215 (Nexy) <1085> acq:0x832706800 count:1
default	17:25:19.795413-0500	Nexy	NSApp cache appearance:
-NSRequiresAquaSystemAppearance: 0
-appearance: (null)
-effectiveAppearance: <NSCompositeAppearance: 0x837d68780
 (
    "<NSAquaAppearance: 0x837d685a0>",
    "<NSSystemAppearance: 0x837d686e0>"
)>
default	17:25:19.838108-0500	Nexy	[com.apple.controlcenter:950C5067-8704-4062-917B-7F9E4958E32D] Sending action(s) in update: NSSceneFenceAction
default	17:25:19.876173-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.54878181.54878190(501)>:21495] from originator [osservice<com.apple.WindowServer(88)>:391] with description <RBSAssertionDescriptor| "AppVisible" ID:400-391-17463 target:21495 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"AppVisible" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	17:25:19.876264-0500	runningboardd	Assertion 400-391-17463 (target:[app<application.com.nexy.assistant.54878181.54878190(501)>:21495]) will be created as active
default	17:25:19.876701-0500	runningboardd	[app<application.com.nexy.assistant.54878181.54878190(501)>:21495] Ignoring jetsam update because this process is not memory-managed
default	17:25:19.876719-0500	runningboardd	[app<application.com.nexy.assistant.54878181.54878190(501)>:21495] Ignoring suspend because this process is not lifecycle managed
default	17:25:19.876739-0500	runningboardd	[app<application.com.nexy.assistant.54878181.54878190(501)>:21495] Ignoring GPU update because this process is not GPU managed
default	17:25:19.876782-0500	runningboardd	[app<application.com.nexy.assistant.54878181.54878190(501)>:21495] Ignoring memory limit update because this process is not memory-managed
default	17:25:19.880306-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.54878181.54878190(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	17:25:19.880955-0500	ControlCenter	Received state update for 21495 (app<application.com.nexy.assistant.54878181.54878190(501)>, running-active-NotVisible
default	17:25:19.881042-0500	gamepolicyd	Received state update for 21495 (app<application.com.nexy.assistant.54878181.54878190(501)>, running-active-NotVisible
default	17:25:19.896332-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.54878181.54878190(501)>:21495] from originator [osservice<com.apple.WindowServer(88)>:391] with description <RBSAssertionDescriptor| "FUSBProcessWindowState: visible" ID:400-391-17464 target:21495 attributes:[
	<RBSDomainAttribute| domain:"com.apple.fuseboard" name:"Visible" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	17:25:19.896421-0500	runningboardd	Assertion 400-391-17464 (target:[app<application.com.nexy.assistant.54878181.54878190(501)>:21495]) will be created as active
default	17:25:19.896825-0500	runningboardd	[app<application.com.nexy.assistant.54878181.54878190(501)>:21495] Ignoring jetsam update because this process is not memory-managed
default	17:25:19.896840-0500	runningboardd	[app<application.com.nexy.assistant.54878181.54878190(501)>:21495] Ignoring suspend because this process is not lifecycle managed
default	17:25:19.896858-0500	runningboardd	[app<application.com.nexy.assistant.54878181.54878190(501)>:21495] Ignoring GPU update because this process is not GPU managed
default	17:25:19.896934-0500	runningboardd	[app<application.com.nexy.assistant.54878181.54878190(501)>:21495] Ignoring memory limit update because this process is not memory-managed
default	17:25:19.896986-0500	runningboardd	[app<application.com.nexy.assistant.54878181.54878190(501)>:21495] visiblity is yes
default	17:25:19.900278-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.54878181.54878190(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	17:25:19.900865-0500	ControlCenter	Received state update for 21495 (app<application.com.nexy.assistant.54878181.54878190(501)>, running-active-NotVisible
default	17:25:19.900981-0500	gamepolicyd	Received state update for 21495 (app<application.com.nexy.assistant.54878181.54878190(501)>, running-active-NotVisible
default	17:25:21.121265-0500	Nexy	[C:3] Alloc com.apple.backboard.hid-services.xpc
default	17:25:21.121339-0500	Nexy	[0x836de0dc0] activating connection: mach=false listener=false peer=false name=(anonymous)
error	17:25:21.122111-0500	Nexy	Unable to obtain a task name port right for pid 391: (os/kern) failure (0x5)
default	17:25:21.122703-0500	Nexy	BKSHIDEventDeliveryManager - connection activation
default	17:25:21.130143-0500	Nexy	terminate:
default	17:25:21.130187-0500	Nexy	void _NSDisableAutomaticTerminationAndLog(NSString *) Terminating
default	17:25:21.130207-0500	Nexy	-[NSApplication _pushPersistentStateTerminationGeneration] sPersistentStateTerminateStackHeight -> 1
default	17:25:21.130327-0500	Nexy	Attempting sudden termination (1st attempt)
default	17:25:21.130343-0500	Nexy	Checking whether app should terminate
default	17:25:21.130420-0500	Nexy	Asking app delegate whether applicationShouldTerminate:
default	17:25:21.130439-0500	Nexy	replyToApplicationShouldTerminate:YES
default	17:25:21.130502-0500	Nexy	App termination approved
default	17:25:21.130511-0500	Nexy	Termination commencing
default	17:25:21.130521-0500	Nexy	Attempting sudden termination (2nd attempt)
default	17:25:21.132694-0500	Nexy	Termination complete. Exiting without sudden termination.
default	17:25:21.136009-0500	Nexy	[0x836de0f00] activating connection: mach=true listener=false peer=false name=com.apple.powerlog.plxpclogger.xpc
default	17:25:21.347898-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.54878181.54878190(501)>:21495] from originator [osservice<com.apple.controlcenter(501)>:615] with description <RBSAssertionDescriptor| "FBWorkspace (BG-Active[40])" ID:400-615-17470 target:21495 attributes:[
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableLPRunReason-Suspend" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableRole-NonUI" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableJetsamPriority-Active" sourceEnvironment:"(null)">
	]>
default	17:25:21.348010-0500	runningboardd	Assertion 400-615-17470 (target:[app<application.com.nexy.assistant.54878181.54878190(501)>:21495]) will be created as active
default	17:25:21.351716-0500	ControlCenter	[app<application.com.nexy.assistant.54878181.54878190>:21495] Workspace state did change: XX-None[0] --> BG-Active[40] (assertion acquired).
default	17:25:21.351972-0500	runningboardd	[app<application.com.nexy.assistant.54878181.54878190(501)>:21495] Ignoring jetsam update because this process is not memory-managed
default	17:25:21.352118-0500	runningboardd	[app<application.com.nexy.assistant.54878181.54878190(501)>:21495] Ignoring suspend because this process is not lifecycle managed
default	17:25:21.352154-0500	runningboardd	[app<application.com.nexy.assistant.54878181.54878190(501)>:21495] Ignoring GPU update because this process is not GPU managed
default	17:25:21.352220-0500	runningboardd	[app<application.com.nexy.assistant.54878181.54878190(501)>:21495] Ignoring memory limit update because this process is not memory-managed
default	17:25:21.354931-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.54878181.54878190(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	17:25:21.355473-0500	ControlCenter	Received state update for 21495 (app<application.com.nexy.assistant.54878181.54878190(501)>, running-active-NotVisible
default	17:25:21.355684-0500	gamepolicyd	Received state update for 21495 (app<application.com.nexy.assistant.54878181.54878190(501)>, running-active-NotVisible
default	17:25:21.994255-0500	audioaccessoryd	AudioStateSnapshot: BtState PoweredOn Route Speaker App com.nexy.assistant, Score 201, Remote -1 NumofApp 2
default	17:25:23.138879-0500	Nexy	Entering exit handler.
default	17:25:23.138941-0500	Nexy	Queueing exit procedure onto XPC queue. Any further messages sent will be discarded. activeSendTransactions=0
default	17:25:23.139043-0500	Nexy	Cancelling XPC connection. Any further reply handler invocations will not retry messages
default	17:25:23.139054-0500	Nexy	[0x836ac0000] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	17:25:23.139081-0500	Nexy	Exiting exit handler.
default	17:25:23.139112-0500	Nexy	XPC connection invalidated (daemon unloaded/disabled)
default	17:25:23.139698-0500	WindowServer	0[outside of RPC]: Process death: 0x0-0x215215 (Nexy) connectionID: D58FB pid: 21495 in session 0x101
default	17:25:23.139760-0500	WindowServer	<BSCompoundAssertion:0x830c11580> ([FocusManager:257]-deferringPolicyEvaluationSuppression) acquire for reason:process death - 0x0-0x215215 (Nexy) acq:0x8327048a0 count:1
default	17:25:23.140559-0500	audiomxd	  ServerSessionManager.mm:478   { "action":"destroy_session", "session":{"ID":"0x1f402a","name":"Nexy(21495)"}, "details":null }
default	17:25:23.140634-0500	audiomxd	AudioApplicationInfoImpl.mm:690   Successfully removed session 0x1f402a from AudioApp, recording state unchanged (app: {"name":"[implicit] Nexy","pid":21495})
default	17:25:23.140659-0500	audiomxd	  ServerSessionManager.mm:1086  destroy audio app instance since was created implicitly by session creation and all sessions now gone (audio app: {"name":"[implicit] Nexy","pid":21495})
default	17:25:23.141128-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsPlaying:]: MXCoreSession com.nexy.assistant with category/mode MediaPlayback/Default and coreSessionID = 43 stopping playing
default	17:25:23.141242-0500	audiomxd	-MXCoreSession- -[MXCoreSession endInterruption:]: Session <ID: 43, PID = 21495, Name = sid:0x1f402a, Nexy(21495), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> is going inactive
default	17:25:23.141357-0500	ControlCenter	[app<application.com.nexy.assistant.54878181.54878190>:21495] Workspace connection invalidated.
default	17:25:23.141392-0500	ControlCenter	[app<application.com.nexy.assistant.54878181.54878190>:21495] Now flagged as pending exit for reason: workspace client connection invalidated
default	17:25:23.141386-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 43, PID = 21495, Name = sid:0x1f402a, Nexy(21495), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	17:25:23.141680-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 43, PID = 21495, Name = sid:0x1f402a, Nexy(21495), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	17:25:23.142712-0500	WindowManager	Connection invalidated | (21495) Nexy
default	17:25:23.142538-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	17:25:23.142683-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	17:25:23.142729-0500	audioaccessoryd	AudioStateChanged: Removed audio session app com.nexy.assistant 201 count 1
default	17:25:23.142901-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	17:25:23.148302-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	17:25:23.141937-0500	audiomxd	UpdateAudioState CID 0x91550001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	17:25:23.142235-0500	audiomxd	UpdateAudioState CID 0x91550001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	17:25:23.149739-0500	WindowServer	0[outside of RPC]: [FocusManager:257] update to deferring policy requested for reason: permitted list updated - 0x0-0x215215 removed - but we are suppressing evaluation for reasons: {(
    "process death - 0x0-0x215215 (Nexy)"
)}
default	17:25:23.150433-0500	WindowServer	0[outside of RPC]: [FocusManager:257] update to deferring policy requested for reason: permitted list updated - 0x1-0x53f7 removed - but we are suppressing evaluation for reasons: {(
    "process death - 0x0-0x215215 (Nexy)"
)}
default	17:25:23.154875-0500	runningboardd	Invalidating assertion 400-391-17464 (target:[app<application.com.nexy.assistant.54878181.54878190(501)>:21495]) from originator [osservice<com.apple.WindowServer(88)>:391]
default	17:25:23.155035-0500	runningboardd	XPC connection invalidated: [app<application.com.nexy.assistant.54878181.54878190(501)>:21495]
default	17:25:23.155183-0500	runningboardd	Invalidating assertion 400-332-17257 (target:[app<application.com.nexy.assistant.54878181.54878190(501)>:21495]) from originator [osservice<com.apple.powerd>:332]
default	17:25:23.155447-0500	runningboardd	Invalidating assertion 400-391-17463 (target:[app<application.com.nexy.assistant.54878181.54878190(501)>:21495]) from originator [osservice<com.apple.WindowServer(88)>:391]
default	17:25:23.171817-0500	mDNSResponder	[R15987] DNSServiceCreateConnection STOP PID[21495](Nexy)
default	17:25:23.171848-0500	kernel	tcp_connection_summary (tcp_drop:1453)[<IPv4-redacted>:55177<-><IPv4-redacted>:443] interface: en0 (skipped: 0)
so_gencnt: 5935053 t_state: CLOSED process: Nexy:21495 Duration: 83.993 sec Conn_Time: 0.029 sec bytes in/out: 4867/1973 pkts in/out: 14/10 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 33.656 ms rttvar: 15.000 ms base rtt: 20 ms so_error: 0 svc/tc: 0 flow: 0x831a8557
default	17:25:23.171861-0500	kernel	tcp_connection_summary [<IPv4-redacted>:55177<-><IPv4-redacted>:443] interface: en0 (skipped: 0)
so_gencnt: 5935053 t_state: CLOSED process: Nexy:21495 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 1/0 RST in/out: 0/1 AccECN (client/server): Disabled/Disabled
default	17:25:23.171889-0500	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:55179<-><IPv4-redacted>:443] interface: en0 (skipped: 0)
so_gencnt: 5935056 t_state: FIN_WAIT_1 process: Nexy:21495 Duration: 83.887 sec Conn_Time: 0.020 sec bytes in/out: 1887290/440133 pkts in/out: 265/82 pkt rxmit: 12 ooo pkts: 6 dup bytes in: 156 ACKs delayed: 155 delayed ACKs sent: 0
rtt: 53.531 ms rttvar: 14.312 ms base rtt: 20 ms so_error: 0 svc/tc: 0 flow: 0x997b93aa
default	17:25:23.171894-0500	kernel	tcp_connection_summary [<IPv4-redacted>:55179<-><IPv4-redacted>:443] interface: en0 (skipped: 0)
so_gencnt: 5935056 t_state: FIN_WAIT_1 process: Nexy:21495 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	17:25:23.172646-0500	runningboardd	[app<application.com.nexy.assistant.54878181.54878190(501)>:21495] termination reported by launchd (0, 0, 0)
default	17:25:23.172697-0500	runningboardd	Removing process: [app<application.com.nexy.assistant.54878181.54878190(501)>:21495]
default	17:25:23.172875-0500	runningboardd	Removing launch job for: [app<application.com.nexy.assistant.54878181.54878190(501)>:21495]
default	17:25:23.173069-0500	runningboardd	Removed job for [app<application.com.nexy.assistant.54878181.54878190(501)>:21495]
default	17:25:23.173105-0500	runningboardd	Removing assertions for terminated process: [app<application.com.nexy.assistant.54878181.54878190(501)>:21495]
default	17:25:23.173137-0500	runningboardd	Removed last relative-start-date-defining assertion for process app<application.com.nexy.assistant.54878181.54878190(501)>
default	17:25:23.177253-0500	ControlCenter	[app<application.com.nexy.assistant.54878181.54878190>:21495] Workspace assertion invalidated: <NSError: 0xc320d0240; domain: RBSAssertionErrorDomain; code: 1; "Assertions were invalidated">
default	17:25:23.180514-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.54878181.54878190(501)>: none (role: None) (endowments: (null))
default	17:25:23.180711-0500	ControlCenter	[app<application.com.nexy.assistant.54878181.54878190>:21495] Process exited: <RBSProcessExitContext| voluntary>.
default	17:25:23.180727-0500	ControlCenter	[app<application.com.nexy.assistant.54878181.54878190>:21495] Setting process task state to: Not Running
default	17:25:23.180737-0500	ControlCenter	[app<application.com.nexy.assistant.54878181.54878190>:21495] Setting process visibility to: Unknown
default	17:25:23.180830-0500	audiomxd	  ServerSessionManager.mm:1327  Monitored process died, pid = 21495, name = Nexy
default	17:25:23.180773-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.54878181.54878190(501)>: none (role: None) (endowments: (null))
default	17:25:23.180767-0500	ControlCenter	[app<application.com.nexy.assistant.54878181.54878190>:21495] Invalidating workspace.
default	17:25:23.180835-0500	ControlCenter	Removing source registration for processHandle: [app<application.com.nexy.assistant.54878181.54878190(501)>:21495]
default	17:25:23.180890-0500	ControlCenter	Received state update for 21495 (app<application.com.nexy.assistant.54878181.54878190(501)>, none-NotVisible
default	17:25:23.181127-0500	ControlCenter	Received state update for 21495 (app<application.com.nexy.assistant.54878181.54878190(501)>, none-NotVisible
default	17:25:23.181220-0500	ControlCenter	Removing: <FBApplicationProcess: 0xc32031f80; app<application.com.nexy.assistant.54878181.54878190>:21495(v79BBE2)>
default	17:25:23.182147-0500	gamepolicyd	Received state update for 21495 (app<application.com.nexy.assistant.54878181.54878190(501)>, none-NotVisible
default	17:25:23.182291-0500	launchservicesd	Hit the server for a process handle 4fa432c000053f7 that resolved to: [app<application.com.nexy.assistant.54878181.54878190(501)>:21495]
default	17:25:23.184495-0500	loginwindow	-[ApplicationManager handleCASEvent:withData:] | CAS notification for appDeath for com.nexy.assistant with asn: LSASN:{hi=0x0;lo=0x215215} for bundle path: /Applications/Nexy.app with URL: file:///Applications/Nexy.app/
default	17:25:23.184535-0500	loginwindow	-[Application setState:] | enter: <Application: 0xc01219400: Nexy> state 3
default	17:25:23.184554-0500	loginwindow	-[PersistentAppsSupport applicationQuit:] | for app:Nexy, _appTrackingState = 2
default	17:25:23.184545-0500	ControlCenter	Stopping tracking for host; (bid:com.nexy.assistant-Item-0-21495)
default	17:25:23.185201-0500	ControlCenter	Removing ephemeral displayable instance DisplayableId(B14481AF) from menu bar. No corresponding host (bid:com.nexy.assistant-Item-0-21495)
default	17:25:23.185235-0500	ControlCenter	Removing displayables [DisplayableAppStatusItem(B14481AF, (bid:com.nexy.assistant-Item-0-21495))]
default	17:25:23.187028-0500	loginwindow	-[Application setState:] | enter: <Application: 0xc01219400: Nexy> state 4
default	17:25:23.187040-0500	loginwindow	-[PersistentAppsSupport applicationQuit:] | for app:Nexy, _appTrackingState = 2
error	17:25:23.354168-0500	runningboardd	RBSStateCapture remove item called for untracked item 400-391-17463 (target:[app<application.com.nexy.assistant.54878181.54878190(501)>:21495])
error	17:25:23.354203-0500	runningboardd	RBSStateCapture remove item called for untracked item 400-332-17257 (target:[app<application.com.nexy.assistant.54878181.54878190(501)>:21495])
error	17:25:23.354289-0500	runningboardd	RBSStateCapture remove item called for untracked item 400-391-17464 (target:[app<application.com.nexy.assistant.54878181.54878190(501)>:21495])
