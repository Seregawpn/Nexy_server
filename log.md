default	21:01:02.661839-0400	lsd	com.nexy.assistant/Unknown Persona:5:5:1:1:Building bundle record for app
default	21:01:02.662009-0400	lsd	com.nexy.assistant/Unknown Persona:5:5:2:1:Built bundle record for app
default	21:01:02.663733-0400	lsd	com.nexy.assistant/Unknown Persona:5:4:2:1:_LSServerRegisterItemInfo result = 0
default	21:01:02.670178-0400	dmd	Received xpc stream event (distributed notification matching) with name: com.apple.LaunchServices.applicationRegistered user info: {
    CFBundleDisplayName = Nexy;
    bundleIDs =     (
        "com.nexy.assistant"
    );
    isPlaceholder = 0;
}
default	21:01:02.673945-0400	runningboardd	Launch request for app<application.com.nexy.assistant.18892826.18892833(501)>[0] is using uid 501 (divined from auid 501 euid 501)
default	21:01:02.674048-0400	runningboardd	Acquiring assertion targeting app<application.com.nexy.assistant.18892826.18892833(501)> from originator [osservice<com.apple.coreservices.uiagent(501)>:17058] with description <RBSAssertionDescriptor| "LS launch com.nexy.assistant" ID:398-17058-446004 target:app<application.com.nexy.assistant.18892826.18892833(501)> attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"LaunchRoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	21:01:02.674144-0400	runningboardd	Assertion 398-17058-446004 (target:app<application.com.nexy.assistant.18892826.18892833(501)>) will be created as active
default	21:01:02.682208-0400	runningboardd	Checking PreventLaunch: global:0 exPath:/Applications/Nexy.app/Contents/MacOS/Nexy predicates:(null) allow:(null)
default	21:01:02.682252-0400	runningboardd	Creating and launching job for: app<application.com.nexy.assistant.18892826.18892833(501)>
default	21:01:02.682269-0400	runningboardd	_mutateContextIfNeeded called for com.nexy.assistant
default	21:01:02.682329-0400	runningboardd	app<application.com.nexy.assistant.18892826.18892833(501)>: -[RBPersonaManager personaForIdentity:context:personaUID:personaUniqueString:] required 0.000000 ms (wallclock); resolved to {4294967295, (null)}
default	21:01:02.722747-0400	gamepolicyd	Hit the server for a process handle 15ebe9370000a4b1 that resolved to: [app<application.com.nexy.assistant.18892826.18892833(501)>:42161]
default	21:01:02.722790-0400	gamepolicyd	Received state update for 42161 (app<application.com.nexy.assistant.18892826.18892833(501)>, running-active-NotVisible
default	21:01:02.726948-0400	runningboardd	[app<application.com.nexy.assistant.18892826.18892833(501)>:42161] Ignoring GPU update because this process is not GPU managed
default	21:01:02.727044-0400	runningboardd	[app<application.com.nexy.assistant.18892826.18892833(501)>:42161] Ignoring memory limit update because this process is not memory-managed
default	21:01:02.727154-0400	runningboardd	[app<application.com.nexy.assistant.18892826.18892833(501)>:42161] reported to RB as running
default	21:01:02.735485-0400	runningboardd	[app<application.com.nexy.assistant.18892826.18892833(501)>:42161] Ignoring jetsam update because this process is not memory-managed
default	21:01:02.735518-0400	runningboardd	[app<application.com.nexy.assistant.18892826.18892833(501)>:42161] Ignoring suspend because this process is not lifecycle managed
default	21:01:02.735568-0400	runningboardd	[app<application.com.nexy.assistant.18892826.18892833(501)>:42161] Ignoring GPU update because this process is not GPU managed
default	21:01:02.735641-0400	runningboardd	[app<application.com.nexy.assistant.18892826.18892833(501)>:42161] Ignoring memory limit update because this process is not memory-managed
default	21:01:02.843887-0400	runningboardd	[app<application.com.nexy.assistant.18892826.18892833(501)>:42161] Ignoring jetsam update because this process is not memory-managed
default	21:01:02.843902-0400	runningboardd	[app<application.com.nexy.assistant.18892826.18892833(501)>:42161] Ignoring suspend because this process is not lifecycle managed
default	21:01:02.843914-0400	runningboardd	[app<application.com.nexy.assistant.18892826.18892833(501)>:42161] Ignoring GPU update because this process is not GPU managed
default	21:01:02.843938-0400	runningboardd	[app<application.com.nexy.assistant.18892826.18892833(501)>:42161] Ignoring memory limit update because this process is not memory-managed
default	21:01:02.844306-0400	gamepolicyd	Received state update for 42161 (app<application.com.nexy.assistant.18892826.18892833(501)>, running-active-NotVisible
default	21:01:02.848790-0400	gamepolicyd	Received state update for 42161 (app<application.com.nexy.assistant.18892826.18892833(501)>, running-active-NotVisible
default	21:01:02.956835-0400	syspolicyd	GK evaluateScanResult: 3, PST: (path: a2cffff67b96be6e), (team: 5NKLL2CLB9), (id: com.nexy.assistant), (bundle_id: (null)), 0, 0, 1, 0, 9, 4, 1
default	21:01:02.967001-0400	tccd	AUTHREQ_SUBJECT: msgID=511.68, subject=com.nexy.assistant,
default	21:01:03.416488-0400	Nexy	[0x10386e0b0] activating connection: mach=true listener=false peer=false name=com.apple.cfprefsd.daemon
default	21:01:03.416577-0400	Nexy	[0x10386f060] activating connection: mach=true listener=false peer=false name=com.apple.cfprefsd.agent
error	21:01:03.559458-0400	Nexy	dlsym cannot find symbol NSMakeRect in CFBundle 0x1038583e0 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	21:01:03.559691-0400	Nexy	dlsym cannot find symbol NSMakePoint in CFBundle 0x1038583e0 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	21:01:03.559900-0400	Nexy	dlsym cannot find symbol NSMakeSize in CFBundle 0x1038583e0 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	21:01:03.560110-0400	Nexy	dlsym cannot find symbol NSMakeRange in CFBundle 0x1038583e0 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
default	21:01:03.654886-0400	Nexy	Registered notify signal com.apple.caulk.alloc.rtdump (0)
default	21:01:03.658365-0400	Nexy	System_Input_Processing_Notification_Handler.mm:456   System_Input_Processing_Notification_Handler::is_vi_available(): Voice isolation DSP is available for client with bundle id com.nexy.assistant (AVFoundation is available, application is not in client deny list, application is not FaceTime variant)
default	21:01:03.659873-0400	Nexy	[0x103854200] activating connection: mach=true listener=false peer=false name=com.apple.cmio.registerassistantservice.system-extensions
fault	21:01:03.662795-0400	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.18892826.18892833 AUID=501> and <type=Application identifier=application.com.nexy.assistant.18892826.18892833>
default	21:01:03.667717-0400	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOInitializeListenersForBundleID: for <private> -> <private>
default	21:01:03.669712-0400	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> vpio_preferenceChangedListener: new value ((null)) for key AUVoiceIOClients/com-nexy-assistant/AUVoiceIOChatFlavor, translatedBundleID com.nexy.assistant, bundleIDs {(
    "com.nexy.assistant"
)}
default	21:01:03.669893-0400	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> vpio_preferenceChangedListener: new value ((null)) for key AUVoiceIOClients/com-nexy-assistant/AUVoiceIOIsAutoChatFlavorEnabled, translatedBundleID com.nexy.assistant, bundleIDs {(
    "com.nexy.assistant"
)}
default	21:01:03.670034-0400	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetSupportedChatFlavorsForBundleID: <private>-><private> get supported chat flavors: <private>
default	21:01:03.670044-0400	Nexy	            HALSystem.cpp:134    Enabling HAL Voice Isolation support
default	21:01:03.670082-0400	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetHiddenChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	21:01:03.670264-0400	Nexy	[0xc9589c000] activating connection: mach=true listener=false peer=false name=com.apple.tccd
default	21:01:03.670517-0400	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOHiddenChatFlavors newValue: (
    1
)
default	21:01:03.670856-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=42161.1, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=42161, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	21:01:03.677119-0400	tccd	AUTHREQ_SUBJECT: msgID=42161.1, subject=com.nexy.assistant,
default	21:01:03.677788-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc05108c00 at /Applications/Nexy.app
default	21:01:03.690126-0400	Nexy	[0xc9589c000] invalidated after the last release of the connection object
default	21:01:03.690174-0400	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetSupportedChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	21:01:03.692962-0400	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOSupportedChatFlavors newValue: (
)
default	21:01:03.694320-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=401.3620, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=42161, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	21:01:03.695138-0400	tccd	AUTHREQ_SUBJECT: msgID=401.3620, subject=com.nexy.assistant,
default	21:01:03.695723-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc05108c00 at /Applications/Nexy.app
error	21:01:03.708096-0400	tccd	Request message contains a target_token to accessing_process (TCCDProcess: identifier=com.nexy.assistant, pid=42161, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy) but TCCDProcess: identifier=com.apple.audio.coreaudiod, pid=401, auid=202, euid=202, binary_path=/usr/sbin/coreaudiod is not a TCC manager for service: kTCCServiceScreenCapture.
default	21:01:03.709026-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=401.3622, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=42161, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	21:01:03.709763-0400	tccd	AUTHREQ_SUBJECT: msgID=401.3622, subject=com.nexy.assistant,
default	21:01:03.710270-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc05108c00 at /Applications/Nexy.app
default	21:01:03.724992-0400	Nexy	  HALPlugInManagement.cpp:440    HALPlugInManagement::RegisterPlugIns: skipping in-process plug-ins
error	21:01:03.725017-0400	Nexy	AddInstanceForFactory: No factory registered for id <CFUUID 0xc94c04140> F8BB1C28-BAE8-11D6-9C31-00039315CD46
default	21:01:03.746500-0400	Nexy	     HALC_ProxyObject.cpp:1456   HALC_Object_PropertyListener: not initialized
default	21:01:03.749135-0400	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	21:01:03.749268-0400	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	21:01:03.754220-0400	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetPreferredChatFlavorForBundleID: <private>-><private> get value: 0
default	21:01:06.108649-0400	kernel	SK[6]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid CD478726-AA11-49E8-B5F6-001E2585A04D flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.63263,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0x95d3d54d tp_proto=0x06"
default	21:01:06.108786-0400	kernel	tcp connect outgoing: [<IPv4-redacted>:63263<-><IPv4-redacted>:53] interface: en0 (skipped: 871)
so_gencnt: 2264427 t_state: SYN_SENT process: Nexy:42161 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xb5bc8159
default	21:01:08.667604-0400	runningboardd	Assertion did invalidate due to timeout: 398-398-446005 (target:[app<application.com.nexy.assistant.18892826.18892833(501)>:42161])
default	21:01:08.868428-0400	runningboardd	[app<application.com.nexy.assistant.18892826.18892833(501)>:42161] Ignoring jetsam update because this process is not memory-managed
default	21:01:08.868495-0400	runningboardd	[app<application.com.nexy.assistant.18892826.18892833(501)>:42161] Ignoring suspend because this process is not lifecycle managed
default	21:01:08.868518-0400	runningboardd	[app<application.com.nexy.assistant.18892826.18892833(501)>:42161] Ignoring GPU update because this process is not GPU managed
default	21:01:08.868551-0400	runningboardd	[app<application.com.nexy.assistant.18892826.18892833(501)>:42161] Ignoring memory limit update because this process is not memory-managed
default	21:01:08.874238-0400	runningboardd	Calculated state for app<application.com.nexy.assistant.18892826.18892833(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	21:01:08.874993-0400	gamepolicyd	Received state update for 42161 (app<application.com.nexy.assistant.18892826.18892833(501)>, running-active-NotVisible
default	21:01:11.109760-0400	kernel	tcp_connection_summary (tcp_close:1692)[<IPv4-redacted>:63263<-><IPv4-redacted>:53] interface: en0 (skipped: 871)
so_gencnt: 2264427 t_state: SYN_SENT process: Nexy:42161 Duration: 5.001 sec Conn_Time: 0.000 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 0.000 ms rttvar: 250.000 ms base rtt: 0 ms so_error: 0 svc/tc: 0 flow: 0xb5bc8159
default	21:01:11.109792-0400	kernel	tcp_connection_summary [<IPv4-redacted>:63263<-><IPv4-redacted>:53] interface: en0 (skipped: 871)
so_gencnt: 2264427 t_state: SYN_SENT process: Nexy:42161 flowctl: 0us (0x) SYN in/out: 0/5 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	21:01:11.110397-0400	kernel	SK[3]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 5D5D3BAD-062E-45C3-8021-9A295F4D58BF flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.63266,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0x6e97bb72 tp_proto=0x06"
default	21:01:11.110526-0400	kernel	tcp connect outgoing: [<IPv4-redacted>:63266<-><IPv4-redacted>:53] interface: en0 (skipped: 871)
so_gencnt: 2264438 t_state: SYN_SENT process: Nexy:42161 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x81f19e66
default	21:01:16.111347-0400	kernel	tcp_connection_summary (tcp_close:1692)[<IPv4-redacted>:63266<-><IPv4-redacted>:53] interface: en0 (skipped: 871)
so_gencnt: 2264438 t_state: SYN_SENT process: Nexy:42161 Duration: 5.001 sec Conn_Time: 0.000 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 0.000 ms rttvar: 250.000 ms base rtt: 0 ms so_error: 0 svc/tc: 0 flow: 0x81f19e66
default	21:01:16.111382-0400	kernel	tcp_connection_summary [<IPv4-redacted>:63266<-><IPv4-redacted>:53] interface: en0 (skipped: 871)
so_gencnt: 2264438 t_state: SYN_SENT process: Nexy:42161 flowctl: 0us (0x) SYN in/out: 0/5 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	21:01:16.139866-0400	Nexy	networkd_settings_read_from_file initialized networkd settings by reading plist directly
default	21:01:16.140105-0400	Nexy	networkd_settings_read_from_file initialized networkd settings by reading plist directly
default	21:01:16.141561-0400	Nexy	nw_path_libinfo_path_check [3E04212C-CAEA-4B4A-BF82-53F8478642D8 Hostname#d057373f:53 tcp, legacy-socket, attribution: developer]
	libinfo check path: <private>
default	21:01:16.141999-0400	mDNSResponder	[R275821] DNSServiceCreateConnection START PID[42161](Nexy)
default	21:01:16.142142-0400	mDNSResponder	[R275822] DNSServiceQueryRecord START -- qname: <mask.hash: '7zTTRCflEvulIXw1JStVAQ=='>, qtype: A, flags: 0x1D000, interface index: 0, client pid: 42161 (Nexy), name hash: f92d5498
default	21:01:16.143146-0400	mDNSResponder	[R275823] DNSServiceQueryRecord START -- qname: <mask.hash: '7zTTRCflEvulIXw1JStVAQ=='>, qtype: AAAA, flags: 0x1D000, interface index: 0, client pid: 42161 (Nexy), name hash: f92d5498
default	21:01:16.151982-0400	kernel	SK[7]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 86201670-5AF6-43C0-8AC2-E1573A4ECD1D flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.63268,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0xb3d6ae6d tp_proto=0x06"
default	21:01:16.152092-0400	kernel	tcp connect outgoing: [<IPv4-redacted>:63268<-><IPv4-redacted>:53] interface: en0 (skipped: 871)
so_gencnt: 2264462 t_state: SYN_SENT process: Nexy:42161 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 4 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xbc2bcbbd
default	21:01:21.112858-0400	kernel	tcp_connection_summary (tcp_close:1692)[<IPv4-redacted>:63268<-><IPv4-redacted>:53] interface: en0 (skipped: 871)
so_gencnt: 2264462 t_state: SYN_SENT process: Nexy:42161 Duration: 4.961 sec Conn_Time: 0.000 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 0.000 ms rttvar: 250.000 ms base rtt: 4 ms so_error: 0 svc/tc: 0 flow: 0xbc2bcbbd
default	21:01:21.112888-0400	kernel	tcp_connection_summary [<IPv4-redacted>:63268<-><IPv4-redacted>:53] interface: en0 (skipped: 871)
so_gencnt: 2264462 t_state: SYN_SENT process: Nexy:42161 flowctl: 0us (0x) SYN in/out: 0/12 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	21:01:21.160840-0400	Nexy	[0xc9589c000] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioComponentRegistrar
default	21:01:21.174779-0400	Nexy	                AUHAL.cpp:420   AUHAL: (0xc92cc5c40) Selecting device 85 from constructor
default	21:01:21.174791-0400	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0xc92cc5c40)
default	21:01:21.174797-0400	Nexy	                AUHAL.cpp:676   SelectDevice: (0xc92cc5c40) not already running
default	21:01:21.174799-0400	Nexy	                AUHAL.cpp:752   SelectDevice: (0xc92cc5c40) nothing to teardown
default	21:01:21.174803-0400	Nexy	                AUHAL.cpp:757   SelectDevice: (0xc92cc5c40) connecting device 85
default	21:01:21.174890-0400	Nexy	                AUHAL.cpp:3413  IsDeviceUsable: (0xc92cc5c40) Device ID: 85 (Input:No | Output:Yes): true
default	21:01:21.175376-0400	Nexy	                AUHAL.cpp:769   SelectDevice: (0xc92cc5c40) created ioproc 0xa for device 85
default	21:01:21.175472-0400	Nexy	                AUHAL.cpp:858   SelectDevice: (0xc92cc5c40) adding 7 device listeners to device 85
default	21:01:21.175621-0400	Nexy	                AUHAL.cpp:858   SelectDevice: (0xc92cc5c40) adding 0 device delegate listeners to device 85
default	21:01:21.175635-0400	Nexy	                AUHAL.cpp:1581  UpdateStreamFormats: -> (0xc92cc5c40)
default	21:01:21.175709-0400	Nexy	                AUHAL.cpp:1677  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  48000 Hz, Float32, interleaved
default	21:01:21.175720-0400	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 1 output streams; not all mono
default	21:01:21.175728-0400	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	21:01:21.175734-0400	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 0 input streams; not all mono
default	21:01:21.175743-0400	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	21:01:21.175829-0400	Nexy	                AUHAL.cpp:1771  UpdateStreamFormats: AUHAL(0xc92cc5c40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	21:01:21.175839-0400	Nexy	                AUHAL.cpp:1777  UpdateStreamFormats: AUHAL(0xc92cc5c40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	21:01:21.175846-0400	Nexy	                AUHAL.cpp:1787  UpdateStreamFormats: <-
default	21:01:21.175849-0400	Nexy	                AUHAL.cpp:895   SelectDevice: (0xc92cc5c40) removing 0 device listeners from device 0
default	21:01:21.175853-0400	Nexy	                AUHAL.cpp:895   SelectDevice: (0xc92cc5c40) removing 0 device delegate listeners from device 0
default	21:01:21.175858-0400	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0xc92cc5c40)
default	21:01:21.175874-0400	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Output stream enables: Stream 0 is DISABLED
default	21:01:21.175964-0400	Nexy	                AUHAL.cpp:2298  SetProperty: (0xc92cc5c40) caller requesting device change from 85 to 91
default	21:01:21.175971-0400	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0xc92cc5c40)
default	21:01:21.175976-0400	Nexy	                AUHAL.cpp:676   SelectDevice: (0xc92cc5c40) not already running
default	21:01:21.175980-0400	Nexy	                AUHAL.cpp:682   SelectDevice: (0xc92cc5c40) disconnecting device 85
default	21:01:21.175982-0400	Nexy	                AUHAL.cpp:746   SelectDevice: (0xc92cc5c40) destroying ioproc 0xa for device 85
default	21:01:21.176047-0400	Nexy	  AVAudioSession_MacOS.mm:1021  initForMacOS
default	21:01:21.176938-0400	Nexy	[0xc9589c280] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioSession
default	21:01:21.178349-0400	audiomxd	  ServerSessionManager.mm:315   { "action":"create_session", "session":{"ID":"0x1ef0a7","name":"Nexy(42161)"}, "details":{"PID":42161,"session_type":"Primary"} }
default	21:01:21.178450-0400	audiomxd	AudioApplicationInfoImpl.mm:250   Setting initial isRecording state: 0 for newly-created AudioApp
	app: {"name":"[implicit] Nexy","pid":42161}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1ef0a7, sessionType: 'prim', isRecording: false }, 
]
default	21:01:21.179205-0400	audiomxd	  ServerSessionManager.mm:1317  Start process monitoring, pid = 42161, name = Nexy
default	21:01:21.179460-0400	Nexy	    SessionCore_Create.mm:99    Created session 0xc957426e0 with ID: 0x1ef0a7
default	21:01:21.180483-0400	Nexy	[0xc9589c3c0] activating connection: mach=true listener=false peer=false name=com.apple.audioanalyticsd
default	21:01:21.180617-0400	Nexy	No persisted cache on this platform.
error	21:01:21.180963-0400	Nexy	Reporter disconnected. { function=sendMessage, reporterID=181080116166657 }
default	21:01:21.180979-0400	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped Unknown {1C-77-54-18-C8-A3:output, 0xa}
default	21:01:21.181032-0400	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	21:01:21.181119-0400	Nexy	                AUHAL.cpp:757   SelectDevice: (0xc92cc5c40) connecting device 91
default	21:01:21.181191-0400	Nexy	                AUHAL.cpp:3413  IsDeviceUsable: (0xc92cc5c40) Device ID: 91 (Input:Yes | Output:No): true
default	21:01:21.182610-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=401.3623, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=42161, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	21:01:21.184741-0400	tccd	AUTHREQ_SUBJECT: msgID=401.3623, subject=com.nexy.assistant,
default	21:01:21.185446-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc05108c00 at /Applications/Nexy.app
default	21:01:21.198863-0400	tccd	AUTHREQ_PROMPTING: msgID=401.3623, service=kTCCServiceMicrophone, subject=Sub:{com.nexy.assistant}Resp:{TCCDProcess: identifier=com.nexy.assistant, pid=42161, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy},
default	21:01:23.693764-0400	tccd	Publishing <TCCDEvent: type=Create, service=kTCCServiceMicrophone, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 3 subscribers: {
    471 = "<TCCDEventSubscriber: token=471, state=Passed, csid=com.apple.chronod>";
    37 = "<TCCDEventSubscriber: token=37, state=Initial, csid=(null)>";
    476 = "<TCCDEventSubscriber: token=476, state=Passed, csid=com.apple.photolibraryd>";
}
default	21:01:23.694129-0400	Nexy	                AUHAL.cpp:769   SelectDevice: (0xc92cc5c40) created ioproc 0xa for device 91
default	21:01:23.694433-0400	Nexy	                AUHAL.cpp:858   SelectDevice: (0xc92cc5c40) adding 7 device listeners to device 91
default	21:01:23.694788-0400	Nexy	                AUHAL.cpp:858   SelectDevice: (0xc92cc5c40) adding 0 device delegate listeners to device 91
default	21:01:23.694808-0400	Nexy	                AUHAL.cpp:1581  UpdateStreamFormats: -> (0xc92cc5c40)
default	21:01:23.694825-0400	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 0 output streams; not all mono
default	21:01:23.694844-0400	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Output render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	21:01:23.695103-0400	chronod	[appAuth:com.nexy.assistant] tcc authorization(s) changed
default	21:01:23.695106-0400	Nexy	                AUHAL.cpp:1677  UpdateStreamFormats: 
  input stream 0 [0x5c]:  1 ch,  24000 Hz, Float32
default	21:01:23.695126-0400	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 1 input streams; all mono
default	21:01:23.695136-0400	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Input render format:  1 ch,  24000 Hz, Float32
default	21:01:23.695312-0400	Nexy	                AUHAL.cpp:1771  UpdateStreamFormats: AUHAL(0xc92cc5c40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	21:01:23.695338-0400	Nexy	                AUHAL.cpp:1777  UpdateStreamFormats: AUHAL(0xc92cc5c40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	21:01:23.695352-0400	Nexy	                AUHAL.cpp:1787  UpdateStreamFormats: <-
default	21:01:23.695360-0400	Nexy	                AUHAL.cpp:895   SelectDevice: (0xc92cc5c40) removing 7 device listeners from device 85
default	21:01:23.695632-0400	Nexy	                AUHAL.cpp:895   SelectDevice: (0xc92cc5c40) removing 0 device delegate listeners from device 85
default	21:01:23.695646-0400	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0xc92cc5c40)
default	21:01:23.696741-0400	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	21:01:23.698982-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=401.3624, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=42161, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	21:01:23.700702-0400	tccd	AUTHREQ_SUBJECT: msgID=401.3624, subject=com.nexy.assistant,
default	21:01:23.702023-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc05108c00 at /Applications/Nexy.app
default	21:01:23.720123-0400	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	21:01:23.721326-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=401.3625, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=42161, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	21:01:23.722326-0400	tccd	AUTHREQ_SUBJECT: msgID=401.3625, subject=com.nexy.assistant,
default	21:01:23.722938-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc05108c00 at /Applications/Nexy.app
default	21:01:23.741468-0400	Nexy	Registered notify signal com.apple.caulk.alloc.audiodump (0)
default	21:01:23.743868-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=401.3626, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=42161, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	21:01:23.745872-0400	tccd	AUTHREQ_SUBJECT: msgID=401.3626, subject=com.nexy.assistant,
default	21:01:23.746716-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc05108c00 at /Applications/Nexy.app
default	21:01:23.759553-0400	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetPreferredChatFlavorForBundleID: <private>-><private> get value: 0
default	21:01:23.759911-0400	coreaudiod	>>> NEGOTIATE [com.nexy.assistant]
default	21:01:23.760051-0400	coreaudiod	<<< NEGOTIATE [com.nexy.assistant]
default	21:01:23.760130-0400	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetSupportedChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	21:01:23.762623-0400	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOSupportedChatFlavors newValue: (
    0,
    2
)
default	21:01:23.763540-0400	coreaudiod	>>> ADAPT [com.nexy.assistant]
default	21:01:23.765317-0400	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xbf63d8300] Created node ADM::com.nexy.assistant_26022.25941.0_airpods noise suppression studio::in-0 with nodeID 0 - reporting period = 10.000000, sample rate = 24000.000000
default	21:01:23.765399-0400	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xbf63d8300] Created node ADM::com.nexy.assistant_26022.25941.0_airpods noise suppression studio::out-0 with nodeID 1 - reporting period = 10.000000, sample rate = 24000.000000
default	21:01:23.859374-0400	coreaudiod	<<< ADAPT [com.nexy.assistant]
default	21:01:23.860698-0400	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:26022 called from <private>
default	21:01:23.860738-0400	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Input {1C-77-54-18-C8-A3:input, 0xa}
default	21:01:23.861007-0400	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	21:01:23.861679-0400	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:26022 called from <private>
default	21:01:23.862286-0400	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(26022)
default	21:01:23.862314-0400	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:26022 called from <private>
default	21:01:23.862504-0400	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:26022 called from <private>
default	21:01:23.865415-0400	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.18892826.18892833(501)>:42161] from originator [osservice<com.apple.powerd>:334] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:398-334-446015 target:42161 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	21:01:23.865446-0400	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(26021)
default	21:01:23.865468-0400	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:26021 called from <private>
default	21:01:23.865899-0400	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:26021 called from <private>
default	21:01:23.866163-0400	runningboardd	Assertion 398-334-446015 (target:[app<application.com.nexy.assistant.18892826.18892833(501)>:42161]) will be created as active
default	21:01:23.868036-0400	runningboardd	[app<application.com.nexy.assistant.18892826.18892833(501)>:42161] Ignoring jetsam update because this process is not memory-managed
default	21:01:23.868452-0400	runningboardd	[app<application.com.nexy.assistant.18892826.18892833(501)>:42161] Ignoring suspend because this process is not lifecycle managed
default	21:01:23.869286-0400	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	21:01:23.869738-0400	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	21:01:23.870018-0400	runningboardd	[app<application.com.nexy.assistant.18892826.18892833(501)>:42161] Ignoring GPU update because this process is not GPU managed
default	21:01:23.870138-0400	runningboardd	[app<application.com.nexy.assistant.18892826.18892833(501)>:42161] Ignoring memory limit update because this process is not memory-managed
default	21:01:23.876197-0400	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(26022)
default	21:01:23.876214-0400	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(26022)
default	21:01:23.876215-0400	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:26022 called from <private>
default	21:01:23.876251-0400	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(26022)
default	21:01:23.876261-0400	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:26022 called from <private>
default	21:01:23.876281-0400	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(26022)
default	21:01:23.876296-0400	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:26022 called from <private>
default	21:01:23.876329-0400	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:26022 called from <private>
default	21:01:23.876368-0400	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:26022 called from <private>
default	21:01:23.876389-0400	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:26022 called from <private>
default	21:01:23.876434-0400	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:26022 called from <private>
default	21:01:23.876487-0400	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:26022 called from <private>
default	21:01:23.884799-0400	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:26022 called from <private>
default	21:01:23.884805-0400	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:26022 called from <private>
default	21:01:23.886533-0400	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ef0a7","name":"Nexy(42161)"}, "details":{"deviceUIDs":["1C-77-54-18-C8-A3:input"],"implicit_category":"Record","input_running":true,"output_running":false} }
default	21:01:23.886611-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 168, PID = 42161, Name = sid:0x1ef0a7, Nexy(42161), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	21:01:23.886938-0400	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(26022)
default	21:01:23.886951-0400	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:26022 called from <private>
default	21:01:23.888020-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 168, PID = 42161, Name = sid:0x1ef0a7, Nexy(42161), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	21:01:23.888462-0400	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1ef0a7, Nexy(42161), 'prim'', AudioCategory changed to 'Record_WithBluetooth'
default	21:01:23.889076-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 168, PID = 42161, Name = sid:0x1ef0a7, Nexy(42161), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	21:01:23.889312-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 168, PID = 42161, Name = sid:0x1ef0a7, Nexy(42161), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	21:01:23.889503-0400	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 168, PID = 42161, Name = sid:0x1ef0a7, Nexy(42161), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> is going active
default	21:01:23.889653-0400	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1ef0a7, Nexy(42161), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 168 starting recording
default	21:01:23.889847-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 168, PID = 42161, Name = sid:0x1ef0a7, Nexy(42161), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	21:01:23.889866-0400	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	21:01:23.890006-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 168, PID = 42161, Name = sid:0x1ef0a7, Nexy(42161), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	21:01:23.890075-0400	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	21:01:23.890094-0400	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found 2 different sessions firstSession={clientName:'sid:0x1ef003, Browser Helper(2350), 'prim'', displayID:'company.thebrowser.browser.helper'}, secondSession={clientName:'sid:0x1ef0a7, Nexy(42161), 'prim'', displayID:'com.nexy.assistant'} but will use session={clientName:'(null)', displayID:'(null)'}
default	21:01:23.890266-0400	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [1, 0]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:input"
)}
default	21:01:23.890278-0400	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	21:01:23.890539-0400	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	21:01:23.890604-0400	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	21:01:23.890666-0400	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	21:01:23.890794-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=401.3627, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=42161, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	21:01:23.894948-0400	runningboardd	Calculated state for app<application.com.nexy.assistant.18892826.18892833(501)>: running-active (role: UserInteractive) (endowments: <private>)
fault	21:01:23.895195-0400	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.18892826.18892833 AUID=501> and <type=Application identifier=application.com.nexy.assistant.18892826.18892833>
default	21:01:23.895457-0400	runningboardd	Invalidating assertion 398-334-446015 (target:[app<application.com.nexy.assistant.18892826.18892833(501)>:42161]) from originator [osservice<com.apple.powerd>:334]
default	21:01:23.896578-0400	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:26021 called from <private>
default	21:01:23.896591-0400	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:26021 called from <private>
default	21:01:23.897681-0400	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:26021 called from <private>
default	21:01:23.897691-0400	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:26021 called from <private>
default	21:01:23.897780-0400	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(26021)
fault	21:01:23.902534-0400	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.18892826.18892833 AUID=501> and <type=Application identifier=application.com.nexy.assistant.18892826.18892833>
default	21:01:23.903987-0400	gamepolicyd	Received state update for 42161 (app<application.com.nexy.assistant.18892826.18892833(501)>, running-active-NotVisible
default	21:01:23.905908-0400	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(26021)
default	21:01:23.973459-0400	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	21:01:24.012562-0400	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:26022 called from <private>
default	21:01:24.012912-0400	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(26022)
default	21:01:24.012929-0400	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:26022 called from <private>
default	21:01:24.012934-0400	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:26022 called from <private>
default	21:01:24.014029-0400	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	21:01:24.014597-0400	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	21:01:24.015594-0400	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(26022)
default	21:01:24.015645-0400	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:26022 called from <private>
default	21:01:24.015655-0400	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:26022 called from <private>
default	21:01:24.020936-0400	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	21:01:24.021207-0400	tccd	AUTHREQ_SUBJECT: msgID=401.3628, subject=com.nexy.assistant,
default	21:01:24.024601-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc05108c00 at /Applications/Nexy.app
default	21:01:24.042579-0400	gamepolicyd	Received state update for 42161 (app<application.com.nexy.assistant.18892826.18892833(501)>, running-active-NotVisible
default	21:01:24.048648-0400	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	21:01:24.049618-0400	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	21:01:24.051305-0400	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	21:01:24.051841-0400	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	21:01:24.055496-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	21:01:24.055537-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	21:01:24.055552-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	21:01:24.055603-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	21:01:24.055666-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	21:01:24.055752-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	21:01:24.056694-0400	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	21:01:24.059767-0400	coreaudiod	>>> ADAPT [com.nexy.assistant]
default	21:01:24.114428-0400	coreaudiod	<<< ADAPT [com.nexy.assistant]
default	21:01:24.117042-0400	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:26022 called from <private>
default	21:01:24.117829-0400	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.18892826.18892833(501)>:42161] from originator [osservice<com.apple.powerd>:334] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:398-334-446020 target:42161 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	21:01:24.118108-0400	runningboardd	Assertion 398-334-446020 (target:[app<application.com.nexy.assistant.18892826.18892833(501)>:42161]) will be created as active
default	21:01:24.118403-0400	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:26022 called from <private>
default	21:01:24.118541-0400	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	21:01:24.120007-0400	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:26022 called from <private>
default	21:01:24.120784-0400	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(26022)
default	21:01:24.120809-0400	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:26022 called from <private>
default	21:01:24.120815-0400	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:26022 called from <private>
default	21:01:24.122529-0400	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	21:01:24.122574-0400	runningboardd	Invalidating assertion 398-334-446020 (target:[app<application.com.nexy.assistant.18892826.18892833(501)>:42161]) from originator [osservice<com.apple.powerd>:334]
default	21:01:24.122910-0400	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	21:01:24.123960-0400	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(26022)
default	21:01:24.124166-0400	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:26022 called from <private>
default	21:01:24.124177-0400	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:26022 called from <private>
default	21:01:24.124190-0400	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:26022 called from <private>
default	21:01:24.127119-0400	runningboardd	[app<application.com.nexy.assistant.18892826.18892833(501)>:42161] Ignoring jetsam update because this process is not memory-managed
default	21:01:24.127145-0400	runningboardd	[app<application.com.nexy.assistant.18892826.18892833(501)>:42161] Ignoring suspend because this process is not lifecycle managed
default	21:01:24.127161-0400	runningboardd	[app<application.com.nexy.assistant.18892826.18892833(501)>:42161] Ignoring GPU update because this process is not GPU managed
default	21:01:24.127198-0400	runningboardd	[app<application.com.nexy.assistant.18892826.18892833(501)>:42161] Ignoring memory limit update because this process is not memory-managed
default	21:01:24.127490-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=401.3629, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=42161, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	21:01:24.129844-0400	tccd	AUTHREQ_SUBJECT: msgID=401.3629, subject=com.nexy.assistant,
default	21:01:24.131516-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc05108c00 at /Applications/Nexy.app
default	21:01:24.131999-0400	gamepolicyd	Received state update for 42161 (app<application.com.nexy.assistant.18892826.18892833(501)>, running-active-NotVisible
default	21:01:24.168190-0400	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.18892826.18892833(501)>:42161] from originator [osservice<com.apple.powerd>:334] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:398-334-446021 target:42161 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	21:01:24.168283-0400	runningboardd	Assertion 398-334-446021 (target:[app<application.com.nexy.assistant.18892826.18892833(501)>:42161]) will be created as active
default	21:01:24.168658-0400	runningboardd	[app<application.com.nexy.assistant.18892826.18892833(501)>:42161] Ignoring jetsam update because this process is not memory-managed
default	21:01:24.168673-0400	runningboardd	[app<application.com.nexy.assistant.18892826.18892833(501)>:42161] Ignoring suspend because this process is not lifecycle managed
default	21:01:24.168689-0400	runningboardd	[app<application.com.nexy.assistant.18892826.18892833(501)>:42161] Ignoring GPU update because this process is not GPU managed
default	21:01:24.168751-0400	runningboardd	[app<application.com.nexy.assistant.18892826.18892833(501)>:42161] Ignoring memory limit update because this process is not memory-managed
default	21:01:24.181921-0400	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	21:01:24.182059-0400	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	21:01:24.182162-0400	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	21:01:24.182846-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	21:01:24.182861-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	21:01:24.182902-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	21:01:24.182939-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	21:01:24.183000-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	21:01:24.183072-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	21:01:24.183090-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	21:01:24.183100-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	21:01:24.183109-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	21:01:24.183115-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	21:01:24.183203-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	21:01:24.183213-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	21:01:24.183376-0400	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	21:01:24.183789-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	21:01:24.183831-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	21:01:24.183887-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	21:01:24.183926-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	21:01:24.183938-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	21:01:24.183947-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	21:01:24.184535-0400	ControlCenter	Navigating to new application [com.nexy.assistant]
default	21:01:25.197673-0400	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xa}
default	21:01:25.198127-0400	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ef0a7","name":"Nexy(42161)"}, "details":{"deviceUIDs":[],"implicit_category":"","input_running":false,"output_running":false} }
default	21:01:25.198297-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 168, PID = 42161, Name = sid:0x1ef0a7, Nexy(42161), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	21:01:25.198410-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 168, PID = 42161, Name = sid:0x1ef0a7, Nexy(42161), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	21:01:25.198456-0400	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found 2 different sessions firstSession={clientName:'sid:0x1ef003, Browser Helper(2350), 'prim'', displayID:'company.thebrowser.browser.helper'}, secondSession={clientName:'sid:0x1ef0a7, Nexy(42161), 'prim'', displayID:'com.nexy.assistant'} but will use session={clientName:'(null)', displayID:'(null)'}
default	21:01:25.198509-0400	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	21:01:25.198518-0400	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1ef0a7, Nexy(42161), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 168 stopping recording
default	21:01:25.198550-0400	audiomxd	-MXCoreSession- -[MXCoreSession endInterruption:]: Session <ID: 168, PID = 42161, Name = sid:0x1ef0a7, Nexy(42161), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> is going inactive
default	21:01:25.198580-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 168, PID = 42161, Name = sid:0x1ef0a7, Nexy(42161), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	21:01:25.198612-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 168, PID = 42161, Name = sid:0x1ef0a7, Nexy(42161), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	21:01:25.198870-0400	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 0]. BT device UIDS: {(
)}
default	21:01:25.198884-0400	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	21:01:25.199255-0400	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 200 flag 0x1 < Hijack > app com.nexy.assistant CID 0xD310001 category Not set
default	21:01:25.201162-0400	audiomxd	UpdateAudioState CID 0xD310001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	21:01:25.201355-0400	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	21:01:25.201502-0400	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	21:01:25.201579-0400	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	21:01:25.201627-0400	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	21:01:25.201687-0400	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	21:01:25.201719-0400	runningboardd	Invalidating assertion 398-334-446021 (target:[app<application.com.nexy.assistant.18892826.18892833(501)>:42161]) from originator [osservice<com.apple.powerd>:334]
default	21:01:25.202214-0400	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	21:01:25.202286-0400	audioaccessoryd	AudioStateChanged: Removed audio session app com.nexy.assistant 201 count 2
default	21:01:25.205647-0400	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	21:01:25.209017-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	21:01:25.209036-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	21:01:25.209052-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	21:01:25.209062-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	21:01:25.209069-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	21:01:25.209078-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	21:01:25.209203-0400	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	21:01:25.299782-0400	Nexy	                AUHAL.cpp:473   ~AUHAL: (0xc92cc5c40) Selecting device 0 from destructor
default	21:01:25.299804-0400	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0xc92cc5c40)
default	21:01:25.299814-0400	Nexy	                AUHAL.cpp:676   SelectDevice: (0xc92cc5c40) not already running
default	21:01:25.299822-0400	Nexy	                AUHAL.cpp:682   SelectDevice: (0xc92cc5c40) disconnecting device 91
default	21:01:25.299829-0400	Nexy	                AUHAL.cpp:746   SelectDevice: (0xc92cc5c40) destroying ioproc 0xa for device 91
default	21:01:25.299873-0400	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xa}
default	21:01:25.299933-0400	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	21:01:25.300156-0400	Nexy	                AUHAL.cpp:848   SelectDevice: (0xc92cc5c40) nothing to setup
default	21:01:25.300173-0400	Nexy	                AUHAL.cpp:858   SelectDevice: (0xc92cc5c40) adding 0 device listeners to device 0
default	21:01:25.300183-0400	Nexy	                AUHAL.cpp:858   SelectDevice: (0xc92cc5c40) adding 0 device delegate listeners to device 0
default	21:01:25.300190-0400	Nexy	                AUHAL.cpp:895   SelectDevice: (0xc92cc5c40) removing 7 device listeners from device 91
default	21:01:25.300472-0400	Nexy	                AUHAL.cpp:895   SelectDevice: (0xc92cc5c40) removing 0 device delegate listeners from device 91
default	21:01:25.300498-0400	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0xc92cc5c40)
default	21:01:25.304860-0400	runningboardd	[app<application.com.nexy.assistant.18892826.18892833(501)>:42161] Ignoring jetsam update because this process is not memory-managed
default	21:01:25.304872-0400	runningboardd	[app<application.com.nexy.assistant.18892826.18892833(501)>:42161] Ignoring suspend because this process is not lifecycle managed
default	21:01:25.304883-0400	runningboardd	[app<application.com.nexy.assistant.18892826.18892833(501)>:42161] Ignoring GPU update because this process is not GPU managed
default	21:01:25.304909-0400	runningboardd	[app<application.com.nexy.assistant.18892826.18892833(501)>:42161] Ignoring memory limit update because this process is not memory-managed
default	21:01:25.307949-0400	runningboardd	Calculated state for app<application.com.nexy.assistant.18892826.18892833(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	21:01:25.308583-0400	gamepolicyd	Received state update for 42161 (app<application.com.nexy.assistant.18892826.18892833(501)>, running-active-NotVisible
default	21:01:25.578063-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=42185.1, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=42161, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.osascript, pid=42185, auid=501, euid=501, binary_path=/usr/bin/osascript}, },
default	21:01:25.580081-0400	tccd	AUTHREQ_SUBJECT: msgID=42185.1, subject=com.nexy.assistant,
default	21:01:25.581036-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d116d00 at /Applications/Nexy.app
default	21:01:25.601710-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=393.5859, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=42161, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.osascript, pid=42185, auid=501, euid=501, binary_path=/usr/bin/osascript}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=393, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	21:01:25.603039-0400	tccd	AUTHREQ_SUBJECT: msgID=393.5859, subject=com.nexy.assistant,
default	21:01:25.603812-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d116d00 at /Applications/Nexy.app
default	21:01:25.643071-0400	launchservicesd	CHECKIN:0x0-0x94f94f 42185 com.nexy.assistant
default	21:01:25.644232-0400	loginwindow	-[Application updateInformation] | Got App URL: file:///Applications/Nexy.app/
default	21:01:25.644505-0400	loginwindow	-[ApplicationManager checkInAppContext:eventData:] | ApplicationManager: Checked in app : Nexy
default	21:01:25.645438-0400	runningboardd	Invalidating assertion 398-363-446006 (target:[app<application.com.nexy.assistant.18892826.18892833(501)>:42161]) from originator [osservice<com.apple.coreservices.launchservicesd>:363]
default	21:01:25.651187-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d116d00 at /Applications/Nexy.app
default	21:01:25.652005-0400	WindowServer	90377[CreateApplication]: Process creation: 0x0-0x94f94f (Nexy) connectionID: 90377 pid: 42185 in session 0x101
default	21:01:25.654409-0400	loginwindow	-[Application updateInformation] | Got App URL: file:///Applications/Nexy.app/
default	21:01:25.752087-0400	runningboardd	[app<application.com.nexy.assistant.18892826.18892833(501)>:42161] Ignoring jetsam update because this process is not memory-managed
default	21:01:25.752104-0400	runningboardd	[app<application.com.nexy.assistant.18892826.18892833(501)>:42161] Ignoring suspend because this process is not lifecycle managed
default	21:01:25.752142-0400	runningboardd	[app<application.com.nexy.assistant.18892826.18892833(501)>:42161] Set darwin role to: None
default	21:01:25.752155-0400	runningboardd	[app<application.com.nexy.assistant.18892826.18892833(501)>:42161] Ignoring GPU update because this process is not GPU managed
default	21:01:25.752173-0400	runningboardd	[app<application.com.nexy.assistant.18892826.18892833(501)>:42161] Ignoring memory limit update because this process is not memory-managed
default	21:01:25.755398-0400	runningboardd	Calculated state for app<application.com.nexy.assistant.18892826.18892833(501)>: running-suspended (role: None) (endowments: (null))
default	21:01:25.755857-0400	gamepolicyd	Received state update for 42161 (app<application.com.nexy.assistant.18892826.18892833(501)>, running-suspended-NotVisible
default	21:01:25.840837-0400	System Events	TCCAccessRequestIndirect: TCCAccessRequestIndirect with pid 42186: target_identity: {
    kTCCCodeIdentityAuditToken = {length = 32, bytes = 0xf5010000 f5010000 14000000 f5010000 ... b7860100 7c310d00 };
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
default	21:01:25.854384-0400	tccd	target_executable_path_URL: file:///Applications/Nexy.app/Contents/MacOS/Nexy
default	21:01:25.865431-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc05108900 at /Applications/Nexy.app
default	21:01:25.879657-0400	tccd	Prompting for access to indirect object System Events by Nexy
default	21:01:26.366293-0400	WindowServer	0[outside of RPC]: Process death: 0x0-0x94f94f (Nexy) connectionID: 90377 pid: 42185 in session 0x101
default	21:01:26.366332-0400	WindowServer	<BSCompoundAssertion:0x7fb0154c0> ([FocusManager:257]-deferringPolicyEvaluationSuppression) acquire for reason:process death - 0x0-0x94f94f (Nexy) acq:0x7ffb8ad20 count:1
default	21:01:26.368313-0400	WindowServer	0[outside of RPC]: [FocusManager:257] update to deferring policy requested for reason: permitted list updated - 0x0-0x94f94f removed - but we are suppressing evaluation for reasons: {(
    "process death - 0x0-0x94f94f (Nexy)"
)}
default	21:01:26.369081-0400	loginwindow	-[ApplicationManager handleCASEvent:withData:] | CAS notification for appDeath for com.nexy.assistant with asn: LSASN:{hi=0x0;lo=0x94f94f} for bundle path: /Applications/Nexy.app with URL: file:///Applications/Nexy.app/
default	21:01:26.369110-0400	loginwindow	-[ApplicationManager(AppDeathHandler) appDeathCleanupHandler:forApp:] | Termination handler for: Nexy : 9763151
default	21:01:26.369167-0400	loginwindow	-[PersistentAppsSupport applicationQuit:] | for app:Nexy, _appTrackingState = 2
default	21:01:26.369560-0400	WindowServer	0[outside of RPC]: [FocusManager:257] update to deferring policy requested for reason: permitted list updated - 0x1-0xa4c9 removed - but we are suppressing evaluation for reasons: {(
    "process death - 0x0-0x94f94f (Nexy)"
)}
default	21:01:26.579808-0400	Nexy	                AUHAL.cpp:420   AUHAL: (0xc92cc5c40) Selecting device 85 from constructor
default	21:01:26.579821-0400	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0xc92cc5c40)
default	21:01:26.579828-0400	Nexy	                AUHAL.cpp:676   SelectDevice: (0xc92cc5c40) not already running
default	21:01:26.579832-0400	Nexy	                AUHAL.cpp:752   SelectDevice: (0xc92cc5c40) nothing to teardown
default	21:01:26.579835-0400	Nexy	                AUHAL.cpp:757   SelectDevice: (0xc92cc5c40) connecting device 85
default	21:01:26.579982-0400	Nexy	                AUHAL.cpp:3413  IsDeviceUsable: (0xc92cc5c40) Device ID: 85 (Input:No | Output:Yes): true
default	21:01:26.580131-0400	Nexy	                AUHAL.cpp:769   SelectDevice: (0xc92cc5c40) created ioproc 0xb for device 85
default	21:01:26.580348-0400	Nexy	                AUHAL.cpp:858   SelectDevice: (0xc92cc5c40) adding 7 device listeners to device 85
default	21:01:26.580529-0400	Nexy	                AUHAL.cpp:858   SelectDevice: (0xc92cc5c40) adding 0 device delegate listeners to device 85
default	21:01:26.580535-0400	Nexy	                AUHAL.cpp:1581  UpdateStreamFormats: -> (0xc92cc5c40)
default	21:01:26.580645-0400	Nexy	                AUHAL.cpp:1677  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  24000 Hz, Float32, interleaved
default	21:01:26.580652-0400	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 1 output streams; not all mono
default	21:01:26.580658-0400	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Output render format:  2 ch,  24000 Hz, Float32, interleaved
default	21:01:26.580667-0400	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 0 input streams; not all mono
default	21:01:26.580674-0400	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	21:01:26.580794-0400	Nexy	                AUHAL.cpp:1771  UpdateStreamFormats: AUHAL(0xc92cc5c40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	21:01:26.580806-0400	Nexy	                AUHAL.cpp:1777  UpdateStreamFormats: AUHAL(0xc92cc5c40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	21:01:26.580811-0400	Nexy	                AUHAL.cpp:1787  UpdateStreamFormats: <-
default	21:01:26.580816-0400	Nexy	                AUHAL.cpp:895   SelectDevice: (0xc92cc5c40) removing 0 device listeners from device 0
default	21:01:26.580821-0400	Nexy	                AUHAL.cpp:895   SelectDevice: (0xc92cc5c40) removing 0 device delegate listeners from device 0
default	21:01:26.580825-0400	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0xc92cc5c40)
default	21:01:26.580845-0400	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Output stream enables: Stream 0 is DISABLED
default	21:01:26.580924-0400	Nexy	                AUHAL.cpp:2298  SetProperty: (0xc92cc5c40) caller requesting device change from 85 to 91
default	21:01:26.580935-0400	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0xc92cc5c40)
default	21:01:26.580939-0400	Nexy	                AUHAL.cpp:676   SelectDevice: (0xc92cc5c40) not already running
default	21:01:26.580943-0400	Nexy	                AUHAL.cpp:682   SelectDevice: (0xc92cc5c40) disconnecting device 85
default	21:01:26.580946-0400	Nexy	                AUHAL.cpp:746   SelectDevice: (0xc92cc5c40) destroying ioproc 0xb for device 85
default	21:01:26.580990-0400	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped Unknown {1C-77-54-18-C8-A3:output, 0xb}
default	21:01:26.581139-0400	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	21:01:26.581298-0400	Nexy	                AUHAL.cpp:757   SelectDevice: (0xc92cc5c40) connecting device 91
default	21:01:26.581454-0400	Nexy	                AUHAL.cpp:3413  IsDeviceUsable: (0xc92cc5c40) Device ID: 91 (Input:Yes | Output:No): true
default	21:01:26.583352-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=401.3630, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=42161, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	21:01:26.588721-0400	tccd	AUTHREQ_SUBJECT: msgID=401.3630, subject=com.nexy.assistant,
default	21:01:26.589477-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc05108900 at /Applications/Nexy.app
default	21:01:26.603630-0400	Nexy	                AUHAL.cpp:769   SelectDevice: (0xc92cc5c40) created ioproc 0xb for device 91
default	21:01:26.603766-0400	Nexy	                AUHAL.cpp:858   SelectDevice: (0xc92cc5c40) adding 7 device listeners to device 91
default	21:01:26.603949-0400	Nexy	                AUHAL.cpp:858   SelectDevice: (0xc92cc5c40) adding 0 device delegate listeners to device 91
default	21:01:26.603957-0400	Nexy	                AUHAL.cpp:1581  UpdateStreamFormats: -> (0xc92cc5c40)
default	21:01:26.603967-0400	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 0 output streams; not all mono
default	21:01:26.603984-0400	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Output render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	21:01:26.604111-0400	Nexy	                AUHAL.cpp:1677  UpdateStreamFormats: 
  input stream 0 [0x5c]:  1 ch,  24000 Hz, Float32
default	21:01:26.604118-0400	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 1 input streams; all mono
default	21:01:26.604125-0400	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Input render format:  1 ch,  24000 Hz, Float32
default	21:01:26.604201-0400	Nexy	                AUHAL.cpp:1771  UpdateStreamFormats: AUHAL(0xc92cc5c40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	21:01:26.604216-0400	Nexy	                AUHAL.cpp:1777  UpdateStreamFormats: AUHAL(0xc92cc5c40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	21:01:26.604219-0400	Nexy	                AUHAL.cpp:1787  UpdateStreamFormats: <-
default	21:01:26.604223-0400	Nexy	                AUHAL.cpp:895   SelectDevice: (0xc92cc5c40) removing 7 device listeners from device 85
default	21:01:26.604559-0400	Nexy	                AUHAL.cpp:895   SelectDevice: (0xc92cc5c40) removing 0 device delegate listeners from device 85
default	21:01:26.604566-0400	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0xc92cc5c40)
default	21:01:26.605205-0400	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	21:01:26.606417-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=401.3631, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=42161, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	21:01:26.607389-0400	tccd	AUTHREQ_SUBJECT: msgID=401.3631, subject=com.nexy.assistant,
default	21:01:26.607964-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc05108900 at /Applications/Nexy.app
default	21:01:26.622102-0400	Nexy	       ACv2Workarounds.mm:51    com.nexy.assistant: fix84702776_86723525_86479548_89800354_SinglePacketDesc: false
default	21:01:26.622328-0400	Nexy	       AudioConverter.cpp:1042  Created a new in process converter -> 0xc9571da40, from  1 ch,  24000 Hz, Float32 to  1 ch,  16000 Hz, Float32
default	21:01:26.622562-0400	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	21:01:26.623706-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=401.3632, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=42161, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	21:01:26.624615-0400	tccd	AUTHREQ_SUBJECT: msgID=401.3632, subject=com.nexy.assistant,
default	21:01:26.625173-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc05108900 at /Applications/Nexy.app
default	21:01:26.640178-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=401.3633, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=42161, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	21:01:26.641026-0400	tccd	AUTHREQ_SUBJECT: msgID=401.3633, subject=com.nexy.assistant,
default	21:01:26.641563-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc05108900 at /Applications/Nexy.app
default	21:01:26.658538-0400	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Input {1C-77-54-18-C8-A3:input, 0xb}
default	21:01:26.659135-0400	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.18892826.18892833(501)>:42161] from originator [osservice<com.apple.powerd>:334] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:398-334-446032 target:42161 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	21:01:26.659245-0400	runningboardd	Assertion 398-334-446032 (target:[app<application.com.nexy.assistant.18892826.18892833(501)>:42161]) will be created as active
default	21:01:26.659564-0400	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ef0a7","name":"Nexy(42161)"}, "details":{"deviceUIDs":["1C-77-54-18-C8-A3:input"],"implicit_category":"Record","input_running":true,"output_running":false} }
default	21:01:26.659589-0400	runningboardd	[app<application.com.nexy.assistant.18892826.18892833(501)>:42161] Ignoring jetsam update because this process is not memory-managed
default	21:01:26.659601-0400	runningboardd	[app<application.com.nexy.assistant.18892826.18892833(501)>:42161] Ignoring suspend because this process is not lifecycle managed
default	21:01:26.659646-0400	runningboardd	[app<application.com.nexy.assistant.18892826.18892833(501)>:42161] Set darwin role to: Background
default	21:01:26.659657-0400	runningboardd	[app<application.com.nexy.assistant.18892826.18892833(501)>:42161] Ignoring GPU update because this process is not GPU managed
default	21:01:26.659667-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 168, PID = 42161, Name = sid:0x1ef0a7, Nexy(42161), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	21:01:26.659704-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Category/Mode changed -- The score for sid:0x1ef0a7, Nexy(42161), 'prim'/com.nexy.assistant was not correct. Old score = 201
default	21:01:26.659708-0400	runningboardd	[app<application.com.nexy.assistant.18892826.18892833(501)>:42161] Ignoring memory limit update because this process is not memory-managed
default	21:01:26.659737-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 168, PID = 42161, Name = sid:0x1ef0a7, Nexy(42161), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	21:01:26.659790-0400	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1ef0a7, Nexy(42161), 'prim'', AudioCategory changed to 'Record_WithBluetooth'
default	21:01:26.659832-0400	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	21:01:26.659945-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 168, PID = 42161, Name = sid:0x1ef0a7, Nexy(42161), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	21:01:26.660023-0400	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	21:01:26.660032-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 168, PID = 42161, Name = sid:0x1ef0a7, Nexy(42161), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	21:01:26.660064-0400	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	21:01:26.660164-0400	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	21:01:26.660166-0400	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 168, PID = 42161, Name = sid:0x1ef0a7, Nexy(42161), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> is going active
default	21:01:26.660198-0400	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1ef0a7, Nexy(42161), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 168 starting recording
default	21:01:26.660319-0400	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	21:01:26.660391-0400	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	21:01:26.660443-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 168, PID = 42161, Name = sid:0x1ef0a7, Nexy(42161), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	21:01:26.660501-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 168, PID = 42161, Name = sid:0x1ef0a7, Nexy(42161), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	21:01:26.660614-0400	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found 2 different sessions firstSession={clientName:'sid:0x1ef003, Browser Helper(2350), 'prim'', displayID:'company.thebrowser.browser.helper'}, secondSession={clientName:'sid:0x1ef0a7, Nexy(42161), 'prim'', displayID:'com.nexy.assistant'} but will use session={clientName:'(null)', displayID:'(null)'}
default	21:01:26.660712-0400	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	21:01:26.660967-0400	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 200 flag 0x1 < Hijack > app com.nexy.assistant CID 0xD310001 category Not set
default	21:01:26.661180-0400	audiomxd	UpdateAudioState CID 0xD310001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	21:01:26.661238-0400	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	21:01:26.661262-0400	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	21:01:26.661278-0400	audioaccessoryd	AudioStateChanged: Added audio session app com.nexy.assistant NULL -> 200 count 3
default	21:01:26.661286-0400	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	21:01:26.665180-0400	runningboardd	Calculated state for app<application.com.nexy.assistant.18892826.18892833(501)>: running-active (role: Background) (endowments: (null))
default	21:01:26.666398-0400	gamepolicyd	Received state update for 42161 (app<application.com.nexy.assistant.18892826.18892833(501)>, running-active-NotVisible
default	21:01:26.666541-0400	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [1, 0]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:input"
)}
default	21:01:26.666555-0400	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	21:01:26.671257-0400	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	21:01:26.671334-0400	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	21:01:26.671391-0400	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	21:01:26.672590-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	21:01:26.672607-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	21:01:26.672620-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	21:01:26.672627-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	21:01:26.672635-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	21:01:26.672642-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	21:01:26.672669-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	21:01:26.672681-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	21:01:26.672689-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	21:01:26.672697-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	21:01:26.672703-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	21:01:26.672719-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	21:01:26.672847-0400	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	21:01:26.673609-0400	ControlCenter	Navigating to new application [com.nexy.assistant]
default	21:01:26.673727-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	21:01:26.673738-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	21:01:26.673748-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	21:01:26.673753-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	21:01:26.673768-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	21:01:26.673774-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	21:01:28.059397-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc05109200 at /Applications/Nexy.app
default	21:01:28.067959-0400	tccd	Publishing <TCCDEvent: type=Create, service=kTCCServiceAppleEvents, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 3 subscribers: {
    471 = "<TCCDEventSubscriber: token=471, state=Passed, csid=com.apple.chronod>";
    37 = "<TCCDEventSubscriber: token=37, state=Initial, csid=(null)>";
    476 = "<TCCDEventSubscriber: token=476, state=Passed, csid=com.apple.photolibraryd>";
}
default	21:01:28.074691-0400	chronod	[appAuth:com.nexy.assistant] tcc authorization(s) changed
error	21:01:32.093580-0400	Nexy	         HALC_ProxyIOContext.cpp:1623  HALC_ProxyIOContext::IOWorkLoop: skipping cycle due to overload
default	21:01:33.689336-0400	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	21:01:33.722379-0400	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xb}
default	21:01:33.722722-0400	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ef0a7","name":"Nexy(42161)"}, "details":{"deviceUIDs":[],"implicit_category":"","input_running":false,"output_running":false} }
default	21:01:33.722898-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 168, PID = 42161, Name = sid:0x1ef0a7, Nexy(42161), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	21:01:33.722975-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 168, PID = 42161, Name = sid:0x1ef0a7, Nexy(42161), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	21:01:33.723172-0400	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	21:01:33.723273-0400	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1ef0a7, Nexy(42161), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 168 stopping recording
default	21:01:33.723325-0400	audiomxd	-MXCoreSession- -[MXCoreSession endInterruption:]: Session <ID: 168, PID = 42161, Name = sid:0x1ef0a7, Nexy(42161), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> is going inactive
default	21:01:33.723377-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 168, PID = 42161, Name = sid:0x1ef0a7, Nexy(42161), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	21:01:33.723443-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 168, PID = 42161, Name = sid:0x1ef0a7, Nexy(42161), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	21:01:33.723597-0400	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 200 flag 0x1 < Hijack > app com.nexy.assistant CID 0xD310001 category Not set
default	21:01:33.723958-0400	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 0]. BT device UIDS: {(
)}
default	21:01:33.723959-0400	audiomxd	UpdateAudioState CID 0xD310001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	21:01:33.723999-0400	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	21:01:33.724039-0400	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	21:01:33.724067-0400	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	21:01:33.724069-0400	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	21:01:33.724082-0400	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	21:01:33.724127-0400	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	21:01:33.724323-0400	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	21:01:33.724349-0400	audioaccessoryd	AudioStateChanged: Removed audio session app com.nexy.assistant 201 count 3
default	21:01:33.727200-0400	runningboardd	Invalidating assertion 398-334-446032 (target:[app<application.com.nexy.assistant.18892826.18892833(501)>:42161]) from originator [osservice<com.apple.powerd>:334]
default	21:01:33.729953-0400	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	21:01:33.731683-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	21:01:33.731695-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	21:01:33.731707-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	21:01:33.731713-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	21:01:33.731720-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	21:01:33.731726-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	21:01:33.731978-0400	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	21:01:33.855372-0400	runningboardd	[app<application.com.nexy.assistant.18892826.18892833(501)>:42161] Ignoring jetsam update because this process is not memory-managed
default	21:01:33.855381-0400	runningboardd	[app<application.com.nexy.assistant.18892826.18892833(501)>:42161] Ignoring suspend because this process is not lifecycle managed
default	21:01:33.855410-0400	runningboardd	[app<application.com.nexy.assistant.18892826.18892833(501)>:42161] Set darwin role to: None
default	21:01:33.855417-0400	runningboardd	[app<application.com.nexy.assistant.18892826.18892833(501)>:42161] Ignoring GPU update because this process is not GPU managed
default	21:01:33.855431-0400	runningboardd	[app<application.com.nexy.assistant.18892826.18892833(501)>:42161] Ignoring memory limit update because this process is not memory-managed
default	21:01:33.858481-0400	runningboardd	Calculated state for app<application.com.nexy.assistant.18892826.18892833(501)>: running-suspended (role: None) (endowments: (null))
default	21:01:33.859594-0400	gamepolicyd	Received state update for 42161 (app<application.com.nexy.assistant.18892826.18892833(501)>, running-suspended-NotVisible
default	21:01:33.919964-0400	Nexy	                AUHAL.cpp:473   ~AUHAL: (0xc92cc5c40) Selecting device 0 from destructor
default	21:01:33.919981-0400	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0xc92cc5c40)
default	21:01:33.919986-0400	Nexy	                AUHAL.cpp:676   SelectDevice: (0xc92cc5c40) not already running
default	21:01:33.919998-0400	Nexy	                AUHAL.cpp:682   SelectDevice: (0xc92cc5c40) disconnecting device 91
default	21:01:33.920006-0400	Nexy	                AUHAL.cpp:746   SelectDevice: (0xc92cc5c40) destroying ioproc 0xb for device 91
default	21:01:33.920031-0400	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xb}
default	21:01:33.920058-0400	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	21:01:33.920192-0400	Nexy	                AUHAL.cpp:848   SelectDevice: (0xc92cc5c40) nothing to setup
default	21:01:33.920207-0400	Nexy	                AUHAL.cpp:858   SelectDevice: (0xc92cc5c40) adding 0 device listeners to device 0
default	21:01:33.920212-0400	Nexy	                AUHAL.cpp:858   SelectDevice: (0xc92cc5c40) adding 0 device delegate listeners to device 0
default	21:01:33.920217-0400	Nexy	                AUHAL.cpp:895   SelectDevice: (0xc92cc5c40) removing 7 device listeners from device 91
default	21:01:33.920375-0400	Nexy	                AUHAL.cpp:895   SelectDevice: (0xc92cc5c40) removing 0 device delegate listeners from device 91
default	21:01:33.920387-0400	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0xc92cc5c40)
default	21:01:33.978684-0400	Nexy	[0xc9589c500] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	21:01:33.979329-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=42161.2, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=42161, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	21:01:33.981033-0400	tccd	AUTHREQ_SUBJECT: msgID=42161.2, subject=com.nexy.assistant,
default	21:01:33.982007-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d116d00 at /Applications/Nexy.app
default	21:01:33.997975-0400	Nexy	[0xc9589c500] invalidated after the last release of the connection object
default	21:01:33.999465-0400	Nexy	[0xc9589c500] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	21:01:34.000029-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=42161.3, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=42161, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	21:01:34.001116-0400	tccd	AUTHREQ_SUBJECT: msgID=42161.3, subject=com.nexy.assistant,
default	21:01:34.001735-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d116d00 at /Applications/Nexy.app
default	21:01:34.015628-0400	Nexy	[0xc9589c500] invalidated after the last release of the connection object
default	21:01:34.016053-0400	Nexy	[0xc9589c500] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	21:01:34.016681-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=42161.4, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=42161, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	21:01:34.017874-0400	tccd	AUTHREQ_SUBJECT: msgID=42161.4, subject=com.nexy.assistant,
default	21:01:34.018591-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d116d00 at /Applications/Nexy.app
default	21:01:34.033031-0400	tccd	Notifying for access  kTCCServiceScreenCapture for target PID[42161], responsiblePID[42161], responsiblePath: /Applications/Nexy.app to UID: 501
default	21:01:34.033366-0400	Nexy	[0xc9589c500] invalidated after the last release of the connection object
default	21:01:34.106765-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d114900 at /Applications/Nexy.app
default	21:01:34.157700-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d116d00 at /Applications/Nexy.app
default	21:01:34.167411-0400	tccd	Publishing <TCCDEvent: type=Modify, service=kTCCServiceScreenCapture, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 0 subscribers: {
}
default	21:01:34.196815-0400	nehelper	Received an apps uninstalled notification with bundle IDs (
    "com.nexy.assistant"
)
default	21:01:34.197463-0400	nehelper	Received an apps uninstalled notification with bundle IDs (
    "com.nexy.assistant"
)
default	21:01:34.793427-0400	nehelper	Removing UUIDs for (
    "com.nexy.assistant"
)
default	21:01:34.799541-0400	nehelper	Handling an apps uninstalled notification with bundle IDs (
    "com.nexy.assistant"
)
default	21:01:34.824688-0400	nehelper	com.apple.preferences.networkprivacy-F67B3EA9-90A6-470B-B321-9BBD719C692B: Populating the cache with 1 UUID(s) for com.nexy.assistant
default	21:01:35.866720-0400	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(26021)
default	21:01:35.866908-0400	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:26021 called from <private>
default	21:01:35.867065-0400	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:26021 called from <private>
default	21:01:35.867144-0400	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(26022)
default	21:01:35.867208-0400	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:26022 called from <private>
default	21:01:35.867769-0400	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:26022 called from <private>
default	21:01:35.876764-0400	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:26022 called from <private>
default	21:01:35.877413-0400	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:26022 called from <private>
default	21:01:36.406532-0400	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(26021)
default	21:01:36.454381-0400	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:26021 called from <private>
default	21:01:41.191595-0400	Nexy	[0xc9589c500] activating connection: mach=true listener=false peer=false name=com.apple.distributed_notifications@Uv3
default	21:01:41.192414-0400	Nexy	[0xc9589c8c0] activating connection: mach=true listener=false peer=false name=com.apple.analyticsd
default	21:01:41.194183-0400	Nexy	Received configuration update from daemon (initial)
default	21:01:41.247766-0400	Nexy	[0xc9589ca00] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
error	21:01:41.248368-0400	tccd	TCCDProcess: identifier=com.nexy.assistant, pid=42161, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy attempted to call TCCAccessRequest for kTCCServiceAccessibility without the recommended com.apple.private.tcc.manager.check-by-audit-token entitlement
default	21:01:41.248552-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=42161.5, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=42161, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.nexy.assistant, pid=42161, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	21:01:41.249823-0400	tccd	AUTHREQ_SUBJECT: msgID=42161.5, subject=com.nexy.assistant,
default	21:01:41.250545-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117600 at /Applications/Nexy.app
default	21:01:41.265155-0400	Nexy	[0xc9589ca00] invalidated after the last release of the connection object
default	21:01:41.266010-0400	Nexy	[0xc9589ca00] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
error	21:01:41.266441-0400	tccd	TCCDProcess: identifier=com.nexy.assistant, pid=42161, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy attempted to call TCCAccessRequest for kTCCServiceAccessibility without the recommended com.apple.private.tcc.manager.check-by-audit-token entitlement
default	21:01:41.266604-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=42161.6, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=42161, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.nexy.assistant, pid=42161, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	21:01:41.267535-0400	tccd	AUTHREQ_SUBJECT: msgID=42161.6, subject=com.nexy.assistant,
default	21:01:41.268312-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117600 at /Applications/Nexy.app
default	21:01:41.282032-0400	Nexy	[0xc9589ca00] invalidated after the last release of the connection object
default	21:01:41.282090-0400	Nexy	[0xc9589ca00] activating connection: mach=true listener=false peer=false name=com.apple.universalaccessAuthWarn
default	21:01:41.282195-0400	Nexy	[0xc9589ca00] invalidated after the last release of the connection object
default	21:01:41.282537-0400	Nexy	[0xc9589cb40] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	21:01:41.283385-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=42161.7, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=42161, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	21:01:41.284439-0400	tccd	AUTHREQ_SUBJECT: msgID=42161.7, subject=com.nexy.assistant,
default	21:01:41.285132-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117600 at /Applications/Nexy.app
default	21:01:41.298234-0400	tccd	Notifying for access  kTCCServiceListenEvent for target PID[42161], responsiblePID[42161], responsiblePath: /Applications/Nexy.app to UID: 501
default	21:01:41.298593-0400	Nexy	[0xc9589cb40] invalidated after the last release of the connection object
default	21:01:41.299077-0400	Nexy	server port 0x0000be0b, session port 0x0000f007
default	21:01:41.300062-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=393.5884, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=42161, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=393, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	21:01:41.300088-0400	tccd	requestor: TCCDProcess: identifier=com.apple.WindowServer, pid=393, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=42161, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	21:01:41.300941-0400	tccd	AUTHREQ_SUBJECT: msgID=393.5884, subject=com.nexy.assistant,
default	21:01:41.301668-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117600 at /Applications/Nexy.app
default	21:01:41.307336-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117300 at /Applications/Nexy.app
default	21:01:41.327250-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d115e00 at /Applications/Nexy.app
default	21:01:41.331890-0400	kernel	SK[7]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid D7D619F3-11A2-4A90-BB11-9A9263B621C1 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.63293,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0x439e36df tp_proto=0x06"
default	21:01:41.332009-0400	Nexy	nw_path_libinfo_path_check [01CEA900-3FA7-4B59-B8AA-3EDBDFC4DA97 IPv4#6c0119df:8081 tcp, legacy-socket, attribution: developer]
	libinfo check path: <private>
default	21:01:41.332015-0400	kernel	tcp connect outgoing: [<IPv4-redacted>:63293<-><IPv4-redacted>:53] interface: en0 (skipped: 871)
so_gencnt: 2264801 t_state: SYN_SENT process: Nexy:42161 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x9d9b21ac
default	21:01:41.332509-0400	kernel	SK[9]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 086D519E-384E-4D3E-AF9D-FB7FDFCE63AA flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.63294,dst=<IPv4-redacted>.8081,proto=0x06 mask=0x0000003f,hash=0x17c52bab tp_proto=0x06"
default	21:01:41.332545-0400	kernel	tcp connect outgoing: [<IPv4-redacted>:63294<-><IPv4-redacted>:8081] interface: en0 (skipped: 871)
so_gencnt: 2264802 t_state: SYN_SENT process: Nexy:42161 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xb7d2b9d7
default	21:01:41.332814-0400	Nexy	server port 0x0000f007, session port 0x0000f007
default	21:01:41.333410-0400	Nexy	[0xc9589cb40] activating connection: mach=true listener=false peer=false name=com.apple.coreservices.launchservicesd
default	21:01:41.333702-0400	tccd	Publishing <TCCDEvent: type=Modify, service=kTCCServiceAccessibility, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 0 subscribers: {
}
default	21:01:41.337157-0400	Nexy	New connection 0xa2c13 main
default	21:01:41.338093-0400	Nexy	[0xc9589cc80] activating connection: mach=true listener=false peer=false name=com.apple.pasteboard.1
default	21:01:41.347690-0400	Nexy	[0xc9589cf00] activating connection: mach=true listener=false peer=false name=com.apple.lsd.mapdb
default	21:01:41.376496-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=393.5885, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=42161, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=393, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	21:01:41.376522-0400	tccd	requestor: TCCDProcess: identifier=com.apple.WindowServer, pid=393, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=42161, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	21:01:41.377477-0400	tccd	AUTHREQ_SUBJECT: msgID=393.5885, subject=com.nexy.assistant,
default	21:01:41.378139-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d115e00 at /Applications/Nexy.app
default	21:01:41.386229-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117600 at /Applications/Nexy.app
default	21:01:41.401680-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117300 at /Applications/Nexy.app
default	21:01:41.405534-0400	tccd	Publishing <TCCDEvent: type=Modify, service=kTCCServiceListenEvent, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 0 subscribers: {
}
default	21:01:41.945839-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117600 at /Applications/Nexy.app
default	21:01:41.961534-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117300 at /Applications/Nexy.app
default	21:01:41.972151-0400	tccd	Publishing <TCCDEvent: type=Modify, service=kTCCServiceScreenCapture, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 0 subscribers: {
}
default	21:01:42.843436-0400	kernel	udp connect: [<IPv4-redacted>:58220<-><IPv4-redacted>:50051] interface:  (skipped: 617)
so_gencnt: 2264835 so_state: 0x0002 process: Nexy:42161 bytes in/out: 0/0 pkts in/out: 0/0 error: 0 so_error: 0 svc/tc: 0 flow: 0x9c90f89c
default	21:01:42.843491-0400	kernel	udp_connection_summary [<IPv4-redacted>:58220<-><IPv4-redacted>:50051] interface:  (skipped: 617)
so_gencnt: 2264835 so_state: 0x0002 process: Nexy:42161 Duration: 0.000 sec Conn_Time: 0.000 sec bytes in/out: 0/0 pkts in/out: 0/0 rxnospace pkts/bytes: 0/0 so_error: 0 svc/tc: 0 flow: 0x9c90f89c flowctl: 0us (0x)
default	21:01:42.844229-0400	kernel	SK[1]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid CD5F74A4-7D03-4CD2-A288-DDDF8A513F93 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.63298,dst=<IPv4-redacted>.50051,proto=0x06 mask=0x0000003f,hash=0xabfad83f tp_proto=0x06"
default	21:01:42.844360-0400	kernel	tcp connect outgoing: [<IPv4-redacted>:63298<-><IPv4-redacted>:50051] interface: en0 (skipped: 871)
so_gencnt: 2264837 t_state: SYN_SENT process: Nexy:42161 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x8ef47624
default	21:01:46.332777-0400	kernel	tcp_connection_summary (tcp_close:1692)[<IPv4-redacted>:63293<-><IPv4-redacted>:53] interface: en0 (skipped: 871)
so_gencnt: 2264801 t_state: SYN_SENT process: Nexy:42161 Duration: 5.001 sec Conn_Time: 0.000 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 0.000 ms rttvar: 250.000 ms base rtt: 0 ms so_error: 0 svc/tc: 0 flow: 0x9d9b21ac
default	21:01:46.332797-0400	kernel	tcp_connection_summary [<IPv4-redacted>:63293<-><IPv4-redacted>:53] interface: en0 (skipped: 871)
so_gencnt: 2264801 t_state: SYN_SENT process: Nexy:42161 flowctl: 0us (0x) SYN in/out: 0/5 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	21:01:46.334137-0400	kernel	SK[0]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 1345A4BC-F58D-496E-84BE-42B661E86127 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.63302,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0x746c81fe tp_proto=0x06"
default	21:01:46.334290-0400	kernel	tcp connect outgoing: [<IPv4-redacted>:63302<-><IPv4-redacted>:53] interface: en0 (skipped: 871)
so_gencnt: 2264857 t_state: SYN_SENT process: Nexy:42161 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x814a9c45
default	21:01:51.334271-0400	kernel	tcp_connection_summary (tcp_close:1692)[<IPv4-redacted>:63302<-><IPv4-redacted>:53] interface: en0 (skipped: 871)
so_gencnt: 2264857 t_state: SYN_SENT process: Nexy:42161 Duration: 5.001 sec Conn_Time: 0.000 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 0.000 ms rttvar: 250.000 ms base rtt: 0 ms so_error: 0 svc/tc: 0 flow: 0x814a9c45
default	21:01:51.334300-0400	kernel	tcp_connection_summary [<IPv4-redacted>:63302<-><IPv4-redacted>:53] interface: en0 (skipped: 871)
so_gencnt: 2264857 t_state: SYN_SENT process: Nexy:42161 flowctl: 0us (0x) SYN in/out: 0/5 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	21:01:51.336599-0400	Nexy	nw_path_libinfo_path_check [87291BC1-1C53-4B40-A692-E855E2F6329E Hostname#d057373f:53 tcp, legacy-socket, attribution: developer]
	libinfo check path: <private>
default	21:01:51.336774-0400	mDNSResponder	[R275913] DNSServiceQueryRecord START -- qname: <mask.hash: '7zTTRCflEvulIXw1JStVAQ=='>, qtype: A, flags: 0x1D000, interface index: 0, client pid: 42161 (Nexy), name hash: f92d5498
default	21:01:51.337580-0400	mDNSResponder	[R275914] DNSServiceQueryRecord START -- qname: <mask.hash: '7zTTRCflEvulIXw1JStVAQ=='>, qtype: AAAA, flags: 0x1D000, interface index: 0, client pid: 42161 (Nexy), name hash: f92d5498
default	21:01:51.339261-0400	kernel	SK[2]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 9F2E9AC7-17C9-4D76-A711-274B0D8B22F4 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.63306,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0xc08bbd63 tp_proto=0x06"
default	21:01:51.339415-0400	kernel	tcp connect outgoing: [<IPv4-redacted>:63306<-><IPv4-redacted>:53] interface: en0 (skipped: 871)
so_gencnt: 2264903 t_state: SYN_SENT process: Nexy:42161 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 5 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x9a0d0f0b
default	21:01:56.337389-0400	kernel	tcp_connection_summary (tcp_close:1692)[<IPv4-redacted>:63306<-><IPv4-redacted>:53] interface: en0 (skipped: 871)
so_gencnt: 2264903 t_state: SYN_SENT process: Nexy:42161 Duration: 4.998 sec Conn_Time: 0.000 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 0.000 ms rttvar: 250.000 ms base rtt: 5 ms so_error: 0 svc/tc: 0 flow: 0x9a0d0f0b
default	21:01:56.337415-0400	kernel	tcp_connection_summary [<IPv4-redacted>:63306<-><IPv4-redacted>:53] interface: en0 (skipped: 871)
so_gencnt: 2264903 t_state: SYN_SENT process: Nexy:42161 flowctl: 0us (0x) SYN in/out: 0/12 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	21:01:58.694169-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117000 at /Applications/Nexy.app
default	21:01:58.711529-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117300 at /Applications/Nexy.app
default	21:01:58.722769-0400	tccd	Publishing <TCCDEvent: type=Modify, service=kTCCServiceListenEvent, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 0 subscribers: {
}
default	21:02:02.915911-0400	kernel	tcp_connection_summary (tcp_close:1692)[<IPv4-redacted>:63298<-><IPv4-redacted>:50051] interface: en0 (skipped: 871)
so_gencnt: 2264837 t_state: SYN_SENT process: Nexy:42161 Duration: 20.071 sec Conn_Time: 0.000 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 0.000 ms rttvar: 250.000 ms base rtt: 0 ms so_error: 0 svc/tc: 0 flow: 0x8ef47624
default	21:02:02.915937-0400	kernel	tcp_connection_summary [<IPv4-redacted>:63298<-><IPv4-redacted>:50051] interface: en0 (skipped: 871)
so_gencnt: 2264837 t_state: SYN_SENT process: Nexy:42161 flowctl: 0us (0x) SYN in/out: 0/9 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	21:02:02.917103-0400	kernel	SK[4]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid B5709723-7CF6-49C6-9DE1-E2C2EFFE2BFB flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.63315,dst=<IPv4-redacted>.50051,proto=0x06 mask=0x0000003f,hash=0x147fa1c9 tp_proto=0x06"
default	21:02:02.917326-0400	kernel	tcp connect outgoing: [<IPv4-redacted>:63315<-><IPv4-redacted>:50051] interface: en0 (skipped: 871)
so_gencnt: 2265037 t_state: SYN_SENT process: Nexy:42161 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xbf7e95b4
default	21:02:11.334078-0400	kernel	tcp_connection_summary (tcp_close:1692)[<IPv4-redacted>:63294<-><IPv4-redacted>:8081] interface: en0 (skipped: 871)
so_gencnt: 2264802 t_state: SYN_SENT process: Nexy:42161 Duration: 30.001 sec Conn_Time: 0.000 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 0.000 ms rttvar: 250.000 ms base rtt: 0 ms so_error: 0 svc/tc: 0 flow: 0xb7d2b9d7
default	21:02:11.334114-0400	kernel	tcp_connection_summary [<IPv4-redacted>:63294<-><IPv4-redacted>:8081] interface: en0 (skipped: 871)
so_gencnt: 2264802 t_state: SYN_SENT process: Nexy:42161 flowctl: 0us (0x) SYN in/out: 0/9 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	21:02:11.339293-0400	Nexy	nw_path_libinfo_path_check [DD68FB2C-347C-4B96-A618-F0F736522A98 IPv4#6c0119df:8081 tcp, legacy-socket, attribution: developer]
	libinfo check path: <private>
default	21:02:11.340121-0400	kernel	SK[1]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 4EA98ABD-3CEE-4333-9259-5F4023D6A314 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.63319,dst=<IPv4-redacted>.8081,proto=0x06 mask=0x0000003f,hash=0xd44500e1 tp_proto=0x06"
default	21:02:11.340264-0400	kernel	tcp connect outgoing: [<IPv4-redacted>:63319<-><IPv4-redacted>:8081] interface: en0 (skipped: 871)
so_gencnt: 2265054 t_state: SYN_SENT process: Nexy:42161 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x9ae97b92
default	21:02:12.852833-0400	kernel	udp connect: [<IPv4-redacted>:52308<-><IPv4-redacted>:50051] interface:  (skipped: 617)
so_gencnt: 2265058 so_state: 0x0002 process: Nexy:42161 bytes in/out: 0/0 pkts in/out: 0/0 error: 0 so_error: 0 svc/tc: 0 flow: 0x821f681b
default	21:02:12.853050-0400	kernel	udp_connection_summary [<IPv4-redacted>:52308<-><IPv4-redacted>:50051] interface:  (skipped: 617)
so_gencnt: 2265058 so_state: 0x0002 process: Nexy:42161 Duration: 0.001 sec Conn_Time: 0.000 sec bytes in/out: 0/0 pkts in/out: 0/0 rxnospace pkts/bytes: 0/0 so_error: 0 svc/tc: 0 flow: 0x821f681b flowctl: 0us (0x)
default	21:02:22.969103-0400	kernel	tcp_connection_summary (tcp_close:1692)[<IPv4-redacted>:63315<-><IPv4-redacted>:50051] interface: en0 (skipped: 871)
so_gencnt: 2265037 t_state: SYN_SENT process: Nexy:42161 Duration: 20.052 sec Conn_Time: 0.000 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 0.000 ms rttvar: 250.000 ms base rtt: 0 ms so_error: 0 svc/tc: 0 flow: 0xbf7e95b4
default	21:02:22.969141-0400	kernel	tcp_connection_summary [<IPv4-redacted>:63315<-><IPv4-redacted>:50051] interface: en0 (skipped: 871)
so_gencnt: 2265037 t_state: SYN_SENT process: Nexy:42161 flowctl: 0us (0x) SYN in/out: 0/9 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	21:02:22.970118-0400	kernel	SK[5]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 9AD10D62-7B29-40BF-A8D3-6B27B100939D flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.63324,dst=<IPv4-redacted>.50051,proto=0x06 mask=0x0000003f,hash=0xab4d0b51 tp_proto=0x06"
default	21:02:22.970280-0400	kernel	tcp connect outgoing: [<IPv4-redacted>:63324<-><IPv4-redacted>:50051] interface: en0 (skipped: 871)
so_gencnt: 2265079 t_state: SYN_SENT process: Nexy:42161 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x8b1d949a
default	21:02:26.340312-0400	kernel	SK[4]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 650F2AC3-57DF-4950-A207-BDC939407811 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.63332,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0x707b381e tp_proto=0x06"
default	21:02:26.340476-0400	kernel	tcp connect outgoing: [<IPv4-redacted>:63332<-><IPv4-redacted>:53] interface: en0 (skipped: 871)
so_gencnt: 2265140 t_state: SYN_SENT process: Nexy:42161 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x8c6525a6
default	21:02:26.371097-0400	loginwindow	-[ApplicationManager(AppDeathHandler) _appQuitTimer:] | _appQuitTimer fired for: ASN: 9763151, name: Nexy with url: file:///Applications/Nexy.app/
default	21:02:26.371448-0400	loginwindow	-[ApplicationManager(AppDeathHandler) _handleLingeringSubordinateProcesses:forApp:] | Last instance of app Nexy at /Applications/Nexy.app, handle lingering spawns.
default	21:02:26.371485-0400	loginwindow	-[ApplicationManager(AppDeathHandler) _handleLingeringSubordinateProcesses:forApp:] | Child applications for Nexy : (
)
default	21:02:26.371510-0400	loginwindow	-[ApplicationManager(AppDeathHandler) _handleLingeringSubordinateProcesses:forApp:] | App Nexy is fully cleaned up.  No user notification is necessary.  Done with handling.
default	21:02:31.340900-0400	kernel	tcp_connection_summary (tcp_close:1692)[<IPv4-redacted>:63332<-><IPv4-redacted>:53] interface: en0 (skipped: 871)
so_gencnt: 2265140 t_state: SYN_SENT process: Nexy:42161 Duration: 5.001 sec Conn_Time: 0.000 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 0.000 ms rttvar: 250.000 ms base rtt: 0 ms so_error: 0 svc/tc: 0 flow: 0x8c6525a6
default	21:02:31.340943-0400	kernel	tcp_connection_summary [<IPv4-redacted>:63332<-><IPv4-redacted>:53] interface: en0 (skipped: 871)
so_gencnt: 2265140 t_state: SYN_SENT process: Nexy:42161 flowctl: 0us (0x) SYN in/out: 0/5 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	21:02:31.341631-0400	kernel	SK[4]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid CFD0EE7B-1958-494E-999B-9A9755434645 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.63334,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0x6e0c6f96 tp_proto=0x06"
default	21:02:31.341810-0400	kernel	tcp connect outgoing: [<IPv4-redacted>:63334<-><IPv4-redacted>:53] interface: en0 (skipped: 871)
so_gencnt: 2265150 t_state: SYN_SENT process: Nexy:42161 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xbbb6e05d
default	21:02:36.342493-0400	kernel	tcp_connection_summary (tcp_close:1692)[<IPv4-redacted>:63334<-><IPv4-redacted>:53] interface: en0 (skipped: 871)
so_gencnt: 2265150 t_state: SYN_SENT process: Nexy:42161 Duration: 5.000 sec Conn_Time: 0.000 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 0.000 ms rttvar: 250.000 ms base rtt: 0 ms so_error: 0 svc/tc: 0 flow: 0xbbb6e05d
default	21:02:36.342515-0400	kernel	tcp_connection_summary [<IPv4-redacted>:63334<-><IPv4-redacted>:53] interface: en0 (skipped: 871)
so_gencnt: 2265150 t_state: SYN_SENT process: Nexy:42161 flowctl: 0us (0x) SYN in/out: 0/5 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	21:02:36.344122-0400	Nexy	nw_path_libinfo_path_check [AEDB3C26-9C0B-4955-99DE-40EEB61807E3 Hostname#d057373f:53 tcp, legacy-socket, attribution: developer]
	libinfo check path: <private>
default	21:02:36.344372-0400	mDNSResponder	[R275933] DNSServiceQueryRecord START -- qname: <mask.hash: '7zTTRCflEvulIXw1JStVAQ=='>, qtype: A, flags: 0x1D000, interface index: 0, client pid: 42161 (Nexy), name hash: f92d5498
default	21:02:36.345469-0400	mDNSResponder	[R275934] DNSServiceQueryRecord START -- qname: <mask.hash: '7zTTRCflEvulIXw1JStVAQ=='>, qtype: AAAA, flags: 0x1D000, interface index: 0, client pid: 42161 (Nexy), name hash: f92d5498
default	21:02:36.348239-0400	kernel	SK[5]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid FC7C5255-CB0D-4FE5-BC07-D4A1FB3F9BAE flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.63340,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0x77c6811f tp_proto=0x06"
default	21:02:36.348417-0400	kernel	tcp connect outgoing: [<IPv4-redacted>:63340<-><IPv4-redacted>:53] interface: en0 (skipped: 871)
so_gencnt: 2265179 t_state: SYN_SENT process: Nexy:42161 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 5 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xa3856f6d
default	21:02:41.341798-0400	kernel	tcp_connection_summary (tcp_close:1692)[<IPv4-redacted>:63319<-><IPv4-redacted>:8081] interface: en0 (skipped: 871)
so_gencnt: 2265054 t_state: SYN_SENT process: Nexy:42161 Duration: 30.002 sec Conn_Time: 0.000 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 0.000 ms rttvar: 250.000 ms base rtt: 0 ms so_error: 0 svc/tc: 0 flow: 0x9ae97b92
default	21:02:41.341835-0400	kernel	tcp_connection_summary [<IPv4-redacted>:63319<-><IPv4-redacted>:8081] interface: en0 (skipped: 871)
so_gencnt: 2265054 t_state: SYN_SENT process: Nexy:42161 flowctl: 0us (0x) SYN in/out: 0/9 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	21:02:41.343961-0400	kernel	tcp_connection_summary (tcp_close:1692)[<IPv4-redacted>:63340<-><IPv4-redacted>:53] interface: en0 (skipped: 871)
so_gencnt: 2265179 t_state: SYN_SENT process: Nexy:42161 Duration: 4.996 sec Conn_Time: 0.000 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 0.000 ms rttvar: 250.000 ms base rtt: 5 ms so_error: 0 svc/tc: 0 flow: 0xa3856f6d
default	21:02:41.343977-0400	kernel	tcp_connection_summary [<IPv4-redacted>:63340<-><IPv4-redacted>:53] interface: en0 (skipped: 871)
so_gencnt: 2265179 t_state: SYN_SENT process: Nexy:42161 flowctl: 0us (0x) SYN in/out: 0/5 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	21:02:42.415791-0400	Nexy	nw_path_libinfo_path_check [08F7017E-DF95-4283-8E74-7CB048E53ECE IPv4#6c0119df:8081 tcp, legacy-socket, attribution: developer]
	libinfo check path: <private>
default	21:02:42.416605-0400	kernel	SK[0]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 13549B33-CEBE-4E7E-912F-B51F0386C8F7 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.63344,dst=<IPv4-redacted>.8081,proto=0x06 mask=0x0000003f,hash=0x0cffcfec tp_proto=0x06"
default	21:02:42.416775-0400	kernel	tcp connect outgoing: [<IPv4-redacted>:63344<-><IPv4-redacted>:8081] interface: en0 (skipped: 871)
so_gencnt: 2265203 t_state: SYN_SENT process: Nexy:42161 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xae9acfb1
default	21:02:42.918631-0400	kernel	udp connect: [<IPv4-redacted>:61030<-><IPv4-redacted>:50051] interface:  (skipped: 617)
so_gencnt: 2265204 so_state: 0x0002 process: Nexy:42161 bytes in/out: 0/0 pkts in/out: 0/0 error: 0 so_error: 0 svc/tc: 0 flow: 0x9e1b90ed
default	21:02:42.918672-0400	kernel	udp_connection_summary [<IPv4-redacted>:61030<-><IPv4-redacted>:50051] interface:  (skipped: 617)
so_gencnt: 2265204 so_state: 0x0002 process: Nexy:42161 Duration: 0.000 sec Conn_Time: 0.000 sec bytes in/out: 0/0 pkts in/out: 0/0 rxnospace pkts/bytes: 0/0 so_error: 0 svc/tc: 0 flow: 0x9e1b90ed flowctl: 0us (0x)
default	21:02:43.040659-0400	kernel	tcp_connection_summary (tcp_close:1692)[<IPv4-redacted>:63324<-><IPv4-redacted>:50051] interface: en0 (skipped: 871)
so_gencnt: 2265079 t_state: SYN_SENT process: Nexy:42161 Duration: 20.071 sec Conn_Time: 0.000 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 0.000 ms rttvar: 250.000 ms base rtt: 0 ms so_error: 0 svc/tc: 0 flow: 0x8b1d949a
default	21:02:43.040692-0400	kernel	tcp_connection_summary [<IPv4-redacted>:63324<-><IPv4-redacted>:50051] interface: en0 (skipped: 871)
so_gencnt: 2265079 t_state: SYN_SENT process: Nexy:42161 flowctl: 0us (0x) SYN in/out: 0/9 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	21:02:43.041260-0400	kernel	SK[5]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid D0CAC4AD-3E22-4E07-87C2-13A73FDE9B46 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.63345,dst=<IPv4-redacted>.50051,proto=0x06 mask=0x0000003f,hash=0x63092c7e tp_proto=0x06"
default	21:02:43.041433-0400	kernel	tcp connect outgoing: [<IPv4-redacted>:63345<-><IPv4-redacted>:50051] interface: en0 (skipped: 871)
so_gencnt: 2265205 t_state: SYN_SENT process: Nexy:42161 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x8dadd031
default	21:03:03.052689-0400	kernel	tcp_connection_summary (tcp_close:1692)[<IPv4-redacted>:63345<-><IPv4-redacted>:50051] interface: en0 (skipped: 871)
so_gencnt: 2265205 t_state: SYN_SENT process: Nexy:42161 Duration: 20.011 sec Conn_Time: 0.000 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 0.000 ms rttvar: 250.000 ms base rtt: 0 ms so_error: 0 svc/tc: 0 flow: 0x8dadd031
default	21:03:03.052723-0400	kernel	tcp_connection_summary [<IPv4-redacted>:63345<-><IPv4-redacted>:50051] interface: en0 (skipped: 871)
so_gencnt: 2265205 t_state: SYN_SENT process: Nexy:42161 flowctl: 0us (0x) SYN in/out: 0/9 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	21:03:03.053411-0400	kernel	SK[0]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 0A09AD46-954E-4447-AA3C-36059A075D45 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.63365,dst=<IPv4-redacted>.50051,proto=0x06 mask=0x0000003f,hash=0x5da5c996 tp_proto=0x06"
default	21:03:03.053549-0400	kernel	tcp connect outgoing: [<IPv4-redacted>:63365<-><IPv4-redacted>:50051] interface: en0 (skipped: 871)
so_gencnt: 2265589 t_state: SYN_SENT process: Nexy:42161 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xb32e71ce
default	21:03:11.346168-0400	kernel	SK[4]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 939EF551-F1AE-4EA6-A053-53EF4D08C2F2 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.63368,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0xeb8ff868 tp_proto=0x06"
default	21:03:11.346327-0400	kernel	tcp connect outgoing: [<IPv4-redacted>:63368<-><IPv4-redacted>:53] interface: en0 (skipped: 871)
so_gencnt: 2265607 t_state: SYN_SENT process: Nexy:42161 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xa859b00f
default	21:03:12.418286-0400	kernel	tcp_connection_summary (tcp_close:1692)[<IPv4-redacted>:63344<-><IPv4-redacted>:8081] interface: en0 (skipped: 871)
so_gencnt: 2265203 t_state: SYN_SENT process: Nexy:42161 Duration: 30.002 sec Conn_Time: 0.000 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 0.000 ms rttvar: 250.000 ms base rtt: 0 ms so_error: 0 svc/tc: 0 flow: 0xae9acfb1
default	21:03:12.418323-0400	kernel	tcp_connection_summary [<IPv4-redacted>:63344<-><IPv4-redacted>:8081] interface: en0 (skipped: 871)
so_gencnt: 2265203 t_state: SYN_SENT process: Nexy:42161 flowctl: 0us (0x) SYN in/out: 0/9 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	21:03:12.986449-0400	kernel	udp connect: [<IPv4-redacted>:49255<-><IPv4-redacted>:50051] interface:  (skipped: 617)
so_gencnt: 2265612 so_state: 0x0002 process: Nexy:42161 bytes in/out: 0/0 pkts in/out: 0/0 error: 0 so_error: 0 svc/tc: 0 flow: 0x8a1d9e96
default	21:03:12.986493-0400	kernel	udp_connection_summary [<IPv4-redacted>:49255<-><IPv4-redacted>:50051] interface:  (skipped: 617)
so_gencnt: 2265612 so_state: 0x0002 process: Nexy:42161 Duration: 0.000 sec Conn_Time: 0.000 sec bytes in/out: 0/0 pkts in/out: 0/0 rxnospace pkts/bytes: 0/0 so_error: 0 svc/tc: 0 flow: 0x8a1d9e96 flowctl: 0us (0x)
default	21:03:14.471986-0400	Nexy	nw_path_libinfo_path_check [F0F8297C-2F47-4E83-9B4A-096A557E1D76 IPv4#6c0119df:8081 tcp, legacy-socket, attribution: developer]
	libinfo check path: <private>
default	21:03:14.472775-0400	kernel	SK[2]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid EC6BB595-8DE1-4E45-A0CC-B4FF293E7AEC flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.63370,dst=<IPv4-redacted>.8081,proto=0x06 mask=0x0000003f,hash=0x2eb1893a tp_proto=0x06"
default	21:03:14.472932-0400	kernel	tcp connect outgoing: [<IPv4-redacted>:63370<-><IPv4-redacted>:8081] interface: en0 (skipped: 871)
so_gencnt: 2265617 t_state: SYN_SENT process: Nexy:42161 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x9ee68c5a
default	21:03:16.347008-0400	kernel	tcp_connection_summary (tcp_close:1692)[<IPv4-redacted>:63368<-><IPv4-redacted>:53] interface: en0 (skipped: 871)
so_gencnt: 2265607 t_state: SYN_SENT process: Nexy:42161 Duration: 5.001 sec Conn_Time: 0.000 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 0.000 ms rttvar: 250.000 ms base rtt: 0 ms so_error: 0 svc/tc: 0 flow: 0xa859b00f
default	21:03:16.347053-0400	kernel	tcp_connection_summary [<IPv4-redacted>:63368<-><IPv4-redacted>:53] interface: en0 (skipped: 871)
so_gencnt: 2265607 t_state: SYN_SENT process: Nexy:42161 flowctl: 0us (0x) SYN in/out: 0/5 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	21:03:16.347743-0400	kernel	SK[4]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 4180A646-ABB5-4032-A10E-B89245C6887E flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.63371,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0x01ac91a1 tp_proto=0x06"
default	21:03:16.347903-0400	kernel	tcp connect outgoing: [<IPv4-redacted>:63371<-><IPv4-redacted>:53] interface: en0 (skipped: 871)
so_gencnt: 2265618 t_state: SYN_SENT process: Nexy:42161 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xb9c2aee3
default	21:03:21.348543-0400	kernel	tcp_connection_summary (tcp_close:1692)[<IPv4-redacted>:63371<-><IPv4-redacted>:53] interface: en0 (skipped: 871)
so_gencnt: 2265618 t_state: SYN_SENT process: Nexy:42161 Duration: 5.001 sec Conn_Time: 0.000 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 0.000 ms rttvar: 250.000 ms base rtt: 0 ms so_error: 0 svc/tc: 0 flow: 0xb9c2aee3
default	21:03:21.348567-0400	kernel	tcp_connection_summary [<IPv4-redacted>:63371<-><IPv4-redacted>:53] interface: en0 (skipped: 871)
so_gencnt: 2265618 t_state: SYN_SENT process: Nexy:42161 flowctl: 0us (0x) SYN in/out: 0/5 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	21:03:21.350025-0400	Nexy	nw_path_libinfo_path_check [3168A1F6-1EF3-4DE8-A53E-996DE4084E0D Hostname#d057373f:53 tcp, legacy-socket, attribution: developer]
	libinfo check path: <private>
default	21:03:21.350189-0400	mDNSResponder	[R275963] DNSServiceQueryRecord START -- qname: <mask.hash: '7zTTRCflEvulIXw1JStVAQ=='>, qtype: A, flags: 0x1D000, interface index: 0, client pid: 42161 (Nexy), name hash: f92d5498
default	21:03:21.350897-0400	mDNSResponder	[R275964] DNSServiceQueryRecord START -- qname: <mask.hash: '7zTTRCflEvulIXw1JStVAQ=='>, qtype: AAAA, flags: 0x1D000, interface index: 0, client pid: 42161 (Nexy), name hash: f92d5498
default	21:03:21.351943-0400	kernel	SK[5]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 6BD612EE-9C7D-43FF-9E51-F3247E9EC8E9 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.63374,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0xf5098f9a tp_proto=0x06"
default	21:03:21.352089-0400	kernel	tcp connect outgoing: [<IPv4-redacted>:63374<-><IPv4-redacted>:53] interface: en0 (skipped: 871)
so_gencnt: 2265635 t_state: SYN_SENT process: Nexy:42161 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 3 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xa1e3a0d8
default	21:03:23.054306-0400	kernel	tcp_connection_summary (tcp_close:1692)[<IPv4-redacted>:63365<-><IPv4-redacted>:50051] interface: en0 (skipped: 871)
so_gencnt: 2265589 t_state: SYN_SENT process: Nexy:42161 Duration: 20.001 sec Conn_Time: 0.000 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 0.000 ms rttvar: 250.000 ms base rtt: 0 ms so_error: 0 svc/tc: 0 flow: 0xb32e71ce
default	21:03:23.054347-0400	kernel	tcp_connection_summary [<IPv4-redacted>:63365<-><IPv4-redacted>:50051] interface: en0 (skipped: 871)
so_gencnt: 2265589 t_state: SYN_SENT process: Nexy:42161 flowctl: 0us (0x) SYN in/out: 0/9 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	21:03:23.055063-0400	kernel	SK[3]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid FD3FB2B1-EB63-42F9-A99E-1A1DC1708349 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.63375,dst=<IPv4-redacted>.50051,proto=0x06 mask=0x0000003f,hash=0xf30aa34f tp_proto=0x06"
default	21:03:23.055227-0400	kernel	tcp connect outgoing: [<IPv4-redacted>:63375<-><IPv4-redacted>:50051] interface: en0 (skipped: 871)
so_gencnt: 2265640 t_state: SYN_SENT process: Nexy:42161 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x8196d808
default	21:03:26.350164-0400	kernel	tcp_connection_summary (tcp_close:1692)[<IPv4-redacted>:63374<-><IPv4-redacted>:53] interface: en0 (skipped: 871)
so_gencnt: 2265635 t_state: SYN_SENT process: Nexy:42161 Duration: 4.999 sec Conn_Time: 0.000 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 0.000 ms rttvar: 250.000 ms base rtt: 3 ms so_error: 0 svc/tc: 0 flow: 0xa1e3a0d8
default	21:03:26.350208-0400	kernel	tcp_connection_summary [<IPv4-redacted>:63374<-><IPv4-redacted>:53] interface: en0 (skipped: 871)
so_gencnt: 2265635 t_state: SYN_SENT process: Nexy:42161 flowctl: 0us (0x) SYN in/out: 0/5 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	21:03:42.860476-0400	Nexy	                AUHAL.cpp:420   AUHAL: (0xc94c94040) Selecting device 85 from constructor
default	21:03:42.860508-0400	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0xc94c94040)
default	21:03:42.860517-0400	Nexy	                AUHAL.cpp:676   SelectDevice: (0xc94c94040) not already running
default	21:03:42.860526-0400	Nexy	                AUHAL.cpp:752   SelectDevice: (0xc94c94040) nothing to teardown
default	21:03:42.860532-0400	Nexy	                AUHAL.cpp:757   SelectDevice: (0xc94c94040) connecting device 85
default	21:03:42.860780-0400	Nexy	                AUHAL.cpp:3413  IsDeviceUsable: (0xc94c94040) Device ID: 85 (Input:No | Output:Yes): true
default	21:03:42.861078-0400	Nexy	                AUHAL.cpp:769   SelectDevice: (0xc94c94040) created ioproc 0xc for device 85
default	21:03:42.861273-0400	Nexy	                AUHAL.cpp:858   SelectDevice: (0xc94c94040) adding 7 device listeners to device 85
default	21:03:42.861541-0400	Nexy	                AUHAL.cpp:858   SelectDevice: (0xc94c94040) adding 0 device delegate listeners to device 85
default	21:03:42.861556-0400	Nexy	                AUHAL.cpp:1581  UpdateStreamFormats: -> (0xc94c94040)
default	21:03:42.861699-0400	Nexy	                AUHAL.cpp:1677  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  48000 Hz, Float32, interleaved
default	21:03:42.861711-0400	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 1 output streams; not all mono
default	21:03:42.861722-0400	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	21:03:42.861732-0400	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 0 input streams; not all mono
default	21:03:42.861746-0400	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	21:03:42.861893-0400	Nexy	                AUHAL.cpp:1771  UpdateStreamFormats: AUHAL(0xc94c94040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	21:03:42.861912-0400	Nexy	                AUHAL.cpp:1777  UpdateStreamFormats: AUHAL(0xc94c94040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	21:03:42.861922-0400	Nexy	                AUHAL.cpp:1787  UpdateStreamFormats: <-
default	21:03:42.861928-0400	Nexy	                AUHAL.cpp:895   SelectDevice: (0xc94c94040) removing 0 device listeners from device 0
default	21:03:42.861934-0400	Nexy	                AUHAL.cpp:895   SelectDevice: (0xc94c94040) removing 0 device delegate listeners from device 0
default	21:03:42.861942-0400	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0xc94c94040)
default	21:03:42.861963-0400	Nexy	                AUHAL.cpp:2298  SetProperty: (0xc94c94040) caller requesting device change from 85 to 85
default	21:03:42.861970-0400	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0xc94c94040)
default	21:03:42.861978-0400	Nexy	                AUHAL.cpp:659   SelectDevice: <- (0xc94c94040) exiting with nothing to do
default	21:03:42.862822-0400	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	21:03:42.863428-0400	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	21:03:42.867935-0400	Nexy	                AUHAL.cpp:473   ~AUHAL: (0xc94c94040) Selecting device 0 from destructor
default	21:03:42.867964-0400	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0xc94c94040)
default	21:03:42.867974-0400	Nexy	                AUHAL.cpp:676   SelectDevice: (0xc94c94040) not already running
default	21:03:42.867980-0400	Nexy	                AUHAL.cpp:682   SelectDevice: (0xc94c94040) disconnecting device 85
default	21:03:42.867989-0400	Nexy	                AUHAL.cpp:746   SelectDevice: (0xc94c94040) destroying ioproc 0xc for device 85
default	21:03:42.868103-0400	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Output {1C-77-54-18-C8-A3:output, 0xc}
default	21:03:42.868182-0400	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	21:03:42.868541-0400	Nexy	                AUHAL.cpp:848   SelectDevice: (0xc94c94040) nothing to setup
default	21:03:42.868556-0400	Nexy	                AUHAL.cpp:858   SelectDevice: (0xc94c94040) adding 0 device listeners to device 0
default	21:03:42.868563-0400	Nexy	                AUHAL.cpp:858   SelectDevice: (0xc94c94040) adding 0 device delegate listeners to device 0
default	21:03:42.868571-0400	Nexy	                AUHAL.cpp:895   SelectDevice: (0xc94c94040) removing 7 device listeners from device 85
default	21:03:42.868815-0400	Nexy	                AUHAL.cpp:895   SelectDevice: (0xc94c94040) removing 0 device delegate listeners from device 85
default	21:03:42.868830-0400	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0xc94c94040)
default	21:03:42.871412-0400	Nexy	                AUHAL.cpp:420   AUHAL: (0xc94c94040) Selecting device 85 from constructor
default	21:03:42.871429-0400	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0xc94c94040)
default	21:03:42.871541-0400	Nexy	                AUHAL.cpp:676   SelectDevice: (0xc94c94040) not already running
default	21:03:42.871592-0400	Nexy	                AUHAL.cpp:752   SelectDevice: (0xc94c94040) nothing to teardown
default	21:03:42.871710-0400	Nexy	                AUHAL.cpp:757   SelectDevice: (0xc94c94040) connecting device 85
default	21:03:42.871901-0400	Nexy	                AUHAL.cpp:3413  IsDeviceUsable: (0xc94c94040) Device ID: 85 (Input:No | Output:Yes): true
default	21:03:42.872327-0400	Nexy	                AUHAL.cpp:769   SelectDevice: (0xc94c94040) created ioproc 0xd for device 85
default	21:03:42.872510-0400	Nexy	                AUHAL.cpp:858   SelectDevice: (0xc94c94040) adding 7 device listeners to device 85
default	21:03:42.872772-0400	Nexy	                AUHAL.cpp:858   SelectDevice: (0xc94c94040) adding 0 device delegate listeners to device 85
default	21:03:42.872791-0400	Nexy	                AUHAL.cpp:1581  UpdateStreamFormats: -> (0xc94c94040)
default	21:03:42.872906-0400	Nexy	                AUHAL.cpp:1677  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  48000 Hz, Float32, interleaved
default	21:03:42.872921-0400	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 1 output streams; not all mono
default	21:03:42.872929-0400	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	21:03:42.872939-0400	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 0 input streams; not all mono
default	21:03:42.872950-0400	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	21:03:42.873076-0400	Nexy	                AUHAL.cpp:1771  UpdateStreamFormats: AUHAL(0xc94c94040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	21:03:42.873110-0400	Nexy	                AUHAL.cpp:1777  UpdateStreamFormats: AUHAL(0xc94c94040) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	21:03:42.873121-0400	Nexy	                AUHAL.cpp:1787  UpdateStreamFormats: <-
default	21:03:42.873127-0400	Nexy	                AUHAL.cpp:895   SelectDevice: (0xc94c94040) removing 0 device listeners from device 0
default	21:03:42.873152-0400	Nexy	                AUHAL.cpp:895   SelectDevice: (0xc94c94040) removing 0 device delegate listeners from device 0
default	21:03:42.873158-0400	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0xc94c94040)
default	21:03:42.873199-0400	Nexy	                AUHAL.cpp:2298  SetProperty: (0xc94c94040) caller requesting device change from 85 to 85
default	21:03:42.873205-0400	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0xc94c94040)
default	21:03:42.873210-0400	Nexy	                AUHAL.cpp:659   SelectDevice: <- (0xc94c94040) exiting with nothing to do
default	21:03:42.873255-0400	Nexy	AudioHardware-mac-imp.cpp:1299   AudioObjectAddPropertyListener: listener was already added
default	21:03:42.874299-0400	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	21:03:42.874697-0400	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	21:03:42.882509-0400	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.18892826.18892833(501)>:42161] from originator [osservice<com.apple.powerd>:334] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:398-334-446313 target:42161 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	21:03:42.882586-0400	runningboardd	Assertion 398-334-446313 (target:[app<application.com.nexy.assistant.18892826.18892833(501)>:42161]) will be created as active
default	21:03:42.882934-0400	runningboardd	[app<application.com.nexy.assistant.18892826.18892833(501)>:42161] Ignoring jetsam update because this process is not memory-managed
default	21:03:42.882949-0400	runningboardd	[app<application.com.nexy.assistant.18892826.18892833(501)>:42161] Ignoring suspend because this process is not lifecycle managed
default	21:03:42.883033-0400	runningboardd	[app<application.com.nexy.assistant.18892826.18892833(501)>:42161] Set darwin role to: Background
default	21:03:42.883052-0400	runningboardd	[app<application.com.nexy.assistant.18892826.18892833(501)>:42161] Ignoring GPU update because this process is not GPU managed
default	21:03:42.883079-0400	runningboardd	[app<application.com.nexy.assistant.18892826.18892833(501)>:42161] Ignoring memory limit update because this process is not memory-managed
default	21:03:42.885241-0400	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xd}
default	21:03:42.886491-0400	runningboardd	Calculated state for app<application.com.nexy.assistant.18892826.18892833(501)>: running-active (role: Background) (endowments: (null))
default	21:03:42.887263-0400	gamepolicyd	Received state update for 42161 (app<application.com.nexy.assistant.18892826.18892833(501)>, running-active-NotVisible
default	21:03:42.888755-0400	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ef0a7","name":"Nexy(42161)"}, "details":{"deviceUIDs":["1C-77-54-18-C8-A3:output"],"implicit_category":"MediaPlayback","input_running":false,"output_running":true} }
default	21:03:42.888880-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 168, PID = 42161, Name = sid:0x1ef0a7, Nexy(42161), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	21:03:42.888916-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Category/Mode changed -- The score for sid:0x1ef0a7, Nexy(42161), 'prim'/com.nexy.assistant was not correct. Old score = 201
default	21:03:42.888947-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 168, PID = 42161, Name = sid:0x1ef0a7, Nexy(42161), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	21:03:42.889025-0400	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1ef0a7, Nexy(42161), 'prim'', AudioCategory changed to 'MediaPlayback'
default	21:03:42.889051-0400	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	21:03:42.889064-0400	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 168, PID = 42161, Name = sid:0x1ef0a7, Nexy(42161), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO> is going active
default	21:03:42.889075-0400	audiomxd	-MXCoreSession- -[MXCoreSession updateIsPlaying:]: MXCoreSession com.nexy.assistant with category/mode MediaPlayback/Default and coreSessionID = 168 starting playing
default	21:03:42.889187-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 168, PID = 42161, Name = sid:0x1ef0a7, Nexy(42161), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	21:03:42.889218-0400	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	21:03:42.889269-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 168, PID = 42161, Name = sid:0x1ef0a7, Nexy(42161), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO>
default	21:03:42.889276-0400	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	21:03:42.889352-0400	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found 2 different sessions firstSession={clientName:'sid:0x1ef003, Browser Helper(2350), 'prim'', displayID:'company.thebrowser.browser.helper'}, secondSession={clientName:'sid:0x1ef0a7, Nexy(42161), 'prim'', displayID:'com.nexy.assistant'} but will use session={clientName:'(null)', displayID:'(null)'}
default	21:03:42.889445-0400	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 201, deviceID = <private>
default	21:03:42.889487-0400	audiomxd	AudioApplicationInfoImpl.mm:395   Successfully updated session 0x1ef0a7 to isSessionRecording: 0
	app: {"name":"[implicit] Nexy","pid":42161}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1ef0a7, sessionType: 'prim', isRecording: false }, 
]
default	21:03:42.889708-0400	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 201 flag 0x1 < Hijack > app com.nexy.assistant CID 0xD310001 category Not set
default	21:03:42.889933-0400	audiomxd	UpdateAudioState CID 0xD310001 audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	21:03:42.890017-0400	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 201,
}
default	21:03:42.890044-0400	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	21:03:42.890063-0400	audioaccessoryd	AudioStateChanged: Added audio session app com.nexy.assistant NULL -> 201 count 3
default	21:03:42.890074-0400	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 201
default	21:03:42.890230-0400	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 1]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)}
default	21:03:42.890247-0400	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	21:03:43.062997-0400	kernel	udp connect: [<IPv4-redacted>:58791<-><IPv4-redacted>:50051] interface:  (skipped: 617)
so_gencnt: 2265965 so_state: 0x0002 process: Nexy:42161 bytes in/out: 0/0 pkts in/out: 0/0 error: 0 so_error: 0 svc/tc: 0 flow: 0x8cb5140f
default	21:03:43.063029-0400	kernel	udp_connection_summary [<IPv4-redacted>:58791<-><IPv4-redacted>:50051] interface:  (skipped: 617)
so_gencnt: 2265965 so_state: 0x0002 process: Nexy:42161 Duration: 0.000 sec Conn_Time: 0.000 sec bytes in/out: 0/0 pkts in/out: 0/0 rxnospace pkts/bytes: 0/0 so_error: 0 svc/tc: 0 flow: 0x8cb5140f flowctl: 0us (0x)
default	21:03:43.063400-0400	kernel	SK[1]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid A1A0DBF5-79D8-4BF4-9B23-7F92E0C3CDAF flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.63402,dst=<IPv4-redacted>.50051,proto=0x06 mask=0x0000003f,hash=0x9b629539 tp_proto=0x06"
default	21:03:43.063626-0400	kernel	tcp connect outgoing: [<IPv4-redacted>:63402<-><IPv4-redacted>:50051] interface: en0 (skipped: 871)
so_gencnt: 2265966 t_state: SYN_SENT process: Nexy:42161 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xb8b005cb
default	21:03:43.082611-0400	kernel	tcp_connection_summary (tcp_close:1692)[<IPv4-redacted>:63375<-><IPv4-redacted>:50051] interface: en0 (skipped: 871)
so_gencnt: 2265640 t_state: SYN_SENT process: Nexy:42161 Duration: 20.028 sec Conn_Time: 0.000 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 0.000 ms rttvar: 250.000 ms base rtt: 0 ms so_error: 0 svc/tc: 0 flow: 0x8196d808
default	21:03:43.082634-0400	kernel	tcp_connection_summary [<IPv4-redacted>:63375<-><IPv4-redacted>:50051] interface: en0 (skipped: 871)
so_gencnt: 2265640 t_state: SYN_SENT process: Nexy:42161 flowctl: 0us (0x) SYN in/out: 0/9 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	21:03:43.219506-0400	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Output {1C-77-54-18-C8-A3:output, 0xd}
default	21:03:43.221703-0400	runningboardd	Invalidating assertion 398-334-446313 (target:[app<application.com.nexy.assistant.18892826.18892833(501)>:42161]) from originator [osservice<com.apple.powerd>:334]
default	21:03:43.222049-0400	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ef0a7","name":"Nexy(42161)"}, "details":{"deviceUIDs":[],"implicit_category":"","input_running":false,"output_running":false} }
default	21:03:43.222132-0400	audiomxd	-MXCoreSession- -[MXCoreSession updateIsPlaying:]: MXCoreSession com.nexy.assistant with category/mode MediaPlayback/Default and coreSessionID = 168 stopping playing
default	21:03:43.222179-0400	audiomxd	-MXCoreSession- -[MXCoreSession endInterruption:]: Session <ID: 168, PID = 42161, Name = sid:0x1ef0a7, Nexy(42161), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> is going inactive
default	21:03:43.222219-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 168, PID = 42161, Name = sid:0x1ef0a7, Nexy(42161), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	21:03:43.222276-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 168, PID = 42161, Name = sid:0x1ef0a7, Nexy(42161), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	21:03:43.222348-0400	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	21:03:43.222455-0400	audiomxd	AudioApplicationInfoImpl.mm:395   Successfully updated session 0x1ef0a7 to isSessionRecording: 0
	app: {"name":"[implicit] Nexy","pid":42161}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1ef0a7, sessionType: 'prim', isRecording: false }, 
]
default	21:03:43.222623-0400	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	21:03:43.222703-0400	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	21:03:43.222727-0400	audioaccessoryd	AudioStateChanged: Removed audio session app com.nexy.assistant 201 count 2
default	21:03:43.223881-0400	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 0]. BT device UIDS: {(
)}
default	21:03:43.223933-0400	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	21:03:43.328074-0400	runningboardd	[app<application.com.nexy.assistant.18892826.18892833(501)>:42161] Ignoring jetsam update because this process is not memory-managed
default	21:03:43.328095-0400	runningboardd	[app<application.com.nexy.assistant.18892826.18892833(501)>:42161] Ignoring suspend because this process is not lifecycle managed
default	21:03:43.328197-0400	runningboardd	[app<application.com.nexy.assistant.18892826.18892833(501)>:42161] Set darwin role to: None
default	21:03:43.328217-0400	runningboardd	[app<application.com.nexy.assistant.18892826.18892833(501)>:42161] Ignoring GPU update because this process is not GPU managed
default	21:03:43.328244-0400	runningboardd	[app<application.com.nexy.assistant.18892826.18892833(501)>:42161] Ignoring memory limit update because this process is not memory-managed
default	21:03:43.332282-0400	runningboardd	Calculated state for app<application.com.nexy.assistant.18892826.18892833(501)>: running-suspended (role: None) (endowments: (null))
default	21:03:43.332981-0400	gamepolicyd	Received state update for 42161 (app<application.com.nexy.assistant.18892826.18892833(501)>, running-suspended-NotVisible
default	21:03:44.474627-0400	kernel	tcp_connection_summary (tcp_close:1692)[<IPv4-redacted>:63370<-><IPv4-redacted>:8081] interface: en0 (skipped: 871)
so_gencnt: 2265617 t_state: SYN_SENT process: Nexy:42161 Duration: 30.002 sec Conn_Time: 0.000 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 0.000 ms rttvar: 250.000 ms base rtt: 0 ms so_error: 0 svc/tc: 0 flow: 0x9ee68c5a
default	21:03:44.474647-0400	kernel	tcp_connection_summary [<IPv4-redacted>:63370<-><IPv4-redacted>:8081] interface: en0 (skipped: 871)
so_gencnt: 2265617 t_state: SYN_SENT process: Nexy:42161 flowctl: 0us (0x) SYN in/out: 0/9 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	21:03:44.496330-0400	Nexy	void _NSDisableAutomaticTerminationAndLog(NSString *) No windows open yet
default	21:03:44.503423-0400	Nexy	CHECKIN: pid=42161
default	21:03:44.514208-0400	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.18892826.18892833(501)>:42161] from originator [osservice<com.apple.coreservices.launchservicesd>:363] with description <RBSAssertionDescriptor| "uielement:42161" ID:398-363-446333 target:42161 attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"RoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	21:03:44.514292-0400	runningboardd	Assertion 398-363-446333 (target:[app<application.com.nexy.assistant.18892826.18892833(501)>:42161]) will be created as active
default	21:03:44.514295-0400	launchservicesd	CHECKIN:0x0-0x965965 42161 com.nexy.assistant
default	21:03:44.514638-0400	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.18892826.18892833(501)>:42161] from originator [osservice<com.apple.coreservices.launchservicesd>:363] with description <RBSAssertionDescriptor| "uielement:42161" ID:398-363-446334 target:42161 attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"RoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	21:03:44.514647-0400	runningboardd	[app<application.com.nexy.assistant.18892826.18892833(501)>:42161] Ignoring jetsam update because this process is not memory-managed
default	21:03:44.514687-0400	runningboardd	[app<application.com.nexy.assistant.18892826.18892833(501)>:42161] Ignoring suspend because this process is not lifecycle managed
default	21:03:44.514718-0400	runningboardd	Assertion 398-363-446334 (target:[app<application.com.nexy.assistant.18892826.18892833(501)>:42161]) will be created as active
default	21:03:44.514761-0400	runningboardd	[app<application.com.nexy.assistant.18892826.18892833(501)>:42161] Set darwin role to: UserInteractive
default	21:03:44.514786-0400	runningboardd	[app<application.com.nexy.assistant.18892826.18892833(501)>:42161] Ignoring GPU update because this process is not GPU managed
default	21:03:44.514839-0400	Nexy	CHECKEDIN: pid=42161 asn=0x0-0x965965 foreground=0
default	21:03:44.514954-0400	runningboardd	[app<application.com.nexy.assistant.18892826.18892833(501)>:42161] Ignoring memory limit update because this process is not memory-managed
default	21:03:44.515245-0400	Nexy	[0xc9589d040] activating connection: mach=true listener=false peer=false name=com.apple.lsd.modifydb
default	21:03:44.517015-0400	WindowServer	a2c13[CreateApplication]: Process creation: 0x0-0x965965 (Nexy) connectionID: A2C13 pid: 42161 in session 0x101
default	21:03:44.579638-0400	Nexy	FBSWorkspace: endpoint monitoring is disabled.
default	21:03:44.579649-0400	Nexy	FBSWorkspace: default shell endpoint is disabled.
default	21:03:44.579720-0400	Nexy	Initializing connection
default	21:03:44.579768-0400	Nexy	Removing all cached process handles
default	21:03:44.579816-0400	Nexy	Sending handshake request attempt #1 to server
default	21:03:44.579854-0400	Nexy	Creating connection to com.apple.runningboard
default	21:03:44.579870-0400	Nexy	[0xc9589d180] activating connection: mach=true listener=false peer=false name=com.apple.runningboard
default	21:03:44.581314-0400	runningboardd	Setting client for [app<application.com.nexy.assistant.18892826.18892833(501)>:42161] as ready
default	21:03:44.582221-0400	Nexy	Handshake succeeded
default	21:03:44.582237-0400	Nexy	Identity resolved as app<application.com.nexy.assistant.18892826.18892833(501)>
default	21:03:44.583439-0400	Nexy	[0xc9589cdc0] Connection returned listener port: 0x14d03
default	21:03:44.584295-0400	distnoted	register name: com.apple.xctest.FakeForceTouchDevice object: com.nexy.assistant token: 2d00000024 pid: 42161
default	21:03:44.587260-0400	Nexy	[0xc9589cdc0] Connection returned listener port: 0x14d03
default	21:03:44.588893-0400	Nexy	Created a new Process Instance Registry XPC connection (inactive)
default	21:03:44.588917-0400	Nexy	[0xc9589d2c0] activating connection: mach=true listener=false peer=false name=com.apple.linkd.autoShortcut
default	21:03:44.589031-0400	Nexy	Activated connection to com.apple.linkd.autoShortcut (ApplicationService)
default	21:03:44.589153-0400	Nexy	[0xc9589d540] activating connection: mach=false listener=true peer=false name=(anonymous)
default	21:03:44.596931-0400	Nexy	[0xc9589d540] Connection returned listener port: 0x13803
default	21:03:44.597701-0400	Nexy	Registered process with identifier 42161-864587
default	21:03:44.626108-0400	WindowServer	a2c13[SetFrontProcessWithInfo]: [DeferringManager] Updating policy {
    advicePolicy: .frontmost;
    frontmostProcess: 0x0-0x965965 (Nexy) mainConnectionID: A2C13;
} for reason: updated frontmost process
default	21:03:44.626197-0400	WindowServer	a2c13[SetFrontProcessWithInfo]: [DeferringManager] Deferring events from frontmost process PSN 0x0-0x965965 (Nexy) -> <pid: 42161>
default	21:03:44.626287-0400	WindowServer	new deferring rules for pid:393: [
    [393-5CD3]; <keyboardFocus; Nexy:0x0-0x965965>; () -> <pid: 42161>; reason: frontmost PSN --> outbound target,
    [393-5CD2]; <keyboardFocus; <frontmost>>; () -> <token: Nexy:0x0-0x965965; pid: 393>; reason: frontmost PSN,
    [393-5CD1]; <keyboardFocus>; () -> <token: <frontmost>; pid: 393>; reason: Deferring to <frontmost>
]
default	21:03:44.626346-0400	WindowServer	[keyboardFocus 0x7facf2b20] setRules:forPID(393): [
    [393-5CD3]; <keyboardFocus; Nexy:0x0-0x965965>; () -> <pid: 42161>; reason: frontmost PSN --> outbound target,
    [393-5CD2]; <keyboardFocus; <frontmost>>; () -> <token: Nexy:0x0-0x965965; pid: 393>; reason: frontmost PSN,
    [393-5CD1]; <keyboardFocus>; () -> <token: <frontmost>; pid: 393>; reason: Deferring to <frontmost>
]
default	21:03:44.626533-0400	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.18892826.18892833(501)>:42161] from originator [osservice<com.apple.coreservices.launchservicesd>:363] with description <RBSAssertionDescriptor| "frontmost:42161" ID:398-363-446338 target:42161 attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"RoleUserInteractiveFocal" sourceEnvironment:"(null)">
	]>
