default	20:21:18.619076-0500	lsd	com.nexy.assistant/Unknown Persona:5:5:1:1:Building bundle record for app
default	20:21:18.619308-0500	lsd	com.nexy.assistant/Unknown Persona:5:5:2:1:Built bundle record for app
default	20:21:18.647377-0500	dmd	Received xpc stream event (distributed notification matching) with name: com.apple.LaunchServices.applicationRegistered user info: {
    CFBundleDisplayName = Nexy;
    bundleIDs =     (
        "com.nexy.assistant"
    );
    isPlaceholder = 0;
}
default	20:21:18.688627-0500	runningboardd	[app<application.com.nexy.assistant.55704030.55704039(501)>:98220] is not RunningBoard jetsam managed.
default	20:21:18.688653-0500	runningboardd	[app<application.com.nexy.assistant.55704030.55704039(501)>:98220] This process will not be managed.
default	20:21:18.688666-0500	runningboardd	Now tracking process: [app<application.com.nexy.assistant.55704030.55704039(501)>:98220]
default	20:21:18.688843-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.55704030.55704039(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:21:18.694206-0500	runningboardd	[app<application.com.nexy.assistant.55704030.55704039(501)>:98220] Ignoring jetsam update because this process is not memory-managed
default	20:21:18.694226-0500	runningboardd	[app<application.com.nexy.assistant.55704030.55704039(501)>:98220] Ignoring suspend because this process is not lifecycle managed
default	20:21:18.694246-0500	runningboardd	[app<application.com.nexy.assistant.55704030.55704039(501)>:98220] Set darwin role to: UserInteractive
default	20:21:18.694269-0500	runningboardd	[app<application.com.nexy.assistant.55704030.55704039(501)>:98220] Ignoring GPU update because this process is not GPU managed
default	20:21:18.694288-0500	runningboardd	[app<application.com.nexy.assistant.55704030.55704039(501)>:98220] Ignoring memory limit update because this process is not memory-managed
default	20:21:18.694520-0500	runningboardd	[app<application.com.nexy.assistant.55704030.55704039(501)>:98220] reported to RB as running
default	20:21:18.710494-0500	loginwindow	-[ApplicationManager checkInAppContext:eventData:] | ApplicationManager: Checked in app : Nexy
default	20:21:18.711508-0500	gamepolicyd	Hit the server for a process handle 11f21e0100017fac that resolved to: [app<application.com.nexy.assistant.55704030.55704039(501)>:98220]
default	20:21:18.711558-0500	gamepolicyd	Received state update for 98220 (app<application.com.nexy.assistant.55704030.55704039(501)>, running-active-NotVisible
default	20:21:18.712096-0500	gamepolicyd	Received state update for 98220 (app<application.com.nexy.assistant.55704030.55704039(501)>, running-active-NotVisible
default	20:21:18.804177-0500	gamepolicyd	Received state update for 98220 (app<application.com.nexy.assistant.55704030.55704039(501)>, running-active-NotVisible
default	20:21:18.917390-0500	syspolicyd	GK evaluateScanResult: 3, PST: (path: a2cffff67b96be6e), (team: 5NKLL2CLB9), (id: com.nexy.assistant), (bundle_id: (null)), 0, 0, 1, 0, 9, 4, 1
default	20:21:18.919523-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=508.37, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=98220, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.syspolicyd, pid=508, auid=0, euid=0, binary_path=/usr/libexec/syspolicyd}, },
default	20:21:18.929059-0500	tccd	AUTHREQ_SUBJECT: msgID=508.37, subject=com.nexy.assistant,
default	20:21:18.930764-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b5166700 at /Applications/Nexy.app
default	20:21:18.948626-0500	syspolicyd	Found provenance data on target: TA(7383662ea0ebd7d1, 2), PST: (path: a2cffff67b96be6e), (team: 5NKLL2CLB9), (id: com.nexy.assistant), (bundle_id: (null))
default	20:21:19.162264-0500	Nexy	[0x106743300] activating connection: mach=true listener=false peer=false name=com.apple.cfprefsd.daemon
default	20:21:19.162341-0500	Nexy	[0x106742200] activating connection: mach=true listener=false peer=false name=com.apple.cfprefsd.agent
error	20:21:19.374448-0500	Nexy	dlsym cannot find symbol NSMakeRect in CFBundle 0x10672c3a0 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	20:21:19.374665-0500	Nexy	dlsym cannot find symbol NSMakePoint in CFBundle 0x10672c3a0 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	20:21:19.374867-0500	Nexy	dlsym cannot find symbol NSMakeSize in CFBundle 0x10672c3a0 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	20:21:19.375066-0500	Nexy	dlsym cannot find symbol NSMakeRange in CFBundle 0x10672c3a0 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
default	20:21:19.376517-0500	Nexy	[0x106744570] activating connection: mach=true listener=false peer=false name=com.apple.coreservices.launchservicesd
default	20:21:19.377727-0500	Nexy	[0x9a38cc000] activating connection: mach=true listener=false peer=false name=com.apple.analyticsd
default	20:21:19.378074-0500	Nexy	[0x9a38cc140] activating connection: mach=true listener=false peer=false name=com.apple.pasteboard.1
default	20:21:19.378628-0500	Nexy	[0x9a38cc280] activating connection: mach=true listener=false peer=false name=com.apple.distributed_notifications@Uv3
default	20:21:19.381171-0500	Nexy	void _NSDisableAutomaticTerminationAndLog(NSString *) No windows open yet
default	20:21:19.381541-0500	Nexy	[0x9a38cc3c0] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	20:21:19.382189-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=98220.1, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=98220, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	20:21:19.383857-0500	tccd	AUTHREQ_SUBJECT: msgID=98220.1, subject=com.nexy.assistant,
default	20:21:19.384629-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b5166a00 at /Applications/Nexy.app
default	20:21:19.398865-0500	Nexy	[0x9a38cc3c0] invalidated after the last release of the connection object
default	20:21:19.399256-0500	Nexy	server port 0x0000320b, session port 0x0000320b
default	20:21:19.400090-0500	Nexy	Received configuration update from daemon (initial)
default	20:21:19.400568-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=391.3295, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=98220, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=391, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	20:21:19.400603-0500	tccd	requestor: TCCDProcess: identifier=com.apple.WindowServer, pid=391, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=98220, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	20:21:19.401770-0500	tccd	AUTHREQ_SUBJECT: msgID=391.3295, subject=com.nexy.assistant,
default	20:21:19.402753-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b5166a00 at /Applications/Nexy.app
default	20:21:19.419678-0500	Nexy	New connection 0x148363 main
default	20:21:19.424371-0500	Nexy	CHECKIN: pid=98220
default	20:21:19.435631-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.55704030.55704039(501)>:98220] from originator [osservice<com.apple.coreservices.launchservicesd>:361] with description <RBSAssertionDescriptor| "uielement:98220" ID:400-361-143838 target:98220 attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"RoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	20:21:19.435781-0500	runningboardd	Assertion 400-361-143838 (target:[app<application.com.nexy.assistant.55704030.55704039(501)>:98220]) will be created as active
default	20:21:19.435853-0500	launchservicesd	CHECKIN:0x0-0x746746 98220 com.nexy.assistant
default	20:21:19.435998-0500	Nexy	CHECKEDIN: pid=98220 asn=0x0-0x746746 foreground=0
default	20:21:19.436304-0500	runningboardd	Invalidating assertion 400-361-143837 (target:[app<application.com.nexy.assistant.55704030.55704039(501)>:98220]) from originator [osservice<com.apple.coreservices.launchservicesd>:361]
default	20:21:19.436327-0500	Nexy	[0x9a38cc3c0] activating connection: mach=false listener=true peer=false name=(anonymous)
default	20:21:19.436345-0500	Nexy	[0x9a38cc3c0] Connection returned listener port: 0x4e03
default	20:21:19.436598-0500	Nexy	[0x9a2b88300] activating connection: mach=false listener=false peer=true name=com.apple.xpc.anonymous.0x9a38cc3c0.peer[361].0x9a2b88300
default	20:21:19.438107-0500	loginwindow	-[Application _updateInformationInternal] | Got App URL: file:///Applications/Nexy.app/
default	20:21:19.438231-0500	loginwindow	-[ApplicationManager checkInAppContext:eventData:] | ApplicationManager: Checked in app : Nexy
default	20:21:19.442616-0500	Nexy	FRONTLOGGING: version 1
default	20:21:19.442625-0500	Nexy	Registered, pid=98220 ASN=0x0,0x746746
default	20:21:19.442894-0500	WindowServer	148363[CreateApplication]: Process creation: 0x0-0x746746 (Nexy) connectionID: 148363 pid: 98220 in session 0x101
default	20:21:19.443275-0500	Nexy	[0x9a38cc500] activating connection: mach=true listener=false peer=false name=com.apple.lsd.mapdb
default	20:21:19.460659-0500	Nexy	[0x9a38cc3c0] Connection returned listener port: 0x4e03
default	20:21:19.461261-0500	Nexy	BringForward: pid=98220 asn=0x0-0x746746 bringForward=0 foreground=0 uiElement=1 launchedByLS=1 modifiersCount=1 allDisabled=0
default	20:21:19.461335-0500	Nexy	BringFrontModifier: pid=98220 asn=0x0-0x746746 Modifier 0 hideAfter=0 hideOthers=0 dontMakeFrontmost=0 mouseDown=0/0 seed=0/0
default	20:21:19.463054-0500	Nexy	Current system appearance, (HLTB: 2), (SLS: 1)
default	20:21:19.466384-0500	Nexy	No persisted cache on this platform.
default	20:21:19.468053-0500	Nexy	Current system appearance, (HLTB: 2), (SLS: 1)
default	20:21:19.468779-0500	Nexy	Post-registration system appearance: (HLTB: 2)
default	20:21:19.472357-0500	Nexy	FBSWorkspace: endpoint monitoring is disabled.
default	20:21:19.472371-0500	Nexy	FBSWorkspace: default shell endpoint is disabled.
default	20:21:19.472444-0500	Nexy	Initializing connection
default	20:21:19.472496-0500	Nexy	Removing all cached process handles
default	20:21:19.472517-0500	Nexy	Sending handshake request attempt #1 to server
default	20:21:19.472527-0500	Nexy	Creating connection to com.apple.runningboard
default	20:21:19.472538-0500	Nexy	[0x9a38cc780] activating connection: mach=true listener=false peer=false name=com.apple.runningboard
default	20:21:19.473040-0500	runningboardd	Setting client for [app<application.com.nexy.assistant.55704030.55704039(501)>:98220] as ready
default	20:21:19.473658-0500	Nexy	Handshake succeeded
default	20:21:19.473671-0500	Nexy	Identity resolved as app<application.com.nexy.assistant.55704030.55704039(501)>
default	20:21:19.483798-0500	Nexy	[0x9a38cc3c0] Connection returned listener port: 0x4e03
default	20:21:19.484962-0500	distnoted	register name: com.apple.xctest.FakeForceTouchDevice object: com.nexy.assistant token: 1e0000001d pid: 98220
default	20:21:19.492722-0500	Nexy	[0x9a38cc3c0] Connection returned listener port: 0x4e03
default	20:21:19.500819-0500	Nexy	Created a new Process Instance Registry XPC connection (inactive)
default	20:21:19.500858-0500	Nexy	[0x9a38cc8c0] activating connection: mach=true listener=false peer=false name=com.apple.linkd.autoShortcut
default	20:21:19.500982-0500	Nexy	Activated connection to com.apple.linkd.autoShortcut (ApplicationService)
default	20:21:19.501414-0500	Nexy	[0x9a38cca00] activating connection: mach=false listener=true peer=false name=(anonymous)
default	20:21:19.504180-0500	Nexy	[0x9a38cca00] Connection returned listener port: 0x6903
default	20:21:19.504909-0500	Nexy	Registered process with identifier 98220-10495980
default	20:21:20.971844-0500	kernel	SK[7]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid DEFC56F3-D5D2-4F93-873D-9F0E83E16E28 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.61500,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0x90e3e5bd tp_proto=0x06"
default	20:21:20.971976-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:61500<-><IPv4-redacted>:53] interface: en0 (skipped: 196)
so_gencnt: 8778436 t_state: SYN_SENT process: Nexy:98220 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x8a847fc6
default	20:21:23.988122-0500	runningboardd	Assertion did invalidate due to timeout: 400-400-143836 (target:[app<application.com.nexy.assistant.55704030.55704039(501)>:98220])
default	20:21:24.089020-0500	runningboardd	[app<application.com.nexy.assistant.55704030.55704039(501)>:98220] Ignoring jetsam update because this process is not memory-managed
default	20:21:24.089031-0500	runningboardd	[app<application.com.nexy.assistant.55704030.55704039(501)>:98220] Ignoring suspend because this process is not lifecycle managed
default	20:21:24.089046-0500	runningboardd	[app<application.com.nexy.assistant.55704030.55704039(501)>:98220] Ignoring GPU update because this process is not GPU managed
default	20:21:24.089063-0500	runningboardd	[app<application.com.nexy.assistant.55704030.55704039(501)>:98220] Ignoring memory limit update because this process is not memory-managed
default	20:21:24.090616-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.55704030.55704039(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:21:24.091542-0500	gamepolicyd	Received state update for 98220 (app<application.com.nexy.assistant.55704030.55704039(501)>, running-active-NotVisible
default	20:21:25.973495-0500	kernel	tcp_connection_summary (tcp_close:1797)[<IPv4-redacted>:61500<-><IPv4-redacted>:53] interface: en0 (skipped: 196)
so_gencnt: 8778436 t_state: SYN_SENT process: Nexy:98220 Duration: 5.002 sec Conn_Time: 0.000 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 0.000 ms rttvar: 250.000 ms base rtt: 0 ms so_error: 0 svc/tc: 0 flow: 0x8a847fc6
default	20:21:25.973534-0500	kernel	tcp_connection_summary [<IPv4-redacted>:61500<-><IPv4-redacted>:53] interface: en0 (skipped: 196)
so_gencnt: 8778436 t_state: SYN_SENT process: Nexy:98220 flowctl: 0us (0x) SYN in/out: 0/5 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	20:21:25.975086-0500	kernel	SK[1]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 1D4A505F-6620-4DFF-8846-320094C06034 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.61501,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0x1f21e185 tp_proto=0x06"
default	20:21:25.975256-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:61501<-><IPv4-redacted>:53] interface: en0 (skipped: 196)
so_gencnt: 8778437 t_state: SYN_SENT process: Nexy:98220 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x933587d8
default	20:21:29.338233-0500	Nexy	NotifyToken::RegisterDispatch(user.uid.501.com.apple.LaunchServices.database) fired for session key <private>
default	20:21:30.469480-0500	Nexy	LSExceptions shared instance invalidated for timeout.
default	20:21:30.974524-0500	kernel	tcp_connection_summary (tcp_close:1797)[<IPv4-redacted>:61501<-><IPv4-redacted>:53] interface: en0 (skipped: 196)
so_gencnt: 8778437 t_state: SYN_SENT process: Nexy:98220 Duration: 4.999 sec Conn_Time: 0.000 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 0.000 ms rttvar: 250.000 ms base rtt: 0 ms so_error: 0 svc/tc: 0 flow: 0x933587d8
default	20:21:30.974554-0500	kernel	tcp_connection_summary [<IPv4-redacted>:61501<-><IPv4-redacted>:53] interface: en0 (skipped: 196)
so_gencnt: 8778437 t_state: SYN_SENT process: Nexy:98220 flowctl: 0us (0x) SYN in/out: 0/5 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	20:21:30.982435-0500	Nexy	networkd_settings_read_from_file initialized networkd settings by reading plist directly
default	20:21:30.983325-0500	Nexy	networkd_settings_read_from_file initialized networkd settings by reading plist directly
default	20:21:30.986561-0500	Nexy	nw_path_libinfo_path_check [7B8F643C-BFBD-4BC3-9794-0FE9B0222235 Hostname#c33dd2db:53 tcp, legacy-socket, attribution: developer]
	libinfo check path: <private>
default	20:21:30.987499-0500	mDNSResponder	[R152305] DNSServiceCreateConnection START PID[98220](Nexy)
default	20:21:30.987862-0500	mDNSResponder	[R152306] DNSServiceQueryRecord START -- qname: <mask.hash: 'EZsJcryDavQKD3Th4XvA1g=='>, qtype: A, flags: 0x1D000, interface index: 0, client pid: 98220 (Nexy), name hash: f92d5498
default	20:21:30.988756-0500	mDNSResponder	[R152307] DNSServiceQueryRecord START -- qname: <mask.hash: 'EZsJcryDavQKD3Th4XvA1g=='>, qtype: AAAA, flags: 0x1D000, interface index: 0, client pid: 98220 (Nexy), name hash: f92d5498
default	20:21:31.023941-0500	kernel	SK[0]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 92651D2D-9B59-420C-BBC2-26B3D1F20767 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.61503,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0xce2e9f74 tp_proto=0x06"
default	20:21:31.024049-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:61503<-><IPv4-redacted>:53] interface: en0 (skipped: 196)
so_gencnt: 8778468 t_state: SYN_SENT process: Nexy:98220 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x8fd3d878
default	20:21:33.573945-0500	spindump	Nexy [98220]: spin: not sampling due to conditions 0x400000000
default	20:21:35.975941-0500	kernel	tcp_connection_summary (tcp_close:1797)[<IPv4-redacted>:61503<-><IPv4-redacted>:53] interface: en0 (skipped: 196)
so_gencnt: 8778468 t_state: SYN_SENT process: Nexy:98220 Duration: 4.952 sec Conn_Time: 0.000 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 0.000 ms rttvar: 250.000 ms base rtt: 0 ms so_error: 0 svc/tc: 0 flow: 0x8fd3d878
default	20:21:35.975979-0500	kernel	tcp_connection_summary [<IPv4-redacted>:61503<-><IPv4-redacted>:53] interface: en0 (skipped: 196)
so_gencnt: 8778468 t_state: SYN_SENT process: Nexy:98220 flowctl: 0us (0x) SYN in/out: 0/5 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	20:21:37.191335-0500	Nexy	Registered notify signal com.apple.caulk.alloc.rtdump (0)
default	20:21:37.192265-0500	Nexy	System_Input_Processing_Notification_Handler.mm:456   System_Input_Processing_Notification_Handler::is_vi_available(): Voice isolation DSP is available for client with bundle id com.nexy.assistant (AVFoundation is available, application is not in client deny list, application is not FaceTime variant)
default	20:21:37.194468-0500	Nexy	[0x9a38ccdc0] activating connection: mach=true listener=false peer=false name=com.apple.cmio.registerassistantservice.system-extensions
fault	20:21:37.199640-0500	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.55704030.55704039 AUID=501> and <type=Application identifier=application.com.nexy.assistant.55704030.55704039>
default	20:21:37.204895-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOInitializeListenersForBundleID: for <private> -> <private>
default	20:21:37.206629-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> vpio_preferenceChangedListener: new value ((null)) for key AUVoiceIOClients/com-nexy-assistant/AUVoiceIOChatFlavor, translatedBundleID com.nexy.assistant, bundleIDs {(
    "com.nexy.assistant"
)}
default	20:21:37.206809-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> vpio_preferenceChangedListener: new value ((null)) for key AUVoiceIOClients/com-nexy-assistant/AUVoiceIOIsAutoChatFlavorEnabled, translatedBundleID com.nexy.assistant, bundleIDs {(
    "com.nexy.assistant"
)}
default	20:21:37.207071-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetSupportedChatFlavorsForBundleID: <private>-><private> get supported chat flavors: <private>
default	20:21:37.207082-0500	Nexy	            HALSystem.cpp:134    Enabling HAL Voice Isolation support
default	20:21:37.207135-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetHiddenChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	20:21:37.207290-0500	Nexy	[0x9a38ccf00] activating connection: mach=true listener=false peer=false name=com.apple.tccd
default	20:21:37.207855-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=98220.2, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=98220, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	20:21:37.208440-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOHiddenChatFlavors newValue: (
    1
)
default	20:21:37.216639-0500	tccd	AUTHREQ_SUBJECT: msgID=98220.2, subject=com.nexy.assistant,
default	20:21:37.217677-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8eed50300 at /Applications/Nexy.app
default	20:21:37.232580-0500	Nexy	[0x9a38ccf00] invalidated after the last release of the connection object
default	20:21:37.232647-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetSupportedChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	20:21:37.236350-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOSupportedChatFlavors newValue: (
)
default	20:21:37.237843-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.3382, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=98220, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=392, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	20:21:37.239329-0500	tccd	AUTHREQ_SUBJECT: msgID=401.3382, subject=com.nexy.assistant,
default	20:21:37.240180-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8eed50300 at /Applications/Nexy.app
error	20:21:37.258383-0500	tccd	Request message contains a target_token to accessing_process (TCCDProcess: identifier=com.nexy.assistant, pid=98220, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy) but TCCDProcess: identifier=com.apple.audio.coreaudiod, pid=401, auid=202, euid=202, binary_path=/usr/sbin/coreaudiod is not a TCC manager for service: kTCCServiceScreenCapture.
default	20:21:37.259459-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.3384, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=98220, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=392, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	20:21:37.260720-0500	tccd	AUTHREQ_SUBJECT: msgID=401.3384, subject=com.nexy.assistant,
default	20:21:37.261575-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8eed50300 at /Applications/Nexy.app
default	20:21:37.279006-0500	Nexy	  HALPlugInManagement.cpp:440    HALPlugInManagement::RegisterPlugIns: skipping in-process plug-ins
error	20:21:37.279491-0500	Nexy	AddInstanceForFactory: No factory registered for id <CFUUID 0x9a53da920> F8BB1C28-BAE8-11D6-9C31-00039315CD46
default	20:21:37.300791-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	20:21:37.300942-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	20:21:37.306338-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetPreferredChatFlavorForBundleID: <private>-><private> get value: 0
default	20:21:37.312086-0500	Nexy	[0x9a38ccf00] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioComponentRegistrar
default	20:21:37.324821-0500	Nexy	                AUHAL.cpp:420   AUHAL: (0x9a49f3840) Selecting device 85 from constructor
default	20:21:37.324829-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0x9a49f3840)
default	20:21:37.324834-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0x9a49f3840) not already running
default	20:21:37.325043-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0x9a49f3840) nothing to teardown
default	20:21:37.325050-0500	Nexy	                AUHAL.cpp:762   SelectDevice: (0x9a49f3840) connecting device 85
default	20:21:37.325134-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0x9a49f3840) Device ID: 85 (Input:No | Output:Yes): true
default	20:21:37.325218-0500	Nexy	                AUHAL.cpp:774   SelectDevice: (0x9a49f3840) created ioproc 0xa for device 85
default	20:21:37.325325-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x9a49f3840) adding 7 device listeners to device 85
default	20:21:37.325505-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x9a49f3840) adding 0 device delegate listeners to device 85
default	20:21:37.325514-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x9a49f3840)
default	20:21:37.325578-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  48000 Hz, Float32, interleaved
default	20:21:37.325587-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	20:21:37.325596-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	20:21:37.325602-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	20:21:37.325609-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	20:21:37.325705-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x9a49f3840) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	20:21:37.325711-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x9a49f3840) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	20:21:37.325716-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	20:21:37.325725-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x9a49f3840) removing 0 device listeners from device 0
default	20:21:37.325731-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x9a49f3840) removing 0 device delegate listeners from device 0
default	20:21:37.325736-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0x9a49f3840)
default	20:21:37.325747-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is DISABLED
default	20:21:37.325820-0500	Nexy	                AUHAL.cpp:2303  SetProperty: (0x9a49f3840) caller requesting device change from 85 to 91
default	20:21:37.325830-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0x9a49f3840)
default	20:21:37.325834-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0x9a49f3840) not already running
default	20:21:37.325838-0500	Nexy	                AUHAL.cpp:687   SelectDevice: (0x9a49f3840) disconnecting device 85
default	20:21:37.325841-0500	Nexy	                AUHAL.cpp:751   SelectDevice: (0x9a49f3840) destroying ioproc 0xa for device 85
default	20:21:37.325890-0500	Nexy	  AVAudioSession_MacOS.mm:1021  initForMacOS
default	20:21:37.326652-0500	Nexy	[0x9a38cd180] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioSession
default	20:21:37.327897-0500	audiomxd	  ServerSessionManager.mm:315   { "action":"create_session", "session":{"ID":"0x1f40ae","name":"Nexy(98220)"}, "details":{"PID":98220,"session_type":"Primary"} }
default	20:21:37.327979-0500	audiomxd	AudioApplicationInfoImpl.mm:250   Setting initial isRecording state: 0 for newly-created AudioApp
	app: {"name":"[implicit] Nexy","pid":98220}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1f40ae, sessionType: 'prim', isRecording: false }, 
]
default	20:21:37.328596-0500	audiomxd	  ServerSessionManager.mm:1322  Start process monitoring, pid = 98220, name = Nexy
default	20:21:37.328829-0500	Nexy	    SessionCore_Create.mm:99    Created session 0x9a392b880 with ID: 0x1f40ae
default	20:21:37.329828-0500	Nexy	[0x9a38cd2c0] activating connection: mach=true listener=false peer=false name=com.apple.audioanalyticsd
error	20:21:37.330207-0500	Nexy	Reporter disconnected. { function=sendMessage, reporterID=421851687813121 }
default	20:21:37.330219-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped Unknown {1C-77-54-18-C8-A3:output, 0xa}
default	20:21:37.330266-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	20:21:37.330349-0500	Nexy	                AUHAL.cpp:762   SelectDevice: (0x9a49f3840) connecting device 91
default	20:21:37.330434-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0x9a49f3840) Device ID: 91 (Input:Yes | Output:No): true
default	20:21:37.331644-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.3385, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=98220, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=392, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	20:21:37.332956-0500	tccd	AUTHREQ_SUBJECT: msgID=401.3385, subject=com.nexy.assistant,
default	20:21:37.333741-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8eed50300 at /Applications/Nexy.app
default	20:21:37.353646-0500	tccd	AUTHREQ_PROMPTING: msgID=401.3385, service=kTCCServiceMicrophone, subject=Sub:{com.nexy.assistant}Resp:{TCCDProcess: identifier=com.nexy.assistant, pid=98220, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy},
default	20:21:39.010823-0500	tccd	Publishing <TCCDEvent: type=Create, service=kTCCServiceMicrophone, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 3 subscribers: {
    39 = "<TCCDEventSubscriber: token=39, state=Passed, csid=com.apple.chronod>";
    38 = "<TCCDEventSubscriber: token=38, state=Initial, csid=(null)>";
    41 = "<TCCDEventSubscriber: token=41, state=Passed, csid=com.apple.photolibraryd>";
}
default	20:21:39.012058-0500	Nexy	                AUHAL.cpp:774   SelectDevice: (0x9a49f3840) created ioproc 0xa for device 91
default	20:21:39.012319-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x9a49f3840) adding 7 device listeners to device 91
default	20:21:39.012609-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x9a49f3840) adding 0 device delegate listeners to device 91
default	20:21:39.012624-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x9a49f3840)
default	20:21:39.012638-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 output streams; not all mono
default	20:21:39.012659-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	20:21:39.012895-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  input stream 0 [0x5c]:  1 ch,  24000 Hz, Float32
default	20:21:39.012907-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 input streams; all mono
default	20:21:39.012917-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  1 ch,  24000 Hz, Float32
default	20:21:39.013191-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x9a49f3840) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	20:21:39.013209-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x9a49f3840) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	20:21:39.013247-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	20:21:39.013293-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x9a49f3840) removing 7 device listeners from device 85
default	20:21:39.013514-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x9a49f3840) removing 0 device delegate listeners from device 85
default	20:21:39.013524-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0x9a49f3840)
default	20:21:39.014369-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	20:21:39.018342-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.3386, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=98220, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=392, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	20:21:39.032644-0500	tccd	AUTHREQ_SUBJECT: msgID=401.3386, subject=com.nexy.assistant,
default	20:21:39.033571-0500	chronod	[appAuth:com.nexy.assistant] tcc authorization(s) changed
default	20:21:39.034373-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8eed50300 at /Applications/Nexy.app
default	20:21:39.073338-0500	Nexy	       ACv2Workarounds.mm:51    com.nexy.assistant: fix84702776_86723525_86479548_89800354_SinglePacketDesc: false
default	20:21:39.073409-0500	Nexy	Registered notify signal com.apple.caulk.alloc.audiodump (0)
default	20:21:39.073503-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0x9a13eeee0, from  1 ch,  24000 Hz, Float32 to  1 ch,  16000 Hz, Float32
default	20:21:39.073757-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	20:21:39.075356-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.3387, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=98220, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=392, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	20:21:39.077033-0500	tccd	AUTHREQ_SUBJECT: msgID=401.3387, subject=com.nexy.assistant,
default	20:21:39.077809-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8eed50300 at /Applications/Nexy.app
default	20:21:39.101512-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.3388, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=98220, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=392, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	20:21:39.103045-0500	tccd	AUTHREQ_SUBJECT: msgID=401.3388, subject=com.nexy.assistant,
default	20:21:39.103889-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8eed50000 at /Applications/Nexy.app
default	20:21:39.131757-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetPreferredChatFlavorForBundleID: <private>-><private> get value: 0
default	20:21:39.132180-0500	coreaudiod	>>> NEGOTIATE [com.nexy.assistant]
default	20:21:39.132349-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetSupportedChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	20:21:39.132342-0500	coreaudiod	<<< NEGOTIATE [com.nexy.assistant]
default	20:21:39.134022-0500	coreaudiod	>>> ADAPT [com.nexy.assistant]
default	20:21:39.135641-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOSupportedChatFlavors newValue: (
    0,
    2
)
default	20:21:39.136406-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xafa0fd200] Created node ADM::com.nexy.assistant_7665.7540.0_airpods noise suppression studio::in-0 with nodeID 0 - reporting period = 10.000000, sample rate = 24000.000000
default	20:21:39.136470-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xafa0fd200] Created node ADM::com.nexy.assistant_7665.7540.0_airpods noise suppression studio::out-0 with nodeID 1 - reporting period = 10.000000, sample rate = 24000.000000
default	20:21:39.253875-0500	coreaudiod	<<< ADAPT [com.nexy.assistant]
default	20:21:39.255964-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Input {1C-77-54-18-C8-A3:input, 0xa}
default	20:21:39.255949-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:7665 called from <private>
default	20:21:39.256079-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	20:21:39.258899-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.55704030.55704039(501)>:98220] from originator [osservice<com.apple.powerd>:332] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:400-332-143888 target:98220 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	20:21:39.259001-0500	runningboardd	Assertion 400-332-143888 (target:[app<application.com.nexy.assistant.55704030.55704039(501)>:98220]) will be created as active
fault	20:21:39.260230-0500	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.55704030.55704039 AUID=501> and <type=Application identifier=application.com.nexy.assistant.55704030.55704039>
default	20:21:39.260649-0500	runningboardd	[app<application.com.nexy.assistant.55704030.55704039(501)>:98220] Ignoring jetsam update because this process is not memory-managed
default	20:21:39.260660-0500	runningboardd	[app<application.com.nexy.assistant.55704030.55704039(501)>:98220] Ignoring suspend because this process is not lifecycle managed
default	20:21:39.260670-0500	runningboardd	[app<application.com.nexy.assistant.55704030.55704039(501)>:98220] Ignoring GPU update because this process is not GPU managed
default	20:21:39.260689-0500	runningboardd	[app<application.com.nexy.assistant.55704030.55704039(501)>:98220] Ignoring memory limit update because this process is not memory-managed
fault	20:21:39.262914-0500	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.55704030.55704039 AUID=501> and <type=Application identifier=application.com.nexy.assistant.55704030.55704039>
default	20:21:39.263755-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:7665 called from <private>
default	20:21:39.264012-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(7665)
default	20:21:39.264030-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(7665)
default	20:21:39.264041-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:7665 called from <private>
default	20:21:39.264046-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:7665 called from <private>
default	20:21:39.264051-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:7665 called from <private>
default	20:21:39.264060-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:7665 called from <private>
default	20:21:39.264795-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(7664)
default	20:21:39.264866-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:7664 called from <private>
default	20:21:39.265022-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:7664 called from <private>
default	20:21:39.265913-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	20:21:39.266473-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	20:21:39.270347-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(7665)
default	20:21:39.270370-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(7665)
default	20:21:39.270379-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(7665)
default	20:21:39.270387-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(7665)
default	20:21:39.270395-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(7665)
default	20:21:39.274792-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:7665 called from <private>
default	20:21:39.274806-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:7665 called from <private>
default	20:21:39.274820-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:7665 called from <private>
default	20:21:39.274831-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:7665 called from <private>
default	20:21:39.274838-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:7665 called from <private>
default	20:21:39.275549-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.55704030.55704039(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:21:39.275960-0500	runningboardd	Invalidating assertion 400-332-143888 (target:[app<application.com.nexy.assistant.55704030.55704039(501)>:98220]) from originator [osservice<com.apple.powerd>:332]
default	20:21:39.276730-0500	gamepolicyd	Received state update for 98220 (app<application.com.nexy.assistant.55704030.55704039(501)>, running-active-NotVisible
default	20:21:39.280628-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(7665)
default	20:21:39.282113-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1f40ae","name":"Nexy(98220)"}, "details":{"deviceUIDs":["1C-77-54-18-C8-A3:input"],"implicit_category":"Record","input_running":true,"output_running":false} }
default	20:21:39.282190-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 174, PID = 98220, Name = sid:0x1f40ae, Nexy(98220), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	20:21:39.282653-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:7664 called from <private>
default	20:21:39.281846-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.3389, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=98220, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=392, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	20:21:39.282247-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 174, PID = 98220, Name = sid:0x1f40ae, Nexy(98220), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	20:21:39.282665-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:7664 called from <private>
default	20:21:39.282685-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 174, PID = 98220, Name = sid:0x1f40ae, Nexy(98220), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	20:21:39.282824-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 174, PID = 98220, Name = sid:0x1f40ae, Nexy(98220), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	20:21:39.282830-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(7664)
default	20:21:39.283004-0500	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 174, PID = 98220, Name = sid:0x1f40ae, Nexy(98220), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> is going active
default	20:21:39.282874-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:7664 called from <private>
default	20:21:39.283030-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1f40ae, Nexy(98220), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 174 starting recording
default	20:21:39.282881-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:7664 called from <private>
default	20:21:39.283577-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(7664)
default	20:21:39.283067-0500	audiomxd	UpdateAudioState CID 0x91550001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:21:39.283596-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(7664)
default	20:21:39.282325-0500	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1f40ae, Nexy(98220), 'prim'', AudioCategory changed to 'Record_WithBluetooth'
default	20:21:39.283607-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(7664)
default	20:21:39.283622-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:7664 called from <private>
default	20:21:39.283802-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 174, PID = 98220, Name = sid:0x1f40ae, Nexy(98220), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	20:21:39.283911-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 174, PID = 98220, Name = sid:0x1f40ae, Nexy(98220), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	20:21:39.283668-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:7664 called from <private>
default	20:21:39.283720-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:7664 called from <private>
default	20:21:39.283746-0500	audiomxd	UpdateAudioState CID 0x91550001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:21:39.283780-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:7664 called from <private>
default	20:21:39.283812-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:7664 called from <private>
default	20:21:39.283864-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:7664 called from <private>
default	20:21:39.284250-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:7664 called from <private>
default	20:21:39.284286-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:7664 called from <private>
default	20:21:39.284477-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [1, 0]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:input"
)}
default	20:21:39.284553-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	20:21:39.286376-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:7664 called from <private>
default	20:21:39.286416-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:7664 called from <private>
default	20:21:39.286541-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(7664)
default	20:21:39.286582-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:7664 called from <private>
default	20:21:39.286636-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:7664 called from <private>
default	20:21:39.286783-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(7664)
default	20:21:39.286842-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(7664)
default	20:21:39.286880-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(7664)
default	20:21:39.286972-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:7664 called from <private>
default	20:21:39.287025-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:7664 called from <private>
default	20:21:39.284116-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:21:39.284219-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:21:39.287062-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:7664 called from <private>
default	20:21:39.287097-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:7664 called from <private>
default	20:21:39.287127-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:7664 called from <private>
default	20:21:39.287163-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:7664 called from <private>
default	20:21:39.287210-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:7664 called from <private>
default	20:21:39.287276-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:7664 called from <private>
default	20:21:39.284517-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	20:21:39.292654-0500	tccd	AUTHREQ_SUBJECT: msgID=401.3389, subject=com.nexy.assistant,
default	20:21:39.327764-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 200 flag 0x1 < Hijack > app com.nexy.assistant CID 0x91550001 category Not set
default	20:21:39.317284-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:7664 called from <private>
default	20:21:39.337678-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	20:21:39.338232-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8eed50300 at /Applications/Nexy.app
default	20:21:39.350735-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:21:39.350805-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:21:39.350833-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:21:39.350939-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:21:39.350975-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:21:39.350997-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	20:21:39.352276-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	20:21:39.360944-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	20:21:39.387424-0500	coreaudiod	>>> NEGOTIATE [com.nexy.assistant]
default	20:21:39.387623-0500	coreaudiod	<<< NEGOTIATE [com.nexy.assistant]
default	20:21:39.391896-0500	runningboardd	[app<application.com.nexy.assistant.55704030.55704039(501)>:98220] Ignoring GPU update because this process is not GPU managed
default	20:21:39.391993-0500	runningboardd	[app<application.com.nexy.assistant.55704030.55704039(501)>:98220] Ignoring memory limit update because this process is not memory-managed
default	20:21:39.392455-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	20:21:39.392736-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	20:21:39.393140-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1f40ae","name":"Nexy(98220)"}, "details":{"deviceUIDs":[],"implicit_category":"","input_running":false,"output_running":false} }
default	20:21:39.392951-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xa}
default	20:21:39.393243-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 174, PID = 98220, Name = sid:0x1f40ae, Nexy(98220), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	20:21:39.392946-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	20:21:39.393296-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 174, PID = 98220, Name = sid:0x1f40ae, Nexy(98220), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	20:21:39.393554-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1f40ae, Nexy(98220), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 174 stopping recording
default	20:21:39.393641-0500	audiomxd	-MXCoreSession- -[MXCoreSession endInterruption:]: Session <ID: 174, PID = 98220, Name = sid:0x1f40ae, Nexy(98220), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> is going inactive
default	20:21:39.393774-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(7665)
default	20:21:39.393770-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 174, PID = 98220, Name = sid:0x1f40ae, Nexy(98220), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	20:21:39.401619-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	20:21:39.401689-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	20:21:39.401787-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	20:21:39.401998-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	20:21:39.402199-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:21:39.402215-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:21:39.402230-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:21:39.402244-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:21:39.402252-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:21:39.402261-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	20:21:39.402424-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	20:21:39.402515-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:21:39.402528-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:21:39.402539-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:21:39.402548-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:21:39.402556-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:21:39.402565-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	20:21:39.402652-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	20:21:39.503695-0500	runningboardd	[app<application.com.nexy.assistant.55704030.55704039(501)>:98220] Ignoring jetsam update because this process is not memory-managed
default	20:21:39.503710-0500	runningboardd	[app<application.com.nexy.assistant.55704030.55704039(501)>:98220] Ignoring suspend because this process is not lifecycle managed
default	20:21:39.503726-0500	runningboardd	[app<application.com.nexy.assistant.55704030.55704039(501)>:98220] Ignoring GPU update because this process is not GPU managed
default	20:21:39.503751-0500	runningboardd	[app<application.com.nexy.assistant.55704030.55704039(501)>:98220] Ignoring memory limit update because this process is not memory-managed
default	20:21:39.506138-0500	Nexy	                AUHAL.cpp:473   ~AUHAL: (0x9a49f3840) Selecting device 0 from destructor
default	20:21:39.506150-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0x9a49f3840)
default	20:21:39.506156-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0x9a49f3840) not already running
default	20:21:39.506164-0500	Nexy	                AUHAL.cpp:687   SelectDevice: (0x9a49f3840) disconnecting device 91
default	20:21:39.506169-0500	Nexy	                AUHAL.cpp:751   SelectDevice: (0x9a49f3840) destroying ioproc 0xa for device 91
default	20:21:39.506189-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xa}
default	20:21:39.506215-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	20:21:39.506341-0500	Nexy	                AUHAL.cpp:853   SelectDevice: (0x9a49f3840) nothing to setup
default	20:21:39.506352-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x9a49f3840) adding 0 device listeners to device 0
default	20:21:39.506357-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x9a49f3840) adding 0 device delegate listeners to device 0
default	20:21:39.506362-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x9a49f3840) removing 7 device listeners from device 91
default	20:21:39.506573-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x9a49f3840) removing 0 device delegate listeners from device 91
default	20:21:39.506589-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0x9a49f3840)
default	20:21:39.507153-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.55704030.55704039(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:21:39.507669-0500	gamepolicyd	Received state update for 98220 (app<application.com.nexy.assistant.55704030.55704039(501)>, running-active-NotVisible
default	20:21:42.025815-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(7665)
default	20:21:42.025866-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:7665 called from <private>
default	20:21:42.025873-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:7665 called from <private>
default	20:21:42.033436-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(7664)
default	20:21:42.033484-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:7664 called from <private>
default	20:21:42.033494-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:7664 called from <private>
default	20:21:42.044559-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(7665)
default	20:21:42.044601-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:7665 called from <private>
default	20:21:42.044609-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:7665 called from <private>
default	20:21:42.049031-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:7664 called from <private>
default	20:21:42.049052-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:7664 called from <private>
default	20:21:42.060118-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:7664 called from <private>
default	20:21:42.060139-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:7664 called from <private>
default	20:21:42.060302-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(7664)
default	20:21:42.065005-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(7664)
default	20:21:42.065316-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:7664 called from <private>
default	20:21:42.065329-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:7664 called from <private>
default	20:21:42.065476-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(7664)
default	20:21:42.072009-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(7664)
default	20:21:42.072067-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(7664)
default	20:21:42.072272-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:7664 called from <private>
default	20:21:42.072284-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:7664 called from <private>
default	20:21:42.072318-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:7664 called from <private>
default	20:21:42.072325-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:7664 called from <private>
default	20:21:42.072333-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:7664 called from <private>
default	20:21:42.072338-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:7664 called from <private>
default	20:21:42.073026-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:7664 called from <private>
default	20:21:42.073163-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:7664 called from <private>
default	20:21:42.073565-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:7664 called from <private>
default	20:21:42.073575-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:7664 called from <private>
default	20:21:42.073945-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:7664 called from <private>
default	20:21:42.073993-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:7664 called from <private>
default	20:21:42.074177-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:7664 called from <private>
default	20:21:42.074296-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:7664 called from <private>
default	20:21:42.074817-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(7664)
default	20:21:42.074861-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:7664 called from <private>
default	20:21:42.074918-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:7664 called from <private>
default	20:21:42.078066-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(7664)
default	20:21:42.078402-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:7664 called from <private>
default	20:21:42.078414-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:7664 called from <private>
default	20:21:42.078434-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:7664 called from <private>
default	20:21:42.078505-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:7664 called from <private>
default	20:21:42.083795-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(7664)
default	20:21:42.083849-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:7664 called from <private>
default	20:21:42.083858-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:7664 called from <private>
default	20:21:42.085222-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(7664)
default	20:21:42.085279-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:7664 called from <private>
default	20:21:42.085289-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:7664 called from <private>
default	20:21:42.085422-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(7664)
default	20:21:42.085441-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:7664 called from <private>
default	20:21:42.085721-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(7664)
default	20:21:42.085736-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:7664 called from <private>
default	20:21:42.086101-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(7664)
default	20:21:42.086373-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:7664 called from <private>
default	20:21:42.087001-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:7664 called from <private>
default	20:21:42.087285-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:7664 called from <private>
default	20:21:42.087552-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:7664 called from <private>
default	20:21:42.089915-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(7664)
default	20:21:42.090095-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:7664 called from <private>
default	20:21:42.090641-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:7664 called from <private>
default	20:21:54.512317-0500	Nexy	                AUHAL.cpp:420   AUHAL: (0x9a49f3840) Selecting device 85 from constructor
default	20:21:54.512347-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0x9a49f3840)
default	20:21:54.512357-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0x9a49f3840) not already running
default	20:21:54.512382-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0x9a49f3840) nothing to teardown
default	20:21:54.512398-0500	Nexy	                AUHAL.cpp:762   SelectDevice: (0x9a49f3840) connecting device 85
default	20:21:54.512543-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0x9a49f3840) Device ID: 85 (Input:No | Output:Yes): true
default	20:21:54.512701-0500	Nexy	                AUHAL.cpp:774   SelectDevice: (0x9a49f3840) created ioproc 0xb for device 85
default	20:21:54.512870-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x9a49f3840) adding 7 device listeners to device 85
default	20:21:54.513096-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x9a49f3840) adding 0 device delegate listeners to device 85
default	20:21:54.513107-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x9a49f3840)
default	20:21:54.513212-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  48000 Hz, Float32, interleaved
default	20:21:54.513226-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	20:21:54.513235-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	20:21:54.513247-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	20:21:54.513261-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	20:21:54.513408-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x9a49f3840) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	20:21:54.513426-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x9a49f3840) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	20:21:54.513433-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	20:21:54.513439-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x9a49f3840) removing 0 device listeners from device 0
default	20:21:54.513446-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x9a49f3840) removing 0 device delegate listeners from device 0
default	20:21:54.513451-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0x9a49f3840)
default	20:21:54.513473-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is DISABLED
default	20:21:54.513564-0500	Nexy	                AUHAL.cpp:2303  SetProperty: (0x9a49f3840) caller requesting device change from 85 to 91
default	20:21:54.513577-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0x9a49f3840)
default	20:21:54.513585-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0x9a49f3840) not already running
default	20:21:54.513592-0500	Nexy	                AUHAL.cpp:687   SelectDevice: (0x9a49f3840) disconnecting device 85
default	20:21:54.513597-0500	Nexy	                AUHAL.cpp:751   SelectDevice: (0x9a49f3840) destroying ioproc 0xb for device 85
default	20:21:54.513638-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped Unknown {1C-77-54-18-C8-A3:output, 0xb}
default	20:21:54.513686-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	20:21:54.513782-0500	Nexy	                AUHAL.cpp:762   SelectDevice: (0x9a49f3840) connecting device 91
default	20:21:54.513891-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0x9a49f3840) Device ID: 91 (Input:Yes | Output:No): true
default	20:21:54.516551-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.3390, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=98220, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=392, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	20:21:54.519588-0500	tccd	AUTHREQ_SUBJECT: msgID=401.3390, subject=com.nexy.assistant,
default	20:21:54.520895-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8eed50300 at /Applications/Nexy.app
default	20:21:54.549402-0500	Nexy	                AUHAL.cpp:774   SelectDevice: (0x9a49f3840) created ioproc 0xb for device 91
default	20:21:54.549604-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x9a49f3840) adding 7 device listeners to device 91
default	20:21:54.549814-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x9a49f3840) adding 0 device delegate listeners to device 91
default	20:21:54.549823-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0x9a49f3840)
default	20:21:54.549835-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 output streams; not all mono
default	20:21:54.549846-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	20:21:54.549983-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  input stream 0 [0x5c]:  1 ch,  24000 Hz, Float32
default	20:21:54.549989-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 input streams; all mono
default	20:21:54.550003-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  1 ch,  24000 Hz, Float32
default	20:21:54.550102-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0x9a49f3840) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	20:21:54.550112-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0x9a49f3840) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	20:21:54.550117-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	20:21:54.550123-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x9a49f3840) removing 7 device listeners from device 85
default	20:21:54.550297-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x9a49f3840) removing 0 device delegate listeners from device 85
default	20:21:54.550304-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0x9a49f3840)
default	20:21:54.550314-0500	Nexy	AudioHardware-mac-imp.cpp:1306   AudioObjectAddPropertyListener: listener was already added
default	20:21:54.550779-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	20:21:54.552000-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.3391, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=98220, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=392, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	20:21:54.553220-0500	tccd	AUTHREQ_SUBJECT: msgID=401.3391, subject=com.nexy.assistant,
default	20:21:54.553874-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8eed50300 at /Applications/Nexy.app
default	20:21:54.571842-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0x9a13ef060, from  1 ch,  24000 Hz, Float32 to  1 ch,  16000 Hz, Float32
default	20:21:54.572105-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	20:21:54.573319-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.3392, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=98220, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=392, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	20:21:54.574623-0500	tccd	AUTHREQ_SUBJECT: msgID=401.3392, subject=com.nexy.assistant,
default	20:21:54.575485-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8eed50300 at /Applications/Nexy.app
default	20:21:54.596374-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.3393, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=98220, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=392, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	20:21:54.597668-0500	tccd	AUTHREQ_SUBJECT: msgID=401.3393, subject=com.nexy.assistant,
default	20:21:54.598427-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8eed50300 at /Applications/Nexy.app
default	20:21:54.616638-0500	coreaudiod	>>> NEGOTIATE [com.nexy.assistant]
default	20:21:54.616835-0500	coreaudiod	<<< NEGOTIATE [com.nexy.assistant]
default	20:21:54.618652-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:7665 called from <private>
default	20:21:54.618730-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	20:21:54.618743-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Input {1C-77-54-18-C8-A3:input, 0xb}
default	20:21:54.619452-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(7664)
default	20:21:54.628179-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.55704030.55704039(501)>:98220] from originator [osservice<com.apple.powerd>:332] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:400-332-143916 target:98220 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	20:21:54.628896-0500	runningboardd	Assertion 400-332-143916 (target:[app<application.com.nexy.assistant.55704030.55704039(501)>:98220]) will be created as active
default	20:21:54.629710-0500	runningboardd	[app<application.com.nexy.assistant.55704030.55704039(501)>:98220] Ignoring jetsam update because this process is not memory-managed
default	20:21:54.629842-0500	runningboardd	[app<application.com.nexy.assistant.55704030.55704039(501)>:98220] Ignoring suspend because this process is not lifecycle managed
default	20:21:54.630009-0500	runningboardd	[app<application.com.nexy.assistant.55704030.55704039(501)>:98220] Ignoring GPU update because this process is not GPU managed
default	20:21:54.630384-0500	runningboardd	[app<application.com.nexy.assistant.55704030.55704039(501)>:98220] Ignoring memory limit update because this process is not memory-managed
default	20:21:54.633356-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	20:21:54.634104-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	20:21:54.619482-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:7664 called from <private>
default	20:21:54.619488-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:7664 called from <private>
default	20:21:54.623558-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:7665 called from <private>
default	20:21:54.623764-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(7665)
default	20:21:54.623781-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:7665 called from <private>
default	20:21:54.623788-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:7665 called from <private>
default	20:21:54.637365-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(7665)
default	20:21:54.637476-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(7665)
default	20:21:54.637538-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(7665)
default	20:21:54.637594-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(7665)
default	20:21:54.644324-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:7665 called from <private>
default	20:21:54.647918-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1f40ae","name":"Nexy(98220)"}, "details":{"deviceUIDs":["1C-77-54-18-C8-A3:input"],"implicit_category":"Record","input_running":true,"output_running":false} }
default	20:21:54.648024-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 174, PID = 98220, Name = sid:0x1f40ae, Nexy(98220), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	20:21:54.648056-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Category/Mode changed -- The score for sid:0x1f40ae, Nexy(98220), 'prim'/com.nexy.assistant was not correct. Old score = 201
default	20:21:54.648189-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 174, PID = 98220, Name = sid:0x1f40ae, Nexy(98220), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	20:21:54.647871-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.55704030.55704039(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:21:54.644336-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:7665 called from <private>
default	20:21:54.644359-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:7665 called from <private>
default	20:21:54.648329-0500	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1f40ae, Nexy(98220), 'prim'', AudioCategory changed to 'Record_WithBluetooth'
default	20:21:54.644376-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:7665 called from <private>
default	20:21:54.648461-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 174, PID = 98220, Name = sid:0x1f40ae, Nexy(98220), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	20:21:54.644382-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:7665 called from <private>
default	20:21:54.648401-0500	audiomxd	UpdateAudioState CID 0x91550001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:21:54.648521-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 174, PID = 98220, Name = sid:0x1f40ae, Nexy(98220), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	20:21:54.644388-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:7665 called from <private>
default	20:21:54.644397-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:7665 called from <private>
default	20:21:54.648750-0500	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 174, PID = 98220, Name = sid:0x1f40ae, Nexy(98220), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> is going active
default	20:21:54.648792-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1f40ae, Nexy(98220), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 174 starting recording
default	20:21:54.644860-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(7665)
default	20:21:54.648941-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 174, PID = 98220, Name = sid:0x1f40ae, Nexy(98220), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	20:21:54.648538-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:7664 called from <private>
default	20:21:54.648633-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:7664 called from <private>
default	20:21:54.648835-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(7664)
default	20:21:54.648873-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:7664 called from <private>
default	20:21:54.649020-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 174, PID = 98220, Name = sid:0x1f40ae, Nexy(98220), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	20:21:54.648900-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:7664 called from <private>
default	20:21:54.649346-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(7664)
default	20:21:54.649424-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(7664)
default	20:21:54.649466-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(7664)
default	20:21:54.649609-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:7664 called from <private>
default	20:21:54.649666-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:7664 called from <private>
default	20:21:54.649707-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:7664 called from <private>
default	20:21:54.649766-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:7664 called from <private>
default	20:21:54.649797-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:7664 called from <private>
default	20:21:54.649817-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:7664 called from <private>
default	20:21:54.648924-0500	runningboardd	Invalidating assertion 400-332-143916 (target:[app<application.com.nexy.assistant.55704030.55704039(501)>:98220]) from originator [osservice<com.apple.powerd>:332]
default	20:21:54.649859-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:7664 called from <private>
default	20:21:54.649892-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:7664 called from <private>
default	20:21:54.649665-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [1, 0]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:input"
)}
default	20:21:54.650010-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	20:21:54.650893-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:7664 called from <private>
default	20:21:54.650902-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:7664 called from <private>
default	20:21:54.651000-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(7664)
default	20:21:54.651038-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:7664 called from <private>
default	20:21:54.651093-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:7664 called from <private>
default	20:21:54.651308-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(7664)
default	20:21:54.651344-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(7664)
default	20:21:54.651432-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(7664)
default	20:21:54.651535-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:7664 called from <private>
default	20:21:54.651602-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:7664 called from <private>
default	20:21:54.648777-0500	audiomxd	UpdateAudioState CID 0x91550001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:21:54.651655-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:7664 called from <private>
default	20:21:54.648613-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:21:54.651710-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:7664 called from <private>
default	20:21:54.649849-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:21:54.649838-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	20:21:54.651741-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:7664 called from <private>
default	20:21:54.648751-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.3394, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=98220, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=392, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	20:21:54.652748-0500	gamepolicyd	Received state update for 98220 (app<application.com.nexy.assistant.55704030.55704039(501)>, running-active-NotVisible
default	20:21:54.651778-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:7664 called from <private>
default	20:21:54.651812-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:7664 called from <private>
default	20:21:54.651849-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:7664 called from <private>
default	20:21:54.731862-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	20:21:54.731880-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.55704030.55704039(501)>:98220] from originator [osservice<com.apple.powerd>:332] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:400-332-143923 target:98220 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	20:21:54.732012-0500	runningboardd	Assertion 400-332-143923 (target:[app<application.com.nexy.assistant.55704030.55704039(501)>:98220]) will be created as active
default	20:21:54.732110-0500	runningboardd	[app<application.com.nexy.assistant.55704030.55704039(501)>:98220] Ignoring jetsam update because this process is not memory-managed
default	20:21:54.732120-0500	runningboardd	[app<application.com.nexy.assistant.55704030.55704039(501)>:98220] Ignoring suspend because this process is not lifecycle managed
default	20:21:54.732194-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	20:21:54.732197-0500	runningboardd	[app<application.com.nexy.assistant.55704030.55704039(501)>:98220] Ignoring GPU update because this process is not GPU managed
default	20:21:54.732398-0500	runningboardd	[app<application.com.nexy.assistant.55704030.55704039(501)>:98220] Ignoring memory limit update because this process is not memory-managed
default	20:21:54.732676-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(7665)
default	20:21:54.732917-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:7665 called from <private>
default	20:21:54.732927-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:7665 called from <private>
default	20:21:54.732939-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:7665 called from <private>
default	20:21:54.741126-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	20:21:54.741178-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	20:21:54.741215-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	20:21:54.741408-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	20:21:54.741554-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:21:54.741569-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:21:54.741585-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:21:54.741594-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:21:54.741600-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:21:54.741612-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	20:21:54.741717-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	20:21:54.741795-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:21:54.741863-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:21:54.741875-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:21:54.741923-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:21:54.741954-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:21:54.741985-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	20:21:54.761053-0500	coreaudiod	>>> ADAPT [com.nexy.assistant]
default	20:21:54.763206-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xafa0fd200] Created node ADM::com.nexy.assistant_7665.7540.0_airpods noise suppression studio::in-0 with nodeID 0 - reporting period = 10.000000, sample rate = 24000.000000
default	20:21:54.763267-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xafa0fd200] Created node ADM::com.nexy.assistant_7665.7540.0_airpods noise suppression studio::out-0 with nodeID 1 - reporting period = 10.000000, sample rate = 24000.000000
default	20:21:54.826411-0500	coreaudiod	<<< ADAPT [com.nexy.assistant]
default	20:21:54.827435-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.55704030.55704039(501)>:98220] from originator [osservice<com.apple.powerd>:332] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:400-332-143924 target:98220 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	20:21:54.827503-0500	runningboardd	Assertion 400-332-143924 (target:[app<application.com.nexy.assistant.55704030.55704039(501)>:98220]) will be created as active
default	20:21:54.828011-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:7665 called from <private>
default	20:21:54.828028-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:7665 called from <private>
default	20:21:54.828341-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	20:21:54.828999-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:7665 called from <private>
default	20:21:54.829015-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:7665 called from <private>
default	20:21:54.829179-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:7665 called from <private>
default	20:21:54.829304-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:7665 called from <private>
default	20:21:54.829292-0500	runningboardd	Invalidating assertion 400-332-143924 (target:[app<application.com.nexy.assistant.55704030.55704039(501)>:98220]) from originator [osservice<com.apple.powerd>:332]
error	20:21:54.829322-0500	Nexy	         HALC_ProxyIOContext.cpp:1075  HALC_ProxyIOContext::_StartIO(): Start failed - StartAndWaitForState returned error 35
default	20:21:54.829329-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:7665 called from <private>
default	20:21:54.829432-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(7665)
default	20:21:54.829447-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:7665 called from <private>
default	20:21:54.829452-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:7665 called from <private>
default	20:21:54.830161-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	20:21:54.830298-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	20:21:54.830657-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(7665)
default	20:21:54.830918-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:7665 called from <private>
default	20:21:54.830929-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:7665 called from <private>
default	20:21:54.830940-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:7665 called from <private>
default	20:21:54.832242-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.3396, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=98220, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=392, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	20:21:54.833555-0500	tccd	AUTHREQ_SUBJECT: msgID=401.3396, subject=com.nexy.assistant,
default	20:21:54.834386-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8eed50300 at /Applications/Nexy.app
default	20:21:54.834969-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	20:21:54.835030-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	20:21:54.835072-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	20:21:54.835175-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	20:21:54.835515-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:21:54.835536-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:21:54.835547-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:21:54.835556-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:21:54.835577-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:21:54.835591-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	20:21:54.835715-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	20:21:54.847084-0500	runningboardd	[app<application.com.nexy.assistant.55704030.55704039(501)>:98220] Ignoring jetsam update because this process is not memory-managed
default	20:21:54.847098-0500	runningboardd	[app<application.com.nexy.assistant.55704030.55704039(501)>:98220] Ignoring suspend because this process is not lifecycle managed
default	20:21:54.847107-0500	runningboardd	[app<application.com.nexy.assistant.55704030.55704039(501)>:98220] Ignoring GPU update because this process is not GPU managed
default	20:21:54.847127-0500	runningboardd	[app<application.com.nexy.assistant.55704030.55704039(501)>:98220] Ignoring memory limit update because this process is not memory-managed
default	20:21:54.850353-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.55704030.55704039(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:21:54.850975-0500	gamepolicyd	Received state update for 98220 (app<application.com.nexy.assistant.55704030.55704039(501)>, running-active-NotVisible
default	20:21:54.856396-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.55704030.55704039(501)>:98220] from originator [osservice<com.apple.powerd>:332] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:400-332-143925 target:98220 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	20:21:54.856467-0500	runningboardd	Assertion 400-332-143925 (target:[app<application.com.nexy.assistant.55704030.55704039(501)>:98220]) will be created as active
default	20:21:54.857083-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:7665 called from <private>
default	20:21:54.857311-0500	runningboardd	[app<application.com.nexy.assistant.55704030.55704039(501)>:98220] Ignoring jetsam update because this process is not memory-managed
default	20:21:54.857328-0500	runningboardd	[app<application.com.nexy.assistant.55704030.55704039(501)>:98220] Ignoring suspend because this process is not lifecycle managed
default	20:21:54.857357-0500	runningboardd	[app<application.com.nexy.assistant.55704030.55704039(501)>:98220] Ignoring GPU update because this process is not GPU managed
default	20:21:54.857410-0500	runningboardd	[app<application.com.nexy.assistant.55704030.55704039(501)>:98220] Ignoring memory limit update because this process is not memory-managed
default	20:21:54.861588-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.55704030.55704039(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:21:54.862006-0500	gamepolicyd	Received state update for 98220 (app<application.com.nexy.assistant.55704030.55704039(501)>, running-active-NotVisible
default	20:21:54.864207-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	20:21:54.864269-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	20:21:54.864311-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	20:21:54.864630-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:21:54.864644-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:21:54.864655-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:21:54.864662-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:21:54.864679-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:21:54.864686-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	20:21:54.864768-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:21:54.864773-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	20:21:54.864782-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:21:54.864794-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:21:54.864804-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:21:54.864813-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:21:54.864835-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	20:21:54.866173-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:21:54.866189-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:21:54.866202-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:21:54.866210-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:21:54.866220-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:21:54.866230-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	20:21:54.866286-0500	ControlCenter	Navigating to new application [com.nexy.assistant]
default	20:21:54.997174-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xb}
default	20:21:54.997438-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1f40ae","name":"Nexy(98220)"}, "details":{"deviceUIDs":[],"implicit_category":"","input_running":false,"output_running":false} }
default	20:21:54.997524-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 174, PID = 98220, Name = sid:0x1f40ae, Nexy(98220), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	20:21:54.997566-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 174, PID = 98220, Name = sid:0x1f40ae, Nexy(98220), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	20:21:54.997669-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1f40ae, Nexy(98220), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 174 stopping recording
default	20:21:54.997687-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	20:21:54.997689-0500	audiomxd	-MXCoreSession- -[MXCoreSession endInterruption:]: Session <ID: 174, PID = 98220, Name = sid:0x1f40ae, Nexy(98220), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> is going inactive
default	20:21:54.997714-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 174, PID = 98220, Name = sid:0x1f40ae, Nexy(98220), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	20:21:54.997750-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 174, PID = 98220, Name = sid:0x1f40ae, Nexy(98220), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	20:21:54.997853-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 0]. BT device UIDS: {(
)}
default	20:21:54.997865-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	20:21:54.998074-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 200 flag 0x1 < Hijack > app com.nexy.assistant CID 0x91550001 category Not set
default	20:21:54.998426-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	20:21:54.998538-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:21:54.999087-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	20:21:54.999116-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	20:21:54.998258-0500	audiomxd	UpdateAudioState CID 0x91550001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	20:21:54.999335-0500	runningboardd	Invalidating assertion 400-332-143925 (target:[app<application.com.nexy.assistant.55704030.55704039(501)>:98220]) from originator [osservice<com.apple.powerd>:332]
default	20:21:54.998292-0500	audiomxd	UpdateAudioState CID 0x91550001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:21:54.999314-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:21:54.999352-0500	audioaccessoryd	AudioStateChanged: Removed audio session app com.nexy.assistant 201 count 3
default	20:21:55.999996-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	20:21:55.001153-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:21:55.001163-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:21:55.001177-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:21:55.001183-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:21:55.001190-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:21:55.001198-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	20:21:55.001285-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	20:21:55.098563-0500	Nexy	                AUHAL.cpp:473   ~AUHAL: (0x9a49f3840) Selecting device 0 from destructor
default	20:21:55.098577-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0x9a49f3840)
default	20:21:55.098586-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0x9a49f3840) not already running
default	20:21:55.098589-0500	Nexy	                AUHAL.cpp:687   SelectDevice: (0x9a49f3840) disconnecting device 91
default	20:21:55.098596-0500	Nexy	                AUHAL.cpp:751   SelectDevice: (0x9a49f3840) destroying ioproc 0xb for device 91
default	20:21:55.098622-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xb}
default	20:21:55.098649-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	20:21:55.098771-0500	Nexy	                AUHAL.cpp:853   SelectDevice: (0x9a49f3840) nothing to setup
default	20:21:55.098782-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x9a49f3840) adding 0 device listeners to device 0
default	20:21:55.098788-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0x9a49f3840) adding 0 device delegate listeners to device 0
default	20:21:55.098794-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x9a49f3840) removing 7 device listeners from device 91
default	20:21:55.098999-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0x9a49f3840) removing 0 device delegate listeners from device 91
default	20:21:55.099010-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0x9a49f3840)
default	20:21:55.103993-0500	runningboardd	[app<application.com.nexy.assistant.55704030.55704039(501)>:98220] Ignoring jetsam update because this process is not memory-managed
default	20:21:55.104005-0500	runningboardd	[app<application.com.nexy.assistant.55704030.55704039(501)>:98220] Ignoring suspend because this process is not lifecycle managed
default	20:21:55.104013-0500	runningboardd	[app<application.com.nexy.assistant.55704030.55704039(501)>:98220] Ignoring GPU update because this process is not GPU managed
default	20:21:55.104032-0500	runningboardd	[app<application.com.nexy.assistant.55704030.55704039(501)>:98220] Ignoring memory limit update because this process is not memory-managed
default	20:21:55.105436-0500	Nexy	[0x9a38cd400] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	20:21:55.106417-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=98220.3, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=98220, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	20:21:55.107243-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.55704030.55704039(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:21:55.107738-0500	gamepolicyd	Received state update for 98220 (app<application.com.nexy.assistant.55704030.55704039(501)>, running-active-NotVisible
default	20:21:55.107769-0500	tccd	AUTHREQ_SUBJECT: msgID=98220.3, subject=com.nexy.assistant,
default	20:21:55.108688-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b5165e00 at /Applications/Nexy.app
default	20:21:55.127372-0500	tccd	Notifying for access  kTCCServiceScreenCapture for target PID[98220], responsiblePID[98220], responsiblePath: /Applications/Nexy.app to UID: 501
default	20:21:55.127688-0500	Nexy	[0x9a38cd400] invalidated after the last release of the connection object
default	20:21:55.324206-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b5166a00 at /Applications/Nexy.app
default	20:21:55.348215-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b5166700 at /Applications/Nexy.app
default	20:21:55.353125-0500	tccd	Publishing <TCCDEvent: type=Modify, service=kTCCServiceScreenCapture, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 0 subscribers: {
}
default	20:21:57.423544-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:7664 called from <private>
default	20:21:57.423552-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:7664 called from <private>
default	20:21:57.424989-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(7664)
default	20:21:57.456007-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(7664)
default	20:21:57.456310-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:7664 called from <private>
error	20:21:59.775784-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceScreenCapture com.nexy.assistant none
default	20:22:03.735596-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b5167c00 at /Applications/Nexy.app
default	20:22:03.767508-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b5164f00 at /Applications/Nexy.app
default	20:22:03.781903-0500	tccd	Publishing <TCCDEvent: type=Modify, service=kTCCServiceScreenCapture, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 0 subscribers: {
}
error	20:22:03.995683-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceScreenCapture com.nexy.assistant full
error	20:22:04.999764-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceScreenCapture com.nexy.assistant full
error	20:22:04.064702-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceMicrophone com.nexy.assistant full
error	20:22:04.065948-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceMicrophone com.nexy.assistant full
default	20:22:10.136353-0500	Nexy	[0x9a38cd400] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	20:22:10.137234-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=98220.4, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=98220, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	20:22:10.138807-0500	tccd	AUTHREQ_SUBJECT: msgID=98220.4, subject=com.nexy.assistant,
default	20:22:10.140872-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b5167c00 at /Applications/Nexy.app
default	20:22:10.170006-0500	Nexy	[0x9a38cd400] invalidated after the last release of the connection object
default	20:22:10.177077-0500	Nexy	 [INFO] SLSWindowListCreateImageProxying:84 request: <private>
default	20:22:10.180339-0500	Nexy	[0x9a38cd400] activating connection: mach=true listener=false peer=false name=com.apple.replayd
default	20:22:10.180531-0500	Nexy	 [INFO] -[RPDaemonProxy consumeSandboxExtension:processNewConnection:]:568
default	20:22:10.181229-0500	Nexy	 [INFO] -[RPDaemonProxy proxyCoreGraphicsWithMethodType:config:machPort:completionHandler:]:1493
default	20:22:10.188817-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=82607.3, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=98220, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.replayd, pid=82607, auid=501, euid=501, binary_path=/usr/libexec/replayd}, },
default	20:22:10.188848-0500	tccd	requestor: TCCDProcess: identifier=com.apple.replayd, pid=82607, auid=501, euid=501, binary_path=/usr/libexec/replayd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=98220, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	20:22:10.189933-0500	tccd	AUTHREQ_SUBJECT: msgID=82607.3, subject=com.nexy.assistant,
default	20:22:10.190642-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b5167c00 at /Applications/Nexy.app
default	20:22:10.219391-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=391.3345, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=98220, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=391, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	20:22:10.219415-0500	tccd	requestor: TCCDProcess: identifier=com.apple.WindowServer, pid=391, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=98220, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	20:22:10.220330-0500	tccd	AUTHREQ_SUBJECT: msgID=391.3345, subject=com.nexy.assistant,
default	20:22:10.220954-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b5167c00 at /Applications/Nexy.app
default	20:22:10.241066-0500	Nexy	 [INFO] SLSWindowListCreateImageProxying_block_invoke:116 request: <private>, error: (null), output: <private>
default	20:22:10.247059-0500	kernel	udp connect: [<IPv4-redacted>:63992<-><IPv4-redacted>:80] interface:  (skipped: 209)
so_gencnt: 8779005 so_state: 0x0102 process: Nexy:98220 bytes in/out: 0/0 pkts in/out: 0/0 error: 0 so_error: 0 svc/tc: 0 flow: 0x8a401321
default	20:22:10.247211-0500	kernel	udp_connection_summary [<IPv4-redacted>:63992<-><IPv4-redacted>:80] interface: en0 (skipped: 209)
so_gencnt: 8779005 so_state: 0x0102 process: Nexy:98220 Duration: 0.000 sec Conn_Time: 0.000 sec bytes in/out: 0/18 pkts in/out: 0/1 rxnospace pkts/bytes: 0/0 so_error: 0 svc/tc: 0 flow: 0x8a401321 flowctl: 0us (0x)
default	20:22:10.248146-0500	Nexy	nw_path_libinfo_path_check [96BB3A1B-45B0-41BB-82D2-B8BC8D01C649 IPv4#d98c0339:53 tcp, legacy-socket, attribution: developer]
	libinfo check path: <private>
default	20:22:10.250140-0500	kernel	SK[7]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 32B4E9AC-5E02-4344-B9DB-3620FDEE127C flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.61518,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0xe7095510 tp_proto=0x06"
default	20:22:10.250236-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:61518<-><IPv4-redacted>:53] interface: en0 (skipped: 196)
so_gencnt: 8779006 t_state: SYN_SENT process: Nexy:98220 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xa1bdffb0
default	20:22:10.265227-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	20:22:10.265566-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant)]
default	20:22:10.265654-0500	ControlCenter	Active activity attributions changed to ["scr:com.nexy.assistant"]
default	20:22:10.268615-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:22:10.268629-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:22:10.268667-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:22:10.268676-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:22:10.268682-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:22:10.268691-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	20:22:10.268860-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	20:22:11.251346-0500	kernel	tcp_connection_summary (tcp_close:1797)[<IPv4-redacted>:61518<-><IPv4-redacted>:53] interface: en0 (skipped: 196)
so_gencnt: 8779006 t_state: SYN_SENT process: Nexy:98220 Duration: 1.001 sec Conn_Time: 0.000 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 0.000 ms rttvar: 250.000 ms base rtt: 0 ms so_error: 0 svc/tc: 0 flow: 0xa1bdffb0
default	20:22:11.251379-0500	kernel	tcp_connection_summary [<IPv4-redacted>:61518<-><IPv4-redacted>:53] interface: en0 (skipped: 196)
so_gencnt: 8779006 t_state: SYN_SENT process: Nexy:98220 flowctl: 0us (0x) SYN in/out: 0/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	20:22:11.254409-0500	kernel	tcp listen: [<IPv4-redacted>:61519<-><IPv4-redacted>:0] interface:  (skipped: 196)
so_gencnt: 8779012 t_state: LISTEN process: Nexy:98220 so_qlimit: 0 error: 0 so_error: 0 svc/tc: 0
default	20:22:11.254632-0500	kernel	tcp_connection_summary (tcp_close:1797)[<IPv4-redacted>:61519<-><IPv4-redacted>:0] interface:  (skipped: 196)
so_gencnt: 8779012 t_state: LISTEN process: Nexy:98220 Duration: 0.000 sec Conn_Time: 0.000 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 0.000 ms rttvar: 250.000 ms base rtt: 0 ms so_error: 0 svc/tc: 0 flow: 0x0
default	20:22:11.254652-0500	kernel	tcp_connection_summary [<IPv4-redacted>:61519<-><IPv4-redacted>:0] interface:  (skipped: 196)
so_gencnt: 8779012 t_state: LISTEN process: Nexy:98220 flowctl: 0us (0x) SYN in/out: 0/0 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	20:22:20.344645-0500	ControlCenter	Recent activity attributions changed to ["scr:com.nexy.assistant"]
default	20:22:26.262309-0500	Nexy	nw_path_libinfo_path_check [E72232E2-ADD3-4D2D-9DE8-77554E2EA2B4 IPv4#d98c0339:53 tcp, legacy-socket, attribution: developer]
	libinfo check path: <private>
default	20:22:26.263081-0500	kernel	SK[2]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 3ECF0EBC-5149-4ADD-A514-DB32FDBF5720 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.61524,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0x16aaf09c tp_proto=0x06"
default	20:22:26.263225-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:61524<-><IPv4-redacted>:53] interface: en0 (skipped: 196)
so_gencnt: 8779083 t_state: SYN_SENT process: Nexy:98220 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xa93d43c8
default	20:22:26.764354-0500	kernel	tcp_connection_summary (tcp_close:1797)[<IPv4-redacted>:61524<-><IPv4-redacted>:53] interface: en0 (skipped: 196)
so_gencnt: 8779083 t_state: SYN_SENT process: Nexy:98220 Duration: 0.501 sec Conn_Time: 0.000 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 0.000 ms rttvar: 250.000 ms base rtt: 0 ms so_error: 0 svc/tc: 0 flow: 0xa93d43c8
default	20:22:26.764389-0500	kernel	tcp_connection_summary [<IPv4-redacted>:61524<-><IPv4-redacted>:53] interface: en0 (skipped: 196)
so_gencnt: 8779083 t_state: SYN_SENT process: Nexy:98220 flowctl: 0us (0x) SYN in/out: 0/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	20:22:26.799803-0500	Nexy	[0x9a38cd540] activating connection: mach=true listener=false peer=false name=com.apple.tccd
default	20:22:26.800370-0500	Nexy	[0x9a38cd680] activating connection: mach=true listener=false peer=false name=com.apple.tccd
default	20:22:26.801211-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=98220.5, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=98220, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	20:22:26.801225-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=98220.6, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=98220, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	20:22:26.803606-0500	tccd	AUTHREQ_SUBJECT: msgID=98220.6, subject=com.nexy.assistant,
default	20:22:26.804033-0500	tccd	AUTHREQ_SUBJECT: msgID=98220.5, subject=com.nexy.assistant,
default	20:22:26.804518-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8eed50600 at /Applications/Nexy.app
default	20:22:26.806114-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8eed50900 at /Applications/Nexy.app
default	20:22:26.820678-0500	Nexy	[0x9a38cd680] invalidated after the last release of the connection object
default	20:22:26.820792-0500	Nexy	Adding shared photo decorator (includeSharedPhotoContacts=YES)
default	20:22:26.821788-0500	Nexy	[0x9a38cd680] activating connection: mach=true listener=false peer=false name=com.apple.tccd
default	20:22:26.822197-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=98220.7, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=98220, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	20:22:26.823007-0500	Nexy	[0x9a38cd540] invalidated after the last release of the connection object
default	20:22:26.823209-0500	tccd	AUTHREQ_SUBJECT: msgID=98220.7, subject=com.nexy.assistant,
default	20:22:26.823791-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8eed50000 at /Applications/Nexy.app
default	20:22:26.839170-0500	tccd	AUTHREQ_PROMPTING: msgID=98220.7, service=kTCCServiceAddressBook, subject=Sub:{com.nexy.assistant}Resp:{TCCDProcess: identifier=com.nexy.assistant, pid=98220, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy},
default	20:22:31.724219-0500	tccd	Publishing <TCCDEvent: type=Create, service=kTCCServiceAddressBook, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 3 subscribers: {
    39 = "<TCCDEventSubscriber: token=39, state=Passed, csid=com.apple.chronod>";
    38 = "<TCCDEventSubscriber: token=38, state=Initial, csid=(null)>";
    41 = "<TCCDEventSubscriber: token=41, state=Passed, csid=com.apple.photolibraryd>";
}
default	20:22:31.724641-0500	Nexy	[0x9a38cd680] invalidated after the last release of the connection object
default	20:22:31.740694-0500	chronod	[appAuth:com.nexy.assistant] tcc authorization(s) changed
default	20:22:31.791703-0500	Nexy	[0x9a38cd680] activating connection: mach=true listener=false peer=false name=com.apple.AddressBook.ContactsAccountsService
default	20:22:31.795347-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=93591.26, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=98220, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.sandboxd, pid=93591, auid=0, euid=0, binary_path=/usr/libexec/sandboxd}, },
default	20:22:31.797719-0500	tccd	AUTHREQ_SUBJECT: msgID=93591.26, subject=com.nexy.assistant,
default	20:22:31.799128-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8eed50300 at /Applications/Nexy.app
default	20:22:31.826915-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=93591.27, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=98220, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.sandboxd, pid=93591, auid=0, euid=0, binary_path=/usr/libexec/sandboxd}, },
default	20:22:31.828294-0500	tccd	AUTHREQ_SUBJECT: msgID=93591.27, subject=com.nexy.assistant,
default	20:22:31.828954-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8eed50300 at /Applications/Nexy.app
default	20:22:31.892704-0500	Nexy	[0x9a38cd540] activating connection: mach=true listener=false peer=false name=com.apple.accountsd.accountmanager
fault	20:22:31.893814-0500	Nexy	Attempted to register account monitor for types client is not authorized to access: <private>
error	20:22:31.893857-0500	Nexy	<private> 0x9a2c1af00: Store registration failed: Error Domain=com.apple.accounts Code=7 "(null)"
error	20:22:31.893878-0500	Nexy	<private> 0x9a2c1af00: Update event received, but store registration failed. This event will be handled, but the behavior is undefined.
default	20:22:31.894646-0500	Nexy	Adding shared photo decorator (includeSharedPhotoContacts=YES)
default	20:22:31.904907-0500	Nexy	[0x9a38cd7c0] activating connection: mach=true listener=false peer=false name=com.apple.AddressBook.ContactsAccountsService
default	20:22:31.909142-0500	Nexy	[0x9a3074280] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	20:22:31.910173-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=60336.1176, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=98220, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=60336, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	20:22:31.910208-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=60336, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=98220, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	20:22:31.913521-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8eed50300 at /Applications/Nexy.app
default	20:22:31.936759-0500	Nexy	[0x9a3074280] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	20:22:31.936861-0500	Nexy	[0x9a3074280] activating connection: mach=false listener=false peer=false name=(anonymous)
default	20:22:31.936958-0500	Nexy	[0x9a30743c0] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	20:22:31.937889-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=60336.1177, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=98220, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=60336, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	20:22:31.937922-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=60336, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=98220, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	20:22:31.962938-0500	Nexy	[0x9a30743c0] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	20:22:31.963093-0500	Nexy	[0x9a30743c0] activating connection: mach=false listener=false peer=false name=(anonymous)
default	20:22:31.963253-0500	Nexy	[0x9a3074500] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	20:22:31.964320-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=60336.1178, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=98220, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=60336, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	20:22:31.964358-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=60336, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=98220, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	20:22:31.965895-0500	tccd	AUTHREQ_SUBJECT: msgID=60336.1178, subject=com.nexy.assistant,
default	20:22:31.966779-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8eed50300 at /Applications/Nexy.app
default	20:22:31.989483-0500	Nexy	[0x9a3074500] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	20:22:31.989552-0500	Nexy	[0x9a3074500] activating connection: mach=false listener=false peer=false name=(anonymous)
default	20:22:31.989618-0500	Nexy	[0x9a3074640] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	20:22:31.990643-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=60336.1179, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=98220, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=60336, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	20:22:31.990704-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=60336, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=98220, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	20:22:31.992280-0500	tccd	AUTHREQ_SUBJECT: msgID=60336.1179, subject=com.nexy.assistant,
default	20:22:31.993094-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8eed50300 at /Applications/Nexy.app
default	20:22:32.015760-0500	Nexy	[0x9a3074640] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	20:22:32.015841-0500	Nexy	[0x9a3074640] activating connection: mach=false listener=false peer=false name=(anonymous)
default	20:22:32.028194-0500	Nexy	Did add XPC store
default	20:22:32.028215-0500	Nexy	Did add prepared store without migration (path: file:///Users/sergiyzasorin/Library/Application%20Support/AddressBook/AddressBook-v22.abcddb)
default	20:22:32.030997-0500	Nexy	0x9a3787b60: Using cached account information
default	20:22:32.031670-0500	Nexy	[0x9a3903700] Session created.
default	20:22:32.031685-0500	Nexy	[0x9a3903700] Session created with Mach Service: <private>
default	20:22:32.031696-0500	Nexy	[0x9a3074c80] activating connection: mach=true listener=false peer=false name=com.apple.contacts.account-caching
default	20:22:32.031883-0500	Nexy	[0x9a3903700] Session activated
default	20:22:32.035512-0500	Nexy	[0x9a3074c80] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	20:22:32.035521-0500	Nexy	[0x9a3903700] Session canceled.
default	20:22:32.035531-0500	Nexy	[0x9a3903700] Disposing of session
default	20:22:32.036276-0500	Nexy	[0x9a3074c80] activating connection: mach=true listener=false peer=false name=com.apple.AddressBook.ContactsAccountsService
default	20:22:32.037228-0500	Nexy	[0x9a3074c80] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	20:22:32.037267-0500	Nexy	Will add prepared store without migration (path: file:///Users/sergiyzasorin/Library/Application%20Support/AddressBook/Sources/4437DACA-BE14-412E-B504-7A2DD2E9DC7D/AddressBook-v22.abcddb)
default	20:22:32.037288-0500	Nexy	Will add XPC store with options: <private> <private>
default	20:22:32.042639-0500	Nexy	[0x9a3077700] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	20:22:32.044352-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=60336.1180, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=98220, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=60336, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	20:22:32.044388-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=60336, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=98220, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	20:22:32.046426-0500	tccd	AUTHREQ_SUBJECT: msgID=60336.1180, subject=com.nexy.assistant,
default	20:22:32.047457-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8eed50300 at /Applications/Nexy.app
default	20:22:32.077531-0500	Nexy	[0x9a3077700] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	20:22:32.077630-0500	Nexy	[0x9a3077700] activating connection: mach=false listener=false peer=false name=(anonymous)
default	20:22:32.077755-0500	Nexy	[0x9a3077840] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	20:22:32.079076-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=60336.1181, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=98220, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=60336, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	20:22:32.079114-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=60336, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=98220, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	20:22:32.081094-0500	tccd	AUTHREQ_SUBJECT: msgID=60336.1181, subject=com.nexy.assistant,
default	20:22:32.082119-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8eed50300 at /Applications/Nexy.app
default	20:22:32.112747-0500	Nexy	[0x9a3077840] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	20:22:32.112843-0500	Nexy	[0x9a3077840] activating connection: mach=false listener=false peer=false name=(anonymous)
default	20:22:32.112927-0500	Nexy	[0x9a3077980] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	20:22:32.114190-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=60336.1182, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=98220, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=60336, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	20:22:32.114228-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=60336, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=98220, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	20:22:32.115945-0500	tccd	AUTHREQ_SUBJECT: msgID=60336.1182, subject=com.nexy.assistant,
default	20:22:32.116868-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8eed50300 at /Applications/Nexy.app
default	20:22:32.147804-0500	Nexy	[0x9a3077980] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	20:22:32.147905-0500	Nexy	[0x9a3077980] activating connection: mach=false listener=false peer=false name=(anonymous)
default	20:22:32.147984-0500	Nexy	[0x9a3077ac0] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	20:22:32.149187-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=60336.1183, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=98220, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=60336, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	20:22:32.149230-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=60336, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=98220, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	20:22:32.151001-0500	tccd	AUTHREQ_SUBJECT: msgID=60336.1183, subject=com.nexy.assistant,
default	20:22:32.151834-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8eed50300 at /Applications/Nexy.app
default	20:22:32.181075-0500	Nexy	[0x9a3077ac0] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	20:22:32.181166-0500	Nexy	[0x9a3077ac0] activating connection: mach=false listener=false peer=false name=(anonymous)
default	20:22:32.193202-0500	Nexy	Did add XPC store
default	20:22:32.193279-0500	Nexy	Did add prepared store without migration (path: file:///Users/sergiyzasorin/Library/Application%20Support/AddressBook/Sources/4437DACA-BE14-412E-B504-7A2DD2E9DC7D/AddressBook-v22.abcddb)
default	20:22:32.193455-0500	Nexy	[0x9a3077d40] activating connection: mach=true listener=false peer=false name=com.apple.AddressBook.ContactsAccountsService
default	20:22:32.194262-0500	Nexy	[0x9a3077d40] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	20:22:32.194300-0500	Nexy	Will add prepared store without migration (path: file:///Users/sergiyzasorin/Library/Application%20Support/AddressBook/AddressBook-v22.abcddb)
default	20:22:32.194324-0500	Nexy	Will add XPC store with options: <private> <private>
default	20:22:32.198597-0500	Nexy	[0x9a309e800] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	20:22:32.200103-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=60336.1184, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=98220, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=60336, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	20:22:32.200150-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=60336, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=98220, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	20:22:32.202186-0500	tccd	AUTHREQ_SUBJECT: msgID=60336.1184, subject=com.nexy.assistant,
default	20:22:32.203097-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8eed50300 at /Applications/Nexy.app
default	20:22:32.234534-0500	Nexy	[0x9a309e800] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	20:22:32.234677-0500	Nexy	[0x9a309e800] activating connection: mach=false listener=false peer=false name=(anonymous)
default	20:22:32.234760-0500	Nexy	[0x9a309e940] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	20:22:32.236124-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=60336.1185, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=98220, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=60336, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	20:22:32.236159-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=60336, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=98220, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	20:22:32.238225-0500	tccd	AUTHREQ_SUBJECT: msgID=60336.1185, subject=com.nexy.assistant,
default	20:22:32.239470-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8eed50300 at /Applications/Nexy.app
default	20:22:32.269450-0500	Nexy	[0x9a309e940] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	20:22:32.269550-0500	Nexy	[0x9a309e940] activating connection: mach=false listener=false peer=false name=(anonymous)
default	20:22:32.269632-0500	Nexy	[0x9a309ea80] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	20:22:32.270737-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=60336.1186, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=98220, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=60336, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	20:22:32.270771-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=60336, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=98220, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	20:22:32.272525-0500	tccd	AUTHREQ_SUBJECT: msgID=60336.1186, subject=com.nexy.assistant,
default	20:22:32.273416-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8eed50300 at /Applications/Nexy.app
default	20:22:32.302242-0500	Nexy	[0x9a309ea80] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	20:22:32.302331-0500	Nexy	[0x9a309ea80] activating connection: mach=false listener=false peer=false name=(anonymous)
default	20:22:32.302412-0500	Nexy	[0x9a309ebc0] activating connection: mach=true listener=false peer=false name=com.apple.contactsd.persistence
default	20:22:32.303936-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=60336.1187, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=98220, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=60336, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	20:22:32.303982-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=60336, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=98220, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	20:22:32.305999-0500	tccd	AUTHREQ_SUBJECT: msgID=60336.1187, subject=com.nexy.assistant,
default	20:22:32.308044-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8eed50300 at /Applications/Nexy.app
default	20:22:32.336792-0500	Nexy	[0x9a309ebc0] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	20:22:32.336956-0500	Nexy	[0x9a309ebc0] activating connection: mach=false listener=false peer=false name=(anonymous)
default	20:22:32.338522-0500	Nexy	Did add XPC store
default	20:22:32.338558-0500	Nexy	Did add prepared store without migration (path: file:///Users/sergiyzasorin/Library/Application%20Support/AddressBook/AddressBook-v22.abcddb)
default	20:22:32.367597-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=60336.1188, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=98220, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=60336, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	20:22:32.367634-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=60336, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=98220, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	20:22:32.369818-0500	tccd	AUTHREQ_SUBJECT: msgID=60336.1188, subject=com.nexy.assistant,
default	20:22:32.371303-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8eed50300 at /Applications/Nexy.app
default	20:22:32.404932-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=60336.1189, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=98220, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.contactsd, pid=60336, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd}, },
default	20:22:32.404968-0500	tccd	requestor: TCCDProcess: identifier=com.apple.contactsd, pid=60336, auid=501, euid=501, binary_path=/System/Library/Frameworks/Contacts.framework/Support/contactsd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=98220, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	20:22:32.406672-0500	tccd	AUTHREQ_SUBJECT: msgID=60336.1189, subject=com.nexy.assistant,
default	20:22:32.407491-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8eed50300 at /Applications/Nexy.app
default	20:22:32.447874-0500	Nexy	"ACMonitoredAccountStore: Fetching accounts of account type com.apple.account.CardDAV..."
default	20:22:32.469579-0500	Nexy	"ACMonitoredAccountStore: Fetched Accounts"
default	20:22:32.469609-0500	Nexy	"ACMonitoredAccountStore: account was added: <private>"
error	20:22:32.469676-0500	Nexy	<private> 0x9a2c1af00: Update event received, but store registration failed. This event will be handled, but the behavior is undefined.
default	20:22:32.474971-0500	Nexy	Removing cached PSC for file:///Users/sergiyzasorin/Library/Application%20Support/AddressBook/ because accounts changed
default	20:22:32.475094-0500	Nexy	[0x9a3074640] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	20:22:32.475110-0500	Nexy	[0x9a3074500] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	20:22:32.475120-0500	Nexy	[0x9a30743c0] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	20:22:32.475128-0500	Nexy	[0x9a3074280] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	20:22:34.718261-0500	Nexy	[0x9a309ef80] activating connection: mach=true listener=false peer=false name=com.apple.system.opendirectoryd.api
default	20:22:41.981954-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=98282.1, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=98220, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.osascript, pid=98282, auid=501, euid=501, binary_path=/usr/bin/osascript}, },
default	20:22:41.983702-0500	tccd	AUTHREQ_SUBJECT: msgID=98282.1, subject=com.nexy.assistant,
default	20:22:41.984515-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b5167c00 at /Applications/Nexy.app
default	20:22:42.002305-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=391.3353, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=98220, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.osascript, pid=98282, auid=501, euid=501, binary_path=/usr/bin/osascript}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=391, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	20:22:42.003381-0500	tccd	AUTHREQ_SUBJECT: msgID=391.3353, subject=com.nexy.assistant,
default	20:22:42.004086-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b5167c00 at /Applications/Nexy.app
default	20:22:42.054387-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b5164f00 at /Applications/Nexy.app
default	20:22:42.085238-0500	Messages	TCCAccessRequestIndirect: TCCAccessRequestIndirect with pid 21394: target_identity: {
    kTCCCodeIdentityAuditToken = {length = 32, bytes = 0xf5010000 f5010000 14000000 f5010000 ... b7860100 9928a000 };
    kTCCCodeIdentityAuthority = kTCCCodeIdentityDesignatedRequirementAuthority;
    kTCCCodeIdentityCSFlags = 536941313;
    kTCCCodeIdentityCanSendToAnyTarget = 0;
    kTCCCodeIdentityDesignatedRequirementData = {length = 160, bytes = 0xfade0c00 000000a0 00000001 00000006 ... 4c32434c 42390000 };
    kTCCCodeIdentityExecutableURL = "file:///Applications/Nexy.app/Contents/MacOS/Nexy";
    kTCCCodeIdentityIdentifier = "com.nexy.assistant";
    kTCCCodeIdentityIdentifierType = 0;
    kTCCCodeIdentityPlatformType = 1;
    kTCCCodeIdentityPromptPolicy = 2;
    kTCCCodeIdentitySDKVersion = 983552;
    kTCCCodeIdentityTeamID = 5NKLL2CLB9;
}
default	20:22:42.106615-0500	tccd	target_executable_path_URL: file:///Applications/Nexy.app/Contents/MacOS/Nexy
default	20:22:42.116667-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8eed50900 at /Applications/Nexy.app
default	20:22:42.134607-0500	tccd	Prompting for access to indirect object Messages by Nexy
default	20:22:46.356770-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8eed50600 at /Applications/Nexy.app
default	20:22:46.363406-0500	tccd	Publishing <TCCDEvent: type=Create, service=kTCCServiceAppleEvents, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 3 subscribers: {
    39 = "<TCCDEventSubscriber: token=39, state=Passed, csid=com.apple.chronod>";
    38 = "<TCCDEventSubscriber: token=38, state=Initial, csid=(null)>";
    41 = "<TCCDEventSubscriber: token=41, state=Passed, csid=com.apple.photolibraryd>";
}
default	20:22:46.377986-0500	chronod	[appAuth:com.nexy.assistant] tcc authorization(s) changed
default	20:22:54.260198-0500	Nexy	"ACMonitoredAccountStore: Fetching accounts of account type com.apple.account.CardDAV..."
default	20:22:54.319355-0500	Nexy	"ACMonitoredAccountStore: Fetched Accounts"
default	20:22:56.962584-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=98302.1, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=98220, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.osascript, pid=98302, auid=501, euid=501, binary_path=/usr/bin/osascript}, },
default	20:22:56.964526-0500	tccd	AUTHREQ_SUBJECT: msgID=98302.1, subject=com.nexy.assistant,
default	20:22:56.965400-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b5165500 at /Applications/Nexy.app
default	20:22:56.986810-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=391.3377, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=98220, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.osascript, pid=98302, auid=501, euid=501, binary_path=/usr/bin/osascript}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=391, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	20:22:56.988185-0500	tccd	AUTHREQ_SUBJECT: msgID=391.3377, subject=com.nexy.assistant,
default	20:22:56.989233-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b5165500 at /Applications/Nexy.app
default	20:22:57.037575-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b5166400 at /Applications/Nexy.app
default	20:22:57.066584-0500	Messages	TCCAccessRequestIndirect: TCCAccessRequestIndirect with pid 21394: target_identity: {
    kTCCCodeIdentityAuditToken = {length = 32, bytes = 0xf5010000 f5010000 14000000 f5010000 ... b7860100 d428a000 };
    kTCCCodeIdentityAuthority = kTCCCodeIdentityDesignatedRequirementAuthority;
    kTCCCodeIdentityCSFlags = 536941313;
    kTCCCodeIdentityCanSendToAnyTarget = 0;
    kTCCCodeIdentityDesignatedRequirementData = {length = 160, bytes = 0xfade0c00 000000a0 00000001 00000006 ... 4c32434c 42390000 };
    kTCCCodeIdentityExecutableURL = "file:///Applications/Nexy.app/Contents/MacOS/Nexy";
    kTCCCodeIdentityIdentifier = "com.nexy.assistant";
    kTCCCodeIdentityIdentifierType = 0;
    kTCCCodeIdentityPlatformType = 1;
    kTCCCodeIdentityPromptPolicy = 2;
    kTCCCodeIdentitySDKVersion = 983552;
    kTCCCodeIdentityTeamID = 5NKLL2CLB9;
}
default	20:22:57.089803-0500	tccd	target_executable_path_URL: file:///Applications/Nexy.app/Contents/MacOS/Nexy
default	20:22:57.103439-0500	Nexy	[0x9a309f0c0] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	20:22:57.104123-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=98220.8, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=98220, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	20:22:57.105793-0500	tccd	AUTHREQ_SUBJECT: msgID=98220.8, subject=com.nexy.assistant,
default	20:22:57.106594-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b5165500 at /Applications/Nexy.app
default	20:22:57.121676-0500	tccd	Notifying for access  kTCCServiceListenEvent for target PID[98220], responsiblePID[98220], responsiblePath: /Applications/Nexy.app to UID: 501
default	20:22:57.122020-0500	Nexy	[0x9a309f0c0] invalidated after the last release of the connection object
default	20:22:57.165493-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b5166d00 at /Applications/Nexy.app
default	20:22:57.187706-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b5166400 at /Applications/Nexy.app
default	20:22:57.192171-0500	tccd	Publishing <TCCDEvent: type=Modify, service=kTCCServiceListenEvent, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 0 subscribers: {
}
error	20:22:57.848135-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceListenEvent com.nexy.assistant none
error	20:22:57.848316-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceListenEvent com.nexy.assistant none
error	20:22:57.848388-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceScreenCapture com.nexy.assistant full
error	20:22:57.848576-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceScreenCapture com.nexy.assistant full
error	20:22:57.897630-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAddressBook com.nexy.assistant full
error	20:22:57.897842-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAddressBook com.nexy.assistant full
error	20:22:57.898016-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAppleEvents com.nexy.assistant full
error	20:22:57.898257-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAppleEvents com.nexy.assistant full
error	20:22:57.899605-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceMicrophone com.nexy.assistant full
error	20:22:57.899609-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceMicrophone com.nexy.assistant full
default	20:23:03.057409-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b5166d00 at /Applications/Nexy.app
default	20:23:03.081003-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b5166400 at /Applications/Nexy.app
default	20:23:03.093791-0500	tccd	Publishing <TCCDEvent: type=Modify, service=kTCCServiceListenEvent, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 0 subscribers: {
}
error	20:23:03.254656-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceListenEvent com.nexy.assistant full
error	20:23:03.254910-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceScreenCapture com.nexy.assistant full
error	20:23:03.257110-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceListenEvent com.nexy.assistant full
error	20:23:03.257353-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceScreenCapture com.nexy.assistant full
error	20:23:03.301125-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAddressBook com.nexy.assistant full
error	20:23:03.301161-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAddressBook com.nexy.assistant full
error	20:23:03.301539-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAppleEvents com.nexy.assistant full
error	20:23:03.301556-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAppleEvents com.nexy.assistant full
error	20:23:03.302885-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceMicrophone com.nexy.assistant full
error	20:23:03.303325-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceMicrophone com.nexy.assistant full
default	20:23:12.132616-0500	Nexy	server port 0x000112cf, session port 0x0000320b
default	20:23:12.134722-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=391.3396, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=98220, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=391, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	20:23:12.134795-0500	tccd	requestor: TCCDProcess: identifier=com.apple.WindowServer, pid=391, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=98220, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	20:23:12.137146-0500	tccd	AUTHREQ_SUBJECT: msgID=391.3396, subject=com.nexy.assistant,
default	20:23:12.139554-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b5165500 at /Applications/Nexy.app
default	20:23:12.178719-0500	Nexy	[0x9a309f0c0] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	20:23:12.179336-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=98220.9, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=98220, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	20:23:12.180506-0500	tccd	AUTHREQ_SUBJECT: msgID=98220.9, subject=com.nexy.assistant,
default	20:23:12.181279-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b5165500 at /Applications/Nexy.app
default	20:23:12.196820-0500	tccd	Notifying for access  kTCCServicePostEvent for target PID[98220], responsiblePID[98220], responsiblePath: /Applications/Nexy.app to UID: 501
default	20:23:12.197177-0500	Nexy	[0x9a309f0c0] invalidated after the last release of the connection object
default	20:23:12.237035-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b5166d00 at /Applications/Nexy.app
default	20:23:12.257523-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b5166400 at /Applications/Nexy.app
default	20:23:12.262710-0500	tccd	Publishing <TCCDEvent: type=Modify, service=kTCCServicePostEvent, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 0 subscribers: {
}
error	20:23:12.316914-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceListenEvent com.nexy.assistant full
error	20:23:12.317120-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceScreenCapture com.nexy.assistant full
error	20:23:12.317301-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAccessibility com.nexy.assistant none
error	20:23:12.362308-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAddressBook com.nexy.assistant full
error	20:23:12.362792-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAppleEvents com.nexy.assistant full
error	20:23:12.363089-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAddressBook com.nexy.assistant full
error	20:23:12.363445-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAppleEvents com.nexy.assistant full
error	20:23:12.363993-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceMicrophone com.nexy.assistant full
error	20:23:12.364648-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceMicrophone com.nexy.assistant full
default	20:23:16.290417-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b5166d00 at /Applications/Nexy.app
default	20:23:16.312134-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b5166400 at /Applications/Nexy.app
default	20:23:16.340069-0500	tccd	Publishing <TCCDEvent: type=Modify, service=kTCCServiceAccessibility, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 0 subscribers: {
}
error	20:23:16.375749-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAccessibility com.nexy.assistant full
error	20:23:16.376465-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceListenEvent com.nexy.assistant full
error	20:23:16.376669-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceScreenCapture com.nexy.assistant full
error	20:23:16.376852-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAccessibility com.nexy.assistant full
error	20:23:16.398389-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAddressBook com.nexy.assistant full
error	20:23:16.398706-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAppleEvents com.nexy.assistant full
error	20:23:16.399743-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceMicrophone com.nexy.assistant full
error	20:23:16.423171-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAccessibility com.nexy.assistant full
error	20:23:16.423877-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceListenEvent com.nexy.assistant full
error	20:23:16.424074-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceScreenCapture com.nexy.assistant full
error	20:23:16.424256-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAccessibility com.nexy.assistant full
error	20:23:16.445332-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAddressBook com.nexy.assistant full
error	20:23:16.445637-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAppleEvents com.nexy.assistant full
error	20:23:16.446660-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceMicrophone com.nexy.assistant full
default	20:23:27.279190-0500	Nexy	[0x9a309f0c0] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
error	20:23:27.279932-0500	tccd	TCCDProcess: identifier=com.nexy.assistant, pid=98220, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy attempted to call TCCAccessRequest for kTCCServiceAccessibility without the recommended com.apple.private.tcc.manager.check-by-audit-token entitlement
default	20:23:27.280113-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=98220.10, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=98220, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.nexy.assistant, pid=98220, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	20:23:27.281603-0500	tccd	AUTHREQ_SUBJECT: msgID=98220.10, subject=com.nexy.assistant,
default	20:23:27.283400-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b5165500 at /Applications/Nexy.app
default	20:23:27.305125-0500	Nexy	[0x9a309f0c0] invalidated after the last release of the connection object
default	20:23:27.311506-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=93591.29, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=98220, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.sandboxd, pid=93591, auid=0, euid=0, binary_path=/usr/libexec/sandboxd}, },
default	20:23:27.328747-0500	tccd	AUTHREQ_SUBJECT: msgID=93591.29, subject=com.nexy.assistant,
default	20:23:27.330507-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b5166400 at /Applications/Nexy.app
default	20:23:27.357932-0500	tccd	Publishing <TCCDEvent: type=Create, service=kTCCServiceSystemPolicyAllFiles, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 0 subscribers: {
}
error	20:23:27.359399-0500	kernel	System Policy: Nexy(98220) deny(1) file-read-data /Users/sergiyzasorin/Library/Messages/chat.db
error	20:23:27.410655-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAccessibility com.nexy.assistant full
error	20:23:27.411504-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceSystemPolicyAllFiles com.nexy.assistant none
error	20:23:27.411977-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceListenEvent com.nexy.assistant full
error	20:23:27.412420-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceScreenCapture com.nexy.assistant full
error	20:23:27.413008-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAccessibility com.nexy.assistant full
error	20:23:27.413499-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAccessibility com.nexy.assistant full
error	20:23:27.413789-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceSystemPolicyAllFiles com.nexy.assistant none
error	20:23:27.414019-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceListenEvent com.nexy.assistant full
error	20:23:27.414364-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceScreenCapture com.nexy.assistant full
default	20:23:27.414669-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b5166400 at /Applications/Nexy.app
error	20:23:27.415033-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAccessibility com.nexy.assistant full
error	20:23:27.457429-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAddressBook com.nexy.assistant full
error	20:23:27.457837-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAppleEvents com.nexy.assistant full
error	20:23:27.458400-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAddressBook com.nexy.assistant full
error	20:23:27.458931-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAppleEvents com.nexy.assistant full
error	20:23:27.459094-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceMicrophone com.nexy.assistant full
error	20:23:27.460553-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceMicrophone com.nexy.assistant full
default	20:23:29.117810-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b5166d00 at /Applications/Nexy.app
default	20:23:29.159805-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b5166400 at /Applications/Nexy.app
default	20:23:29.170350-0500	tccd	Publishing <TCCDEvent: type=Modify, service=kTCCServiceSystemPolicyAllFiles, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 0 subscribers: {
}
error	20:23:29.336316-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAccessibility com.nexy.assistant full
error	20:23:29.336878-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceSystemPolicyAllFiles com.nexy.assistant full
error	20:23:29.337124-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceListenEvent com.nexy.assistant full
error	20:23:29.337580-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceScreenCapture com.nexy.assistant full
error	20:23:29.337836-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAccessibility com.nexy.assistant full
error	20:23:29.338223-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAccessibility com.nexy.assistant full
error	20:23:29.338732-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceSystemPolicyAllFiles com.nexy.assistant full
error	20:23:29.338967-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceListenEvent com.nexy.assistant full
error	20:23:29.339171-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceScreenCapture com.nexy.assistant full
error	20:23:29.339350-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAccessibility com.nexy.assistant full
error	20:23:29.380809-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAddressBook com.nexy.assistant full
error	20:23:29.380909-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAddressBook com.nexy.assistant full
error	20:23:29.381206-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAppleEvents com.nexy.assistant full
error	20:23:29.382306-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceMicrophone com.nexy.assistant full
error	20:23:29.382464-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAppleEvents com.nexy.assistant full
error	20:23:29.383719-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceMicrophone com.nexy.assistant full
default	20:23:39.263921-0500	Nexy	"The connection to ACDAccountStore was invalidated."
default	20:23:39.263875-0500	Nexy	[0x9a38cd540] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	20:23:42.451102-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=93591.30, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=98220, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.sandboxd, pid=93591, auid=0, euid=0, binary_path=/usr/libexec/sandboxd}, },
default	20:23:42.453600-0500	tccd	AUTHREQ_SUBJECT: msgID=93591.30, subject=com.nexy.assistant,
default	20:23:42.455286-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b5165500 at /Applications/Nexy.app
default	20:23:44.509562-0500	WindowServer	0[outside of RPC]: Process death: 0x0-0x746746 (Nexy) connectionID: 148363 pid: 98220 in session 0x101
default	20:23:44.509634-0500	WindowServer	<BSCompoundAssertion:0x830c11580> ([FocusManager:257]-deferringPolicyEvaluationSuppression) acquire for reason:process death - 0x0-0x746746 (Nexy) acq:0x8320991e0 count:1
default	20:23:44.511526-0500	audiomxd	  ServerSessionManager.mm:478   { "action":"destroy_session", "session":{"ID":"0x1f40ae","name":"Nexy(98220)"}, "details":null }
default	20:23:44.511584-0500	audiomxd	AudioApplicationInfoImpl.mm:690   Successfully removed session 0x1f40ae from AudioApp, recording state unchanged (app: {"name":"[implicit] Nexy","pid":98220})
default	20:23:44.511645-0500	audiomxd	  ServerSessionManager.mm:1086  destroy audio app instance since was created implicitly by session creation and all sessions now gone (audio app: {"name":"[implicit] Nexy","pid":98220})
default	20:23:44.514684-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 174, PID = 98220, Name = sid:0x1f40ae, Nexy(98220), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	20:23:44.515126-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 174, PID = 98220, Name = sid:0x1f40ae, Nexy(98220), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	20:23:44.516849-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:23:44.517000-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:23:44.517091-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:23:44.515995-0500	audiomxd	UpdateAudioState CID 0x91550001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:23:44.516721-0500	audiomxd	UpdateAudioState CID 0x91550001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:23:44.520390-0500	WindowServer	0[outside of RPC]: [FocusManager:257] update to deferring policy requested for reason: permitted list updated - 0x0-0x746746 removed - but we are suppressing evaluation for reasons: {(
    "process death - 0x0-0x746746 (Nexy)"
)}
default	20:23:44.520814-0500	WindowServer	0[outside of RPC]: [FocusManager:257] update to deferring policy requested for reason: permitted list updated - 0x1-0x17fac removed - but we are suppressing evaluation for reasons: {(
    "process death - 0x0-0x746746 (Nexy)"
)}
default	20:23:44.526268-0500	runningboardd	XPC connection invalidated: [app<application.com.nexy.assistant.55704030.55704039(501)>:98220]
default	20:23:44.528542-0500	coreaudiod	>>> NEGOTIATE [com.nexy.assistant]
default	20:23:44.528938-0500	coreaudiod	<<< NEGOTIATE [com.nexy.assistant]
default	20:23:44.535398-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:23:44.538791-0500	coreaudiod	IssueReporting.cpp:492   RTAID [ use_case=Generic report_type=RMS Generic Chain clientID=ADM node=ADM::com.nexy.assistant_7665.7540.0_airpods noise suppression studio::out-0 issue_detected_sample_time=3360.000000 ] -- [ rms:[-120.000000], peaks:[-240.000000] ]
default	20:23:44.538814-0500	coreaudiod	IssueReporting.cpp:492   RTAID [ use_case=Generic report_type=RMS Generic Chain clientID=ADM node=ADM::com.nexy.assistant_7665.7540.0_airpods noise suppression studio::in-0 issue_detected_sample_time=0.000000 ] -- [ rms:[-120.000000], peaks:[-240.000000] ]
default	20:23:44.547414-0500	mDNSResponder	[R152305] DNSServiceCreateConnection STOP PID[98220](Nexy)
default	20:23:44.549493-0500	runningboardd	[app<application.com.nexy.assistant.55704030.55704039(501)>:98220] termination reported by launchd (0, 0, 0)
default	20:23:44.549544-0500	runningboardd	Removing process: [app<application.com.nexy.assistant.55704030.55704039(501)>:98220]
default	20:23:44.549832-0500	runningboardd	Removing launch job for: [app<application.com.nexy.assistant.55704030.55704039(501)>:98220]
default	20:23:44.550122-0500	runningboardd	Removed job for [app<application.com.nexy.assistant.55704030.55704039(501)>:98220]
default	20:23:44.550160-0500	runningboardd	Removing assertions for terminated process: [app<application.com.nexy.assistant.55704030.55704039(501)>:98220]
default	20:23:44.556663-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.55704030.55704039(501)>: none (role: None) (endowments: (null))
default	20:23:44.556998-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.55704030.55704039(501)>: none (role: None) (endowments: (null))
default	20:23:44.557085-0500	audiomxd	  ServerSessionManager.mm:1327  Monitored process died, pid = 98220, name = Nexy
default	20:23:44.557976-0500	launchservicesd	Hit the server for a process handle 11f21e0100017fac that resolved to: [app<application.com.nexy.assistant.55704030.55704039(501)>:98220]
default	20:23:44.558073-0500	gamepolicyd	Received state update for 98220 (app<application.com.nexy.assistant.55704030.55704039(501)>, none-NotVisible
default	20:23:44.563163-0500	loginwindow	-[ApplicationManager handleCASEvent:withData:] | CAS notification for appDeath for com.nexy.assistant with asn: LSASN:{hi=0x0;lo=0x746746} for bundle path: /Applications/Nexy.app with URL: file:///Applications/Nexy.app/
default	20:23:44.563204-0500	loginwindow	-[Application setState:] | enter: <Application: 0xc0121b160: Nexy> state 3
default	20:23:44.563250-0500	loginwindow	-[PersistentAppsSupport applicationQuit:] | for app:Nexy, _appTrackingState = 2
default	20:23:44.571058-0500	loginwindow	-[Application setState:] | enter: <Application: 0xc0121b160: Nexy> state 4
default	20:23:44.571069-0500	loginwindow	-[PersistentAppsSupport applicationQuit:] | for app:Nexy, _appTrackingState = 2
default	20:23:47.661725-0500	logger	launching: /usr/bin/open -a /Applications/Nexy.app
default	20:23:47.767334-0500	lsd	com.nexy.assistant/Unknown Persona:5:5:1:1:Building bundle record for app
default	20:23:47.767524-0500	lsd	com.nexy.assistant/Unknown Persona:5:5:2:1:Built bundle record for app
default	20:23:47.769149-0500	lsd	com.nexy.assistant/Unknown Persona:5:4:2:1:_LSServerRegisterItemInfo result = 0
default	20:23:47.792841-0500	runningboardd	Launch request for app<application.com.nexy.assistant.55704030.55704039(501)>[0] is using uid 501 (divined from auid 501 euid 501)
default	20:23:47.792929-0500	runningboardd	Acquiring assertion targeting app<application.com.nexy.assistant.55704030.55704039(501)> from originator [osservice<com.apple.coreservices.uiagent(501)>:35920] with description <RBSAssertionDescriptor| "LS launch com.nexy.assistant" ID:400-35920-144228 target:app<application.com.nexy.assistant.55704030.55704039(501)> attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"LaunchRoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	20:23:47.793024-0500	runningboardd	Assertion 400-35920-144228 (target:app<application.com.nexy.assistant.55704030.55704039(501)>) will be created as active
default	20:23:47.795481-0500	dmd	Received xpc stream event (distributed notification matching) with name: com.apple.LaunchServices.applicationRegistered user info: {
    CFBundleDisplayName = Nexy;
    bundleIDs =     (
        "com.nexy.assistant"
    );
    isPlaceholder = 0;
}
default	20:23:47.797733-0500	runningboardd	Checking PreventLaunch: global:0 exPath:/Applications/Nexy.app/Contents/MacOS/Nexy predicates:(null) allow:(null)
default	20:23:47.797785-0500	runningboardd	Creating and launching job for: app<application.com.nexy.assistant.55704030.55704039(501)>
default	20:23:47.797802-0500	runningboardd	_mutateContextIfNeeded called for com.nexy.assistant
default	20:23:47.797914-0500	runningboardd	app<application.com.nexy.assistant.55704030.55704039(501)>: -[RBPersonaManager personaForIdentity:context:personaUID:personaUniqueString:] required 0.000954 ms (wallclock); resolved to {4294967295, (null)}
default	20:23:47.816107-0500	runningboardd	[app<application.com.nexy.assistant.55704030.55704039(501)>:98347] is not RunningBoard jetsam managed.
default	20:23:47.816150-0500	runningboardd	[app<application.com.nexy.assistant.55704030.55704039(501)>:98347] This process will not be managed.
default	20:23:47.816170-0500	runningboardd	Now tracking process: [app<application.com.nexy.assistant.55704030.55704039(501)>:98347]
default	20:23:47.816349-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.55704030.55704039(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:23:47.817248-0500	gamepolicyd	Hit the server for a process handle fe534190001802b that resolved to: [app<application.com.nexy.assistant.55704030.55704039(501)>:98347]
default	20:23:47.817300-0500	gamepolicyd	Received state update for 98347 (app<application.com.nexy.assistant.55704030.55704039(501)>, running-active-NotVisible
default	20:23:47.820930-0500	runningboardd	Using default underlying assertion for app: [app<application.com.nexy.assistant.55704030.55704039(501)>:98347]
default	20:23:47.821017-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.55704030.55704039(501)>:98347] from originator [app<application.com.nexy.assistant.55704030.55704039(501)>:98347] with description <RBSAssertionDescriptor| "RB Underlying Assertion" ID:400-400-144229 target:98347 attributes:[
	<RBSDomainAttribute| domain:"com.apple.underlying" name:"defaultUnderlyingAppAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	20:23:47.821219-0500	runningboardd	Assertion 400-400-144229 (target:[app<application.com.nexy.assistant.55704030.55704039(501)>:98347]) will be created as active
default	20:23:47.821495-0500	runningboardd	[app<application.com.nexy.assistant.55704030.55704039(501)>:98347] Ignoring jetsam update because this process is not memory-managed
default	20:23:47.821512-0500	runningboardd	[app<application.com.nexy.assistant.55704030.55704039(501)>:98347] Ignoring suspend because this process is not lifecycle managed
default	20:23:47.821536-0500	runningboardd	[app<application.com.nexy.assistant.55704030.55704039(501)>:98347] Set darwin role to: UserInteractive
default	20:23:47.821547-0500	runningboardd	[app<application.com.nexy.assistant.55704030.55704039(501)>:98347] Ignoring GPU update because this process is not GPU managed
default	20:23:47.821569-0500	runningboardd	[app<application.com.nexy.assistant.55704030.55704039(501)>:98347] Ignoring memory limit update because this process is not memory-managed
default	20:23:47.821773-0500	runningboardd	[app<application.com.nexy.assistant.55704030.55704039(501)>:98347] reported to RB as running
default	20:23:47.823812-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.55704030.55704039(501)>:98347] from originator [osservice<com.apple.coreservices.launchservicesd>:361] with description <RBSAssertionDescriptor| "uielement:98347" ID:400-361-144230 target:98347 attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"RoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	20:23:47.823930-0500	runningboardd	Assertion 400-361-144230 (target:[app<application.com.nexy.assistant.55704030.55704039(501)>:98347]) will be created as active
default	20:23:47.824111-0500	CoreServicesUIAgent	LAUNCH: 0x0-0x75f75f com.nexy.assistant starting stopped process.
default	20:23:47.825412-0500	runningboardd	[app<application.com.nexy.assistant.55704030.55704039(501)>:98347] Ignoring jetsam update because this process is not memory-managed
default	20:23:47.825460-0500	runningboardd	[app<application.com.nexy.assistant.55704030.55704039(501)>:98347] Ignoring suspend because this process is not lifecycle managed
default	20:23:47.825542-0500	runningboardd	[app<application.com.nexy.assistant.55704030.55704039(501)>:98347] Ignoring GPU update because this process is not GPU managed
default	20:23:47.825608-0500	runningboardd	[app<application.com.nexy.assistant.55704030.55704039(501)>:98347] Ignoring memory limit update because this process is not memory-managed
default	20:23:47.825670-0500	loginwindow	-[Application _updateInformationInternal] | Got App URL: file:///Applications/Nexy.app/
default	20:23:47.825723-0500	runningboardd	Successfully acquired underlying assertion for [app<application.com.nexy.assistant.55704030.55704039(501)>:98347]
default	20:23:47.825907-0500	loginwindow	-[Application setState:] | enter: <Application: 0xc0121b160: Nexy> state 2
default	20:23:47.825944-0500	loginwindow	-[ApplicationManager checkInAppContext:eventData:] | ApplicationManager: Checked in app : Nexy
default	20:23:47.827452-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.55704030.55704039(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:23:47.827807-0500	runningboardd	Invalidating assertion 400-35920-144228 (target:app<application.com.nexy.assistant.55704030.55704039(501)>) from originator [osservice<com.apple.coreservices.uiagent(501)>:35920]
default	20:23:47.827863-0500	runningboardd	[app<application.com.nexy.assistant.55704030.55704039(501)>:98347] Ignoring jetsam update because this process is not memory-managed
default	20:23:47.827881-0500	runningboardd	[app<application.com.nexy.assistant.55704030.55704039(501)>:98347] Ignoring suspend because this process is not lifecycle managed
default	20:23:47.827892-0500	runningboardd	[app<application.com.nexy.assistant.55704030.55704039(501)>:98347] Ignoring GPU update because this process is not GPU managed
default	20:23:47.827925-0500	runningboardd	[app<application.com.nexy.assistant.55704030.55704039(501)>:98347] Ignoring memory limit update because this process is not memory-managed
default	20:23:47.828282-0500	gamepolicyd	Received state update for 98347 (app<application.com.nexy.assistant.55704030.55704039(501)>, running-active-NotVisible
default	20:23:47.833597-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.55704030.55704039(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:23:47.852513-0500	logger	verifying new process for /Applications/Nexy.app/Contents/MacOS/Nexy
default	20:23:47.903861-0500	logger	detected new pid 98347 for /Applications/Nexy.app/Contents/MacOS/Nexy
default	20:23:47.920039-0500	Nexy	[0x10673ca40] activating connection: mach=true listener=false peer=false name=com.apple.cfprefsd.daemon
default	20:23:47.920113-0500	Nexy	[0x10673cf80] activating connection: mach=true listener=false peer=false name=com.apple.cfprefsd.agent
default	20:23:47.932424-0500	runningboardd	[app<application.com.nexy.assistant.55704030.55704039(501)>:98347] Ignoring jetsam update because this process is not memory-managed
default	20:23:47.932435-0500	runningboardd	[app<application.com.nexy.assistant.55704030.55704039(501)>:98347] Ignoring suspend because this process is not lifecycle managed
default	20:23:47.932447-0500	runningboardd	[app<application.com.nexy.assistant.55704030.55704039(501)>:98347] Ignoring GPU update because this process is not GPU managed
default	20:23:47.932593-0500	gamepolicyd	Received state update for 98347 (app<application.com.nexy.assistant.55704030.55704039(501)>, running-active-NotVisible
default	20:23:47.932466-0500	runningboardd	[app<application.com.nexy.assistant.55704030.55704039(501)>:98347] Ignoring memory limit update because this process is not memory-managed
default	20:23:47.935976-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.55704030.55704039(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:23:47.936516-0500	gamepolicyd	Received state update for 98347 (app<application.com.nexy.assistant.55704030.55704039(501)>, running-active-NotVisible
error	20:23:48.045702-0500	Nexy	dlsym cannot find symbol NSMakeRect in CFBundle 0x10672c300 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	20:23:48.045942-0500	Nexy	dlsym cannot find symbol NSMakePoint in CFBundle 0x10672c300 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	20:23:48.046140-0500	Nexy	dlsym cannot find symbol NSMakeSize in CFBundle 0x10672c300 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	20:23:48.046340-0500	Nexy	dlsym cannot find symbol NSMakeRange in CFBundle 0x10672c300 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
default	20:23:48.048059-0500	Nexy	[0x106745bc0] activating connection: mach=true listener=false peer=false name=com.apple.coreservices.launchservicesd
default	20:23:48.048983-0500	Nexy	[0xc7d7f8000] activating connection: mach=true listener=false peer=false name=com.apple.analyticsd
default	20:23:48.049381-0500	Nexy	[0xc7d7f8140] activating connection: mach=true listener=false peer=false name=com.apple.pasteboard.1
default	20:23:48.049874-0500	Nexy	[0xc7d7f8280] activating connection: mach=true listener=false peer=false name=com.apple.distributed_notifications@Uv3
default	20:23:48.052071-0500	Nexy	void _NSDisableAutomaticTerminationAndLog(NSString *) No windows open yet
default	20:23:48.052654-0500	Nexy	[0xc7d7f83c0] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	20:23:48.053498-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=98347.1, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=98347, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	20:23:48.055970-0500	tccd	AUTHREQ_SUBJECT: msgID=98347.1, subject=com.nexy.assistant,
default	20:23:48.057343-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b5165500 at /Applications/Nexy.app
default	20:23:48.083237-0500	Nexy	[0xc7d7f83c0] invalidated after the last release of the connection object
default	20:23:48.083548-0500	Nexy	server port 0x0000350f, session port 0x0000350f
default	20:23:48.084609-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=391.3419, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=98347, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=391, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	20:23:48.084636-0500	tccd	requestor: TCCDProcess: identifier=com.apple.WindowServer, pid=391, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=98347, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	20:23:48.085829-0500	tccd	AUTHREQ_SUBJECT: msgID=391.3419, subject=com.nexy.assistant,
default	20:23:48.086739-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b5165500 at /Applications/Nexy.app
default	20:23:48.130764-0500	Nexy	FRONTLOGGING: version 1
default	20:23:48.130769-0500	Nexy	Registered, pid=98347 ASN=0x0,0x75f75f
default	20:23:48.131236-0500	WindowServer	1315f3[CreateApplication]: Process creation: 0x0-0x75f75f (Nexy) connectionID: 1315F3 pid: 98347 in session 0x101
default	20:23:48.130547-0500	loginwindow	-[Application _updateInformationInternal] | Got App URL: file:///Applications/Nexy.app/
default	20:23:48.130650-0500	loginwindow	-[ApplicationManager checkInAppContext:eventData:] | ApplicationManager: Checked in app : Nexy
default	20:23:48.131725-0500	Nexy	[0xc7d7f8500] activating connection: mach=true listener=false peer=false name=com.apple.lsd.mapdb
default	20:23:48.134665-0500	Nexy	BringForward: pid=98347 asn=0x0-0x75f75f bringForward=0 foreground=0 uiElement=1 launchedByLS=1 modifiersCount=1 allDisabled=0
default	20:23:48.135031-0500	Nexy	BringFrontModifier: pid=98347 asn=0x0-0x75f75f Modifier 0 hideAfter=0 hideOthers=0 dontMakeFrontmost=0 mouseDown=0/0 seed=0/0
default	20:23:48.135763-0500	Nexy	Current system appearance, (HLTB: 2), (SLS: 1)
default	20:23:48.139238-0500	Nexy	No persisted cache on this platform.
default	20:23:48.143980-0500	Nexy	Post-registration system appearance: (HLTB: 2)
default	20:23:48.148057-0500	runningboardd	Setting client for [app<application.com.nexy.assistant.55704030.55704039(501)>:98347] as ready
default	20:23:48.148756-0500	Nexy	Handshake succeeded
default	20:23:48.148776-0500	Nexy	Identity resolved as app<application.com.nexy.assistant.55704030.55704039(501)>
default	20:23:48.149311-0500	Nexy	[0xc7d7f83c0] Connection returned listener port: 0x4703
default	20:23:48.155174-0500	Nexy	[0xc7d7f83c0] Connection returned listener port: 0x4703
default	20:23:48.161664-0500	Nexy	[0xc7d7f8a00] Connection returned listener port: 0x6503
default	20:23:49.110409-0500	kernel	SK[6]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid F078DE3E-5026-4CC8-8D07-316D304EA04E flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.61557,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0x927f868b tp_proto=0x06"
default	20:23:49.110527-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:61557<-><IPv4-redacted>:53] interface: en0 (skipped: 196)
so_gencnt: 8779663 t_state: SYN_SENT process: Nexy:98347 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xb3b5131e
default	20:23:53.192723-0500	runningboardd	Assertion did invalidate due to timeout: 400-400-144229 (target:[app<application.com.nexy.assistant.55704030.55704039(501)>:98347])
default	20:23:53.388195-0500	runningboardd	[app<application.com.nexy.assistant.55704030.55704039(501)>:98347] Ignoring jetsam update because this process is not memory-managed
default	20:23:53.388206-0500	runningboardd	[app<application.com.nexy.assistant.55704030.55704039(501)>:98347] Ignoring suspend because this process is not lifecycle managed
default	20:23:53.388216-0500	runningboardd	[app<application.com.nexy.assistant.55704030.55704039(501)>:98347] Ignoring GPU update because this process is not GPU managed
default	20:23:53.388230-0500	runningboardd	[app<application.com.nexy.assistant.55704030.55704039(501)>:98347] Ignoring memory limit update because this process is not memory-managed
default	20:23:53.390718-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.55704030.55704039(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:23:53.391249-0500	gamepolicyd	Received state update for 98347 (app<application.com.nexy.assistant.55704030.55704039(501)>, running-active-NotVisible
default	20:23:54.110966-0500	kernel	tcp_connection_summary (tcp_close:1797)[<IPv4-redacted>:61557<-><IPv4-redacted>:53] interface: en0 (skipped: 196)
so_gencnt: 8779663 t_state: SYN_SENT process: Nexy:98347 Duration: 5.001 sec Conn_Time: 0.000 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 0.000 ms rttvar: 250.000 ms base rtt: 0 ms so_error: 0 svc/tc: 0 flow: 0xb3b5131e
default	20:23:54.110991-0500	kernel	tcp_connection_summary [<IPv4-redacted>:61557<-><IPv4-redacted>:53] interface: en0 (skipped: 196)
so_gencnt: 8779663 t_state: SYN_SENT process: Nexy:98347 flowctl: 0us (0x) SYN in/out: 0/5 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	20:23:54.111562-0500	kernel	SK[4]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 03F8FC17-E6B5-4399-9664-65A956E7CB97 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.61562,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0xd7d146d1 tp_proto=0x06"
default	20:23:54.111711-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:61562<-><IPv4-redacted>:53] interface: en0 (skipped: 196)
so_gencnt: 8779711 t_state: SYN_SENT process: Nexy:98347 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xbd98652e
default	20:23:58.462932-0500	Nexy	NotifyToken::RegisterDispatch(user.uid.501.com.apple.LaunchServices.database) fired for session key <private>
default	20:23:59.112435-0500	kernel	tcp_connection_summary (tcp_close:1797)[<IPv4-redacted>:61562<-><IPv4-redacted>:53] interface: en0 (skipped: 196)
so_gencnt: 8779711 t_state: SYN_SENT process: Nexy:98347 Duration: 5.001 sec Conn_Time: 0.000 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 0.000 ms rttvar: 250.000 ms base rtt: 0 ms so_error: 0 svc/tc: 0 flow: 0xbd98652e
default	20:23:59.112459-0500	kernel	tcp_connection_summary [<IPv4-redacted>:61562<-><IPv4-redacted>:53] interface: en0 (skipped: 196)
so_gencnt: 8779711 t_state: SYN_SENT process: Nexy:98347 flowctl: 0us (0x) SYN in/out: 0/5 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	20:23:59.117490-0500	Nexy	networkd_settings_read_from_file initialized networkd settings by reading plist directly
default	20:23:59.117702-0500	Nexy	networkd_settings_read_from_file initialized networkd settings by reading plist directly
default	20:23:59.119354-0500	Nexy	nw_path_libinfo_path_check [3AAC289F-3A52-4056-A856-366023D4B839 Hostname#7a69cc0f:53 tcp, legacy-socket, attribution: developer]
	libinfo check path: <private>
default	20:23:59.119884-0500	mDNSResponder	[R152461] DNSServiceCreateConnection START PID[98347](Nexy)
default	20:23:59.120028-0500	mDNSResponder	[R152462] DNSServiceQueryRecord START -- qname: <mask.hash: 'EZsJcryDavQKD3Th4XvA1g=='>, qtype: A, flags: 0x1D000, interface index: 0, client pid: 98347 (Nexy), name hash: f92d5498
default	20:23:59.121094-0500	mDNSResponder	[R152463] DNSServiceQueryRecord START -- qname: <mask.hash: 'EZsJcryDavQKD3Th4XvA1g=='>, qtype: AAAA, flags: 0x1D000, interface index: 0, client pid: 98347 (Nexy), name hash: f92d5498
default	20:23:59.147072-0500	Nexy	LSExceptions shared instance invalidated for timeout.
default	20:23:59.172919-0500	kernel	SK[1]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 2618B5A5-AC74-4B1D-A18D-E75AD45672A1 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.61563,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0x5bc22e2a tp_proto=0x06"
default	20:23:59.173049-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:61563<-><IPv4-redacted>:53] interface: en0 (skipped: 196)
so_gencnt: 8779726 t_state: SYN_SENT process: Nexy:98347 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x819ae328
default	20:24:04.113878-0500	kernel	tcp_connection_summary (tcp_close:1797)[<IPv4-redacted>:61563<-><IPv4-redacted>:53] interface: en0 (skipped: 196)
so_gencnt: 8779726 t_state: SYN_SENT process: Nexy:98347 Duration: 4.941 sec Conn_Time: 0.000 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 0.000 ms rttvar: 250.000 ms base rtt: 0 ms so_error: 0 svc/tc: 0 flow: 0x819ae328
default	20:24:04.113898-0500	kernel	tcp_connection_summary [<IPv4-redacted>:61563<-><IPv4-redacted>:53] interface: en0 (skipped: 196)
so_gencnt: 8779726 t_state: SYN_SENT process: Nexy:98347 flowctl: 0us (0x) SYN in/out: 0/5 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	20:24:05.210069-0500	Nexy	[0xc7d7f8dc0] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	20:24:05.211127-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=98347.2, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=98347, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	20:24:05.212610-0500	tccd	AUTHREQ_SUBJECT: msgID=98347.2, subject=com.nexy.assistant,
default	20:24:05.213598-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b5165500 at /Applications/Nexy.app
default	20:24:05.239465-0500	Nexy	[0xc7d7f8dc0] invalidated after the last release of the connection object
default	20:24:05.241199-0500	Nexy	server port 0x00004b17, session port 0x0000350f
default	20:24:05.242094-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=391.3422, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=98347, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=391, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	20:24:05.242125-0500	tccd	requestor: TCCDProcess: identifier=com.apple.WindowServer, pid=391, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=98347, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	20:24:05.243092-0500	tccd	AUTHREQ_SUBJECT: msgID=391.3422, subject=com.nexy.assistant,
default	20:24:05.243743-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b5165500 at /Applications/Nexy.app
default	20:24:05.274444-0500	Nexy	  AVAudioSession_MacOS.mm:1021  initForMacOS
default	20:24:05.275073-0500	Nexy	[0xc7d7f8f00] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioSession
default	20:24:05.276032-0500	audiomxd	  ServerSessionManager.mm:315   { "action":"create_session", "session":{"ID":"0x1f40af","name":"Nexy(98347)"}, "details":{"PID":98347,"session_type":"Primary"} }
default	20:24:05.276124-0500	audiomxd	AudioApplicationInfoImpl.mm:250   Setting initial isRecording state: 0 for newly-created AudioApp
	app: {"name":"[implicit] Nexy","pid":98347}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1f40af, sessionType: 'prim', isRecording: false }, 
]
default	20:24:05.276913-0500	audiomxd	  ServerSessionManager.mm:1322  Start process monitoring, pid = 98347, name = Nexy
default	20:24:05.277234-0500	Nexy	    SessionCore_Create.mm:99    Created session 0xc7d8b8640 with ID: 0x1f40af
default	20:24:05.277491-0500	Nexy	Registered notify signal com.apple.caulk.alloc.rtdump (0)
default	20:24:05.278290-0500	Nexy	System_Input_Processing_Notification_Handler.mm:456   System_Input_Processing_Notification_Handler::is_vi_available(): Voice isolation DSP is available for client with bundle id com.nexy.assistant (AVFoundation is available, application is not in client deny list, application is not FaceTime variant)
default	20:24:05.279584-0500	Nexy	[0xc7d7f9040] activating connection: mach=true listener=false peer=false name=com.apple.cmio.registerassistantservice.system-extensions
fault	20:24:05.281872-0500	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.55704030.55704039 AUID=501> and <type=Application identifier=application.com.nexy.assistant.55704030.55704039>
default	20:24:05.286824-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOInitializeListenersForBundleID: for <private> -> <private>
default	20:24:05.288408-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> vpio_preferenceChangedListener: new value ((null)) for key AUVoiceIOClients/com-nexy-assistant/AUVoiceIOChatFlavor, translatedBundleID com.nexy.assistant, bundleIDs {(
    "com.nexy.assistant"
)}
default	20:24:05.288546-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> vpio_preferenceChangedListener: new value ((null)) for key AUVoiceIOClients/com-nexy-assistant/AUVoiceIOIsAutoChatFlavorEnabled, translatedBundleID com.nexy.assistant, bundleIDs {(
    "com.nexy.assistant"
)}
default	20:24:05.288710-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetSupportedChatFlavorsForBundleID: <private>-><private> get supported chat flavors: <private>
default	20:24:05.288721-0500	Nexy	            HALSystem.cpp:134    Enabling HAL Voice Isolation support
default	20:24:05.288752-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetHiddenChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	20:24:05.288872-0500	Nexy	[0xc7d7f9180] activating connection: mach=true listener=false peer=false name=com.apple.tccd
default	20:24:05.289366-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=98347.3, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=98347, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	20:24:05.289417-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOHiddenChatFlavors newValue: (
    1
)
default	20:24:05.296741-0500	tccd	AUTHREQ_SUBJECT: msgID=98347.3, subject=com.nexy.assistant,
default	20:24:05.297971-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8eed50300 at /Applications/Nexy.app
default	20:24:05.315635-0500	Nexy	[0xc7d7f9180] invalidated after the last release of the connection object
default	20:24:05.315788-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetPreferredChatFlavorForBundleID: <private>-><private> get value: 0
default	20:24:05.315831-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetSupportedChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	20:24:05.316108-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOSupportedChatFlavors newValue: (
    0,
    2
)
default	20:24:05.317410-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.3400, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=98347, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=392, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	20:24:05.318454-0500	tccd	AUTHREQ_SUBJECT: msgID=401.3400, subject=com.nexy.assistant,
default	20:24:05.319055-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8eed50300 at /Applications/Nexy.app
default	20:24:05.339298-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.3402, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=98347, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=392, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	20:24:05.357748-0500	Nexy	  HALPlugInManagement.cpp:440    HALPlugInManagement::RegisterPlugIns: skipping in-process plug-ins
error	20:24:05.357768-0500	Nexy	AddInstanceForFactory: No factory registered for id <CFUUID 0xc7f3a2960> F8BB1C28-BAE8-11D6-9C31-00039315CD46
error	20:24:05.378768-0500	Nexy	         HALC_ProxyObjectMap.cpp:174   HALC_ProxyObjectMap::_CopyObjectByObjectID: failed to create the local object
error	20:24:05.378781-0500	Nexy	            HALC_ShellDevice.cpp:2673  HALC_ShellDevice::RebuildControlList: couldn't find the control object
default	20:24:05.381597-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	20:24:05.381736-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	20:24:05.386234-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetPreferredChatFlavorForBundleID: <private>-><private> get value: 0
default	20:24:05.387813-0500	Nexy	       AggregateDevice.mm:914   fetched default input device, ID = 91
default	20:24:05.400099-0500	tccd	AUTHREQ_SUBJECT: msgID=98360.1, subject=com.nexy.assistant,
default	20:24:05.411731-0500	Nexy	       AggregateDevice.mm:688   Built valid aggregate 126
default	20:24:05.454488-0500	Nexy	                AUHAL.cpp:420   AUHAL: (0xc7e9ea340) Selecting device 85 from constructor
default	20:24:05.454498-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0xc7e9ea340)
default	20:24:05.454503-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0xc7e9ea340) not already running
default	20:24:05.454509-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0xc7e9ea340) nothing to teardown
default	20:24:05.454513-0500	Nexy	                AUHAL.cpp:762   SelectDevice: (0xc7e9ea340) connecting device 85
default	20:24:05.454602-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0xc7e9ea340) Device ID: 85 (Input:No | Output:Yes): true
default	20:24:05.454689-0500	Nexy	                AUHAL.cpp:774   SelectDevice: (0xc7e9ea340) created ioproc 0xa for device 85
default	20:24:05.454802-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0xc7e9ea340) adding 7 device listeners to device 85
default	20:24:05.454958-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0xc7e9ea340) adding 0 device delegate listeners to device 85
default	20:24:05.454969-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0xc7e9ea340)
default	20:24:05.455032-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  48000 Hz, Float32, interleaved
default	20:24:05.455039-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	20:24:05.455044-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	20:24:05.455050-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	20:24:05.455058-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	20:24:05.455142-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0xc7e9ea340) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	20:24:05.455151-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0xc7e9ea340) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	20:24:05.455157-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	20:24:05.455161-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0xc7e9ea340) removing 0 device listeners from device 0
default	20:24:05.455164-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0xc7e9ea340) removing 0 device delegate listeners from device 0
default	20:24:05.455168-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0xc7e9ea340)
default	20:24:05.455219-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is DISABLED
default	20:24:05.455514-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	20:24:05.457360-0500	Nexy	       ACv2Workarounds.mm:51    com.nexy.assistant: fix84702776_86723525_86479548_89800354_SinglePacketDesc: false
default	20:24:05.457406-0500	Nexy	Registered notify signal com.apple.caulk.alloc.audiodump (0)
default	20:24:05.457536-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0xc7ade2ee0, from  2 ch,  44100 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	20:24:05.457556-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	20:24:05.458746-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	20:24:05.458991-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	20:24:05.460772-0500	kernel	udp connect: [<IPv4-redacted>:0<-><IPv4-redacted>:0] interface:  (skipped: 209)
so_gencnt: 8779755 so_state: 0x0000 process: Nexy:98347 bytes in/out: 0/0 pkts in/out: 0/0 error: 49 so_error: 0 svc/tc: 0 flow: 0x0
default	20:24:05.460786-0500	kernel	udp_connection_summary [<IPv4-redacted>:0<-><IPv4-redacted>:0] interface:  (skipped: 209)
so_gencnt: 8779755 so_state: 0x0000 process: Nexy:98347 Duration: 0.000 sec Conn_Time: 0.000 sec bytes in/out: 0/0 pkts in/out: 0/0 rxnospace pkts/bytes: 0/0 so_error: 0 svc/tc: 0 flow: 0x0 flowctl: 0us (0x)
default	20:24:05.464857-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	20:24:05.464870-0500	kernel	udp connect: [<IPv4-redacted>:64942<-><IPv4-redacted>:443] interface:  (skipped: 209)
so_gencnt: 8779756 so_state: 0x0002 process: Nexy:98347 bytes in/out: 0/0 pkts in/out: 0/0 error: 0 so_error: 0 svc/tc: 0 flow: 0xa6bda34c
default	20:24:05.464890-0500	kernel	udp_connection_summary [<IPv4-redacted>:64942<-><IPv4-redacted>:443] interface:  (skipped: 209)
so_gencnt: 8779756 so_state: 0x0002 process: Nexy:98347 Duration: 0.000 sec Conn_Time: 0.000 sec bytes in/out: 0/0 pkts in/out: 0/0 rxnospace pkts/bytes: 0/0 so_error: 0 svc/tc: 0 flow: 0xa6bda34c flowctl: 0us (0x)
default	20:24:05.465092-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	20:24:05.465164-0500	kernel	udp_connection_summary [<IPv4-redacted>:53183<-><IPv4-redacted>:53] interface: en0 (skipped: 209)
so_gencnt: 8779754 so_state: 0x0132 process: Nexy:98347 Duration: 0.024 sec Conn_Time: 0.024 sec bytes in/out: 353/192 pkts in/out: 3/3 rxnospace pkts/bytes: 0/0 so_error: 0 svc/tc: 0 flow: 0xaac05bfd flowctl: 0us (0x)
default	20:24:05.467116-0500	kernel	SK[6]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 9A812DEB-4DB0-4DCD-864B-9E6234E47B47 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.61566,dst=<IPv4-redacted>.443,proto=0x06 mask=0x0000003f,hash=0x3e2b65da tp_proto=0x06"
default	20:24:05.467175-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:61566<-><IPv4-redacted>:443] interface: en0 (skipped: 196)
so_gencnt: 8779757 t_state: SYN_SENT process: Nexy:98347 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xaeac872f
default	20:24:05.467386-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0xc7ade30c0, from  2 ch,  44100 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	20:24:05.467401-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	20:24:05.467766-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	20:24:05.468461-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0xc7ade30f0, from  2 ch,  48000 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	20:24:05.468472-0500	Nexy	       AudioConverter.cpp:1317  AudioConverter -> 0xc7ade30f0: The in-process GetProperty call returned 1886547824 for property 1886546285 with size 8.
default	20:24:05.468477-0500	Nexy	AudioConverter -> 0xc7ade30f0: The in-process SetProperty call returned 1886547824 for property 1936876385 with size 4.
default	20:24:05.468477-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	20:24:05.468488-0500	Nexy	AudioConverter -> 0xc7ade30f0: The in-process SetProperty call returned 1886547824 for property 1936876401 with size 4.
default	20:24:05.468493-0500	Nexy	AudioConverter -> 0xc7ade30f0: The in-process SetProperty call returned 1886547824 for property 1886547309 with size 4.
default	20:24:05.469244-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0xc7ade2ac0, from  2 ch,  48000 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	20:24:05.469253-0500	Nexy	       AudioConverter.cpp:1317  AudioConverter -> 0xc7ade2ac0: The in-process GetProperty call returned 1886547824 for property 1886546285 with size 8.
default	20:24:05.469259-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	20:24:05.469259-0500	Nexy	AudioConverter -> 0xc7ade2ac0: The in-process SetProperty call returned 1886547824 for property 1936876385 with size 4.
default	20:24:05.469280-0500	Nexy	AudioConverter -> 0xc7ade2ac0: The in-process SetProperty call returned 1886547824 for property 1936876401 with size 4.
default	20:24:05.469285-0500	Nexy	AudioConverter -> 0xc7ade2ac0: The in-process SetProperty call returned 1886547824 for property 1886547309 with size 4.
default	20:24:05.469438-0500	Nexy	       AudioConverter.cpp:1317  AudioConverter -> 0xc7ade2ac0: The in-process GetProperty call returned 1886547824 for property 1886546285 with size 8.
default	20:24:05.470976-0500	kernel	SK[6]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid ECA2E5E3-D2DC-4F12-857C-7CD73E860FE1 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.61567,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0x7f96a694 tp_proto=0x06"
default	20:24:05.471012-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:61567<-><IPv4-redacted>:53] interface: en0 (skipped: 196)
so_gencnt: 8779758 t_state: SYN_SENT process: Nexy:98347 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xa78e35d3
default	20:24:05.472141-0500	Nexy	nw_path_libinfo_path_check [9C231B3A-5CCE-4917-A6A0-EC440FEA9476 Hostname#a4d533db:443 tcp, legacy-socket, attribution: developer]
	libinfo check path: <private>
default	20:24:05.472254-0500	mDNSResponder	[R152464] DNSServiceQueryRecord START -- qname: <mask.hash: 'O8Fw0oYtazaEgJCdnx5gaw=='>, qtype: A, flags: 0x1D000, interface index: 0, client pid: 98347 (Nexy), name hash: 2d50b096
default	20:24:05.481362-0500	kernel	tcp connected: [<IPv4-redacted>:61566<-><IPv4-redacted>:443] interface: en0 (skipped: 196)
so_gencnt: 8779757 t_state: ESTABLISHED process: Nexy:98347 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xaeac872f
default	20:24:05.487804-0500	kernel	SK[7]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 03F2D079-FC6A-409E-AD48-57648C4A8F1E flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.61568,dst=<IPv4-redacted>.443,proto=0x06 mask=0x0000003f,hash=0xe9a9615e tp_proto=0x06"
default	20:24:05.487850-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:61568<-><IPv4-redacted>:443] interface: en0 (skipped: 196)
so_gencnt: 8779768 t_state: SYN_SENT process: Nexy:98347 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 14 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x9672f901
default	20:24:05.500020-0500	kernel	tcp connected: [<IPv4-redacted>:61568<-><IPv4-redacted>:443] interface: en0 (skipped: 196)
so_gencnt: 8779768 t_state: ESTABLISHED process: Nexy:98347 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 14 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x9672f901
default	20:24:05.635955-0500	System Events	TCCAccessRequestIndirect: TCCAccessRequestIndirect with pid 98361: target_identity: {
    kTCCCodeIdentityAuditToken = {length = 32, bytes = 0xf5010000 f5010000 14000000 f5010000 ... b7860100 4f29a000 };
    kTCCCodeIdentityAuthority = kTCCCodeIdentityDesignatedRequirementAuthority;
    kTCCCodeIdentityCSFlags = 536941313;
    kTCCCodeIdentityCanSendToAnyTarget = 0;
    kTCCCodeIdentityDesignatedRequirementData = {length = 160, bytes = 0xfade0c00 000000a0 00000001 00000006 ... 4c32434c 42390000 };
    kTCCCodeIdentityExecutableURL = "file:///Applications/Nexy.app/Contents/MacOS/Nexy";
    kTCCCodeIdentityIdentifier = "com.nexy.assistant";
    kTCCCodeIdentityIdentifierType = 0;
    kTCCCodeIdentityPlatformType = 1;
    kTCCCodeIdentityPromptPolicy = 2;
    kTCCCodeIdentitySDKVersion = 983552;
    kTCCCodeIdentityTeamID = 5NKLL2CLB9;
}
default	20:24:05.649313-0500	tccd	target_executable_path_URL: file:///Applications/Nexy.app/Contents/MacOS/Nexy
default	20:24:05.661202-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8eed50900 at /Applications/Nexy.app
default	20:24:05.681900-0500	tccd	Prompting for access to indirect object System Events by Nexy
default	20:24:06.005655-0500	Nexy	[0xc7d7f9680] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	20:24:06.006392-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=98347.4, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=98347, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	20:24:06.018141-0500	tccd	AUTHREQ_SUBJECT: msgID=98347.4, subject=com.nexy.assistant,
default	20:24:06.019432-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b5165500 at /Applications/Nexy.app
default	20:24:06.055341-0500	Nexy	[0xc7d7f9680] invalidated after the last release of the connection object
default	20:24:06.059077-0500	Nexy	[0xc7d7f97c0] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	20:24:06.060591-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=98347.5, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=98347, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	20:24:06.062923-0500	tccd	AUTHREQ_SUBJECT: msgID=98347.5, subject=com.nexy.assistant,
default	20:24:06.064212-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b5166d00 at /Applications/Nexy.app
default	20:24:06.154951-0500	Nexy	[0xc7d7f97c0] invalidated after the last release of the connection object
default	20:24:06.155081-0500	Nexy	 [INFO] SLSHWCaptureDesktopProxying:485 request: <private>
default	20:24:06.157309-0500	Nexy	[0xc7d7f97c0] activating connection: mach=true listener=false peer=false name=com.apple.replayd
default	20:24:06.171717-0500	Nexy	 [INFO] -[RPDaemonProxy consumeSandboxExtension:processNewConnection:]:568
default	20:24:06.171892-0500	Nexy	 [INFO] -[RPDaemonProxy proxyCoreGraphicsWithMethodType:config:machPort:completionHandler:]:1493
default	20:24:06.181826-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=82607.4, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=98347, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.replayd, pid=82607, auid=501, euid=501, binary_path=/usr/libexec/replayd}, },
default	20:24:06.182015-0500	tccd	requestor: TCCDProcess: identifier=com.apple.replayd, pid=82607, auid=501, euid=501, binary_path=/usr/libexec/replayd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=98347, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	20:24:06.191010-0500	tccd	AUTHREQ_SUBJECT: msgID=82607.4, subject=com.nexy.assistant,
default	20:24:06.193677-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b5166d00 at /Applications/Nexy.app
default	20:24:06.262993-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=391.3428, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=98347, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=391, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	20:24:06.263027-0500	tccd	requestor: TCCDProcess: identifier=com.apple.WindowServer, pid=391, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=98347, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	20:24:06.264606-0500	tccd	AUTHREQ_SUBJECT: msgID=391.3428, subject=com.nexy.assistant,
default	20:24:06.265693-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b5166d00 at /Applications/Nexy.app
default	20:24:06.334237-0500	Nexy	 [INFO] SLSHWCaptureDesktopProxying_block_invoke:506 request: <private>, error: (null), windowInfo: (null)
fault	20:24:06.377090-0500	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.55704030.55704039 AUID=501> and <type=Application identifier=application.com.nexy.assistant.55704030.55704039>
fault	20:24:06.379450-0500	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.55704030.55704039 AUID=501> and <type=Application identifier=application.com.nexy.assistant.55704030.55704039>
default	20:24:06.407984-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	20:24:06.408258-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant)]
default	20:24:06.408334-0500	ControlCenter	Active activity attributions changed to ["scr:com.nexy.assistant"]
default	20:24:06.564284-0500	Nexy	[0xc7d7f9a40] activating connection: mach=true listener=false peer=false name=com.apple.usernoted.client
default	20:24:06.580537-0500	distnoted	register name: com.apple.nsquiet_safe_quit_give_reason object: com.nexy.assistant token: 2300000021 pid: 98347
default	20:24:06.582694-0500	Nexy	       AudioConverter.cpp:1317  AudioConverter -> 0xc7ade2ac0: The in-process GetProperty call returned 1886547824 for property 1886546285 with size 8.
default	20:24:06.582825-0500	Nexy	       AudioConverter.cpp:1317  AudioConverter -> 0xc7ade2ac0: The in-process GetProperty call returned 1886547824 for property 1886546285 with size 8.
default	20:24:06.583165-0500	Nexy	         AVAudioEngine.mm:1182  Engine@0xc7c35c600: start, was running 0
default	20:24:06.586244-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.55704030.55704039(501)>:98347] from originator [osservice<com.apple.powerd>:332] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:400-332-144259 target:98347 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	20:24:06.586324-0500	runningboardd	Assertion 400-332-144259 (target:[app<application.com.nexy.assistant.55704030.55704039(501)>:98347]) will be created as active
default	20:24:06.586628-0500	runningboardd	[app<application.com.nexy.assistant.55704030.55704039(501)>:98347] Ignoring jetsam update because this process is not memory-managed
default	20:24:06.586642-0500	runningboardd	[app<application.com.nexy.assistant.55704030.55704039(501)>:98347] Ignoring suspend because this process is not lifecycle managed
default	20:24:06.586666-0500	runningboardd	[app<application.com.nexy.assistant.55704030.55704039(501)>:98347] Ignoring GPU update because this process is not GPU managed
default	20:24:06.586781-0500	runningboardd	[app<application.com.nexy.assistant.55704030.55704039(501)>:98347] Ignoring memory limit update because this process is not memory-managed
default	20:24:06.587316-0500	usernoted	Connection com.nexy.assistant with path: /Applications/Nexy.app
default	20:24:06.589754-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.55704030.55704039(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:24:06.590334-0500	gamepolicyd	Received state update for 98347 (app<application.com.nexy.assistant.55704030.55704039(501)>, running-active-NotVisible
default	20:24:06.592413-0500	Nexy	NSApp cache appearance:
-NSRequiresAquaSystemAppearance: 0
-appearance: (null)
-effectiveAppearance: <NSCompositeAppearance: 0xc7c178780
 (
    "<NSDarkAquaAppearance: 0xc7c1788c0>",
    "<NSSystemAppearance: 0xc7c1786e0>"
)>
default	20:24:06.594336-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xa}
default	20:24:06.595380-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1f40af","name":"Nexy(98347)"}, "details":{"deviceUIDs":["1C-77-54-18-C8-A3:output"],"implicit_category":"MediaPlayback","input_running":false,"output_running":true} }
default	20:24:06.595474-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 175, PID = 98347, Name = sid:0x1f40af, Nexy(98347), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	20:24:06.595540-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 175, PID = 98347, Name = sid:0x1f40af, Nexy(98347), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	20:24:06.595782-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:24:06.595598-0500	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1f40af, Nexy(98347), 'prim'', AudioCategory changed to 'MediaPlayback'
default	20:24:06.595819-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:24:06.595633-0500	audiomxd	UpdateAudioState CID 0x91550001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:24:06.595659-0500	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 175, PID = 98347, Name = sid:0x1f40af, Nexy(98347), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO> is going active
default	20:24:06.595673-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsPlaying:]: MXCoreSession com.nexy.assistant with category/mode MediaPlayback/Default and coreSessionID = 175 starting playing
default	20:24:06.595880-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 175, PID = 98347, Name = sid:0x1f40af, Nexy(98347), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	20:24:06.595947-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 175, PID = 98347, Name = sid:0x1f40af, Nexy(98347), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO>
default	20:24:06.596134-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 201, deviceID = <private>
default	20:24:06.596163-0500	Nexy	[0xc7d7f9f40] activating connection: mach=true listener=false peer=false name=com.apple.dock.fullscreen
default	20:24:06.596178-0500	audiomxd	AudioApplicationInfoImpl.mm:395   Successfully updated session 0x1f40af to isSessionRecording: 0
	app: {"name":"[implicit] Nexy","pid":98347}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1f40af, sessionType: 'prim', isRecording: false }, 
]
default	20:24:06.596295-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 1]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)}
default	20:24:06.596335-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	20:24:06.596354-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 201 flag 0x1 < Hijack > app com.nexy.assistant CID 0x91550001 category Not set
default	20:24:06.596554-0500	audiomxd	UpdateAudioState CID 0x91550001 audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	20:24:06.596626-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 201,
}
default	20:24:06.596651-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	20:24:06.596663-0500	audioaccessoryd	AudioStateChanged: Added audio session app com.nexy.assistant NULL -> 201 count 4
default	20:24:06.596685-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 201
default	20:24:06.597732-0500	Nexy	[0xc7d7fa080] activating connection: mach=true listener=false peer=false name=com.apple.fonts
default	20:24:06.601315-0500	Nexy	(<private>) deleteSearchableItemsWithDomainIdentifiers, protectionClass:(null), domainIdentifiers number:1
default	20:24:06.601742-0500	Nexy	sConnectionName: com.apple.spotlight.IndexAgent
default	20:24:06.601756-0500	Nexy	Start service name com.apple.spotlight.IndexAgent
default	20:24:06.601757-0500	Nexy	[C:1] Alloc com.apple.controlcenter.statusitems
default	20:24:06.601788-0500	Nexy	[0xc7d7fa1c0] activating connection: mach=true listener=false peer=false name=com.apple.spotlight.IndexAgent
default	20:24:06.601830-0500	Nexy	[0xc7d7fa440] activating connection: mach=false listener=false peer=false name=(anonymous)
default	20:24:06.601902-0500	Nexy	FBSWorkspace registering source: <private>
default	20:24:06.603214-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	20:24:06.603306-0500	Nexy	<FBSWorkspaceScenesClient:0xc7cd1d720 <private>> attempting immediate handshake from activate
default	20:24:06.603362-0500	Nexy	<FBSWorkspaceScenesClient:0xc7cd1d720 <private>> sent handshake
default	20:24:06.603468-0500	Nexy	Realizing settings extension __NSStatusItemSceneHostSettings__ on FBSSceneSettings
default	20:24:06.603485-0500	ControlCenter	Asked to bootstrap a new process for handle: [app<application.com.nexy.assistant.55704030.55704039(501)>:98347]
default	20:24:06.603517-0500	ControlCenter	Creating process (sync=true) for handle: [app<application.com.nexy.assistant.55704030.55704039(501)>:98347]
default	20:24:06.603598-0500	ControlCenter	[app<application.com.nexy.assistant.55704030.55704039>:98347] Registering event dispatcher at init
default	20:24:06.603688-0500	ControlCenter	Created <FBWorkspace: 0xc327a5fe0; <FBApplicationProcess: 0xc3130c000; app<application.com.nexy.assistant.55704030.55704039>:98347(vA02935)>>
default	20:24:06.603708-0500	ControlCenter	Bootstrapping app<application.com.nexy.assistant.55704030.55704039> with intent background
default	20:24:06.604054-0500	runningboardd	Launch request for app<application.com.nexy.assistant.55704030.55704039(501)>[0] is using uid 501 (divined from auid 501 euid 501)
default	20:24:06.604171-0500	runningboardd	Acquiring assertion targeting app<application.com.nexy.assistant.55704030.55704039(501)> from originator [osservice<com.apple.controlcenter(501)>:615] with description <RBSAssertionDescriptor| "FBApplicationProcess" ID:400-615-144260 target:app<application.com.nexy.assistant.55704030.55704039(501)> attributes:[
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableLPRunReason-Suspend" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableRole-NonUI" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableJetsamPriority-Active" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableBootstrapping" sourceEnvironment:"(null)">
	]>
