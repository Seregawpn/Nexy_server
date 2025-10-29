default	16:55:24.191967-0400	kernel	SK[6]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid C381451B-9E16-425E-942F-97FD96522621 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.61846,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0x35d13a26 tp_proto=0x06"
default	16:55:24.192075-0400	kernel	tcp connect outgoing: [<IPv4-redacted>:61846<-><IPv4-redacted>:53] interface: en0 (skipped: 1087)
so_gencnt: 2603681 t_state: SYN_SENT process: Nexy:20663 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x98f82589
default	16:55:24.210207-0400	kernel	tcp connected: [<IPv4-redacted>:61846<-><IPv4-redacted>:53] interface: en0 (skipped: 1087)
so_gencnt: 2603681 t_state: ESTABLISHED process: Nexy:20663 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x98f82589
default	16:55:24.210525-0400	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:61846<-><IPv4-redacted>:53] interface: en0 (skipped: 1087)
so_gencnt: 2603681 t_state: FIN_WAIT_1 process: Nexy:20663 Duration: 0.018 sec Conn_Time: 0.018 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 18.000 ms rttvar: 9.000 ms base rtt: 18 ms so_error: 0 svc/tc: 0 flow: 0x98f82589
default	16:55:24.210535-0400	kernel	tcp_connection_summary [<IPv4-redacted>:61846<-><IPv4-redacted>:53] interface: en0 (skipped: 1087)
so_gencnt: 2603681 t_state: FIN_WAIT_1 process: Nexy:20663 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	16:55:24.238435-0400	Nexy	[0xa5e0e8000] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioComponentRegistrar
default	16:55:24.634861-0400	Nexy	                AUHAL.cpp:420   AUHAL: (0xa5f0bea40) Selecting device 85 from constructor
default	16:55:24.634876-0400	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0xa5f0bea40)
default	16:55:24.634884-0400	Nexy	                AUHAL.cpp:676   SelectDevice: (0xa5f0bea40) not already running
default	16:55:24.634887-0400	Nexy	                AUHAL.cpp:752   SelectDevice: (0xa5f0bea40) nothing to teardown
default	16:55:24.634892-0400	Nexy	                AUHAL.cpp:757   SelectDevice: (0xa5f0bea40) connecting device 85
default	16:55:24.635015-0400	Nexy	                AUHAL.cpp:3413  IsDeviceUsable: (0xa5f0bea40) Device ID: 85 (Input:No | Output:Yes): true
default	16:55:24.635128-0400	Nexy	                AUHAL.cpp:769   SelectDevice: (0xa5f0bea40) created ioproc 0xa for device 85
default	16:55:24.635263-0400	Nexy	                AUHAL.cpp:858   SelectDevice: (0xa5f0bea40) adding 7 device listeners to device 85
default	16:55:24.635492-0400	Nexy	                AUHAL.cpp:858   SelectDevice: (0xa5f0bea40) adding 0 device delegate listeners to device 85
default	16:55:24.635503-0400	Nexy	                AUHAL.cpp:1581  UpdateStreamFormats: -> (0xa5f0bea40)
default	16:55:24.635596-0400	Nexy	                AUHAL.cpp:1677  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  48000 Hz, Float32, interleaved
default	16:55:24.635607-0400	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 1 output streams; not all mono
default	16:55:24.635620-0400	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	16:55:24.635631-0400	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 0 input streams; not all mono
default	16:55:24.635639-0400	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	16:55:24.635756-0400	Nexy	                AUHAL.cpp:1771  UpdateStreamFormats: AUHAL(0xa5f0bea40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	16:55:24.635768-0400	Nexy	                AUHAL.cpp:1777  UpdateStreamFormats: AUHAL(0xa5f0bea40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	16:55:24.635776-0400	Nexy	                AUHAL.cpp:1787  UpdateStreamFormats: <-
default	16:55:24.635782-0400	Nexy	                AUHAL.cpp:895   SelectDevice: (0xa5f0bea40) removing 0 device listeners from device 0
default	16:55:24.635787-0400	Nexy	                AUHAL.cpp:895   SelectDevice: (0xa5f0bea40) removing 0 device delegate listeners from device 0
default	16:55:24.635792-0400	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0xa5f0bea40)
default	16:55:24.635806-0400	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Output stream enables: Stream 0 is DISABLED
default	16:55:24.635890-0400	Nexy	                AUHAL.cpp:2298  SetProperty: (0xa5f0bea40) caller requesting device change from 85 to 91
default	16:55:24.635901-0400	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0xa5f0bea40)
default	16:55:24.635907-0400	Nexy	                AUHAL.cpp:676   SelectDevice: (0xa5f0bea40) not already running
default	16:55:24.635914-0400	Nexy	                AUHAL.cpp:682   SelectDevice: (0xa5f0bea40) disconnecting device 85
default	16:55:24.635920-0400	Nexy	                AUHAL.cpp:746   SelectDevice: (0xa5f0bea40) destroying ioproc 0xa for device 85
default	16:55:24.635967-0400	Nexy	  AVAudioSession_MacOS.mm:1021  initForMacOS
default	16:55:24.636996-0400	Nexy	[0xa5e0e8280] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioSession
default	16:55:24.638209-0400	audiomxd	  ServerSessionManager.mm:315   { "action":"create_session", "session":{"ID":"0x1ef0c0","name":"Nexy(20663)"}, "details":{"PID":20663,"session_type":"Primary"} }
default	16:55:24.638298-0400	audiomxd	AudioApplicationInfoImpl.mm:250   Setting initial isRecording state: 0 for newly-created AudioApp
	app: {"name":"[implicit] Nexy","pid":20663}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1ef0c0, sessionType: 'prim', isRecording: false }, 
]
default	16:55:24.639046-0400	audiomxd	  ServerSessionManager.mm:1317  Start process monitoring, pid = 20663, name = Nexy
default	16:55:24.639369-0400	Nexy	    SessionCore_Create.mm:99    Created session 0xa5dbba680 with ID: 0x1ef0c0
default	16:55:24.640836-0400	Nexy	[0xa5e0e83c0] activating connection: mach=true listener=false peer=false name=com.apple.audioanalyticsd
default	16:55:24.640985-0400	Nexy	No persisted cache on this platform.
error	16:55:24.641315-0400	Nexy	Reporter disconnected. { function=sendMessage, reporterID=88746909237249 }
default	16:55:24.641330-0400	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped Unknown {1C-77-54-18-C8-A3:output, 0xa}
default	16:55:24.641391-0400	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	16:55:24.641490-0400	Nexy	                AUHAL.cpp:757   SelectDevice: (0xa5f0bea40) connecting device 91
default	16:55:24.641588-0400	Nexy	                AUHAL.cpp:3413  IsDeviceUsable: (0xa5f0bea40) Device ID: 91 (Input:Yes | Output:No): true
default	16:55:24.642824-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=401.4104, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=20663, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	16:55:24.643939-0400	tccd	AUTHREQ_SUBJECT: msgID=401.4104, subject=com.nexy.assistant,
default	16:55:24.644628-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x969135800 at /Applications/Nexy.app
default	16:55:24.659066-0400	tccd	AUTHREQ_PROMPTING: msgID=401.4104, service=kTCCServiceMicrophone, subject=Sub:{com.nexy.assistant}Resp:{TCCDProcess: identifier=com.nexy.assistant, pid=20663, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy},
default	16:55:25.903050-0400	tccd	Publishing <TCCDEvent: type=Create, service=kTCCServiceMicrophone, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 3 subscribers: {
    471 = "<TCCDEventSubscriber: token=471, state=Passed, csid=com.apple.chronod>";
    37 = "<TCCDEventSubscriber: token=37, state=Initial, csid=(null)>";
    476 = "<TCCDEventSubscriber: token=476, state=Passed, csid=com.apple.photolibraryd>";
}
default	16:55:25.903964-0400	Nexy	                AUHAL.cpp:769   SelectDevice: (0xa5f0bea40) created ioproc 0xa for device 91
default	16:55:25.904280-0400	Nexy	                AUHAL.cpp:858   SelectDevice: (0xa5f0bea40) adding 7 device listeners to device 91
default	16:55:25.904683-0400	Nexy	                AUHAL.cpp:858   SelectDevice: (0xa5f0bea40) adding 0 device delegate listeners to device 91
default	16:55:25.904700-0400	Nexy	                AUHAL.cpp:1581  UpdateStreamFormats: -> (0xa5f0bea40)
default	16:55:25.904719-0400	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 0 output streams; not all mono
default	16:55:25.904740-0400	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Output render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	16:55:25.905025-0400	Nexy	                AUHAL.cpp:1677  UpdateStreamFormats: 
  input stream 0 [0x5c]:  1 ch,  24000 Hz, Float32