default	21:03:44.626943-0400	runningboardd	Assertion 398-363-446338 (target:[app<application.com.nexy.assistant.18892826.18892833(501)>:42161]) will be created as active
default	21:03:44.627383-0400	WindowServer	chain did update (setDeferringRules) <keyboardFocus; display: null> containsEndOfChain: YES; [
    <token: <frontmost>; pid: 393>,
    <token: Nexy:0x0-0x965965; pid: 393>,
    <pid: 42161>
]
default	21:03:44.630328-0400	runningboardd	[app<application.com.nexy.assistant.18892826.18892833(501)>:42161] Ignoring jetsam update because this process is not memory-managed
default	21:03:44.630340-0400	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.18892826.18892833(501)>:42161] from originator [osservice<com.apple.coreservices.launchservicesd>:363] with description <RBSAssertionDescriptor| "notification:42161" ID:398-363-446339 target:42161 attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"LSNotification" sourceEnvironment:"(null)">
	]>
default	21:03:44.630343-0400	runningboardd	[app<application.com.nexy.assistant.18892826.18892833(501)>:42161] Ignoring suspend because this process is not lifecycle managed
default	21:03:44.630388-0400	runningboardd	[app<application.com.nexy.assistant.18892826.18892833(501)>:42161] Set darwin role to: UserInteractiveFocal
default	21:03:44.630410-0400	runningboardd	[app<application.com.nexy.assistant.18892826.18892833(501)>:42161] Ignoring GPU update because this process is not GPU managed
default	21:03:44.630451-0400	runningboardd	Assertion 398-363-446339 (target:[app<application.com.nexy.assistant.18892826.18892833(501)>:42161]) will be created as active
default	21:03:44.630495-0400	runningboardd	[app<application.com.nexy.assistant.18892826.18892833(501)>:42161] Ignoring memory limit update because this process is not memory-managed
default	21:03:44.634391-0400	runningboardd	Calculated state for app<application.com.nexy.assistant.18892826.18892833(501)>: running-active (role: UserInteractiveFocal) (endowments: <private>)
default	21:03:44.634819-0400	runningboardd	[app<application.com.nexy.assistant.18892826.18892833(501)>:42161] Ignoring jetsam update because this process is not memory-managed
default	21:03:44.634830-0400	runningboardd	[app<application.com.nexy.assistant.18892826.18892833(501)>:42161] Ignoring suspend because this process is not lifecycle managed
default	21:03:44.634843-0400	runningboardd	[app<application.com.nexy.assistant.18892826.18892833(501)>:42161] Ignoring GPU update because this process is not GPU managed
default	21:03:44.634860-0400	runningboardd	[app<application.com.nexy.assistant.18892826.18892833(501)>:42161] Ignoring memory limit update because this process is not memory-managed
default	21:03:44.635449-0400	gamepolicyd	Received state update for 42161 (app<application.com.nexy.assistant.18892826.18892833(501)>, running-active-NotVisible
default	21:03:44.638379-0400	runningboardd	Calculated state for app<application.com.nexy.assistant.18892826.18892833(501)>: running-active (role: UserInteractiveFocal) (endowments: <private>)
default	21:03:44.639147-0400	gamepolicyd	Received state update for 42161 (app<application.com.nexy.assistant.18892826.18892833(501)>, running-active-NotVisible
default	21:03:44.651935-0400	Nexy	[0xc9589d7c0] activating connection: mach=true listener=false peer=false name=com.apple.usernoted.client
default	21:03:44.688287-0400	distnoted	register name: com.apple.nsquiet_safe_quit_give_reason object: com.nexy.assistant token: 3100000032 pid: 42161
default	21:03:44.711841-0400	Nexy	NSApp cache appearance:
-NSRequiresAquaSystemAppearance: 0
-appearance: (null)
-effectiveAppearance: <NSCompositeAppearance: 0xc95725400
 (
    "<NSDarkAquaAppearance: 0xc957254a0>",
    "<NSSystemAppearance: 0xc95725360>"
)>
default	21:03:44.715462-0400	usernoted	Connection com.nexy.assistant with path: /Applications/Nexy.app
default	21:03:44.737977-0400	Nexy	[0xc9589de00] activating connection: mach=true listener=false peer=false name=com.apple.dock.fullscreen
default	21:03:44.741327-0400	Nexy	[0xc9589df40] activating connection: mach=true listener=false peer=false name=com.apple.fonts
default	21:03:44.747847-0400	Nexy	(<private>) deleteSearchableItemsWithDomainIdentifiers, protectionClass:(null), domainIdentifiers number:1
default	21:03:44.748395-0400	Nexy	sConnectionName: com.apple.spotlight.IndexAgent
default	21:03:44.748415-0400	Nexy	Start service name com.apple.spotlight.IndexAgent
default	21:03:44.748490-0400	Nexy	[0xc9589e080] activating connection: mach=true listener=false peer=false name=com.apple.spotlight.IndexAgent
default	21:03:44.770649-0400	Nexy	[C:1] Alloc com.apple.controlcenter.statusitems
default	21:03:44.770777-0400	Nexy	[0xc9589e1c0] activating connection: mach=false listener=false peer=false name=(anonymous)
default	21:03:44.770936-0400	Nexy	FBSWorkspace registering source: <private>
default	21:03:44.776113-0400	Nexy	FBSWorkspace connected to endpoint : <private>
default	21:03:44.776333-0400	Nexy	<FBSWorkspaceScenesClient:0xc957263a0 <private>> attempting immediate handshake from activate
default	21:03:44.776527-0400	Nexy	<FBSWorkspaceScenesClient:0xc957263a0 <private>> sent handshake
default	21:03:44.776879-0400	Nexy	Realizing settings extension __NSStatusItemSceneHostSettings__ on FBSSceneSettings
default	21:03:44.797332-0400	ControlCenter	Asked to bootstrap a new process for handle: [app<application.com.nexy.assistant.18892826.18892833(501)>:42161]
default	21:03:44.797463-0400	ControlCenter	Creating process (sync=true) for handle: [app<application.com.nexy.assistant.18892826.18892833(501)>:42161]
default	21:03:44.798293-0400	ControlCenter	[app<application.com.nexy.assistant.18892826.18892833>:42161] Registering event dispatcher at init
default	21:03:44.798860-0400	ControlCenter	Created <FBWorkspace: 0xaf79aa620; <FBApplicationProcess: 0xaf8352e80; app<application.com.nexy.assistant.18892826.18892833>:42161(vD314B)>>
default	21:03:44.799115-0400	ControlCenter	Bootstrapping app<application.com.nexy.assistant.18892826.18892833> with intent background
default	21:03:44.799998-0400	runningboardd	Launch request for app<application.com.nexy.assistant.18892826.18892833(501)>[0] is using uid 501 (divined from auid 501 euid 501)
default	21:03:44.800260-0400	runningboardd	Acquiring assertion targeting app<application.com.nexy.assistant.18892826.18892833(501)> from originator [osservice<com.apple.controlcenter(501)>:632] with description <RBSAssertionDescriptor| "FBApplicationProcess" ID:398-632-446340 target:app<application.com.nexy.assistant.18892826.18892833(501)> attributes:[
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableLPRunReason-Suspend" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableRole-NonUI" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableJetsamPriority-Active" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableBootstrapping" sourceEnvironment:"(null)">
	]>
default	21:03:44.800623-0400	runningboardd	Assertion 398-632-446340 (target:app<application.com.nexy.assistant.18892826.18892833(501)>) will be created as active
default	21:03:44.800681-0400	runningboardd	setting abstract target for <RBSAssertionDescriptor| "FBApplicationProcess" ID:398-632-446340 target:app<application.com.nexy.assistant.18892826.18892833(501)> attributes:[
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableLPRunReason-Suspend" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableRole-NonUI" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableJetsamPriority-Active" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableBootstrapping" sourceEnvironment:"(null)">
	]> to [app<application.com.nexy.assistant.18892826.18892833(501)>:42161]
default	21:03:44.801798-0400	Nexy	Realizing settings extension __NSStatusItemSceneClientSettings__ on FBSSceneClientSettings
default	21:03:44.806794-0400	Nexy	Realizing settings extension FBSSceneSettingsCore on FBSSceneSettings
default	21:03:44.807068-0400	runningboardd	[app<application.com.nexy.assistant.18892826.18892833(501)>:42161] Ignoring jetsam update because this process is not memory-managed
default	21:03:44.807140-0400	runningboardd	[app<application.com.nexy.assistant.18892826.18892833(501)>:42161] Ignoring suspend because this process is not lifecycle managed
default	21:03:44.807491-0400	runningboardd	[app<application.com.nexy.assistant.18892826.18892833(501)>:42161] Ignoring GPU update because this process is not GPU managed
default	21:03:44.807667-0400	runningboardd	[app<application.com.nexy.assistant.18892826.18892833(501)>:42161] Ignoring memory limit update because this process is not memory-managed
default	21:03:44.809747-0400	Nexy	Realizing settings extension FBSSceneClientSettingsCore on FBSSceneClientSettings
default	21:03:44.810911-0400	runningboardd	Calculated state for app<application.com.nexy.assistant.18892826.18892833(501)>: running-active (role: UserInteractiveFocal) (endowments: <private>)
default	21:03:44.811507-0400	Nexy	Requesting scene <FBSScene: 0xc957266c0; com.apple.controlcenter:7394A576-D823-4503-AA70-D223BBF79BC1> from com.apple.controlcenter.statusitems
default	21:03:44.814745-0400	Nexy	Request for <FBSScene: 0xc957266c0; com.apple.controlcenter:7394A576-D823-4503-AA70-D223BBF79BC1> complete!
default	21:03:44.815007-0400	Nexy	Realizing settings extension FBSSceneTransitionContextCore on FBSSceneTransitionContext
default	21:03:44.815896-0400	ControlCenter	[app<application.com.nexy.assistant.18892826.18892833>:42161] Bootstrap success!
default	21:03:44.816761-0400	ControlCenter	[app<application.com.nexy.assistant.18892826.18892833>:42161] Setting process visibility to: Background
default	21:03:44.816876-0400	ControlCenter	[app<application.com.nexy.assistant.18892826.18892833>:42161] No launch watchdog for this process, dropping initial assertion in 2.0s
default	21:03:44.817341-0400	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.18892826.18892833(501)>:42161] from originator [osservice<com.apple.controlcenter(501)>:632] with description <RBSAssertionDescriptor| "FBWorkspaceDomain: injecting saved endowment" ID:398-632-446341 target:42161 attributes:[
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"WorkspaceEndpointInjection" sourceEnvironment:"(null)">
	]>
default	21:03:44.817461-0400	runningboardd	Assertion 398-632-446341 (target:[app<application.com.nexy.assistant.18892826.18892833(501)>:42161]) will be created as active
default	21:03:44.818013-0400	runningboardd	[app<application.com.nexy.assistant.18892826.18892833(501)>:42161] Ignoring jetsam update because this process is not memory-managed
default	21:03:44.818104-0400	runningboardd	[app<application.com.nexy.assistant.18892826.18892833(501)>:42161] Ignoring suspend because this process is not lifecycle managed
default	21:03:44.818137-0400	runningboardd	[app<application.com.nexy.assistant.18892826.18892833(501)>:42161] Ignoring GPU update because this process is not GPU managed
default	21:03:44.818263-0400	runningboardd	[app<application.com.nexy.assistant.18892826.18892833(501)>:42161] Ignoring memory limit update because this process is not memory-managed
default	21:03:44.818731-0400	Nexy	Realizing settings extension __NSHostedViewSceneSettings__ on FBSSceneSettings
default	21:03:44.819205-0400	Nexy	Realizing settings extension __NSClientHostedViewSceneSettings__ on FBSSceneClientSettings
default	21:03:44.819645-0400	Nexy	Realizing settings extension __NSStatusItemAuxiliaryViewSceneSettings__ on FBSSceneSettings
default	21:03:44.819736-0400	Nexy	Realizing settings extension __NSClientStatusItemAuxiliaryViewSceneSettings__ on FBSSceneClientSettings
default	21:03:44.820508-0400	Nexy	Requesting scene <FBSScene: 0xc957268a0; com.apple.controlcenter:7394A576-D823-4503-AA70-D223BBF79BC1-Aux[1]-NSStatusItemView> from com.apple.controlcenter.statusitems
default	21:03:44.821122-0400	Nexy	Request for <FBSScene: 0xc957268a0; com.apple.controlcenter:7394A576-D823-4503-AA70-D223BBF79BC1-Aux[1]-NSStatusItemView> complete!
default	21:03:44.823945-0400	runningboardd	Calculated state for app<application.com.nexy.assistant.18892826.18892833(501)>: running-active (role: UserInteractiveFocal) (endowments: <private>)
default	21:03:44.824990-0400	ControlCenter	Adding: <FBApplicationProcess: 0xaf8352e80; app<application.com.nexy.assistant.18892826.18892833>:42161(vD314B)>
default	21:03:44.825706-0400	ControlCenter	[app<application.com.nexy.assistant.18892826.18892833>:42161] Connection established.
default	21:03:44.825969-0400	ControlCenter	[app<application.com.nexy.assistant.18892826.18892833>:42161] created proxy of <BSXPCServiceConnectionProxy<FBSWorkspaceServiceServerInterface>: 0xaf8ce40e0>
default	21:03:44.826004-0400	ControlCenter	Received state update for 42161 (app<application.com.nexy.assistant.18892826.18892833(501)>, running-active-NotVisible
default	21:03:44.826061-0400	ControlCenter	[app<application.com.nexy.assistant.18892826.18892833>:42161] Connection to remote process established!
default	21:03:44.827786-0400	gamepolicyd	Received state update for 42161 (app<application.com.nexy.assistant.18892826.18892833(501)>, running-active-NotVisible
default	21:03:44.829297-0400	gamepolicyd	Received state update for 42161 (app<application.com.nexy.assistant.18892826.18892833(501)>, running-active-NotVisible
default	21:03:44.835303-0400	suggestd	SGDSpotlightReceiver: deleting 1 domain identifiers (1 after removing overlaps) for com.nexy.assistant: <private>
default	21:03:44.839180-0400	ControlCenter	Asked to bootstrap a new process for handle: [app<application.com.nexy.assistant.18892826.18892833(501)>:42161]
default	21:03:44.839209-0400	ControlCenter	A process already exists for this handle: <FBApplicationProcess: 0xaf8352e80; app<application.com.nexy.assistant.18892826.18892833>:42161(vD314B)>
default	21:03:44.839420-0400	ControlCenter	[app<application.com.nexy.assistant.18892826.18892833>:42161] Registered new scene: <FBWorkspaceScene: 0xaf5dc6640; com.apple.controlcenter:7394A576-D823-4503-AA70-D223BBF79BC1> (fromRemnant = 0)
default	21:03:44.839490-0400	ControlCenter	[app<application.com.nexy.assistant.18892826.18892833>:42161] Workspace interruption policy did change: reconnect
default	21:03:44.839874-0400	ControlCenter	[com.apple.controlcenter:7394A576-D823-4503-AA70-D223BBF79BC1] Client process connected: [app<application.com.nexy.assistant.18892826.18892833(501)>:42161]
default	21:03:44.839895-0400	Nexy	Request for <FBSScene: 0xc957266c0; com.apple.controlcenter:7394A576-D823-4503-AA70-D223BBF79BC1> complete!
default	21:03:44.840106-0400	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.18892826.18892833(501)>:42161] from originator [osservice<com.apple.controlcenter(501)>:632] with description <RBSAssertionDescriptor| "com.apple.frontboard.after-life.interrupted" ID:398-632-446342 target:42161 attributes:[
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"AfterLife-Interrupted" sourceEnvironment:"(null)">
	]>
default	21:03:44.840276-0400	runningboardd	Assertion 398-632-446342 (target:[app<application.com.nexy.assistant.18892826.18892833(501)>:42161]) will be created as inactive as originator process has not exited
default	21:03:44.841200-0400	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.18892826.18892833(501)>:42161] from originator [osservice<com.apple.controlcenter(501)>:632] with description <RBSAssertionDescriptor| "FBWorkspace (BG-Active[40])" ID:398-632-446343 target:42161 attributes:[
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableLPRunReason-Suspend" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableRole-NonUI" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableJetsamPriority-Active" sourceEnvironment:"(null)">
	]>
default	21:03:44.841296-0400	Nexy	[com.apple.controlcenter:7394A576-D823-4503-AA70-D223BBF79BC1-Aux[1]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
default	21:03:44.841382-0400	runningboardd	Assertion 398-632-446343 (target:[app<application.com.nexy.assistant.18892826.18892833(501)>:42161]) will be created as active
default	21:03:44.841510-0400	Nexy	[com.apple.controlcenter:7394A576-D823-4503-AA70-D223BBF79BC1-Aux[1]-NSStatusItemView] Dropping transition context because the scene is reconnecting
default	21:03:44.841655-0400	ControlCenter	[app<application.com.nexy.assistant.18892826.18892833>:42161] Workspace state did change: XX-None[0] --> BG-Active[40] (assertion acquired).
default	21:03:44.842194-0400	runningboardd	[app<application.com.nexy.assistant.18892826.18892833(501)>:42161] Ignoring jetsam update because this process is not memory-managed
default	21:03:44.842283-0400	runningboardd	[app<application.com.nexy.assistant.18892826.18892833(501)>:42161] Ignoring suspend because this process is not lifecycle managed
default	21:03:44.842365-0400	ControlCenter	Asked to bootstrap a new process for handle: [app<application.com.nexy.assistant.18892826.18892833(501)>:42161]
default	21:03:44.842448-0400	ControlCenter	A process already exists for this handle: <FBApplicationProcess: 0xaf8352e80; app<application.com.nexy.assistant.18892826.18892833>:42161(vD314B)>
default	21:03:44.842487-0400	runningboardd	[app<application.com.nexy.assistant.18892826.18892833(501)>:42161] Ignoring GPU update because this process is not GPU managed
default	21:03:44.842664-0400	ControlCenter	[app<application.com.nexy.assistant.18892826.18892833>:42161] Registered new scene: <FBWorkspaceScene: 0xaf5dc7780; com.apple.controlcenter:7394A576-D823-4503-AA70-D223BBF79BC1-Aux[1]-NSStatusItemView> (fromRemnant = 0)
default	21:03:44.842773-0400	runningboardd	[app<application.com.nexy.assistant.18892826.18892833(501)>:42161] Ignoring memory limit update because this process is not memory-managed
default	21:03:44.843000-0400	ControlCenter	[com.apple.controlcenter:7394A576-D823-4503-AA70-D223BBF79BC1-Aux[1]-NSStatusItemView] Client process connected: [app<application.com.nexy.assistant.18892826.18892833(501)>:42161]
default	21:03:44.843209-0400	Nexy	<FBSWorkspaceScenesClient:0xc957263a0 <private>> Reconnecting scene com.apple.controlcenter:7394A576-D823-4503-AA70-D223BBF79BC1
default	21:03:44.843818-0400	Nexy	<FBSWorkspaceScenesClient:0xc957263a0 <private>> Reconnecting scene com.apple.controlcenter:7394A576-D823-4503-AA70-D223BBF79BC1-Aux[1]-NSStatusItemView
default	21:03:44.844146-0400	Nexy	Request for <FBSScene: 0xc957268a0; com.apple.controlcenter:7394A576-D823-4503-AA70-D223BBF79BC1-Aux[1]-NSStatusItemView> complete!
default	21:03:44.850989-0400	runningboardd	Calculated state for app<application.com.nexy.assistant.18892826.18892833(501)>: running-active (role: UserInteractiveFocal) (endowments: <private>)
default	21:03:44.852485-0400	ControlCenter	Received state update for 42161 (app<application.com.nexy.assistant.18892826.18892833(501)>, running-active-NotVisible
default	21:03:44.856636-0400	gamepolicyd	Received state update for 42161 (app<application.com.nexy.assistant.18892826.18892833(501)>, running-active-NotVisible
default	21:03:44.867985-0400	Nexy	[com.apple.controlcenter:7394A576-D823-4503-AA70-D223BBF79BC1-Aux[1]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
default	21:03:44.868588-0400	Nexy	Warning: the app is using `-[NSStatusBarButton setHighlightsBy:]` to set the highlight behavior. Instead, consider removing that setting. That will enable macOS to highlight the status bar button as appropriate for all configurations (e.g., light, dark, and increased contrast modes).
default	21:03:44.870353-0400	Nexy	[com.apple.controlcenter:7394A576-D823-4503-AA70-D223BBF79BC1-Aux[1]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
default	21:03:44.907270-0400	Nexy	Registering for test daemon availability notify post.
default	21:03:44.907690-0400	Nexy	notify_get_state check indicated test daemon not ready.
default	21:03:44.907965-0400	Nexy	notify_get_state check indicated test daemon not ready.
default	21:03:44.908117-0400	Nexy	notify_get_state check indicated test daemon not ready.
default	21:03:44.911349-0400	Nexy	[0xc9589e580] activating connection: mach=true listener=false peer=false name=com.apple.coreservices.appleevents
default	21:03:44.912566-0400	Nexy	[0xc9589cdc0] Connection returned listener port: 0x14d03
default	21:03:44.913222-0400	Nexy	SignalReady: pid=42161 asn=0x0-0x965965
default	21:03:44.913721-0400	Nexy	SIGNAL: pid=42161 asn=0x0x-0x965965
default	21:03:44.915124-0400	loginwindow	-[Application updateInformation] | Got App URL: file:///Applications/Nexy.app/
default	21:03:44.922941-0400	Nexy	[com.apple.controlcenter:7394A576-D823-4503-AA70-D223BBF79BC1-Aux[1]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
default	21:03:44.926861-0400	Nexy	void _NSDisableAutomaticTerminationAndLog(NSString *) Restoring windows
default	21:03:44.926872-0400	Nexy	-[NSApplication _reopenWindowsAsNecessaryIncludingRestorableState:withFullFidelity:completionHandler:] shouldRestoreState=1 hasPersistentStateToRestore=0 shouldStillRestoreStateAfterPrompting=0
default	21:03:44.926899-0400	Nexy	[0xc9589d900] activating connection: mach=true listener=false peer=false name=com.apple.window_proxies
default	21:03:44.927151-0400	Nexy	[0xc9589d900] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	21:03:44.939618-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117300 at /Applications/Nexy.app
default	21:03:44.943530-0400	Nexy	void _NSEnableAutomaticTerminationAndLog(NSString *) Restoring windows
default	21:03:44.958707-0400	Nexy	[C:2] Alloc <private>
default	21:03:44.958775-0400	Nexy	[0xc9589d900] activating connection: mach=false listener=false peer=false name=(anonymous)
error	21:03:44.959031-0400	kernel	Sandbox: WindowManager(584) deny(1) mach-task-name others [Nexy(42161)]
default	21:03:44.961539-0400	ControlCenter	Host properties initialized; (bid:com.nexy.assistant-Item-0-42161). State(applicationItem: true, clientRequestsVisibility: true, neverClip: false)
default	21:03:44.962368-0400	WindowManager	Connection activated | (42161) Nexy
default	21:03:44.964601-0400	ControlCenter	Starting to track host; (bid:com.nexy.assistant-Item-0-42161)
default	21:03:44.965344-0400	ControlCenter	Created new displayable type DisplayableAppStatusItemType(A1F80334, (bid:com.nexy.assistant-Item-0-42161)) for (bid:com.nexy.assistant-Item-0-42161)
default	21:03:44.967118-0400	ControlCenter	Adding displayable items for status items; [(bid:com.nexy.assistant-Item-0-42161)]
default	21:03:44.967928-0400	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.18892826.18892833(501)>:42161] from originator [app<application.com.nexy.assistant.18892826.18892833(501)>:42161] with description <RBSAssertionDescriptor| "AudioHAL" ID:398-42161-446344 target:42161 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	21:03:44.968031-0400	runningboardd	Assertion 398-42161-446344 (target:[app<application.com.nexy.assistant.18892826.18892833(501)>:42161]) will be created as active
default	21:03:44.968343-0400	ControlCenter	Created instance DisplayableId(34A7C29C) in .menuBar for DisplayableAppStatusItemType(A1F80334, (bid:com.nexy.assistant-Item-0-42161)) .menuBar
default	21:03:44.968621-0400	runningboardd	Invalidating assertion 398-42161-446344 (target:[app<application.com.nexy.assistant.18892826.18892833(501)>:42161]) from originator [app<application.com.nexy.assistant.18892826.18892833(501)>:42161]
default	21:03:44.968847-0400	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.18892826.18892833(501)>:42161] from originator [app<application.com.nexy.assistant.18892826.18892833(501)>:42161] with description <RBSAssertionDescriptor| "AudioHAL" ID:398-42161-446345 target:42161 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	21:03:44.968952-0400	runningboardd	Assertion 398-42161-446345 (target:[app<application.com.nexy.assistant.18892826.18892833(501)>:42161]) will be created as active
default	21:03:44.971467-0400	runningboardd	[app<application.com.nexy.assistant.18892826.18892833(501)>:42161] Ignoring jetsam update because this process is not memory-managed
default	21:03:44.971532-0400	runningboardd	[app<application.com.nexy.assistant.18892826.18892833(501)>:42161] Ignoring suspend because this process is not lifecycle managed
default	21:03:44.972007-0400	runningboardd	[app<application.com.nexy.assistant.18892826.18892833(501)>:42161] Ignoring GPU update because this process is not GPU managed
default	21:03:44.972465-0400	runningboardd	[app<application.com.nexy.assistant.18892826.18892833(501)>:42161] Ignoring memory limit update because this process is not memory-managed
default	21:03:44.977694-0400	runningboardd	Calculated state for app<application.com.nexy.assistant.18892826.18892833(501)>: running-active (role: UserInteractiveFocal) (endowments: <private>)
default	21:03:44.978394-0400	runningboardd	Invalidating assertion 398-42161-446345 (target:[app<application.com.nexy.assistant.18892826.18892833(501)>:42161]) from originator [app<application.com.nexy.assistant.18892826.18892833(501)>:42161]
default	21:03:44.978627-0400	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.18892826.18892833(501)>:42161] from originator [app<application.com.nexy.assistant.18892826.18892833(501)>:42161] with description <RBSAssertionDescriptor| "AudioHAL" ID:398-42161-446346 target:42161 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	21:03:44.978735-0400	runningboardd	Assertion 398-42161-446346 (target:[app<application.com.nexy.assistant.18892826.18892833(501)>:42161]) will be created as active
default	21:03:44.978929-0400	ControlCenter	Received state update for 42161 (app<application.com.nexy.assistant.18892826.18892833(501)>, running-active-NotVisible
default	21:03:44.979288-0400	runningboardd	Invalidating assertion 398-42161-446346 (target:[app<application.com.nexy.assistant.18892826.18892833(501)>:42161]) from originator [app<application.com.nexy.assistant.18892826.18892833(501)>:42161]
default	21:03:44.979509-0400	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.18892826.18892833(501)>:42161] from originator [app<application.com.nexy.assistant.18892826.18892833(501)>:42161] with description <RBSAssertionDescriptor| "AudioHAL" ID:398-42161-446347 target:42161 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	21:03:44.979569-0400	runningboardd	Assertion 398-42161-446347 (target:[app<application.com.nexy.assistant.18892826.18892833(501)>:42161]) will be created as active
default	21:03:44.979846-0400	runningboardd	Invalidating assertion 398-42161-446347 (target:[app<application.com.nexy.assistant.18892826.18892833(501)>:42161]) from originator [app<application.com.nexy.assistant.18892826.18892833(501)>:42161]
default	21:03:44.980032-0400	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.18892826.18892833(501)>:42161] from originator [app<application.com.nexy.assistant.18892826.18892833(501)>:42161] with description <RBSAssertionDescriptor| "AudioHAL" ID:398-42161-446348 target:42161 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	21:03:44.980087-0400	runningboardd	Assertion 398-42161-446348 (target:[app<application.com.nexy.assistant.18892826.18892833(501)>:42161]) will be created as active
default	21:03:44.980418-0400	runningboardd	Invalidating assertion 398-42161-446348 (target:[app<application.com.nexy.assistant.18892826.18892833(501)>:42161]) from originator [app<application.com.nexy.assistant.18892826.18892833(501)>:42161]
default	21:03:44.980660-0400	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.18892826.18892833(501)>:42161] from originator [app<application.com.nexy.assistant.18892826.18892833(501)>:42161] with description <RBSAssertionDescriptor| "AudioHAL" ID:398-42161-446349 target:42161 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	21:03:44.980715-0400	runningboardd	Assertion 398-42161-446349 (target:[app<application.com.nexy.assistant.18892826.18892833(501)>:42161]) will be created as active
default	21:03:44.981077-0400	runningboardd	Invalidating assertion 398-42161-446349 (target:[app<application.com.nexy.assistant.18892826.18892833(501)>:42161]) from originator [app<application.com.nexy.assistant.18892826.18892833(501)>:42161]
default	21:03:44.982826-0400	Nexy	[com.apple.controlcenter:7394A576-D823-4503-AA70-D223BBF79BC1-Aux[1]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
default	21:03:44.984524-0400	Nexy	[com.apple.controlcenter:7394A576-D823-4503-AA70-D223BBF79BC1] Sending action(s) in update: NSSceneFenceAction
default	21:03:44.985852-0400	gamepolicyd	Received state update for 42161 (app<application.com.nexy.assistant.18892826.18892833(501)>, running-active-NotVisible
default	21:03:45.004795-0400	Nexy	[0xc9589ca00] activating connection: mach=false listener=false peer=false name=com.apple.ViewBridgeAuxiliary
default	21:03:45.006004-0400	ControlCenter	Created ephemaral instance DisplayableId(34A7C29C) for (bid:com.nexy.assistant-Item-0-42161) with positioning .ephemeral
default	21:03:45.018599-0400	Nexy	[0xc9589e6c0] activating connection: mach=false listener=false peer=false name=(anonymous)
default	21:03:45.019570-0400	Nexy	[0xc9589e800] activating connection: mach=false listener=true peer=false name=(anonymous)
default	21:03:45.019587-0400	Nexy	[0xc9589e800] Connection returned listener port: 0x1dd03
default	21:03:45.024143-0400	Nexy	[0xc9589ca00] invalidated after the last release of the connection object
default	21:03:45.024307-0400	Nexy	[com.apple.controlcenter:7394A576-D823-4503-AA70-D223BBF79BC1] Received action(s): NSStatusItemChangeVisibilityAction
default	21:03:45.029768-0400	Nexy	[com.apple.controlcenter:7394A576-D823-4503-AA70-D223BBF79BC1] Observer <NSSceneStatusItem: 0xc93d12d80> handled action(s): <private>
default	21:03:45.032741-0400	Nexy	[com.apple.controlcenter:7394A576-D823-4503-AA70-D223BBF79BC1-Aux[1]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
default	21:03:45.033440-0400	Nexy	[com.apple.controlcenter:7394A576-D823-4503-AA70-D223BBF79BC1] Sending action(s) in update: NSSceneFenceAction
default	21:03:45.034490-0400	Nexy	[com.apple.controlcenter:7394A576-D823-4503-AA70-D223BBF79BC1-Aux[1]-NSStatusItemView] Received action(s) in scene-update: NSSceneFenceAction
default	21:03:45.036837-0400	Nexy	[com.apple.controlcenter:7394A576-D823-4503-AA70-D223BBF79BC1-Aux[1]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
default	21:03:45.045881-0400	kernel	udp connect: [<IPv4-redacted>:58659<-><IPv4-redacted>:50051] interface:  (skipped: 617)
so_gencnt: 2265976 so_state: 0x0002 process: Nexy:42161 bytes in/out: 0/0 pkts in/out: 0/0 error: 0 so_error: 0 svc/tc: 0 flow: 0x97f894d3
default	21:03:45.045908-0400	kernel	udp_connection_summary [<IPv4-redacted>:58659<-><IPv4-redacted>:50051] interface:  (skipped: 617)
so_gencnt: 2265976 so_state: 0x0002 process: Nexy:42161 Duration: 0.000 sec Conn_Time: 0.000 sec bytes in/out: 0/0 pkts in/out: 0/0 rxnospace pkts/bytes: 0/0 so_error: 0 svc/tc: 0 flow: 0x97f894d3 flowctl: 0us (0x)
default	21:03:45.058262-0400	Nexy	[com.apple.controlcenter:7394A576-D823-4503-AA70-D223BBF79BC1] Sending action(s) in update: NSSceneFenceAction
default	21:03:45.069735-0400	Nexy	[com.apple.controlcenter:7394A576-D823-4503-AA70-D223BBF79BC1] Sending action(s) in update: NSSceneFenceAction
default	21:03:45.072828-0400	runningboardd	[app<application.com.nexy.assistant.18892826.18892833(501)>:42161] Ignoring jetsam update because this process is not memory-managed
default	21:03:45.072846-0400	runningboardd	[app<application.com.nexy.assistant.18892826.18892833(501)>:42161] Ignoring suspend because this process is not lifecycle managed
default	21:03:45.072875-0400	runningboardd	[app<application.com.nexy.assistant.18892826.18892833(501)>:42161] Ignoring GPU update because this process is not GPU managed
default	21:03:45.072932-0400	runningboardd	[app<application.com.nexy.assistant.18892826.18892833(501)>:42161] Ignoring memory limit update because this process is not memory-managed
default	21:03:45.076947-0400	runningboardd	Calculated state for app<application.com.nexy.assistant.18892826.18892833(501)>: running-active (role: UserInteractiveFocal) (endowments: <private>)
default	21:03:45.077610-0400	ControlCenter	Received state update for 42161 (app<application.com.nexy.assistant.18892826.18892833(501)>, running-active-NotVisible
default	21:03:45.078063-0400	gamepolicyd	Received state update for 42161 (app<application.com.nexy.assistant.18892826.18892833(501)>, running-active-NotVisible
default	21:03:45.100399-0400	Nexy	[0xc9589e940] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	21:03:45.101480-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=42161.8, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=42161, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	21:03:45.103637-0400	tccd	AUTHREQ_SUBJECT: msgID=42161.8, subject=com.nexy.assistant,
default	21:03:45.105209-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117300 at /Applications/Nexy.app
default	21:03:45.124070-0400	Nexy	[0xc9589e940] invalidated after the last release of the connection object
default	21:03:45.125653-0400	Nexy	 [INFO] SLSHWCaptureDesktopProxying:485 request: <private>
default	21:03:45.129164-0400	Nexy	[0xc9589e940] activating connection: mach=true listener=false peer=false name=com.apple.replayd
default	21:03:45.129410-0400	Nexy	 [INFO] -[RPDaemonProxy consumeSandboxExtension:processNewConnection:]:568
default	21:03:45.129545-0400	Nexy	 [INFO] -[RPDaemonProxy proxyCoreGraphicsWithMethodType:config:machPort:completionHandler:]:1486
default	21:03:45.142992-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=26656.2, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=42161, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.replayd, pid=26656, auid=501, euid=501, binary_path=/usr/libexec/replayd}, },
default	21:03:45.143028-0400	tccd	requestor: TCCDProcess: identifier=com.apple.replayd, pid=26656, auid=501, euid=501, binary_path=/usr/libexec/replayd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=42161, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	21:03:45.145250-0400	tccd	AUTHREQ_SUBJECT: msgID=26656.2, subject=com.nexy.assistant,
default	21:03:45.146372-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117300 at /Applications/Nexy.app
default	21:03:45.175995-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=393.5921, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=42161, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=393, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	21:03:45.176019-0400	tccd	requestor: TCCDProcess: identifier=com.apple.WindowServer, pid=393, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=42161, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	21:03:45.177084-0400	tccd	AUTHREQ_SUBJECT: msgID=393.5921, subject=com.nexy.assistant,
default	21:03:45.177776-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117300 at /Applications/Nexy.app
default	21:03:45.186388-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=42323.1, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=42161, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.osascript, pid=42323, auid=501, euid=501, binary_path=/usr/bin/osascript}, },
default	21:03:45.188061-0400	tccd	AUTHREQ_SUBJECT: msgID=42323.1, subject=com.nexy.assistant,
default	21:03:45.188795-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d116400 at /Applications/Nexy.app
default	21:03:45.191432-0400	Nexy	*warn* MailCS ======%%% _setMailMessageAttributes skip:1
default	21:03:45.196237-0400	Nexy	Start service name com.apple.spotlightknowledged
default	21:03:45.197402-0400	Nexy	[GMS] availability notification token 89
default	21:03:45.205595-0400	Nexy	 [INFO] SLSHWCaptureDesktopProxying_block_invoke:506 request: <private>, error: (null), windowInfo: (null)
default	21:03:45.210100-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=393.5922, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=42161, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.osascript, pid=42323, auid=501, euid=501, binary_path=/usr/bin/osascript}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=393, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	21:03:45.211220-0400	tccd	AUTHREQ_SUBJECT: msgID=393.5922, subject=com.nexy.assistant,
default	21:03:45.211864-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d116400 at /Applications/Nexy.app
default	21:03:45.223171-0400	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	21:03:45.223239-0400	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant)]
default	21:03:45.223278-0400	ControlCenter	Active activity attributions changed to ["scr:com.nexy.assistant"]
default	21:03:45.244103-0400	ControlCenter	[app<application.com.nexy.assistant.18892826.18892833>:42161] Workspace state did change: BG-Active[40] --> XX-None[0] (assertion dropped).
default	21:03:45.245258-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d116400 at /Applications/Nexy.app
default	21:03:45.247473-0400	runningboardd	Invalidating assertion 398-632-446343 (target:[app<application.com.nexy.assistant.18892826.18892833(501)>:42161]) from originator [osservice<com.apple.controlcenter(501)>:632]
default	21:03:45.255590-0400	Nexy	[0xc9589ca00] activating connection: mach=false listener=false peer=false name=com.apple.hiservices-xpcservice
default	21:03:45.258806-0400	Nexy	+[IMKClient subclass]: chose IMKClient_Modern
default	21:03:45.258836-0400	Nexy	+[IMKInputSession subclass]: chose IMKInputSession_Modern
default	21:03:45.261492-0400	Nexy	[0xc9589ea80] activating connection: mach=true listener=false peer=false name=com.apple.inputmethodkit.getxpcendpoint
default	21:03:45.262619-0400	Nexy	[0xc9589ebc0] activating connection: mach=false listener=false peer=false name=(anonymous)
default	21:03:45.266158-0400	System Events	TCCAccessRequestIndirect: TCCAccessRequestIndirect with pid 42186: target_identity: {
    kTCCCodeIdentityAuditToken = {length = 32, bytes = 0xf5010000 f5010000 14000000 f5010000 ... b7860100 01330d00 };
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
default	21:03:45.277664-0400	tccd	target_executable_path_URL: file:///Applications/Nexy.app/Contents/MacOS/Nexy
default	21:03:45.300967-0400	WindowServer	0[outside of RPC]: [DeferringManager] Updating policy {
    advicePolicy: .frontmost;
    frontmostProcess: 0x0-0x965965 (Nexy) mainConnectionID: A2C13;
} for reason: deferringPolicyEvaluationSuppression
default	21:03:45.301084-0400	WindowServer	0[outside of RPC]: [DeferringManager] Deferring events from frontmost process PSN 0x0-0x965965 (Nexy) -> <pid: 42161>
default	21:03:45.301175-0400	WindowServer	new deferring rules for pid:393: [
    [393-5CD6]; <keyboardFocus; Nexy:0x0-0x965965>; () -> <pid: 42161>; reason: frontmost PSN --> outbound target,
    [393-5CD5]; <keyboardFocus; <frontmost>>; () -> <token: Nexy:0x0-0x965965; pid: 393>; reason: frontmost PSN,
    [393-5CD4]; <keyboardFocus>; () -> <token: <frontmost>; pid: 393>; reason: Deferring to <frontmost>
]
default	21:03:45.301208-0400	WindowServer	[keyboardFocus 0x7facf2b20] setRules:forPID(393): [
    [393-5CD6]; <keyboardFocus; Nexy:0x0-0x965965>; () -> <pid: 42161>; reason: frontmost PSN --> outbound target,
    [393-5CD5]; <keyboardFocus; <frontmost>>; () -> <token: Nexy:0x0-0x965965; pid: 393>; reason: frontmost PSN,
    [393-5CD4]; <keyboardFocus>; () -> <token: <frontmost>; pid: 393>; reason: Deferring to <frontmost>
]
default	21:03:45.301937-0400	WindowServer	chain did update (setDeferringRules) <keyboardFocus; display: null> containsEndOfChain: YES; [
    <token: <frontmost>; pid: 393>,
    <token: Nexy:0x0-0x965965; pid: 393>,
    <pid: 42161>
]
default	21:03:45.356532-0400	runningboardd	[app<application.com.nexy.assistant.18892826.18892833(501)>:42161] Ignoring jetsam update because this process is not memory-managed
default	21:03:45.356545-0400	runningboardd	[app<application.com.nexy.assistant.18892826.18892833(501)>:42161] Ignoring suspend because this process is not lifecycle managed
default	21:03:45.356556-0400	runningboardd	[app<application.com.nexy.assistant.18892826.18892833(501)>:42161] Ignoring GPU update because this process is not GPU managed
default	21:03:45.356589-0400	runningboardd	[app<application.com.nexy.assistant.18892826.18892833(501)>:42161] Ignoring memory limit update because this process is not memory-managed
default	21:03:45.359622-0400	runningboardd	Calculated state for app<application.com.nexy.assistant.18892826.18892833(501)>: running-active (role: UserInteractiveFocal) (endowments: <private>)
default	21:03:45.359963-0400	ControlCenter	Received state update for 42161 (app<application.com.nexy.assistant.18892826.18892833(501)>, running-active-NotVisible
default	21:03:45.360034-0400	gamepolicyd	Received state update for 42161 (app<application.com.nexy.assistant.18892826.18892833(501)>, running-active-NotVisible
default	21:03:45.430617-0400	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.18892826.18892833(501)>:42161] from originator [osservice<com.apple.WindowServer(88)>:393] with description <RBSAssertionDescriptor| "AppDrawing" ID:398-393-446354 target:42161 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"AppDrawing" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	21:03:45.430711-0400	runningboardd	Assertion 398-393-446354 (target:[app<application.com.nexy.assistant.18892826.18892833(501)>:42161]) will be created as active
default	21:03:45.431149-0400	runningboardd	[app<application.com.nexy.assistant.18892826.18892833(501)>:42161] Ignoring jetsam update because this process is not memory-managed
default	21:03:45.431165-0400	runningboardd	[app<application.com.nexy.assistant.18892826.18892833(501)>:42161] Ignoring suspend because this process is not lifecycle managed
default	21:03:45.431183-0400	runningboardd	[app<application.com.nexy.assistant.18892826.18892833(501)>:42161] Ignoring GPU update because this process is not GPU managed
default	21:03:45.431219-0400	runningboardd	[app<application.com.nexy.assistant.18892826.18892833(501)>:42161] Ignoring memory limit update because this process is not memory-managed
default	21:03:45.434678-0400	runningboardd	Calculated state for app<application.com.nexy.assistant.18892826.18892833(501)>: running-active (role: UserInteractiveFocal) (endowments: <private>)
default	21:03:45.435177-0400	ControlCenter	Received state update for 42161 (app<application.com.nexy.assistant.18892826.18892833(501)>, running-active-NotVisible
default	21:03:45.435303-0400	gamepolicyd	Received state update for 42161 (app<application.com.nexy.assistant.18892826.18892833(501)>, running-active-NotVisible
default	21:03:46.911009-0400	runningboardd	Invalidating assertion 398-632-446340 (target:app<application.com.nexy.assistant.18892826.18892833(501)>) from originator [osservice<com.apple.controlcenter(501)>:632]
default	21:03:47.013777-0400	runningboardd	Removed last relative-start-date-defining assertion for process app<application.com.nexy.assistant.18892826.18892833(501)>
default	21:03:47.015080-0400	runningboardd	[app<application.com.nexy.assistant.18892826.18892833(501)>:42161] Ignoring jetsam update because this process is not memory-managed
default	21:03:47.015096-0400	runningboardd	[app<application.com.nexy.assistant.18892826.18892833(501)>:42161] Ignoring suspend because this process is not lifecycle managed
default	21:03:47.015109-0400	runningboardd	[app<application.com.nexy.assistant.18892826.18892833(501)>:42161] Ignoring GPU update because this process is not GPU managed
default	21:03:47.015132-0400	runningboardd	[app<application.com.nexy.assistant.18892826.18892833(501)>:42161] Ignoring memory limit update because this process is not memory-managed
default	21:03:47.019784-0400	runningboardd	Calculated state for app<application.com.nexy.assistant.18892826.18892833(501)>: running-active (role: UserInteractiveFocal) (endowments: <private>)
default	21:03:47.024715-0400	ControlCenter	Received state update for 42161 (app<application.com.nexy.assistant.18892826.18892833(501)>, running-active-NotVisible
default	21:03:47.025228-0400	gamepolicyd	Received state update for 42161 (app<application.com.nexy.assistant.18892826.18892833(501)>, running-active-NotVisible
default	21:03:49.689076-0400	Nexy	void _updateToReflectAutomaticTerminationState(void) Setting _kLSApplicationWouldBeTerminatedByTALKey=0
default	21:03:50.436423-0400	runningboardd	Assertion did invalidate due to timeout: 398-363-446339 (target:[app<application.com.nexy.assistant.18892826.18892833(501)>:42161])
default	21:03:50.639646-0400	runningboardd	[app<application.com.nexy.assistant.18892826.18892833(501)>:42161] Ignoring jetsam update because this process is not memory-managed
default	21:03:50.639657-0400	runningboardd	[app<application.com.nexy.assistant.18892826.18892833(501)>:42161] Ignoring suspend because this process is not lifecycle managed
default	21:03:50.639666-0400	runningboardd	[app<application.com.nexy.assistant.18892826.18892833(501)>:42161] Ignoring GPU update because this process is not GPU managed
default	21:03:50.639686-0400	runningboardd	[app<application.com.nexy.assistant.18892826.18892833(501)>:42161] Ignoring memory limit update because this process is not memory-managed
default	21:03:50.643455-0400	runningboardd	Calculated state for app<application.com.nexy.assistant.18892826.18892833(501)>: running-active (role: UserInteractiveFocal) (endowments: <private>)
default	21:03:50.643925-0400	ControlCenter	Received state update for 42161 (app<application.com.nexy.assistant.18892826.18892833(501)>, running-active-NotVisible
default	21:03:50.644516-0400	gamepolicyd	Received state update for 42161 (app<application.com.nexy.assistant.18892826.18892833(501)>, running-active-NotVisible
default	21:03:53.914334-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=393.5923, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=42161, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=393, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	21:03:53.914360-0400	tccd	requestor: TCCDProcess: identifier=com.apple.WindowServer, pid=393, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=42161, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	21:03:53.915949-0400	tccd	AUTHREQ_SUBJECT: msgID=393.5923, subject=com.nexy.assistant,
default	21:03:53.916591-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d116400 at /Applications/Nexy.app
default	21:03:55.045156-0400	Nexy	LSExceptions shared instance invalidated for timeout.
default	21:03:55.280658-0400	ControlCenter	Recent activity attributions changed to ["scr:com.nexy.assistant"]
default	21:03:57.550741-0400	runningboardd	Invalidating assertion 398-363-446338 (target:[app<application.com.nexy.assistant.18892826.18892833(501)>:42161]) from originator [osservice<com.apple.coreservices.launchservicesd>:363]
default	21:03:57.557543-0400	Nexy	void _updateToReflectAutomaticTerminationState(void) Setting _kLSApplicationWouldBeTerminatedByTALKey=1
default	21:03:57.654561-0400	runningboardd	[app<application.com.nexy.assistant.18892826.18892833(501)>:42161] Ignoring jetsam update because this process is not memory-managed
default	21:03:57.654592-0400	runningboardd	[app<application.com.nexy.assistant.18892826.18892833(501)>:42161] Ignoring suspend because this process is not lifecycle managed
default	21:03:57.654623-0400	runningboardd	[app<application.com.nexy.assistant.18892826.18892833(501)>:42161] Set darwin role to: UserInteractive
default	21:03:57.654633-0400	runningboardd	[app<application.com.nexy.assistant.18892826.18892833(501)>:42161] Ignoring GPU update because this process is not GPU managed
default	21:03:57.654681-0400	runningboardd	[app<application.com.nexy.assistant.18892826.18892833(501)>:42161] Ignoring memory limit update because this process is not memory-managed
default	21:03:57.657995-0400	runningboardd	Calculated state for app<application.com.nexy.assistant.18892826.18892833(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	21:03:57.658282-0400	ControlCenter	Received state update for 42161 (app<application.com.nexy.assistant.18892826.18892833(501)>, running-active-NotVisible
default	21:03:57.658409-0400	gamepolicyd	Received state update for 42161 (app<application.com.nexy.assistant.18892826.18892833(501)>, running-active-NotVisible
default	21:04:02.614234-0400	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.18892826.18892833(501)>:42161] from originator [osservice<com.apple.controlcenter(501)>:632] with description <RBSAssertionDescriptor| "FBWorkspace (BG-Active[40])" ID:398-632-446371 target:42161 attributes:[
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableLPRunReason-Suspend" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableRole-NonUI" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableJetsamPriority-Active" sourceEnvironment:"(null)">
	]>
default	21:04:02.614361-0400	runningboardd	Assertion 398-632-446371 (target:[app<application.com.nexy.assistant.18892826.18892833(501)>:42161]) will be created as active
default	21:04:02.614473-0400	ControlCenter	[app<application.com.nexy.assistant.18892826.18892833>:42161] Workspace state did change: XX-None[0] --> BG-Active[40] (assertion acquired).
default	21:04:02.614661-0400	runningboardd	[app<application.com.nexy.assistant.18892826.18892833(501)>:42161] Ignoring jetsam update because this process is not memory-managed
default	21:04:02.614675-0400	runningboardd	[app<application.com.nexy.assistant.18892826.18892833(501)>:42161] Ignoring suspend because this process is not lifecycle managed
default	21:04:02.614685-0400	runningboardd	[app<application.com.nexy.assistant.18892826.18892833(501)>:42161] Ignoring GPU update because this process is not GPU managed
default	21:04:02.614720-0400	runningboardd	[app<application.com.nexy.assistant.18892826.18892833(501)>:42161] Ignoring memory limit update because this process is not memory-managed
default	21:04:02.619443-0400	runningboardd	Calculated state for app<application.com.nexy.assistant.18892826.18892833(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	21:04:02.619987-0400	ControlCenter	Received state update for 42161 (app<application.com.nexy.assistant.18892826.18892833(501)>, running-active-NotVisible
default	21:04:02.620209-0400	gamepolicyd	Received state update for 42161 (app<application.com.nexy.assistant.18892826.18892833(501)>, running-active-NotVisible
default	21:04:02.718635-0400	ControlCenter	[app<application.com.nexy.assistant.18892826.18892833>:42161] Workspace state did change: BG-Active[40] --> XX-None[0] (assertion dropped).
default	21:04:02.718698-0400	runningboardd	Invalidating assertion 398-632-446371 (target:[app<application.com.nexy.assistant.18892826.18892833(501)>:42161]) from originator [osservice<com.apple.controlcenter(501)>:632]
default	21:04:02.823182-0400	runningboardd	[app<application.com.nexy.assistant.18892826.18892833(501)>:42161] Ignoring jetsam update because this process is not memory-managed
default	21:04:02.823190-0400	runningboardd	[app<application.com.nexy.assistant.18892826.18892833(501)>:42161] Ignoring suspend because this process is not lifecycle managed
default	21:04:02.823216-0400	runningboardd	[app<application.com.nexy.assistant.18892826.18892833(501)>:42161] Ignoring GPU update because this process is not GPU managed
default	21:04:02.823242-0400	runningboardd	[app<application.com.nexy.assistant.18892826.18892833(501)>:42161] Ignoring memory limit update because this process is not memory-managed
default	21:04:02.827923-0400	runningboardd	Calculated state for app<application.com.nexy.assistant.18892826.18892833(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	21:04:02.828243-0400	ControlCenter	Received state update for 42161 (app<application.com.nexy.assistant.18892826.18892833(501)>, running-active-NotVisible
default	21:04:02.829245-0400	gamepolicyd	Received state update for 42161 (app<application.com.nexy.assistant.18892826.18892833(501)>, running-active-NotVisible
default	21:04:03.065361-0400	kernel	tcp_connection_summary (tcp_close:1692)[<IPv4-redacted>:63402<-><IPv4-redacted>:50051] interface: en0 (skipped: 871)
so_gencnt: 2265966 t_state: SYN_SENT process: Nexy:42161 Duration: 20.002 sec Conn_Time: 0.000 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 0.000 ms rttvar: 250.000 ms base rtt: 0 ms so_error: 0 svc/tc: 0 flow: 0xb8b005cb
default	21:04:03.065396-0400	kernel	tcp_connection_summary [<IPv4-redacted>:63402<-><IPv4-redacted>:50051] interface: en0 (skipped: 871)
so_gencnt: 2265966 t_state: SYN_SENT process: Nexy:42161 flowctl: 0us (0x) SYN in/out: 0/9 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	21:04:03.066291-0400	kernel	SK[4]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid DF7A1FC5-F6E3-4367-9394-31B99BF6B4E7 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.63410,dst=<IPv4-redacted>.50051,proto=0x06 mask=0x0000003f,hash=0x021ae25d tp_proto=0x06"
default	21:04:03.066374-0400	kernel	tcp connect outgoing: [<IPv4-redacted>:63410<-><IPv4-redacted>:50051] interface: en0 (skipped: 871)
so_gencnt: 2266017 t_state: SYN_SENT process: Nexy:42161 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xa73f9863
default	21:04:05.584414-0400	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.18892826.18892833(501)>:42161] from originator [osservice<com.apple.controlcenter(501)>:632] with description <RBSAssertionDescriptor| "FBWorkspace (BG-Active[40])" ID:398-632-446387 target:42161 attributes:[
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableLPRunReason-Suspend" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableRole-NonUI" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableJetsamPriority-Active" sourceEnvironment:"(null)">
	]>
default	21:04:05.584554-0400	runningboardd	Assertion 398-632-446387 (target:[app<application.com.nexy.assistant.18892826.18892833(501)>:42161]) will be created as active
default	21:04:05.588001-0400	ControlCenter	[app<application.com.nexy.assistant.18892826.18892833>:42161] Workspace state did change: XX-None[0] --> BG-Active[40] (assertion acquired).
default	21:04:05.588218-0400	runningboardd	[app<application.com.nexy.assistant.18892826.18892833(501)>:42161] Ignoring jetsam update because this process is not memory-managed
default	21:04:05.588265-0400	runningboardd	[app<application.com.nexy.assistant.18892826.18892833(501)>:42161] Ignoring suspend because this process is not lifecycle managed
default	21:04:05.588345-0400	runningboardd	[app<application.com.nexy.assistant.18892826.18892833(501)>:42161] Ignoring GPU update because this process is not GPU managed
default	21:04:05.588402-0400	runningboardd	[app<application.com.nexy.assistant.18892826.18892833(501)>:42161] Ignoring memory limit update because this process is not memory-managed
default	21:04:05.591782-0400	runningboardd	Calculated state for app<application.com.nexy.assistant.18892826.18892833(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	21:04:05.592272-0400	ControlCenter	Received state update for 42161 (app<application.com.nexy.assistant.18892826.18892833(501)>, running-active-NotVisible
default	21:04:05.592390-0400	gamepolicyd	Received state update for 42161 (app<application.com.nexy.assistant.18892826.18892833(501)>, running-active-NotVisible
default	21:04:05.690237-0400	ControlCenter	[app<application.com.nexy.assistant.18892826.18892833>:42161] Workspace state did change: BG-Active[40] --> XX-None[0] (assertion dropped).
default	21:04:05.690448-0400	runningboardd	Invalidating assertion 398-632-446387 (target:[app<application.com.nexy.assistant.18892826.18892833(501)>:42161]) from originator [osservice<com.apple.controlcenter(501)>:632]
default	21:04:05.860604-0400	runningboardd	[app<application.com.nexy.assistant.18892826.18892833(501)>:42161] Ignoring jetsam update because this process is not memory-managed
default	21:04:05.860620-0400	runningboardd	[app<application.com.nexy.assistant.18892826.18892833(501)>:42161] Ignoring suspend because this process is not lifecycle managed
default	21:04:05.860635-0400	runningboardd	[app<application.com.nexy.assistant.18892826.18892833(501)>:42161] Ignoring GPU update because this process is not GPU managed
default	21:04:05.860665-0400	runningboardd	[app<application.com.nexy.assistant.18892826.18892833(501)>:42161] Ignoring memory limit update because this process is not memory-managed
default	21:04:05.866030-0400	runningboardd	Calculated state for app<application.com.nexy.assistant.18892826.18892833(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	21:04:05.866817-0400	ControlCenter	Received state update for 42161 (app<application.com.nexy.assistant.18892826.18892833(501)>, running-active-NotVisible
default	21:04:05.867038-0400	gamepolicyd	Received state update for 42161 (app<application.com.nexy.assistant.18892826.18892833(501)>, running-active-NotVisible
default	21:04:07.661864-0400	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.18892826.18892833(501)>:42161] from originator [osservice<com.apple.controlcenter(501)>:632] with description <RBSAssertionDescriptor| "FBWorkspace (BG-Active[40])" ID:398-632-446405 target:42161 attributes:[
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableLPRunReason-Suspend" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableRole-NonUI" sourceEnvironment:"(null)">,
	<RBSDomainAttribute| domain:"com.apple.frontboard" name:"SuspendableJetsamPriority-Active" sourceEnvironment:"(null)">
	]>
default	21:04:07.662010-0400	runningboardd	Assertion 398-632-446405 (target:[app<application.com.nexy.assistant.18892826.18892833(501)>:42161]) will be created as active
default	21:04:07.662225-0400	ControlCenter	[app<application.com.nexy.assistant.18892826.18892833>:42161] Workspace state did change: XX-None[0] --> BG-Active[40] (assertion acquired).
default	21:04:07.662347-0400	runningboardd	[app<application.com.nexy.assistant.18892826.18892833(501)>:42161] Ignoring jetsam update because this process is not memory-managed
default	21:04:07.662358-0400	runningboardd	[app<application.com.nexy.assistant.18892826.18892833(501)>:42161] Ignoring suspend because this process is not lifecycle managed
default	21:04:07.662444-0400	runningboardd	[app<application.com.nexy.assistant.18892826.18892833(501)>:42161] Ignoring GPU update because this process is not GPU managed
default	21:04:07.662570-0400	runningboardd	[app<application.com.nexy.assistant.18892826.18892833(501)>:42161] Ignoring memory limit update because this process is not memory-managed
default	21:04:07.666486-0400	runningboardd	Calculated state for app<application.com.nexy.assistant.18892826.18892833(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	21:04:07.667496-0400	ControlCenter	Received state update for 42161 (app<application.com.nexy.assistant.18892826.18892833(501)>, running-active-NotVisible
default	21:04:07.768277-0400	ControlCenter	[app<application.com.nexy.assistant.18892826.18892833>:42161] Workspace state did change: BG-Active[40] --> XX-None[0] (assertion dropped).
default	21:04:07.768424-0400	runningboardd	Invalidating assertion 398-632-446405 (target:[app<application.com.nexy.assistant.18892826.18892833(501)>:42161]) from originator [osservice<com.apple.controlcenter(501)>:632]
default	21:04:07.876152-0400	runningboardd	[app<application.com.nexy.assistant.18892826.18892833(501)>:42161] Ignoring jetsam update because this process is not memory-managed
default	21:04:07.876214-0400	runningboardd	[app<application.com.nexy.assistant.18892826.18892833(501)>:42161] Ignoring suspend because this process is not lifecycle managed
default	21:04:07.876285-0400	runningboardd	[app<application.com.nexy.assistant.18892826.18892833(501)>:42161] Ignoring GPU update because this process is not GPU managed
default	21:04:07.876370-0400	runningboardd	[app<application.com.nexy.assistant.18892826.18892833(501)>:42161] Ignoring memory limit update because this process is not memory-managed
default	21:04:07.885144-0400	runningboardd	Calculated state for app<application.com.nexy.assistant.18892826.18892833(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	21:04:07.885565-0400	ControlCenter	Received state update for 42161 (app<application.com.nexy.assistant.18892826.18892833(501)>, running-active-NotVisible
default	21:04:07.888158-0400	gamepolicyd	Received state update for 42161 (app<application.com.nexy.assistant.18892826.18892833(501)>, running-active-NotVisible
default	21:04:13.068506-0400	kernel	udp connect: [<IPv4-redacted>:49445<-><IPv4-redacted>:50051] interface:  (skipped: 617)
so_gencnt: 2266175 so_state: 0x0002 process: Nexy:42161 bytes in/out: 0/0 pkts in/out: 0/0 error: 0 so_error: 0 svc/tc: 0 flow: 0xb4f8ea46
default	21:04:13.068547-0400	kernel	udp_connection_summary [<IPv4-redacted>:49445<-><IPv4-redacted>:50051] interface:  (skipped: 617)
so_gencnt: 2266175 so_state: 0x0002 process: Nexy:42161 Duration: 0.000 sec Conn_Time: 0.000 sec bytes in/out: 0/0 pkts in/out: 0/0 rxnospace pkts/bytes: 0/0 so_error: 0 svc/tc: 0 flow: 0xb4f8ea46 flowctl: 0us (0x)
default	21:04:15.052720-0400	kernel	udp connect: [<IPv4-redacted>:62645<-><IPv4-redacted>:50051] interface:  (skipped: 617)
so_gencnt: 2266179 so_state: 0x0002 process: Nexy:42161 bytes in/out: 0/0 pkts in/out: 0/0 error: 0 so_error: 0 svc/tc: 0 flow: 0xa6a2a868
default	21:04:15.052769-0400	kernel	udp_connection_summary [<IPv4-redacted>:62645<-><IPv4-redacted>:50051] interface:  (skipped: 617)
so_gencnt: 2266179 so_state: 0x0002 process: Nexy:42161 Duration: 0.000 sec Conn_Time: 0.000 sec bytes in/out: 0/0 pkts in/out: 0/0 rxnospace pkts/bytes: 0/0 so_error: 0 svc/tc: 0 flow: 0xa6a2a868 flowctl: 0us (0x)
default	21:04:25.852448-0400	WindowServer	a2c13[StealKeyFocusReturningID]: [DeferringManager] Updating policy {
    advicePolicy: .keyThief;
    frontmostProcess: 0x0-0x926926 (Console) mainConnectionID: 8B9E7;
    keyThiefConnectionID: A2C13;
} for reason: key thief updated a2c13 0x0-0x965965 (Nexy)
default	21:04:25.852497-0400	WindowServer	<BSCompoundAssertion:0x7fb015380> (com.apple.backboard.hid.delivery.localDelivery.preventFlushing) acquire for reason:key thief updated a2c13 0x0-0x965965 (Nexy) <7831> acq:0x800bd26a0 count:1
default	21:04:25.917095-0400	Nexy	[com.apple.controlcenter:7394A576-D823-4503-AA70-D223BBF79BC1] Sending action(s) in update: NSSceneFenceAction
default	21:04:25.949863-0400	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.18892826.18892833(501)>:42161] from originator [osservice<com.apple.WindowServer(88)>:393] with description <RBSAssertionDescriptor| "AppVisible" ID:398-393-446412 target:42161 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"AppVisible" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	21:04:25.949928-0400	runningboardd	Assertion 398-393-446412 (target:[app<application.com.nexy.assistant.18892826.18892833(501)>:42161]) will be created as active
default	21:04:25.950392-0400	runningboardd	[app<application.com.nexy.assistant.18892826.18892833(501)>:42161] Ignoring jetsam update because this process is not memory-managed
default	21:04:25.950407-0400	runningboardd	[app<application.com.nexy.assistant.18892826.18892833(501)>:42161] Ignoring suspend because this process is not lifecycle managed
default	21:04:25.950417-0400	runningboardd	[app<application.com.nexy.assistant.18892826.18892833(501)>:42161] Ignoring GPU update because this process is not GPU managed
default	21:04:25.950439-0400	runningboardd	[app<application.com.nexy.assistant.18892826.18892833(501)>:42161] Ignoring memory limit update because this process is not memory-managed
default	21:04:25.953573-0400	runningboardd	Calculated state for app<application.com.nexy.assistant.18892826.18892833(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	21:04:25.954052-0400	ControlCenter	Received state update for 42161 (app<application.com.nexy.assistant.18892826.18892833(501)>, running-active-NotVisible
default	21:04:25.954174-0400	gamepolicyd	Received state update for 42161 (app<application.com.nexy.assistant.18892826.18892833(501)>, running-active-NotVisible
default	21:04:25.967616-0400	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.18892826.18892833(501)>:42161] from originator [osservice<com.apple.WindowServer(88)>:393] with description <RBSAssertionDescriptor| "FUSBProcessWindowState: visible" ID:398-393-446413 target:42161 attributes:[
	<RBSDomainAttribute| domain:"com.apple.fuseboard" name:"Visible" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	21:04:25.967689-0400	runningboardd	Assertion 398-393-446413 (target:[app<application.com.nexy.assistant.18892826.18892833(501)>:42161]) will be created as active
default	21:04:25.968040-0400	runningboardd	[app<application.com.nexy.assistant.18892826.18892833(501)>:42161] Ignoring jetsam update because this process is not memory-managed
default	21:04:25.968056-0400	runningboardd	[app<application.com.nexy.assistant.18892826.18892833(501)>:42161] Ignoring suspend because this process is not lifecycle managed
default	21:04:25.968071-0400	runningboardd	[app<application.com.nexy.assistant.18892826.18892833(501)>:42161] Ignoring GPU update because this process is not GPU managed
default	21:04:25.968146-0400	runningboardd	[app<application.com.nexy.assistant.18892826.18892833(501)>:42161] Ignoring memory limit update because this process is not memory-managed
default	21:04:25.968185-0400	runningboardd	[app<application.com.nexy.assistant.18892826.18892833(501)>:42161] visiblity is yes
default	21:04:25.971379-0400	runningboardd	Calculated state for app<application.com.nexy.assistant.18892826.18892833(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	21:04:25.971801-0400	ControlCenter	Received state update for 42161 (app<application.com.nexy.assistant.18892826.18892833(501)>, running-active-NotVisible
default	21:04:25.971889-0400	gamepolicyd	Received state update for 42161 (app<application.com.nexy.assistant.18892826.18892833(501)>, running-active-NotVisible
default	21:04:27.012799-0400	Nexy	[C:3] Alloc com.apple.backboard.hid-services.xpc
default	21:04:27.012892-0400	Nexy	[0xc9589f980] activating connection: mach=false listener=false peer=false name=(anonymous)
error	21:04:27.013638-0400	Nexy	Unable to obtain a task name port right for pid 393: (os/kern) failure (0x5)
default	21:04:27.013926-0400	Nexy	BKSHIDEventDeliveryManager - connection activation
default	21:04:27.016437-0400	Nexy	terminate:
default	21:04:27.016462-0400	Nexy	void _NSDisableAutomaticTerminationAndLog(NSString *) Terminating
default	21:04:27.016482-0400	Nexy	-[NSApplication _pushPersistentStateTerminationGeneration] sPersistentStateTerminateStackHeight -> 1
default	21:04:27.016611-0400	Nexy	Attempting sudden termination (1st attempt)
default	21:04:27.016633-0400	Nexy	Checking whether app should terminate
default	21:04:27.017199-0400	Nexy	Asking app delegate whether applicationShouldTerminate:
default	21:04:27.017230-0400	Nexy	replyToApplicationShouldTerminate:YES
default	21:04:27.017287-0400	Nexy	App termination approved
default	21:04:27.017302-0400	Nexy	Termination commencing
default	21:04:27.017312-0400	Nexy	Attempting sudden termination (2nd attempt)
default	21:04:27.018572-0400	Nexy	Termination complete. Exiting without sudden termination.
default	21:04:27.019100-0400	Nexy	[0xc9589fac0] activating connection: mach=true listener=false peer=false name=com.apple.powerlog.plxpclogger.xpc
default	21:04:27.019176-0400	Nexy	Entering exit handler.
default	21:04:27.019187-0400	Nexy	Queueing exit procedure onto XPC queue. Any further messages sent will be discarded. activeSendTransactions=0
default	21:04:27.019246-0400	Nexy	Cancelling XPC connection. Any further reply handler invocations will not retry messages
default	21:04:27.019257-0400	Nexy	[0xc9589c8c0] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	21:04:27.019304-0400	Nexy	Exiting exit handler.
default	21:04:27.019325-0400	Nexy	XPC connection invalidated (daemon unloaded/disabled)
default	21:04:27.028281-0400	audiomxd	  ServerSessionManager.mm:472   { "action":"destroy_session", "session":{"ID":"0x1ef0a7","name":"Nexy(42161)"}, "details":null }
default	21:04:27.028311-0400	audiomxd	AudioApplicationInfoImpl.mm:690   Successfully removed session 0x1ef0a7 from AudioApp, recording state unchanged (app: {"name":"[implicit] Nexy","pid":42161})
default	21:04:27.028323-0400	audiomxd	  ServerSessionManager.mm:1081  destroy audio app instance since was created implicitly by session creation and all sessions now gone (audio app: {"name":"[implicit] Nexy","pid":42161})
default	21:04:27.028656-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 168, PID = 42161, Name = sid:0x1ef0a7, Nexy(42161), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	21:04:27.028793-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 168, PID = 42161, Name = sid:0x1ef0a7, Nexy(42161), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	21:04:27.029681-0400	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	21:04:27.029916-0400	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	21:04:27.030088-0400	WindowServer	0[outside of RPC]: Process death: 0x0-0x965965 (Nexy) connectionID: A2C13 pid: 42161 in session 0x101
default	21:04:27.030111-0400	WindowServer	<BSCompoundAssertion:0x7fb0154c0> ([FocusManager:257]-deferringPolicyEvaluationSuppression) acquire for reason:process death - 0x0-0x965965 (Nexy) acq:0x800bd09e0 count:1
default	21:04:27.030114-0400	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	21:04:27.030289-0400	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	21:04:27.030853-0400	WindowManager	Connection invalidated | (42161) Nexy
default	21:04:27.031625-0400	ControlCenter	[app<application.com.nexy.assistant.18892826.18892833>:42161] Workspace connection invalidated.
default	21:04:27.031646-0400	ControlCenter	[app<application.com.nexy.assistant.18892826.18892833>:42161] Now flagged as pending exit for reason: workspace client connection invalidated
default	21:04:27.041254-0400	WindowServer	0[outside of RPC]: [FocusManager:257] update to deferring policy requested for reason: permitted list updated - 0x0-0x965965 removed - but we are suppressing evaluation for reasons: {(
    "process death - 0x0-0x965965 (Nexy)"
)}
default	21:04:27.042027-0400	WindowServer	0[outside of RPC]: [FocusManager:257] update to deferring policy requested for reason: permitted list updated - 0x1-0xa4b1 removed - but we are suppressing evaluation for reasons: {(
    "process death - 0x0-0x965965 (Nexy)"
)}
default	21:04:27.043015-0400	kernel	tcp_connection_summary (tcp_close:1692)[<IPv4-redacted>:63410<-><IPv4-redacted>:50051] interface: en0 (skipped: 871)
so_gencnt: 2266017 t_state: SYN_SENT process: Nexy:42161 Duration: 23.977 sec Conn_Time: 0.000 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 0.000 ms rttvar: 250.000 ms base rtt: 0 ms so_error: 0 svc/tc: 0 flow: 0xa73f9863
default	21:04:27.043032-0400	kernel	tcp_connection_summary [<IPv4-redacted>:63410<-><IPv4-redacted>:50051] interface: en0 (skipped: 871)
so_gencnt: 2266017 t_state: SYN_SENT process: Nexy:42161 flowctl: 0us (0x) SYN in/out: 0/9 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	21:04:27.043184-0400	mDNSResponder	[R275821] DNSServiceCreateConnection STOP PID[42161](Nexy)
default	21:04:27.044266-0400	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	21:04:27.044533-0400	runningboardd	Invalidating assertion 398-393-446413 (target:[app<application.com.nexy.assistant.18892826.18892833(501)>:42161]) from originator [osservice<com.apple.WindowServer(88)>:393]
default	21:04:27.044559-0400	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	21:04:27.044687-0400	runningboardd	XPC connection invalidated: [app<application.com.nexy.assistant.18892826.18892833(501)>:42161]
default	21:04:27.044861-0400	runningboardd	Invalidating assertion 398-393-446412 (target:[app<application.com.nexy.assistant.18892826.18892833(501)>:42161]) from originator [osservice<com.apple.WindowServer(88)>:393]
default	21:04:27.045121-0400	runningboardd	[app<application.com.nexy.assistant.18892826.18892833(501)>:42161] termination reported by launchd (0, 0, 0)
default	21:04:27.045171-0400	runningboardd	Removing process: [app<application.com.nexy.assistant.18892826.18892833(501)>:42161]
default	21:04:27.045380-0400	runningboardd	Removing launch job for: [app<application.com.nexy.assistant.18892826.18892833(501)>:42161]
default	21:04:27.045609-0400	runningboardd	Removed job for [app<application.com.nexy.assistant.18892826.18892833(501)>:42161]
default	21:04:27.045653-0400	runningboardd	Removing assertions for terminated process: [app<application.com.nexy.assistant.18892826.18892833(501)>:42161]
default	21:04:27.045691-0400	runningboardd	Removed last relative-start-date-defining assertion for process app<application.com.nexy.assistant.18892826.18892833(501)>
default	21:04:27.050679-0400	coreaudiod	>>> NEGOTIATE [com.nexy.assistant]
default	21:04:27.051068-0400	coreaudiod	<<< NEGOTIATE [com.nexy.assistant]
default	21:04:27.052156-0400	coreaudiod	IssueReporting.cpp:492   RTAID [ use_case=Generic report_type=RMS Generic Chain clientID=ADM node=ADM::com.nexy.assistant_26022.25941.0_airpods noise suppression studio::out-0 issue_detected_sample_time=192000.000000 ] -- [ rms:[-59.849834], peaks:[-31.280546] ]
default	21:04:27.052170-0400	coreaudiod	IssueReporting.cpp:492   RTAID [ use_case=Generic report_type=RMS Generic Chain clientID=ADM node=ADM::com.nexy.assistant_26022.25941.0_airpods noise suppression studio::in-0 issue_detected_sample_time=0.000000 ] -- [ rms:[-58.598026], peaks:[-30.313717] ]
default	21:04:27.055408-0400	runningboardd	Calculated state for app<application.com.nexy.assistant.18892826.18892833(501)>: none (role: None) (endowments: (null))
default	21:04:27.055689-0400	runningboardd	Calculated state for app<application.com.nexy.assistant.18892826.18892833(501)>: none (role: None) (endowments: (null))
default	21:04:27.055720-0400	ControlCenter	[app<application.com.nexy.assistant.18892826.18892833>:42161] Process exited: <RBSProcessExitContext| voluntary>.
default	21:04:27.055740-0400	ControlCenter	[app<application.com.nexy.assistant.18892826.18892833>:42161] Setting process task state to: Not Running
default	21:04:27.055788-0400	ControlCenter	[app<application.com.nexy.assistant.18892826.18892833>:42161] Setting process visibility to: Unknown
default	21:04:27.055820-0400	ControlCenter	Received state update for 42161 (app<application.com.nexy.assistant.18892826.18892833(501)>, none-NotVisible
default	21:04:27.055835-0400	audiomxd	  ServerSessionManager.mm:1322  Monitored process died, pid = 42161, name = Nexy
default	21:04:27.055861-0400	ControlCenter	[app<application.com.nexy.assistant.18892826.18892833>:42161] Invalidating workspace.
default	21:04:27.055932-0400	ControlCenter	Removing source registration for processHandle: [app<application.com.nexy.assistant.18892826.18892833(501)>:42161]
default	21:04:27.056118-0400	ControlCenter	Received state update for 42161 (app<application.com.nexy.assistant.18892826.18892833(501)>, none-NotVisible
default	21:04:27.056313-0400	loginwindow	-[ApplicationManager handleCASEvent:withData:] | CAS notification for appDeath for com.nexy.assistant with asn: LSASN:{hi=0x0;lo=0x965965} for bundle path: /Applications/Nexy.app with URL: file:///Applications/Nexy.app/
default	21:04:27.056344-0400	loginwindow	-[ApplicationManager(AppDeathHandler) appDeathCleanupHandler:forApp:] | Termination handler for: Nexy : 9853285
default	21:04:27.056365-0400	ControlCenter	Removing: <FBApplicationProcess: 0xaf8352e80; app<application.com.nexy.assistant.18892826.18892833>:42161(vD314B)>
default	21:04:27.056395-0400	loginwindow	-[PersistentAppsSupport applicationQuit:] | for app:Nexy, _appTrackingState = 2
default	21:04:27.059679-0400	gamepolicyd	Received state update for 42161 (app<application.com.nexy.assistant.18892826.18892833(501)>, none-NotVisible
default	21:04:27.060133-0400	ControlCenter	Stopping tracking for host; (bid:com.nexy.assistant-Item-0-42161)
default	21:04:27.060213-0400	gamepolicyd	Received state update for 42161 (app<application.com.nexy.assistant.18892826.18892833(501)>, none-NotVisible
default	21:04:27.060415-0400	launchservicesd	Hit the server for a process handle 15ebe9370000a4b1 that resolved to: [app<application.com.nexy.assistant.18892826.18892833(501)>:42161]
default	21:04:27.062432-0400	ControlCenter	Removing ephemeral displayable instance DisplayableId(34A7C29C) from menu bar. No corresponding host (bid:com.nexy.assistant-Item-0-42161)
default	21:04:27.062498-0400	ControlCenter	Removing displayables [DisplayableAppStatusItem(34A7C29C, (bid:com.nexy.assistant-Item-0-42161))]
error	21:04:27.245306-0400	runningboardd	RBSStateCapture remove item called for untracked item 398-393-446413 (target:[app<application.com.nexy.assistant.18892826.18892833(501)>:42161])
error	21:04:27.245330-0400	runningboardd	RBSStateCapture remove item called for untracked item 398-393-446412 (target:[app<application.com.nexy.assistant.18892826.18892833(501)>:42161])