default	20:24:06.604137-0500	Nexy	Realizing settings extension __NSStatusItemSceneClientSettings__ on FBSSceneClientSettings
default	20:24:06.604325-0500	runningboardd	Assertion 400-615-144260 (target:app<application.com.nexy.assistant.55704030.55704039(501)>) will be created as active
default	20:24:06.604362-0500	runningboardd	setting abstract target for <RBSAssertionDescriptor| "FBApplicationProcess" ID:400-615-144260 target:app<application.com.nexy.assistant.55704030.55704039(501)> attributes:[
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableLPRunReason-Suspend" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableRole-NonUI" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableJetsamPriority-Active" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableBootstrapping" sourceEnvironment:"(null)">
	]> to [app<application.com.nexy.assistant.55704030.55704039(501)>:98347]
default	20:24:06.604741-0500	runningboardd	[app<application.com.nexy.assistant.55704030.55704039(501)>:98347] Ignoring jetsam update because this process is not memory-managed
default	20:24:06.604753-0500	runningboardd	[app<application.com.nexy.assistant.55704030.55704039(501)>:98347] Ignoring suspend because this process is not lifecycle managed
default	20:24:06.604790-0500	runningboardd	[app<application.com.nexy.assistant.55704030.55704039(501)>:98347] Ignoring GPU update because this process is not GPU managed
default	20:24:06.604988-0500	runningboardd	[app<application.com.nexy.assistant.55704030.55704039(501)>:98347] Ignoring memory limit update because this process is not memory-managed
default	20:24:06.606127-0500	suggestd	SGDSpotlightReceiver: deleting 1 domain identifiers (1 after removing overlaps) for com.nexy.assistant: <private>
default	20:24:06.606643-0500	Nexy	Realizing settings extension FBSSceneSettingsCore on FBSSceneSettings
default	20:24:06.608732-0500	Nexy	Realizing settings extension FBSSceneClientSettingsCore on FBSSceneClientSettings
default	20:24:06.609390-0500	Nexy	Requesting scene <FBSScene: 0xc7cd1da40; com.apple.controlcenter:449CC7F2-8D7E-4BE0-8DBE-31E5C2A1CFEE> from com.apple.controlcenter.statusitems
default	20:24:06.609867-0500	Nexy	Request for <FBSScene: 0xc7cd1da40; com.apple.controlcenter:449CC7F2-8D7E-4BE0-8DBE-31E5C2A1CFEE> complete!
default	20:24:06.609966-0500	Nexy	Realizing settings extension FBSSceneTransitionContextCore on FBSSceneTransitionContext
default	20:24:06.610301-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.55704030.55704039(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:24:06.611907-0500	Nexy	Realizing settings extension __NSHostedViewSceneSettings__ on FBSSceneSettings
default	20:24:06.612276-0500	Nexy	Realizing settings extension __NSClientHostedViewSceneSettings__ on FBSSceneClientSettings
default	20:24:06.612523-0500	Nexy	Realizing settings extension __NSStatusItemAuxiliaryViewSceneSettings__ on FBSSceneSettings
default	20:24:06.612543-0500	ControlCenter	[app<application.com.nexy.assistant.55704030.55704039>:98347] Bootstrap success!
default	20:24:06.612561-0500	Nexy	Realizing settings extension __NSClientStatusItemAuxiliaryViewSceneSettings__ on FBSSceneClientSettings
default	20:24:06.612883-0500	Nexy	Requesting scene <FBSScene: 0xc7cd1db80; com.apple.controlcenter:449CC7F2-8D7E-4BE0-8DBE-31E5C2A1CFEE-Aux[1]-NSStatusItemView> from com.apple.controlcenter.statusitems
default	20:24:06.613085-0500	ControlCenter	[app<application.com.nexy.assistant.55704030.55704039>:98347] Setting process visibility to: Background
default	20:24:06.613135-0500	Nexy	Request for <FBSScene: 0xc7cd1db80; com.apple.controlcenter:449CC7F2-8D7E-4BE0-8DBE-31E5C2A1CFEE-Aux[1]-NSStatusItemView> complete!
default	20:24:06.613146-0500	ControlCenter	[app<application.com.nexy.assistant.55704030.55704039>:98347] No launch watchdog for this process, dropping initial assertion in 2.0s
default	20:24:06.613451-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.55704030.55704039(501)>:98347] from originator [osservice<com.apple.controlcenter(501)>:615] with description <RBSAssertionDescriptor| "FBWorkspaceDomain: injecting saved endowment" ID:400-615-144261 target:98347 attributes:[
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"WorkspaceEndpointInjection" sourceEnvironment:"(null)">
	]>