default	16:55:25.905041-0400	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 1 input streams; all mono
default	16:55:25.905054-0400	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Input render format:  1 ch,  24000 Hz, Float32
default	16:55:25.905236-0400	Nexy	                AUHAL.cpp:1771  UpdateStreamFormats: AUHAL(0xa5f0bea40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	16:55:25.905252-0400	Nexy	                AUHAL.cpp:1777  UpdateStreamFormats: AUHAL(0xa5f0bea40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	16:55:25.905261-0400	Nexy	                AUHAL.cpp:1787  UpdateStreamFormats: <-
default	16:55:25.905334-0400	Nexy	                AUHAL.cpp:895   SelectDevice: (0xa5f0bea40) removing 7 device listeners from device 85
default	16:55:25.905651-0400	Nexy	                AUHAL.cpp:895   SelectDevice: (0xa5f0bea40) removing 0 device delegate listeners from device 85
default	16:55:25.905664-0400	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0xa5f0bea40)
default	16:55:25.906018-0400	chronod	[appAuth:com.nexy.assistant] tcc authorization(s) changed
default	16:55:25.906676-0400	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	16:55:25.908526-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=401.4105, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=20663, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	16:55:25.910178-0400	tccd	AUTHREQ_SUBJECT: msgID=401.4105, subject=com.nexy.assistant,
default	16:55:25.911731-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x969135800 at /Applications/Nexy.app
default	16:55:25.929552-0400	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	16:55:25.930818-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=401.4106, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=20663, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	16:55:25.931821-0400	tccd	AUTHREQ_SUBJECT: msgID=401.4106, subject=com.nexy.assistant,
default	16:55:25.932413-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x969135800 at /Applications/Nexy.app
default	16:55:25.948873-0400	Nexy	Registered notify signal com.apple.caulk.alloc.audiodump (0)
default	16:55:25.950800-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=401.4107, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=20663, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	16:55:25.952208-0400	tccd	AUTHREQ_SUBJECT: msgID=401.4107, subject=com.nexy.assistant,
default	16:55:25.952883-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x969135800 at /Applications/Nexy.app
default	16:55:25.965533-0400	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetPreferredChatFlavorForBundleID: <private>-><private> get value: 0
default	16:55:25.965862-0400	coreaudiod	>>> NEGOTIATE [com.nexy.assistant]
default	16:55:25.965995-0400	coreaudiod	<<< NEGOTIATE [com.nexy.assistant]
default	16:55:25.966126-0400	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetSupportedChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	16:55:25.967802-0400	coreaudiod	>>> ADAPT [com.nexy.assistant]
default	16:55:25.968719-0400	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOSupportedChatFlavors newValue: (
    0,
    2
)
default	16:55:25.969693-0400	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xbf61fd500] Created node ADM::com.nexy.assistant_28259.28176.0_airpods noise suppression studio::in-0 with nodeID 0 - reporting period = 10.000000, sample rate = 24000.000000
default	16:55:25.969757-0400	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xbf61fd500] Created node ADM::com.nexy.assistant_28259.28176.0_airpods noise suppression studio::out-0 with nodeID 1 - reporting period = 10.000000, sample rate = 24000.000000
default	16:55:26.046987-0400	runningboardd	Assertion did invalidate due to timeout: 398-398-500194 (target:[app<application.com.nexy.assistant.19166461.19166467(501)>:20663])
default	16:55:26.059400-0400	coreaudiod	<<< ADAPT [com.nexy.assistant]
default	16:55:26.061078-0400	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:28259 called from <private>
default	16:55:26.061120-0400	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	16:55:26.061129-0400	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Input {1C-77-54-18-C8-A3:input, 0xa}
default	16:55:26.065291-0400	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.19166461.19166467(501)>:20663] from originator [osservice<com.apple.powerd>:334] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:398-334-500209 target:20663 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	16:55:26.065427-0400	runningboardd	Assertion 398-334-500209 (target:[app<application.com.nexy.assistant.19166461.19166467(501)>:20663]) will be created as active
default	16:55:26.061808-0400	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(28258)
default	16:55:26.061842-0400	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:28258 called from <private>
default	16:55:26.061849-0400	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:28258 called from <private>
default	16:55:26.063024-0400	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:28259 called from <private>
default	16:55:26.063442-0400	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(28259)
default	16:55:26.068084-0400	runningboardd	[app<application.com.nexy.assistant.19166461.19166467(501)>:20663] Ignoring jetsam update because this process is not memory-managed
default	16:55:26.063467-0400	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:28259 called from <private>
default	16:55:26.063870-0400	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:28259 called from <private>
default	16:55:26.068164-0400	runningboardd	[app<application.com.nexy.assistant.19166461.19166467(501)>:20663] Ignoring suspend because this process is not lifecycle managed
default	16:55:26.068321-0400	runningboardd	[app<application.com.nexy.assistant.19166461.19166467(501)>:20663] Ignoring GPU update because this process is not GPU managed
default	16:55:26.069448-0400	runningboardd	[app<application.com.nexy.assistant.19166461.19166467(501)>:20663] Ignoring memory limit update because this process is not memory-managed
fault	16:55:26.070295-0400	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.19166461.19166467 AUID=501> and <type=Application identifier=application.com.nexy.assistant.19166461.19166467>
default	16:55:26.070873-0400	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	16:55:26.071036-0400	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	16:55:26.073147-0400	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(28259)
default	16:55:26.073175-0400	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(28259)
default	16:55:26.073188-0400	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(28259)
default	16:55:26.073194-0400	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(28259)
default	16:55:26.073204-0400	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(28259)
default	16:55:26.073215-0400	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(28259)
default	16:55:26.074119-0400	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:28259 called from <private>
default	16:55:26.074129-0400	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:28259 called from <private>
default	16:55:26.074150-0400	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:28259 called from <private>
default	16:55:26.074170-0400	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:28259 called from <private>
default	16:55:26.074179-0400	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:28259 called from <private>
default	16:55:26.074187-0400	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:28259 called from <private>
default	16:55:26.074232-0400	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:28259 called from <private>
fault	16:55:26.075725-0400	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.19166461.19166467 AUID=501> and <type=Application identifier=application.com.nexy.assistant.19166461.19166467>
default	16:55:26.080245-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=401.4108, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=20663, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	16:55:26.080641-0400	runningboardd	Calculated state for app<application.com.nexy.assistant.19166461.19166467(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	16:55:26.080924-0400	runningboardd	Invalidating assertion 398-334-500209 (target:[app<application.com.nexy.assistant.19166461.19166467(501)>:20663]) from originator [osservice<com.apple.powerd>:334]
default	16:55:26.081816-0400	tccd	AUTHREQ_SUBJECT: msgID=401.4108, subject=com.nexy.assistant,
default	16:55:26.082125-0400	gamepolicyd	Received state update for 20663 (app<application.com.nexy.assistant.19166461.19166467(501)>, running-active-NotVisible
default	16:55:26.083087-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x969135800 at /Applications/Nexy.app
default	16:55:26.084201-0400	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(28259)
default	16:55:26.084500-0400	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ef0c0","name":"Nexy(20663)"}, "details":{"deviceUIDs":["1C-77-54-18-C8-A3:input"],"implicit_category":"Record","input_running":true,"output_running":false} }
default	16:55:26.084942-0400	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:28258 called from <private>
default	16:55:26.084954-0400	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:28258 called from <private>
default	16:55:26.084639-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 193, PID = 20663, Name = sid:0x1ef0c0, Nexy(20663), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	16:55:26.085180-0400	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(28258)
default	16:55:26.084753-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 193, PID = 20663, Name = sid:0x1ef0c0, Nexy(20663), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	16:55:26.085510-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 193, PID = 20663, Name = sid:0x1ef0c0, Nexy(20663), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	16:55:26.085905-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 193, PID = 20663, Name = sid:0x1ef0c0, Nexy(20663), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	16:55:26.086399-0400	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 193, PID = 20663, Name = sid:0x1ef0c0, Nexy(20663), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> is going active
default	16:55:26.086453-0400	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1ef0c0, Nexy(20663), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 193 starting recording
default	16:55:26.086726-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 193, PID = 20663, Name = sid:0x1ef0c0, Nexy(20663), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	16:55:26.084918-0400	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1ef0c0, Nexy(20663), 'prim'', AudioCategory changed to 'Record_WithBluetooth'
default	16:55:26.086852-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 193, PID = 20663, Name = sid:0x1ef0c0, Nexy(20663), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	16:55:26.086931-0400	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1ef0c0, Nexy(20663), 'prim'', displayID:'com.nexy.assistant'}
default	16:55:26.087110-0400	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [1, 0]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:input"
)}
default	16:55:26.087124-0400	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	16:55:26.087322-0400	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	16:55:26.094100-0400	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:28258 called from <private>
default	16:55:26.094111-0400	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:28258 called from <private>
default	16:55:26.094187-0400	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(28258)
default	16:55:26.098959-0400	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(28258)
default	16:55:26.099234-0400	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:28258 called from <private>
default	16:55:26.099241-0400	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:28258 called from <private>
default	16:55:26.099314-0400	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(28258)
default	16:55:26.100313-0400	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	16:55:26.100373-0400	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	16:55:26.100404-0400	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	16:55:26.100620-0400	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	16:55:26.102349-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	16:55:26.102359-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	16:55:26.102405-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	16:55:26.102524-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	16:55:26.102602-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	16:55:26.102641-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	16:55:26.103899-0400	coreaudiod	>>> NEGOTIATE [com.nexy.assistant]
default	16:55:26.104527-0400	coreaudiod	<<< NEGOTIATE [com.nexy.assistant]
default	16:55:26.103684-0400	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	16:55:26.105237-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	16:55:26.105663-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	16:55:26.106321-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	16:55:26.106672-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	16:55:26.108431-0400	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:28259 called from <private>
default	16:55:26.108457-0400	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:28259 called from <private>
default	16:55:26.109899-0400	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	16:55:26.106918-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	16:55:26.110090-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	16:55:26.110850-0400	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:28259 called from <private>
default	16:55:26.119843-0400	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(28258)
default	16:55:26.119997-0400	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:28258 called from <private>
default	16:55:26.120078-0400	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:28258 called from <private>
default	16:55:26.115849-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=401.4109, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=20663, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	16:55:26.120151-0400	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:28258 called from <private>
default	16:55:26.115001-0400	runningboardd	Invalidating assertion 398-334-500210 (target:[app<application.com.nexy.assistant.19166461.19166467(501)>:20663]) from originator [osservice<com.apple.powerd>:334]
default	16:55:26.120239-0400	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:28258 called from <private>
default	16:55:26.182674-0400	coreaudiod	<<< ADAPT [com.nexy.assistant]
default	16:55:26.184184-0400	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:28259 called from <private>
default	16:55:26.186017-0400	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.19166461.19166467(501)>:20663] from originator [osservice<com.apple.powerd>:334] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:398-334-500212 target:20663 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	16:55:26.184235-0400	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:28259 called from <private>
default	16:55:26.184777-0400	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	16:55:26.186348-0400	runningboardd	Assertion 398-334-500212 (target:[app<application.com.nexy.assistant.19166461.19166467(501)>:20663]) will be created as active
default	16:55:26.188945-0400	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:28259 called from <private>
default	16:55:26.188962-0400	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:28259 called from <private>
default	16:55:26.189068-0400	runningboardd	Invalidating assertion 398-334-500212 (target:[app<application.com.nexy.assistant.19166461.19166467(501)>:20663]) from originator [osservice<com.apple.powerd>:334]
default	16:55:26.189121-0400	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:28259 called from <private>
default	16:55:26.189866-0400	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:28259 called from <private>
error	16:55:26.189879-0400	Nexy	         HALC_ProxyIOContext.cpp:1075  HALC_ProxyIOContext::_StartIO(): Start failed - StartAndWaitForState returned error 35
default	16:55:26.189888-0400	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:28259 called from <private>
default	16:55:26.190038-0400	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(28259)
default	16:55:26.190905-0400	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	16:55:26.191098-0400	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	16:55:26.191698-0400	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(28259)
default	16:55:26.191842-0400	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:28259 called from <private>
default	16:55:26.191998-0400	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:28259 called from <private>
default	16:55:26.192115-0400	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:28259 called from <private>
default	16:55:26.192135-0400	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:28259 called from <private>
default	16:55:26.194088-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=401.4110, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=20663, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	16:55:26.195271-0400	tccd	AUTHREQ_SUBJECT: msgID=401.4110, subject=com.nexy.assistant,
default	16:55:26.195935-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x969135800 at /Applications/Nexy.app
default	16:55:26.196001-0400	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	16:55:26.196043-0400	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	16:55:26.196079-0400	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	16:55:26.196235-0400	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	16:55:26.196777-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	16:55:26.196796-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	16:55:26.196810-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	16:55:26.196818-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	16:55:26.196825-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	16:55:26.196835-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	16:55:26.196969-0400	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	16:55:26.212918-0400	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:28259 called from <private>
default	16:55:26.212973-0400	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:28259 called from <private>
default	16:55:26.213097-0400	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.19166461.19166467(501)>:20663] from originator [osservice<com.apple.powerd>:334] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:398-334-500213 target:20663 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	16:55:26.213762-0400	runningboardd	Assertion 398-334-500213 (target:[app<application.com.nexy.assistant.19166461.19166467(501)>:20663]) will be created as active
default	16:55:26.215728-0400	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:28259 called from <private>
default	16:55:26.215785-0400	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	16:55:26.217384-0400	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:28259 called from <private>
default	16:55:26.217703-0400	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(28259)
default	16:55:26.217720-0400	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:28259 called from <private>
default	16:55:26.217736-0400	runningboardd	Invalidating assertion 398-334-500213 (target:[app<application.com.nexy.assistant.19166461.19166467(501)>:20663]) from originator [osservice<com.apple.powerd>:334]
default	16:55:26.217726-0400	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:28259 called from <private>
default	16:55:26.218600-0400	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	16:55:26.218739-0400	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	16:55:26.219110-0400	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(28259)
default	16:55:26.219258-0400	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:28259 called from <private>
default	16:55:26.219273-0400	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:28259 called from <private>
default	16:55:26.219289-0400	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:28259 called from <private>
default	16:55:26.220840-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=401.4111, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=20663, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	16:55:26.222234-0400	tccd	AUTHREQ_SUBJECT: msgID=401.4111, subject=com.nexy.assistant,
default	16:55:26.223083-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x969135800 at /Applications/Nexy.app
default	16:55:26.223913-0400	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	16:55:26.223975-0400	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	16:55:26.224020-0400	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	16:55:26.224153-0400	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	16:55:26.224706-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	16:55:26.224720-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	16:55:26.240446-0400	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:28259 called from <private>
default	16:55:26.241947-0400	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.19166461.19166467(501)>:20663] from originator [osservice<com.apple.powerd>:334] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:398-334-500214 target:20663 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	16:55:26.242023-0400	runningboardd	Assertion 398-334-500214 (target:[app<application.com.nexy.assistant.19166461.19166467(501)>:20663]) will be created as active
default	16:55:26.249167-0400	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	16:55:26.249213-0400	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	16:55:26.249249-0400	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	16:55:26.249665-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	16:55:26.249674-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	16:55:26.249686-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	16:55:26.249701-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	16:55:26.249711-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	16:55:26.249733-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	16:55:26.512653-0400	audioaccessoryd	AudioStateSnapshot: Route:Bluetooth App com.nexy.assistant, Score 200, Remote 100NumofApp 1
default	16:55:27.270926-0400	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xa}
default	16:55:27.271316-0400	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ef0c0","name":"Nexy(20663)"}, "details":{"deviceUIDs":[],"implicit_category":"","input_running":false,"output_running":false} }
default	16:55:27.271482-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 193, PID = 20663, Name = sid:0x1ef0c0, Nexy(20663), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	16:55:27.271560-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 193, PID = 20663, Name = sid:0x1ef0c0, Nexy(20663), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	16:55:27.271603-0400	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1ef0c0, Nexy(20663), 'prim'', displayID:'com.nexy.assistant'}
default	16:55:27.271665-0400	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	16:55:27.271682-0400	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1ef0c0, Nexy(20663), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 193 stopping recording
default	16:55:27.271716-0400	audiomxd	-MXCoreSession- -[MXCoreSession endInterruption:]: Session <ID: 193, PID = 20663, Name = sid:0x1ef0c0, Nexy(20663), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> is going inactive
default	16:55:27.271779-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 193, PID = 20663, Name = sid:0x1ef0c0, Nexy(20663), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	16:55:27.271872-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 193, PID = 20663, Name = sid:0x1ef0c0, Nexy(20663), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	16:55:27.272077-0400	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 0]. BT device UIDS: {(
)}
default	16:55:27.272090-0400	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	16:55:27.272125-0400	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 200 flag 0x1 < Hijack > app com.nexy.assistant CID 0xD310001 category Not set
default	16:55:27.272428-0400	audiomxd	UpdateAudioState CID 0xD310001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	16:55:27.272480-0400	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	16:55:27.272541-0400	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	16:55:27.272578-0400	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	16:55:27.272598-0400	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	16:55:27.272618-0400	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	16:55:27.272696-0400	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	16:55:27.272711-0400	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	16:55:27.272727-0400	audioaccessoryd	AudioStateChanged: Removed audio session app com.nexy.assistant 201 count 0
default	16:55:27.275346-0400	runningboardd	Invalidating assertion 398-334-500214 (target:[app<application.com.nexy.assistant.19166461.19166467(501)>:20663]) from originator [osservice<com.apple.powerd>:334]
default	16:55:27.278868-0400	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	16:55:27.282179-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	16:55:27.282188-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	16:55:27.282201-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	16:55:27.282207-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	16:55:27.282212-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	16:55:27.282218-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	16:55:27.282320-0400	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	16:55:27.288827-0400	runningboardd	[app<application.com.nexy.assistant.19166461.19166467(501)>:20663] Ignoring jetsam update because this process is not memory-managed
default	16:55:27.288846-0400	runningboardd	[app<application.com.nexy.assistant.19166461.19166467(501)>:20663] Ignoring suspend because this process is not lifecycle managed
default	16:55:27.288861-0400	runningboardd	[app<application.com.nexy.assistant.19166461.19166467(501)>:20663] Ignoring GPU update because this process is not GPU managed
default	16:55:27.288888-0400	runningboardd	[app<application.com.nexy.assistant.19166461.19166467(501)>:20663] Ignoring memory limit update because this process is not memory-managed
default	16:55:27.292766-0400	runningboardd	Calculated state for app<application.com.nexy.assistant.19166461.19166467(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	16:55:27.293503-0400	gamepolicyd	Received state update for 20663 (app<application.com.nexy.assistant.19166461.19166467(501)>, running-active-NotVisible
default	16:55:27.372447-0400	Nexy	                AUHAL.cpp:473   ~AUHAL: (0xa5f0bea40) Selecting device 0 from destructor
default	16:55:27.372461-0400	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0xa5f0bea40)
default	16:55:27.372467-0400	Nexy	                AUHAL.cpp:676   SelectDevice: (0xa5f0bea40) not already running
default	16:55:27.372473-0400	Nexy	                AUHAL.cpp:682   SelectDevice: (0xa5f0bea40) disconnecting device 91
default	16:55:27.372478-0400	Nexy	                AUHAL.cpp:746   SelectDevice: (0xa5f0bea40) destroying ioproc 0xa for device 91
default	16:55:27.372503-0400	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xa}
default	16:55:27.372530-0400	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	16:55:27.372661-0400	Nexy	                AUHAL.cpp:848   SelectDevice: (0xa5f0bea40) nothing to setup
default	16:55:27.372673-0400	Nexy	                AUHAL.cpp:858   SelectDevice: (0xa5f0bea40) adding 0 device listeners to device 0
default	16:55:27.372679-0400	Nexy	                AUHAL.cpp:858   SelectDevice: (0xa5f0bea40) adding 0 device delegate listeners to device 0
default	16:55:27.372685-0400	Nexy	                AUHAL.cpp:895   SelectDevice: (0xa5f0bea40) removing 7 device listeners from device 91
default	16:55:27.372905-0400	Nexy	                AUHAL.cpp:895   SelectDevice: (0xa5f0bea40) removing 0 device delegate listeners from device 91
default	16:55:27.372917-0400	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0xa5f0bea40)
default	16:55:27.637527-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=20671.1, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=20663, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.osascript, pid=20671, auid=501, euid=501, binary_path=/usr/bin/osascript}, },
default	16:55:27.639570-0400	tccd	AUTHREQ_SUBJECT: msgID=20671.1, subject=com.nexy.assistant,
default	16:55:27.640398-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117600 at /Applications/Nexy.app
default	16:55:27.661067-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=393.6891, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=20663, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.osascript, pid=20671, auid=501, euid=501, binary_path=/usr/bin/osascript}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=393, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	16:55:27.662405-0400	tccd	AUTHREQ_SUBJECT: msgID=393.6891, subject=com.nexy.assistant,
default	16:55:27.663616-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117600 at /Applications/Nexy.app
default	16:55:27.705028-0400	loginwindow	-[Application updateInformation] | Got App URL: file:///Applications/Nexy.app/
default	16:55:27.705156-0400	loginwindow	-[ApplicationManager checkInAppContext:eventData:] | ApplicationManager: Checked in app : Nexy
default	16:55:27.704171-0400	launchservicesd	CHECKIN:0x0-0xa91a91 20671 com.nexy.assistant
default	16:55:27.706031-0400	runningboardd	Invalidating assertion 398-363-500195 (target:[app<application.com.nexy.assistant.19166461.19166467(501)>:20663]) from originator [osservice<com.apple.coreservices.launchservicesd>:363]
default	16:55:27.711707-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117600 at /Applications/Nexy.app
default	16:55:27.711961-0400	WindowServer	beae3[CreateApplication]: Process creation: 0x0-0xa91a91 (Nexy) connectionID: BEAE3 pid: 20671 in session 0x101
default	16:55:27.714478-0400	loginwindow	-[Application updateInformation] | Got App URL: file:///Applications/Nexy.app/
default	16:55:27.813882-0400	runningboardd	[app<application.com.nexy.assistant.19166461.19166467(501)>:20663] Ignoring jetsam update because this process is not memory-managed
default	16:55:27.813896-0400	runningboardd	[app<application.com.nexy.assistant.19166461.19166467(501)>:20663] Ignoring suspend because this process is not lifecycle managed
default	16:55:27.813934-0400	runningboardd	[app<application.com.nexy.assistant.19166461.19166467(501)>:20663] Set darwin role to: None
default	16:55:27.813945-0400	runningboardd	[app<application.com.nexy.assistant.19166461.19166467(501)>:20663] Ignoring GPU update because this process is not GPU managed
default	16:55:27.813962-0400	runningboardd	[app<application.com.nexy.assistant.19166461.19166467(501)>:20663] Ignoring memory limit update because this process is not memory-managed
default	16:55:27.816739-0400	runningboardd	Calculated state for app<application.com.nexy.assistant.19166461.19166467(501)>: running-suspended (role: None) (endowments: (null))
default	16:55:27.817094-0400	gamepolicyd	Received state update for 20663 (app<application.com.nexy.assistant.19166461.19166467(501)>, running-suspended-NotVisible
default	16:55:27.878555-0400	System Events	TCCAccessRequestIndirect: TCCAccessRequestIndirect with pid 20672: target_identity: {
    kTCCCodeIdentityAuditToken = {length = 32, bytes = 0xf5010000 f5010000 14000000 f5010000 ... b7860100 6ed90f00 };
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
default	16:55:27.898890-0400	tccd	target_executable_path_URL: file:///Applications/Nexy.app/Contents/MacOS/Nexy
default	16:55:27.943743-0400	WindowServer	0[outside of RPC]: Process death: 0x0-0xa91a91 (Nexy) connectionID: BEAE3 pid: 20671 in session 0x101
default	16:55:27.943764-0400	WindowServer	<BSCompoundAssertion:0x7fb0154c0> ([FocusManager:257]-deferringPolicyEvaluationSuppression) acquire for reason:process death - 0x0-0xa91a91 (Nexy) acq:0x8012af520 count:1
default	16:55:27.944324-0400	WindowServer	0[outside of RPC]: [FocusManager:257] update to deferring policy requested for reason: permitted list updated - 0x0-0xa91a91 removed - but we are suppressing evaluation for reasons: {(
    "process death - 0x0-0xa91a91 (Nexy)"
)}
default	16:55:27.944518-0400	WindowServer	0[outside of RPC]: [FocusManager:257] update to deferring policy requested for reason: permitted list updated - 0x1-0x50bf removed - but we are suppressing evaluation for reasons: {(
    "process death - 0x0-0xa91a91 (Nexy)"
)}
default	16:55:27.947191-0400	loginwindow	-[ApplicationManager handleCASEvent:withData:] | CAS notification for appDeath for com.nexy.assistant with asn: LSASN:{hi=0x0;lo=0xa91a91} for bundle path: /Applications/Nexy.app with URL: file:///Applications/Nexy.app/
default	16:55:27.947216-0400	loginwindow	-[ApplicationManager(AppDeathHandler) appDeathCleanupHandler:forApp:] | Termination handler for: Nexy : 11082385
default	16:55:27.947283-0400	loginwindow	-[PersistentAppsSupport applicationQuit:] | for app:Nexy, _appTrackingState = 2
default	16:55:28.104849-0400	Nexy	                AUHAL.cpp:420   AUHAL: (0xa5f0bea40) Selecting device 85 from constructor
default	16:55:28.104857-0400	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0xa5f0bea40)
default	16:55:28.104863-0400	Nexy	                AUHAL.cpp:676   SelectDevice: (0xa5f0bea40) not already running
default	16:55:28.104867-0400	Nexy	                AUHAL.cpp:752   SelectDevice: (0xa5f0bea40) nothing to teardown
default	16:55:28.104871-0400	Nexy	                AUHAL.cpp:757   SelectDevice: (0xa5f0bea40) connecting device 85
default	16:55:28.104975-0400	Nexy	                AUHAL.cpp:3413  IsDeviceUsable: (0xa5f0bea40) Device ID: 85 (Input:No | Output:Yes): true
default	16:55:28.105082-0400	Nexy	                AUHAL.cpp:769   SelectDevice: (0xa5f0bea40) created ioproc 0xb for device 85
default	16:55:28.105221-0400	Nexy	                AUHAL.cpp:858   SelectDevice: (0xa5f0bea40) adding 7 device listeners to device 85
default	16:55:28.105365-0400	Nexy	                AUHAL.cpp:858   SelectDevice: (0xa5f0bea40) adding 0 device delegate listeners to device 85
default	16:55:28.105371-0400	Nexy	                AUHAL.cpp:1581  UpdateStreamFormats: -> (0xa5f0bea40)
default	16:55:28.105442-0400	Nexy	                AUHAL.cpp:1677  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  24000 Hz, Float32, interleaved
default	16:55:28.105453-0400	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 1 output streams; not all mono
default	16:55:28.105459-0400	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Output render format:  2 ch,  24000 Hz, Float32, interleaved
default	16:55:28.105465-0400	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 0 input streams; not all mono
default	16:55:28.105472-0400	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	16:55:28.105580-0400	Nexy	                AUHAL.cpp:1771  UpdateStreamFormats: AUHAL(0xa5f0bea40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	16:55:28.105588-0400	Nexy	                AUHAL.cpp:1777  UpdateStreamFormats: AUHAL(0xa5f0bea40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	16:55:28.105593-0400	Nexy	                AUHAL.cpp:1787  UpdateStreamFormats: <-
default	16:55:28.105597-0400	Nexy	                AUHAL.cpp:895   SelectDevice: (0xa5f0bea40) removing 0 device listeners from device 0
default	16:55:28.105601-0400	Nexy	                AUHAL.cpp:895   SelectDevice: (0xa5f0bea40) removing 0 device delegate listeners from device 0
default	16:55:28.105603-0400	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0xa5f0bea40)
default	16:55:28.105617-0400	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Output stream enables: Stream 0 is DISABLED
default	16:55:28.105674-0400	Nexy	                AUHAL.cpp:2298  SetProperty: (0xa5f0bea40) caller requesting device change from 85 to 91
default	16:55:28.105679-0400	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0xa5f0bea40)
default	16:55:28.105684-0400	Nexy	                AUHAL.cpp:676   SelectDevice: (0xa5f0bea40) not already running
default	16:55:28.105688-0400	Nexy	                AUHAL.cpp:682   SelectDevice: (0xa5f0bea40) disconnecting device 85
default	16:55:28.105691-0400	Nexy	                AUHAL.cpp:746   SelectDevice: (0xa5f0bea40) destroying ioproc 0xb for device 85
default	16:55:28.105707-0400	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped Unknown {1C-77-54-18-C8-A3:output, 0xb}
default	16:55:28.105731-0400	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	16:55:28.105809-0400	Nexy	                AUHAL.cpp:757   SelectDevice: (0xa5f0bea40) connecting device 91
default	16:55:28.105895-0400	Nexy	                AUHAL.cpp:3413  IsDeviceUsable: (0xa5f0bea40) Device ID: 91 (Input:Yes | Output:No): true
default	16:55:28.107062-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=401.4112, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=20663, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	16:55:28.107994-0400	tccd	AUTHREQ_SUBJECT: msgID=401.4112, subject=com.nexy.assistant,
default	16:55:28.108562-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x969135800 at /Applications/Nexy.app
default	16:55:28.121236-0400	Nexy	                AUHAL.cpp:769   SelectDevice: (0xa5f0bea40) created ioproc 0xb for device 91
default	16:55:28.121423-0400	Nexy	                AUHAL.cpp:858   SelectDevice: (0xa5f0bea40) adding 7 device listeners to device 91
default	16:55:28.121664-0400	Nexy	                AUHAL.cpp:858   SelectDevice: (0xa5f0bea40) adding 0 device delegate listeners to device 91
default	16:55:28.121689-0400	Nexy	                AUHAL.cpp:1581  UpdateStreamFormats: -> (0xa5f0bea40)
default	16:55:28.121756-0400	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 0 output streams; not all mono
default	16:55:28.121795-0400	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Output render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	16:55:28.121968-0400	Nexy	                AUHAL.cpp:1677  UpdateStreamFormats: 
  input stream 0 [0x5c]:  1 ch,  24000 Hz, Float32
default	16:55:28.122009-0400	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 1 input streams; all mono
default	16:55:28.122018-0400	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Input render format:  1 ch,  24000 Hz, Float32
default	16:55:28.122178-0400	Nexy	                AUHAL.cpp:1771  UpdateStreamFormats: AUHAL(0xa5f0bea40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	16:55:28.122215-0400	Nexy	                AUHAL.cpp:1777  UpdateStreamFormats: AUHAL(0xa5f0bea40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	16:55:28.122239-0400	Nexy	                AUHAL.cpp:1787  UpdateStreamFormats: <-
default	16:55:28.122246-0400	Nexy	                AUHAL.cpp:895   SelectDevice: (0xa5f0bea40) removing 7 device listeners from device 85
default	16:55:28.122529-0400	Nexy	                AUHAL.cpp:895   SelectDevice: (0xa5f0bea40) removing 0 device delegate listeners from device 85
default	16:55:28.122559-0400	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0xa5f0bea40)
default	16:55:28.123446-0400	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	16:55:28.124512-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=401.4113, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=20663, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	16:55:28.125286-0400	tccd	AUTHREQ_SUBJECT: msgID=401.4113, subject=com.nexy.assistant,
default	16:55:28.125803-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x969135800 at /Applications/Nexy.app
default	16:55:28.143579-0400	Nexy	       ACv2Workarounds.mm:51    com.nexy.assistant: fix84702776_86723525_86479548_89800354_SinglePacketDesc: false
default	16:55:28.143647-0400	Nexy	       AudioConverter.cpp:1042  Created a new in process converter -> 0xa5d0267c0, from  1 ch,  24000 Hz, Float32 to  1 ch,  16000 Hz, Float32
default	16:55:28.143872-0400	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	16:55:28.144850-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=401.4114, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=20663, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	16:55:28.145631-0400	tccd	AUTHREQ_SUBJECT: msgID=401.4114, subject=com.nexy.assistant,
default	16:55:28.146152-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x969135800 at /Applications/Nexy.app
default	16:55:28.159655-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=401.4115, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=20663, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	16:55:28.160427-0400	tccd	AUTHREQ_SUBJECT: msgID=401.4115, subject=com.nexy.assistant,
default	16:55:28.160947-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x969135800 at /Applications/Nexy.app
default	16:55:28.176646-0400	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Input {1C-77-54-18-C8-A3:input, 0xb}
default	16:55:28.178910-0400	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ef0c0","name":"Nexy(20663)"}, "details":{"deviceUIDs":["1C-77-54-18-C8-A3:input"],"implicit_category":"Record","input_running":true,"output_running":false} }
default	16:55:28.178978-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 193, PID = 20663, Name = sid:0x1ef0c0, Nexy(20663), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	16:55:28.179001-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Category/Mode changed -- The score for sid:0x1ef0c0, Nexy(20663), 'prim'/com.nexy.assistant was not correct. Old score = 201
default	16:55:28.179025-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 193, PID = 20663, Name = sid:0x1ef0c0, Nexy(20663), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	16:55:28.179166-0400	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.19166461.19166467(501)>:20663] from originator [osservice<com.apple.powerd>:334] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:398-334-500228 target:20663 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	16:55:28.179069-0400	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1ef0c0, Nexy(20663), 'prim'', AudioCategory changed to 'Record_WithBluetooth'
default	16:55:28.179234-0400	runningboardd	Assertion 398-334-500228 (target:[app<application.com.nexy.assistant.19166461.19166467(501)>:20663]) will be created as active
default	16:55:28.179224-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 193, PID = 20663, Name = sid:0x1ef0c0, Nexy(20663), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	16:55:28.179307-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 193, PID = 20663, Name = sid:0x1ef0c0, Nexy(20663), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	16:55:28.179420-0400	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 193, PID = 20663, Name = sid:0x1ef0c0, Nexy(20663), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> is going active
default	16:55:28.179455-0400	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1ef0c0, Nexy(20663), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 193 starting recording
default	16:55:28.179714-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 193, PID = 20663, Name = sid:0x1ef0c0, Nexy(20663), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	16:55:28.179817-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 193, PID = 20663, Name = sid:0x1ef0c0, Nexy(20663), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	16:55:28.179661-0400	runningboardd	[app<application.com.nexy.assistant.19166461.19166467(501)>:20663] Ignoring jetsam update because this process is not memory-managed
default	16:55:28.180120-0400	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	16:55:28.179908-0400	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1ef0c0, Nexy(20663), 'prim'', displayID:'com.nexy.assistant'}
default	16:55:28.179958-0400	runningboardd	[app<application.com.nexy.assistant.19166461.19166467(501)>:20663] Ignoring suspend because this process is not lifecycle managed
default	16:55:28.180154-0400	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	16:55:28.179744-0400	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	16:55:28.180053-0400	runningboardd	[app<application.com.nexy.assistant.19166461.19166467(501)>:20663] Set darwin role to: Background
default	16:55:28.180115-0400	runningboardd	[app<application.com.nexy.assistant.19166461.19166467(501)>:20663] Ignoring GPU update because this process is not GPU managed
default	16:55:28.180207-0400	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	16:55:28.180078-0400	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	16:55:28.180169-0400	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	16:55:28.180198-0400	runningboardd	[app<application.com.nexy.assistant.19166461.19166467(501)>:20663] Ignoring memory limit update because this process is not memory-managed
default	16:55:28.180248-0400	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	16:55:28.180461-0400	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 200 flag 0x1 < Hijack > app com.nexy.assistant CID 0xD310001 category Not set
default	16:55:28.180696-0400	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [1, 0]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:input"
)}
default	16:55:28.180702-0400	audiomxd	UpdateAudioState CID 0xD310001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	16:55:28.180777-0400	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	16:55:28.180802-0400	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	16:55:28.180815-0400	audioaccessoryd	AudioStateChanged: Added audio session app com.nexy.assistant NULL -> 200 count 1
default	16:55:28.180825-0400	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
error	16:55:28.180833-0400	audioaccessoryd	Updating local audio category 100 -> 200 app com.nexy.assistant
error	16:55:28.180871-0400	audioaccessoryd	Relaying via 24B92680-715A-E821-B5AF-358E78C2DAF9 inWxAddress 1C:77:54:18:C8:A3 to 88:20:0D:45:06:51 with options {
    "playingApp" : "com.nexy.assistant",
    "hostStreamingState" : "YES",
    "btAddress" : "A0:9A:8E:0D:58:86",
    "btName" : "Mac",
    "otherDeviceAudioCategory" : 200,
}
default	16:55:28.180917-0400	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	16:55:28.180763-0400	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	16:55:28.184046-0400	runningboardd	Calculated state for app<application.com.nexy.assistant.19166461.19166467(501)>: running-active (role: Background) (endowments: (null))
default	16:55:28.184381-0400	gamepolicyd	Received state update for 20663 (app<application.com.nexy.assistant.19166461.19166467(501)>, running-active-NotVisible
default	16:55:28.186688-0400	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	16:55:28.186734-0400	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	16:55:28.186784-0400	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	16:55:28.187195-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	16:55:28.187207-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	16:55:28.187233-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	16:55:28.187266-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	16:55:28.187309-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	16:55:28.187333-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	16:55:28.187354-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	16:55:28.187380-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	16:55:28.187444-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	16:55:28.187470-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	16:55:28.187537-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	16:55:28.187582-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	16:55:28.187773-0400	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	16:55:28.187844-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	16:55:28.187853-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	16:55:28.187881-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	16:55:28.187922-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	16:55:28.187982-0400	ControlCenter	Navigating to new application [com.nexy.assistant]
default	16:55:28.187974-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	16:55:28.188018-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	16:55:29.515719-0400	audioaccessoryd	AudioStateSnapshot: Route:Bluetooth App com.nexy.assistant, Score 200, Remote 100NumofApp 1
default	16:55:32.514897-0400	audioaccessoryd	AudioStateSnapshot: Route:Bluetooth App com.nexy.assistant, Score 200, Remote 100NumofApp 1
default	16:55:35.274333-0400	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xb}
default	16:55:35.274883-0400	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ef0c0","name":"Nexy(20663)"}, "details":{"deviceUIDs":[],"implicit_category":"","input_running":false,"output_running":false} }
default	16:55:35.275139-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 193, PID = 20663, Name = sid:0x1ef0c0, Nexy(20663), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	16:55:35.275255-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 193, PID = 20663, Name = sid:0x1ef0c0, Nexy(20663), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	16:55:35.275322-0400	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1ef0c0, Nexy(20663), 'prim'', displayID:'com.nexy.assistant'}
default	16:55:35.275432-0400	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	16:55:35.275441-0400	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1ef0c0, Nexy(20663), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 193 stopping recording
default	16:55:35.275497-0400	audiomxd	-MXCoreSession- -[MXCoreSession endInterruption:]: Session <ID: 193, PID = 20663, Name = sid:0x1ef0c0, Nexy(20663), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> is going inactive
default	16:55:35.275561-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 193, PID = 20663, Name = sid:0x1ef0c0, Nexy(20663), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	16:55:35.275634-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 193, PID = 20663, Name = sid:0x1ef0c0, Nexy(20663), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	16:55:35.275876-0400	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 0]. BT device UIDS: {(
)}
default	16:55:35.275902-0400	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	16:55:35.275938-0400	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 200 flag 0x1 < Hijack > app com.nexy.assistant CID 0xD310001 category Not set
default	16:55:35.276412-0400	audiomxd	UpdateAudioState CID 0xD310001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	16:55:35.276499-0400	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	16:55:35.276602-0400	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	16:55:35.276669-0400	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	16:55:35.276705-0400	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	16:55:35.276750-0400	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	16:55:35.276866-0400	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	16:55:35.276884-0400	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	16:55:35.276899-0400	audioaccessoryd	AudioStateChanged: Removed audio session app com.nexy.assistant 201 count 0
default	16:55:35.279627-0400	runningboardd	Invalidating assertion 398-334-500228 (target:[app<application.com.nexy.assistant.19166461.19166467(501)>:20663]) from originator [osservice<com.apple.powerd>:334]
default	16:55:35.284130-0400	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	16:55:35.285985-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	16:55:35.286009-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	16:55:35.286024-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	16:55:35.286032-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	16:55:35.286041-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	16:55:35.286050-0400	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	16:55:35.286170-0400	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	16:55:35.382230-0400	runningboardd	[app<application.com.nexy.assistant.19166461.19166467(501)>:20663] Ignoring jetsam update because this process is not memory-managed
default	16:55:35.382260-0400	runningboardd	[app<application.com.nexy.assistant.19166461.19166467(501)>:20663] Ignoring suspend because this process is not lifecycle managed
default	16:55:35.382338-0400	runningboardd	[app<application.com.nexy.assistant.19166461.19166467(501)>:20663] Set darwin role to: None
default	16:55:35.382366-0400	runningboardd	[app<application.com.nexy.assistant.19166461.19166467(501)>:20663] Ignoring GPU update because this process is not GPU managed
default	16:55:35.382412-0400	runningboardd	[app<application.com.nexy.assistant.19166461.19166467(501)>:20663] Ignoring memory limit update because this process is not memory-managed
default	16:55:35.387650-0400	runningboardd	Calculated state for app<application.com.nexy.assistant.19166461.19166467(501)>: running-suspended (role: None) (endowments: (null))
default	16:55:35.388267-0400	gamepolicyd	Received state update for 20663 (app<application.com.nexy.assistant.19166461.19166467(501)>, running-suspended-NotVisible
default	16:55:35.456754-0400	Nexy	                AUHAL.cpp:473   ~AUHAL: (0xa5f0bea40) Selecting device 0 from destructor
default	16:55:35.456785-0400	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0xa5f0bea40)
default	16:55:35.456800-0400	Nexy	                AUHAL.cpp:676   SelectDevice: (0xa5f0bea40) not already running
default	16:55:35.456814-0400	Nexy	                AUHAL.cpp:682   SelectDevice: (0xa5f0bea40) disconnecting device 91
default	16:55:35.456829-0400	Nexy	                AUHAL.cpp:746   SelectDevice: (0xa5f0bea40) destroying ioproc 0xb for device 91
default	16:55:35.456890-0400	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xb}
default	16:55:35.456955-0400	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	16:55:35.457282-0400	Nexy	                AUHAL.cpp:848   SelectDevice: (0xa5f0bea40) nothing to setup
default	16:55:35.457313-0400	Nexy	                AUHAL.cpp:858   SelectDevice: (0xa5f0bea40) adding 0 device listeners to device 0
default	16:55:35.457329-0400	Nexy	                AUHAL.cpp:858   SelectDevice: (0xa5f0bea40) adding 0 device delegate listeners to device 0
default	16:55:35.457345-0400	Nexy	                AUHAL.cpp:895   SelectDevice: (0xa5f0bea40) removing 7 device listeners from device 91
default	16:55:35.457878-0400	Nexy	                AUHAL.cpp:895   SelectDevice: (0xa5f0bea40) removing 0 device delegate listeners from device 91
default	16:55:35.457914-0400	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0xa5f0bea40)
default	16:55:35.475961-0400	Nexy	[0xa5e0e8500] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	16:55:35.477164-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=20663.2, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=20663, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	16:55:35.479473-0400	tccd	AUTHREQ_SUBJECT: msgID=20663.2, subject=com.nexy.assistant,
default	16:55:35.480447-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117600 at /Applications/Nexy.app
default	16:55:35.503002-0400	Nexy	[0xa5e0e8500] invalidated after the last release of the connection object
default	16:55:35.504394-0400	Nexy	[0xa5e0e8500] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	16:55:35.505026-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=20663.3, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=20663, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	16:55:35.506191-0400	tccd	AUTHREQ_SUBJECT: msgID=20663.3, subject=com.nexy.assistant,
default	16:55:35.506812-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117600 at /Applications/Nexy.app
default	16:55:35.519850-0400	Nexy	[0xa5e0e8500] invalidated after the last release of the connection object
default	16:55:35.520083-0400	Nexy	[0xa5e0e8500] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	16:55:35.520611-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=20663.4, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=20663, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	16:55:35.521601-0400	tccd	AUTHREQ_SUBJECT: msgID=20663.4, subject=com.nexy.assistant,
default	16:55:35.522198-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117600 at /Applications/Nexy.app
default	16:55:35.535144-0400	tccd	Notifying for access  kTCCServiceScreenCapture for target PID[20663], responsiblePID[20663], responsiblePath: /Applications/Nexy.app to UID: 501
default	16:55:35.535386-0400	Nexy	[0xa5e0e8500] invalidated after the last release of the connection object
default	16:55:35.623796-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d114300 at /Applications/Nexy.app
default	16:55:35.654809-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117600 at /Applications/Nexy.app
default	16:55:35.660681-0400	tccd	Publishing <TCCDEvent: type=Modify, service=kTCCServiceScreenCapture, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 0 subscribers: {
}
default	16:55:35.665313-0400	nehelper	Received an apps uninstalled notification with bundle IDs (
    "com.nexy.assistant"
)
default	16:55:35.665498-0400	nehelper	Received an apps uninstalled notification with bundle IDs (
    "com.nexy.assistant"
)
default	16:55:36.262624-0400	nehelper	Removing UUIDs for (
    "com.nexy.assistant"
)
default	16:55:36.268865-0400	nehelper	Handling an apps uninstalled notification with bundle IDs (
    "com.nexy.assistant"
)
default	16:55:36.288501-0400	nehelper	com.apple.preferences.networkprivacy-F67B3EA9-90A6-470B-B321-9BBD719C692B: Populating the cache with 1 UUID(s) for com.nexy.assistant
default	16:55:37.500215-0400	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(28258)
default	16:55:37.500245-0400	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:28258 called from <private>
default	16:55:37.500263-0400	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:28258 called from <private>
default	16:55:37.503812-0400	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(28259)
default	16:55:37.503905-0400	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:28259 called from <private>
default	16:55:37.503916-0400	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:28259 called from <private>
default	16:55:37.532908-0400	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:28258 called from <private>
default	16:55:37.532973-0400	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:28258 called from <private>
default	16:55:37.532998-0400	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(28259)
default	16:55:37.568351-0400	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:28258 called from <private>
default	16:55:37.568552-0400	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:28258 called from <private>
default	16:55:37.568759-0400	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:28258 called from <private>
default	16:55:37.568803-0400	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:28258 called from <private>
default	16:55:37.569041-0400	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(28258)
default	16:55:37.569282-0400	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(28258)
default	16:55:37.569494-0400	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:28258 called from <private>
default	16:55:37.569581-0400	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:28258 called from <private>
default	16:55:37.569669-0400	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(28258)
default	16:55:37.573055-0400	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:28258 called from <private>
default	16:55:37.573102-0400	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:28258 called from <private>
default	16:55:42.683934-0400	Nexy	[0xa5e0e88c0] activating connection: mach=true listener=false peer=false name=com.apple.analyticsd
default	16:55:42.771563-0400	Nexy	[0xa5e0e8a00] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
error	16:55:42.772273-0400	tccd	TCCDProcess: identifier=com.nexy.assistant, pid=20663, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy attempted to call TCCAccessRequest for kTCCServiceAccessibility without the recommended com.apple.private.tcc.manager.check-by-audit-token entitlement
default	16:55:42.772483-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=20663.5, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=20663, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.nexy.assistant, pid=20663, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	16:55:42.774059-0400	tccd	AUTHREQ_SUBJECT: msgID=20663.5, subject=com.nexy.assistant,
default	16:55:42.774998-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d116100 at /Applications/Nexy.app
default	16:55:42.792547-0400	Nexy	[0xa5e0e8a00] invalidated after the last release of the connection object
default	16:55:42.793406-0400	Nexy	[0xa5e0e8a00] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
error	16:55:42.793926-0400	tccd	TCCDProcess: identifier=com.nexy.assistant, pid=20663, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy attempted to call TCCAccessRequest for kTCCServiceAccessibility without the recommended com.apple.private.tcc.manager.check-by-audit-token entitlement
default	16:55:42.794193-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=20663.6, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=20663, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.nexy.assistant, pid=20663, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	16:55:42.795365-0400	tccd	AUTHREQ_SUBJECT: msgID=20663.6, subject=com.nexy.assistant,
default	16:55:42.796371-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d116100 at /Applications/Nexy.app
default	16:55:42.811887-0400	Nexy	[0xa5e0e8a00] invalidated after the last release of the connection object
default	16:55:42.811956-0400	Nexy	[0xa5e0e8a00] activating connection: mach=true listener=false peer=false name=com.apple.universalaccessAuthWarn
default	16:55:42.812058-0400	Nexy	[0xa5e0e8a00] invalidated after the last release of the connection object
default	16:55:42.812484-0400	Nexy	[0xa5e0e8b40] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	16:55:42.813009-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=20663.7, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=20663, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	16:55:42.814050-0400	tccd	AUTHREQ_SUBJECT: msgID=20663.7, subject=com.nexy.assistant,
default	16:55:42.814740-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d116100 at /Applications/Nexy.app
default	16:55:42.828615-0400	tccd	Notifying for access  kTCCServiceListenEvent for target PID[20663], responsiblePID[20663], responsiblePath: /Applications/Nexy.app to UID: 501
default	16:55:42.828790-0400	Nexy	[0xa5e0e8b40] invalidated after the last release of the connection object
default	16:55:42.829083-0400	Nexy	server port 0x0000f823, session port 0x0000bd43
default	16:55:42.830070-0400	tccd	AUTHREQ_ATTRIBUTION: msgID=393.6910, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=20663, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=393, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	16:55:42.830094-0400	tccd	requestor: TCCDProcess: identifier=com.apple.WindowServer, pid=393, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=20663, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	16:55:42.831279-0400	tccd	AUTHREQ_SUBJECT: msgID=393.6910, subject=com.nexy.assistant,
default	16:55:42.832480-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117600 at /Applications/Nexy.app
default	16:55:42.843841-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d116a00 at /Applications/Nexy.app
default	16:55:42.866151-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d116100 at /Applications/Nexy.app
default	16:55:42.871063-0400	tccd	Publishing <TCCDEvent: type=Modify, service=kTCCServiceAccessibility, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 0 subscribers: {
}
default	16:55:42.924952-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d114600 at /Applications/Nexy.app
default	16:55:43.090748-0400	tccd	AUTHREQ_SUBJECT: msgID=393.6914, subject=com.nexy.assistant,
default	16:55:43.110328-0400	kernel	SK[7]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 537197DE-0ECD-467F-8CB3-D5E44F15A66B flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.61848,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0xd126b336 tp_proto=0x06"
default	16:55:43.138760-0400	Nexy	nw_path_libinfo_path_check [92003C20-254C-45D9-8348-0D59524CD8FB IPv4#3d72ccf6:8081 tcp, legacy-socket, attribution: developer]
	libinfo check path: <private>
default	16:55:43.144620-0400	kernel	tcp connected: [<IPv4-redacted>:61849<-><IPv4-redacted>:53] interface: en0 (skipped: 1087)
so_gencnt: 2603761 t_state: ESTABLISHED process: Nexy:20663 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 13 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xa1c9f466
default	16:55:43.145102-0400	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:61849<-><IPv4-redacted>:53] interface: en0 (skipped: 1087)
so_gencnt: 2603761 t_state: FIN_WAIT_1 process: Nexy:20663 Duration: 0.014 sec Conn_Time: 0.013 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 13.000 ms rttvar: 6.500 ms base rtt: 13 ms so_error: 0 svc/tc: 0 flow: 0xa1c9f466
default	16:55:43.145112-0400	kernel	tcp_connection_summary [<IPv4-redacted>:61849<-><IPv4-redacted>:53] interface: en0 (skipped: 1087)
so_gencnt: 2603761 t_state: FIN_WAIT_1 process: Nexy:20663 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	16:55:43.150612-0400	Nexy	New connection 0x14c3e3 main
default	16:55:43.150862-0400	Nexy	[0xa5e0e8c80] activating connection: mach=true listener=false peer=false name=com.apple.pasteboard.1
default	16:55:43.166219-0400	Nexy	[0xa5e0e8f00] activating connection: mach=true listener=false peer=false name=com.apple.lsd.mapdb
default	16:55:43.195424-0400	Nexy	nw_path_libinfo_path_check [D3541A84-9396-4572-8C04-84F5B73C4AD6 Hostname#d2541e69:443 tcp, legacy-socket, attribution: developer]
	libinfo check path: <private>
default	16:55:43.195616-0400	mDNSResponder	[R310905] DNSServiceCreateConnection START PID[20663](Nexy)
default	16:55:43.216609-0400	kernel	SK[6]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid F3E68A45-7288-439E-82FE-5772E643E3A0 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.61851,dst=<IPv4-redacted>.443,proto=0x06 mask=0x0000003f,hash=0x7f9358f3 tp_proto=0x06"
default	16:55:43.216733-0400	kernel	tcp connect outgoing: [<IPv4-redacted>:61851<-><IPv4-redacted>:443] interface: en0 (skipped: 1087)
so_gencnt: 2603774 t_state: SYN_SENT process: Nexy:20663 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xac1bea30
default	16:55:43.246155-0400	kernel	tcp connected: [<IPv4-redacted>:61851<-><IPv4-redacted>:443] interface: en0 (skipped: 1087)
so_gencnt: 2603774 t_state: ESTABLISHED process: Nexy:20663 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xac1bea30
default	16:55:43.429371-0400	Nexy	nw_path_libinfo_path_check [9A8E4FCA-E24E-48E1-9418-61AC124C5BDD Hostname#bb84451f:443 tcp, legacy-socket, attribution: developer]
	libinfo check path: <private>
default	16:55:43.429594-0400	mDNSResponder	[R310908] DNSServiceQueryRecord START -- qname: <mask.hash: '2M6q9I8vyy1ql8eChmIyow=='>, qtype: A, flags: 0x1D000, interface index: 0, client pid: 20663 (Nexy), name hash: c6742fa2
default	16:55:43.430586-0400	mDNSResponder	[R310909] DNSServiceQueryRecord START -- qname: <mask.hash: '2M6q9I8vyy1ql8eChmIyow=='>, qtype: AAAA, flags: 0x1D000, interface index: 0, client pid: 20663 (Nexy), name hash: c6742fa2
default	16:55:43.486265-0400	kernel	SK[1]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid D6645D26-F75F-4749-9CEC-7DAC2B3817E9 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.61852,dst=<IPv4-redacted>.443,proto=0x06 mask=0x0000003f,hash=0x78d9885b tp_proto=0x06"
default	16:55:43.486412-0400	kernel	tcp connect outgoing: [<IPv4-redacted>:61852<-><IPv4-redacted>:443] interface: en0 (skipped: 1087)
so_gencnt: 2603789 t_state: SYN_SENT process: Nexy:20663 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xb54389d5
default	16:55:43.499284-0400	kernel	tcp connected: [<IPv4-redacted>:61852<-><IPv4-redacted>:443] interface: en0 (skipped: 1087)
so_gencnt: 2603789 t_state: ESTABLISHED process: Nexy:20663 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xb54389d5
default	16:55:44.259542-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117300 at /Applications/Nexy.app
default	16:55:44.296303-0400	tccd	Publishing <TCCDEvent: type=Modify, service=kTCCServiceScreenCapture, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 0 subscribers: {
}
default	16:55:44.704567-0400	kernel	udp connect: [<IPv4-redacted>:63101<-><IPv4-redacted>:50051] interface:  (skipped: 634)
so_gencnt: 2603814 so_state: 0x0002 process: Nexy:20663 bytes in/out: 0/0 pkts in/out: 0/0 error: 0 so_error: 0 svc/tc: 0 flow: 0xaf81a114
default	16:55:44.704581-0400	kernel	udp_connection_summary [<IPv4-redacted>:63101<-><IPv4-redacted>:50051] interface:  (skipped: 634)
so_gencnt: 2603814 so_state: 0x0002 process: Nexy:20663 Duration: 0.000 sec Conn_Time: 0.000 sec bytes in/out: 0/0 pkts in/out: 0/0 rxnospace pkts/bytes: 0/0 so_error: 0 svc/tc: 0 flow: 0xaf81a114 flowctl: 0us (0x)
default	16:55:44.706192-0400	kernel	SK[5]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid E0C5273B-905F-4399-844E-FB3596522F63 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.61854,dst=<IPv4-redacted>.50051,proto=0x06 mask=0x0000003f,hash=0x40d6cb67 tp_proto=0x06"
default	16:55:44.706248-0400	kernel	tcp connect outgoing: [<IPv4-redacted>:61854<-><IPv4-redacted>:50051] interface: en0 (skipped: 1087)
so_gencnt: 2603816 t_state: SYN_SENT process: Nexy:20663 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 22 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x86307ad6
default	16:55:44.735094-0400	kernel	tcp connected: [<IPv4-redacted>:61854<-><IPv4-redacted>:50051] interface: en0 (skipped: 1087)
so_gencnt: 2603816 t_state: ESTABLISHED process: Nexy:20663 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 22 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x86307ad6
default	16:55:46.501182-0400	Nexy	                AUHAL.cpp:420   AUHAL: (0xa5d09e340) Selecting device 85 from constructor
default	16:55:46.501204-0400	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0xa5d09e340)
default	16:55:46.501210-0400	Nexy	                AUHAL.cpp:676   SelectDevice: (0xa5d09e340) not already running
default	16:55:46.501216-0400	Nexy	                AUHAL.cpp:752   SelectDevice: (0xa5d09e340) nothing to teardown
default	16:55:46.501221-0400	Nexy	                AUHAL.cpp:757   SelectDevice: (0xa5d09e340) connecting device 85
default	16:55:46.501398-0400	Nexy	                AUHAL.cpp:3413  IsDeviceUsable: (0xa5d09e340) Device ID: 85 (Input:No | Output:Yes): true
default	16:55:46.504281-0400	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	16:55:46.516138-0400	Nexy	                AUHAL.cpp:848   SelectDevice: (0xa5d09e340) nothing to setup
default	16:55:46.516151-0400	Nexy	                AUHAL.cpp:858   SelectDevice: (0xa5d09e340) adding 0 device listeners to device 0
default	16:55:46.516156-0400	Nexy	                AUHAL.cpp:858   SelectDevice: (0xa5d09e340) adding 0 device delegate listeners to device 0
default	16:55:46.516164-0400	Nexy	                AUHAL.cpp:895   SelectDevice: (0xa5d09e340) removing 7 device listeners from device 85
default	16:55:46.516474-0400	Nexy	                AUHAL.cpp:895   SelectDevice: (0xa5d09e340) removing 0 device delegate listeners from device 85
default	16:55:46.516484-0400	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0xa5d09e340)
default	16:55:46.517533-0400	Nexy	                AUHAL.cpp:420   AUHAL: (0xa5d09e340) Selecting device 85 from constructor
default	16:55:46.517540-0400	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0xa5d09e340)
default	16:55:46.517544-0400	Nexy	                AUHAL.cpp:676   SelectDevice: (0xa5d09e340) not already running
default	16:55:46.517868-0400	Nexy	                AUHAL.cpp:752   SelectDevice: (0xa5d09e340) nothing to teardown
default	16:55:46.517960-0400	Nexy	                AUHAL.cpp:757   SelectDevice: (0xa5d09e340) connecting device 85
default	16:55:46.518162-0400	Nexy	                AUHAL.cpp:3413  IsDeviceUsable: (0xa5d09e340) Device ID: 85 (Input:No | Output:Yes): true
default	16:55:46.523711-0400	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.19166461.19166467(501)>:20663] from originator [osservice<com.apple.powerd>:334] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:398-334-500339 target:20663 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	16:55:46.523806-0400	runningboardd	Assertion 398-334-500339 (target:[app<application.com.nexy.assistant.19166461.19166467(501)>:20663]) will be created as active
default	16:55:46.559859-0400	runningboardd	[app<application.com.nexy.assistant.19166461.19166467(501)>:20663] Ignoring jetsam update because this process is not memory-managed
default	16:55:46.559876-0400	runningboardd	[app<application.com.nexy.assistant.19166461.19166467(501)>:20663] Ignoring suspend because this process is not lifecycle managed
default	16:55:46.559968-0400	runningboardd	[app<application.com.nexy.assistant.19166461.19166467(501)>:20663] Set darwin role to: Background
default	16:55:46.559987-0400	runningboardd	[app<application.com.nexy.assistant.19166461.19166467(501)>:20663] Ignoring GPU update because this process is not GPU managed
default	16:55:46.560030-0400	runningboardd	[app<application.com.nexy.assistant.19166461.19166467(501)>:20663] Ignoring memory limit update because this process is not memory-managed
default	16:55:46.565572-0400	gamepolicyd	Received state update for 20663 (app<application.com.nexy.assistant.19166461.19166467(501)>, running-active-NotVisible
default	16:55:46.854027-0400	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xd}
default	16:55:46.854996-0400	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ef0c0","name":"Nexy(20663)"}, "details":{"deviceUIDs":["1C-77-54-18-C8-A3:output"],"implicit_category":"MediaPlayback","input_running":false,"output_running":true} }
default	16:55:46.855139-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 193, PID = 20663, Name = sid:0x1ef0c0, Nexy(20663), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	16:55:46.855190-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Category/Mode changed -- The score for sid:0x1ef0c0, Nexy(20663), 'prim'/com.nexy.assistant was not correct. Old score = 201
default	16:55:46.855225-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 193, PID = 20663, Name = sid:0x1ef0c0, Nexy(20663), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	16:55:46.855276-0400	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1ef0c0, Nexy(20663), 'prim'', AudioCategory changed to 'MediaPlayback'
default	16:55:46.855307-0400	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	16:55:46.855336-0400	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 193, PID = 20663, Name = sid:0x1ef0c0, Nexy(20663), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO> is going active
default	16:55:46.855354-0400	audiomxd	-MXCoreSession- -[MXCoreSession updateIsPlaying:]: MXCoreSession com.nexy.assistant with category/mode MediaPlayback/Default and coreSessionID = 193 starting playing
default	16:55:46.855427-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 193, PID = 20663, Name = sid:0x1ef0c0, Nexy(20663), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	16:55:46.855458-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 193, PID = 20663, Name = sid:0x1ef0c0, Nexy(20663), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO>
default	16:55:46.855484-0400	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1ef0c0, Nexy(20663), 'prim'', displayID:'com.nexy.assistant'}
default	16:55:46.855506-0400	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Will try to see if we can get the shared route for session = <ID: 193, PID = 20663, Name = sid:0x1ef0c0, Nexy(20663), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO>. Old (200) and New (201) scores.
default	16:55:46.855499-0400	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	16:55:46.855559-0400	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	16:55:46.855540-0400	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 201, deviceID = <private>
default	16:55:46.855575-0400	audiomxd	AudioApplicationInfoImpl.mm:395   Successfully updated session 0x1ef0c0 to isSessionRecording: 0
	app: {"name":"[implicit] Nexy","pid":20663}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1ef0c0, sessionType: 'prim', isRecording: false }, 
]
default	16:55:46.855730-0400	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 201 flag 0x1 < Hijack > app com.nexy.assistant CID 0xD310001 category Not set
default	16:55:46.855755-0400	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 1]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)}
default	16:55:46.855768-0400	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	16:55:46.855942-0400	audiomxd	UpdateAudioState CID 0xD310001 audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	16:55:46.856024-0400	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 201,
}
default	16:55:46.856056-0400	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	16:55:46.856072-0400	audioaccessoryd	AudioStateChanged: Added audio session app com.nexy.assistant NULL -> 201 count 1
default	16:55:46.856084-0400	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 201
error	16:55:46.856095-0400	audioaccessoryd	Updating local audio category 100 -> 201 app com.nexy.assistant
error	16:55:46.856151-0400	audioaccessoryd	Relaying via 24B92680-715A-E821-B5AF-358E78C2DAF9 inWxAddress 1C:77:54:18:C8:A3 to 88:20:0D:45:06:51 with options {
    "playingApp" : "com.nexy.assistant",
    "hostStreamingState" : "YES",
    "btAddress" : "A0:9A:8E:0D:58:86",
    "btName" : "Mac",
    "otherDeviceAudioCategory" : 201,
}
default	16:55:46.856218-0400	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.nexy.assistant
default	16:55:47.495840-0400	audioaccessoryd	AudioStateSnapshot: Route:Bluetooth App com.nexy.assistant, Score 201, Remote 100NumofApp 1
error	16:55:47.712882-0400	Nexy	         HALC_ProxyIOContext.cpp:1623  HALC_ProxyIOContext::IOWorkLoop: skipping cycle due to overload
error	16:55:49.936548-0400	Nexy	         HALC_ProxyIOContext.cpp:1623  HALC_ProxyIOContext::IOWorkLoop: skipping cycle due to overload
error	16:55:50.055685-0400	Nexy	         HALC_ProxyIOContext.cpp:1623  HALC_ProxyIOContext::IOWorkLoop: skipping cycle due to overload
error	16:55:51.154630-0400	Nexy	         HALC_ProxyIOContext.cpp:1623  HALC_ProxyIOContext::IOWorkLoop: skipping cycle due to overload
default	16:55:51.703568-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d114000 at /Applications/Nexy.app
default	16:55:51.719710-0400	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117c00 at /Applications/Nexy.app
default	16:55:51.730340-0400	tccd	Publishing <TCCDEvent: type=Modify, service=kTCCServiceListenEvent, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 0 subscribers: {
}
error	16:55:52.331007-0400	Nexy	         HALC_ProxyIOContext.cpp:1623  HALC_ProxyIOContext::IOWorkLoop: skipping cycle due to overload
error	16:55:52.429902-0400	Nexy	         HALC_ProxyIOContext.cpp:1623  HALC_ProxyIOContext::IOWorkLoop: skipping cycle due to overload
error	16:55:52.736954-0400	Nexy	         HALC_ProxyIOContext.cpp:1623  HALC_ProxyIOContext::IOWorkLoop: skipping cycle due to overload
default	16:55:53.514461-0400	audioaccessoryd	AudioStateSnapshot: Route:Bluetooth App com.nexy.assistant, Score 201, Remote 100NumofApp 1
default	16:55:56.501529-0400	audioaccessoryd	AudioStateSnapshot: Route:Bluetooth App com.nexy.assistant, Score 201, Remote 100NumofApp 1
error	16:55:57.644180-0400	Nexy	         HALC_ProxyIOContext.cpp:1623  HALC_ProxyIOContext::IOWorkLoop: skipping cycle due to overload
default	16:55:59.068532-0400	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Output {1C-77-54-18-C8-A3:output, 0xd}
default	16:55:59.069538-0400	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ef0c0","name":"Nexy(20663)"}, "details":{"deviceUIDs":[],"implicit_category":"","input_running":false,"output_running":false} }
default	16:55:59.069776-0400	audiomxd	-MXCoreSession- -[MXCoreSession updateIsPlaying:]: MXCoreSession com.nexy.assistant with category/mode MediaPlayback/Default and coreSessionID = 193 stopping playing
default	16:55:59.069880-0400	audiomxd	-MXCoreSession- -[MXCoreSession endInterruption:]: Session <ID: 193, PID = 20663, Name = sid:0x1ef0c0, Nexy(20663), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> is going inactive
default	16:55:59.069961-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 193, PID = 20663, Name = sid:0x1ef0c0, Nexy(20663), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	16:55:59.070100-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 193, PID = 20663, Name = sid:0x1ef0c0, Nexy(20663), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	16:55:59.070245-0400	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	16:55:59.070332-0400	audiomxd	AudioApplicationInfoImpl.mm:395   Successfully updated session 0x1ef0c0 to isSessionRecording: 0
	app: {"name":"[implicit] Nexy","pid":20663}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1ef0c0, sessionType: 'prim', isRecording: false }, 
]
default	16:55:59.070501-0400	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 0]. BT device UIDS: {(
)}
default	16:55:59.070522-0400	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	16:55:59.070554-0400	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	16:55:59.070610-0400	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	16:55:59.070647-0400	audioaccessoryd	AudioStateChanged: Removed audio session app com.nexy.assistant 201 count 0
default	16:55:59.077529-0400	runningboardd	Invalidating assertion 398-334-500339 (target:[app<application.com.nexy.assistant.19166461.19166467(501)>:20663]) from originator [osservice<com.apple.powerd>:334]
default	16:55:59.179224-0400	runningboardd	[app<application.com.nexy.assistant.19166461.19166467(501)>:20663] Ignoring jetsam update because this process is not memory-managed
default	16:55:59.179244-0400	runningboardd	[app<application.com.nexy.assistant.19166461.19166467(501)>:20663] Ignoring suspend because this process is not lifecycle managed
default	16:55:59.179356-0400	runningboardd	[app<application.com.nexy.assistant.19166461.19166467(501)>:20663] Set darwin role to: None
default	16:55:59.179373-0400	runningboardd	[app<application.com.nexy.assistant.19166461.19166467(501)>:20663] Ignoring GPU update because this process is not GPU managed
default	16:55:59.179402-0400	runningboardd	[app<application.com.nexy.assistant.19166461.19166467(501)>:20663] Ignoring memory limit update because this process is not memory-managed
default	16:55:59.184102-0400	runningboardd	Calculated state for app<application.com.nexy.assistant.19166461.19166467(501)>: running-suspended (role: None) (endowments: (null))
default	16:55:59.184751-0400	gamepolicyd	Received state update for 20663 (app<application.com.nexy.assistant.19166461.19166467(501)>, running-suspended-NotVisible
default	16:56:13.147762-0400	kernel	SK[3]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid F1E42B01-7835-46F6-9F2A-EB3247CE3B60 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.61870,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0x3ea0673b tp_proto=0x06"
default	16:56:13.147845-0400	kernel	tcp connect outgoing: [<IPv4-redacted>:61870<-><IPv4-redacted>:53] interface: en0 (skipped: 1087)
so_gencnt: 2604116 t_state: SYN_SENT process: Nexy:20663 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 13 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x88c04cc7
default	16:56:13.160615-0400	kernel	tcp connected: [<IPv4-redacted>:61870<-><IPv4-redacted>:53] interface: en0 (skipped: 1087)
so_gencnt: 2604116 t_state: ESTABLISHED process: Nexy:20663 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 13 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x88c04cc7
default	16:56:13.161292-0400	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:61870<-><IPv4-redacted>:53] interface: en0 (skipped: 1087)
so_gencnt: 2604116 t_state: FIN_WAIT_1 process: Nexy:20663 Duration: 0.014 sec Conn_Time: 0.013 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 13.000 ms rttvar: 6.500 ms base rtt: 13 ms so_error: 0 svc/tc: 0 flow: 0x88c04cc7
default	16:56:13.161314-0400	kernel	tcp_connection_summary [<IPv4-redacted>:61870<-><IPv4-redacted>:53] interface: en0 (skipped: 1087)
so_gencnt: 2604116 t_state: FIN_WAIT_1 process: Nexy:20663 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	16:56:13.161859-0400	kernel	SK[4]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 09DEF92C-6511-4C51-9497-4938BAB29900 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.61871,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0x62c06e92 tp_proto=0x06"
default	16:56:13.161906-0400	kernel	tcp connect outgoing: [<IPv4-redacted>:61871<-><IPv4-redacted>:53] interface: en0 (skipped: 1087)
so_gencnt: 2604117 t_state: SYN_SENT process: Nexy:20663 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 13 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x8e28b65b
default	16:56:13.175888-0400	kernel	tcp connected: [<IPv4-redacted>:61871<-><IPv4-redacted>:53] interface: en0 (skipped: 1087)
so_gencnt: 2604117 t_state: ESTABLISHED process: Nexy:20663 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 13 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x8e28b65b
default	16:56:13.176271-0400	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:61871<-><IPv4-redacted>:53] interface: en0 (skipped: 1087)
so_gencnt: 2604117 t_state: FIN_WAIT_1 process: Nexy:20663 Duration: 0.015 sec Conn_Time: 0.014 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 14.000 ms rttvar: 7.000 ms base rtt: 13 ms so_error: 0 svc/tc: 0 flow: 0x8e28b65b
default	16:56:13.176292-0400	kernel	tcp_connection_summary [<IPv4-redacted>:61871<-><IPv4-redacted>:53] interface: en0 (skipped: 1087)
so_gencnt: 2604117 t_state: FIN_WAIT_1 process: Nexy:20663 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	16:56:27.948671-0400	loginwindow	-[ApplicationManager(AppDeathHandler) _appQuitTimer:] | _appQuitTimer fired for: ASN: 11082385, name: Nexy with url: file:///Applications/Nexy.app/
default	16:56:27.949125-0400	loginwindow	-[ApplicationManager(AppDeathHandler) _handleLingeringSubordinateProcesses:forApp:] | Last instance of app Nexy at /Applications/Nexy.app, handle lingering spawns.
default	16:56:27.949157-0400	loginwindow	-[ApplicationManager(AppDeathHandler) _handleLingeringSubordinateProcesses:forApp:] | Child applications for Nexy : (
)
default	16:56:27.949184-0400	loginwindow	-[ApplicationManager(AppDeathHandler) _handleLingeringSubordinateProcesses:forApp:] | App Nexy is fully cleaned up.  No user notification is necessary.  Done with handling.
default	16:56:43.178416-0400	kernel	SK[0]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid ECA121F8-EE57-4218-8E3C-147C5162EDCB flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.61878,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0xfc90f71c tp_proto=0x06"
default	16:56:43.178491-0400	kernel	tcp connect outgoing: [<IPv4-redacted>:61878<-><IPv4-redacted>:53] interface: en0 (skipped: 1087)
so_gencnt: 2604226 t_state: SYN_SENT process: Nexy:20663 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 13 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xbcd3b9a5
default	16:56:43.191240-0400	kernel	tcp connected: [<IPv4-redacted>:61878<-><IPv4-redacted>:53] interface: en0 (skipped: 1087)
so_gencnt: 2604226 t_state: ESTABLISHED process: Nexy:20663 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 13 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xbcd3b9a5
default	16:56:43.191834-0400	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:61878<-><IPv4-redacted>:53] interface: en0 (skipped: 1087)
so_gencnt: 2604226 t_state: FIN_WAIT_1 process: Nexy:20663 Duration: 0.013 sec Conn_Time: 0.013 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 13.000 ms rttvar: 6.500 ms base rtt: 13 ms so_error: 0 svc/tc: 0 flow: 0xbcd3b9a5
default	16:56:43.191855-0400	kernel	tcp_connection_summary [<IPv4-redacted>:61878<-><IPv4-redacted>:53] interface: en0 (skipped: 1087)
so_gencnt: 2604226 t_state: FIN_WAIT_1 process: Nexy:20663 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	16:56:43.192384-0400	kernel	SK[3]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 867D283C-2E29-41C2-A892-7656A0D81040 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.61879,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0x2061239e tp_proto=0x06"
default	16:56:43.192439-0400	kernel	tcp connect outgoing: [<IPv4-redacted>:61879<-><IPv4-redacted>:53] interface: en0 (skipped: 1087)
so_gencnt: 2604227 t_state: SYN_SENT process: Nexy:20663 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 13 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xac424736
default	16:56:43.214224-0400	kernel	tcp connected: [<IPv4-redacted>:61879<-><IPv4-redacted>:53] interface: en0 (skipped: 1087)
so_gencnt: 2604227 t_state: ESTABLISHED process: Nexy:20663 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 13 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xac424736
default	16:56:43.214638-0400	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:61879<-><IPv4-redacted>:53] interface: en0 (skipped: 1087)
so_gencnt: 2604227 t_state: FIN_WAIT_1 process: Nexy:20663 Duration: 0.022 sec Conn_Time: 0.022 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 22.000 ms rttvar: 11.000 ms base rtt: 13 ms so_error: 0 svc/tc: 0 flow: 0xac424736
default	16:56:43.214662-0400	kernel	tcp_connection_summary [<IPv4-redacted>:61879<-><IPv4-redacted>:53] interface: en0 (skipped: 1087)
so_gencnt: 2604227 t_state: FIN_WAIT_1 process: Nexy:20663 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	16:56:47.238682-0400	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.19166461.19166467(501)>:20663] from originator [osservice<com.apple.powerd>:334] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:398-334-500431 target:20663 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	16:56:47.238858-0400	runningboardd	Assertion 398-334-500431 (target:[app<application.com.nexy.assistant.19166461.19166467(501)>:20663]) will be created as active
default	16:56:47.240272-0400	runningboardd	[app<application.com.nexy.assistant.19166461.19166467(501)>:20663] Ignoring jetsam update because this process is not memory-managed
default	16:56:47.240348-0400	runningboardd	[app<application.com.nexy.assistant.19166461.19166467(501)>:20663] Ignoring suspend because this process is not lifecycle managed
default	16:56:47.240525-0400	runningboardd	[app<application.com.nexy.assistant.19166461.19166467(501)>:20663] Set darwin role to: Background
default	16:56:47.240649-0400	runningboardd	[app<application.com.nexy.assistant.19166461.19166467(501)>:20663] Ignoring GPU update because this process is not GPU managed
default	16:56:47.240756-0400	runningboardd	[app<application.com.nexy.assistant.19166461.19166467(501)>:20663] Ignoring memory limit update because this process is not memory-managed
default	16:56:47.247068-0400	runningboardd	Calculated state for app<application.com.nexy.assistant.19166461.19166467(501)>: running-active (role: Background) (endowments: (null))
default	16:56:47.247801-0400	gamepolicyd	Received state update for 20663 (app<application.com.nexy.assistant.19166461.19166467(501)>, running-active-NotVisible
default	16:56:47.758352-0400	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xd}
default	16:56:47.759228-0400	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ef0c0","name":"Nexy(20663)"}, "details":{"deviceUIDs":["1C-77-54-18-C8-A3:output"],"implicit_category":"MediaPlayback","input_running":false,"output_running":true} }
default	16:56:47.759383-0400	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 193, PID = 20663, Name = sid:0x1ef0c0, Nexy(20663), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO> is going active
default	16:56:47.759402-0400	audiomxd	-MXCoreSession- -[MXCoreSession updateIsPlaying:]: MXCoreSession com.nexy.assistant with category/mode MediaPlayback/Default and coreSessionID = 193 starting playing
default	16:56:47.759490-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 193, PID = 20663, Name = sid:0x1ef0c0, Nexy(20663), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	16:56:47.759540-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 193, PID = 20663, Name = sid:0x1ef0c0, Nexy(20663), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO>
default	16:56:47.759565-0400	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1ef0c0, Nexy(20663), 'prim'', displayID:'com.nexy.assistant'}
default	16:56:47.759607-0400	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 201, deviceID = <private>
default	16:56:47.759635-0400	audiomxd	AudioApplicationInfoImpl.mm:395   Successfully updated session 0x1ef0c0 to isSessionRecording: 0
	app: {"name":"[implicit] Nexy","pid":20663}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1ef0c0, sessionType: 'prim', isRecording: false }, 
]
default	16:56:47.759695-0400	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 1]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)}
default	16:56:47.759708-0400	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	16:56:47.759850-0400	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 201 flag 0x1 < Hijack > app com.nexy.assistant CID 0xD310001 category Not set
default	16:56:47.760045-0400	audiomxd	UpdateAudioState CID 0xD310001 audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	16:56:47.760138-0400	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 201,
}
default	16:56:47.760165-0400	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	16:56:47.760178-0400	audioaccessoryd	AudioStateChanged: Added audio session app com.nexy.assistant NULL -> 201 count 1
default	16:56:47.760186-0400	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 201
error	16:56:47.760198-0400	audioaccessoryd	Updating local audio category 100 -> 201 app com.nexy.assistant
error	16:56:47.760252-0400	audioaccessoryd	Relaying via 24B92680-715A-E821-B5AF-358E78C2DAF9 inWxAddress 1C:77:54:18:C8:A3 to 88:20:0D:45:06:51 with options {
    "playingApp" : "com.nexy.assistant",
    "hostStreamingState" : "YES",
    "btAddress" : "A0:9A:8E:0D:58:86",
    "btName" : "Mac",
    "otherDeviceAudioCategory" : 201,
}
default	16:56:47.760318-0400	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.nexy.assistant
default	16:56:50.512427-0400	audioaccessoryd	AudioStateSnapshot: Route:Bluetooth App com.nexy.assistant, Score 201, Remote 100NumofApp 1
error	16:56:52.635613-0400	Nexy	         HALC_ProxyIOContext.cpp:1623  HALC_ProxyIOContext::IOWorkLoop: skipping cycle due to overload
default	16:56:53.504020-0400	audioaccessoryd	AudioStateSnapshot: Route:Bluetooth App com.nexy.assistant, Score 201, Remote 100NumofApp 1
default	16:56:56.512469-0400	audioaccessoryd	AudioStateSnapshot: Route:Bluetooth App com.nexy.assistant, Score 201, Remote 100NumofApp 1
error	16:56:57.639558-0400	Nexy	         HALC_ProxyIOContext.cpp:1623  HALC_ProxyIOContext::IOWorkLoop: skipping cycle due to overload
default	16:56:57.839621-0400	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Output {1C-77-54-18-C8-A3:output, 0xd}
default	16:56:57.840204-0400	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ef0c0","name":"Nexy(20663)"}, "details":{"deviceUIDs":[],"implicit_category":"","input_running":false,"output_running":false} }
default	16:56:57.840358-0400	audiomxd	-MXCoreSession- -[MXCoreSession updateIsPlaying:]: MXCoreSession com.nexy.assistant with category/mode MediaPlayback/Default and coreSessionID = 193 stopping playing
default	16:56:57.840450-0400	audiomxd	-MXCoreSession- -[MXCoreSession endInterruption:]: Session <ID: 193, PID = 20663, Name = sid:0x1ef0c0, Nexy(20663), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> is going inactive
default	16:56:57.840528-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 193, PID = 20663, Name = sid:0x1ef0c0, Nexy(20663), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	16:56:57.840646-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 193, PID = 20663, Name = sid:0x1ef0c0, Nexy(20663), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	16:56:57.840780-0400	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	16:56:57.840874-0400	audiomxd	AudioApplicationInfoImpl.mm:395   Successfully updated session 0x1ef0c0 to isSessionRecording: 0
	app: {"name":"[implicit] Nexy","pid":20663}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1ef0c0, sessionType: 'prim', isRecording: false }, 
]
default	16:56:57.841034-0400	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	16:56:57.841142-0400	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	16:56:57.841171-0400	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 0]. BT device UIDS: {(
)}
default	16:56:57.841190-0400	audioaccessoryd	AudioStateChanged: Removed audio session app com.nexy.assistant 201 count 0
default	16:56:57.841201-0400	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	16:56:57.847090-0400	runningboardd	Invalidating assertion 398-334-500431 (target:[app<application.com.nexy.assistant.19166461.19166467(501)>:20663]) from originator [osservice<com.apple.powerd>:334]
default	16:56:57.953160-0400	runningboardd	[app<application.com.nexy.assistant.19166461.19166467(501)>:20663] Ignoring jetsam update because this process is not memory-managed
default	16:56:57.953186-0400	runningboardd	[app<application.com.nexy.assistant.19166461.19166467(501)>:20663] Ignoring suspend because this process is not lifecycle managed
default	16:56:57.953284-0400	runningboardd	[app<application.com.nexy.assistant.19166461.19166467(501)>:20663] Set darwin role to: None
default	16:56:57.953305-0400	runningboardd	[app<application.com.nexy.assistant.19166461.19166467(501)>:20663] Ignoring GPU update because this process is not GPU managed
default	16:56:57.953342-0400	runningboardd	[app<application.com.nexy.assistant.19166461.19166467(501)>:20663] Ignoring memory limit update because this process is not memory-managed
default	16:56:57.958060-0400	runningboardd	Calculated state for app<application.com.nexy.assistant.19166461.19166467(501)>: running-suspended (role: None) (endowments: (null))
default	16:56:57.958895-0400	gamepolicyd	Received state update for 20663 (app<application.com.nexy.assistant.19166461.19166467(501)>, running-suspended-NotVisible
default	16:57:13.216650-0400	kernel	SK[2]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 0E3F88E4-D553-4C84-83F2-6321D18ED530 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.61885,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0x162cfe69 tp_proto=0x06"
default	16:57:13.216746-0400	kernel	tcp connect outgoing: [<IPv4-redacted>:61885<-><IPv4-redacted>:53] interface: en0 (skipped: 1087)
so_gencnt: 2604273 t_state: SYN_SENT process: Nexy:20663 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 13 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x9d7a39ed
default	16:57:13.231503-0400	kernel	tcp connected: [<IPv4-redacted>:61885<-><IPv4-redacted>:53] interface: en0 (skipped: 1087)
so_gencnt: 2604273 t_state: ESTABLISHED process: Nexy:20663 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 13 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x9d7a39ed
default	16:57:13.232270-0400	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:61885<-><IPv4-redacted>:53] interface: en0 (skipped: 1087)
so_gencnt: 2604273 t_state: FIN_WAIT_1 process: Nexy:20663 Duration: 0.016 sec Conn_Time: 0.015 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 15.000 ms rttvar: 7.500 ms base rtt: 13 ms so_error: 0 svc/tc: 0 flow: 0x9d7a39ed
default	16:57:13.232296-0400	kernel	tcp_connection_summary [<IPv4-redacted>:61885<-><IPv4-redacted>:53] interface: en0 (skipped: 1087)
so_gencnt: 2604273 t_state: FIN_WAIT_1 process: Nexy:20663 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	16:57:13.232893-0400	kernel	SK[3]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 6B96E0CB-9FB3-497E-BEF1-A3C6E4765654 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.61886,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0xb536e744 tp_proto=0x06"
default	16:57:13.232953-0400	kernel	tcp connect outgoing: [<IPv4-redacted>:61886<-><IPv4-redacted>:53] interface: en0 (skipped: 1087)
so_gencnt: 2604274 t_state: SYN_SENT process: Nexy:20663 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 13 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x85a3934a
default	16:57:13.252180-0400	kernel	tcp connected: [<IPv4-redacted>:61886<-><IPv4-redacted>:53] interface: en0 (skipped: 1087)
so_gencnt: 2604274 t_state: ESTABLISHED process: Nexy:20663 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 13 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x85a3934a
default	16:57:13.252671-0400	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:61886<-><IPv4-redacted>:53] interface: en0 (skipped: 1087)
so_gencnt: 2604274 t_state: FIN_WAIT_1 process: Nexy:20663 Duration: 0.020 sec Conn_Time: 0.019 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 19.000 ms rttvar: 9.500 ms base rtt: 13 ms so_error: 0 svc/tc: 0 flow: 0x85a3934a
default	16:57:13.252684-0400	kernel	tcp_connection_summary [<IPv4-redacted>:61886<-><IPv4-redacted>:53] interface: en0 (skipped: 1087)
so_gencnt: 2604274 t_state: FIN_WAIT_1 process: Nexy:20663 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	16:57:43.254493-0400	kernel	SK[2]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid EF8A2A7E-8D39-4157-9C74-F4E70ABB7DD0 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.61902,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0xf9a7d590 tp_proto=0x06"
default	16:57:43.254555-0400	kernel	tcp connect outgoing: [<IPv4-redacted>:61902<-><IPv4-redacted>:53] interface: en0 (skipped: 1087)
so_gencnt: 2604499 t_state: SYN_SENT process: Nexy:20663 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 13 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x9e87a4c7
default	16:57:43.276221-0400	kernel	tcp connected: [<IPv4-redacted>:61902<-><IPv4-redacted>:53] interface: en0 (skipped: 1087)
so_gencnt: 2604499 t_state: ESTABLISHED process: Nexy:20663 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 13 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x9e87a4c7
default	16:57:43.276956-0400	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:61902<-><IPv4-redacted>:53] interface: en0 (skipped: 1087)
so_gencnt: 2604499 t_state: FIN_WAIT_1 process: Nexy:20663 Duration: 0.022 sec Conn_Time: 0.021 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 21.000 ms rttvar: 10.500 ms base rtt: 13 ms so_error: 0 svc/tc: 0 flow: 0x9e87a4c7
default	16:57:43.276978-0400	kernel	tcp_connection_summary [<IPv4-redacted>:61902<-><IPv4-redacted>:53] interface: en0 (skipped: 1087)
so_gencnt: 2604499 t_state: FIN_WAIT_1 process: Nexy:20663 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	16:57:43.277522-0400	kernel	SK[2]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 0CD53DC2-A667-4ABA-A9D4-4CB024CDD1E9 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.61903,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0x68375c51 tp_proto=0x06"
default	16:57:43.277565-0400	kernel	tcp connect outgoing: [<IPv4-redacted>:61903<-><IPv4-redacted>:53] interface: en0 (skipped: 1087)
so_gencnt: 2604500 t_state: SYN_SENT process: Nexy:20663 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 13 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x98744faa
default	16:57:43.291743-0400	kernel	tcp connected: [<IPv4-redacted>:61903<-><IPv4-redacted>:53] interface: en0 (skipped: 1087)
so_gencnt: 2604500 t_state: ESTABLISHED process: Nexy:20663 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 12 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x98744faa
default	16:57:43.292148-0400	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:61903<-><IPv4-redacted>:53] interface: en0 (skipped: 1087)
so_gencnt: 2604500 t_state: FIN_WAIT_1 process: Nexy:20663 Duration: 0.014 sec Conn_Time: 0.014 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 14.000 ms rttvar: 7.000 ms base rtt: 12 ms so_error: 0 svc/tc: 0 flow: 0x98744faa
default	16:57:43.292167-0400	kernel	tcp_connection_summary [<IPv4-redacted>:61903<-><IPv4-redacted>:53] interface: en0 (skipped: 1087)
so_gencnt: 2604500 t_state: FIN_WAIT_1 process: Nexy:20663 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	16:58:01.555162-0400	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:61852<-><IPv4-redacted>:443] interface: en0 (skipped: 1087)
so_gencnt: 2603789 t_state: FIN_WAIT_1 process: Nexy:20663 Duration: 138.068 sec Conn_Time: 0.013 sec bytes in/out: 97544667/2619 pkts in/out: 15076/4 pkt rxmit: 0 ooo pkts: 2182 dup bytes in: 0 ACKs delayed: 10303 delayed ACKs sent: 0
rtt: 12.656 ms rttvar: 3.375 ms base rtt: 11 ms so_error: 0 svc/tc: 0 flow: 0xb54389d5
default	16:58:01.555186-0400	kernel	tcp_connection_summary [<IPv4-redacted>:61852<-><IPv4-redacted>:443] interface: en0 (skipped: 1087)
so_gencnt: 2603789 t_state: FIN_WAIT_1 process: Nexy:20663 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	16:58:01.559288-0400	kernel	tcp_connection_summary (tcp_drop:1348)[<IPv4-redacted>:61851<-><IPv4-redacted>:443] interface: en0 (skipped: 1087)
so_gencnt: 2603774 t_state: CLOSED process: Nexy:20663 Duration: 138.342 sec Conn_Time: 0.030 sec bytes in/out: 8749/1774 pkts in/out: 5/4 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 36.281 ms rttvar: 19.687 ms base rtt: 28 ms so_error: 0 svc/tc: 0 flow: 0xac1bea30
default	16:58:01.559305-0400	kernel	tcp_connection_summary [<IPv4-redacted>:61851<-><IPv4-redacted>:443] interface: en0 (skipped: 1087)
so_gencnt: 2603774 t_state: CLOSED process: Nexy:20663 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 1/0 RST in/out: 0/1 AccECN (client/server): Disabled/Disabled
default	16:58:01.560738-0400	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:61850<-><IPv4-redacted>:8081] interface: en0 (skipped: 1087)
so_gencnt: 2603762 t_state: FIN_WAIT_1 process: Nexy:20663 Duration: 138.418 sec Conn_Time: 0.022 sec bytes in/out: 1369/116 pkts in/out: 1/1 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 22.000 ms rttvar: 8.250 ms base rtt: 21 ms so_error: 0 svc/tc: 0 flow: 0xb5254ee6
default	16:58:01.560753-0400	kernel	tcp_connection_summary [<IPv4-redacted>:61850<-><IPv4-redacted>:8081] interface: en0 (skipped: 1087)
so_gencnt: 2603762 t_state: FIN_WAIT_1 process: Nexy:20663 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	16:58:01.561939-0400	Nexy	                AUHAL.cpp:473   ~AUHAL: (0xa5d09e340) Selecting device 0 from destructor
default	16:58:01.561989-0400	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0xa5d09e340)
default	16:58:01.562001-0400	Nexy	                AUHAL.cpp:676   SelectDevice: (0xa5d09e340) not already running
default	16:58:01.562011-0400	Nexy	                AUHAL.cpp:682   SelectDevice: (0xa5d09e340) disconnecting device 85
default	16:58:01.562024-0400	Nexy	                AUHAL.cpp:746   SelectDevice: (0xa5d09e340) destroying ioproc 0xd for device 85
default	16:58:01.562071-0400	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Output {1C-77-54-18-C8-A3:output, 0xd}
default	16:58:01.562124-0400	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	16:58:01.562354-0400	Nexy	                AUHAL.cpp:848   SelectDevice: (0xa5d09e340) nothing to setup
default	16:58:01.562378-0400	Nexy	                AUHAL.cpp:858   SelectDevice: (0xa5d09e340) adding 0 device listeners to device 0
default	16:58:01.562396-0400	Nexy	                AUHAL.cpp:858   SelectDevice: (0xa5d09e340) adding 0 device delegate listeners to device 0
default	16:58:01.562407-0400	Nexy	                AUHAL.cpp:895   SelectDevice: (0xa5d09e340) removing 7 device listeners from device 85
default	16:58:01.562834-0400	Nexy	                AUHAL.cpp:895   SelectDevice: (0xa5d09e340) removing 0 device delegate listeners from device 85
default	16:58:01.562860-0400	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0xa5d09e340)
default	16:58:01.717317-0400	Nexy	Entering exit handler.
default	16:58:01.717391-0400	Nexy	Queueing exit procedure onto XPC queue. Any further messages sent will be discarded. activeSendTransactions=0
default	16:58:01.717477-0400	Nexy	Cancelling XPC connection. Any further reply handler invocations will not retry messages
default	16:58:01.717492-0400	Nexy	[0xa5e0e88c0] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	16:58:01.717510-0400	Nexy	Exiting exit handler.
default	16:58:01.717560-0400	Nexy	XPC connection invalidated (daemon unloaded/disabled)
default	16:58:01.722698-0400	audiomxd	  ServerSessionManager.mm:472   { "action":"destroy_session", "session":{"ID":"0x1ef0c0","name":"Nexy(20663)"}, "details":null }
default	16:58:01.722731-0400	audiomxd	AudioApplicationInfoImpl.mm:690   Successfully removed session 0x1ef0c0 from AudioApp, recording state unchanged (app: {"name":"[implicit] Nexy","pid":20663})
default	16:58:01.722747-0400	audiomxd	  ServerSessionManager.mm:1081  destroy audio app instance since was created implicitly by session creation and all sessions now gone (audio app: {"name":"[implicit] Nexy","pid":20663})
default	16:58:01.724770-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 193, PID = 20663, Name = sid:0x1ef0c0, Nexy(20663), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	16:58:01.725218-0400	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 193, PID = 20663, Name = sid:0x1ef0c0, Nexy(20663), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	16:58:01.726526-0400	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	16:58:01.726634-0400	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	16:58:01.726037-0400	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	16:58:01.726423-0400	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	16:58:01.732228-0400	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:61854<-><IPv4-redacted>:50051] interface: en0 (skipped: 1087)
so_gencnt: 2603816 t_state: FIN_WAIT_1 process: Nexy:20663 Duration: 137.025 sec Conn_Time: 0.029 sec bytes in/out: 1865951/1021 pkts in/out: 410/16 pkt rxmit: 1 ooo pkts: 108 dup bytes in: 0 ACKs delayed: 96 delayed ACKs sent: 0
rtt: 75.750 ms rttvar: 87.250 ms base rtt: 21 ms so_error: 0 svc/tc: 0 flow: 0x86307ad6
default	16:58:01.732249-0400	kernel	tcp_connection_summary [<IPv4-redacted>:61854<-><IPv4-redacted>:50051] interface: en0 (skipped: 1087)
so_gencnt: 2603816 t_state: FIN_WAIT_1 process: Nexy:20663 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	16:58:01.732459-0400	mDNSResponder	[R310905] DNSServiceCreateConnection STOP PID[20663](Nexy)
default	16:58:01.734797-0400	runningboardd	[app<application.com.nexy.assistant.19166461.19166467(501)>:20663] termination reported by launchd (0, 0, 0)
default	16:58:01.734853-0400	runningboardd	Removing process: [app<application.com.nexy.assistant.19166461.19166467(501)>:20663]
default	16:58:01.735142-0400	runningboardd	Removing launch job for: [app<application.com.nexy.assistant.19166461.19166467(501)>:20663]
default	16:58:01.735394-0400	runningboardd	Removed job for [app<application.com.nexy.assistant.19166461.19166467(501)>:20663]
default	16:58:01.735423-0400	runningboardd	Removing assertions for terminated process: [app<application.com.nexy.assistant.19166461.19166467(501)>:20663]
default	16:58:01.735945-0400	runningboardd	Calculated state for app<application.com.nexy.assistant.19166461.19166467(501)>: none (role: None) (endowments: (null))
default	16:58:01.736032-0400	audiomxd	  ServerSessionManager.mm:1322  Monitored process died, pid = 20663, name = Nexy
default	16:58:01.737226-0400	launchservicesd	Hit the server for a process handle 18bde185000050b7 that resolved to: [app<application.com.nexy.assistant.19166461.19166467(501)>:20663]
default	16:58:01.737497-0400	gamepolicyd	Received state update for 20663 (app<application.com.nexy.assistant.19166461.19166467(501)>, none-NotVisible
default	16:58:01.737778-0400	coreaudiod	>>> NEGOTIATE [com.nexy.assistant]
default	16:58:01.738003-0400	coreaudiod	<<< NEGOTIATE [com.nexy.assistant]
default	16:58:01.739518-0400	coreaudiod	IssueReporting.cpp:492   RTAID [ use_case=Generic report_type=RMS Generic Chain clientID=ADM node=ADM::com.nexy.assistant_28259.28176.0_airpods noise suppression studio::out-0 issue_detected_sample_time=192960.000000 ] -- [ rms:[-40.131344], peaks:[-18.090284] ]
default	16:58:01.739540-0400	coreaudiod	IssueReporting.cpp:492   RTAID [ use_case=Generic report_type=RMS Generic Chain clientID=ADM node=ADM::com.nexy.assistant_28259.28176.0_airpods noise suppression studio::in-0 issue_detected_sample_time=0.000000 ] -- [ rms:[-38.031281], peaks:[-17.004322] ]
default	16:58:01.742677-0400	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	16:58:01.742770-0400	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}