default	20:24:06.613516-0500	runningboardd	Assertion 400-615-144261 (target:[app<application.com.nexy.assistant.55704030.55704039(501)>:98347]) will be created as active
default	20:24:06.613922-0500	runningboardd	[app<application.com.nexy.assistant.55704030.55704039(501)>:98347] Ignoring jetsam update because this process is not memory-managed
default	20:24:06.614928-0500	Nexy	[com.apple.controlcenter:449CC7F2-8D7E-4BE0-8DBE-31E5C2A1CFEE-Aux[1]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
default	20:24:06.614948-0500	Nexy	[com.apple.controlcenter:449CC7F2-8D7E-4BE0-8DBE-31E5C2A1CFEE-Aux[1]-NSStatusItemView] Dropping transition context because the scene is reconnecting
default	20:24:06.613935-0500	runningboardd	[app<application.com.nexy.assistant.55704030.55704039(501)>:98347] Ignoring suspend because this process is not lifecycle managed
default	20:24:06.614979-0500	runningboardd	[app<application.com.nexy.assistant.55704030.55704039(501)>:98347] Ignoring GPU update because this process is not GPU managed
default	20:24:06.615611-0500	runningboardd	[app<application.com.nexy.assistant.55704030.55704039(501)>:98347] Ignoring memory limit update because this process is not memory-managed
default	20:24:06.619438-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.55704030.55704039(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:24:06.619613-0500	Nexy	[com.apple.controlcenter:449CC7F2-8D7E-4BE0-8DBE-31E5C2A1CFEE-Aux[1]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
default	20:24:06.619633-0500	Nexy	[com.apple.controlcenter:449CC7F2-8D7E-4BE0-8DBE-31E5C2A1CFEE-Aux[1]-NSStatusItemView] Dropping transition context because the scene is reconnecting
default	20:24:06.619750-0500	Nexy	Warning: the app is using `-[NSStatusBarButton setHighlightsBy:]` to set the highlight behavior. Instead, consider removing that setting. That will enable macOS to highlight the status bar button as appropriate for all configurations (e.g., light, dark, and increased contrast modes).
default	20:24:06.619911-0500	ControlCenter	Adding: <FBApplicationProcess: 0xc3130c000; app<application.com.nexy.assistant.55704030.55704039>:98347(vA02935)>
default	20:24:06.620511-0500	ControlCenter	[app<application.com.nexy.assistant.55704030.55704039>:98347] Connection established.
default	20:24:06.620610-0500	ControlCenter	[app<application.com.nexy.assistant.55704030.55704039>:98347] created proxy of <BSXPCServiceConnectionProxy<FBSWorkspaceServiceServerInterface>: 0xc36670150>
default	20:24:06.620631-0500	ControlCenter	Received state update for 98347 (app<application.com.nexy.assistant.55704030.55704039(501)>, running-active-NotVisible
default	20:24:06.620639-0500	ControlCenter	[app<application.com.nexy.assistant.55704030.55704039>:98347] Connection to remote process established!
default	20:24:06.628566-0500	ControlCenter	Asked to bootstrap a new process for handle: [app<application.com.nexy.assistant.55704030.55704039(501)>:98347]
default	20:24:06.628592-0500	ControlCenter	A process already exists for this handle: <FBApplicationProcess: 0xc3130c000; app<application.com.nexy.assistant.55704030.55704039>:98347(vA02935)>
default	20:24:06.628710-0500	ControlCenter	[app<application.com.nexy.assistant.55704030.55704039>:98347] Registered new scene: <FBWorkspaceScene: 0xc346c6a00; com.apple.controlcenter:449CC7F2-8D7E-4BE0-8DBE-31E5C2A1CFEE> (fromRemnant = 0)
default	20:24:06.628750-0500	ControlCenter	[app<application.com.nexy.assistant.55704030.55704039>:98347] Workspace interruption policy did change: reconnect
default	20:24:06.628981-0500	ControlCenter	[com.apple.controlcenter:449CC7F2-8D7E-4BE0-8DBE-31E5C2A1CFEE] Client process connected: [app<application.com.nexy.assistant.55704030.55704039(501)>:98347]
default	20:24:06.628998-0500	Nexy	Request for <FBSScene: 0xc7cd1da40; com.apple.controlcenter:449CC7F2-8D7E-4BE0-8DBE-31E5C2A1CFEE> complete!
default	20:24:06.629065-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.55704030.55704039(501)>:98347] from originator [osservice<com.apple.controlcenter(501)>:615] with description <RBSAssertionDescriptor| "com.apple.frontboard.after-life.interrupted" ID:400-615-144262 target:98347 attributes:[
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"AfterLife-Interrupted" sourceEnvironment:"(null)">
	]>
default	20:24:06.629157-0500	runningboardd	Assertion 400-615-144262 (target:[app<application.com.nexy.assistant.55704030.55704039(501)>:98347]) will be created as inactive as originator process has not exited
default	20:24:06.629697-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.55704030.55704039(501)>:98347] from originator [osservice<com.apple.controlcenter(501)>:615] with description <RBSAssertionDescriptor| "FBWorkspace (BG-Active[40])" ID:400-615-144263 target:98347 attributes:[
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableLPRunReason-Suspend" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableRole-NonUI" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableJetsamPriority-Active" sourceEnvironment:"(null)">
	]>
default	20:24:06.629829-0500	runningboardd	Assertion 400-615-144263 (target:[app<application.com.nexy.assistant.55704030.55704039(501)>:98347]) will be created as active
default	20:24:06.630635-0500	runningboardd	[app<application.com.nexy.assistant.55704030.55704039(501)>:98347] Ignoring jetsam update because this process is not memory-managed
default	20:24:06.629965-0500	ControlCenter	[app<application.com.nexy.assistant.55704030.55704039>:98347] Workspace state did change: XX-None[0] --> BG-Active[40] (assertion acquired).
default	20:24:06.630768-0500	runningboardd	[app<application.com.nexy.assistant.55704030.55704039(501)>:98347] Ignoring suspend because this process is not lifecycle managed
default	20:24:06.630860-0500	runningboardd	[app<application.com.nexy.assistant.55704030.55704039(501)>:98347] Ignoring GPU update because this process is not GPU managed
default	20:24:06.631136-0500	runningboardd	[app<application.com.nexy.assistant.55704030.55704039(501)>:98347] Ignoring memory limit update because this process is not memory-managed
default	20:24:06.630740-0500	Nexy	<FBSWorkspaceScenesClient:0xc7cd1d720 <private>> Reconnecting scene com.apple.controlcenter:449CC7F2-8D7E-4BE0-8DBE-31E5C2A1CFEE
default	20:24:06.631051-0500	ControlCenter	Asked to bootstrap a new process for handle: [app<application.com.nexy.assistant.55704030.55704039(501)>:98347]
default	20:24:06.631108-0500	ControlCenter	A process already exists for this handle: <FBApplicationProcess: 0xc3130c000; app<application.com.nexy.assistant.55704030.55704039>:98347(vA02935)>
default	20:24:06.631270-0500	ControlCenter	[app<application.com.nexy.assistant.55704030.55704039>:98347] Registered new scene: <FBWorkspaceScene: 0xc346c7000; com.apple.controlcenter:449CC7F2-8D7E-4BE0-8DBE-31E5C2A1CFEE-Aux[1]-NSStatusItemView> (fromRemnant = 0)
default	20:24:06.632378-0500	Nexy	Request for <FBSScene: 0xc7cd1db80; com.apple.controlcenter:449CC7F2-8D7E-4BE0-8DBE-31E5C2A1CFEE-Aux[1]-NSStatusItemView> complete!
default	20:24:06.632366-0500	ControlCenter	[com.apple.controlcenter:449CC7F2-8D7E-4BE0-8DBE-31E5C2A1CFEE-Aux[1]-NSStatusItemView] Client process connected: [app<application.com.nexy.assistant.55704030.55704039(501)>:98347]
default	20:24:06.632814-0500	Nexy	<FBSWorkspaceScenesClient:0xc7cd1d720 <private>> Reconnecting scene com.apple.controlcenter:449CC7F2-8D7E-4BE0-8DBE-31E5C2A1CFEE-Aux[1]-NSStatusItemView
default	20:24:06.635639-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.55704030.55704039(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:24:06.636352-0500	Nexy	Registering for test daemon availability notify post.
default	20:24:06.636576-0500	Nexy	notify_get_state check indicated test daemon not ready.
default	20:24:06.636759-0500	Nexy	notify_get_state check indicated test daemon not ready.
default	20:24:06.636900-0500	Nexy	notify_get_state check indicated test daemon not ready.
default	20:24:06.641855-0500	Nexy	[0xc7d7fa6c0] activating connection: mach=true listener=false peer=false name=com.apple.coreservices.appleevents
default	20:24:06.650950-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b5166d00 at /Applications/Nexy.app
default	20:24:06.658035-0500	Nexy	[0xc7d7f83c0] Connection returned listener port: 0x4703
default	20:24:06.658792-0500	Nexy	SignalReady: pid=98347 asn=0x0-0x75f75f
default	20:24:06.659468-0500	Nexy	SIGNAL: pid=98347 asn=0x0x-0x75f75f
default	20:24:06.660353-0500	loginwindow	-[Application _updateInformationInternal] | Got App URL: file:///Applications/Nexy.app/
default	20:24:06.678538-0500	Nexy	[com.apple.controlcenter:449CC7F2-8D7E-4BE0-8DBE-31E5C2A1CFEE-Aux[1]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
default	20:24:06.682548-0500	Nexy	[com.apple.controlcenter:449CC7F2-8D7E-4BE0-8DBE-31E5C2A1CFEE-Aux[1]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
default	20:24:06.686988-0500	Nexy	void _NSDisableAutomaticTerminationAndLog(NSString *) Restoring windows
default	20:24:06.686997-0500	Nexy	-[NSApplication _reopenWindowsAsNecessaryIncludingRestorableState:withFullFidelity:completionHandler:] shouldRestoreState=1 hasPersistentStateToRestore=0 shouldStillRestoreStateAfterPrompting=0
default	20:24:06.687017-0500	Nexy	[0xc7d7f9540] activating connection: mach=true listener=false peer=false name=com.apple.window_proxies
default	20:24:06.687170-0500	Nexy	[0xc7d7f9540] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	20:24:06.692011-0500	Nexy	void _NSEnableAutomaticTerminationAndLog(NSString *) Restoring windows
default	20:24:06.696244-0500	Nexy	[C:2] Alloc <private>
default	20:24:06.696216-0500	ControlCenter	Received state update for 98347 (app<application.com.nexy.assistant.55704030.55704039(501)>, running-active-NotVisible
default	20:24:06.696304-0500	Nexy	[0xc7d7f9540] activating connection: mach=false listener=false peer=false name=(anonymous)
default	20:24:06.698005-0500	Nexy	[0xc7d7f92c0] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
error	20:24:06.698853-0500	tccd	TCCDProcess: identifier=com.nexy.assistant, pid=98347, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy attempted to call TCCAccessRequest for kTCCServiceAccessibility without the recommended com.apple.private.tcc.manager.check-by-audit-token entitlement
default	20:24:06.698983-0500	Nexy	[0xc7d7f92c0] invalidated after the last release of the connection object
default	20:24:06.698810-0500	ControlCenter	Host properties initialized; (bid:com.nexy.assistant-Item-0-98347). State(applicationItem: true, clientRequestsVisibility: true, neverClip: false)
default	20:24:06.699522-0500	WindowManager	Connection activated | (98347) Nexy
default	20:24:06.700632-0500	gamepolicyd	Received state update for 98347 (app<application.com.nexy.assistant.55704030.55704039(501)>, running-active-NotVisible
default	20:24:06.700850-0500	ControlCenter	Starting to track host; (bid:com.nexy.assistant-Item-0-98347)
default	20:24:06.701447-0500	ControlCenter	Created new displayable type DisplayableAppStatusItemType(3DB48099, (bid:com.nexy.assistant-Item-0-98347)) for (bid:com.nexy.assistant-Item-0-98347)
default	20:24:06.702344-0500	ControlCenter	Adding displayable items for status items; [(bid:com.nexy.assistant-Item-0-98347)]
default	20:24:06.703820-0500	ControlCenter	Created instance DisplayableId(BC04A446) in .menuBar for DisplayableAppStatusItemType(3DB48099, (bid:com.nexy.assistant-Item-0-98347)) .menuBar
default	20:24:06.704860-0500	Nexy	void _NSDisableAutomaticTerminationAndLog(NSString *) NSAccessibility Request Received
default	20:24:06.713794-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.55704030.55704039(501)>:98347] from originator [app<application.com.nexy.assistant.55704030.55704039(501)>:98347] with description <RBSAssertionDescriptor| "AudioHAL" ID:400-98347-144264 target:98347 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	20:24:06.714265-0500	runningboardd	Assertion 400-98347-144264 (target:[app<application.com.nexy.assistant.55704030.55704039(501)>:98347]) will be created as active
default	20:24:06.716926-0500	runningboardd	[app<application.com.nexy.assistant.55704030.55704039(501)>:98347] Ignoring jetsam update because this process is not memory-managed
default	20:24:06.716986-0500	runningboardd	[app<application.com.nexy.assistant.55704030.55704039(501)>:98347] Ignoring suspend because this process is not lifecycle managed
default	20:24:06.717103-0500	runningboardd	[app<application.com.nexy.assistant.55704030.55704039(501)>:98347] Ignoring GPU update because this process is not GPU managed
default	20:24:06.719432-0500	runningboardd	[app<application.com.nexy.assistant.55704030.55704039(501)>:98347] Ignoring memory limit update because this process is not memory-managed
default	20:24:06.720102-0500	ControlCenter	Created ephemaral instance DisplayableId(BC04A446) for (bid:com.nexy.assistant-Item-0-98347) with positioning .ephemeral
default	20:24:06.728948-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.55704030.55704039(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:24:06.730077-0500	ControlCenter	Received state update for 98347 (app<application.com.nexy.assistant.55704030.55704039(501)>, running-active-NotVisible
default	20:24:06.736471-0500	gamepolicyd	Received state update for 98347 (app<application.com.nexy.assistant.55704030.55704039(501)>, running-active-NotVisible
default	20:24:07.061600-0500	Nexy	[com.apple.controlcenter:449CC7F2-8D7E-4BE0-8DBE-31E5C2A1CFEE-Aux[1]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
default	20:24:07.063008-0500	Nexy	[com.apple.controlcenter:449CC7F2-8D7E-4BE0-8DBE-31E5C2A1CFEE] Sending action(s) in update: NSSceneFenceAction
default	20:24:07.071809-0500	Nexy	[com.apple.controlcenter:449CC7F2-8D7E-4BE0-8DBE-31E5C2A1CFEE-Aux[1]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
default	20:24:07.072200-0500	Nexy	[com.apple.controlcenter:449CC7F2-8D7E-4BE0-8DBE-31E5C2A1CFEE] Sending action(s) in update: NSSceneFenceAction
default	20:24:07.072738-0500	Nexy	[com.apple.controlcenter:449CC7F2-8D7E-4BE0-8DBE-31E5C2A1CFEE-Aux[1]-NSStatusItemView] Received action(s) in scene-update: NSSceneFenceAction
default	20:24:07.075294-0500	Nexy	[com.apple.controlcenter:449CC7F2-8D7E-4BE0-8DBE-31E5C2A1CFEE-Aux[1]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
default	20:24:07.093677-0500	Nexy	[com.apple.controlcenter:449CC7F2-8D7E-4BE0-8DBE-31E5C2A1CFEE] Sending action(s) in update: NSSceneFenceAction
default	20:24:07.102936-0500	Nexy	*warn* MailCS ======%%% _setMailMessageAttributes skip:1
default	20:24:07.107317-0500	Nexy	Start service name com.apple.spotlightknowledged
default	20:24:07.108598-0500	Nexy	[GMS] availability notification token 100
default	20:24:07.192606-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.55704030.55704039(501)>:98347] from originator [osservice<com.apple.WindowServer(88)>:391] with description <RBSAssertionDescriptor| "AppDrawing" ID:400-391-144265 target:98347 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"AppDrawing" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	20:24:07.192703-0500	runningboardd	Assertion 400-391-144265 (target:[app<application.com.nexy.assistant.55704030.55704039(501)>:98347]) will be created as active
default	20:24:07.193212-0500	runningboardd	[app<application.com.nexy.assistant.55704030.55704039(501)>:98347] Ignoring jetsam update because this process is not memory-managed
default	20:24:07.193229-0500	runningboardd	[app<application.com.nexy.assistant.55704030.55704039(501)>:98347] Ignoring suspend because this process is not lifecycle managed
default	20:24:07.193248-0500	runningboardd	[app<application.com.nexy.assistant.55704030.55704039(501)>:98347] Ignoring GPU update because this process is not GPU managed
default	20:24:07.193284-0500	runningboardd	[app<application.com.nexy.assistant.55704030.55704039(501)>:98347] Ignoring memory limit update because this process is not memory-managed
default	20:24:07.196639-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.55704030.55704039(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:24:07.197299-0500	ControlCenter	Received state update for 98347 (app<application.com.nexy.assistant.55704030.55704039(501)>, running-active-NotVisible
default	20:24:07.197402-0500	gamepolicyd	Received state update for 98347 (app<application.com.nexy.assistant.55704030.55704039(501)>, running-active-NotVisible
default	20:24:07.280340-0500	ControlCenter	[app<application.com.nexy.assistant.55704030.55704039>:98347] Workspace state did change: BG-Active[40] --> XX-None[0] (assertion dropped).
default	20:24:07.280596-0500	runningboardd	Invalidating assertion 400-615-144263 (target:[app<application.com.nexy.assistant.55704030.55704039(501)>:98347]) from originator [osservice<com.apple.controlcenter(501)>:615]
default	20:24:07.388739-0500	runningboardd	[app<application.com.nexy.assistant.55704030.55704039(501)>:98347] Ignoring jetsam update because this process is not memory-managed
default	20:24:07.388751-0500	runningboardd	[app<application.com.nexy.assistant.55704030.55704039(501)>:98347] Ignoring suspend because this process is not lifecycle managed
default	20:24:07.388761-0500	runningboardd	[app<application.com.nexy.assistant.55704030.55704039(501)>:98347] Ignoring GPU update because this process is not GPU managed
default	20:24:07.388781-0500	runningboardd	[app<application.com.nexy.assistant.55704030.55704039(501)>:98347] Ignoring memory limit update because this process is not memory-managed
default	20:24:07.393610-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.55704030.55704039(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:24:07.394516-0500	ControlCenter	Received state update for 98347 (app<application.com.nexy.assistant.55704030.55704039(501)>, running-active-NotVisible
default	20:24:07.394943-0500	gamepolicyd	Received state update for 98347 (app<application.com.nexy.assistant.55704030.55704039(501)>, running-active-NotVisible
default	20:24:07.464869-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8eed50600 at /Applications/Nexy.app
default	20:24:07.471751-0500	tccd	Publishing <TCCDEvent: type=Create, service=kTCCServiceAppleEvents, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 3 subscribers: {
    39 = "<TCCDEventSubscriber: token=39, state=Passed, csid=com.apple.chronod>";
    38 = "<TCCDEventSubscriber: token=38, state=Initial, csid=(null)>";
    41 = "<TCCDEventSubscriber: token=41, state=Passed, csid=com.apple.photolibraryd>";
}
default	20:24:07.482309-0500	chronod	[appAuth:com.nexy.assistant] tcc authorization(s) changed
error	20:24:07.534584-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceSystemPolicyAllFiles com.nexy.assistant full
error	20:24:07.535478-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAccessibility com.nexy.assistant full
error	20:24:07.535495-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceListenEvent com.nexy.assistant full
error	20:24:07.536006-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceSystemPolicyAllFiles com.nexy.assistant full
error	20:24:07.593154-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAddressBook com.nexy.assistant full
error	20:24:07.594269-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAppleEvents com.nexy.assistant full
error	20:24:07.594472-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAppleEvents com.nexy.assistant full
error	20:24:07.594796-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAddressBook com.nexy.assistant full
error	20:24:07.595803-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAppleEvents com.nexy.assistant full
error	20:24:07.595927-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceAppleEvents com.nexy.assistant full
error	20:24:07.596478-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceMicrophone com.nexy.assistant full
error	20:24:07.598647-0500	SecurityPrivacyExtension	/AppleInternal/Library/BuildRoots/4~CCKzugBjdyGA3WHu9ip90KmiFMk4I5oJfOTbSBk/Library/Caches/com.apple.xbs/Sources/SecurityPref/Extension/Privacy/TCC+PrivacyServicesProvider.swift:195 loadAuthorizationStates(for:) new entry: kTCCServiceMicrophone com.nexy.assistant full
default	20:24:08.712533-0500	runningboardd	Invalidating assertion 400-615-144260 (target:app<application.com.nexy.assistant.55704030.55704039(501)>) from originator [osservice<com.apple.controlcenter(501)>:615]
default	20:24:11.582773-0500	Nexy	void _updateToReflectAutomaticTerminationState(void) Setting _kLSApplicationWouldBeTerminatedByTALKey=1
default	20:24:14.730010-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=391.3439, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=98347, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=391, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	20:24:14.730052-0500	tccd	requestor: TCCDProcess: identifier=com.apple.WindowServer, pid=391, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=98347, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	20:24:14.732084-0500	tccd	AUTHREQ_SUBJECT: msgID=391.3439, subject=com.nexy.assistant,
default	20:24:14.733230-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b5166700 at /Applications/Nexy.app
default	20:24:16.366040-0500	ControlCenter	Recent activity attributions changed to ["scr:com.nexy.assistant"]
default	20:24:17.345613-0500	Nexy	LSExceptions shared instance invalidated for timeout.
default	20:24:19.165409-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=391.3440, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=98347, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=391, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	20:24:19.165462-0500	tccd	requestor: TCCDProcess: identifier=com.apple.WindowServer, pid=391, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=98347, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	20:24:19.167562-0500	tccd	AUTHREQ_SUBJECT: msgID=391.3440, subject=com.nexy.assistant,
default	20:24:19.168888-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b5166700 at /Applications/Nexy.app
default	20:24:38.926409-0500	Nexy	[com.apple.controlcenter:449CC7F2-8D7E-4BE0-8DBE-31E5C2A1CFEE] Sending action(s) in update: NSSceneFenceAction
default	20:24:39.569406-0500	Nexy	[com.apple.controlcenter:449CC7F2-8D7E-4BE0-8DBE-31E5C2A1CFEE] Sending action(s) in update: NSSceneFenceAction
default	20:24:39.571218-0500	Nexy	                AUHAL.cpp:420   AUHAL: (0xc7e9eaa40) Selecting device 85 from constructor
default	20:24:39.571244-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0xc7e9eaa40)
default	20:24:39.571250-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0xc7e9eaa40) not already running
default	20:24:39.571259-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0xc7e9eaa40) nothing to teardown
default	20:24:39.571263-0500	Nexy	                AUHAL.cpp:762   SelectDevice: (0xc7e9eaa40) connecting device 85
default	20:24:39.571368-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0xc7e9eaa40) Device ID: 85 (Input:No | Output:Yes): true
default	20:24:39.571872-0500	Nexy	                AUHAL.cpp:774   SelectDevice: (0xc7e9eaa40) created ioproc 0xb for device 85
default	20:24:39.572029-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0xc7e9eaa40) adding 7 device listeners to device 85
default	20:24:39.572202-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0xc7e9eaa40) adding 0 device delegate listeners to device 85
default	20:24:39.572211-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0xc7e9eaa40)
default	20:24:39.572273-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  48000 Hz, Float32, interleaved
default	20:24:39.572283-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	20:24:39.572288-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	20:24:39.572295-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	20:24:39.572303-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	20:24:39.572391-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0xc7e9eaa40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	20:24:39.572402-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0xc7e9eaa40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	20:24:39.572407-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	20:24:39.572411-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0xc7e9eaa40) removing 0 device listeners from device 0
default	20:24:39.572415-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0xc7e9eaa40) removing 0 device delegate listeners from device 0
default	20:24:39.572417-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0xc7e9eaa40)
default	20:24:39.572434-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is DISABLED
default	20:24:39.572478-0500	Nexy	                AUHAL.cpp:2303  SetProperty: (0xc7e9eaa40) caller requesting device change from 85 to 91
default	20:24:39.572485-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0xc7e9eaa40)
default	20:24:39.572491-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0xc7e9eaa40) not already running
default	20:24:39.572495-0500	Nexy	                AUHAL.cpp:687   SelectDevice: (0xc7e9eaa40) disconnecting device 85
default	20:24:39.572499-0500	Nexy	                AUHAL.cpp:751   SelectDevice: (0xc7e9eaa40) destroying ioproc 0xb for device 85
default	20:24:39.572520-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped Unknown {1C-77-54-18-C8-A3:output, 0xb}
default	20:24:39.572746-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 1]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:24:39.573132-0500	Nexy	                AUHAL.cpp:762   SelectDevice: (0xc7e9eaa40) connecting device 91
default	20:24:39.573200-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0xc7e9eaa40) Device ID: 91 (Input:Yes | Output:No): true
default	20:24:39.575047-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.3403, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=98347, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=392, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	20:24:39.577039-0500	tccd	AUTHREQ_SUBJECT: msgID=401.3403, subject=com.nexy.assistant,
default	20:24:39.578011-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8eed50300 at /Applications/Nexy.app
default	20:24:39.589243-0500	Nexy	 [INFO] SLSHWCaptureDesktopProxying:485 request: <private>
default	20:24:39.589287-0500	Nexy	 [INFO] -[RPDaemonProxy proxyCoreGraphicsWithMethodType:config:machPort:completionHandler:]:1493
default	20:24:39.591267-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=82607.5, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=98347, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.replayd, pid=82607, auid=501, euid=501, binary_path=/usr/libexec/replayd}, },
default	20:24:39.591304-0500	tccd	requestor: TCCDProcess: identifier=com.apple.replayd, pid=82607, auid=501, euid=501, binary_path=/usr/libexec/replayd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=98347, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	20:24:39.592744-0500	tccd	AUTHREQ_SUBJECT: msgID=82607.5, subject=com.nexy.assistant,
default	20:24:39.593944-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b5166700 at /Applications/Nexy.app
default	20:24:39.598462-0500	Nexy	                AUHAL.cpp:774   SelectDevice: (0xc7e9eaa40) created ioproc 0xa for device 91
default	20:24:39.598583-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0xc7e9eaa40) adding 7 device listeners to device 91
default	20:24:39.598999-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0xc7e9eaa40) adding 0 device delegate listeners to device 91
default	20:24:39.599006-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0xc7e9eaa40)
default	20:24:39.599014-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 output streams; not all mono
default	20:24:39.599024-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	20:24:39.599137-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  input stream 0 [0x5c]:  1 ch,  24000 Hz, Float32
default	20:24:39.599143-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 input streams; all mono
default	20:24:39.599149-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  1 ch,  24000 Hz, Float32
default	20:24:39.599229-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0xc7e9eaa40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	20:24:39.599240-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0xc7e9eaa40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	20:24:39.599244-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	20:24:39.599248-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0xc7e9eaa40) removing 7 device listeners from device 85
default	20:24:39.599407-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0xc7e9eaa40) removing 0 device delegate listeners from device 85
default	20:24:39.599416-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0xc7e9eaa40)
default	20:24:39.599931-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	20:24:39.600905-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.3404, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=98347, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=392, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	20:24:39.601954-0500	tccd	AUTHREQ_SUBJECT: msgID=401.3404, subject=com.nexy.assistant,
default	20:24:39.602543-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8eed50300 at /Applications/Nexy.app
default	20:24:39.611447-0500	Nexy	 [INFO] SLSHWCaptureDesktopProxying:485 request: <private>
default	20:24:39.611479-0500	Nexy	 [INFO] -[RPDaemonProxy proxyCoreGraphicsWithMethodType:config:machPort:completionHandler:]:1493
default	20:24:39.619371-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	20:24:39.620378-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=391.3450, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=98347, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=391, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	20:24:39.620382-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.3405, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=98347, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=392, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	20:24:39.620405-0500	tccd	requestor: TCCDProcess: identifier=com.apple.WindowServer, pid=391, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=98347, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	20:24:39.621247-0500	tccd	AUTHREQ_SUBJECT: msgID=391.3450, subject=com.nexy.assistant,
default	20:24:39.621467-0500	tccd	AUTHREQ_SUBJECT: msgID=401.3405, subject=com.nexy.assistant,
default	20:24:39.621881-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b5166700 at /Applications/Nexy.app
default	20:24:39.622112-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8eed50300 at /Applications/Nexy.app
default	20:24:39.642740-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.3406, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=98347, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=392, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	20:24:39.643788-0500	tccd	AUTHREQ_SUBJECT: msgID=401.3406, subject=com.nexy.assistant,
default	20:24:39.644370-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8eed50300 at /Applications/Nexy.app
default	20:24:39.663695-0500	Nexy	 [INFO] SLSHWCaptureDesktopProxying_block_invoke:506 request: <private>, error: (null), windowInfo: (null)
default	20:24:39.665414-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=82607.6, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=98347, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.replayd, pid=82607, auid=501, euid=501, binary_path=/usr/libexec/replayd}, },
default	20:24:39.665456-0500	tccd	requestor: TCCDProcess: identifier=com.apple.replayd, pid=82607, auid=501, euid=501, binary_path=/usr/libexec/replayd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=98347, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	20:24:39.667434-0500	tccd	AUTHREQ_SUBJECT: msgID=82607.6, subject=com.nexy.assistant,
default	20:24:39.670260-0500	coreaudiod	>>> NEGOTIATE [com.nexy.assistant]
default	20:24:39.670521-0500	coreaudiod	<<< NEGOTIATE [com.nexy.assistant]
default	20:24:39.671118-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b5166700 at /Applications/Nexy.app
default	20:24:39.671798-0500	coreaudiod	>>> ADAPT [com.nexy.assistant]
default	20:24:39.672789-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xafa0fd200] Created node ADM::com.nexy.assistant_7690.7540.0_airpods noise suppression studio::in-0 with nodeID 0 - reporting period = 10.000000, sample rate = 24000.000000
default	20:24:39.672859-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xafa0fd200] Created node ADM::com.nexy.assistant_7690.7540.0_airpods noise suppression studio::out-0 with nodeID 1 - reporting period = 10.000000, sample rate = 24000.000000
default	20:24:39.697818-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	20:24:39.697901-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant)]
default	20:24:39.697972-0500	ControlCenter	Active activity attributions changed to ["scr:com.nexy.assistant"]
default	20:24:39.728812-0500	Nexy	 [INFO] SLSHWCaptureDesktopProxying_block_invoke:506 request: <private>, error: (null), windowInfo: (null)
default	20:24:39.769262-0500	coreaudiod	<<< ADAPT [com.nexy.assistant]
default	20:24:39.770785-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:7690 called from <private>
default	20:24:39.770836-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Input {1C-77-54-18-C8-A3:input, 0xa}
default	20:24:39.772726-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:7690 called from <private>
default	20:24:39.775383-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(7690)
default	20:24:39.775419-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:7690 called from <private>
default	20:24:39.775433-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:7690 called from <private>
default	20:24:39.777089-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(7696)
default	20:24:39.777105-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:7696 called from <private>
default	20:24:39.777111-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:7696 called from <private>
default	20:24:39.782397-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	20:24:39.783374-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	20:24:39.778398-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(7689)
default	20:24:39.781383-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(7696)
default	20:24:39.781542-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:7689 called from <private>
default	20:24:39.781586-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:7689 called from <private>
default	20:24:39.781588-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:7696 called from <private>
default	20:24:39.781888-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:7696 called from <private>
default	20:24:39.785630-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(7690)
default	20:24:39.785691-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(7690)
default	20:24:39.785751-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(7690)
default	20:24:39.785825-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(7690)
default	20:24:39.785943-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:7690 called from <private>
default	20:24:39.785978-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:7690 called from <private>
default	20:24:39.782342-0500	runningboardd	Invalidating assertion 400-98347-144264 (target:[app<application.com.nexy.assistant.55704030.55704039(501)>:98347]) from originator [app<application.com.nexy.assistant.55704030.55704039(501)>:98347]
default	20:24:39.783246-0500	runningboardd	Invalidating assertion 400-332-144259 (target:[app<application.com.nexy.assistant.55704030.55704039(501)>:98347]) from originator [osservice<com.apple.powerd>:332]
default	20:24:39.786035-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:7690 called from <private>
default	20:24:39.786103-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:7690 called from <private>
default	20:24:39.789000-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.55704030.55704039(501)>:98347] from originator [app<application.com.nexy.assistant.55704030.55704039(501)>:98347] with description <RBSAssertionDescriptor| "AudioHAL" ID:400-98347-144315 target:98347 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	20:24:39.789211-0500	runningboardd	Assertion 400-98347-144315 (target:[app<application.com.nexy.assistant.55704030.55704039(501)>:98347]) will be created as active
default	20:24:39.786154-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:7690 called from <private>
default	20:24:39.786189-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:7690 called from <private>
default	20:24:39.786243-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:7690 called from <private>
default	20:24:39.796338-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:7689 called from <private>
default	20:24:39.796356-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:7689 called from <private>
default	20:24:39.796500-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(7689)
default	20:24:39.796545-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:7689 called from <private>
default	20:24:39.796600-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:7689 called from <private>
default	20:24:39.798852-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(7689)
default	20:24:39.798875-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(7689)
default	20:24:39.799340-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(7689)
default	20:24:39.804882-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(7696)
default	20:24:39.804914-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(7690)
default	20:24:39.805094-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:7689 called from <private>
default	20:24:39.805113-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:7689 called from <private>
default	20:24:39.805130-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:7689 called from <private>
default	20:24:39.805140-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:7689 called from <private>
default	20:24:39.805171-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:7689 called from <private>
error	20:24:39.807708-0500	Nexy	         HALC_ProxyIOContext.cpp:1075  HALC_ProxyIOContext::_StartIO(): Start failed - StartAndWaitForState returned error 35
default	20:24:39.807780-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:7689 called from <private>
default	20:24:39.810250-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	20:24:39.807817-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:7689 called from <private>
default	20:24:39.807868-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:7689 called from <private>
default	20:24:39.810683-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	20:24:39.808011-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:7696 called from <private>
default	20:24:39.808073-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:7696 called from <private>
default	20:24:39.808300-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(7696)
default	20:24:39.811173-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:7689 called from <private>
default	20:24:39.811186-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:7689 called from <private>
default	20:24:39.811795-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(7696)
default	20:24:39.811813-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(7696)
default	20:24:39.778475-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	20:24:39.811865-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(7696)
default	20:24:39.811906-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(7696)
default	20:24:39.811953-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(7696)
default	20:24:39.811996-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:7696 called from <private>
default	20:24:39.812047-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:7696 called from <private>
default	20:24:39.812134-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:7696 called from <private>
default	20:24:39.812165-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:7696 called from <private>
default	20:24:39.812211-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:7696 called from <private>
default	20:24:39.812246-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:7696 called from <private>
default	20:24:39.812279-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:7696 called from <private>
default	20:24:39.812335-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:7696 called from <private>
default	20:24:39.812370-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:7696 called from <private>
default	20:24:39.812398-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:7696 called from <private>
default	20:24:39.812457-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:7696 called from <private>
default	20:24:39.811103-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.3407, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=98347, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=392, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	20:24:39.812493-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:7696 called from <private>
default	20:24:39.812544-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:7696 called from <private>
default	20:24:39.812572-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:7696 called from <private>
default	20:24:39.812598-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:7696 called from <private>
default	20:24:39.812628-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:7696 called from <private>
default	20:24:39.818701-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	20:24:39.837224-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:7689 called from <private>
default	20:24:39.837384-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:7689 called from <private>
default	20:24:39.839449-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(7696)
default	20:24:39.839521-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(7689)
default	20:24:39.839961-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:7696 called from <private>
default	20:24:39.840289-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:7689 called from <private>
default	20:24:39.840519-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:7696 called from <private>
error	20:24:39.864856-0500	Nexy	kAudioUnitErr_TooManyFramesToProcess : inFramesToProcess=960, mMaxFramesPerSlice=941
error	20:24:39.864876-0500	Nexy	  from <private>, render err: -10874
default	20:24:39.886157-0500	Nexy	         AVAudioEngine.mm:1461  Engine@0xc7c35c600: iounit configuration changed > stopping the engine
default	20:24:39.886190-0500	Nexy	         AVAudioEngine.mm:1236  Engine@0xc7c35c600: stop, was running 1
default	20:24:39.886253-0500	Nexy	         AVAudioEngine.mm:1219  Engine@0xc7c35c600: pause, was running 1
default	20:24:39.887762-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	20:24:39.887854-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant)]
default	20:24:39.887947-0500	ControlCenter	Active activity attributions changed to ["scr:com.nexy.assistant"]
default	20:24:39.887989-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	20:24:39.902056-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:24:39.902069-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:24:39.902081-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:24:39.902091-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:24:39.902098-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:24:39.902106-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	20:24:39.902188-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	20:24:39.913717-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	20:24:39.913736-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	20:24:39.924936-0500	coreaudiod	>>> NEGOTIATE [com.nexy.assistant]
default	20:24:39.925081-0500	coreaudiod	<<< NEGOTIATE [com.nexy.assistant]
default	20:24:39.926610-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.55704030.55704039(501)>:98347] from originator [osservice<com.apple.powerd>:332] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:400-332-144324 target:98347 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	20:24:39.926867-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:7690 called from <private>
default	20:24:39.926906-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:7690 called from <private>
default	20:24:39.928203-0500	runningboardd	Assertion 400-332-144324 (target:[app<application.com.nexy.assistant.55704030.55704039(501)>:98347]) will be created as active
default	20:24:39.928107-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:7690 called from <private>
default	20:24:39.928123-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:7690 called from <private>
default	20:24:39.928677-0500	runningboardd	Invalidating assertion 400-98347-144315 (target:[app<application.com.nexy.assistant.55704030.55704039(501)>:98347]) from originator [app<application.com.nexy.assistant.55704030.55704039(501)>:98347]
default	20:24:39.928307-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:7690 called from <private>
default	20:24:39.928873-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.55704030.55704039(501)>:98347] from originator [app<application.com.nexy.assistant.55704030.55704039(501)>:98347] with description <RBSAssertionDescriptor| "AudioHAL" ID:400-98347-144325 target:98347 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	20:24:39.928947-0500	runningboardd	Assertion 400-98347-144325 (target:[app<application.com.nexy.assistant.55704030.55704039(501)>:98347]) will be created as active
default	20:24:39.933329-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.3408, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=98347, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=392, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	20:24:39.934712-0500	tccd	AUTHREQ_SUBJECT: msgID=401.3408, subject=com.nexy.assistant,
default	20:24:39.935648-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8eed50300 at /Applications/Nexy.app
default	20:24:39.935729-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	20:24:39.940654-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	20:24:39.940730-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant), [mic] Nexy (com.nexy.assistant)]
default	20:24:39.940783-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant", "scr:com.nexy.assistant"]
default	20:24:39.946115-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	20:24:39.946185-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant)]
default	20:24:39.946233-0500	ControlCenter	Active activity attributions changed to ["scr:com.nexy.assistant"]
default	20:24:39.946249-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	20:24:39.958375-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:24:39.958384-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:24:39.958391-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:24:39.958398-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	20:24:39.958508-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	20:24:39.960817-0500	coreaudiod	>>> ADAPT [com.nexy.assistant]
default	20:24:39.962646-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xafa0fd200] Created node ADM::com.nexy.assistant_7690.7540.0_airpods noise suppression studio::in-0 with nodeID 0 - reporting period = 10.000000, sample rate = 24000.000000
default	20:24:39.962716-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xafa0fd200] Created node ADM::com.nexy.assistant_7690.7540.0_airpods noise suppression studio::out-0 with nodeID 1 - reporting period = 10.000000, sample rate = 24000.000000
default	20:24:39.998502-0500	coreaudiod	<<< ADAPT [com.nexy.assistant]
default	20:24:40.999618-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.55704030.55704039(501)>:98347] from originator [osservice<com.apple.powerd>:332] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:400-332-144328 target:98347 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	20:24:40.999682-0500	runningboardd	Assertion 400-332-144328 (target:[app<application.com.nexy.assistant.55704030.55704039(501)>:98347]) will be created as active
default	20:24:40.999804-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:7690 called from <private>
default	20:24:40.999995-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:7690 called from <private>
default	20:24:40.000526-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:7690 called from <private>
default	20:24:40.000581-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	20:24:40.001317-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:7690 called from <private>
default	20:24:40.001416-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(7690)
default	20:24:40.001446-0500	runningboardd	Invalidating assertion 400-332-144328 (target:[app<application.com.nexy.assistant.55704030.55704039(501)>:98347]) from originator [osservice<com.apple.powerd>:332]
default	20:24:40.001435-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:7690 called from <private>
default	20:24:40.001441-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:7690 called from <private>
default	20:24:40.001496-0500	runningboardd	Invalidating assertion 400-98347-144327 (target:[app<application.com.nexy.assistant.55704030.55704039(501)>:98347]) from originator [app<application.com.nexy.assistant.55704030.55704039(501)>:98347]
default	20:24:40.002047-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	20:24:40.002319-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	20:24:40.002660-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(7690)
default	20:24:40.002944-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:7690 called from <private>
default	20:24:40.003438-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.55704030.55704039(501)>:98347] from originator [app<application.com.nexy.assistant.55704030.55704039(501)>:98347] with description <RBSAssertionDescriptor| "AudioHAL" ID:400-98347-144329 target:98347 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	20:24:40.003520-0500	runningboardd	Assertion 400-98347-144329 (target:[app<application.com.nexy.assistant.55704030.55704039(501)>:98347]) will be created as active
default	20:24:40.002957-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:7690 called from <private>
default	20:24:40.002969-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:7690 called from <private>
default	20:24:40.005990-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.3409, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=98347, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=392, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	20:24:40.007714-0500	tccd	AUTHREQ_SUBJECT: msgID=401.3409, subject=com.nexy.assistant,
default	20:24:40.008383-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	20:24:40.008784-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8eed50300 at /Applications/Nexy.app
default	20:24:40.012813-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	20:24:40.012881-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant), [mic] Nexy (com.nexy.assistant)]
default	20:24:40.012927-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant", "scr:com.nexy.assistant"]
default	20:24:40.013158-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:24:40.013168-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:24:40.013178-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:24:40.013184-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:24:40.013190-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:24:40.013196-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	20:24:40.013243-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:24:40.013318-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	20:24:40.013333-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:24:40.013379-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:24:40.013416-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:24:40.013607-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:24:40.013617-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	20:24:40.013645-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:24:40.013653-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:24:40.013660-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:24:40.013668-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:24:40.013691-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:24:40.013710-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	20:24:40.013736-0500	ControlCenter	Navigating to new application [com.nexy.assistant]
default	20:24:40.018013-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	20:24:40.018068-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant)]
default	20:24:40.018140-0500	ControlCenter	Active activity attributions changed to ["scr:com.nexy.assistant"]
default	20:24:40.019023-0500	runningboardd	[app<application.com.nexy.assistant.55704030.55704039(501)>:98347] Ignoring jetsam update because this process is not memory-managed
default	20:24:40.019052-0500	runningboardd	[app<application.com.nexy.assistant.55704030.55704039(501)>:98347] Ignoring suspend because this process is not lifecycle managed
default	20:24:40.019085-0500	runningboardd	[app<application.com.nexy.assistant.55704030.55704039(501)>:98347] Ignoring GPU update because this process is not GPU managed
default	20:24:40.019148-0500	runningboardd	[app<application.com.nexy.assistant.55704030.55704039(501)>:98347] Ignoring memory limit update because this process is not memory-managed
default	20:24:40.027165-0500	ControlCenter	Received state update for 98347 (app<application.com.nexy.assistant.55704030.55704039(501)>, running-active-NotVisible
default	20:24:40.028369-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:24:40.028384-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:24:40.028393-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:24:40.028400-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:24:40.028435-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:24:40.028450-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	20:24:40.028613-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	20:24:40.029717-0500	gamepolicyd	Received state update for 98347 (app<application.com.nexy.assistant.55704030.55704039(501)>, running-active-NotVisible
default	20:24:40.044364-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	20:24:40.049177-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	20:24:40.049237-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant), [mic] Nexy (com.nexy.assistant)]
default	20:24:40.049283-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant", "scr:com.nexy.assistant"]
default	20:24:40.049546-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:24:40.049559-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:24:40.049566-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:24:40.049576-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:24:40.049582-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:24:40.049588-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	20:24:40.049657-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:24:40.049691-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:24:40.049727-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	20:24:40.049750-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:24:40.049782-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:24:40.049814-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:24:40.049844-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	20:24:40.049870-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:24:40.049877-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:24:40.049884-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:24:40.049889-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:24:40.049912-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:24:40.049918-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	20:24:40.049945-0500	ControlCenter	Navigating to new application [com.nexy.assistant]
default	20:24:40.129116-0500	ControlCenter	Received state update for 98347 (app<application.com.nexy.assistant.55704030.55704039(501)>, running-active-NotVisible
default	20:24:40.129429-0500	gamepolicyd	Received state update for 98347 (app<application.com.nexy.assistant.55704030.55704039(501)>, running-active-NotVisible
default	20:24:42.702363-0500	Nexy	[com.apple.controlcenter:449CC7F2-8D7E-4BE0-8DBE-31E5C2A1CFEE] Sending action(s) in update: NSSceneFenceAction
default	20:24:43.447443-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xa}
default	20:24:43.448097-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1f40af","name":"Nexy(98347)"}, "details":{"deviceUIDs":[],"implicit_category":"","input_running":false,"output_running":false} }
default	20:24:43.448257-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 175, PID = 98347, Name = sid:0x1f40af, Nexy(98347), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	20:24:43.448331-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 175, PID = 98347, Name = sid:0x1f40af, Nexy(98347), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	20:24:43.448466-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	20:24:43.448468-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1f40af, Nexy(98347), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 175 stopping recording
default	20:24:43.448493-0500	audiomxd	-MXCoreSession- -[MXCoreSession endInterruption:]: Session <ID: 175, PID = 98347, Name = sid:0x1f40af, Nexy(98347), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> is going inactive
default	20:24:43.448556-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 175, PID = 98347, Name = sid:0x1f40af, Nexy(98347), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	20:24:43.448642-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 175, PID = 98347, Name = sid:0x1f40af, Nexy(98347), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	20:24:43.448961-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 200 flag 0x1 < Hijack > app com.nexy.assistant CID 0x91550001 category Not set
default	20:24:43.448952-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 0]. BT device UIDS: {(
)}
default	20:24:43.449542-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	20:24:43.449573-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	20:24:43.451276-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	20:24:43.451486-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:24:43.451742-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:24:43.451756-0500	audioaccessoryd	AudioStateChanged: Removed audio session app com.nexy.assistant 201 count 3
default	20:24:43.448998-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	20:24:43.451324-0500	runningboardd	Invalidating assertion 400-98347-144329 (target:[app<application.com.nexy.assistant.55704030.55704039(501)>:98347]) from originator [app<application.com.nexy.assistant.55704030.55704039(501)>:98347]
default	20:24:43.449357-0500	audiomxd	UpdateAudioState CID 0x91550001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	20:24:43.449461-0500	audiomxd	UpdateAudioState CID 0x91550001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:24:43.451426-0500	runningboardd	Invalidating assertion 400-332-144330 (target:[app<application.com.nexy.assistant.55704030.55704039(501)>:98347]) from originator [osservice<com.apple.powerd>:332]
default	20:24:43.461267-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	20:24:43.461410-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant)]
default	20:24:43.461489-0500	ControlCenter	Active activity attributions changed to ["scr:com.nexy.assistant"]
default	20:24:43.461508-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	20:24:43.462384-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:24:43.462404-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:24:43.462419-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:24:43.462426-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:24:43.462435-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:24:43.462444-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	20:24:43.462704-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	20:24:43.471476-0500	Nexy	nw_path_libinfo_path_check [3EE04601-9338-4390-85CA-A6F78BC82BFF Hostname#cc1c3c92:80 tcp, legacy-socket, attribution: developer]
	libinfo check path: <private>
default	20:24:43.471654-0500	mDNSResponder	[R152534] DNSServiceQueryRecord START -- qname: <mask.hash: 'WYUTXafykb7b/ZdEN+VCdQ=='>, qtype: A, flags: 0x1D000, interface index: 0, client pid: 98347 (Nexy), name hash: b360ab20
default	20:24:43.472527-0500	mDNSResponder	[R152535] DNSServiceQueryRecord START -- qname: <mask.hash: 'WYUTXafykb7b/ZdEN+VCdQ=='>, qtype: AAAA, flags: 0x1D000, interface index: 0, client pid: 98347 (Nexy), name hash: b360ab20
default	20:24:43.473439-0500	kernel	SK[6]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 98AEBA34-5718-4534-8C3D-A32AD2E56748 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.61586,dst=<IPv4-redacted>.80,proto=0x06 mask=0x0000003f,hash=0x64d6f8e0 tp_proto=0x06"
default	20:24:43.473553-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:61586<-><IPv4-redacted>:80] interface: en0 (skipped: 196)
so_gencnt: 8780103 t_state: SYN_SENT process: Nexy:98347 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xabb5a52c
default	20:24:43.478385-0500	kernel	tcp connected: [<IPv4-redacted>:61586<-><IPv4-redacted>:80] interface: en0 (skipped: 196)
so_gencnt: 8780103 t_state: ESTABLISHED process: Nexy:98347 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xabb5a52c
default	20:24:43.507742-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	20:24:43.507842-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant)]
default	20:24:43.548474-0500	Nexy	                AUHAL.cpp:473   ~AUHAL: (0xc7e9eaa40) Selecting device 0 from destructor
default	20:24:43.548491-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0xc7e9eaa40)
default	20:24:43.548499-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0xc7e9eaa40) not already running
default	20:24:43.548502-0500	Nexy	                AUHAL.cpp:687   SelectDevice: (0xc7e9eaa40) disconnecting device 91
default	20:24:43.548510-0500	Nexy	                AUHAL.cpp:751   SelectDevice: (0xc7e9eaa40) destroying ioproc 0xa for device 91
default	20:24:43.548557-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xa}
default	20:24:43.548621-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	20:24:43.548814-0500	Nexy	                AUHAL.cpp:853   SelectDevice: (0xc7e9eaa40) nothing to setup
default	20:24:43.548827-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0xc7e9eaa40) adding 0 device listeners to device 0
default	20:24:43.548842-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0xc7e9eaa40) adding 0 device delegate listeners to device 0
default	20:24:43.548866-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0xc7e9eaa40) removing 7 device listeners from device 91
default	20:24:43.549139-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0xc7e9eaa40) removing 0 device delegate listeners from device 91
default	20:24:43.549164-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0xc7e9eaa40)
default	20:24:43.557956-0500	runningboardd	[app<application.com.nexy.assistant.55704030.55704039(501)>:98347] Ignoring jetsam update because this process is not memory-managed
default	20:24:43.557969-0500	runningboardd	[app<application.com.nexy.assistant.55704030.55704039(501)>:98347] Ignoring suspend because this process is not lifecycle managed
default	20:24:43.557979-0500	runningboardd	[app<application.com.nexy.assistant.55704030.55704039(501)>:98347] Ignoring GPU update because this process is not GPU managed
default	20:24:43.557998-0500	runningboardd	[app<application.com.nexy.assistant.55704030.55704039(501)>:98347] Ignoring memory limit update because this process is not memory-managed
default	20:24:43.561147-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.55704030.55704039(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:24:43.561778-0500	ControlCenter	Received state update for 98347 (app<application.com.nexy.assistant.55704030.55704039(501)>, running-active-NotVisible
default	20:24:43.561981-0500	gamepolicyd	Received state update for 98347 (app<application.com.nexy.assistant.55704030.55704039(501)>, running-active-NotVisible
default	20:24:43.772588-0500	kernel	tcp_connection_summary (tcp_usrclosed:3220)[<IPv4-redacted>:61586<-><IPv4-redacted>:80] interface: en0 (skipped: 196)
so_gencnt: 8780103 t_state: LAST_ACK process: Nexy:98347 Duration: 0.299 sec Conn_Time: 0.005 sec bytes in/out: 398/32869 pkts in/out: 3/8 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 5.250 ms rttvar: 0.437 ms base rtt: 5 ms so_error: 0 svc/tc: 0 flow: 0xabb5a52c
default	20:24:43.772612-0500	kernel	tcp_connection_summary [<IPv4-redacted>:61586<-><IPv4-redacted>:80] interface: en0 (skipped: 196)
so_gencnt: 8780103 t_state: LAST_ACK process: Nexy:98347 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 1/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	20:24:43.788211-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0xc7b651980, from  2 ch,  48000 Hz, Float32, deinterleaved to  2 ch,  24000 Hz, Float32, interleaved
default	20:24:43.788256-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	20:24:43.788749-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	20:24:43.789679-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0xc7b6519e0, from  2 ch,  24000 Hz, Float32, deinterleaved to  2 ch,  24000 Hz, Float32, interleaved
default	20:24:43.789693-0500	Nexy	       AudioConverter.cpp:1317  AudioConverter -> 0xc7b6519e0: The in-process GetProperty call returned 1886547824 for property 1886546285 with size 8.
default	20:24:43.789700-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	20:24:43.789705-0500	Nexy	AudioConverter -> 0xc7b6519e0: The in-process SetProperty call returned 1886547824 for property 1936876385 with size 4.
default	20:24:43.789717-0500	Nexy	AudioConverter -> 0xc7b6519e0: The in-process SetProperty call returned 1886547824 for property 1936876401 with size 4.
default	20:24:43.789724-0500	Nexy	AudioConverter -> 0xc7b6519e0: The in-process SetProperty call returned 1886547824 for property 1886547309 with size 4.
default	20:24:43.790760-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0xc7b650ea0, from  2 ch,  24000 Hz, Float32, deinterleaved to  2 ch,  24000 Hz, Float32, interleaved
default	20:24:43.790774-0500	Nexy	AudioConverter -> 0xc7b650ea0: The in-process SetProperty call returned 1886547824 for property 1936876385 with size 4.
default	20:24:43.790781-0500	Nexy	AudioConverter -> 0xc7b650ea0: The in-process SetProperty call returned 1886547824 for property 1936876401 with size 4.
default	20:24:43.790779-0500	Nexy	       AudioConverter.cpp:1317  AudioConverter -> 0xc7b650ea0: The in-process GetProperty call returned 1886547824 for property 1886546285 with size 8.
default	20:24:43.790786-0500	Nexy	AudioConverter -> 0xc7b650ea0: The in-process SetProperty call returned 1886547824 for property 1886547309 with size 4.
default	20:24:43.790791-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	20:24:43.790997-0500	Nexy	       AudioConverter.cpp:1317  AudioConverter -> 0xc7b650ea0: The in-process GetProperty call returned 1886547824 for property 1886546285 with size 8.
default	20:24:43.791203-0500	Nexy	         AVAudioEngine.mm:1182  Engine@0xc7c35c600: start, was running 0
default	20:24:43.793796-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xa}
default	20:24:43.793889-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.55704030.55704039(501)>:98347] from originator [app<application.com.nexy.assistant.55704030.55704039(501)>:98347] with description <RBSAssertionDescriptor| "AudioHAL" ID:400-98347-144333 target:98347 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	20:24:43.793975-0500	runningboardd	Assertion 400-98347-144333 (target:[app<application.com.nexy.assistant.55704030.55704039(501)>:98347]) will be created as active
default	20:24:43.794617-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1f40af","name":"Nexy(98347)"}, "details":{"deviceUIDs":["1C-77-54-18-C8-A3:output"],"implicit_category":"MediaPlayback","input_running":false,"output_running":true} }
default	20:24:43.794540-0500	runningboardd	[app<application.com.nexy.assistant.55704030.55704039(501)>:98347] Ignoring jetsam update because this process is not memory-managed
default	20:24:43.794538-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.55704030.55704039(501)>:98347] from originator [osservice<com.apple.powerd>:332] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:400-332-144334 target:98347 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	20:24:43.794552-0500	runningboardd	[app<application.com.nexy.assistant.55704030.55704039(501)>:98347] Ignoring suspend because this process is not lifecycle managed
default	20:24:43.794639-0500	runningboardd	Assertion 400-332-144334 (target:[app<application.com.nexy.assistant.55704030.55704039(501)>:98347]) will be created as active
default	20:24:43.794653-0500	runningboardd	[app<application.com.nexy.assistant.55704030.55704039(501)>:98347] Ignoring GPU update because this process is not GPU managed
default	20:24:43.794717-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 175, PID = 98347, Name = sid:0x1f40af, Nexy(98347), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	20:24:43.794744-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Category/Mode changed -- The score for sid:0x1f40af, Nexy(98347), 'prim'/com.nexy.assistant was not correct. Old score = 201
default	20:24:43.794789-0500	runningboardd	[app<application.com.nexy.assistant.55704030.55704039(501)>:98347] Ignoring memory limit update because this process is not memory-managed
default	20:24:43.794774-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 175, PID = 98347, Name = sid:0x1f40af, Nexy(98347), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	20:24:43.794837-0500	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1f40af, Nexy(98347), 'prim'', AudioCategory changed to 'MediaPlayback'
default	20:24:43.794892-0500	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 175, PID = 98347, Name = sid:0x1f40af, Nexy(98347), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO> is going active
default	20:24:43.794950-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsPlaying:]: MXCoreSession com.nexy.assistant with category/mode MediaPlayback/Default and coreSessionID = 175 starting playing
default	20:24:43.794913-0500	audiomxd	UpdateAudioState CID 0x91550001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:24:43.795094-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 175, PID = 98347, Name = sid:0x1f40af, Nexy(98347), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	20:24:43.795185-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 175, PID = 98347, Name = sid:0x1f40af, Nexy(98347), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO>
default	20:24:43.795283-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:24:43.795324-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:24:43.795407-0500	audiomxd	AudioApplicationInfoImpl.mm:395   Successfully updated session 0x1f40af to isSessionRecording: 0
	app: {"name":"[implicit] Nexy","pid":98347}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1f40af, sessionType: 'prim', isRecording: false }, 
]
default	20:24:43.795377-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 201, deviceID = <private>
default	20:24:43.795651-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 1]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)}
default	20:24:43.795708-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 201 flag 0x1 < Hijack > app com.nexy.assistant CID 0x91550001 category Not set
default	20:24:43.795663-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	20:24:43.796041-0500	audiomxd	UpdateAudioState CID 0x91550001 audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	20:24:43.796156-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 201,
}
default	20:24:43.796194-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	20:24:43.796210-0500	audioaccessoryd	AudioStateChanged: Added audio session app com.nexy.assistant NULL -> 201 count 4
default	20:24:43.796231-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 201
default	20:24:43.798623-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.55704030.55704039(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:24:43.798924-0500	runningboardd	[app<application.com.nexy.assistant.55704030.55704039(501)>:98347] Ignoring jetsam update because this process is not memory-managed
default	20:24:43.798953-0500	runningboardd	[app<application.com.nexy.assistant.55704030.55704039(501)>:98347] Ignoring suspend because this process is not lifecycle managed
default	20:24:43.799115-0500	ControlCenter	Received state update for 98347 (app<application.com.nexy.assistant.55704030.55704039(501)>, running-active-NotVisible
default	20:24:43.798980-0500	runningboardd	[app<application.com.nexy.assistant.55704030.55704039(501)>:98347] Ignoring GPU update because this process is not GPU managed
default	20:24:43.799027-0500	runningboardd	[app<application.com.nexy.assistant.55704030.55704039(501)>:98347] Ignoring memory limit update because this process is not memory-managed
default	20:24:43.799278-0500	gamepolicyd	Received state update for 98347 (app<application.com.nexy.assistant.55704030.55704039(501)>, running-active-NotVisible
default	20:24:43.801975-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.55704030.55704039(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:24:43.802366-0500	ControlCenter	Received state update for 98347 (app<application.com.nexy.assistant.55704030.55704039(501)>, running-active-NotVisible
default	20:24:43.802503-0500	gamepolicyd	Received state update for 98347 (app<application.com.nexy.assistant.55704030.55704039(501)>, running-active-NotVisible
default	20:24:43.822289-0500	Nexy	[com.apple.controlcenter:449CC7F2-8D7E-4BE0-8DBE-31E5C2A1CFEE] Sending action(s) in update: NSSceneFenceAction
default	20:24:45.458317-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	20:24:45.458426-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant)]
default	20:24:45.575376-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(7696)
default	20:24:45.575490-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:7696 called from <private>
default	20:24:45.575510-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:7696 called from <private>
default	20:24:45.576788-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(7689)
default	20:24:45.578252-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:7689 called from <private>
default	20:24:45.578280-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:7689 called from <private>
default	20:24:45.580677-0500	runningboardd	Invalidating assertion 400-98347-144333 (target:[app<application.com.nexy.assistant.55704030.55704039(501)>:98347]) from originator [app<application.com.nexy.assistant.55704030.55704039(501)>:98347]
default	20:24:45.579210-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(7696)
default	20:24:45.579289-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(7690)
default	20:24:45.580054-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:7696 called from <private>
default	20:24:45.581093-0500	runningboardd	Invalidating assertion 400-332-144334 (target:[app<application.com.nexy.assistant.55704030.55704039(501)>:98347]) from originator [osservice<com.apple.powerd>:332]
default	20:24:45.580111-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:7690 called from <private>
default	20:24:45.580125-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:7696 called from <private>
default	20:24:45.580166-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:7690 called from <private>
default	20:24:45.585760-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	20:24:45.598995-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:7689 called from <private>
default	20:24:45.599037-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:7689 called from <private>
default	20:24:45.599180-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(7689)
default	20:24:45.599200-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:7689 called from <private>
default	20:24:45.599206-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:7689 called from <private>
default	20:24:45.599664-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(7696)
default	20:24:45.599694-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:7696 called from <private>
default	20:24:45.599693-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(7690)
default	20:24:45.599700-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:7696 called from <private>
default	20:24:45.599716-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:7690 called from <private>
default	20:24:45.599724-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:7690 called from <private>
default	20:24:45.604083-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(7689)
default	20:24:45.604135-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(7689)
default	20:24:45.604494-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:7689 called from <private>
default	20:24:45.604505-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:7689 called from <private>
default	20:24:45.604531-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:7689 called from <private>
default	20:24:45.604542-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:7689 called from <private>
default	20:24:45.604549-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:7689 called from <private>
default	20:24:45.606093-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(7689)
error	20:24:45.606424-0500	Nexy	         HALC_ProxyIOContext.cpp:1075  HALC_ProxyIOContext::_StartIO(): Start failed - StartAndWaitForState returned error 35
default	20:24:45.606456-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:7689 called from <private>
default	20:24:45.606496-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:7689 called from <private>
default	20:24:45.606568-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:7689 called from <private>
default	20:24:45.609915-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:7689 called from <private>
default	20:24:45.609184-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.55704030.55704039(501)>:98347] from originator [app<application.com.nexy.assistant.55704030.55704039(501)>:98347] with description <RBSAssertionDescriptor| "AudioHAL" ID:400-98347-144336 target:98347 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	20:24:45.609452-0500	runningboardd	Assertion 400-98347-144336 (target:[app<application.com.nexy.assistant.55704030.55704039(501)>:98347]) will be created as active
default	20:24:45.609949-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:7689 called from <private>
default	20:24:45.610194-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(7689)
default	20:24:45.610352-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:7689 called from <private>
default	20:24:45.610362-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:7689 called from <private>
default	20:24:45.612756-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(7689)
default	20:24:45.612934-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(7689)
default	20:24:45.614268-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(7689)
default	20:24:45.614687-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:7689 called from <private>
default	20:24:45.614726-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:7689 called from <private>
default	20:24:45.614953-0500	runningboardd	Invalidating assertion 400-98347-144336 (target:[app<application.com.nexy.assistant.55704030.55704039(501)>:98347]) from originator [app<application.com.nexy.assistant.55704030.55704039(501)>:98347]
default	20:24:45.614864-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:7689 called from <private>
default	20:24:45.614928-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:7689 called from <private>
default	20:24:45.614962-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:7689 called from <private>
default	20:24:45.617882-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:7696 called from <private>
default	20:24:45.617913-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:7696 called from <private>
default	20:24:45.619832-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	20:24:45.618115-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(7696)
error	20:24:45.618204-0500	Nexy	         HALC_ProxyIOContext.cpp:1075  HALC_ProxyIOContext::_StartIO(): Start failed - StartAndWaitForState returned error 35
default	20:24:45.620050-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	20:24:45.618215-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:7689 called from <private>
default	20:24:45.619798-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.55704030.55704039(501)>:98347] from originator [app<application.com.nexy.assistant.55704030.55704039(501)>:98347] with description <RBSAssertionDescriptor| "AudioHAL" ID:400-98347-144338 target:98347 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	20:24:45.619937-0500	runningboardd	Assertion 400-98347-144338 (target:[app<application.com.nexy.assistant.55704030.55704039(501)>:98347]) will be created as active
default	20:24:45.618222-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:7689 called from <private>
default	20:24:45.618230-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:7689 called from <private>
default	20:24:45.621051-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(7696)
default	20:24:45.621092-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(7696)
default	20:24:45.621167-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(7696)
default	20:24:45.621216-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(7696)
default	20:24:45.621280-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(7696)
default	20:24:45.621598-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:7696 called from <private>
default	20:24:45.621609-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:7696 called from <private>
default	20:24:45.621653-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:7696 called from <private>
default	20:24:45.621695-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:7696 called from <private>
default	20:24:45.621761-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:7696 called from <private>
default	20:24:45.621844-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:7696 called from <private>
default	20:24:45.621963-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:7696 called from <private>
default	20:24:45.622035-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:7696 called from <private>
default	20:24:45.622091-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:7696 called from <private>
default	20:24:45.622132-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:7696 called from <private>
default	20:24:45.622184-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:7696 called from <private>
default	20:24:45.622270-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:7696 called from <private>
default	20:24:45.622355-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:7696 called from <private>
default	20:24:45.622459-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:7696 called from <private>
default	20:24:45.622481-0500	runningboardd	Invalidating assertion 400-98347-144338 (target:[app<application.com.nexy.assistant.55704030.55704039(501)>:98347]) from originator [app<application.com.nexy.assistant.55704030.55704039(501)>:98347]
default	20:24:45.688826-0500	runningboardd	[app<application.com.nexy.assistant.55704030.55704039(501)>:98347] Ignoring jetsam update because this process is not memory-managed
default	20:24:45.688836-0500	runningboardd	[app<application.com.nexy.assistant.55704030.55704039(501)>:98347] Ignoring suspend because this process is not lifecycle managed
default	20:24:45.688846-0500	runningboardd	[app<application.com.nexy.assistant.55704030.55704039(501)>:98347] Ignoring GPU update because this process is not GPU managed
default	20:24:45.688875-0500	runningboardd	[app<application.com.nexy.assistant.55704030.55704039(501)>:98347] Ignoring memory limit update because this process is not memory-managed
default	20:24:45.691572-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.55704030.55704039(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:24:45.691951-0500	ControlCenter	Received state update for 98347 (app<application.com.nexy.assistant.55704030.55704039(501)>, running-active-NotVisible
default	20:24:45.692171-0500	gamepolicyd	Received state update for 98347 (app<application.com.nexy.assistant.55704030.55704039(501)>, running-active-NotVisible
default	20:24:46.238420-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.55704030.55704039(501)>:98347] from originator [osservice<com.apple.powerd>:332] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:400-332-144344 target:98347 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	20:24:46.238517-0500	runningboardd	Assertion 400-332-144344 (target:[app<application.com.nexy.assistant.55704030.55704039(501)>:98347]) will be created as active
default	20:24:46.238807-0500	runningboardd	[app<application.com.nexy.assistant.55704030.55704039(501)>:98347] Ignoring jetsam update because this process is not memory-managed
default	20:24:46.238818-0500	runningboardd	[app<application.com.nexy.assistant.55704030.55704039(501)>:98347] Ignoring suspend because this process is not lifecycle managed
default	20:24:46.238851-0500	runningboardd	[app<application.com.nexy.assistant.55704030.55704039(501)>:98347] Ignoring GPU update because this process is not GPU managed
default	20:24:46.238940-0500	runningboardd	[app<application.com.nexy.assistant.55704030.55704039(501)>:98347] Ignoring memory limit update because this process is not memory-managed
default	20:24:46.245501-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.55704030.55704039(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:24:46.246634-0500	ControlCenter	Received state update for 98347 (app<application.com.nexy.assistant.55704030.55704039(501)>, running-active-NotVisible
default	20:24:46.248775-0500	gamepolicyd	Received state update for 98347 (app<application.com.nexy.assistant.55704030.55704039(501)>, running-active-NotVisible
default	20:24:46.276390-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:7689 called from <private>
default	20:24:46.276478-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:7689 called from <private>
default	20:24:46.279315-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:7689 called from <private>
default	20:24:46.279365-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:7689 called from <private>
default	20:24:46.281089-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0xc7b650a20, from  2 ch,  24000 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	20:24:46.281116-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	20:24:46.283129-0500	runningboardd	Invalidating assertion 400-98347-144340 (target:[app<application.com.nexy.assistant.55704030.55704039(501)>:98347]) from originator [app<application.com.nexy.assistant.55704030.55704039(501)>:98347]
default	20:24:46.284187-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.55704030.55704039(501)>:98347] from originator [app<application.com.nexy.assistant.55704030.55704039(501)>:98347] with description <RBSAssertionDescriptor| "AudioHAL" ID:400-98347-144346 target:98347 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	20:24:46.284293-0500	runningboardd	Assertion 400-98347-144346 (target:[app<application.com.nexy.assistant.55704030.55704039(501)>:98347]) will be created as active
default	20:24:46.285751-0500	runningboardd	Invalidating assertion 400-332-144344 (target:[app<application.com.nexy.assistant.55704030.55704039(501)>:98347]) from originator [osservice<com.apple.powerd>:332]
default	20:24:46.285989-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.55704030.55704039(501)>:98347] from originator [osservice<com.apple.powerd>:332] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:400-332-144347 target:98347 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	20:24:46.286117-0500	runningboardd	Assertion 400-332-144347 (target:[app<application.com.nexy.assistant.55704030.55704039(501)>:98347]) will be created as active
default	20:24:46.285177-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	20:24:46.891618-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:7689 called from <private>
default	20:24:46.891793-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xa}
default	20:24:46.892339-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 1]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:24:46.892538-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0xc7e9ea340) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	20:24:46.892565-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0xc7e9ea340) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	20:24:46.892573-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	20:24:46.893198-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 201
default	20:24:46.892815-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0xc7e9ea340) Device ID: 85 (Input:No | Output:Yes): true
default	20:24:46.892827-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0xc7e9ea340)
default	20:24:46.892911-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  48000 Hz, Float32, interleaved
default	20:24:46.892921-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	20:24:46.892946-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	20:24:46.892997-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	20:24:46.893030-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	20:24:46.893562-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0xc7b650ea0, from  2 ch,  24000 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	20:24:46.893599-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	20:24:46.893712-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xa}
default	20:24:46.894092-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 1]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)} Server update was not required.
default	20:24:46.894253-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0xc7e9ea340) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	20:24:46.894283-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0xc7e9ea340) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	20:24:46.894290-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	20:24:46.895154-0500	Nexy	         AVAudioEngine.mm:1461  Engine@0xc7c35c600: iounit configuration changed > stopping the engine
default	20:24:46.895178-0500	Nexy	         AVAudioEngine.mm:1236  Engine@0xc7c35c600: stop, was running 1
default	20:24:46.895188-0500	Nexy	         AVAudioEngine.mm:1219  Engine@0xc7c35c600: pause, was running 1
default	20:24:46.901725-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Output {1C-77-54-18-C8-A3:output, 0xa}
default	20:24:46.902077-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1f40af","name":"Nexy(98347)"}, "details":{"deviceUIDs":[],"implicit_category":"","input_running":false,"output_running":false} }
default	20:24:46.902206-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsPlaying:]: MXCoreSession com.nexy.assistant with category/mode MediaPlayback/Default and coreSessionID = 175 stopping playing
default	20:24:46.902259-0500	audiomxd	-MXCoreSession- -[MXCoreSession endInterruption:]: Session <ID: 175, PID = 98347, Name = sid:0x1f40af, Nexy(98347), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> is going inactive
default	20:24:46.902292-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 175, PID = 98347, Name = sid:0x1f40af, Nexy(98347), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	20:24:46.902378-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 175, PID = 98347, Name = sid:0x1f40af, Nexy(98347), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	20:24:46.902771-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 0]. BT device UIDS: {(
)}
default	20:24:46.902781-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	20:24:46.903706-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:24:46.903472-0500	runningboardd	Invalidating assertion 400-98347-144346 (target:[app<application.com.nexy.assistant.55704030.55704039(501)>:98347]) from originator [app<application.com.nexy.assistant.55704030.55704039(501)>:98347]
default	20:24:46.903765-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:24:46.902662-0500	audiomxd	AudioApplicationInfoImpl.mm:395   Successfully updated session 0x1f40af to isSessionRecording: 0
	app: {"name":"[implicit] Nexy","pid":98347}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1f40af, sessionType: 'prim', isRecording: false }, 
]
default	20:24:46.903789-0500	audioaccessoryd	AudioStateChanged: Removed audio session app com.nexy.assistant 201 count 2
default	20:24:46.903572-0500	runningboardd	Invalidating assertion 400-332-144347 (target:[app<application.com.nexy.assistant.55704030.55704039(501)>:98347]) from originator [osservice<com.apple.powerd>:332]
default	20:24:46.903386-0500	audiomxd	UpdateAudioState CID 0x91550001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:24:46.998372-0500	runningboardd	[app<application.com.nexy.assistant.55704030.55704039(501)>:98347] Ignoring jetsam update because this process is not memory-managed
default	20:24:46.998394-0500	runningboardd	[app<application.com.nexy.assistant.55704030.55704039(501)>:98347] Ignoring suspend because this process is not lifecycle managed
default	20:24:46.998404-0500	runningboardd	[app<application.com.nexy.assistant.55704030.55704039(501)>:98347] Ignoring GPU update because this process is not GPU managed
default	20:24:46.998456-0500	runningboardd	[app<application.com.nexy.assistant.55704030.55704039(501)>:98347] Ignoring memory limit update because this process is not memory-managed
default	20:24:47.002113-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.55704030.55704039(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:24:47.002686-0500	ControlCenter	Received state update for 98347 (app<application.com.nexy.assistant.55704030.55704039(501)>, running-active-NotVisible
default	20:24:47.002862-0500	gamepolicyd	Received state update for 98347 (app<application.com.nexy.assistant.55704030.55704039(501)>, running-active-NotVisible
default	20:24:47.020957-0500	Nexy	         AVAudioEngine.mm:1437  Engine@0xc7c35c600: iounit configuration changed > posting notification
default	20:24:55.527421-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	20:24:55.527522-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant)]
default	20:24:55.684619-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	20:24:55.684679-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant)]
default	20:24:59.825213-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant", "scr:com.nexy.assistant"]
default	20:24:59.826909-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:24:59.826931-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:24:59.826975-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:24:59.826991-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:24:59.827003-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:24:59.827017-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	20:24:59.827189-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	20:25:03.462444-0500	ControlCenter	Recent activity attributions changed to ["scr:com.nexy.assistant"]
default	20:25:04.494930-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.55704030.55704039(501)>:98347] from originator [osservice<com.apple.controlcenter(501)>:615] with description <RBSAssertionDescriptor| "FBWorkspace (BG-Active[40])" ID:400-615-144442 target:98347 attributes:[
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableLPRunReason-Suspend" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableRole-NonUI" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableJetsamPriority-Active" sourceEnvironment:"(null)">
	]>
default	20:25:04.495162-0500	runningboardd	Assertion 400-615-144442 (target:[app<application.com.nexy.assistant.55704030.55704039(501)>:98347]) will be created as active
default	20:25:04.495400-0500	ControlCenter	[app<application.com.nexy.assistant.55704030.55704039>:98347] Workspace state did change: XX-None[0] --> BG-Active[40] (assertion acquired).
default	20:25:04.495733-0500	runningboardd	[app<application.com.nexy.assistant.55704030.55704039(501)>:98347] Ignoring jetsam update because this process is not memory-managed
default	20:25:04.495754-0500	runningboardd	[app<application.com.nexy.assistant.55704030.55704039(501)>:98347] Ignoring suspend because this process is not lifecycle managed
default	20:25:04.495773-0500	runningboardd	[app<application.com.nexy.assistant.55704030.55704039(501)>:98347] Ignoring GPU update because this process is not GPU managed
default	20:25:04.495822-0500	runningboardd	[app<application.com.nexy.assistant.55704030.55704039(501)>:98347] Ignoring memory limit update because this process is not memory-managed
default	20:25:04.500921-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.55704030.55704039(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:25:04.501849-0500	ControlCenter	Received state update for 98347 (app<application.com.nexy.assistant.55704030.55704039(501)>, running-active-NotVisible
default	20:25:04.502356-0500	gamepolicyd	Received state update for 98347 (app<application.com.nexy.assistant.55704030.55704039(501)>, running-active-NotVisible
default	20:25:04.599675-0500	ControlCenter	[app<application.com.nexy.assistant.55704030.55704039>:98347] Workspace state did change: BG-Active[40] --> XX-None[0] (assertion dropped).
default	20:25:04.599858-0500	runningboardd	Invalidating assertion 400-615-144442 (target:[app<application.com.nexy.assistant.55704030.55704039(501)>:98347]) from originator [osservice<com.apple.controlcenter(501)>:615]
default	20:25:04.707979-0500	runningboardd	[app<application.com.nexy.assistant.55704030.55704039(501)>:98347] Ignoring jetsam update because this process is not memory-managed
default	20:25:04.708017-0500	runningboardd	[app<application.com.nexy.assistant.55704030.55704039(501)>:98347] Ignoring suspend because this process is not lifecycle managed
default	20:25:04.708045-0500	runningboardd	[app<application.com.nexy.assistant.55704030.55704039(501)>:98347] Ignoring GPU update because this process is not GPU managed
default	20:25:04.708117-0500	runningboardd	[app<application.com.nexy.assistant.55704030.55704039(501)>:98347] Ignoring memory limit update because this process is not memory-managed
default	20:25:04.712424-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.55704030.55704039(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:25:04.712765-0500	ControlCenter	Received state update for 98347 (app<application.com.nexy.assistant.55704030.55704039(501)>, running-active-NotVisible
default	20:25:04.714190-0500	gamepolicyd	Received state update for 98347 (app<application.com.nexy.assistant.55704030.55704039(501)>, running-active-NotVisible
default	20:25:06.623037-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.55704030.55704039(501)>:98347] from originator [osservice<com.apple.controlcenter(501)>:615] with description <RBSAssertionDescriptor| "FBWorkspace (BG-Active[40])" ID:400-615-144466 target:98347 attributes:[
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableLPRunReason-Suspend" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableRole-NonUI" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableJetsamPriority-Active" sourceEnvironment:"(null)">
	]>
default	20:25:06.623205-0500	runningboardd	Assertion 400-615-144466 (target:[app<application.com.nexy.assistant.55704030.55704039(501)>:98347]) will be created as active
default	20:25:06.623353-0500	ControlCenter	[app<application.com.nexy.assistant.55704030.55704039>:98347] Workspace state did change: XX-None[0] --> BG-Active[40] (assertion acquired).
default	20:25:06.624756-0500	runningboardd	[app<application.com.nexy.assistant.55704030.55704039(501)>:98347] Ignoring jetsam update because this process is not memory-managed
default	20:25:06.624916-0500	runningboardd	[app<application.com.nexy.assistant.55704030.55704039(501)>:98347] Ignoring suspend because this process is not lifecycle managed
default	20:25:06.624973-0500	runningboardd	[app<application.com.nexy.assistant.55704030.55704039(501)>:98347] Ignoring GPU update because this process is not GPU managed
default	20:25:06.625102-0500	runningboardd	[app<application.com.nexy.assistant.55704030.55704039(501)>:98347] Ignoring memory limit update because this process is not memory-managed
default	20:25:06.632991-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.55704030.55704039(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:25:06.728984-0500	ControlCenter	[app<application.com.nexy.assistant.55704030.55704039>:98347] Workspace state did change: BG-Active[40] --> XX-None[0] (assertion dropped).
default	20:25:06.729336-0500	runningboardd	Invalidating assertion 400-615-144466 (target:[app<application.com.nexy.assistant.55704030.55704039(501)>:98347]) from originator [osservice<com.apple.controlcenter(501)>:615]
default	20:25:06.838190-0500	runningboardd	[app<application.com.nexy.assistant.55704030.55704039(501)>:98347] Ignoring jetsam update because this process is not memory-managed
default	20:25:06.838210-0500	runningboardd	[app<application.com.nexy.assistant.55704030.55704039(501)>:98347] Ignoring suspend because this process is not lifecycle managed
default	20:25:06.838238-0500	runningboardd	[app<application.com.nexy.assistant.55704030.55704039(501)>:98347] Ignoring GPU update because this process is not GPU managed
default	20:25:06.838278-0500	runningboardd	[app<application.com.nexy.assistant.55704030.55704039(501)>:98347] Ignoring memory limit update because this process is not memory-managed
default	20:25:06.841772-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.55704030.55704039(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:25:06.842005-0500	ControlCenter	Received state update for 98347 (app<application.com.nexy.assistant.55704030.55704039(501)>, running-active-NotVisible
default	20:25:06.842396-0500	gamepolicyd	Received state update for 98347 (app<application.com.nexy.assistant.55704030.55704039(501)>, running-active-NotVisible
default	20:25:11.569740-0500	WindowServer	1315f3[StealKeyFocusReturningID]: [DeferringManager] Updating policy {
    advicePolicy: .keyThief;
    frontmostProcess: 0x0-0x14014 (Finder) mainConnectionID: 59907;
    keyThiefConnectionID: 1315F3;
} for reason: key thief updated 1315f3 0x0-0x75f75f (Nexy)
default	20:25:11.569823-0500	WindowServer	<BSCompoundAssertion:0x830c11400> (com.apple.backboard.hid.delivery.localDelivery.preventFlushing) acquire for reason:key thief updated 1315f3 0x0-0x75f75f (Nexy) <5740> acq:0x833ab9160 count:1
default	20:25:12.565839-0500	WindowServer	destinations for Keyboard event: (<keyboardFocus; Nexy.98347>)
default	20:25:12.685600-0500	WindowServer	destinations for Keyboard event: (<keyboardFocus; Nexy.98347>)
default	20:25:12.796854-0500	WindowServer	destinations for Keyboard event: (<keyboardFocus; Nexy.98347>)
default	20:25:12.866602-0500	WindowServer	destinations for Keyboard event: (<keyboardFocus; Nexy.98347>)
default	20:25:12.969059-0500	WindowServer	destinations for Keyboard event: (<keyboardFocus; Nexy.98347>)
default	20:25:13.031337-0500	WindowServer	destinations for Keyboard event: (<keyboardFocus; Nexy.98347>)
default	20:25:13.109482-0500	WindowServer	destinations for Keyboard event: (<keyboardFocus; Nexy.98347>)
default	20:25:13.177122-0500	WindowServer	destinations for Keyboard event: (<keyboardFocus; Nexy.98347>)
default	20:25:13.261157-0500	WindowServer	destinations for Keyboard event: (<keyboardFocus; Nexy.98347>)
default	20:25:13.331707-0500	WindowServer	destinations for Keyboard event: (<keyboardFocus; Nexy.98347>)
default	20:25:18.864151-0500	WindowServer	destinations for Keyboard event: (<keyboardFocus; Nexy.98347>)
default	20:25:19.771035-0500	Nexy	                AUHAL.cpp:420   AUHAL: (0xc7e9eb840) Selecting device 85 from constructor
default	20:25:19.771055-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0xc7e9eb840)
default	20:25:19.771064-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0xc7e9eb840) not already running
default	20:25:19.771069-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0xc7e9eb840) nothing to teardown
default	20:25:19.771073-0500	Nexy	                AUHAL.cpp:762   SelectDevice: (0xc7e9eb840) connecting device 85
default	20:25:19.771178-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0xc7e9eb840) Device ID: 85 (Input:No | Output:Yes): true
default	20:25:19.771397-0500	Nexy	                AUHAL.cpp:774   SelectDevice: (0xc7e9eb840) created ioproc 0xc for device 85
default	20:25:19.771394-0500	Nexy	[com.apple.controlcenter:449CC7F2-8D7E-4BE0-8DBE-31E5C2A1CFEE] Sending action(s) in update: NSSceneFenceAction
default	20:25:19.771541-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0xc7e9eb840) adding 7 device listeners to device 85
default	20:25:19.771743-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0xc7e9eb840) adding 0 device delegate listeners to device 85
default	20:25:19.771756-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0xc7e9eb840)
default	20:25:19.771858-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  48000 Hz, Float32, interleaved
default	20:25:19.771871-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	20:25:19.771878-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	20:25:19.771886-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	20:25:19.771895-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	20:25:19.772034-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0xc7e9eb840) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	20:25:19.772047-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0xc7e9eb840) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	20:25:19.772054-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	20:25:19.772061-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0xc7e9eb840) removing 0 device listeners from device 0
default	20:25:19.772064-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0xc7e9eb840) removing 0 device delegate listeners from device 0
default	20:25:19.772068-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0xc7e9eb840)
default	20:25:19.772095-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is DISABLED
default	20:25:19.772164-0500	Nexy	                AUHAL.cpp:2303  SetProperty: (0xc7e9eb840) caller requesting device change from 85 to 91
default	20:25:19.772176-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0xc7e9eb840)
default	20:25:19.772181-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0xc7e9eb840) not already running
default	20:25:19.772186-0500	Nexy	                AUHAL.cpp:687   SelectDevice: (0xc7e9eb840) disconnecting device 85
default	20:25:19.772192-0500	Nexy	                AUHAL.cpp:751   SelectDevice: (0xc7e9eb840) destroying ioproc 0xc for device 85
default	20:25:19.772222-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped Unknown {1C-77-54-18-C8-A3:output, 0xc}
default	20:25:19.772253-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	20:25:19.772367-0500	Nexy	                AUHAL.cpp:762   SelectDevice: (0xc7e9eb840) connecting device 91
default	20:25:19.772485-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0xc7e9eb840) Device ID: 91 (Input:Yes | Output:No): true
default	20:25:19.775155-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.3410, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=98347, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=392, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	20:25:19.775769-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0xc7afefc30, from  2 ch,  24000 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	20:25:19.775804-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	20:25:19.776238-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	20:25:19.776973-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0xc7afefbd0, from  2 ch,  48000 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	20:25:19.776987-0500	Nexy	       AudioConverter.cpp:1317  AudioConverter -> 0xc7afefbd0: The in-process GetProperty call returned 1886547824 for property 1886546285 with size 8.
default	20:25:19.776994-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	20:25:19.776999-0500	Nexy	AudioConverter -> 0xc7afefbd0: The in-process SetProperty call returned 1886547824 for property 1936876385 with size 4.
default	20:25:19.777009-0500	Nexy	AudioConverter -> 0xc7afefbd0: The in-process SetProperty call returned 1886547824 for property 1936876401 with size 4.
default	20:25:19.777015-0500	Nexy	AudioConverter -> 0xc7afefbd0: The in-process SetProperty call returned 1886547824 for property 1886547309 with size 4.
default	20:25:19.777071-0500	tccd	AUTHREQ_SUBJECT: msgID=401.3410, subject=com.nexy.assistant,
default	20:25:19.777750-0500	Nexy	       AudioConverter.cpp:1067  Created a new in process converter -> 0xc7afef930, from  2 ch,  48000 Hz, Float32, deinterleaved to  2 ch,  48000 Hz, Float32, interleaved
default	20:25:19.777760-0500	Nexy	       AudioConverter.cpp:1317  AudioConverter -> 0xc7afef930: The in-process GetProperty call returned 1886547824 for property 1886546285 with size 8.
default	20:25:19.777766-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	20:25:19.777766-0500	Nexy	AudioConverter -> 0xc7afef930: The in-process SetProperty call returned 1886547824 for property 1936876385 with size 4.
default	20:25:19.777780-0500	Nexy	AudioConverter -> 0xc7afef930: The in-process SetProperty call returned 1886547824 for property 1936876401 with size 4.
default	20:25:19.777785-0500	Nexy	AudioConverter -> 0xc7afef930: The in-process SetProperty call returned 1886547824 for property 1886547309 with size 4.
default	20:25:19.777942-0500	Nexy	       AudioConverter.cpp:1317  AudioConverter -> 0xc7afef930: The in-process GetProperty call returned 1886547824 for property 1886546285 with size 8.
default	20:25:19.778244-0500	Nexy	         AVAudioEngine.mm:1182  Engine@0xc7c35c600: start, was running 0
default	20:25:19.778450-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8eed50300 at /Applications/Nexy.app
default	20:25:19.778714-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.55704030.55704039(501)>:98347] from originator [app<application.com.nexy.assistant.55704030.55704039(501)>:98347] with description <RBSAssertionDescriptor| "AudioHAL" ID:400-98347-144479 target:98347 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	20:25:19.778799-0500	runningboardd	Assertion 400-98347-144479 (target:[app<application.com.nexy.assistant.55704030.55704039(501)>:98347]) will be created as active
default	20:25:19.780666-0500	runningboardd	[app<application.com.nexy.assistant.55704030.55704039(501)>:98347] Ignoring jetsam update because this process is not memory-managed
default	20:25:19.780991-0500	runningboardd	[app<application.com.nexy.assistant.55704030.55704039(501)>:98347] Ignoring suspend because this process is not lifecycle managed
default	20:25:19.781048-0500	runningboardd	[app<application.com.nexy.assistant.55704030.55704039(501)>:98347] Ignoring GPU update because this process is not GPU managed
default	20:25:19.781114-0500	runningboardd	[app<application.com.nexy.assistant.55704030.55704039(501)>:98347] Ignoring memory limit update because this process is not memory-managed
default	20:25:19.781215-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.55704030.55704039(501)>:98347] from originator [osservice<com.apple.powerd>:332] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:400-332-144480 target:98347 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	20:25:19.781326-0500	runningboardd	Assertion 400-332-144480 (target:[app<application.com.nexy.assistant.55704030.55704039(501)>:98347]) will be created as active
default	20:25:19.784408-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.55704030.55704039(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:25:19.784771-0500	runningboardd	[app<application.com.nexy.assistant.55704030.55704039(501)>:98347] Ignoring jetsam update because this process is not memory-managed
default	20:25:19.784781-0500	runningboardd	[app<application.com.nexy.assistant.55704030.55704039(501)>:98347] Ignoring suspend because this process is not lifecycle managed
default	20:25:19.784805-0500	runningboardd	[app<application.com.nexy.assistant.55704030.55704039(501)>:98347] Ignoring GPU update because this process is not GPU managed
default	20:25:19.784883-0500	runningboardd	[app<application.com.nexy.assistant.55704030.55704039(501)>:98347] Ignoring memory limit update because this process is not memory-managed
default	20:25:19.785108-0500	ControlCenter	Received state update for 98347 (app<application.com.nexy.assistant.55704030.55704039(501)>, running-active-NotVisible
default	20:25:19.785257-0500	gamepolicyd	Received state update for 98347 (app<application.com.nexy.assistant.55704030.55704039(501)>, running-active-NotVisible
default	20:25:19.788474-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.55704030.55704039(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:25:19.789208-0500	ControlCenter	Received state update for 98347 (app<application.com.nexy.assistant.55704030.55704039(501)>, running-active-NotVisible
default	20:25:19.789402-0500	gamepolicyd	Received state update for 98347 (app<application.com.nexy.assistant.55704030.55704039(501)>, running-active-NotVisible
default	20:25:19.796801-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xa}
default	20:25:19.797872-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1f40af","name":"Nexy(98347)"}, "details":{"deviceUIDs":["1C-77-54-18-C8-A3:output"],"implicit_category":"MediaPlayback","input_running":false,"output_running":true} }
default	20:25:19.798127-0500	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 175, PID = 98347, Name = sid:0x1f40af, Nexy(98347), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO> is going active
default	20:25:19.798146-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsPlaying:]: MXCoreSession com.nexy.assistant with category/mode MediaPlayback/Default and coreSessionID = 175 starting playing
default	20:25:19.798271-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 175, PID = 98347, Name = sid:0x1f40af, Nexy(98347), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	20:25:19.798331-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 175, PID = 98347, Name = sid:0x1f40af, Nexy(98347), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO>
default	20:25:19.798469-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 201, deviceID = <private>
default	20:25:19.798494-0500	audiomxd	AudioApplicationInfoImpl.mm:395   Successfully updated session 0x1f40af to isSessionRecording: 0
	app: {"name":"[implicit] Nexy","pid":98347}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1f40af, sessionType: 'prim', isRecording: false }, 
]
default	20:25:19.798561-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 1]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)}
default	20:25:19.798573-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	20:25:19.798862-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 201 flag 0x1 < Hijack > app com.nexy.assistant CID 0x91550001 category Not set
default	20:25:19.799077-0500	audiomxd	UpdateAudioState CID 0x91550001 audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	20:25:19.799156-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 201,
}
default	20:25:19.799180-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	20:25:19.799196-0500	audioaccessoryd	AudioStateChanged: Added audio session app com.nexy.assistant NULL -> 201 count 4
default	20:25:19.799218-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 201
default	20:25:19.801403-0500	Nexy	                AUHAL.cpp:774   SelectDevice: (0xc7e9eb840) created ioproc 0xb for device 91
default	20:25:19.801500-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0xc7e9eb840) adding 7 device listeners to device 91
default	20:25:19.801747-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0xc7e9eb840) adding 0 device delegate listeners to device 91
default	20:25:19.801758-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0xc7e9eb840)
default	20:25:19.801765-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 output streams; not all mono
default	20:25:19.801779-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	20:25:19.801912-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  input stream 0 [0x5c]:  1 ch,  24000 Hz, Float32
default	20:25:19.801919-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 input streams; all mono
default	20:25:19.801925-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  1 ch,  24000 Hz, Float32
default	20:25:19.802023-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0xc7e9eb840) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	20:25:19.802040-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0xc7e9eb840) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	20:25:19.802045-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	20:25:19.802048-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0xc7e9eb840) removing 7 device listeners from device 85
default	20:25:19.802244-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0xc7e9eb840) removing 0 device delegate listeners from device 85
default	20:25:19.802256-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0xc7e9eb840)
default	20:25:19.802272-0500	Nexy	AudioHardware-mac-imp.cpp:1306   AudioObjectAddPropertyListener: listener was already added
default	20:25:19.803215-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	20:25:19.804506-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.3411, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=98347, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=392, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	20:25:19.805788-0500	tccd	AUTHREQ_SUBJECT: msgID=401.3411, subject=com.nexy.assistant,
default	20:25:19.806453-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8eed50300 at /Applications/Nexy.app
default	20:25:19.810532-0500	Nexy	 [INFO] SLSHWCaptureDesktopProxying:485 request: <private>
default	20:25:19.810532-0500	Nexy	 [INFO] SLSHWCaptureDesktopProxying:485 request: <private>
default	20:25:19.810585-0500	Nexy	 [INFO] -[RPDaemonProxy proxyCoreGraphicsWithMethodType:config:machPort:completionHandler:]:1493
default	20:25:19.810586-0500	Nexy	 [INFO] -[RPDaemonProxy proxyCoreGraphicsWithMethodType:config:machPort:completionHandler:]:1493
default	20:25:19.812602-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=82607.7, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=98347, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.replayd, pid=82607, auid=501, euid=501, binary_path=/usr/libexec/replayd}, },
default	20:25:19.812630-0500	tccd	requestor: TCCDProcess: identifier=com.apple.replayd, pid=82607, auid=501, euid=501, binary_path=/usr/libexec/replayd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=98347, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	20:25:19.813934-0500	tccd	AUTHREQ_SUBJECT: msgID=82607.7, subject=com.nexy.assistant,
default	20:25:19.815005-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b5166400 at /Applications/Nexy.app
default	20:25:19.824033-0500	Nexy	                AUHAL.cpp:1898  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	20:25:19.824997-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.3412, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=98347, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=392, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	20:25:19.826050-0500	tccd	AUTHREQ_SUBJECT: msgID=401.3412, subject=com.nexy.assistant,
default	20:25:19.826659-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8eed50300 at /Applications/Nexy.app
default	20:25:19.843848-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.3413, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=98347, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=392, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	20:25:19.844870-0500	tccd	AUTHREQ_SUBJECT: msgID=401.3413, subject=com.nexy.assistant,
default	20:25:19.845443-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8eed50300 at /Applications/Nexy.app
default	20:25:19.857038-0500	Nexy	 [INFO] SLSHWCaptureDesktopProxying_block_invoke:506 request: <private>, error: (null), windowInfo: (null)
default	20:25:19.857952-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=82607.8, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=98347, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.replayd, pid=82607, auid=501, euid=501, binary_path=/usr/libexec/replayd}, },
default	20:25:19.857984-0500	tccd	requestor: TCCDProcess: identifier=com.apple.replayd, pid=82607, auid=501, euid=501, binary_path=/usr/libexec/replayd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=98347, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	20:25:19.858911-0500	tccd	AUTHREQ_SUBJECT: msgID=82607.8, subject=com.nexy.assistant,
default	20:25:19.859579-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8b5166400 at /Applications/Nexy.app
default	20:25:19.863192-0500	coreaudiod	>>> NEGOTIATE [com.nexy.assistant]
default	20:25:19.863392-0500	coreaudiod	<<< NEGOTIATE [com.nexy.assistant]
default	20:25:19.864923-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:7690 called from <private>
default	20:25:19.864960-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Input {1C-77-54-18-C8-A3:input, 0xb}
default	20:25:19.865044-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	20:25:19.865794-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:7690 called from <private>
default	20:25:19.866033-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(7690)
default	20:25:19.866046-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:7690 called from <private>
default	20:25:19.866177-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(7696)
default	20:25:19.867086-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:7690 called from <private>
default	20:25:19.867110-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:7696 called from <private>
default	20:25:19.870229-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	20:25:19.867191-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:7696 called from <private>
default	20:25:19.867748-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(7689)
default	20:25:19.870203-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(7696)
default	20:25:19.870647-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	20:25:19.870290-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:7696 called from <private>
default	20:25:19.870297-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:7696 called from <private>
default	20:25:19.870542-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:7689 called from <private>
default	20:25:19.870589-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:7689 called from <private>
default	20:25:19.867752-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	20:25:19.872917-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(7690)
default	20:25:19.873016-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(7690)
default	20:25:19.873030-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:7690 called from <private>
default	20:25:19.873105-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(7690)
default	20:25:19.873121-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:7690 called from <private>
default	20:25:19.873150-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(7690)
default	20:25:19.873174-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:7690 called from <private>
default	20:25:19.873327-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:7690 called from <private>
default	20:25:19.873378-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:7690 called from <private>
default	20:25:19.873425-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:7690 called from <private>
default	20:25:19.873536-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:7690 called from <private>
default	20:25:19.873542-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:7690 called from <private>
default	20:25:19.873832-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:7690 called from <private>
default	20:25:19.873871-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:7690 called from <private>
default	20:25:19.870793-0500	runningboardd	Invalidating assertion 400-98347-144479 (target:[app<application.com.nexy.assistant.55704030.55704039(501)>:98347]) from originator [app<application.com.nexy.assistant.55704030.55704039(501)>:98347]
default	20:25:19.882108-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:7689 called from <private>
default	20:25:19.882145-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:7689 called from <private>
default	20:25:19.883135-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(7689)
default	20:25:19.871973-0500	runningboardd	Invalidating assertion 400-332-144480 (target:[app<application.com.nexy.assistant.55704030.55704039(501)>:98347]) from originator [osservice<com.apple.powerd>:332]
default	20:25:19.883179-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:7689 called from <private>
default	20:25:19.883291-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:7689 called from <private>
default	20:25:19.886015-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(7689)
default	20:25:19.886044-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(7689)
default	20:25:19.888328-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:7689 called from <private>
default	20:25:19.888343-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:7689 called from <private>
default	20:25:19.888360-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:7689 called from <private>
default	20:25:19.888380-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:7689 called from <private>
default	20:25:19.888386-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:7689 called from <private>
default	20:25:19.889115-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(7689)
default	20:25:19.891160-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(7696)
default	20:25:19.892213-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.55704030.55704039(501)>:98347] from originator [app<application.com.nexy.assistant.55704030.55704039(501)>:98347] with description <RBSAssertionDescriptor| "AudioHAL" ID:400-98347-144482 target:98347 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	20:25:19.891195-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(7690)
default	20:25:19.892427-0500	runningboardd	Assertion 400-98347-144482 (target:[app<application.com.nexy.assistant.55704030.55704039(501)>:98347]) will be created as active
default	20:25:19.891644-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:7690 called from <private>
error	20:25:19.892246-0500	Nexy	         HALC_ProxyIOContext.cpp:1075  HALC_ProxyIOContext::_StartIO(): Start failed - StartAndWaitForState returned error 35
default	20:25:19.892347-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:7689 called from <private>
default	20:25:19.896655-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	20:25:19.897130-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	20:25:19.892431-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:7689 called from <private>
default	20:25:19.892545-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:7689 called from <private>
default	20:25:19.892908-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:7696 called from <private>
default	20:25:19.893039-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:7696 called from <private>
default	20:25:19.893721-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(7696)
default	20:25:19.896212-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:7689 called from <private>
default	20:25:19.896282-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:7689 called from <private>
default	20:25:19.898081-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(7696)
default	20:25:19.898164-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(7696)
default	20:25:19.898238-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(7696)
default	20:25:19.898277-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(7696)
default	20:25:19.898334-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(7696)
default	20:25:19.898341-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:7696 called from <private>
default	20:25:19.898399-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:7696 called from <private>
default	20:25:19.898467-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:7696 called from <private>
default	20:25:19.898495-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:7696 called from <private>
default	20:25:19.898530-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:7696 called from <private>
default	20:25:19.898577-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:7696 called from <private>
default	20:25:19.898624-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:7696 called from <private>
default	20:25:19.898711-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:7696 called from <private>
default	20:25:19.898770-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:7696 called from <private>
default	20:25:19.898813-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:7696 called from <private>
default	20:25:19.898848-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:7696 called from <private>
default	20:25:19.898879-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:7696 called from <private>
default	20:25:19.898906-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:7696 called from <private>
default	20:25:19.898962-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:7696 called from <private>
default	20:25:19.899019-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:7696 called from <private>
default	20:25:19.898391-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.3414, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=98347, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=392, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	20:25:19.899055-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:7696 called from <private>
default	20:25:19.945368-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0xc7e9ea340) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	20:25:19.941025-0500	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1f40af, Nexy(98347), 'prim'', AudioCategory changed to 'PlayAndRecord_WithBluetooth'
default	20:25:19.945399-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0xc7e9ea340) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	20:25:19.945441-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	20:25:19.947211-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 201 flag 0x1 < Hijack > app com.nexy.assistant CID 0x91550001 category Not set
default	20:25:19.955535-0500	Nexy	         AVAudioEngine.mm:1461  Engine@0xc7c35c600: iounit configuration changed > stopping the engine
default	20:25:19.955703-0500	Nexy	         AVAudioEngine.mm:1236  Engine@0xc7c35c600: stop, was running 1
default	20:25:19.956154-0500	Nexy	         AVAudioEngine.mm:1219  Engine@0xc7c35c600: pause, was running 1
default	20:25:19.956404-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:25:19.956485-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:25:19.970067-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8eed50300 at /Applications/Nexy.app
default	20:25:19.975847-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:25:19.975876-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:25:19.975909-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:25:19.975934-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:25:19.975944-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:25:19.975951-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	20:25:19.976106-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	20:25:19.994016-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Output {1C-77-54-18-C8-A3:output, 0xa}
default	20:25:19.995526-0500	runningboardd	Invalidating assertion 400-332-144489 (target:[app<application.com.nexy.assistant.55704030.55704039(501)>:98347]) from originator [osservice<com.apple.powerd>:332]
default	20:25:19.995713-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1f40af","name":"Nexy(98347)"}, "details":{"deviceUIDs":["1C-77-54-18-C8-A3:input"],"implicit_category":"Record","input_running":true,"output_running":false} }
default	20:25:19.995842-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 175, PID = 98347, Name = sid:0x1f40af, Nexy(98347), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = YES, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	20:25:19.995882-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Category/Mode changed -- The score for sid:0x1f40af, Nexy(98347), 'prim'/com.nexy.assistant was not correct. Old score = 501
default	20:25:19.995922-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 175, PID = 98347, Name = sid:0x1f40af, Nexy(98347), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = YES, Recording = YES>
default	20:25:19.996062-0500	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1f40af, Nexy(98347), 'prim'', AudioCategory changed to 'Record_WithBluetooth'
default	20:25:19.996088-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	20:25:19.996102-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 175, PID = 98347, Name = sid:0x1f40af, Nexy(98347), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = YES, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	20:25:19.996146-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 175, PID = 98347, Name = sid:0x1f40af, Nexy(98347), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = YES, Recording = YES>
default	20:25:19.996283-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsPlaying:]: MXCoreSession com.nexy.assistant with category/mode Record_WithBluetooth/Default and coreSessionID = 175 stopping playing
default	20:25:19.996315-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 175, PID = 98347, Name = sid:0x1f40af, Nexy(98347), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	20:25:19.996346-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 175, PID = 98347, Name = sid:0x1f40af, Nexy(98347), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	20:25:20.008271-0500	coreaudiod	>>> NEGOTIATE [com.nexy.assistant]
default	20:25:20.008485-0500	coreaudiod	<<< NEGOTIATE [com.nexy.assistant]
default	20:25:20.011081-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:7690 called from <private>
default	20:25:20.011135-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:7690 called from <private>
default	20:25:20.014070-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	20:25:20.013839-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.55704030.55704039(501)>:98347] from originator [osservice<com.apple.powerd>:332] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:400-332-144491 target:98347 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	20:25:20.014429-0500	runningboardd	Assertion 400-332-144491 (target:[app<application.com.nexy.assistant.55704030.55704039(501)>:98347]) will be created as active
default	20:25:20.014674-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	20:25:20.012501-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:7690 called from <private>
default	20:25:20.012708-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(7690)
default	20:25:20.012737-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:7690 called from <private>
default	20:25:20.012746-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:7690 called from <private>
default	20:25:20.015491-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	20:25:20.016287-0500	runningboardd	Invalidating assertion 400-98347-144484 (target:[app<application.com.nexy.assistant.55704030.55704039(501)>:98347]) from originator [app<application.com.nexy.assistant.55704030.55704039(501)>:98347]
default	20:25:20.023122-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.3415, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=98347, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=392, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	20:25:20.025273-0500	tccd	AUTHREQ_SUBJECT: msgID=401.3415, subject=com.nexy.assistant,
default	20:25:20.037153-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	20:25:20.037303-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant), [mic] Nexy (com.nexy.assistant)]
default	20:25:20.037400-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant", "scr:com.nexy.assistant"]
default	20:25:20.039297-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:25:20.039323-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:25:20.039338-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:25:20.039346-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:25:20.039355-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:25:20.039364-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	20:25:20.039457-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:25:20.039510-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:25:20.039613-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:25:20.039652-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:25:20.039704-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:25:20.039719-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	20:25:20.039737-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	20:25:20.039855-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:25:20.039869-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:25:20.039880-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:25:20.039892-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:25:20.039902-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:25:20.039911-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	20:25:20.039951-0500	ControlCenter	Navigating to new application [com.nexy.assistant]
default	20:25:20.045815-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	20:25:20.045893-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant)]
default	20:25:20.046013-0500	ControlCenter	Active activity attributions changed to ["scr:com.nexy.assistant"]
default	20:25:20.046046-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	20:25:20.067682-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	20:25:20.070168-0500	coreaudiod	IssueReporting.cpp:492   RTAID [ use_case=Generic report_type=RMS Generic Chain clientID=ADM node=ADM::com.nexy.assistant_7690.7540.0_airpods noise suppression studio::out-0 issue_detected_sample_time=81600.000000 ] -- [ rms:[-29.433420], peaks:[-9.467350] ]
default	20:25:20.070226-0500	coreaudiod	IssueReporting.cpp:492   RTAID [ use_case=Generic report_type=RMS Generic Chain clientID=ADM node=ADM::com.nexy.assistant_7690.7540.0_airpods noise suppression studio::in-0 issue_detected_sample_time=0.000000 ] -- [ rms:[-36.674717], peaks:[-14.180912] ]
default	20:25:20.072037-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xafa0fd200] Created node ADM::com.nexy.assistant_7690.7540.0_airpods noise suppression studio::in-0 with nodeID 0 - reporting period = 10.000000, sample rate = 24000.000000
default	20:25:20.072339-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xafa0fd200] Created node ADM::com.nexy.assistant_7690.7540.0_airpods noise suppression studio::out-0 with nodeID 1 - reporting period = 10.000000, sample rate = 24000.000000
default	20:25:20.097754-0500	runningboardd	[app<application.com.nexy.assistant.55704030.55704039(501)>:98347] Ignoring jetsam update because this process is not memory-managed
default	20:25:20.097781-0500	runningboardd	[app<application.com.nexy.assistant.55704030.55704039(501)>:98347] Ignoring suspend because this process is not lifecycle managed
default	20:25:20.097805-0500	runningboardd	[app<application.com.nexy.assistant.55704030.55704039(501)>:98347] Ignoring GPU update because this process is not GPU managed
default	20:25:20.097873-0500	runningboardd	[app<application.com.nexy.assistant.55704030.55704039(501)>:98347] Ignoring memory limit update because this process is not memory-managed
default	20:25:20.105739-0500	Nexy	         AVAudioEngine.mm:1437  Engine@0xc7c35c600: iounit configuration changed > posting notification
default	20:25:20.118827-0500	ControlCenter	Received state update for 98347 (app<application.com.nexy.assistant.55704030.55704039(501)>, running-active-NotVisible
default	20:25:20.121051-0500	gamepolicyd	Received state update for 98347 (app<application.com.nexy.assistant.55704030.55704039(501)>, running-active-NotVisible
default	20:25:20.167474-0500	coreaudiod	<<< ADAPT [com.nexy.assistant]
default	20:25:20.168582-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.55704030.55704039(501)>:98347] from originator [osservice<com.apple.powerd>:332] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:400-332-144493 target:98347 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	20:25:20.168659-0500	runningboardd	Assertion 400-332-144493 (target:[app<application.com.nexy.assistant.55704030.55704039(501)>:98347]) will be created as active
default	20:25:20.169094-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:7690 called from <private>
default	20:25:20.169506-0500	runningboardd	[app<application.com.nexy.assistant.55704030.55704039(501)>:98347] Ignoring jetsam update because this process is not memory-managed
default	20:25:20.169522-0500	runningboardd	[app<application.com.nexy.assistant.55704030.55704039(501)>:98347] Ignoring suspend because this process is not lifecycle managed
default	20:25:20.169534-0500	runningboardd	[app<application.com.nexy.assistant.55704030.55704039(501)>:98347] Ignoring GPU update because this process is not GPU managed
default	20:25:20.169661-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:7690 called from <private>
default	20:25:20.169559-0500	runningboardd	[app<application.com.nexy.assistant.55704030.55704039(501)>:98347] Ignoring memory limit update because this process is not memory-managed
default	20:25:20.169719-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	20:25:20.170491-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:7690 called from <private>
default	20:25:20.170860-0500	runningboardd	Invalidating assertion 400-98347-144492 (target:[app<application.com.nexy.assistant.55704030.55704039(501)>:98347]) from originator [app<application.com.nexy.assistant.55704030.55704039(501)>:98347]
default	20:25:20.171226-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	20:25:20.170650-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(7690)
default	20:25:20.171566-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	20:25:20.170669-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:7690 called from <private>
default	20:25:20.170675-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:7690 called from <private>
default	20:25:20.172240-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(7690)
default	20:25:20.172370-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:7690 called from <private>
default	20:25:20.172383-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:7690 called from <private>
default	20:25:20.172396-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:7690 called from <private>
default	20:25:20.173144-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.55704030.55704039(501)>:98347] from originator [app<application.com.nexy.assistant.55704030.55704039(501)>:98347] with description <RBSAssertionDescriptor| "AudioHAL" ID:400-98347-144494 target:98347 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	20:25:20.173263-0500	runningboardd	Assertion 400-98347-144494 (target:[app<application.com.nexy.assistant.55704030.55704039(501)>:98347]) will be created as active
default	20:25:20.174458-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.3416, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=98347, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=392, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	20:25:20.176754-0500	tccd	AUTHREQ_SUBJECT: msgID=401.3416, subject=com.nexy.assistant,
default	20:25:20.177722-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x8eed50300 at /Applications/Nexy.app
default	20:25:20.177864-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.55704030.55704039(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:25:20.178374-0500	runningboardd	Invalidating assertion 400-332-144493 (target:[app<application.com.nexy.assistant.55704030.55704039(501)>:98347]) from originator [osservice<com.apple.powerd>:332]
default	20:25:20.182315-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	20:25:20.186791-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	20:25:20.186858-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant), [mic] Nexy (com.nexy.assistant)]
default	20:25:20.186908-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant", "scr:com.nexy.assistant"]
default	20:25:20.187256-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:25:20.187273-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:25:20.187288-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:25:20.187323-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:25:20.187335-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:25:20.187342-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	20:25:20.187372-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:25:20.187386-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:25:20.187398-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:25:20.187407-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:25:20.187417-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:25:20.187424-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	20:25:20.187443-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:25:20.187452-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:25:20.187494-0500	ControlCenter	Navigating to new application [com.nexy.assistant]
default	20:25:20.187482-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:25:20.187540-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:25:20.187568-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:25:20.187593-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	20:25:20.187675-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	20:25:20.192734-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	20:25:20.192836-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant)]
default	20:25:20.192909-0500	ControlCenter	Active activity attributions changed to ["scr:com.nexy.assistant"]
default	20:25:20.192943-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	20:25:20.203353-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:25:20.203612-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:25:20.203639-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:25:20.203649-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:25:20.203656-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:25:20.203664-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	20:25:20.203757-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	20:25:20.204627-0500	ControlCenter	Received state update for 98347 (app<application.com.nexy.assistant.55704030.55704039(501)>, running-active-NotVisible
default	20:25:20.205004-0500	gamepolicyd	Received state update for 98347 (app<application.com.nexy.assistant.55704030.55704039(501)>, running-active-NotVisible
default	20:25:20.207182-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.55704030.55704039(501)>:98347] from originator [osservice<com.apple.powerd>:332] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:400-332-144495 target:98347 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	20:25:20.207710-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:7690 called from <private>
default	20:25:20.208255-0500	runningboardd	Assertion 400-332-144495 (target:[app<application.com.nexy.assistant.55704030.55704039(501)>:98347]) will be created as active
default	20:25:20.215799-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	20:25:20.221091-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	20:25:20.221179-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant), [mic] Nexy (com.nexy.assistant)]
default	20:25:20.221237-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant", "scr:com.nexy.assistant"]
default	20:25:20.221869-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:25:20.221884-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:25:20.221895-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:25:20.221908-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:25:20.221916-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:25:20.221925-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	20:25:20.221968-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:25:20.221990-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:25:20.222016-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:25:20.222053-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	20:25:20.222054-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:25:20.222105-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:25:20.222141-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	20:25:20.222227-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:25:20.222235-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:25:20.222290-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:25:20.222306-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:25:20.222317-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:25:20.222326-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	20:25:20.222328-0500	ControlCenter	Navigating to new application [com.nexy.assistant]
default	20:25:20.471919-0500	kernel	tcp_connection_summary (tcp_drop:1453)[<IPv4-redacted>:61567<-><IPv4-redacted>:53] interface: en0 (skipped: 196)
so_gencnt: 8779758 t_state: SYN_SENT process: Nexy:98347 Duration: 75.001 sec Conn_Time: 0.000 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 0.000 ms rttvar: 250.000 ms base rtt: 0 ms so_error: 60 svc/tc: 0 flow: 0xa78e35d3
default	20:25:20.471941-0500	kernel	tcp_connection_summary [<IPv4-redacted>:61567<-><IPv4-redacted>:53] interface: en0 (skipped: 196)
so_gencnt: 8779758 t_state: SYN_SENT process: Nexy:98347 flowctl: 0us (0x) SYN in/out: 0/11 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	20:25:20.898890-0500	WindowServer	destinations for Keyboard event: (<keyboardFocus; Nexy.98347>)
default	20:25:21.023837-0500	Nexy	[com.apple.controlcenter:449CC7F2-8D7E-4BE0-8DBE-31E5C2A1CFEE] Sending action(s) in update: NSSceneFenceAction
default	20:25:21.392833-0500	kernel	tcp_connection_summary (tcp_usrclosed:3220)[<IPv4-redacted>:61566<-><IPv4-redacted>:443] interface: en0 (skipped: 196)
so_gencnt: 8779757 t_state: LAST_ACK process: Nexy:98347 Duration: 75.926 sec Conn_Time: 0.014 sec bytes in/out: 523982/1321 pkts in/out: 55/8 pkt rxmit: 0 ooo pkts: 9 dup bytes in: 0 ACKs delayed: 2 delayed ACKs sent: 0
rtt: 17.468 ms rttvar: 6.437 ms base rtt: 12 ms so_error: 0 svc/tc: 0 flow: 0xaeac872f
default	20:25:21.392857-0500	kernel	tcp_connection_summary [<IPv4-redacted>:61566<-><IPv4-redacted>:443] interface: en0 (skipped: 196)
so_gencnt: 8779757 t_state: LAST_ACK process: Nexy:98347 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 1/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	20:25:21.393882-0500	Nexy	[0xc7d1c4dc0] activating connection: mach=true listener=false peer=false name=com.apple.SystemConfiguration.DNSConfiguration
default	20:25:21.395530-0500	Nexy	[0xc7d1c4dc0] invalidated after the last release of the connection object
default	20:25:21.396625-0500	kernel	udp connect: [<IPv4-redacted>:62717<-><IPv4-redacted>:53] interface:  (skipped: 209)
so_gencnt: 8780376 so_state: 0x0102 process: Nexy:98347 bytes in/out: 0/0 pkts in/out: 0/0 error: 0 so_error: 0 svc/tc: 0 flow: 0xa5e1c50f
default	20:25:21.919708-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xb}
default	20:25:21.920159-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1f40af","name":"Nexy(98347)"}, "details":{"deviceUIDs":[],"implicit_category":"","input_running":false,"output_running":false} }
default	20:25:21.920373-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 175, PID = 98347, Name = sid:0x1f40af, Nexy(98347), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	20:25:21.920463-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 175, PID = 98347, Name = sid:0x1f40af, Nexy(98347), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	20:25:21.920631-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1f40af, Nexy(98347), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 175 stopping recording
default	20:25:21.920641-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	20:25:21.920664-0500	audiomxd	-MXCoreSession- -[MXCoreSession endInterruption:]: Session <ID: 175, PID = 98347, Name = sid:0x1f40af, Nexy(98347), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> is going inactive
default	20:25:21.920697-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 175, PID = 98347, Name = sid:0x1f40af, Nexy(98347), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	20:25:21.920737-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 175, PID = 98347, Name = sid:0x1f40af, Nexy(98347), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	20:25:21.920909-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 0]. BT device UIDS: {(
)}
default	20:25:21.920928-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	20:25:21.921041-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 200 flag 0x1 < Hijack > app com.nexy.assistant CID 0x91550001 category Not set
default	20:25:21.921539-0500	audiomxd	UpdateAudioState CID 0x91550001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	20:25:21.921632-0500	audiomxd	UpdateAudioState CID 0x91550001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:25:21.921721-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	20:25:21.924050-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:25:21.924216-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	20:25:21.924279-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	20:25:21.924454-0500	runningboardd	Invalidating assertion 400-98347-144494 (target:[app<application.com.nexy.assistant.55704030.55704039(501)>:98347]) from originator [app<application.com.nexy.assistant.55704030.55704039(501)>:98347]
default	20:25:21.924482-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:25:21.924626-0500	runningboardd	Invalidating assertion 400-332-144495 (target:[app<application.com.nexy.assistant.55704030.55704039(501)>:98347]) from originator [osservice<com.apple.powerd>:332]
default	20:25:21.924524-0500	audioaccessoryd	AudioStateChanged: Removed audio session app com.nexy.assistant 201 count 3
default	20:25:21.933135-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	20:25:21.933269-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant)]
default	20:25:21.933372-0500	ControlCenter	Active activity attributions changed to ["scr:com.nexy.assistant"]
default	20:25:21.933399-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	20:25:21.934104-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:25:21.934122-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:25:21.934138-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:25:21.934145-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:25:21.934154-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:25:21.934163-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	20:25:21.934551-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	20:25:21.965364-0500	WindowServer	destinations for Keyboard event: (<keyboardFocus; Nexy.98347>)
default	20:25:22.025079-0500	Nexy	                AUHAL.cpp:473   ~AUHAL: (0xc7e9eb840) Selecting device 0 from destructor
default	20:25:22.025094-0500	Nexy	                AUHAL.cpp:629   SelectDevice: -> (0xc7e9eb840)
default	20:25:22.025101-0500	Nexy	                AUHAL.cpp:681   SelectDevice: (0xc7e9eb840) not already running
default	20:25:22.025108-0500	Nexy	                AUHAL.cpp:687   SelectDevice: (0xc7e9eb840) disconnecting device 91
default	20:25:22.025115-0500	Nexy	                AUHAL.cpp:751   SelectDevice: (0xc7e9eb840) destroying ioproc 0xb for device 91
default	20:25:22.025152-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xb}
default	20:25:22.025194-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	20:25:22.025369-0500	Nexy	                AUHAL.cpp:853   SelectDevice: (0xc7e9eb840) nothing to setup
default	20:25:22.025383-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0xc7e9eb840) adding 0 device listeners to device 0
default	20:25:22.025392-0500	Nexy	                AUHAL.cpp:863   SelectDevice: (0xc7e9eb840) adding 0 device delegate listeners to device 0
default	20:25:22.025398-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0xc7e9eb840) removing 7 device listeners from device 91
default	20:25:22.025691-0500	Nexy	                AUHAL.cpp:900   SelectDevice: (0xc7e9eb840) removing 0 device delegate listeners from device 91
default	20:25:22.025712-0500	Nexy	                AUHAL.cpp:916   SelectDevice: <- (0xc7e9eb840)
default	20:25:22.029139-0500	WindowServer	destinations for Keyboard event: (<keyboardFocus; Nexy.98347>)
default	20:25:22.030422-0500	runningboardd	[app<application.com.nexy.assistant.55704030.55704039(501)>:98347] Ignoring jetsam update because this process is not memory-managed
default	20:25:22.030436-0500	runningboardd	[app<application.com.nexy.assistant.55704030.55704039(501)>:98347] Ignoring suspend because this process is not lifecycle managed
default	20:25:22.030451-0500	runningboardd	[app<application.com.nexy.assistant.55704030.55704039(501)>:98347] Ignoring GPU update because this process is not GPU managed
default	20:25:22.030498-0500	runningboardd	[app<application.com.nexy.assistant.55704030.55704039(501)>:98347] Ignoring memory limit update because this process is not memory-managed
default	20:25:22.034131-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.55704030.55704039(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	20:25:22.034805-0500	ControlCenter	Received state update for 98347 (app<application.com.nexy.assistant.55704030.55704039(501)>, running-active-NotVisible
default	20:25:22.035166-0500	gamepolicyd	Received state update for 98347 (app<application.com.nexy.assistant.55704030.55704039(501)>, running-active-NotVisible
default	20:25:22.318588-0500	Nexy	[C:3] Alloc com.apple.backboard.hid-services.xpc
default	20:25:22.318670-0500	Nexy	[0xc7d1c4dc0] activating connection: mach=false listener=false peer=false name=(anonymous)
error	20:25:22.319439-0500	Nexy	Unable to obtain a task name port right for pid 391: (os/kern) failure (0x5)
default	20:25:22.320898-0500	Nexy	BKSHIDEventDeliveryManager - connection activation
default	20:25:22.325464-0500	Nexy	terminate:
default	20:25:22.325551-0500	Nexy	void _NSDisableAutomaticTerminationAndLog(NSString *) Terminating
default	20:25:22.325578-0500	Nexy	-[NSApplication _pushPersistentStateTerminationGeneration] sPersistentStateTerminateStackHeight -> 1
default	20:25:22.325829-0500	Nexy	Attempting sudden termination (1st attempt)
default	20:25:22.325854-0500	Nexy	Checking whether app should terminate
default	20:25:22.325993-0500	Nexy	Asking app delegate whether applicationShouldTerminate:
default	20:25:22.326102-0500	Nexy	replyToApplicationShouldTerminate:YES
default	20:25:22.326227-0500	Nexy	App termination approved
default	20:25:22.326309-0500	Nexy	Termination commencing
default	20:25:22.326370-0500	Nexy	Attempting sudden termination (2nd attempt)
default	20:25:22.329986-0500	Nexy	Termination complete. Exiting without sudden termination.
default	20:25:22.336148-0500	Nexy	[0xc7d1c5040] activating connection: mach=true listener=false peer=false name=com.apple.powerlog.plxpclogger.xpc
default	20:25:23.403997-0500	kernel	udp connect: [<IPv4-redacted>:0<-><IPv4-redacted>:0] interface:  (skipped: 209)
so_gencnt: 8780396 so_state: 0x0000 process: Nexy:98347 bytes in/out: 0/0 pkts in/out: 0/0 error: 49 so_error: 0 svc/tc: 0 flow: 0x0
default	20:25:23.404027-0500	kernel	udp_connection_summary [<IPv4-redacted>:0<-><IPv4-redacted>:0] interface:  (skipped: 209)
so_gencnt: 8780396 so_state: 0x0000 process: Nexy:98347 Duration: 0.000 sec Conn_Time: 0.000 sec bytes in/out: 0/0 pkts in/out: 0/0 rxnospace pkts/bytes: 0/0 so_error: 0 svc/tc: 0 flow: 0x0 flowctl: 0us (0x)
default	20:25:24.048497-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(7696)
default	20:25:24.048578-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:7696 called from <private>
default	20:25:24.048587-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:7696 called from <private>
default	20:25:24.050276-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(7690)
default	20:25:24.050276-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(7696)
default	20:25:24.050319-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:7696 called from <private>
default	20:25:24.050326-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:7690 called from <private>
default	20:25:24.050328-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:7696 called from <private>
default	20:25:24.050337-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:7690 called from <private>
default	20:25:24.050407-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(7689)
default	20:25:24.050487-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:7689 called from <private>
default	20:25:24.050529-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:7689 called from <private>
default	20:25:24.069439-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(7696)
default	20:25:24.069492-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(7690)
default	20:25:24.069518-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:7690 called from <private>
default	20:25:24.069524-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:7690 called from <private>
default	20:25:24.073785-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:7689 called from <private>
default	20:25:24.073813-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:7689 called from <private>
default	20:25:24.073856-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:7696 called from <private>
default	20:25:24.073867-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:7696 called from <private>
default	20:25:24.073952-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(7689)
default	20:25:24.074100-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(7696)
default	20:25:24.074186-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:7689 called from <private>
default	20:25:24.074289-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:7689 called from <private>
default	20:25:24.075117-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(7689)
default	20:25:24.075413-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(7689)
default	20:25:24.075535-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:7689 called from <private>
default	20:25:24.075608-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:7689 called from <private>
default	20:25:24.075714-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:7689 called from <private>
default	20:25:24.075875-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:7689 called from <private>
default	20:25:24.075903-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:7689 called from <private>
default	20:25:24.075931-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:7689 called from <private>
default	20:25:24.076145-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:7689 called from <private>
default	20:25:24.076217-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:7689 called from <private>
default	20:25:24.076394-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(7689)
default	20:25:24.076880-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	20:25:24.076438-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:7689 called from <private>
default	20:25:24.077435-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	20:25:24.076478-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:7689 called from <private>
default	20:25:24.076889-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(7689)
default	20:25:24.077064-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:7689 called from <private>
default	20:25:24.077074-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:7689 called from <private>
default	20:25:24.077111-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:7689 called from <private>
default	20:25:24.077176-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:7689 called from <private>
default	20:25:24.079838-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(7696)
default	20:25:24.079866-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(7689)
default	20:25:24.079881-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(7696)
default	20:25:24.079893-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:7689 called from <private>
default	20:25:24.079895-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(7696)
default	20:25:24.079901-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:7689 called from <private>
default	20:25:24.079938-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(7689)
default	20:25:24.079950-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(7696)
default	20:25:24.079978-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(7689)
default	20:25:24.080007-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(7696)
default	20:25:24.079982-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:7689 called from <private>
default	20:25:24.080076-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:7689 called from <private>
default	20:25:24.080108-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:7689 called from <private>
default	20:25:24.080127-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:7696 called from <private>
default	20:25:24.080137-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:7689 called from <private>
default	20:25:24.080159-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:7696 called from <private>
default	20:25:24.080216-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:7696 called from <private>
default	20:25:24.080286-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:7696 called from <private>
default	20:25:24.080316-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:7696 called from <private>
default	20:25:24.080324-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:7696 called from <private>
default	20:25:24.080349-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:7696 called from <private>
default	20:25:24.080379-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:7696 called from <private>
default	20:25:24.080387-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:7696 called from <private>
default	20:25:24.080405-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:7696 called from <private>
default	20:25:24.080430-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:7696 called from <private>
default	20:25:24.080437-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:7696 called from <private>
default	20:25:24.080470-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:7696 called from <private>
default	20:25:24.080514-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:7696 called from <private>
default	20:25:24.080543-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:7696 called from <private>
default	20:25:24.080585-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:7696 called from <private>
default	20:25:24.095942-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:7689 called from <private>
default	20:25:24.095977-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:7689 called from <private>
default	20:25:24.096124-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(7689)
default	20:25:24.100639-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(7689)
default	20:25:24.100822-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:7689 called from <private>
default	20:25:24.100831-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:7689 called from <private>
default	20:25:24.100883-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:7689 called from <private>
default	20:25:24.100893-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:7689 called from <private>
default	20:25:24.100899-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:7689 called from <private>
default	20:25:24.100905-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:7689 called from <private>
default	20:25:24.103125-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0xc7e9ea340) Device ID: 85 (Input:No | Output:Yes): true
default	20:25:24.103157-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0xc7e9ea340)
default	20:25:24.103348-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  48000 Hz, Float32, interleaved
default	20:25:24.103359-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	20:25:24.103367-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	20:25:24.103379-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 0 input streams; not all mono
default	20:25:24.103389-0500	Nexy	                AUHAL.cpp:1706  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	20:25:24.104193-0500	Nexy	                AUHAL.cpp:1776  UpdateStreamFormats: AUHAL(0xc7e9ea340) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	20:25:24.104229-0500	Nexy	                AUHAL.cpp:1782  UpdateStreamFormats: AUHAL(0xc7e9ea340) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	20:25:24.104253-0500	Nexy	                AUHAL.cpp:1792  UpdateStreamFormats: <-
default	20:25:24.105130-0500	Nexy	                AUHAL.cpp:3418  IsDeviceUsable: (0xc7e9ea340) Device ID: 85 (Input:No | Output:Yes): true
default	20:25:24.105211-0500	Nexy	                AUHAL.cpp:1586  UpdateStreamFormats: -> (0xc7e9ea340)
default	20:25:24.106719-0500	Nexy	                AUHAL.cpp:1682  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  48000 Hz, Float32, interleaved
default	20:25:24.106774-0500	Nexy	                AUHAL.cpp:1694  UpdateStreamFormats: 1 output streams; not all mono
default	20:25:24.113925-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:7689 called from <private>
default	20:25:24.114940-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(7696)
default	20:25:24.115001-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(7689)
default	20:25:24.115329-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:7696 called from <private>
default	20:25:24.230377-0500	Nexy	         AVAudioEngine.mm:1437  Engine@0xc7c35c600: iounit configuration changed > posting notification
default	20:25:24.338886-0500	Nexy	Entering exit handler.
default	20:25:24.338939-0500	Nexy	Queueing exit procedure onto XPC queue. Any further messages sent will be discarded. activeSendTransactions=0
default	20:25:24.339005-0500	Nexy	Cancelling XPC connection. Any further reply handler invocations will not retry messages
default	20:25:24.339015-0500	Nexy	[0xc7d7f8000] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	20:25:24.339031-0500	Nexy	Exiting exit handler.
default	20:25:24.341195-0500	audiomxd	  ServerSessionManager.mm:478   { "action":"destroy_session", "session":{"ID":"0x1f40af","name":"Nexy(98347)"}, "details":null }
default	20:25:24.341221-0500	audiomxd	AudioApplicationInfoImpl.mm:690   Successfully removed session 0x1f40af from AudioApp, recording state unchanged (app: {"name":"[implicit] Nexy","pid":98347})
default	20:25:24.341232-0500	audiomxd	  ServerSessionManager.mm:1086  destroy audio app instance since was created implicitly by session creation and all sessions now gone (audio app: {"name":"[implicit] Nexy","pid":98347})
default	20:25:24.341511-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 175, PID = 98347, Name = sid:0x1f40af, Nexy(98347), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	20:25:24.342139-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:25:24.342202-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:25:24.341727-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 175, PID = 98347, Name = sid:0x1f40af, Nexy(98347), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	20:25:24.342238-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:25:24.342464-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:25:24.341150-0500	WindowServer	0[outside of RPC]: Process death: 0x0-0x75f75f (Nexy) connectionID: 1315F3 pid: 98347 in session 0x101
default	20:25:24.341175-0500	WindowServer	<BSCompoundAssertion:0x830c11580> ([FocusManager:257]-deferringPolicyEvaluationSuppression) acquire for reason:process death - 0x0-0x75f75f (Nexy) acq:0x8344fbb00 count:1
default	20:25:24.341892-0500	audiomxd	UpdateAudioState CID 0x91550001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:25:24.342087-0500	audiomxd	UpdateAudioState CID 0x91550001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	20:25:24.344013-0500	WindowManager	Connection invalidated | (98347) Nexy
default	20:25:24.344166-0500	ControlCenter	[app<application.com.nexy.assistant.55704030.55704039>:98347] Workspace connection invalidated.
default	20:25:24.344193-0500	ControlCenter	[app<application.com.nexy.assistant.55704030.55704039>:98347] Now flagged as pending exit for reason: workspace client connection invalidated
default	20:25:24.344856-0500	WindowServer	0[outside of RPC]: [FocusManager:257] update to deferring policy requested for reason: permitted list updated - 0x0-0x75f75f removed - but we are suppressing evaluation for reasons: {(
    "process death - 0x0-0x75f75f (Nexy)"
)}
default	20:25:24.345280-0500	WindowServer	0[outside of RPC]: [FocusManager:257] update to deferring policy requested for reason: permitted list updated - 0x1-0x1802b removed - but we are suppressing evaluation for reasons: {(
    "process death - 0x0-0x75f75f (Nexy)"
)}
default	20:25:24.346982-0500	runningboardd	Invalidating assertion 400-391-144477 (target:[app<application.com.nexy.assistant.55704030.55704039(501)>:98347]) from originator [osservice<com.apple.WindowServer(88)>:391]
default	20:25:24.347064-0500	runningboardd	XPC connection invalidated: [app<application.com.nexy.assistant.55704030.55704039(501)>:98347]
default	20:25:24.347157-0500	runningboardd	Invalidating assertion 400-391-144476 (target:[app<application.com.nexy.assistant.55704030.55704039(501)>:98347]) from originator [osservice<com.apple.WindowServer(88)>:391]
default	20:25:24.377676-0500	kernel	tcp_connection_summary (tcp_drop:1453)[<IPv4-redacted>:61568<-><IPv4-redacted>:443] interface: en0 (skipped: 196)
so_gencnt: 8779768 t_state: CLOSED process: Nexy:98347 Duration: 78.889 sec Conn_Time: 0.012 sec bytes in/out: 4693/941 pkts in/out: 6/4 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 12.812 ms rttvar: 3.250 ms base rtt: 12 ms so_error: 0 svc/tc: 0 flow: 0x9672f901
default	20:25:24.377695-0500	kernel	tcp_connection_summary [<IPv4-redacted>:61568<-><IPv4-redacted>:443] interface: en0 (skipped: 196)
so_gencnt: 8779768 t_state: CLOSED process: Nexy:98347 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 1/0 RST in/out: 0/1 AccECN (client/server): Disabled/Disabled
default	20:25:24.377767-0500	kernel	udp_connection_summary [<IPv4-redacted>:62717<-><IPv4-redacted>:53] interface: en0 (skipped: 209)
so_gencnt: 8780376 so_state: 0x0102 process: Nexy:98347 Duration: 2.981 sec Conn_Time: 2.981 sec bytes in/out: 353/192 pkts in/out: 3/3 rxnospace pkts/bytes: 0/0 so_error: 0 svc/tc: 0 flow: 0xa5e1c50f flowctl: 0us (0x)
default	20:25:24.377963-0500	mDNSResponder	[R152461] DNSServiceCreateConnection STOP PID[98347](Nexy)
default	20:25:24.379312-0500	runningboardd	[app<application.com.nexy.assistant.55704030.55704039(501)>:98347] termination reported by launchd (0, 0, 0)
default	20:25:24.379348-0500	runningboardd	Removing process: [app<application.com.nexy.assistant.55704030.55704039(501)>:98347]
default	20:25:24.379652-0500	runningboardd	Removing launch job for: [app<application.com.nexy.assistant.55704030.55704039(501)>:98347]
default	20:25:24.379899-0500	runningboardd	Removed job for [app<application.com.nexy.assistant.55704030.55704039(501)>:98347]
default	20:25:24.379941-0500	runningboardd	Removing assertions for terminated process: [app<application.com.nexy.assistant.55704030.55704039(501)>:98347]
default	20:25:24.379981-0500	runningboardd	Removed last relative-start-date-defining assertion for process app<application.com.nexy.assistant.55704030.55704039(501)>
default	20:25:24.385241-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.55704030.55704039(501)>: none (role: None) (endowments: (null))
default	20:25:24.385713-0500	ControlCenter	[app<application.com.nexy.assistant.55704030.55704039>:98347] Process exited: <RBSProcessExitContext| voluntary>.
default	20:25:24.385740-0500	ControlCenter	[app<application.com.nexy.assistant.55704030.55704039>:98347] Setting process task state to: Not Running
default	20:25:24.385752-0500	ControlCenter	[app<application.com.nexy.assistant.55704030.55704039>:98347] Setting process visibility to: Unknown
default	20:25:24.385778-0500	ControlCenter	Received state update for 98347 (app<application.com.nexy.assistant.55704030.55704039(501)>, none-NotVisible
default	20:25:24.385790-0500	ControlCenter	[app<application.com.nexy.assistant.55704030.55704039>:98347] Invalidating workspace.
default	20:25:24.385818-0500	ControlCenter	Removing source registration for processHandle: [app<application.com.nexy.assistant.55704030.55704039(501)>:98347]
default	20:25:24.385765-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.55704030.55704039(501)>: none (role: None) (endowments: (null))
default	20:25:24.385823-0500	audiomxd	  ServerSessionManager.mm:1327  Monitored process died, pid = 98347, name = Nexy
default	20:25:24.385941-0500	ControlCenter	Received state update for 98347 (app<application.com.nexy.assistant.55704030.55704039(501)>, none-NotVisible
default	20:25:24.386300-0500	gamepolicyd	Received state update for 98347 (app<application.com.nexy.assistant.55704030.55704039(501)>, none-NotVisible
default	20:25:24.386707-0500	gamepolicyd	Received state update for 98347 (app<application.com.nexy.assistant.55704030.55704039(501)>, none-NotVisible
default	20:25:24.386924-0500	launchservicesd	Hit the server for a process handle fe534190001802b that resolved to: [app<application.com.nexy.assistant.55704030.55704039(501)>:98347]
default	20:25:24.388192-0500	ControlCenter	Removing: <FBApplicationProcess: 0xc3130c000; app<application.com.nexy.assistant.55704030.55704039>:98347(vA02935)>
default	20:25:24.392635-0500	loginwindow	-[ApplicationManager handleCASEvent:withData:] | CAS notification for appDeath for com.nexy.assistant with asn: LSASN:{hi=0x0;lo=0x75f75f} for bundle path: /Applications/Nexy.app with URL: file:///Applications/Nexy.app/
default	20:25:24.392698-0500	loginwindow	-[Application setState:] | enter: <Application: 0xc0121b160: Nexy> state 3
default	20:25:24.392740-0500	loginwindow	-[PersistentAppsSupport applicationQuit:] | for app:Nexy, _appTrackingState = 2
default	20:25:24.393706-0500	loginwindow	-[Application setState:] | enter: <Application: 0xc0121b160: Nexy> state 4
default	20:25:24.393724-0500	loginwindow	-[PersistentAppsSupport applicationQuit:] | for app:Nexy, _appTrackingState = 2
default	20:25:24.398257-0500	ControlCenter	Stopping tracking for host; (bid:com.nexy.assistant-Item-0-98347)
default	20:25:24.401560-0500	ControlCenter	Removing ephemeral displayable instance DisplayableId(BC04A446) from menu bar. No corresponding host (bid:com.nexy.assistant-Item-0-98347)
default	20:25:24.401621-0500	ControlCenter	Removing displayables [DisplayableAppStatusItem(BC04A446, (bid:com.nexy.assistant-Item-0-98347))]
error	20:25:24.548065-0500	runningboardd	RBSStateCapture remove item called for untracked item 400-391-144477 (target:[app<application.com.nexy.assistant.55704030.55704039(501)>:98347])
error	20:25:24.548089-0500	runningboardd	RBSStateCapture remove item called for untracked item 400-391-144476 (target:[app<application.com.nexy.assistant.55704030.55704039(501)>:98347])
default	20:25:24.746022-0500	coreaudiod	>>> NEGOTIATE [com.nexy.assistant]
default	20:25:24.746426-0500	coreaudiod	<<< NEGOTIATE [com.nexy.assistant]
default	20:25:24.749589-0500	coreaudiod	IssueReporting.cpp:492   RTAID [ use_case=Generic report_type=RMS Generic Chain clientID=ADM node=ADM::com.nexy.assistant_7690.7540.0_airpods noise suppression studio::out-0 issue_detected_sample_time=40800.000000 ] -- [ rms:[-45.816235], peaks:[-20.715057] ]
default	20:25:24.749610-0500	coreaudiod	IssueReporting.cpp:492   RTAID [ use_case=Generic report_type=RMS Generic Chain clientID=ADM node=ADM::com.nexy.assistant_7690.7540.0_airpods noise suppression studio::in-0 issue_detected_sample_time=0.000000 ] -- [ rms:[-52.978825], peaks:[-32.840179] ]
default	20:25:40.058598-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant", "scr:com.nexy.assistant"]
default	20:25:40.059995-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:25:40.060019-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:25:40.060062-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:25:40.060082-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	20:25:40.060095-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	20:25:40.060103-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	20:25:40.060602-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
