default	11:27:24.972445-0500	lsd	com.nexy.assistant/Unknown Persona:5:4:2:1:_LSServerRegisterItemInfo result = 0
default	11:27:24.979402-0500	runningboardd	Launch request for app<application.com.nexy.assistant.21576034.21576040(501)>[0] is using uid 501 (divined from auid 501 euid 501)
default	11:27:24.979468-0500	runningboardd	Acquiring assertion targeting app<application.com.nexy.assistant.21576034.21576040(501)> from originator [osservice<com.apple.coreservices.uiagent(501)>:61646] with description <RBSAssertionDescriptor| "LS launch com.nexy.assistant" ID:397-61646-135380 target:app<application.com.nexy.assistant.21576034.21576040(501)> attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"LaunchRoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	11:27:24.979536-0500	runningboardd	Assertion 397-61646-135380 (target:app<application.com.nexy.assistant.21576034.21576040(501)>) will be created as active
default	11:27:25.013205-0500	gamepolicyd	Hit the server for a process handle 358f5a100000ac9 that resolved to: [app<application.com.nexy.assistant.21576034.21576040(501)>:2761]
default	11:27:25.013243-0500	gamepolicyd	Received state update for 2761 (app<application.com.nexy.assistant.21576034.21576040(501)>, running-active-NotVisible
default	11:27:25.017906-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.21576034.21576040(501)>:2761] from originator [osservice<com.apple.coreservices.launchservicesd>:361] with description <RBSAssertionDescriptor| "uielement:2761" ID:397-361-135382 target:2761 attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"RoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	11:27:25.021270-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.21576034.21576040(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	11:27:25.021544-0500	runningboardd	Invalidating assertion 397-61646-135380 (target:app<application.com.nexy.assistant.21576034.21576040(501)>) from originator [osservice<com.apple.coreservices.uiagent(501)>:61646]
default	11:27:25.021584-0500	runningboardd	[app<application.com.nexy.assistant.21576034.21576040(501)>:2761] Ignoring jetsam update because this process is not memory-managed
default	11:27:25.021596-0500	runningboardd	[app<application.com.nexy.assistant.21576034.21576040(501)>:2761] Ignoring suspend because this process is not lifecycle managed
default	11:27:25.021692-0500	gamepolicyd	Received state update for 2761 (app<application.com.nexy.assistant.21576034.21576040(501)>, running-active-NotVisible
default	11:27:25.021608-0500	runningboardd	[app<application.com.nexy.assistant.21576034.21576040(501)>:2761] Ignoring GPU update because this process is not GPU managed
default	11:27:25.021713-0500	runningboardd	[app<application.com.nexy.assistant.21576034.21576040(501)>:2761] Ignoring memory limit update because this process is not memory-managed
default	11:27:25.024818-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.21576034.21576040(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	11:27:25.123277-0500	runningboardd	[app<application.com.nexy.assistant.21576034.21576040(501)>:2761] Ignoring jetsam update because this process is not memory-managed
default	11:27:25.123296-0500	runningboardd	[app<application.com.nexy.assistant.21576034.21576040(501)>:2761] Ignoring suspend because this process is not lifecycle managed
default	11:27:25.123311-0500	runningboardd	[app<application.com.nexy.assistant.21576034.21576040(501)>:2761] Ignoring GPU update because this process is not GPU managed
default	11:27:25.123346-0500	runningboardd	[app<application.com.nexy.assistant.21576034.21576040(501)>:2761] Ignoring memory limit update because this process is not memory-managed
default	11:27:25.199202-0500	syspolicyd	GK evaluateScanResult: 3, PST: (path: a2cffff67b96be6e), (team: 5NKLL2CLB9), (id: com.nexy.assistant), (bundle_id: (null)), 0, 0, 1, 0, 9, 4, 1
default	11:27:25.201128-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=460.24, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=2761, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.syspolicyd, pid=460, auid=0, euid=0, binary_path=/usr/libexec/syspolicyd}, },
default	11:27:25.210048-0500	tccd	AUTHREQ_SUBJECT: msgID=460.24, subject=com.nexy.assistant,
default	11:27:25.210869-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa5f977c00 at /Applications/Nexy.app
default	11:27:25.404941-0500	Nexy	[0x1063387a0] activating connection: mach=true listener=false peer=false name=com.apple.cfprefsd.daemon
default	11:27:25.405109-0500	Nexy	[0x106338d10] activating connection: mach=true listener=false peer=false name=com.apple.cfprefsd.agent
error	11:27:25.721256-0500	Nexy	dlsym cannot find symbol NSMakeRect in CFBundle 0xa56620000 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	11:27:25.721527-0500	Nexy	dlsym cannot find symbol NSMakePoint in CFBundle 0xa56620000 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	11:27:25.721769-0500	Nexy	dlsym cannot find symbol NSMakeSize in CFBundle 0xa56620000 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	11:27:25.722032-0500	Nexy	dlsym cannot find symbol NSMakeRange in CFBundle 0xa56620000 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
default	11:27:25.723360-0500	Nexy	[0x1063422e0] activating connection: mach=true listener=false peer=false name=com.apple.coreservices.launchservicesd
default	11:27:25.724034-0500	Nexy	[0xa576c8000] activating connection: mach=true listener=false peer=false name=com.apple.analyticsd
default	11:27:25.724368-0500	Nexy	[0xa576c8140] activating connection: mach=true listener=false peer=false name=com.apple.pasteboard.1
default	11:27:25.724787-0500	Nexy	[0xa576c8280] activating connection: mach=true listener=false peer=false name=com.apple.distributed_notifications@Uv3
default	11:27:25.730272-0500	tccd	AUTHREQ_SUBJECT: msgID=2761.1, subject=com.nexy.assistant,
default	11:27:25.748739-0500	Nexy	[0xa576c83c0] invalidated after the last release of the connection object
default	11:27:25.748987-0500	Nexy	server port 0x0000360b, session port 0x0000360b
default	11:27:25.750022-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=391.2189, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=2761, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=391, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	11:27:25.750055-0500	tccd	requestor: TCCDProcess: identifier=com.apple.WindowServer, pid=391, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=2761, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	11:27:25.751239-0500	tccd	AUTHREQ_SUBJECT: msgID=391.2189, subject=com.nexy.assistant,
default	11:27:25.752131-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa5f976a00 at /Applications/Nexy.app
default	11:27:25.773869-0500	Nexy	New connection 0xed8ab main
default	11:27:25.787025-0500	Nexy	[0xa576c83c0] activating connection: mach=false listener=true peer=false name=(anonymous)
default	11:27:25.787034-0500	Nexy	[0xa576c83c0] Connection returned listener port: 0x4f03
default	11:27:25.787581-0500	loginwindow	-[Application updateInformation] | Got App URL: file:///Applications/Nexy.app/
default	11:27:25.787390-0500	runningboardd	Invalidating assertion 397-361-135382 (target:[app<application.com.nexy.assistant.21576034.21576040(501)>:2761]) from originator [osservice<com.apple.coreservices.launchservicesd>:361]
default	11:27:25.787190-0500	Nexy	[0xa56660300] activating connection: mach=false listener=false peer=true name=com.apple.xpc.anonymous.0xa576c83c0.peer[361].0xa56660300
default	11:27:25.787692-0500	loginwindow	-[ApplicationManager checkInAppContext:eventData:] | ApplicationManager: Checked in app : Nexy
default	11:27:25.788472-0500	Nexy	FRONTLOGGING: version 1
default	11:27:25.788506-0500	Nexy	Registered, pid=2761 ASN=0x0,0x3f83f8
default	11:27:25.788734-0500	WindowServer	ed8ab[CreateApplication]: Process creation: 0x0-0x3f83f8 (Nexy) connectionID: ED8AB pid: 2761 in session 0x101
default	11:27:25.792139-0500	Nexy	No persisted cache on this platform.
default	11:27:25.793360-0500	Nexy	Current system appearance, (HLTB: 1), (SLS: 0)
default	11:27:25.795795-0500	Nexy	FBSWorkspace: endpoint monitoring is disabled.
default	11:27:25.795806-0500	Nexy	FBSWorkspace: default shell endpoint is disabled.
default	11:27:25.795854-0500	Nexy	Initializing connection
default	11:27:25.795892-0500	Nexy	Removing all cached process handles
default	11:27:25.795918-0500	Nexy	Sending handshake request attempt #1 to server
default	11:27:25.795928-0500	Nexy	Creating connection to com.apple.runningboard
default	11:27:25.795937-0500	Nexy	[0xa576c8640] activating connection: mach=true listener=false peer=false name=com.apple.runningboard
default	11:27:25.796343-0500	Nexy	[0xa576c83c0] Connection returned listener port: 0x4f03
default	11:27:25.796385-0500	runningboardd	Setting client for [app<application.com.nexy.assistant.21576034.21576040(501)>:2761] as ready
default	11:27:25.797074-0500	Nexy	Handshake succeeded
default	11:27:25.797092-0500	Nexy	Identity resolved as app<application.com.nexy.assistant.21576034.21576040(501)>
default	11:27:25.797246-0500	distnoted	register name: com.apple.xctest.FakeForceTouchDevice object: com.nexy.assistant token: 1e0000001d pid: 2761
default	11:27:25.800426-0500	Nexy	[0xa576c83c0] Connection returned listener port: 0x4f03
default	11:27:25.803901-0500	Nexy	Created a new Process Instance Registry XPC connection (inactive)
default	11:27:25.803925-0500	Nexy	[0xa576c8780] activating connection: mach=true listener=false peer=false name=com.apple.linkd.autoShortcut
default	11:27:25.804016-0500	Nexy	Activated connection to com.apple.linkd.autoShortcut (ApplicationService)
default	11:27:25.804065-0500	Nexy	[0xa576c8a00] activating connection: mach=false listener=true peer=false name=(anonymous)
default	11:27:26.029881-0500	Nexy	Registered notify signal com.apple.caulk.alloc.rtdump (0)
default	11:27:26.034792-0500	Nexy	System_Input_Processing_Notification_Handler.mm:456   System_Input_Processing_Notification_Handler::is_vi_available(): Voice isolation DSP is available for client with bundle id com.nexy.assistant (AVFoundation is available, application is not in client deny list, application is not FaceTime variant)
default	11:27:26.039197-0500	Nexy	[0xa576c8b40] activating connection: mach=true listener=false peer=false name=com.apple.cmio.registerassistantservice.system-extensions
fault	11:27:26.043560-0500	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.21576034.21576040 AUID=501> and <type=Application identifier=application.com.nexy.assistant.21576034.21576040>
default	11:27:26.047796-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOInitializeListenersForBundleID: for <private> -> <private>
default	11:27:26.049717-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> vpio_preferenceChangedListener: new value ((null)) for key AUVoiceIOClients/com-nexy-assistant/AUVoiceIOChatFlavor, translatedBundleID com.nexy.assistant, bundleIDs {(
    "com.nexy.assistant"
)}
default	11:27:26.049884-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> vpio_preferenceChangedListener: new value ((null)) for key AUVoiceIOClients/com-nexy-assistant/AUVoiceIOIsAutoChatFlavorEnabled, translatedBundleID com.nexy.assistant, bundleIDs {(
    "com.nexy.assistant"
)}
default	11:27:26.050040-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetSupportedChatFlavorsForBundleID: <private>-><private> get supported chat flavors: <private>
default	11:27:26.050054-0500	Nexy	            HALSystem.cpp:134    Enabling HAL Voice Isolation support
default	11:27:26.050539-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetHiddenChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	11:27:26.051079-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOHiddenChatFlavors newValue: (
    1
)
default	11:27:26.051198-0500	Nexy	[0xa576c8c80] activating connection: mach=true listener=false peer=false name=com.apple.tccd
default	11:27:26.052561-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=2761.2, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=2761, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	11:27:26.060094-0500	tccd	AUTHREQ_SUBJECT: msgID=2761.2, subject=com.nexy.assistant,
default	11:27:26.060710-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc12d15b00 at /Applications/Nexy.app
default	11:27:26.072561-0500	Nexy	[0xa576c8c80] invalidated after the last release of the connection object
default	11:27:26.072606-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetSupportedChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	11:27:26.075081-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOSupportedChatFlavors newValue: (
)
default	11:27:26.077054-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=404.1200, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=2761, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=392, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	11:27:26.077874-0500	tccd	AUTHREQ_SUBJECT: msgID=404.1200, subject=com.nexy.assistant,
default	11:27:26.078418-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc12d14c00 at /Applications/Nexy.app
error	11:27:26.090419-0500	tccd	Request message contains a target_token to accessing_process (TCCDProcess: identifier=com.nexy.assistant, pid=2761, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy) but TCCDProcess: identifier=com.apple.audio.coreaudiod, pid=404, auid=202, euid=202, binary_path=/usr/sbin/coreaudiod is not a TCC manager for service: kTCCServiceScreenCapture.
default	11:27:26.091305-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=404.1202, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=2761, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=392, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	11:27:26.092052-0500	tccd	AUTHREQ_SUBJECT: msgID=404.1202, subject=com.nexy.assistant,
default	11:27:26.092551-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc12d14c00 at /Applications/Nexy.app
default	11:27:26.107021-0500	Nexy	  HALPlugInManagement.cpp:440    HALPlugInManagement::RegisterPlugIns: skipping in-process plug-ins
error	11:27:26.107709-0500	Nexy	AddInstanceForFactory: No factory registered for id <CFUUID 0xa56ced8e0> F8BB1C28-BAE8-11D6-9C31-00039315CD46
error	11:27:26.123169-0500	Nexy	         HALC_ProxyObjectMap.cpp:174   HALC_ProxyObjectMap::_CopyObjectByObjectID: failed to create the local object
error	11:27:26.123178-0500	Nexy	            HALC_ShellDevice.cpp:2673  HALC_ShellDevice::RebuildControlList: couldn't find the control object
default	11:27:26.128985-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	11:27:26.129127-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	11:27:26.135194-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetPreferredChatFlavorForBundleID: <private>-><private> get value: 0
default	11:27:28.696947-0500	kernel	SK[8]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 4B0F8299-CF61-4594-9C15-AC2F9F5E57FD flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.56838,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0xda64b6ee tp_proto=0x06"
default	11:27:28.696995-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:56838<-><IPv4-redacted>:53] interface: utun6 (skipped: 516)
so_gencnt: 748669 t_state: SYN_SENT process: Nexy:2761 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xbc0aafeb
default	11:27:28.697521-0500	kernel	tcp connected: [<IPv4-redacted>:56838<-><IPv4-redacted>:53] interface: utun6 (skipped: 516)
so_gencnt: 748669 t_state: ESTABLISHED process: Nexy:2761 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xbc0aafeb
default	11:27:28.697819-0500	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:56838<-><IPv4-redacted>:53] interface: utun6 (skipped: 516)
so_gencnt: 748669 t_state: FIN_WAIT_1 process: Nexy:2761 Duration: 0.001 sec Conn_Time: 0.000 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 1.000 ms rttvar: 0.500 ms base rtt: 1 ms so_error: 0 svc/tc: 0 flow: 0xbc0aafeb
default	11:27:28.697828-0500	kernel	tcp_connection_summary [<IPv4-redacted>:56838<-><IPv4-redacted>:53] interface: utun6 (skipped: 516)
so_gencnt: 748669 t_state: FIN_WAIT_1 process: Nexy:2761 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	11:27:28.725016-0500	Nexy	[0xa576c8c80] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioComponentRegistrar
default	11:27:28.742376-0500	Nexy	                AUHAL.cpp:420   AUHAL: (0xa56760740) Selecting device 85 from constructor
default	11:27:28.742383-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0xa56760740)
default	11:27:28.742389-0500	Nexy	                AUHAL.cpp:676   SelectDevice: (0xa56760740) not already running
default	11:27:28.742393-0500	Nexy	                AUHAL.cpp:752   SelectDevice: (0xa56760740) nothing to teardown
default	11:27:28.742398-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0xa56760740) connecting device 85
default	11:27:28.742494-0500	Nexy	                AUHAL.cpp:3413  IsDeviceUsable: (0xa56760740) Device ID: 85 (Input:No | Output:Yes): true
default	11:27:28.742868-0500	Nexy	                AUHAL.cpp:769   SelectDevice: (0xa56760740) created ioproc 0xa for device 85
default	11:27:28.742984-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0xa56760740) adding 7 device listeners to device 85
default	11:27:28.743161-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0xa56760740) adding 0 device delegate listeners to device 85
default	11:27:28.743170-0500	Nexy	                AUHAL.cpp:1581  UpdateStreamFormats: -> (0xa56760740)
default	11:27:28.743238-0500	Nexy	                AUHAL.cpp:1677  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  48000 Hz, Float32, interleaved
default	11:27:28.743247-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 1 output streams; not all mono
default	11:27:28.743253-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	11:27:28.743261-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 0 input streams; not all mono
default	11:27:28.743268-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	11:27:28.743350-0500	Nexy	                AUHAL.cpp:1771  UpdateStreamFormats: AUHAL(0xa56760740) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	11:27:28.743360-0500	Nexy	                AUHAL.cpp:1777  UpdateStreamFormats: AUHAL(0xa56760740) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	11:27:28.743364-0500	Nexy	                AUHAL.cpp:1787  UpdateStreamFormats: <-
default	11:27:28.743367-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0xa56760740) removing 0 device listeners from device 0
default	11:27:28.743376-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0xa56760740) removing 0 device delegate listeners from device 0
default	11:27:28.743383-0500	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0xa56760740)
default	11:27:28.743400-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Output stream enables: Stream 0 is DISABLED
default	11:27:28.743776-0500	Nexy	                AUHAL.cpp:2298  SetProperty: (0xa56760740) caller requesting device change from 85 to 91
default	11:27:28.743784-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0xa56760740)
default	11:27:28.743788-0500	Nexy	                AUHAL.cpp:676   SelectDevice: (0xa56760740) not already running
default	11:27:28.743793-0500	Nexy	                AUHAL.cpp:682   SelectDevice: (0xa56760740) disconnecting device 85
default	11:27:28.743799-0500	Nexy	                AUHAL.cpp:746   SelectDevice: (0xa56760740) destroying ioproc 0xa for device 85
default	11:27:28.744486-0500	Nexy	  AVAudioSession_MacOS.mm:1021  initForMacOS
default	11:27:28.746567-0500	Nexy	[0xa576c8f00] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioSession
default	11:27:28.749005-0500	audiomxd	  ServerSessionManager.mm:315   { "action":"create_session", "session":{"ID":"0x1c5042","name":"Nexy(2761)"}, "details":{"PID":2761,"session_type":"Primary"} }
default	11:27:28.749121-0500	audiomxd	AudioApplicationInfoImpl.mm:250   Setting initial isRecording state: 0 for newly-created AudioApp
	app: {"name":"[implicit] Nexy","pid":2761}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1c5042, sessionType: 'prim', isRecording: false }, 
]
default	11:27:28.751110-0500	audiomxd	  ServerSessionManager.mm:1317  Start process monitoring, pid = 2761, name = Nexy
default	11:27:28.751549-0500	Nexy	    SessionCore_Create.mm:99    Created session 0xa575dd280 with ID: 0x1c5042
default	11:27:28.754127-0500	Nexy	[0xa576c9040] activating connection: mach=true listener=false peer=false name=com.apple.audioanalyticsd
error	11:27:28.755635-0500	Nexy	Reporter disconnected. { function=sendMessage, reporterID=11858404704257 }
default	11:27:28.755651-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped Unknown {1C-77-54-18-C8-A3:output, 0xa}
default	11:27:28.755706-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	11:27:28.755837-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0xa56760740) connecting device 91
default	11:27:28.755976-0500	Nexy	                AUHAL.cpp:3413  IsDeviceUsable: (0xa56760740) Device ID: 91 (Input:Yes | Output:No): true
default	11:27:28.757757-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=404.1203, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=2761, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=392, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	11:27:28.759473-0500	tccd	AUTHREQ_SUBJECT: msgID=404.1203, subject=com.nexy.assistant,
default	11:27:28.760349-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc12d14c00 at /Applications/Nexy.app
default	11:27:28.781624-0500	tccd	AUTHREQ_PROMPTING: msgID=404.1203, service=kTCCServiceMicrophone, subject=Sub:{com.nexy.assistant}Resp:{TCCDProcess: identifier=com.nexy.assistant, pid=2761, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy},
default	11:27:29.987796-0500	runningboardd	Assertion did invalidate due to timeout: 397-397-135381 (target:[app<application.com.nexy.assistant.21576034.21576040(501)>:2761])
default	11:27:30.182511-0500	runningboardd	[app<application.com.nexy.assistant.21576034.21576040(501)>:2761] Ignoring jetsam update because this process is not memory-managed
default	11:27:30.182533-0500	runningboardd	[app<application.com.nexy.assistant.21576034.21576040(501)>:2761] Ignoring suspend because this process is not lifecycle managed
default	11:27:30.182547-0500	runningboardd	[app<application.com.nexy.assistant.21576034.21576040(501)>:2761] Ignoring GPU update because this process is not GPU managed
default	11:27:30.182570-0500	runningboardd	[app<application.com.nexy.assistant.21576034.21576040(501)>:2761] Ignoring memory limit update because this process is not memory-managed
default	11:27:30.185292-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.21576034.21576040(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	11:27:30.185832-0500	gamepolicyd	Received state update for 2761 (app<application.com.nexy.assistant.21576034.21576040(501)>, running-active-NotVisible
default	11:27:30.382446-0500	Nexy	                AUHAL.cpp:769   SelectDevice: (0xa56760740) created ioproc 0xa for device 91
default	11:27:30.382721-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0xa56760740) adding 7 device listeners to device 91
default	11:27:30.383060-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0xa56760740) adding 0 device delegate listeners to device 91
default	11:27:30.383080-0500	Nexy	                AUHAL.cpp:1581  UpdateStreamFormats: -> (0xa56760740)
default	11:27:30.383097-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 0 output streams; not all mono
default	11:27:30.383119-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Output render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	11:27:30.383371-0500	Nexy	                AUHAL.cpp:1677  UpdateStreamFormats: 
  input stream 0 [0x5c]:  1 ch,  24000 Hz, Float32
default	11:27:30.383385-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 1 input streams; all mono
default	11:27:30.383395-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Input render format:  1 ch,  24000 Hz, Float32
default	11:27:30.380980-0500	tccd	Publishing <TCCDEvent: type=Create, service=kTCCServiceMicrophone, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 3 subscribers: {
    482 = "<TCCDEventSubscriber: token=482, state=Passed, csid=com.apple.chronod>";
    36 = "<TCCDEventSubscriber: token=36, state=Passed, csid=com.apple.cloudd>";
    485 = "<TCCDEventSubscriber: token=485, state=Passed, csid=com.apple.photolibraryd>";
}
default	11:27:30.383559-0500	Nexy	                AUHAL.cpp:1771  UpdateStreamFormats: AUHAL(0xa56760740) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	11:27:30.383579-0500	Nexy	                AUHAL.cpp:1777  UpdateStreamFormats: AUHAL(0xa56760740) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	11:27:30.383589-0500	Nexy	                AUHAL.cpp:1787  UpdateStreamFormats: <-
default	11:27:30.383598-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0xa56760740) removing 7 device listeners from device 85
default	11:27:30.383888-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0xa56760740) removing 0 device delegate listeners from device 85
default	11:27:30.383904-0500	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0xa56760740)
default	11:27:30.385010-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	11:27:30.384917-0500	chronod	[appAuth:com.nexy.assistant] tcc authorization(s) changed
default	11:27:30.386869-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=404.1204, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=2761, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=392, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	11:27:30.388533-0500	tccd	AUTHREQ_SUBJECT: msgID=404.1204, subject=com.nexy.assistant,
default	11:27:30.390640-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc12d14c00 at /Applications/Nexy.app
default	11:27:30.408791-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	11:27:30.410248-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=404.1205, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=2761, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=392, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	11:27:30.411550-0500	tccd	AUTHREQ_SUBJECT: msgID=404.1205, subject=com.nexy.assistant,
default	11:27:30.412271-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc12d14c00 at /Applications/Nexy.app
default	11:27:30.427495-0500	Nexy	Registered notify signal com.apple.caulk.alloc.audiodump (0)
default	11:27:30.430341-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=404.1206, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=2761, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=392, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	11:27:30.431670-0500	tccd	AUTHREQ_SUBJECT: msgID=404.1206, subject=com.nexy.assistant,
default	11:27:30.433348-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc12d14c00 at /Applications/Nexy.app
default	11:27:30.449709-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetPreferredChatFlavorForBundleID: <private>-><private> get value: 0
default	11:27:30.450077-0500	coreaudiod	>>> NEGOTIATE [com.nexy.assistant]
default	11:27:30.450263-0500	coreaudiod	<<< NEGOTIATE [com.nexy.assistant]
default	11:27:30.450289-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetSupportedChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	11:27:30.451692-0500	coreaudiod	>>> ADAPT [com.nexy.assistant]
default	11:27:30.453702-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xc50bf0600] Created node ADM::com.nexy.assistant_5728.5639.0_airpods noise suppression studio::in-0 with nodeID 0 - reporting period = 10.000000, sample rate = 24000.000000
default	11:27:30.453775-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xc50bf0600] Created node ADM::com.nexy.assistant_5728.5639.0_airpods noise suppression studio::out-0 with nodeID 1 - reporting period = 10.000000, sample rate = 24000.000000
default	11:27:30.453926-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOSupportedChatFlavors newValue: (
    0,
    2
)
default	11:27:30.558511-0500	coreaudiod	<<< ADAPT [com.nexy.assistant]
default	11:27:30.560703-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Input {1C-77-54-18-C8-A3:input, 0xa}
default	11:27:30.560657-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:5728 called from <private>
default	11:27:30.561769-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:5728 called from <private>
default	11:27:30.562203-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(5728)
default	11:27:30.562222-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:5728 called from <private>
default	11:27:30.562228-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:5728 called from <private>
default	11:27:30.562711-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(5727)
default	11:27:30.563189-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:5727 called from <private>
default	11:27:30.564371-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	11:27:30.565471-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	11:27:30.563287-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:5727 called from <private>
default	11:27:30.567370-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.21576034.21576040(501)>:2761] from originator [osservice<com.apple.powerd>:332] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:397-332-135409 target:2761 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	11:27:30.567667-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(5728)
default	11:27:30.567550-0500	runningboardd	Assertion 397-332-135409 (target:[app<application.com.nexy.assistant.21576034.21576040(501)>:2761]) will be created as active
default	11:27:30.567706-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(5728)
default	11:27:30.568008-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:5728 called from <private>
default	11:27:30.568023-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:5728 called from <private>
default	11:27:30.568039-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:5728 called from <private>
default	11:27:30.568051-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:5728 called from <private>
default	11:27:30.568092-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:5728 called from <private>
default	11:27:30.568156-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:5728 called from <private>
default	11:27:30.578491-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:5727 called from <private>
default	11:27:30.579088-0500	runningboardd	[app<application.com.nexy.assistant.21576034.21576040(501)>:2761] Ignoring jetsam update because this process is not memory-managed
default	11:27:30.579199-0500	runningboardd	[app<application.com.nexy.assistant.21576034.21576040(501)>:2761] Ignoring suspend because this process is not lifecycle managed
default	11:27:30.579730-0500	runningboardd	[app<application.com.nexy.assistant.21576034.21576040(501)>:2761] Ignoring GPU update because this process is not GPU managed
default	11:27:30.580117-0500	runningboardd	[app<application.com.nexy.assistant.21576034.21576040(501)>:2761] Ignoring memory limit update because this process is not memory-managed
default	11:27:30.580545-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1c5042","name":"Nexy(2761)"}, "details":{"deviceUIDs":["1C-77-54-18-C8-A3:input"],"implicit_category":"Record","input_running":true,"output_running":false} }
default	11:27:30.580789-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 67, PID = 2761, Name = sid:0x1c5042, Nexy(2761), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	11:27:30.580955-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 67, PID = 2761, Name = sid:0x1c5042, Nexy(2761), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	11:27:30.581365-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 67, PID = 2761, Name = sid:0x1c5042, Nexy(2761), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	11:27:30.581470-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 67, PID = 2761, Name = sid:0x1c5042, Nexy(2761), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	11:27:30.581883-0500	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 67, PID = 2761, Name = sid:0x1c5042, Nexy(2761), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> is going active
default	11:27:30.581943-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1c5042, Nexy(2761), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 67 starting recording
default	11:27:30.581176-0500	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1c5042, Nexy(2761), 'prim'', AudioCategory changed to 'Record_WithBluetooth'
default	11:27:30.581454-0500	audiomxd	UpdateAudioState CID 0x218B0001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	11:27:30.578512-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:5727 called from <private>
default	11:27:30.582730-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 67, PID = 2761, Name = sid:0x1c5042, Nexy(2761), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	11:27:30.579566-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(5727)
default	11:27:30.579940-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(5728)
default	11:27:30.583421-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 67, PID = 2761, Name = sid:0x1c5042, Nexy(2761), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	11:27:30.583632-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1c5042, Nexy(2761), 'prim'', displayID:'com.nexy.assistant'}
default	11:27:30.579979-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:5728 called from <private>
default	11:27:30.583384-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=404.1207, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=2761, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=392, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	11:27:30.584279-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	11:27:30.583961-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [1, 0]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:input"
)}
default	11:27:30.584008-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	11:27:30.584105-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	11:27:30.588552-0500	tccd	AUTHREQ_SUBJECT: msgID=404.1207, subject=com.nexy.assistant,
fault	11:27:30.589498-0500	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.21576034.21576040 AUID=501> and <type=Application identifier=application.com.nexy.assistant.21576034.21576040>
default	11:27:30.592354-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:5727 called from <private>
default	11:27:30.592376-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:5727 called from <private>
default	11:27:30.592520-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(5727)
default	11:27:30.593616-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc12d14c00 at /Applications/Nexy.app
fault	11:27:30.595346-0500	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.21576034.21576040 AUID=501> and <type=Application identifier=application.com.nexy.assistant.21576034.21576040>
default	11:27:30.595835-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.21576034.21576040(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	11:27:30.596352-0500	runningboardd	Invalidating assertion 397-332-135409 (target:[app<application.com.nexy.assistant.21576034.21576040(501)>:2761]) from originator [osservice<com.apple.powerd>:332]
default	11:27:30.596659-0500	gamepolicyd	Received state update for 2761 (app<application.com.nexy.assistant.21576034.21576040(501)>, running-active-NotVisible
default	11:27:30.599041-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(5727)
default	11:27:30.599201-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:5727 called from <private>
default	11:27:30.599211-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:5727 called from <private>
default	11:27:30.599291-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(5727)
default	11:27:30.610300-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(5727)
default	11:27:30.610646-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:5727 called from <private>
default	11:27:30.610652-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:5727 called from <private>
default	11:27:30.610718-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:5727 called from <private>
default	11:27:30.610742-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:5727 called from <private>
default	11:27:30.610754-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:5727 called from <private>
default	11:27:30.610760-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:5727 called from <private>
default	11:27:30.610821-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:5727 called from <private>
default	11:27:30.610913-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:5727 called from <private>
default	11:27:30.617989-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	11:27:30.642002-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.21576034.21576040(501)>:2761] from originator [osservice<com.apple.powerd>:332] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:397-332-135410 target:2761 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	11:27:30.642936-0500	runningboardd	Assertion 397-332-135410 (target:[app<application.com.nexy.assistant.21576034.21576040(501)>:2761]) will be created as active
default	11:27:30.642652-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:5728 called from <private>
default	11:27:30.642822-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(5728)
default	11:27:30.642863-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:5728 called from <private>
default	11:27:30.642873-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:5728 called from <private>
default	11:27:30.644104-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	11:27:30.644006-0500	runningboardd	Invalidating assertion 397-332-135410 (target:[app<application.com.nexy.assistant.21576034.21576040(501)>:2761]) from originator [osservice<com.apple.powerd>:332]
default	11:27:30.648014-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	11:27:30.650829-0500	tccd	AUTHREQ_SUBJECT: msgID=404.1208, subject=com.nexy.assistant,
default	11:27:30.651283-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:27:30.651362-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:27:30.651417-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	11:27:30.651426-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:27:30.651434-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	11:27:30.651443-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	11:27:30.662062-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	11:27:30.662605-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:27:30.662615-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:27:30.662638-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	11:27:30.662661-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:27:30.662713-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	11:27:30.662823-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	11:27:30.669084-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:27:30.679326-0500	coreaudiod	>>> ADAPT [com.nexy.assistant]
default	11:27:30.681581-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xc50bf0600] Created node ADM::com.nexy.assistant_5728.5639.0_airpods noise suppression studio::in-0 with nodeID 0 - reporting period = 10.000000, sample rate = 24000.000000
default	11:27:30.681643-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xc50bf0600] Created node ADM::com.nexy.assistant_5728.5639.0_airpods noise suppression studio::out-0 with nodeID 1 - reporting period = 10.000000, sample rate = 24000.000000
default	11:27:30.698916-0500	runningboardd	[app<application.com.nexy.assistant.21576034.21576040(501)>:2761] Ignoring jetsam update because this process is not memory-managed
default	11:27:30.698928-0500	runningboardd	[app<application.com.nexy.assistant.21576034.21576040(501)>:2761] Ignoring suspend because this process is not lifecycle managed
default	11:27:30.698937-0500	runningboardd	[app<application.com.nexy.assistant.21576034.21576040(501)>:2761] Ignoring GPU update because this process is not GPU managed
default	11:27:30.698959-0500	runningboardd	[app<application.com.nexy.assistant.21576034.21576040(501)>:2761] Ignoring memory limit update because this process is not memory-managed
default	11:27:30.701776-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.21576034.21576040(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	11:27:30.702238-0500	gamepolicyd	Received state update for 2761 (app<application.com.nexy.assistant.21576034.21576040(501)>, running-active-NotVisible
default	11:27:30.716375-0500	coreaudiod	<<< ADAPT [com.nexy.assistant]
default	11:27:30.718321-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:5728 called from <private>
default	11:27:30.718359-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:5728 called from <private>
default	11:27:30.718435-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	11:27:30.719949-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.21576034.21576040(501)>:2761] from originator [osservice<com.apple.powerd>:332] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:397-332-135412 target:2761 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	11:27:30.720027-0500	runningboardd	Assertion 397-332-135412 (target:[app<application.com.nexy.assistant.21576034.21576040(501)>:2761]) will be created as active
default	11:27:30.720428-0500	runningboardd	[app<application.com.nexy.assistant.21576034.21576040(501)>:2761] Ignoring jetsam update because this process is not memory-managed
default	11:27:30.721261-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:5728 called from <private>
default	11:27:30.720475-0500	runningboardd	[app<application.com.nexy.assistant.21576034.21576040(501)>:2761] Ignoring suspend because this process is not lifecycle managed
default	11:27:30.721162-0500	runningboardd	[app<application.com.nexy.assistant.21576034.21576040(501)>:2761] Ignoring GPU update because this process is not GPU managed
default	11:27:30.721287-0500	runningboardd	[app<application.com.nexy.assistant.21576034.21576040(501)>:2761] Ignoring memory limit update because this process is not memory-managed
default	11:27:30.721391-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(5728)
default	11:27:30.721407-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:5728 called from <private>
default	11:27:30.721415-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:5728 called from <private>
default	11:27:30.722557-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	11:27:30.722688-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	11:27:30.723274-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(5728)
default	11:27:30.723457-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:5728 called from <private>
default	11:27:30.723469-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:5728 called from <private>
default	11:27:30.723484-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:5728 called from <private>
default	11:27:30.725521-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=404.1209, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=2761, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=392, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	11:27:30.727108-0500	tccd	AUTHREQ_SUBJECT: msgID=404.1209, subject=com.nexy.assistant,
default	11:27:30.727596-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.21576034.21576040(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	11:27:30.727895-0500	runningboardd	Invalidating assertion 397-332-135412 (target:[app<application.com.nexy.assistant.21576034.21576040(501)>:2761]) from originator [osservice<com.apple.powerd>:332]
default	11:27:30.728197-0500	gamepolicyd	Received state update for 2761 (app<application.com.nexy.assistant.21576034.21576040(501)>, running-active-NotVisible
default	11:27:30.728274-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc12d14c00 at /Applications/Nexy.app
default	11:27:30.729154-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	11:27:30.729218-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	11:27:30.729290-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	11:27:30.729489-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	11:27:30.729676-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:27:30.729703-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:27:30.729718-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	11:27:30.729727-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:27:30.729734-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	11:27:30.729742-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	11:27:30.729969-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	11:27:30.729980-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:27:30.729989-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:27:30.730005-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	11:27:30.730014-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:27:30.730021-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	11:27:30.730050-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	11:27:30.748548-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.21576034.21576040(501)>:2761] from originator [osservice<com.apple.powerd>:332] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:397-332-135413 target:2761 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	11:27:30.749150-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:5728 called from <private>
default	11:27:30.751053-0500	runningboardd	Assertion 397-332-135413 (target:[app<application.com.nexy.assistant.21576034.21576040(501)>:2761]) will be created as active
default	11:27:30.759228-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	11:27:30.759388-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	11:27:30.759479-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	11:27:30.760176-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:27:30.760189-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:27:30.760202-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	11:27:30.760210-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:27:30.760215-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	11:27:30.760222-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	11:27:30.760272-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:27:30.760308-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:27:30.760343-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	11:27:30.760353-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	11:27:30.760416-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:27:30.760472-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	11:27:30.760518-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	11:27:30.761691-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:27:30.761699-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:27:30.761710-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	11:27:30.761715-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:27:30.761730-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	11:27:30.761738-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	11:27:30.761868-0500	ControlCenter	Navigating to new application [com.nexy.assistant]
default	11:27:31.776849-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xa}
default	11:27:31.777322-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1c5042","name":"Nexy(2761)"}, "details":{"deviceUIDs":[],"implicit_category":"","input_running":false,"output_running":false} }
default	11:27:31.777506-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 67, PID = 2761, Name = sid:0x1c5042, Nexy(2761), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	11:27:31.777597-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 67, PID = 2761, Name = sid:0x1c5042, Nexy(2761), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	11:27:31.777647-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1c5042, Nexy(2761), 'prim'', displayID:'com.nexy.assistant'}
default	11:27:31.777713-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	11:27:31.777728-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1c5042, Nexy(2761), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 67 stopping recording
default	11:27:31.777776-0500	audiomxd	-MXCoreSession- -[MXCoreSession endInterruption:]: Session <ID: 67, PID = 2761, Name = sid:0x1c5042, Nexy(2761), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> is going inactive
default	11:27:31.777813-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 67, PID = 2761, Name = sid:0x1c5042, Nexy(2761), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	11:27:31.777857-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 67, PID = 2761, Name = sid:0x1c5042, Nexy(2761), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	11:27:31.778002-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 0]. BT device UIDS: {(
)}
default	11:27:31.778012-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 200 flag 0x1 < Hijack > app com.nexy.assistant CID 0x218B0001 category Not set
default	11:27:31.778016-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	11:27:31.781752-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	11:27:31.781794-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	11:27:31.781816-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	11:27:31.781842-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	11:27:31.781933-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	11:27:31.781949-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	11:27:31.781965-0500	audioaccessoryd	AudioStateChanged: Removed audio session app com.nexy.assistant 201 count 0
default	11:27:31.781614-0500	audiomxd	UpdateAudioState CID 0x218B0001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	11:27:31.781460-0500	runningboardd	Invalidating assertion 397-332-135413 (target:[app<application.com.nexy.assistant.21576034.21576040(501)>:2761]) from originator [osservice<com.apple.powerd>:332]
default	11:27:31.781682-0500	audiomxd	UpdateAudioState CID 0x218B0001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	11:27:31.784140-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	11:27:31.787755-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:27:31.787785-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:27:31.787800-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	11:27:31.787808-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:27:31.787817-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	11:27:31.787830-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	11:27:31.788007-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	11:27:31.878760-0500	Nexy	                AUHAL.cpp:473   ~AUHAL: (0xa56760740) Selecting device 0 from destructor
default	11:27:31.878777-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0xa56760740)
default	11:27:31.878786-0500	Nexy	                AUHAL.cpp:676   SelectDevice: (0xa56760740) not already running
default	11:27:31.878791-0500	Nexy	                AUHAL.cpp:682   SelectDevice: (0xa56760740) disconnecting device 91
default	11:27:31.878798-0500	Nexy	                AUHAL.cpp:746   SelectDevice: (0xa56760740) destroying ioproc 0xa for device 91
default	11:27:31.878837-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xa}
default	11:27:31.878870-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	11:27:31.879048-0500	Nexy	                AUHAL.cpp:848   SelectDevice: (0xa56760740) nothing to setup
default	11:27:31.879061-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0xa56760740) adding 0 device listeners to device 0
default	11:27:31.879070-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0xa56760740) adding 0 device delegate listeners to device 0
default	11:27:31.879076-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0xa56760740) removing 7 device listeners from device 91
default	11:27:31.879326-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0xa56760740) removing 0 device delegate listeners from device 91
default	11:27:31.879339-0500	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0xa56760740)
default	11:27:31.885862-0500	runningboardd	[app<application.com.nexy.assistant.21576034.21576040(501)>:2761] Ignoring jetsam update because this process is not memory-managed
default	11:27:31.885883-0500	runningboardd	[app<application.com.nexy.assistant.21576034.21576040(501)>:2761] Ignoring suspend because this process is not lifecycle managed
default	11:27:31.885894-0500	runningboardd	[app<application.com.nexy.assistant.21576034.21576040(501)>:2761] Ignoring GPU update because this process is not GPU managed
default	11:27:31.885910-0500	runningboardd	[app<application.com.nexy.assistant.21576034.21576040(501)>:2761] Ignoring memory limit update because this process is not memory-managed
default	11:27:31.889484-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.21576034.21576040(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	11:27:31.894200-0500	gamepolicyd	Received state update for 2761 (app<application.com.nexy.assistant.21576034.21576040(501)>, running-active-NotVisible
default	11:27:32.137274-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=2766.1, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=2761, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.osascript, pid=2766, auid=501, euid=501, binary_path=/usr/bin/osascript}, },
default	11:27:32.139121-0500	tccd	AUTHREQ_SUBJECT: msgID=2766.1, subject=com.nexy.assistant,
default	11:27:32.139897-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa5f977600 at /Applications/Nexy.app
default	11:27:32.156889-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=391.2200, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=2761, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.osascript, pid=2766, auid=501, euid=501, binary_path=/usr/bin/osascript}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=391, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	11:27:32.158104-0500	tccd	AUTHREQ_SUBJECT: msgID=391.2200, subject=com.nexy.assistant,
default	11:27:32.158819-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa5f977600 at /Applications/Nexy.app
default	11:27:32.203279-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa5f977900 at /Applications/Nexy.app
default	11:27:32.348939-0500	System Events	TCCAccessRequestIndirect: TCCAccessRequestIndirect with pid 2767: target_identity: {
    kTCCCodeIdentityAuditToken = {length = 32, bytes = 0xf5010000 f5010000 14000000 f5010000 ... b9860100 de7a0300 };
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
default	11:27:32.360352-0500	tccd	target_executable_path_URL: file:///Applications/Nexy.app/Contents/MacOS/Nexy
default	11:27:32.580323-0500	Nexy	[0xa576c9400] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	11:27:32.580871-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=2761.3, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=2761, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	11:27:32.581861-0500	tccd	AUTHREQ_SUBJECT: msgID=2761.3, subject=com.nexy.assistant,
default	11:27:32.582443-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa5f976d00 at /Applications/Nexy.app
default	11:27:32.596900-0500	Nexy	                AUHAL.cpp:420   AUHAL: (0xa56760740) Selecting device 85 from constructor
default	11:27:32.596911-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0xa56760740)
default	11:27:32.596918-0500	Nexy	                AUHAL.cpp:676   SelectDevice: (0xa56760740) not already running
default	11:27:32.596921-0500	Nexy	                AUHAL.cpp:752   SelectDevice: (0xa56760740) nothing to teardown
default	11:27:32.596925-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0xa56760740) connecting device 85
default	11:27:32.597002-0500	Nexy	                AUHAL.cpp:3413  IsDeviceUsable: (0xa56760740) Device ID: 85 (Input:No | Output:Yes): true
default	11:27:32.597110-0500	Nexy	                AUHAL.cpp:769   SelectDevice: (0xa56760740) created ioproc 0xb for device 85
default	11:27:32.597244-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0xa56760740) adding 7 device listeners to device 85
default	11:27:32.597407-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0xa56760740) adding 0 device delegate listeners to device 85
default	11:27:32.597414-0500	Nexy	                AUHAL.cpp:1581  UpdateStreamFormats: -> (0xa56760740)
default	11:27:32.597476-0500	Nexy	                AUHAL.cpp:1677  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  24000 Hz, Float32, interleaved
default	11:27:32.597487-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 1 output streams; not all mono
default	11:27:32.597492-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Output render format:  2 ch,  24000 Hz, Float32, interleaved
default	11:27:32.597498-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 0 input streams; not all mono
default	11:27:32.597506-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	11:27:32.597584-0500	Nexy	                AUHAL.cpp:1771  UpdateStreamFormats: AUHAL(0xa56760740) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	11:27:32.597593-0500	Nexy	                AUHAL.cpp:1777  UpdateStreamFormats: AUHAL(0xa56760740) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	11:27:32.597598-0500	Nexy	                AUHAL.cpp:1787  UpdateStreamFormats: <-
default	11:27:32.597603-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0xa56760740) removing 0 device listeners from device 0
default	11:27:32.597606-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0xa56760740) removing 0 device delegate listeners from device 0
default	11:27:32.597610-0500	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0xa56760740)
default	11:27:32.597620-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Output stream enables: Stream 0 is DISABLED
default	11:27:32.597676-0500	Nexy	                AUHAL.cpp:2298  SetProperty: (0xa56760740) caller requesting device change from 85 to 91
default	11:27:32.597685-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0xa56760740)
default	11:27:32.598901-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=404.1210, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=2761, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=392, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	11:27:32.599765-0500	tccd	AUTHREQ_SUBJECT: msgID=404.1210, subject=com.nexy.assistant,
default	11:27:32.600285-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc12d15b00 at /Applications/Nexy.app
default	11:27:32.612142-0500	Nexy	                AUHAL.cpp:769   SelectDevice: (0xa56760740) created ioproc 0xb for device 91
default	11:27:32.612250-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0xa56760740) adding 7 device listeners to device 91
default	11:27:32.612430-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0xa56760740) adding 0 device delegate listeners to device 91
default	11:27:32.612442-0500	Nexy	                AUHAL.cpp:1581  UpdateStreamFormats: -> (0xa56760740)
default	11:27:32.612449-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 0 output streams; not all mono
default	11:27:32.612459-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Output render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	11:27:32.612586-0500	Nexy	                AUHAL.cpp:1677  UpdateStreamFormats: 
  input stream 0 [0x5c]:  1 ch,  24000 Hz, Float32
default	11:27:32.612596-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 1 input streams; all mono
default	11:27:32.612601-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Input render format:  1 ch,  24000 Hz, Float32
default	11:27:32.612684-0500	Nexy	                AUHAL.cpp:1771  UpdateStreamFormats: AUHAL(0xa56760740) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	11:27:32.612695-0500	Nexy	                AUHAL.cpp:1777  UpdateStreamFormats: AUHAL(0xa56760740) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	11:27:32.612701-0500	Nexy	                AUHAL.cpp:1787  UpdateStreamFormats: <-
default	11:27:32.612706-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0xa56760740) removing 7 device listeners from device 85
default	11:27:32.612859-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0xa56760740) removing 0 device delegate listeners from device 85
default	11:27:32.612865-0500	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0xa56760740)
default	11:27:32.613379-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	11:27:32.615694-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc12d15b00 at /Applications/Nexy.app
default	11:27:32.628566-0500	Nexy	       ACv2Workarounds.mm:51    com.nexy.assistant: fix84702776_86723525_86479548_89800354_SinglePacketDesc: false
default	11:27:32.628849-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	11:27:32.629725-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=404.1212, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=2761, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=392, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	11:27:32.644328-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=404.1213, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=2761, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=392, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	11:27:32.663158-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1c5042","name":"Nexy(2761)"}, "details":{"deviceUIDs":["1C-77-54-18-C8-A3:input"],"implicit_category":"Record","input_running":true,"output_running":false} }
default	11:27:32.663260-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 67, PID = 2761, Name = sid:0x1c5042, Nexy(2761), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	11:27:32.663296-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Category/Mode changed -- The score for sid:0x1c5042, Nexy(2761), 'prim'/com.nexy.assistant was not correct. Old score = 201
default	11:27:32.663324-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 67, PID = 2761, Name = sid:0x1c5042, Nexy(2761), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	11:27:32.663597-0500	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1c5042, Nexy(2761), 'prim'', AudioCategory changed to 'Record_WithBluetooth'
default	11:27:32.663758-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 67, PID = 2761, Name = sid:0x1c5042, Nexy(2761), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	11:27:32.663800-0500	audiomxd	UpdateAudioState CID 0x218B0001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	11:27:32.663862-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 67, PID = 2761, Name = sid:0x1c5042, Nexy(2761), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	11:27:32.663906-0500	audiomxd	UpdateAudioState CID 0x218B0001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	11:27:32.663924-0500	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 67, PID = 2761, Name = sid:0x1c5042, Nexy(2761), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> is going active
default	11:27:32.663960-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	11:27:32.663935-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1c5042, Nexy(2761), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 67 starting recording
default	11:27:32.664011-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	11:27:32.664047-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	11:27:32.663968-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.21576034.21576040(501)>:2761] from originator [osservice<com.apple.powerd>:332] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:397-332-135433 target:2761 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	11:27:32.664071-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 67, PID = 2761, Name = sid:0x1c5042, Nexy(2761), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	11:27:32.664071-0500	runningboardd	Assertion 397-332-135433 (target:[app<application.com.nexy.assistant.21576034.21576040(501)>:2761]) will be created as active
default	11:27:32.664419-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [1, 0]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:input"
)}
default	11:27:32.664434-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	11:27:32.664170-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 67, PID = 2761, Name = sid:0x1c5042, Nexy(2761), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	11:27:32.664541-0500	runningboardd	[app<application.com.nexy.assistant.21576034.21576040(501)>:2761] Ignoring jetsam update because this process is not memory-managed
default	11:27:32.664596-0500	runningboardd	[app<application.com.nexy.assistant.21576034.21576040(501)>:2761] Ignoring suspend because this process is not lifecycle managed
default	11:27:32.664136-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	11:27:32.664633-0500	runningboardd	[app<application.com.nexy.assistant.21576034.21576040(501)>:2761] Ignoring GPU update because this process is not GPU managed
default	11:27:32.664268-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1c5042, Nexy(2761), 'prim'', displayID:'com.nexy.assistant'}
default	11:27:32.664714-0500	runningboardd	[app<application.com.nexy.assistant.21576034.21576040(501)>:2761] Ignoring memory limit update because this process is not memory-managed
default	11:27:32.664421-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	11:27:32.664784-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 200 flag 0x1 < Hijack > app com.nexy.assistant CID 0x218B0001 category Not set
default	11:27:32.673588-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	11:27:32.673674-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	11:27:32.675518-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:27:32.675529-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:27:32.675538-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	11:27:32.675544-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:27:32.675566-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	11:27:32.675602-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	11:27:32.675724-0500	ControlCenter	Navigating to new application [com.nexy.assistant]
default	11:27:34.922945-0500	audioaccessoryd	AudioStateSnapshot: Route:Bluetooth App com.nexy.assistant, Score 200, Remote 0NumofApp 1
default	11:27:35.662590-0500	Nexy	NotifyToken::RegisterDispatch(user.uid.501.com.apple.LaunchServices.database) fired for session key <private>
default	11:27:36.793190-0500	Nexy	LSExceptions shared instance invalidated for timeout.
default	11:27:37.922907-0500	audioaccessoryd	AudioStateSnapshot: Route:Bluetooth App com.nexy.assistant, Score 200, Remote 0NumofApp 1
default	11:27:40.922859-0500	audioaccessoryd	AudioStateSnapshot: Route:Bluetooth App com.nexy.assistant, Score 200, Remote 0NumofApp 1
default	11:27:41.641999-0500	coreaudiod	IssueReporting.cpp:492   RTAID [ use_case=Generic report_type=RMS Generic Chain clientID=ADM node=ADM::com.nexy.assistant_5728.5639.0_airpods noise suppression studio::in-0 issue_detected_sample_time=0.000000 ] -- [ rms:[-38.299797], peaks:[-18.846317] ]
default	11:27:41.644156-0500	coreaudiod	IssueReporting.cpp:492   RTAID [ use_case=Generic report_type=RMS Generic Chain clientID=ADM node=ADM::com.nexy.assistant_5728.5639.0_airpods noise suppression studio::out-0 issue_detected_sample_time=240000.000000 ] -- [ rms:[-38.393181], peaks:[-14.356901] ]
default	11:27:43.922909-0500	audioaccessoryd	AudioStateSnapshot: Route:Bluetooth App com.nexy.assistant, Score 200, Remote 0NumofApp 1
default	11:27:45.688009-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xb}
default	11:27:45.688544-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1c5042","name":"Nexy(2761)"}, "details":{"deviceUIDs":[],"implicit_category":"","input_running":false,"output_running":false} }
default	11:27:45.688785-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 67, PID = 2761, Name = sid:0x1c5042, Nexy(2761), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	11:27:45.688899-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 67, PID = 2761, Name = sid:0x1c5042, Nexy(2761), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	11:27:45.688981-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1c5042, Nexy(2761), 'prim'', displayID:'com.nexy.assistant'}
default	11:27:45.689100-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	11:27:45.689100-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1c5042, Nexy(2761), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 67 stopping recording
default	11:27:45.689158-0500	audiomxd	-MXCoreSession- -[MXCoreSession endInterruption:]: Session <ID: 67, PID = 2761, Name = sid:0x1c5042, Nexy(2761), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> is going inactive
default	11:27:45.689224-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 67, PID = 2761, Name = sid:0x1c5042, Nexy(2761), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	11:27:45.689317-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 67, PID = 2761, Name = sid:0x1c5042, Nexy(2761), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	11:27:45.689529-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 0]. BT device UIDS: {(
)}
default	11:27:45.689615-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 200 flag 0x1 < Hijack > app com.nexy.assistant CID 0x218B0001 category Not set
default	11:27:45.689548-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	11:27:45.693593-0500	runningboardd	Invalidating assertion 397-332-135433 (target:[app<application.com.nexy.assistant.21576034.21576040(501)>:2761]) from originator [osservice<com.apple.powerd>:332]
default	11:27:45.695303-0500	audiomxd	UpdateAudioState CID 0x218B0001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	11:27:45.695414-0500	audiomxd	UpdateAudioState CID 0x218B0001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	11:27:45.695518-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	11:27:45.695588-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	11:27:45.695621-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	11:27:45.695666-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	11:27:45.695818-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	11:27:45.695849-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	11:27:45.695877-0500	audioaccessoryd	AudioStateChanged: Removed audio session app com.nexy.assistant 201 count 0
default	11:27:45.698297-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	11:27:45.701826-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:27:45.701843-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:27:45.701858-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	11:27:45.701869-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:27:45.701879-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	11:27:45.701888-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	11:27:45.702032-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	11:27:45.790066-0500	Nexy	                AUHAL.cpp:473   ~AUHAL: (0xa56760740) Selecting device 0 from destructor
default	11:27:45.790092-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0xa56760740)
default	11:27:45.790103-0500	Nexy	                AUHAL.cpp:676   SelectDevice: (0xa56760740) not already running
default	11:27:45.790115-0500	Nexy	                AUHAL.cpp:682   SelectDevice: (0xa56760740) disconnecting device 91
default	11:27:45.790129-0500	Nexy	                AUHAL.cpp:746   SelectDevice: (0xa56760740) destroying ioproc 0xb for device 91
default	11:27:45.790204-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xb}
default	11:27:45.790275-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	11:27:45.790549-0500	Nexy	                AUHAL.cpp:848   SelectDevice: (0xa56760740) nothing to setup
default	11:27:45.790570-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0xa56760740) adding 0 device listeners to device 0
default	11:27:45.790577-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0xa56760740) adding 0 device delegate listeners to device 0
default	11:27:45.790585-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0xa56760740) removing 7 device listeners from device 91
default	11:27:45.790822-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0xa56760740) removing 0 device delegate listeners from device 91
default	11:27:45.790839-0500	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0xa56760740)
default	11:27:45.798829-0500	runningboardd	[app<application.com.nexy.assistant.21576034.21576040(501)>:2761] Ignoring jetsam update because this process is not memory-managed
default	11:27:45.798846-0500	runningboardd	[app<application.com.nexy.assistant.21576034.21576040(501)>:2761] Ignoring suspend because this process is not lifecycle managed
default	11:27:45.798858-0500	runningboardd	[app<application.com.nexy.assistant.21576034.21576040(501)>:2761] Ignoring GPU update because this process is not GPU managed
default	11:27:45.798878-0500	runningboardd	[app<application.com.nexy.assistant.21576034.21576040(501)>:2761] Ignoring memory limit update because this process is not memory-managed
default	11:27:45.802294-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.21576034.21576040(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	11:27:45.802951-0500	gamepolicyd	Received state update for 2761 (app<application.com.nexy.assistant.21576034.21576040(501)>, running-active-NotVisible
default	11:27:45.809045-0500	Nexy	[0xa576c9540] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	11:27:45.810338-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=2761.4, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=2761, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	11:27:45.812074-0500	tccd	AUTHREQ_SUBJECT: msgID=2761.4, subject=com.nexy.assistant,
default	11:27:45.813051-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa5f976d00 at /Applications/Nexy.app
default	11:27:45.830631-0500	tccd	Notifying for access  kTCCServiceListenEvent for target PID[2761], responsiblePID[2761], responsiblePath: /Applications/Nexy.app to UID: 501
default	11:27:45.830965-0500	Nexy	[0xa576c9540] invalidated after the last release of the connection object
default	11:27:45.914623-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa5f976400 at /Applications/Nexy.app
default	11:27:45.932574-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa5f977c00 at /Applications/Nexy.app
default	11:27:45.937262-0500	tccd	Publishing <TCCDEvent: type=Modify, service=kTCCServiceListenEvent, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 0 subscribers: {
}
default	11:27:47.916377-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(5727)
default	11:27:47.916408-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:5727 called from <private>
default	11:27:47.916414-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:5727 called from <private>
default	11:27:47.916870-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(5728)
default	11:27:47.916888-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:5728 called from <private>
default	11:27:47.916894-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:5728 called from <private>
default	11:27:47.921204-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:5727 called from <private>
default	11:27:47.921221-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:5727 called from <private>
default	11:27:47.921344-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(5727)
default	11:27:47.921363-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:5727 called from <private>
default	11:27:47.921370-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:5727 called from <private>
default	11:27:47.925338-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(5727)
default	11:27:47.925689-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(5727)
default	11:27:47.925720-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(5727)
default	11:27:47.927896-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:5727 called from <private>
default	11:27:47.927912-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:5727 called from <private>
default	11:27:47.927934-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:5727 called from <private>
default	11:27:47.927944-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:5727 called from <private>
default	11:27:47.927952-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:5727 called from <private>
default	11:27:47.927958-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:5727 called from <private>
default	11:27:47.927963-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:5727 called from <private>
default	11:27:47.927999-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:5727 called from <private>
default	11:27:47.928478-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(5728)
default	11:27:47.928812-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:5728 called from <private>
default	11:27:47.928863-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:5728 called from <private>
default	11:27:47.929610-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:5727 called from <private>
default	11:27:47.929640-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:5727 called from <private>
default	11:27:47.930672-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(5727)
default	11:27:47.938065-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:5727 called from <private>
default	11:27:47.938082-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:5727 called from <private>
default	11:27:47.938149-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(5727)
default	11:27:47.940773-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(5727)
default	11:27:47.940917-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:5727 called from <private>
default	11:27:47.940927-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:5727 called from <private>
default	11:27:47.941014-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(5727)
default	11:27:47.946906-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:5727 called from <private>
default	11:27:47.946969-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:5727 called from <private>
default	11:27:47.947062-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:5727 called from <private>
default	11:27:47.947098-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:5727 called from <private>
default	11:27:47.947138-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:5727 called from <private>
default	11:27:52.936307-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa5f974300 at /Applications/Nexy.app
default	11:27:52.954518-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa5f976400 at /Applications/Nexy.app
default	11:27:52.964581-0500	tccd	Publishing <TCCDEvent: type=Modify, service=kTCCServiceListenEvent, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 0 subscribers: {
}
default	11:27:58.838639-0500	Nexy	[0xa576c9540] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	11:27:58.840440-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=2761.5, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=2761, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	11:27:58.843354-0500	tccd	AUTHREQ_SUBJECT: msgID=2761.5, subject=com.nexy.assistant,
default	11:27:58.844739-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa5f974000 at /Applications/Nexy.app
default	11:27:58.868093-0500	tccd	Notifying for access  kTCCServiceScreenCapture for target PID[2761], responsiblePID[2761], responsiblePath: /Applications/Nexy.app to UID: 501
default	11:27:58.868659-0500	Nexy	[0xa576c9540] invalidated after the last release of the connection object
default	11:27:58.924596-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa5f974300 at /Applications/Nexy.app
default	11:27:58.941939-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa5f977300 at /Applications/Nexy.app
default	11:27:58.946296-0500	tccd	Publishing <TCCDEvent: type=Modify, service=kTCCServiceScreenCapture, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 0 subscribers: {
}
default	11:28:01.798219-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa5f974300 at /Applications/Nexy.app
default	11:28:01.815347-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa5f975500 at /Applications/Nexy.app
default	11:28:01.825078-0500	tccd	Publishing <TCCDEvent: type=Modify, service=kTCCServiceScreenCapture, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 0 subscribers: {
}
default	11:28:12.407643-0500	audiomxd	  ServerSessionManager.mm:472   { "action":"destroy_session", "session":{"ID":"0x1c5042","name":"Nexy(2761)"}, "details":null }
default	11:28:12.407701-0500	audiomxd	AudioApplicationInfoImpl.mm:690   Successfully removed session 0x1c5042 from AudioApp, recording state unchanged (app: {"name":"[implicit] Nexy","pid":2761})
default	11:28:12.407712-0500	audiomxd	  ServerSessionManager.mm:1081  destroy audio app instance since was created implicitly by session creation and all sessions now gone (audio app: {"name":"[implicit] Nexy","pid":2761})
default	11:28:12.408119-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 67, PID = 2761, Name = sid:0x1c5042, Nexy(2761), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	11:28:12.408366-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 67, PID = 2761, Name = sid:0x1c5042, Nexy(2761), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	11:28:12.408539-0500	audiomxd	UpdateAudioState CID 0x218B0001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	11:28:12.408662-0500	audiomxd	UpdateAudioState CID 0x218B0001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	11:28:12.406438-0500	WindowServer	0[outside of RPC]: Process death: 0x0-0x3f83f8 (Nexy) connectionID: ED8AB pid: 2761 in session 0x101
default	11:28:12.406527-0500	WindowServer	<BSCompoundAssertion:0x7c9011500> ([FocusManager:257]-deferringPolicyEvaluationSuppression) acquire for reason:process death - 0x0-0x3f83f8 (Nexy) acq:0x7c6a02da0 count:1
default	11:28:12.408778-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	11:28:12.408843-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	11:28:12.408858-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	11:28:12.409544-0500	WindowServer	0[outside of RPC]: [FocusManager:257] update to deferring policy requested for reason: permitted list updated - 0x0-0x3f83f8 removed - but we are suppressing evaluation for reasons: {(
    "process death - 0x0-0x3f83f8 (Nexy)"
)}
default	11:28:12.409823-0500	WindowServer	0[outside of RPC]: [FocusManager:257] update to deferring policy requested for reason: permitted list updated - 0x1-0xac9 removed - but we are suppressing evaluation for reasons: {(
    "process death - 0x0-0x3f83f8 (Nexy)"
)}
default	11:28:12.414417-0500	runningboardd	XPC connection invalidated: [app<application.com.nexy.assistant.21576034.21576040(501)>:2761]
default	11:28:12.415771-0500	coreaudiod	>>> NEGOTIATE [com.nexy.assistant]
default	11:28:12.416090-0500	coreaudiod	<<< NEGOTIATE [com.nexy.assistant]
default	11:28:12.417136-0500	coreaudiod	IssueReporting.cpp:492   RTAID [ use_case=Generic report_type=RMS Generic Chain clientID=ADM node=ADM::com.nexy.assistant_5728.5639.0_airpods noise suppression studio::out-0 issue_detected_sample_time=336960.000000 ] -- [ rms:[-40.646893], peaks:[-16.972660] ]
default	11:28:12.417166-0500	coreaudiod	IssueReporting.cpp:492   RTAID [ use_case=Generic report_type=RMS Generic Chain clientID=ADM node=ADM::com.nexy.assistant_5728.5639.0_airpods noise suppression studio::in-0 issue_detected_sample_time=0.000000 ] -- [ rms:[-41.423210], peaks:[-23.010017] ]
default	11:28:12.418751-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	11:28:12.422790-0500	kernel	Nexy[2761] triggered unnest of range 0x1f6000000->0x1f8000000 of DYLD shared region in VM map 0x664b2dcf2f27720f. While not abnormal for debuggers, this increases system memory footprint until the target exits.
default	11:28:12.422807-0500	kernel	Nexy[2761] triggered unnest of range 0x1f8000000->0x1fa000000 of DYLD shared region in VM map 0x664b2dcf2f27720f. While not abnormal for debuggers, this increases system memory footprint until the target exits.
default	11:28:12.483342-0500	Nexy	[0x105d6b040] activating connection: mach=true listener=false peer=false name=com.apple.cfprefsd.daemon
default	11:28:12.483416-0500	Nexy	[0x105d6b580] activating connection: mach=true listener=false peer=false name=com.apple.cfprefsd.agent
error	11:28:12.610455-0500	Nexy	dlsym cannot find symbol NSMakeRect in CFBundle 0x992f24000 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	11:28:12.610682-0500	Nexy	dlsym cannot find symbol NSMakePoint in CFBundle 0x992f24000 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	11:28:12.610888-0500	Nexy	dlsym cannot find symbol NSMakeSize in CFBundle 0x992f24000 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	11:28:12.611088-0500	Nexy	dlsym cannot find symbol NSMakeRange in CFBundle 0x992f24000 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
default	11:28:12.612232-0500	Nexy	[0x105d58280] activating connection: mach=true listener=false peer=false name=com.apple.coreservices.launchservicesd
default	11:28:12.613043-0500	Nexy	[0x99338c000] activating connection: mach=true listener=false peer=false name=com.apple.analyticsd
default	11:28:12.613352-0500	Nexy	[0x99338c140] activating connection: mach=true listener=false peer=false name=com.apple.pasteboard.1
default	11:28:12.613795-0500	Nexy	[0x99338c280] activating connection: mach=true listener=false peer=false name=com.apple.distributed_notifications@Uv3
default	11:28:12.615797-0500	Nexy	void _NSDisableAutomaticTerminationAndLog(NSString *) No windows open yet
default	11:28:12.616137-0500	Nexy	[0x99338c3c0] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	11:28:12.616828-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=2761.1, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=2761, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	11:28:12.618537-0500	tccd	AUTHREQ_SUBJECT: msgID=2761.1, subject=com.nexy.assistant,
default	11:28:12.619167-0500	Nexy	Received configuration update from daemon (initial)
default	11:28:12.619220-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa5f977c00 at /Applications/Nexy.app
default	11:28:12.633444-0500	Nexy	[0x99338c3c0] invalidated after the last release of the connection object
default	11:28:12.633799-0500	Nexy	server port 0x0000330f, session port 0x0000330f
default	11:28:12.634861-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=391.2244, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=2761, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=391, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	11:28:12.634888-0500	tccd	requestor: TCCDProcess: identifier=com.apple.WindowServer, pid=391, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=2761, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	11:28:12.635824-0500	tccd	AUTHREQ_SUBJECT: msgID=391.2244, subject=com.nexy.assistant,
default	11:28:12.636506-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa5f977c00 at /Applications/Nexy.app
default	11:28:12.652240-0500	Nexy	New connection 0xefff3 main
default	11:28:12.654576-0500	Nexy	CHECKIN: pid=2761
default	11:28:12.660593-0500	launchservicesd	CHECKIN:0x0-0x3f83f8 2761 com.nexy.assistant
default	11:28:12.660707-0500	Nexy	CHECKEDIN: pid=2761 asn=0x0-0x3f83f8 foreground=0
default	11:28:12.660973-0500	Nexy	[0x99338c3c0] activating connection: mach=false listener=true peer=false name=(anonymous)
default	11:28:12.660984-0500	Nexy	[0x99338c3c0] Connection returned listener port: 0x4f03
default	11:28:12.661231-0500	Nexy	[0x992f6c300] activating connection: mach=false listener=false peer=true name=com.apple.xpc.anonymous.0x99338c3c0.peer[361].0x992f6c300
default	11:28:12.661499-0500	loginwindow	-[Application updateInformation] | Got App URL: file:///Applications/Nexy.app/
default	11:28:12.661624-0500	loginwindow	-[ApplicationManager checkInAppContext:eventData:] | ApplicationManager: Checked in app : Nexy
default	11:28:12.662118-0500	Nexy	FRONTLOGGING: version 1
default	11:28:12.662126-0500	Nexy	Registered, pid=2761 ASN=0x0,0x3f83f8
default	11:28:12.662314-0500	WindowServer	efff3[CreateApplication]: Process creation: 0x0-0x3f83f8 (Nexy) connectionID: EFFF3 pid: 2761 in session 0x101
default	11:28:12.662765-0500	Nexy	[0x99338c500] activating connection: mach=true listener=false peer=false name=com.apple.lsd.mapdb
default	11:28:12.663300-0500	Nexy	[0x99338c3c0] Connection returned listener port: 0x4f03
default	11:28:12.663682-0500	Nexy	BringForward: pid=2761 asn=0x0-0x3f83f8 bringForward=0 foreground=0 uiElement=1 launchedByLS=1 modifiersCount=1 allDisabled=0
default	11:28:12.663707-0500	Nexy	BringFrontModifier: pid=2761 asn=0x0-0x3f83f8 Modifier 0 hideAfter=0 hideOthers=0 dontMakeFrontmost=0 mouseDown=0/0 seed=0/0
default	11:28:12.664288-0500	Nexy	Current system appearance, (HLTB: 1), (SLS: 0)
default	11:28:12.666529-0500	Nexy	No persisted cache on this platform.
default	11:28:12.673369-0500	Nexy	Current system appearance, (HLTB: 1), (SLS: 0)
default	11:28:12.674207-0500	Nexy	Post-registration system appearance: (HLTB: 1)
default	11:28:12.676316-0500	Nexy	FBSWorkspace: endpoint monitoring is disabled.
default	11:28:12.676326-0500	Nexy	FBSWorkspace: default shell endpoint is disabled.
default	11:28:12.676389-0500	Nexy	Initializing connection
default	11:28:12.676434-0500	Nexy	Removing all cached process handles
default	11:28:12.676460-0500	Nexy	Sending handshake request attempt #1 to server
default	11:28:12.676471-0500	Nexy	Creating connection to com.apple.runningboard
default	11:28:12.676481-0500	Nexy	[0x99338c640] activating connection: mach=true listener=false peer=false name=com.apple.runningboard
default	11:28:12.676951-0500	runningboardd	Setting client for [app<application.com.nexy.assistant.21576034.21576040(501)>:2761] as ready
default	11:28:12.676995-0500	Nexy	[0x99338c3c0] Connection returned listener port: 0x4f03
default	11:28:12.677578-0500	Nexy	Handshake succeeded
default	11:28:12.677597-0500	Nexy	Identity resolved as app<application.com.nexy.assistant.21576034.21576040(501)>
default	11:28:12.677898-0500	distnoted	register name: com.apple.xctest.FakeForceTouchDevice object: com.nexy.assistant token: 1e0000001d pid: 2761
default	11:28:12.680675-0500	Nexy	[0x99338c3c0] Connection returned listener port: 0x4f03
default	11:28:12.693764-0500	Nexy	Created a new Process Instance Registry XPC connection (inactive)
default	11:28:12.693789-0500	Nexy	[0x99338c8c0] activating connection: mach=true listener=false peer=false name=com.apple.linkd.autoShortcut
default	11:28:12.693901-0500	Nexy	Activated connection to com.apple.linkd.autoShortcut (ApplicationService)
default	11:28:12.693950-0500	Nexy	[0x99338ca00] activating connection: mach=false listener=true peer=false name=(anonymous)
default	11:28:12.695745-0500	Nexy	[0x99338ca00] Connection returned listener port: 0x7003
default	11:28:12.696438-0500	Nexy	Registered process with identifier 2761-228140
default	11:28:12.821314-0500	Nexy	Registered notify signal com.apple.caulk.alloc.rtdump (0)
default	11:28:12.824098-0500	Nexy	System_Input_Processing_Notification_Handler.mm:456   System_Input_Processing_Notification_Handler::is_vi_available(): Voice isolation DSP is available for client with bundle id com.nexy.assistant (AVFoundation is available, application is not in client deny list, application is not FaceTime variant)
default	11:28:12.825481-0500	Nexy	[0x99338cb40] activating connection: mach=true listener=false peer=false name=com.apple.cmio.registerassistantservice.system-extensions
default	11:28:12.827467-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOInitializeListenersForBundleID: for <private> -> <private>
default	11:28:12.828988-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> vpio_preferenceChangedListener: new value ((null)) for key AUVoiceIOClients/com-nexy-assistant/AUVoiceIOChatFlavor, translatedBundleID com.nexy.assistant, bundleIDs {(
    "com.nexy.assistant"
)}
default	11:28:12.829145-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> vpio_preferenceChangedListener: new value ((null)) for key AUVoiceIOClients/com-nexy-assistant/AUVoiceIOIsAutoChatFlavorEnabled, translatedBundleID com.nexy.assistant, bundleIDs {(
    "com.nexy.assistant"
)}
default	11:28:12.829277-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetSupportedChatFlavorsForBundleID: <private>-><private> get supported chat flavors: <private>
default	11:28:12.829288-0500	Nexy	            HALSystem.cpp:134    Enabling HAL Voice Isolation support
default	11:28:12.829317-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetHiddenChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	11:28:12.829454-0500	Nexy	[0x99338cc80] activating connection: mach=true listener=false peer=false name=com.apple.tccd
default	11:28:12.829654-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOHiddenChatFlavors newValue: (
    1
)
default	11:28:12.829998-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=2761.2, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=2761, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	11:28:12.835766-0500	tccd	AUTHREQ_SUBJECT: msgID=2761.2, subject=com.nexy.assistant,
default	11:28:12.836361-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc128d8900 at /Applications/Nexy.app
default	11:28:12.848488-0500	Nexy	[0x99338cc80] invalidated after the last release of the connection object
default	11:28:12.848623-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetPreferredChatFlavorForBundleID: <private>-><private> get value: 0
default	11:28:12.848659-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetSupportedChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	11:28:12.848934-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOSupportedChatFlavors newValue: (
    0,
    2
)
default	11:28:12.850181-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=404.1214, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=2761, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=392, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	11:28:12.850935-0500	tccd	AUTHREQ_SUBJECT: msgID=404.1214, subject=com.nexy.assistant,
default	11:28:12.851479-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc128d8900 at /Applications/Nexy.app
error	11:28:12.863560-0500	tccd	Request message contains a target_token to accessing_process (TCCDProcess: identifier=com.nexy.assistant, pid=2761, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy) but TCCDProcess: identifier=com.apple.audio.coreaudiod, pid=404, auid=202, euid=202, binary_path=/usr/sbin/coreaudiod is not a TCC manager for service: kTCCServiceScreenCapture.
default	11:28:12.864445-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=404.1216, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=2761, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=392, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	11:28:12.865171-0500	tccd	AUTHREQ_SUBJECT: msgID=404.1216, subject=com.nexy.assistant,
default	11:28:12.865689-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc128d8900 at /Applications/Nexy.app
default	11:28:12.879215-0500	Nexy	  HALPlugInManagement.cpp:440    HALPlugInManagement::RegisterPlugIns: skipping in-process plug-ins
error	11:28:12.879231-0500	Nexy	AddInstanceForFactory: No factory registered for id <CFUUID 0x992e359e0> F8BB1C28-BAE8-11D6-9C31-00039315CD46
error	11:28:12.894220-0500	Nexy	         HALC_ProxyObjectMap.cpp:174   HALC_ProxyObjectMap::_CopyObjectByObjectID: failed to create the local object
error	11:28:12.894231-0500	Nexy	            HALC_ShellDevice.cpp:2673  HALC_ShellDevice::RebuildControlList: couldn't find the control object
default	11:28:12.896950-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	11:28:12.897084-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	11:28:12.901257-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetPreferredChatFlavorForBundleID: <private>-><private> get value: 0
default	11:28:14.352799-0500	kernel	SK[6]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 03D94FA0-B538-4A08-B402-20FCA8FA736C flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.56844,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0x7a9553e0 tp_proto=0x06"
default	11:28:14.352881-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:56844<-><IPv4-redacted>:53] interface: utun6 (skipped: 516)
so_gencnt: 748755 t_state: SYN_SENT process: Nexy:2761 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 1 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x840ec9eb
default	11:28:14.353612-0500	kernel	tcp connected: [<IPv4-redacted>:56844<-><IPv4-redacted>:53] interface: utun6 (skipped: 516)
so_gencnt: 748755 t_state: ESTABLISHED process: Nexy:2761 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 1 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x840ec9eb
default	11:28:14.354057-0500	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:56844<-><IPv4-redacted>:53] interface: utun6 (skipped: 516)
so_gencnt: 748755 t_state: FIN_WAIT_1 process: Nexy:2761 Duration: 0.002 sec Conn_Time: 0.001 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 1.000 ms rttvar: 0.500 ms base rtt: 1 ms so_error: 0 svc/tc: 0 flow: 0x840ec9eb
default	11:28:14.354067-0500	kernel	tcp_connection_summary [<IPv4-redacted>:56844<-><IPv4-redacted>:53] interface: utun6 (skipped: 516)
so_gencnt: 748755 t_state: FIN_WAIT_1 process: Nexy:2761 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	11:28:14.371541-0500	Nexy	[0x99338cc80] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioComponentRegistrar
default	11:28:14.383223-0500	Nexy	                AUHAL.cpp:420   AUHAL: (0x992064740) Selecting device 85 from constructor
default	11:28:14.383234-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0x992064740)
default	11:28:14.383240-0500	Nexy	                AUHAL.cpp:676   SelectDevice: (0x992064740) not already running
default	11:28:14.383244-0500	Nexy	                AUHAL.cpp:752   SelectDevice: (0x992064740) nothing to teardown
default	11:28:14.383248-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0x992064740) connecting device 85
default	11:28:14.383347-0500	Nexy	                AUHAL.cpp:3413  IsDeviceUsable: (0x992064740) Device ID: 85 (Input:No | Output:Yes): true
default	11:28:14.383440-0500	Nexy	                AUHAL.cpp:769   SelectDevice: (0x992064740) created ioproc 0xa for device 85
default	11:28:14.383526-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x992064740) adding 7 device listeners to device 85
default	11:28:14.383675-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x992064740) adding 0 device delegate listeners to device 85
default	11:28:14.383682-0500	Nexy	                AUHAL.cpp:1581  UpdateStreamFormats: -> (0x992064740)
default	11:28:14.383744-0500	Nexy	                AUHAL.cpp:1677  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  48000 Hz, Float32, interleaved
default	11:28:14.383754-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 1 output streams; not all mono
default	11:28:14.383759-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	11:28:14.383764-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 0 input streams; not all mono
default	11:28:14.383771-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	11:28:14.383857-0500	Nexy	                AUHAL.cpp:1771  UpdateStreamFormats: AUHAL(0x992064740) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	11:28:14.383867-0500	Nexy	                AUHAL.cpp:1777  UpdateStreamFormats: AUHAL(0x992064740) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	11:28:14.383873-0500	Nexy	                AUHAL.cpp:1787  UpdateStreamFormats: <-
default	11:28:14.383877-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x992064740) removing 0 device listeners from device 0
default	11:28:14.383882-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x992064740) removing 0 device delegate listeners from device 0
default	11:28:14.383893-0500	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0x992064740)
default	11:28:14.383908-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Output stream enables: Stream 0 is DISABLED
default	11:28:14.383991-0500	Nexy	                AUHAL.cpp:2298  SetProperty: (0x992064740) caller requesting device change from 85 to 91
default	11:28:14.384000-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0x992064740)
default	11:28:14.384005-0500	Nexy	                AUHAL.cpp:676   SelectDevice: (0x992064740) not already running
default	11:28:14.384010-0500	Nexy	                AUHAL.cpp:682   SelectDevice: (0x992064740) disconnecting device 85
default	11:28:14.384015-0500	Nexy	                AUHAL.cpp:746   SelectDevice: (0x992064740) destroying ioproc 0xa for device 85
default	11:28:14.384072-0500	Nexy	  AVAudioSession_MacOS.mm:1021  initForMacOS
default	11:28:14.384541-0500	Nexy	[0x99338cf00] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioSession
default	11:28:14.385467-0500	audiomxd	  ServerSessionManager.mm:315   { "action":"create_session", "session":{"ID":"0x1c5043","name":"Nexy(2761)"}, "details":{"PID":2761,"session_type":"Primary"} }
default	11:28:14.385545-0500	audiomxd	AudioApplicationInfoImpl.mm:250   Setting initial isRecording state: 0 for newly-created AudioApp
	app: {"name":"[implicit] Nexy","pid":2761}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1c5043, sessionType: 'prim', isRecording: false }, 
]
default	11:28:14.385876-0500	Nexy	    SessionCore_Create.mm:99    Created session 0x9932852a0 with ID: 0x1c5043
default	11:28:14.386430-0500	Nexy	[0x99338d040] activating connection: mach=true listener=false peer=false name=com.apple.audioanalyticsd
error	11:28:14.386832-0500	Nexy	Reporter disconnected. { function=sendMessage, reporterID=11858404704257 }
default	11:28:14.386847-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped Unknown {1C-77-54-18-C8-A3:output, 0xa}
default	11:28:14.386894-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	11:28:14.386976-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0x992064740) connecting device 91
default	11:28:14.387051-0500	Nexy	                AUHAL.cpp:3413  IsDeviceUsable: (0x992064740) Device ID: 91 (Input:Yes | Output:No): true
default	11:28:14.388501-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=404.1217, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=2761, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=392, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	11:28:14.389890-0500	tccd	AUTHREQ_SUBJECT: msgID=404.1217, subject=com.nexy.assistant,
default	11:28:14.390525-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc128d8900 at /Applications/Nexy.app
default	11:28:14.403975-0500	Nexy	                AUHAL.cpp:769   SelectDevice: (0x992064740) created ioproc 0xa for device 91
default	11:28:14.404107-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x992064740) adding 7 device listeners to device 91
default	11:28:14.404268-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x992064740) adding 0 device delegate listeners to device 91
default	11:28:14.404274-0500	Nexy	                AUHAL.cpp:1581  UpdateStreamFormats: -> (0x992064740)
default	11:28:14.404280-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 0 output streams; not all mono
default	11:28:14.404290-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Output render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	11:28:14.404408-0500	Nexy	                AUHAL.cpp:1677  UpdateStreamFormats: 
  input stream 0 [0x5c]:  1 ch,  24000 Hz, Float32
default	11:28:14.404414-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 1 input streams; all mono
default	11:28:14.404419-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Input render format:  1 ch,  24000 Hz, Float32
default	11:28:14.404501-0500	Nexy	                AUHAL.cpp:1771  UpdateStreamFormats: AUHAL(0x992064740) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	11:28:14.404510-0500	Nexy	                AUHAL.cpp:1777  UpdateStreamFormats: AUHAL(0x992064740) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	11:28:14.404514-0500	Nexy	                AUHAL.cpp:1787  UpdateStreamFormats: <-
default	11:28:14.404520-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x992064740) removing 7 device listeners from device 85
default	11:28:14.404680-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x992064740) removing 0 device delegate listeners from device 85
default	11:28:14.404689-0500	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0x992064740)
default	11:28:14.405272-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	11:28:14.406219-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=404.1218, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=2761, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=392, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	11:28:14.407026-0500	tccd	AUTHREQ_SUBJECT: msgID=404.1218, subject=com.nexy.assistant,
default	11:28:14.407589-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc128d8900 at /Applications/Nexy.app
default	11:28:14.419652-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	11:28:14.420591-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=404.1219, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=2761, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=392, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	11:28:14.421514-0500	tccd	AUTHREQ_SUBJECT: msgID=404.1219, subject=com.nexy.assistant,
default	11:28:14.422055-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc128d8900 at /Applications/Nexy.app
default	11:28:14.434756-0500	Nexy	Registered notify signal com.apple.caulk.alloc.audiodump (0)
default	11:28:14.436122-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=404.1220, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=2761, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=392, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	11:28:14.436892-0500	tccd	AUTHREQ_SUBJECT: msgID=404.1220, subject=com.nexy.assistant,
default	11:28:14.437418-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc128d8900 at /Applications/Nexy.app
default	11:28:14.449908-0500	coreaudiod	>>> NEGOTIATE [com.nexy.assistant]
default	11:28:14.450066-0500	coreaudiod	<<< NEGOTIATE [com.nexy.assistant]
default	11:28:14.450784-0500	coreaudiod	>>> ADAPT [com.nexy.assistant]
default	11:28:14.451059-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xc50bf2400] Created node ADM::com.nexy.assistant_5740.5639.0_airpods noise suppression studio::in-0 with nodeID 0 - reporting period = 10.000000, sample rate = 24000.000000
default	11:28:14.451124-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xc50bf2400] Created node ADM::com.nexy.assistant_5740.5639.0_airpods noise suppression studio::out-0 with nodeID 1 - reporting period = 10.000000, sample rate = 24000.000000
default	11:28:14.519972-0500	coreaudiod	<<< ADAPT [com.nexy.assistant]
default	11:28:14.521790-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:5740 called from <private>
default	11:28:14.521848-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Input {1C-77-54-18-C8-A3:input, 0xa}
default	11:28:14.522815-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:5740 called from <private>
default	11:28:14.523004-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(5740)
default	11:28:14.523025-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:5740 called from <private>
default	11:28:14.523030-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:5740 called from <private>
default	11:28:14.523607-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(5739)
default	11:28:14.523621-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:5739 called from <private>
default	11:28:14.523895-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:5739 called from <private>
default	11:28:14.525985-0500	runningboardd	ignoring [app<application.com.nexy.assistant.21576034.21576040(501)>:2761] as candidate for concrete target as it is terminating
default	11:28:14.528373-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
fault	11:28:14.528956-0500	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.21576034.21576040 AUID=501> and <type=Application identifier=application.com.nexy.assistant.21576034.21576040>
default	11:28:14.529422-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	11:28:14.535497-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(5740)
default	11:28:14.535515-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(5740)
default	11:28:14.535520-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:5740 called from <private>
default	11:28:14.535526-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(5740)
default	11:28:14.535530-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:5740 called from <private>
default	11:28:14.535538-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:5740 called from <private>
default	11:28:14.535545-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:5740 called from <private>
default	11:28:14.535594-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:5740 called from <private>
default	11:28:14.535604-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(5740)
default	11:28:14.535618-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:5740 called from <private>
default	11:28:14.535682-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:5740 called from <private>
default	11:28:14.538964-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1c5043","name":"Nexy(2761)"}, "details":{"deviceUIDs":["1C-77-54-18-C8-A3:input"],"implicit_category":"Record","input_running":true,"output_running":false} }
default	11:28:14.535723-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:5740 called from <private>
default	11:28:14.540065-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 68, PID = 2761, Name = sid:0x1c5043, Nexy(2761), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	11:28:14.540262-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 68, PID = 2761, Name = sid:0x1c5043, Nexy(2761), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	11:28:14.541043-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 68, PID = 2761, Name = sid:0x1c5043, Nexy(2761), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	11:28:14.541134-0500	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1c5043, Nexy(2761), 'prim'', AudioCategory changed to 'Record_WithBluetooth'
default	11:28:14.541280-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 68, PID = 2761, Name = sid:0x1c5043, Nexy(2761), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	11:28:14.541295-0500	audiomxd	UpdateAudioState CID 0x218B0001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	11:28:14.542216-0500	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 68, PID = 2761, Name = sid:0x1c5043, Nexy(2761), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> is going active
default	11:28:14.542292-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1c5043, Nexy(2761), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 68 starting recording
default	11:28:14.542520-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 68, PID = 2761, Name = sid:0x1c5043, Nexy(2761), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	11:28:14.537441-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(5740)
default	11:28:14.542557-0500	audiomxd	UpdateAudioState CID 0x218B0001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	11:28:14.538281-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:5740 called from <private>
default	11:28:14.538382-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:5740 called from <private>
default	11:28:14.542684-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 68, PID = 2761, Name = sid:0x1c5043, Nexy(2761), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	11:28:14.538446-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:5740 called from <private>
default	11:28:14.542776-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1c5043, Nexy(2761), 'prim'', displayID:'com.nexy.assistant'}
default	11:28:14.539108-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(5739)
default	11:28:14.542978-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	11:28:14.541562-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	11:28:14.542690-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
fault	11:28:14.538223-0500	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.21576034.21576040 AUID=501> and <type=Application identifier=application.com.nexy.assistant.21576034.21576040>
default	11:28:14.540465-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=404.1221, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=2761, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=392, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	11:28:14.542979-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [1, 0]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:input"
)}
default	11:28:14.543018-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	11:28:14.547975-0500	tccd	AUTHREQ_SUBJECT: msgID=404.1221, subject=com.nexy.assistant,
default	11:28:14.549952-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:5739 called from <private>
default	11:28:14.549964-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:5739 called from <private>
default	11:28:14.550117-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:5739 called from <private>
default	11:28:14.550127-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:5739 called from <private>
default	11:28:14.550211-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(5739)
default	11:28:14.550071-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc128d8900 at /Applications/Nexy.app
default	11:28:14.557454-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(5739)
default	11:28:14.557658-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:5739 called from <private>
default	11:28:14.557667-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:5739 called from <private>
default	11:28:14.557773-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(5739)
default	11:28:14.562256-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(5739)
default	11:28:14.562505-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:5739 called from <private>
default	11:28:14.562514-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:5739 called from <private>
default	11:28:14.562571-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:5739 called from <private>
default	11:28:14.562580-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:5739 called from <private>
default	11:28:14.562587-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:5739 called from <private>
default	11:28:14.562592-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:5739 called from <private>
default	11:28:14.562599-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:5739 called from <private>
default	11:28:14.562644-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:5739 called from <private>
default	11:28:14.562711-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:5739 called from <private>
default	11:28:14.562767-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:5739 called from <private>
default	11:28:14.562832-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:5739 called from <private>
default	11:28:14.562946-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:5739 called from <private>
default	11:28:14.563035-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:5739 called from <private>
default	11:28:14.563102-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:5739 called from <private>
default	11:28:14.563292-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(5739)
default	11:28:14.563308-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:5739 called from <private>
default	11:28:14.563354-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:5739 called from <private>
default	11:28:14.592261-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:28:14.592279-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:28:14.592294-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	11:28:14.592360-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:28:14.592401-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	11:28:14.592428-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	11:28:14.608582-0500	coreaudiod	>>> ADAPT [com.nexy.assistant]
default	11:28:14.610450-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xc50bf2400] Created node ADM::com.nexy.assistant_5740.5639.0_airpods noise suppression studio::in-0 with nodeID 0 - reporting period = 10.000000, sample rate = 24000.000000
default	11:28:14.610515-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xc50bf2400] Created node ADM::com.nexy.assistant_5740.5639.0_airpods noise suppression studio::out-0 with nodeID 1 - reporting period = 10.000000, sample rate = 24000.000000
default	11:28:14.647861-0500	coreaudiod	<<< ADAPT [com.nexy.assistant]
default	11:28:14.648694-0500	runningboardd	ignoring [app<application.com.nexy.assistant.21576034.21576040(501)>:2761] as candidate for concrete target as it is terminating
default	11:28:14.650712-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:5740 called from <private>
default	11:28:14.650742-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:5740 called from <private>
default	11:28:14.651072-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	11:28:14.652040-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:5740 called from <private>
default	11:28:14.652389-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(5740)
default	11:28:14.652406-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:5740 called from <private>
default	11:28:14.652414-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:5740 called from <private>
default	11:28:14.653322-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	11:28:14.653551-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	11:28:14.654016-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(5740)
default	11:28:14.654139-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:5740 called from <private>
default	11:28:14.654149-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:5740 called from <private>
default	11:28:14.654162-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:5740 called from <private>
default	11:28:14.655492-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=404.1223, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=2761, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=392, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	11:28:14.657094-0500	tccd	AUTHREQ_SUBJECT: msgID=404.1223, subject=com.nexy.assistant,
default	11:28:14.657748-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xc128d8900 at /Applications/Nexy.app
default	11:28:14.659018-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	11:28:14.659060-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	11:28:14.659094-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	11:28:14.659207-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	11:28:14.659710-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:28:14.659722-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:28:14.659730-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	11:28:14.659738-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:28:14.659756-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	11:28:14.659766-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	11:28:14.659955-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	11:28:14.676186-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:5740 called from <private>
default	11:28:14.676858-0500	runningboardd	ignoring [app<application.com.nexy.assistant.21576034.21576040(501)>:2761] as candidate for concrete target as it is terminating
default	11:28:14.682566-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	11:28:14.682625-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	11:28:14.682662-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	11:28:14.683166-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:28:14.683176-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:28:14.683185-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	11:28:14.683193-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:28:14.683199-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	11:28:14.683206-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	11:28:14.683259-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:28:14.683294-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:28:14.683326-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	11:28:14.683365-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:28:14.683428-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	11:28:14.683479-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	11:28:14.683473-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	11:28:14.683682-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:28:14.683690-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:28:14.683696-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	11:28:14.683702-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:28:14.683708-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	11:28:14.683749-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	11:28:14.683779-0500	ControlCenter	Navigating to new application [com.nexy.assistant]
default	11:28:15.703474-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xa}
default	11:28:15.703954-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1c5043","name":"Nexy(2761)"}, "details":{"deviceUIDs":[],"implicit_category":"","input_running":false,"output_running":false} }
default	11:28:15.704142-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 68, PID = 2761, Name = sid:0x1c5043, Nexy(2761), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	11:28:15.704221-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 68, PID = 2761, Name = sid:0x1c5043, Nexy(2761), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	11:28:15.704262-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1c5043, Nexy(2761), 'prim'', displayID:'com.nexy.assistant'}
default	11:28:15.704336-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	11:28:15.704344-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1c5043, Nexy(2761), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 68 stopping recording
default	11:28:15.704380-0500	audiomxd	-MXCoreSession- -[MXCoreSession endInterruption:]: Session <ID: 68, PID = 2761, Name = sid:0x1c5043, Nexy(2761), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> is going inactive
default	11:28:15.704430-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 68, PID = 2761, Name = sid:0x1c5043, Nexy(2761), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	11:28:15.704473-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 68, PID = 2761, Name = sid:0x1c5043, Nexy(2761), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	11:28:15.704639-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 0]. BT device UIDS: {(
)}
default	11:28:15.704655-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	11:28:15.704775-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 200 flag 0x1 < Hijack > app com.nexy.assistant CID 0x218B0001 category Not set
default	11:28:15.708865-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	11:28:15.708937-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	11:28:15.708969-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	11:28:15.708682-0500	audiomxd	UpdateAudioState CID 0x218B0001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	11:28:15.708996-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	11:28:15.708765-0500	audiomxd	UpdateAudioState CID 0x218B0001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	11:28:15.709124-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	11:28:15.709141-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	11:28:15.709161-0500	audioaccessoryd	AudioStateChanged: Removed audio session app com.nexy.assistant 201 count 0
default	11:28:15.712100-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	11:28:15.716084-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:28:15.716103-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:28:15.716119-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	11:28:15.716129-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:28:15.716139-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	11:28:15.716150-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	11:28:15.716389-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	11:28:15.805140-0500	Nexy	                AUHAL.cpp:473   ~AUHAL: (0x992064740) Selecting device 0 from destructor
default	11:28:15.805162-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0x992064740)
default	11:28:15.805175-0500	Nexy	                AUHAL.cpp:676   SelectDevice: (0x992064740) not already running
default	11:28:15.805182-0500	Nexy	                AUHAL.cpp:682   SelectDevice: (0x992064740) disconnecting device 91
default	11:28:15.805202-0500	Nexy	                AUHAL.cpp:746   SelectDevice: (0x992064740) destroying ioproc 0xa for device 91
default	11:28:15.805238-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xa}
default	11:28:15.805282-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	11:28:15.805493-0500	Nexy	                AUHAL.cpp:848   SelectDevice: (0x992064740) nothing to setup
default	11:28:15.805519-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x992064740) adding 0 device listeners to device 0
default	11:28:15.805538-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x992064740) adding 0 device delegate listeners to device 0
default	11:28:15.805550-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x992064740) removing 7 device listeners from device 91
default	11:28:15.805798-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x992064740) removing 0 device delegate listeners from device 91
default	11:28:15.805811-0500	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0x992064740)
default	11:28:15.940756-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=2794.1, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=2761, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.osascript, pid=2794, auid=501, euid=501, binary_path=/usr/bin/osascript}, },
default	11:28:15.942354-0500	tccd	AUTHREQ_SUBJECT: msgID=2794.1, subject=com.nexy.assistant,
default	11:28:15.942984-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa5f977c00 at /Applications/Nexy.app
default	11:28:15.958122-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=391.2245, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=2761, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.osascript, pid=2794, auid=501, euid=501, binary_path=/usr/bin/osascript}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=391, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	11:28:15.959146-0500	tccd	AUTHREQ_SUBJECT: msgID=391.2245, subject=com.nexy.assistant,
default	11:28:15.959760-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa5f977c00 at /Applications/Nexy.app
default	11:28:15.991983-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa5f975500 at /Applications/Nexy.app
default	11:28:16.011827-0500	System Events	TCCAccessRequestIndirect: TCCAccessRequestIndirect with pid 2767: target_identity: {
    kTCCCodeIdentityAuditToken = {length = 32, bytes = 0xf5010000 f5010000 14000000 f5010000 ... b9860100 2f7b0300 };
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
default	11:28:16.027431-0500	tccd	target_executable_path_URL: file:///Applications/Nexy.app/Contents/MacOS/Nexy
default	11:28:17.016647-0500	Nexy	[0x99338d400] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
error	11:28:17.017271-0500	tccd	TCCDProcess: identifier=com.nexy.assistant, pid=2761, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy attempted to call TCCAccessRequest for kTCCServiceAccessibility without the recommended com.apple.private.tcc.manager.check-by-audit-token entitlement
default	11:28:17.017448-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=2761.3, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=2761, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.nexy.assistant, pid=2761, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	11:28:17.018619-0500	tccd	AUTHREQ_SUBJECT: msgID=2761.3, subject=com.nexy.assistant,
default	11:28:17.019320-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa5f976400 at /Applications/Nexy.app
default	11:28:17.032429-0500	Nexy	[0x99338d400] invalidated after the last release of the connection object
default	11:28:17.032541-0500	Nexy	[0x99338d400] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
error	11:28:17.032949-0500	tccd	TCCDProcess: identifier=com.nexy.assistant, pid=2761, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy attempted to call TCCAccessRequest for kTCCServiceAccessibility without the recommended com.apple.private.tcc.manager.check-by-audit-token entitlement
default	11:28:17.033118-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=2761.4, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=2761, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.nexy.assistant, pid=2761, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	11:28:17.034053-0500	tccd	AUTHREQ_SUBJECT: msgID=2761.4, subject=com.nexy.assistant,
default	11:28:17.034737-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa5f976400 at /Applications/Nexy.app
default	11:28:17.047236-0500	Nexy	[0x99338d400] invalidated after the last release of the connection object
default	11:28:17.047302-0500	Nexy	[0x99338d400] activating connection: mach=true listener=false peer=false name=com.apple.universalaccessAuthWarn
default	11:28:17.047394-0500	Nexy	[0x99338d400] invalidated after the last release of the connection object
default	11:28:17.055529-0500	Nexy	server port 0x00010733, session port 0x0000330f
default	11:28:17.058257-0500	kernel	SK[6]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 9C0CEE88-F4A8-4C1A-A943-BD2C5942D263 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.56845,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0x3ec5558c tp_proto=0x06"
default	11:28:17.058336-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:56845<-><IPv4-redacted>:53] interface: utun6 (skipped: 516)
so_gencnt: 748756 t_state: SYN_SENT process: Nexy:2761 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 1 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xad386c38
default	11:28:17.058959-0500	kernel	tcp connected: [<IPv4-redacted>:56845<-><IPv4-redacted>:53] interface: utun6 (skipped: 516)
so_gencnt: 748756 t_state: ESTABLISHED process: Nexy:2761 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 1 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xad386c38
default	11:28:17.071419-0500	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:56845<-><IPv4-redacted>:53] interface: utun6 (skipped: 516)
so_gencnt: 748756 t_state: FIN_WAIT_1 process: Nexy:2761 Duration: 0.013 sec Conn_Time: 0.001 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 1.000 ms rttvar: 0.500 ms base rtt: 1 ms so_error: 0 svc/tc: 0 flow: 0xad386c38
default	11:28:17.071436-0500	kernel	tcp_connection_summary [<IPv4-redacted>:56845<-><IPv4-redacted>:53] interface: utun6 (skipped: 516)
so_gencnt: 748756 t_state: FIN_WAIT_1 process: Nexy:2761 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	11:28:17.071731-0500	kernel	SK[7]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 7B576C07-5B0A-4E03-84D1-CDFA013DA41D flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.56846,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0x82ec1157 tp_proto=0x06"
default	11:28:17.071760-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:56846<-><IPv4-redacted>:53] interface: utun6 (skipped: 516)
so_gencnt: 748757 t_state: SYN_SENT process: Nexy:2761 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 1 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xb5a61f96
default	11:28:17.072364-0500	Nexy	networkd_settings_read_from_file initialized networkd settings by reading plist directly
default	11:28:17.072488-0500	kernel	tcp connected: [<IPv4-redacted>:56846<-><IPv4-redacted>:53] interface: utun6 (skipped: 516)
so_gencnt: 748757 t_state: ESTABLISHED process: Nexy:2761 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 1 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xb5a61f96
default	11:28:17.072611-0500	Nexy	networkd_settings_read_from_file initialized networkd settings by reading plist directly
default	11:28:17.072683-0500	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:56846<-><IPv4-redacted>:53] interface: utun6 (skipped: 516)
so_gencnt: 748757 t_state: FIN_WAIT_1 process: Nexy:2761 Duration: 0.001 sec Conn_Time: 0.001 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 1.000 ms rttvar: 0.500 ms base rtt: 1 ms so_error: 0 svc/tc: 0 flow: 0xb5a61f96
default	11:28:17.072693-0500	kernel	tcp_connection_summary [<IPv4-redacted>:56846<-><IPv4-redacted>:53] interface: utun6 (skipped: 516)
so_gencnt: 748757 t_state: FIN_WAIT_1 process: Nexy:2761 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	11:28:17.073759-0500	Nexy	nw_path_libinfo_path_check [167F86EB-D9A0-478B-B656-4DC16AEE5956 IPv4#c40f1370:443 tcp, legacy-socket, attribution: developer]
	libinfo check path: <private>
default	11:28:17.075269-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa5f974300 at /Applications/Nexy.app
default	11:28:17.075495-0500	kernel	SK[8]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 35C7088E-E640-4165-A9CF-6F5174C8F322 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.56847,dst=<IPv4-redacted>.443,proto=0x06 mask=0x0000003f,hash=0xc933b95a tp_proto=0x06"
default	11:28:17.075536-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:56847<-><IPv4-redacted>:443] interface: utun6 (skipped: 516)
so_gencnt: 748758 t_state: SYN_SENT process: Nexy:2761 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x927e2a1a
default	11:28:17.076246-0500	kernel	tcp connected: [<IPv4-redacted>:56847<-><IPv4-redacted>:443] interface: utun6 (skipped: 516)
so_gencnt: 748758 t_state: ESTABLISHED process: Nexy:2761 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x927e2a1a
default	11:28:17.095614-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa5f974000 at /Applications/Nexy.app
default	11:28:17.099874-0500	tccd	Publishing <TCCDEvent: type=Modify, service=kTCCServiceAccessibility, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 0 subscribers: {
}
default	11:28:17.240483-0500	Nexy	[0x99338d540] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	11:28:17.241043-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=2761.5, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=2761, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	11:28:17.246814-0500	tccd	AUTHREQ_SUBJECT: msgID=2761.5, subject=com.nexy.assistant,
default	11:28:17.247412-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa5f974000 at /Applications/Nexy.app
default	11:28:17.260004-0500	Nexy	[0x99338d540] invalidated after the last release of the connection object
default	11:28:17.611119-0500	kernel	udp connect: [<IPv4-redacted>:62685<-><IPv4-redacted>:443] interface:  (skipped: 239)
so_gencnt: 748761 so_state: 0x0002 process: Nexy:2761 bytes in/out: 0/0 pkts in/out: 0/0 error: 0 so_error: 0 svc/tc: 0 flow: 0xa5da5c1d
default	11:28:17.611138-0500	kernel	udp_connection_summary [<IPv4-redacted>:62685<-><IPv4-redacted>:443] interface:  (skipped: 239)
so_gencnt: 748761 so_state: 0x0002 process: Nexy:2761 Duration: 0.000 sec Conn_Time: 0.000 sec bytes in/out: 0/0 pkts in/out: 0/0 rxnospace pkts/bytes: 0/0 so_error: 0 svc/tc: 0 flow: 0xa5da5c1d flowctl: 0us (0x)
default	11:28:17.613251-0500	kernel	SK[7]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 7F3AC794-F8FB-4142-9032-F4630B6EDD76 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.56849,dst=<IPv4-redacted>.443,proto=0x06 mask=0x0000003f,hash=0x6cddd0ae tp_proto=0x06"
default	11:28:17.613318-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:56849<-><IPv4-redacted>:443] interface: utun6 (skipped: 516)
so_gencnt: 748763 t_state: SYN_SENT process: Nexy:2761 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 1 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xb7972149
default	11:28:17.613876-0500	kernel	tcp connected: [<IPv4-redacted>:56849<-><IPv4-redacted>:443] interface: utun6 (skipped: 516)
so_gencnt: 748763 t_state: ESTABLISHED process: Nexy:2761 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 1 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xb7972149
default	11:28:17.664597-0500	Nexy	[0x99338d7c0] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	11:28:17.665329-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=2761.6, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=2761, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	11:28:17.666517-0500	tccd	AUTHREQ_SUBJECT: msgID=2761.6, subject=com.nexy.assistant,
default	11:28:17.667180-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa5f977600 at /Applications/Nexy.app
default	11:28:17.680545-0500	Nexy	[0x99338d7c0] invalidated after the last release of the connection object
default	11:28:17.681639-0500	Nexy	 [INFO] SLSHWCaptureDesktopProxying:485 request: <private>
default	11:28:17.683875-0500	Nexy	[0x99338d7c0] activating connection: mach=true listener=false peer=false name=com.apple.replayd
default	11:28:17.683986-0500	Nexy	 [INFO] -[RPDaemonProxy consumeSandboxExtension:processNewConnection:]:568
default	11:28:17.684109-0500	Nexy	 [INFO] -[RPDaemonProxy proxyCoreGraphicsWithMethodType:config:machPort:completionHandler:]:1486
default	11:28:17.687890-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=2055.4, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=2761, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.replayd, pid=2055, auid=501, euid=501, binary_path=/usr/libexec/replayd}, },
default	11:28:17.687916-0500	tccd	requestor: TCCDProcess: identifier=com.apple.replayd, pid=2055, auid=501, euid=501, binary_path=/usr/libexec/replayd is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=2761, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	11:28:17.688839-0500	tccd	AUTHREQ_SUBJECT: msgID=2055.4, subject=com.nexy.assistant,
default	11:28:17.688968-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=2800.1, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=2761, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.osascript, pid=2800, auid=501, euid=501, binary_path=/usr/bin/osascript}, },
default	11:28:17.689441-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa5f977600 at /Applications/Nexy.app
default	11:28:17.690176-0500	tccd	AUTHREQ_SUBJECT: msgID=2800.1, subject=com.nexy.assistant,
default	11:28:17.690725-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa5f977900 at /Applications/Nexy.app
default	11:28:17.705779-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=391.2246, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=2761, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.osascript, pid=2800, auid=501, euid=501, binary_path=/usr/bin/osascript}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=391, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	11:28:17.706645-0500	tccd	AUTHREQ_SUBJECT: msgID=391.2246, subject=com.nexy.assistant,
default	11:28:17.707209-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa5f977900 at /Applications/Nexy.app
default	11:28:17.720220-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=391.2247, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=2761, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=391, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	11:28:17.720242-0500	tccd	requestor: TCCDProcess: identifier=com.apple.WindowServer, pid=391, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=2761, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	11:28:17.720982-0500	tccd	AUTHREQ_SUBJECT: msgID=391.2247, subject=com.nexy.assistant,
default	11:28:17.721515-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa5f977900 at /Applications/Nexy.app
default	11:28:17.751235-0500	Nexy	 [INFO] SLSHWCaptureDesktopProxying_block_invoke:506 request: <private>, error: (null), windowInfo: (null)
default	11:28:17.767013-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa5f976700 at /Applications/Nexy.app
default	11:28:17.783375-0500	System Events	TCCAccessRequestIndirect: TCCAccessRequestIndirect with pid 2767: target_identity: {
    kTCCCodeIdentityAuditToken = {length = 32, bytes = 0xf5010000 f5010000 14000000 f5010000 ... b9860100 3b7b0300 };
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
default	11:28:17.794883-0500	tccd	target_executable_path_URL: file:///Applications/Nexy.app/Contents/MacOS/Nexy
default	11:28:17.929255-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(5739)
default	11:28:17.929294-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:5739 called from <private>
default	11:28:17.929302-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:5739 called from <private>
default	11:28:17.929934-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(5740)
default	11:28:17.929950-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:5740 called from <private>
default	11:28:17.929955-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:5740 called from <private>
default	11:28:17.939939-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(5740)
default	11:28:17.939960-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:5740 called from <private>
default	11:28:17.939966-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:5740 called from <private>
default	11:28:17.940232-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:5739 called from <private>
default	11:28:17.940241-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:5739 called from <private>
default	11:28:17.940850-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(5739)
default	11:28:17.943373-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(5739)
default	11:28:17.943387-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(5739)
default	11:28:17.943521-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(5739)
default	11:28:17.943625-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:5739 called from <private>
default	11:28:17.943633-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:5739 called from <private>
default	11:28:17.943811-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(5739)
default	11:28:17.952044-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:5739 called from <private>
default	11:28:17.952058-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:5739 called from <private>
default	11:28:17.952435-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:5739 called from <private>
default	11:28:17.952446-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:5739 called from <private>
default	11:28:17.952538-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(5739)
default	11:28:17.957989-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(5739)
default	11:28:17.958231-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:5739 called from <private>
default	11:28:17.958270-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:5739 called from <private>
default	11:28:17.958400-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(5739)
default	11:28:17.965904-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(5739)
default	11:28:17.966135-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:5739 called from <private>
default	11:28:17.966145-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:5739 called from <private>
default	11:28:17.966166-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:5739 called from <private>
default	11:28:17.966176-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:5739 called from <private>
default	11:28:17.966181-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:5739 called from <private>
default	11:28:17.966187-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:5739 called from <private>
default	11:28:17.966192-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:5739 called from <private>
default	11:28:17.966200-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:5739 called from <private>
default	11:28:17.966308-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:5739 called from <private>
default	11:28:17.966393-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:5739 called from <private>
default	11:28:17.966485-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:5739 called from <private>
default	11:28:17.966563-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:5739 called from <private>
default	11:28:17.966644-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:5739 called from <private>
default	11:28:17.966716-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:5739 called from <private>
default	11:28:17.966769-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:5739 called from <private>
default	11:28:17.966826-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:5739 called from <private>
default	11:28:17.966876-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:5739 called from <private>
default	11:28:17.966958-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:5739 called from <private>
default	11:28:17.967082-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:5739 called from <private>
default	11:28:17.967360-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:5739 called from <private>
default	11:28:18.246431-0500	Nexy	[0x99338db80] activating connection: mach=true listener=false peer=false name=com.apple.usernoted.client
default	11:28:18.269486-0500	usernoted	Connection com.nexy.assistant with path: /Applications/Nexy.app
default	11:28:18.273813-0500	distnoted	register name: com.apple.nsquiet_safe_quit_give_reason object: com.nexy.assistant token: 2400000020 pid: 2761
default	11:28:18.285911-0500	Nexy	                AUHAL.cpp:420   AUHAL: (0x992065540) Selecting device 85 from constructor
default	11:28:18.285921-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0x992065540)
default	11:28:18.285942-0500	Nexy	                AUHAL.cpp:676   SelectDevice: (0x992065540) not already running
default	11:28:18.285947-0500	Nexy	                AUHAL.cpp:752   SelectDevice: (0x992065540) nothing to teardown
default	11:28:18.285950-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0x992065540) connecting device 85
default	11:28:18.286098-0500	Nexy	                AUHAL.cpp:3413  IsDeviceUsable: (0x992065540) Device ID: 85 (Input:No | Output:Yes): true
default	11:28:18.286221-0500	Nexy	                AUHAL.cpp:769   SelectDevice: (0x992065540) created ioproc 0xb for device 85
default	11:28:18.286374-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x992065540) adding 7 device listeners to device 85
default	11:28:18.286591-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x992065540) adding 0 device delegate listeners to device 85
default	11:28:18.286603-0500	Nexy	                AUHAL.cpp:1581  UpdateStreamFormats: -> (0x992065540)
default	11:28:18.286695-0500	Nexy	                AUHAL.cpp:1677  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  48000 Hz, Float32, interleaved
default	11:28:18.286704-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 1 output streams; not all mono
default	11:28:18.286710-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	11:28:18.286716-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 0 input streams; not all mono
default	11:28:18.286725-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	11:28:18.286859-0500	Nexy	                AUHAL.cpp:1771  UpdateStreamFormats: AUHAL(0x992065540) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	11:28:18.286875-0500	Nexy	                AUHAL.cpp:1777  UpdateStreamFormats: AUHAL(0x992065540) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	11:28:18.286880-0500	Nexy	                AUHAL.cpp:1787  UpdateStreamFormats: <-
default	11:28:18.286887-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x992065540) removing 0 device listeners from device 0
default	11:28:18.286891-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x992065540) removing 0 device delegate listeners from device 0
default	11:28:18.286895-0500	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0x992065540)
default	11:28:18.286911-0500	Nexy	                AUHAL.cpp:2298  SetProperty: (0x992065540) caller requesting device change from 85 to 85
default	11:28:18.286916-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0x992065540)
default	11:28:18.286920-0500	Nexy	                AUHAL.cpp:659   SelectDevice: <- (0x992065540) exiting with nothing to do
default	11:28:18.287461-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	11:28:18.287595-0500	Nexy	NSApp cache appearance:
-NSRequiresAquaSystemAppearance: 0
-appearance: (null)
-effectiveAppearance: <NSCompositeAppearance: 0x992e30780
 (
    "<NSAquaAppearance: 0x992e30640>",
    "<NSSystemAppearance: 0x992e306e0>"
)>
default	11:28:18.287934-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	11:28:18.290272-0500	Nexy	                AUHAL.cpp:473   ~AUHAL: (0x992065540) Selecting device 0 from destructor
default	11:28:18.290282-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0x992065540)
default	11:28:18.290291-0500	Nexy	                AUHAL.cpp:676   SelectDevice: (0x992065540) not already running
default	11:28:18.290297-0500	Nexy	                AUHAL.cpp:682   SelectDevice: (0x992065540) disconnecting device 85
default	11:28:18.290302-0500	Nexy	                AUHAL.cpp:746   SelectDevice: (0x992065540) destroying ioproc 0xb for device 85
default	11:28:18.290343-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Output {1C-77-54-18-C8-A3:output, 0xb}
default	11:28:18.290393-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	11:28:18.290504-0500	Nexy	                AUHAL.cpp:848   SelectDevice: (0x992065540) nothing to setup
default	11:28:18.290512-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x992065540) adding 0 device listeners to device 0
default	11:28:18.290518-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x992065540) adding 0 device delegate listeners to device 0
default	11:28:18.290524-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x992065540) removing 7 device listeners from device 85
default	11:28:18.290781-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x992065540) removing 0 device delegate listeners from device 85
default	11:28:18.290791-0500	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0x992065540)
default	11:28:18.290936-0500	Nexy	[0x99338e080] activating connection: mach=true listener=false peer=false name=com.apple.dock.fullscreen
default	11:28:18.291522-0500	Nexy	[0x99338e1c0] activating connection: mach=true listener=false peer=false name=com.apple.fonts
default	11:28:18.291661-0500	Nexy	                AUHAL.cpp:420   AUHAL: (0x992065540) Selecting device 85 from constructor
default	11:28:18.291671-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0x992065540)
default	11:28:18.291676-0500	Nexy	                AUHAL.cpp:676   SelectDevice: (0x992065540) not already running
default	11:28:18.291681-0500	Nexy	                AUHAL.cpp:752   SelectDevice: (0x992065540) nothing to teardown
default	11:28:18.291685-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0x992065540) connecting device 85
default	11:28:18.291759-0500	Nexy	                AUHAL.cpp:3413  IsDeviceUsable: (0x992065540) Device ID: 85 (Input:No | Output:Yes): true
default	11:28:18.291840-0500	Nexy	                AUHAL.cpp:769   SelectDevice: (0x992065540) created ioproc 0xc for device 85
default	11:28:18.291958-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x992065540) adding 7 device listeners to device 85
default	11:28:18.292138-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x992065540) adding 0 device delegate listeners to device 85
default	11:28:18.292146-0500	Nexy	                AUHAL.cpp:1581  UpdateStreamFormats: -> (0x992065540)
default	11:28:18.292215-0500	Nexy	                AUHAL.cpp:1677  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  48000 Hz, Float32, interleaved
default	11:28:18.292223-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 1 output streams; not all mono
default	11:28:18.292228-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	11:28:18.292236-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 0 input streams; not all mono
default	11:28:18.292243-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	11:28:18.292334-0500	Nexy	                AUHAL.cpp:1771  UpdateStreamFormats: AUHAL(0x992065540) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	11:28:18.292342-0500	Nexy	                AUHAL.cpp:1777  UpdateStreamFormats: AUHAL(0x992065540) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	11:28:18.292347-0500	Nexy	                AUHAL.cpp:1787  UpdateStreamFormats: <-
default	11:28:18.292351-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x992065540) removing 0 device listeners from device 0
default	11:28:18.292356-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x992065540) removing 0 device delegate listeners from device 0
default	11:28:18.292359-0500	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0x992065540)
default	11:28:18.292367-0500	Nexy	                AUHAL.cpp:2298  SetProperty: (0x992065540) caller requesting device change from 85 to 85
default	11:28:18.292371-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0x992065540)
default	11:28:18.292375-0500	Nexy	                AUHAL.cpp:659   SelectDevice: <- (0x992065540) exiting with nothing to do
default	11:28:18.292380-0500	Nexy	AudioHardware-mac-imp.cpp:1299   AudioObjectAddPropertyListener: listener was already added
default	11:28:18.292753-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	11:28:18.292960-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Output stream enables: Stream 0 is ENABLED
default	11:28:18.294045-0500	Nexy	(<private>) deleteSearchableItemsWithDomainIdentifiers, protectionClass:(null), domainIdentifiers number:1
default	11:28:18.294411-0500	Nexy	[C:1] Alloc com.apple.controlcenter.statusitems
default	11:28:18.294348-0500	Nexy	sConnectionName: com.apple.spotlight.IndexAgent
default	11:28:18.294497-0500	Nexy	Start service name com.apple.spotlight.IndexAgent
default	11:28:18.294517-0500	Nexy	[0x99338e300] activating connection: mach=false listener=false peer=false name=(anonymous)
default	11:28:18.294544-0500	Nexy	[0x99338e440] activating connection: mach=true listener=false peer=false name=com.apple.spotlight.IndexAgent
default	11:28:18.294604-0500	Nexy	FBSWorkspace registering source: <private>
default	11:28:18.294956-0500	runningboardd	ignoring [app<application.com.nexy.assistant.21576034.21576040(501)>:2761] as candidate for concrete target as it is terminating
default	11:28:18.295710-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	11:28:18.295774-0500	Nexy	<FBSWorkspaceScenesClient:0x99134c280 <private>> attempting immediate handshake from activate
default	11:28:18.295819-0500	Nexy	<FBSWorkspaceScenesClient:0x99134c280 <private>> sent handshake
default	11:28:18.295933-0500	Nexy	Realizing settings extension __NSStatusItemSceneHostSettings__ on FBSSceneSettings
default	11:28:18.296024-0500	suggestd	SGDSpotlightReceiver: deleting 1 domain identifiers (1 after removing overlaps) for com.nexy.assistant: <private>
default	11:28:18.299179-0500	Nexy	<FBSWorkspaceScenesClient:0x99134c280 <private>> was invalidated
default	11:28:18.299195-0500	Nexy	FBSWorkspace unregistering source: <private>
default	11:28:18.299541-0500	Nexy	Realizing settings extension __NSStatusItemSceneClientSettings__ on FBSSceneClientSettings
default	11:28:18.300735-0500	Nexy	Realizing settings extension FBSSceneSettingsCore on FBSSceneSettings
default	11:28:18.302118-0500	Nexy	Realizing settings extension FBSSceneClientSettingsCore on FBSSceneClientSettings
default	11:28:18.302675-0500	Nexy	Requesting scene <FBSScene: 0x99134c5a0; com.apple.controlcenter:FF8E74B5-C650-4C0C-A623-97A03E059BD0> from com.apple.controlcenter.statusitems
error	11:28:18.302862-0500	Nexy	Error creating <FBSScene: 0x99134c5a0; com.apple.controlcenter:FF8E74B5-C650-4C0C-A623-97A03E059BD0>: <NSError: 0x9946068e0; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
default	11:28:18.304189-0500	Nexy	Request for <FBSScene: 0x99134c5a0; com.apple.controlcenter:FF8E74B5-C650-4C0C-A623-97A03E059BD0> complete!
default	11:28:18.309689-0500	Nexy	Warning: the app is using `-[NSStatusBarButton setHighlightsBy:]` to set the highlight behavior. Instead, consider removing that setting. That will enable macOS to highlight the status bar button as appropriate for all configurations (e.g., light, dark, and increased contrast modes).
default	11:28:18.325994-0500	Nexy	Registering for test daemon availability notify post.
default	11:28:18.326109-0500	Nexy	notify_get_state check indicated test daemon not ready.
default	11:28:18.326216-0500	Nexy	notify_get_state check indicated test daemon not ready.
default	11:28:18.326296-0500	Nexy	notify_get_state check indicated test daemon not ready.
default	11:28:18.327527-0500	Nexy	[0x99338e800] activating connection: mach=true listener=false peer=false name=com.apple.coreservices.appleevents
default	11:28:18.327977-0500	Nexy	[0x99338c3c0] Connection returned listener port: 0x4f03
default	11:28:18.328304-0500	Nexy	SignalReady: pid=2761 asn=0x0-0x3f83f8
default	11:28:18.328699-0500	Nexy	SIGNAL: pid=2761 asn=0x0x-0x3f83f8
default	11:28:18.329340-0500	loginwindow	-[Application updateInformation] | Got App URL: file:///Applications/Nexy.app/
default	11:28:18.332318-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa5f977600 at /Applications/Nexy.app
error	11:28:18.337347-0500	Nexy	scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
default	11:28:18.342559-0500	Nexy	void _NSDisableAutomaticTerminationAndLog(NSString *) Restoring windows
default	11:28:18.342571-0500	Nexy	-[NSApplication _reopenWindowsAsNecessaryIncludingRestorableState:withFullFidelity:completionHandler:] shouldRestoreState=1 hasPersistentStateToRestore=0 shouldStillRestoreStateAfterPrompting=0
default	11:28:18.342597-0500	Nexy	[0x99338d680] activating connection: mach=true listener=false peer=false name=com.apple.window_proxies
default	11:28:18.342678-0500	Nexy	[0x99338d680] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	11:28:18.343519-0500	Nexy	void _NSEnableAutomaticTerminationAndLog(NSString *) Restoring windows
default	11:28:18.346271-0500	runningboardd	ignoring [app<application.com.nexy.assistant.21576034.21576040(501)>:2761] as candidate for concrete target as it is terminating
default	11:28:18.346307-0500	runningboardd	Acquiring assertion targeting 2761 from originator [app<application.com.nexy.assistant.21576034.21576040(501)>:2761] with description <RBSAssertionDescriptor| "AudioHAL" ID:397-2761-135631 target:2761 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
error	11:28:18.346541-0500	Nexy	Error acquiring assertion: <Error Domain=RBSAssertionErrorDomain Code=2 "Specified target process 2761 does not exist" UserInfo={NSLocalizedFailureReason=Specified target process 2761 does not exist}>
error	11:28:18.346554-0500	Nexy	          HALRBSAssertionGlue.mm:98    Failed to acquire the AudioHAL RBSAssertion for pid: 2761 with code: 2 - RBSAssertionErrorDomain
default	11:28:18.346698-0500	runningboardd	ignoring [app<application.com.nexy.assistant.21576034.21576040(501)>:2761] as candidate for concrete target as it is terminating
default	11:28:18.346723-0500	runningboardd	Acquiring assertion targeting 2761 from originator [app<application.com.nexy.assistant.21576034.21576040(501)>:2761] with description <RBSAssertionDescriptor| "AudioHAL" ID:397-2761-135632 target:2761 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
error	11:28:18.346868-0500	Nexy	Error acquiring assertion: <Error Domain=RBSAssertionErrorDomain Code=2 "Specified target process 2761 does not exist" UserInfo={NSLocalizedFailureReason=Specified target process 2761 does not exist}>
error	11:28:18.346880-0500	Nexy	          HALRBSAssertionGlue.mm:98    Failed to acquire the AudioHAL RBSAssertion for pid: 2761 with code: 2 - RBSAssertionErrorDomain
default	11:28:18.347038-0500	runningboardd	ignoring [app<application.com.nexy.assistant.21576034.21576040(501)>:2761] as candidate for concrete target as it is terminating
default	11:28:18.347068-0500	runningboardd	Acquiring assertion targeting 2761 from originator [app<application.com.nexy.assistant.21576034.21576040(501)>:2761] with description <RBSAssertionDescriptor| "AudioHAL" ID:397-2761-135633 target:2761 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
error	11:28:18.347189-0500	Nexy	Error acquiring assertion: <Error Domain=RBSAssertionErrorDomain Code=2 "Specified target process 2761 does not exist" UserInfo={NSLocalizedFailureReason=Specified target process 2761 does not exist}>
error	11:28:18.347198-0500	Nexy	          HALRBSAssertionGlue.mm:98    Failed to acquire the AudioHAL RBSAssertion for pid: 2761 with code: 2 - RBSAssertionErrorDomain
default	11:28:18.347305-0500	runningboardd	ignoring [app<application.com.nexy.assistant.21576034.21576040(501)>:2761] as candidate for concrete target as it is terminating
default	11:28:18.347326-0500	runningboardd	Acquiring assertion targeting 2761 from originator [app<application.com.nexy.assistant.21576034.21576040(501)>:2761] with description <RBSAssertionDescriptor| "AudioHAL" ID:397-2761-135634 target:2761 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
error	11:28:18.347410-0500	Nexy	Error acquiring assertion: <Error Domain=RBSAssertionErrorDomain Code=2 "Specified target process 2761 does not exist" UserInfo={NSLocalizedFailureReason=Specified target process 2761 does not exist}>
error	11:28:18.347419-0500	Nexy	          HALRBSAssertionGlue.mm:98    Failed to acquire the AudioHAL RBSAssertion for pid: 2761 with code: 2 - RBSAssertionErrorDomain
default	11:28:18.347558-0500	runningboardd	ignoring [app<application.com.nexy.assistant.21576034.21576040(501)>:2761] as candidate for concrete target as it is terminating
default	11:28:18.347588-0500	runningboardd	Acquiring assertion targeting 2761 from originator [app<application.com.nexy.assistant.21576034.21576040(501)>:2761] with description <RBSAssertionDescriptor| "AudioHAL" ID:397-2761-135635 target:2761 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
error	11:28:18.347733-0500	Nexy	Error acquiring assertion: <Error Domain=RBSAssertionErrorDomain Code=2 "Specified target process 2761 does not exist" UserInfo={NSLocalizedFailureReason=Specified target process 2761 does not exist}>
error	11:28:18.347743-0500	Nexy	          HALRBSAssertionGlue.mm:98    Failed to acquire the AudioHAL RBSAssertion for pid: 2761 with code: 2 - RBSAssertionErrorDomain
default	11:28:18.353171-0500	Nexy	[C:2] Alloc <private>
default	11:28:18.353209-0500	Nexy	[0x99338d400] activating connection: mach=false listener=false peer=false name=(anonymous)
error	11:28:18.353430-0500	kernel	Sandbox: WindowManager(580) deny(1) mach-task-name others [Nexy(2761)]
default	11:28:18.355066-0500	WindowManager	Connection activated | (2761) Nexy
default	11:28:18.448014-0500	Nexy	*warn* MailCS ======%%% _setMailMessageAttributes skip:1
default	11:28:18.452223-0500	Nexy	Start service name com.apple.spotlightknowledged
default	11:28:18.453054-0500	Nexy	[GMS] availability notification token 76
default	11:28:18.569967-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	11:28:18.570055-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[scr] Nexy (com.nexy.assistant)]
default	11:28:18.570101-0500	ControlCenter	Active activity attributions changed to ["scr:com.nexy.assistant"]
default	11:28:18.572307-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:28:18.572319-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:28:18.572335-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	11:28:18.572340-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:28:18.572349-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	11:28:18.572355-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	11:28:18.572453-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	11:28:18.655635-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Output {1C-77-54-18-C8-A3:output, 0xc}
default	11:28:18.656471-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1c5043","name":"Nexy(2761)"}, "details":{"deviceUIDs":["1C-77-54-18-C8-A3:output"],"implicit_category":"MediaPlayback","input_running":false,"output_running":true} }
default	11:28:18.656570-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 68, PID = 2761, Name = sid:0x1c5043, Nexy(2761), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	11:28:18.656599-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Category/Mode changed -- The score for sid:0x1c5043, Nexy(2761), 'prim'/com.nexy.assistant was not correct. Old score = 201
default	11:28:18.656630-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 68, PID = 2761, Name = sid:0x1c5043, Nexy(2761), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	11:28:18.656673-0500	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1c5043, Nexy(2761), 'prim'', AudioCategory changed to 'MediaPlayback'
default	11:28:18.656693-0500	audiomxd	UpdateAudioState CID 0x218B0001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	11:28:18.656721-0500	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 68, PID = 2761, Name = sid:0x1c5043, Nexy(2761), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO> is going active
default	11:28:18.656732-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsPlaying:]: MXCoreSession com.nexy.assistant with category/mode MediaPlayback/Default and coreSessionID = 68 starting playing
default	11:28:18.656788-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 68, PID = 2761, Name = sid:0x1c5043, Nexy(2761), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	11:28:18.656800-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	11:28:18.656836-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	11:28:18.656816-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 68, PID = 2761, Name = sid:0x1c5043, Nexy(2761), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO>
default	11:28:18.656842-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1c5043, Nexy(2761), 'prim'', displayID:'com.nexy.assistant'}
default	11:28:18.656864-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Will try to see if we can get the shared route for session = <ID: 68, PID = 2761, Name = sid:0x1c5043, Nexy(2761), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = YES, Playing = YES, Recording = NO>. Old (200) and New (201) scores.
default	11:28:18.656892-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 201, deviceID = <private>
default	11:28:18.657022-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 1]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:output"
)}
default	11:28:18.656928-0500	audiomxd	AudioApplicationInfoImpl.mm:395   Successfully updated session 0x1c5043 to isSessionRecording: 0
	app: {"name":"[implicit] Nexy","pid":2761}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1c5043, sessionType: 'prim', isRecording: false }, 
]
default	11:28:18.657033-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	11:28:18.657136-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 201 flag 0x1 < Hijack > app com.nexy.assistant CID 0x218B0001 category Not set
default	11:28:18.658112-0500	audiomxd	UpdateAudioState CID 0x218B0001 audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	11:28:18.658226-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 201,
}
default	11:28:18.658256-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 201,
}
default	11:28:18.658277-0500	audioaccessoryd	AudioStateChanged: Added audio session app com.nexy.assistant NULL -> 201 count 1
default	11:28:18.658288-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 201
error	11:28:18.658299-0500	audioaccessoryd	Updating local audio category 100 -> 201 app com.nexy.assistant
default	11:28:18.658360-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 201 App com.nexy.assistant
default	11:28:19.338243-0500	Nexy	FBSWorkspace registering source: <private>
default	11:28:19.338299-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	11:28:19.338406-0500	Nexy	<FBSWorkspaceScenesClient:0x99134cbe0 <private>> attempting immediate handshake from activate
default	11:28:19.338454-0500	Nexy	<FBSWorkspaceScenesClient:0x99134cbe0 <private>> sent handshake
default	11:28:19.338913-0500	Nexy	Requesting scene <FBSScene: 0x99134c6e0; com.apple.controlcenter:6A2979A5-ED91-46FA-9AD1-F7CC56572F18> from com.apple.controlcenter.statusitems
default	11:28:19.339356-0500	Nexy	<FBSWorkspaceScenesClient:0x99134cbe0 <private>> was invalidated
default	11:28:19.339440-0500	Nexy	FBSWorkspace unregistering source: <private>
default	11:28:19.339469-0500	Nexy	Request for <FBSScene: 0x99134c6e0; com.apple.controlcenter:6A2979A5-ED91-46FA-9AD1-F7CC56572F18> complete!
error	11:28:19.339545-0500	Nexy	Error creating <FBSScene: 0x99134c6e0; com.apple.controlcenter:6A2979A5-ED91-46FA-9AD1-F7CC56572F18>: <NSError: 0x994600630; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	11:28:19.339615-0500	Nexy	No scene exists for identity: com.apple.controlcenter:6A2979A5-ED91-46FA-9AD1-F7CC56572F18
default	11:28:19.339648-0500	Nexy	Realizing settings extension FBSSceneTransitionContextCore on FBSSceneTransitionContext
default	11:28:19.341706-0500	Nexy	FBSWorkspace registering source: <private>
default	11:28:19.341732-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	11:28:19.341793-0500	Nexy	<FBSWorkspaceScenesClient:0x99134c460 <private>> attempting immediate handshake from activate
default	11:28:19.341818-0500	Nexy	<FBSWorkspaceScenesClient:0x99134c460 <private>> sent handshake
default	11:28:19.341912-0500	Nexy	Realizing settings extension __NSHostedViewSceneSettings__ on FBSSceneSettings
default	11:28:19.342343-0500	Nexy	Realizing settings extension __NSClientHostedViewSceneSettings__ on FBSSceneClientSettings
default	11:28:19.342503-0500	Nexy	<FBSWorkspaceScenesClient:0x99134c460 <private>> was invalidated
default	11:28:19.342521-0500	Nexy	FBSWorkspace unregistering source: <private>
default	11:28:19.342719-0500	Nexy	Realizing settings extension __NSStatusItemAuxiliaryViewSceneSettings__ on FBSSceneSettings
default	11:28:19.342772-0500	Nexy	Realizing settings extension __NSClientStatusItemAuxiliaryViewSceneSettings__ on FBSSceneClientSettings
default	11:28:19.343209-0500	Nexy	Requesting scene <FBSScene: 0x99134cc80; com.apple.controlcenter:6A2979A5-ED91-46FA-9AD1-F7CC56572F18-Aux[1]-NSStatusItemView> from com.apple.controlcenter.statusitems
error	11:28:19.343430-0500	Nexy	Error creating <FBSScene: 0x99134cc80; com.apple.controlcenter:6A2979A5-ED91-46FA-9AD1-F7CC56572F18-Aux[1]-NSStatusItemView>: <NSError: 0x994600a20; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
default	11:28:19.343480-0500	Nexy	Request for <FBSScene: 0x99134cc80; com.apple.controlcenter:6A2979A5-ED91-46FA-9AD1-F7CC56572F18-Aux[1]-NSStatusItemView> complete!
error	11:28:19.343847-0500	Nexy	scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	11:28:19.343868-0500	Nexy	[com.apple.controlcenter:6A2979A5-ED91-46FA-9AD1-F7CC56572F18] No matching scene to invalidate for this identity.
error	11:28:19.343894-0500	Nexy	auxiliary scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	11:28:19.343941-0500	Nexy	Unhandled disconnected scene <private>
error	11:28:19.344043-0500	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
default	11:28:19.922867-0500	audioaccessoryd	AudioStateSnapshot: Route:Bluetooth App com.nexy.assistant, Score 201, Remote 0NumofApp 1
default	11:28:20.345304-0500	Nexy	FBSWorkspace registering source: <private>
default	11:28:20.345346-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	11:28:20.345432-0500	Nexy	<FBSWorkspaceScenesClient:0x99134cc80 <private>> attempting immediate handshake from activate
default	11:28:20.345463-0500	Nexy	<FBSWorkspaceScenesClient:0x99134cc80 <private>> sent handshake
default	11:28:20.345784-0500	Nexy	Requesting scene <FBSScene: 0x99134c6e0; com.apple.controlcenter:232EEACA-C1E9-4738-B9F0-8D1B20C43CD0> from com.apple.controlcenter.statusitems
default	11:28:20.346088-0500	Nexy	Request for <FBSScene: 0x99134c6e0; com.apple.controlcenter:232EEACA-C1E9-4738-B9F0-8D1B20C43CD0> complete!
default	11:28:20.346393-0500	Nexy	<FBSWorkspaceScenesClient:0x99134cc80 <private>> was invalidated
default	11:28:20.346421-0500	Nexy	FBSWorkspace unregistering source: <private>
default	11:28:20.346466-0500	Nexy	FBSWorkspace registering source: <private>
default	11:28:20.346483-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	11:28:20.346525-0500	Nexy	<FBSWorkspaceScenesClient:0x99134cdc0 <private>> attempting immediate handshake from activate
default	11:28:20.346544-0500	Nexy	<FBSWorkspaceScenesClient:0x99134cdc0 <private>> sent handshake
error	11:28:20.346601-0500	Nexy	Error creating <FBSScene: 0x99134c6e0; com.apple.controlcenter:232EEACA-C1E9-4738-B9F0-8D1B20C43CD0>: <NSError: 0x994600990; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	11:28:20.346618-0500	Nexy	No scene exists for identity: com.apple.controlcenter:232EEACA-C1E9-4738-B9F0-8D1B20C43CD0
default	11:28:20.346689-0500	Nexy	Requesting scene <FBSScene: 0x99134cbe0; com.apple.controlcenter:232EEACA-C1E9-4738-B9F0-8D1B20C43CD0-Aux[2]-NSStatusItemView> from com.apple.controlcenter.statusitems
default	11:28:20.346961-0500	Nexy	Request for <FBSScene: 0x99134cbe0; com.apple.controlcenter:232EEACA-C1E9-4738-B9F0-8D1B20C43CD0-Aux[2]-NSStatusItemView> complete!
default	11:28:20.346990-0500	Nexy	<FBSWorkspaceScenesClient:0x99134cdc0 <private>> was invalidated
default	11:28:20.347009-0500	Nexy	FBSWorkspace unregistering source: <private>
error	11:28:20.347059-0500	Nexy	Error creating <FBSScene: 0x99134cbe0; com.apple.controlcenter:232EEACA-C1E9-4738-B9F0-8D1B20C43CD0-Aux[2]-NSStatusItemView>: <NSError: 0x9946008a0; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	11:28:20.347078-0500	Nexy	No scene exists for identity: com.apple.controlcenter:232EEACA-C1E9-4738-B9F0-8D1B20C43CD0-Aux[2]-NSStatusItemView
default	11:28:20.347851-0500	Nexy	[com.apple.controlcenter:232EEACA-C1E9-4738-B9F0-8D1B20C43CD0-Aux[2]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
error	11:28:20.348159-0500	Nexy	scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	11:28:20.348176-0500	Nexy	[com.apple.controlcenter:232EEACA-C1E9-4738-B9F0-8D1B20C43CD0] No matching scene to invalidate for this identity.
error	11:28:20.348201-0500	Nexy	auxiliary scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	11:28:20.348216-0500	Nexy	[com.apple.controlcenter:232EEACA-C1E9-4738-B9F0-8D1B20C43CD0-Aux[2]-NSStatusItemView] No matching scene to invalidate for this identity.
error	11:28:20.348624-0500	Nexy	Unhandled disconnected scene <private>
error	11:28:20.348701-0500	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
error	11:28:20.348764-0500	Nexy	Unhandled disconnected auxiliary scene <private>
error	11:28:20.348795-0500	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
default	11:28:21.348995-0500	Nexy	FBSWorkspace registering source: <private>
default	11:28:21.349037-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	11:28:21.349123-0500	Nexy	<FBSWorkspaceScenesClient:0x99134cbe0 <private>> attempting immediate handshake from activate
default	11:28:21.349153-0500	Nexy	<FBSWorkspaceScenesClient:0x99134cbe0 <private>> sent handshake
default	11:28:21.349450-0500	Nexy	Requesting scene <FBSScene: 0x99134c6e0; com.apple.controlcenter:D3D2456A-A195-4445-B8A1-4DD3DAAF29CF> from com.apple.controlcenter.statusitems
default	11:28:21.349716-0500	Nexy	Request for <FBSScene: 0x99134c6e0; com.apple.controlcenter:D3D2456A-A195-4445-B8A1-4DD3DAAF29CF> complete!
default	11:28:21.350055-0500	Nexy	<FBSWorkspaceScenesClient:0x99134cbe0 <private>> was invalidated
default	11:28:21.350091-0500	Nexy	FBSWorkspace unregistering source: <private>
default	11:28:21.350141-0500	Nexy	FBSWorkspace registering source: <private>
default	11:28:21.350157-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	11:28:21.350199-0500	Nexy	<FBSWorkspaceScenesClient:0x99134cdc0 <private>> attempting immediate handshake from activate
default	11:28:21.350219-0500	Nexy	<FBSWorkspaceScenesClient:0x99134cdc0 <private>> sent handshake
error	11:28:21.350276-0500	Nexy	Error creating <FBSScene: 0x99134c6e0; com.apple.controlcenter:D3D2456A-A195-4445-B8A1-4DD3DAAF29CF>: <NSError: 0x994600a20; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	11:28:21.350294-0500	Nexy	No scene exists for identity: com.apple.controlcenter:D3D2456A-A195-4445-B8A1-4DD3DAAF29CF
default	11:28:21.350375-0500	Nexy	Requesting scene <FBSScene: 0x99134cc80; com.apple.controlcenter:D3D2456A-A195-4445-B8A1-4DD3DAAF29CF-Aux[3]-NSStatusItemView> from com.apple.controlcenter.statusitems
default	11:28:21.350563-0500	Nexy	Request for <FBSScene: 0x99134cc80; com.apple.controlcenter:D3D2456A-A195-4445-B8A1-4DD3DAAF29CF-Aux[3]-NSStatusItemView> complete!
default	11:28:21.350817-0500	Nexy	<FBSWorkspaceScenesClient:0x99134cdc0 <private>> was invalidated
default	11:28:21.350840-0500	Nexy	FBSWorkspace unregistering source: <private>
error	11:28:21.350893-0500	Nexy	Error creating <FBSScene: 0x99134cc80; com.apple.controlcenter:D3D2456A-A195-4445-B8A1-4DD3DAAF29CF-Aux[3]-NSStatusItemView>: <NSError: 0x9946005d0; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	11:28:21.350908-0500	Nexy	No scene exists for identity: com.apple.controlcenter:D3D2456A-A195-4445-B8A1-4DD3DAAF29CF-Aux[3]-NSStatusItemView
default	11:28:21.351054-0500	Nexy	[com.apple.controlcenter:D3D2456A-A195-4445-B8A1-4DD3DAAF29CF-Aux[3]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
error	11:28:21.351267-0500	Nexy	scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	11:28:21.351281-0500	Nexy	[com.apple.controlcenter:D3D2456A-A195-4445-B8A1-4DD3DAAF29CF] No matching scene to invalidate for this identity.
error	11:28:21.351305-0500	Nexy	auxiliary scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	11:28:21.351320-0500	Nexy	[com.apple.controlcenter:D3D2456A-A195-4445-B8A1-4DD3DAAF29CF-Aux[3]-NSStatusItemView] No matching scene to invalidate for this identity.
error	11:28:21.351763-0500	Nexy	Unhandled disconnected scene <private>
error	11:28:21.351838-0500	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
error	11:28:21.351888-0500	Nexy	Unhandled disconnected auxiliary scene <private>
error	11:28:21.351922-0500	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
default	11:28:22.352669-0500	Nexy	FBSWorkspace registering source: <private>
default	11:28:22.352705-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	11:28:22.352792-0500	Nexy	<FBSWorkspaceScenesClient:0x99134cc80 <private>> attempting immediate handshake from activate
default	11:28:22.352821-0500	Nexy	<FBSWorkspaceScenesClient:0x99134cc80 <private>> sent handshake
default	11:28:22.353116-0500	Nexy	Requesting scene <FBSScene: 0x99134c6e0; com.apple.controlcenter:25CB4B66-C013-436C-9059-58EC9B75BF5C> from com.apple.controlcenter.statusitems
default	11:28:22.353355-0500	Nexy	Request for <FBSScene: 0x99134c6e0; com.apple.controlcenter:25CB4B66-C013-436C-9059-58EC9B75BF5C> complete!
default	11:28:22.353634-0500	Nexy	<FBSWorkspaceScenesClient:0x99134cc80 <private>> was invalidated
default	11:28:22.353658-0500	Nexy	FBSWorkspace unregistering source: <private>
default	11:28:22.353701-0500	Nexy	FBSWorkspace registering source: <private>
default	11:28:22.353717-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	11:28:22.353754-0500	Nexy	<FBSWorkspaceScenesClient:0x99134cdc0 <private>> attempting immediate handshake from activate
default	11:28:22.353771-0500	Nexy	<FBSWorkspaceScenesClient:0x99134cdc0 <private>> sent handshake
error	11:28:22.353820-0500	Nexy	Error creating <FBSScene: 0x99134c6e0; com.apple.controlcenter:25CB4B66-C013-436C-9059-58EC9B75BF5C>: <NSError: 0x994600870; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	11:28:22.353836-0500	Nexy	No scene exists for identity: com.apple.controlcenter:25CB4B66-C013-436C-9059-58EC9B75BF5C
default	11:28:22.353893-0500	Nexy	Requesting scene <FBSScene: 0x99134cbe0; com.apple.controlcenter:25CB4B66-C013-436C-9059-58EC9B75BF5C-Aux[4]-NSStatusItemView> from com.apple.controlcenter.statusitems
default	11:28:22.354046-0500	Nexy	Request for <FBSScene: 0x99134cbe0; com.apple.controlcenter:25CB4B66-C013-436C-9059-58EC9B75BF5C-Aux[4]-NSStatusItemView> complete!
default	11:28:22.354127-0500	Nexy	<FBSWorkspaceScenesClient:0x99134cdc0 <private>> was invalidated
default	11:28:22.354149-0500	Nexy	FBSWorkspace unregistering source: <private>
error	11:28:22.354198-0500	Nexy	Error creating <FBSScene: 0x99134cbe0; com.apple.controlcenter:25CB4B66-C013-436C-9059-58EC9B75BF5C-Aux[4]-NSStatusItemView>: <NSError: 0x994600840; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	11:28:22.354213-0500	Nexy	No scene exists for identity: com.apple.controlcenter:25CB4B66-C013-436C-9059-58EC9B75BF5C-Aux[4]-NSStatusItemView
default	11:28:22.354528-0500	Nexy	[com.apple.controlcenter:25CB4B66-C013-436C-9059-58EC9B75BF5C-Aux[4]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
error	11:28:22.354718-0500	Nexy	scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	11:28:22.354747-0500	Nexy	[com.apple.controlcenter:25CB4B66-C013-436C-9059-58EC9B75BF5C] No matching scene to invalidate for this identity.
error	11:28:22.354768-0500	Nexy	auxiliary scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	11:28:22.354779-0500	Nexy	[com.apple.controlcenter:25CB4B66-C013-436C-9059-58EC9B75BF5C-Aux[4]-NSStatusItemView] No matching scene to invalidate for this identity.
error	11:28:22.355140-0500	Nexy	Unhandled disconnected scene <private>
error	11:28:22.355201-0500	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
error	11:28:22.355247-0500	Nexy	Unhandled disconnected auxiliary scene <private>
error	11:28:22.355273-0500	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
default	11:28:22.922863-0500	audioaccessoryd	AudioStateSnapshot: Route:Bluetooth App com.nexy.assistant, Score 201, Remote 0NumofApp 1
default	11:28:23.275693-0500	Nexy	void _updateToReflectAutomaticTerminationState(void) Setting _kLSApplicationWouldBeTerminatedByTALKey=1
default	11:28:23.356215-0500	Nexy	FBSWorkspace registering source: <private>
default	11:28:23.356256-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	11:28:23.356358-0500	Nexy	<FBSWorkspaceScenesClient:0x99134cbe0 <private>> attempting immediate handshake from activate
default	11:28:23.356389-0500	Nexy	<FBSWorkspaceScenesClient:0x99134cbe0 <private>> sent handshake
default	11:28:23.356715-0500	Nexy	Requesting scene <FBSScene: 0x99134c6e0; com.apple.controlcenter:45B6D88E-6CFE-44D6-8FA2-83A300FBF752> from com.apple.controlcenter.statusitems
default	11:28:23.356995-0500	Nexy	Request for <FBSScene: 0x99134c6e0; com.apple.controlcenter:45B6D88E-6CFE-44D6-8FA2-83A300FBF752> complete!
default	11:28:23.357434-0500	Nexy	<FBSWorkspaceScenesClient:0x99134cbe0 <private>> was invalidated
default	11:28:23.357467-0500	Nexy	FBSWorkspace unregistering source: <private>
error	11:28:23.357568-0500	Nexy	Error creating <FBSScene: 0x99134c6e0; com.apple.controlcenter:45B6D88E-6CFE-44D6-8FA2-83A300FBF752>: <NSError: 0x9946002a0; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	11:28:23.357594-0500	Nexy	No scene exists for identity: com.apple.controlcenter:45B6D88E-6CFE-44D6-8FA2-83A300FBF752
default	11:28:23.357636-0500	Nexy	Requesting scene <FBSScene: 0x99134cdc0; com.apple.controlcenter:45B6D88E-6CFE-44D6-8FA2-83A300FBF752-Aux[5]-NSStatusItemView> from com.apple.controlcenter.statusitems
error	11:28:23.357816-0500	Nexy	Error creating <FBSScene: 0x99134cdc0; com.apple.controlcenter:45B6D88E-6CFE-44D6-8FA2-83A300FBF752-Aux[5]-NSStatusItemView>: <NSError: 0x994600870; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
default	11:28:23.357866-0500	Nexy	Request for <FBSScene: 0x99134cdc0; com.apple.controlcenter:45B6D88E-6CFE-44D6-8FA2-83A300FBF752-Aux[5]-NSStatusItemView> complete!
error	11:28:23.358047-0500	Nexy	scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	11:28:23.358067-0500	Nexy	[com.apple.controlcenter:45B6D88E-6CFE-44D6-8FA2-83A300FBF752] No matching scene to invalidate for this identity.
error	11:28:23.358097-0500	Nexy	auxiliary scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	11:28:23.358128-0500	Nexy	Unhandled disconnected scene <private>
error	11:28:23.358200-0500	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
default	11:28:24.050851-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Output {1C-77-54-18-C8-A3:output, 0xc}
default	11:28:24.051276-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1c5043","name":"Nexy(2761)"}, "details":{"deviceUIDs":[],"implicit_category":"","input_running":false,"output_running":false} }
default	11:28:24.051384-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsPlaying:]: MXCoreSession com.nexy.assistant with category/mode MediaPlayback/Default and coreSessionID = 68 stopping playing
default	11:28:24.051439-0500	audiomxd	-MXCoreSession- -[MXCoreSession endInterruption:]: Session <ID: 68, PID = 2761, Name = sid:0x1c5043, Nexy(2761), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> is going inactive
default	11:28:24.051476-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 68, PID = 2761, Name = sid:0x1c5043, Nexy(2761), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	11:28:24.051534-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 68, PID = 2761, Name = sid:0x1c5043, Nexy(2761), 'prim', BundleID = com.nexy.assistant, Category = MediaPlayback, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	11:28:24.051613-0500	audiomxd	UpdateAudioState CID 0x218B0001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	11:28:24.051660-0500	audiomxd	AudioApplicationInfoImpl.mm:395   Successfully updated session 0x1c5043 to isSessionRecording: 0
	app: {"name":"[implicit] Nexy","pid":2761}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1c5043, sessionType: 'prim', isRecording: false }, 
]
default	11:28:24.051722-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 0]. BT device UIDS: {(
)}
default	11:28:24.051731-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	11:28:24.051803-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	11:28:24.051868-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	11:28:24.051892-0500	audioaccessoryd	AudioStateChanged: Removed audio session app com.nexy.assistant 201 count 0
default	11:28:24.258523-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=2806.1, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=2761, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.osascript, pid=2806, auid=501, euid=501, binary_path=/usr/bin/osascript}, },
default	11:28:24.260063-0500	tccd	AUTHREQ_SUBJECT: msgID=2806.1, subject=com.nexy.assistant,
default	11:28:24.260694-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa5f977300 at /Applications/Nexy.app
default	11:28:24.276484-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=391.2249, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=2761, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.osascript, pid=2806, auid=501, euid=501, binary_path=/usr/bin/osascript}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=391, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	11:28:24.277482-0500	tccd	AUTHREQ_SUBJECT: msgID=391.2249, subject=com.nexy.assistant,
default	11:28:24.278079-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa5f977300 at /Applications/Nexy.app
default	11:28:24.307887-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa5f976400 at /Applications/Nexy.app
default	11:28:24.326260-0500	System Events	TCCAccessRequestIndirect: TCCAccessRequestIndirect with pid 2767: target_identity: {
    kTCCCodeIdentityAuditToken = {length = 32, bytes = 0xf5010000 f5010000 14000000 f5010000 ... b9860100 4f7b0300 };
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
default	11:28:24.345799-0500	tccd	target_executable_path_URL: file:///Applications/Nexy.app/Contents/MacOS/Nexy
default	11:28:24.359348-0500	Nexy	FBSWorkspace registering source: <private>
default	11:28:24.359380-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	11:28:24.359453-0500	Nexy	<FBSWorkspaceScenesClient:0x99134cd20 <private>> attempting immediate handshake from activate
default	11:28:24.359482-0500	Nexy	<FBSWorkspaceScenesClient:0x99134cd20 <private>> sent handshake
default	11:28:24.359707-0500	Nexy	Requesting scene <FBSScene: 0x99134c6e0; com.apple.controlcenter:77E23FE0-45E8-418B-B5B4-F458FB14B5AF> from com.apple.controlcenter.statusitems
default	11:28:24.359910-0500	Nexy	Request for <FBSScene: 0x99134c6e0; com.apple.controlcenter:77E23FE0-45E8-418B-B5B4-F458FB14B5AF> complete!
default	11:28:24.360246-0500	Nexy	Requesting scene <FBSScene: 0x99134cf00; com.apple.controlcenter:77E23FE0-45E8-418B-B5B4-F458FB14B5AF-Aux[6]-NSStatusItemView> from com.apple.controlcenter.statusitems
default	11:28:24.360366-0500	Nexy	<FBSWorkspaceScenesClient:0x99134cd20 <private>> was invalidated
default	11:28:24.360393-0500	Nexy	FBSWorkspace unregistering source: <private>
default	11:28:24.360441-0500	Nexy	Request for <FBSScene: 0x99134cf00; com.apple.controlcenter:77E23FE0-45E8-418B-B5B4-F458FB14B5AF-Aux[6]-NSStatusItemView> complete!
error	11:28:24.360450-0500	Nexy	Error creating <FBSScene: 0x99134c6e0; com.apple.controlcenter:77E23FE0-45E8-418B-B5B4-F458FB14B5AF>: <NSError: 0x9947446f0; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	11:28:24.360460-0500	Nexy	No scene exists for identity: com.apple.controlcenter:77E23FE0-45E8-418B-B5B4-F458FB14B5AF
error	11:28:24.360481-0500	Nexy	Error creating <FBSScene: 0x99134cf00; com.apple.controlcenter:77E23FE0-45E8-418B-B5B4-F458FB14B5AF-Aux[6]-NSStatusItemView>: <NSError: 0x994744a20; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	11:28:24.360491-0500	Nexy	No scene exists for identity: com.apple.controlcenter:77E23FE0-45E8-418B-B5B4-F458FB14B5AF-Aux[6]-NSStatusItemView
error	11:28:24.360594-0500	Nexy	scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	11:28:24.360605-0500	Nexy	[com.apple.controlcenter:77E23FE0-45E8-418B-B5B4-F458FB14B5AF] No matching scene to invalidate for this identity.
error	11:28:24.360629-0500	Nexy	auxiliary scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	11:28:24.360649-0500	Nexy	Unhandled disconnected scene <private>
error	11:28:24.360702-0500	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
default	11:28:25.362179-0500	Nexy	FBSWorkspace registering source: <private>
default	11:28:25.362236-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	11:28:25.362384-0500	Nexy	<FBSWorkspaceScenesClient:0x99134cf00 <private>> attempting immediate handshake from activate
default	11:28:25.362430-0500	Nexy	<FBSWorkspaceScenesClient:0x99134cf00 <private>> sent handshake
default	11:28:25.362894-0500	Nexy	Requesting scene <FBSScene: 0x99134c6e0; com.apple.controlcenter:C35F8D6F-0741-446E-B712-359B10950170> from com.apple.controlcenter.statusitems
default	11:28:25.363343-0500	Nexy	Request for <FBSScene: 0x99134c6e0; com.apple.controlcenter:C35F8D6F-0741-446E-B712-359B10950170> complete!
default	11:28:25.363843-0500	Nexy	<FBSWorkspaceScenesClient:0x99134cf00 <private>> was invalidated
default	11:28:25.363913-0500	Nexy	FBSWorkspace unregistering source: <private>
default	11:28:25.364006-0500	Nexy	FBSWorkspace registering source: <private>
default	11:28:25.364042-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	11:28:25.364131-0500	Nexy	<FBSWorkspaceScenesClient:0x99134ca00 <private>> attempting immediate handshake from activate
default	11:28:25.364171-0500	Nexy	<FBSWorkspaceScenesClient:0x99134ca00 <private>> sent handshake
error	11:28:25.364284-0500	Nexy	Error creating <FBSScene: 0x99134c6e0; com.apple.controlcenter:C35F8D6F-0741-446E-B712-359B10950170>: <NSError: 0x994600600; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	11:28:25.364320-0500	Nexy	No scene exists for identity: com.apple.controlcenter:C35F8D6F-0741-446E-B712-359B10950170
default	11:28:25.364449-0500	Nexy	Requesting scene <FBSScene: 0x99134c960; com.apple.controlcenter:C35F8D6F-0741-446E-B712-359B10950170-Aux[7]-NSStatusItemView> from com.apple.controlcenter.statusitems
default	11:28:25.364778-0500	Nexy	Request for <FBSScene: 0x99134c960; com.apple.controlcenter:C35F8D6F-0741-446E-B712-359B10950170-Aux[7]-NSStatusItemView> complete!
default	11:28:25.365067-0500	Nexy	<FBSWorkspaceScenesClient:0x99134ca00 <private>> was invalidated
default	11:28:25.365118-0500	Nexy	FBSWorkspace unregistering source: <private>
error	11:28:25.365215-0500	Nexy	Error creating <FBSScene: 0x99134c960; com.apple.controlcenter:C35F8D6F-0741-446E-B712-359B10950170-Aux[7]-NSStatusItemView>: <NSError: 0x994600ab0; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	11:28:25.365245-0500	Nexy	No scene exists for identity: com.apple.controlcenter:C35F8D6F-0741-446E-B712-359B10950170-Aux[7]-NSStatusItemView
default	11:28:25.365587-0500	Nexy	[com.apple.controlcenter:C35F8D6F-0741-446E-B712-359B10950170-Aux[7]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
error	11:28:25.365981-0500	Nexy	scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	11:28:25.366018-0500	Nexy	[com.apple.controlcenter:C35F8D6F-0741-446E-B712-359B10950170] No matching scene to invalidate for this identity.
error	11:28:25.366074-0500	Nexy	auxiliary scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	11:28:25.366106-0500	Nexy	[com.apple.controlcenter:C35F8D6F-0741-446E-B712-359B10950170-Aux[7]-NSStatusItemView] No matching scene to invalidate for this identity.
error	11:28:25.366724-0500	Nexy	Unhandled disconnected scene <private>
error	11:28:25.366841-0500	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
error	11:28:25.366931-0500	Nexy	Unhandled disconnected auxiliary scene <private>
error	11:28:25.366991-0500	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
default	11:28:26.367264-0500	Nexy	FBSWorkspace registering source: <private>
default	11:28:26.367290-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	11:28:26.367341-0500	Nexy	<FBSWorkspaceScenesClient:0x99134c960 <private>> attempting immediate handshake from activate
default	11:28:26.367362-0500	Nexy	<FBSWorkspaceScenesClient:0x99134c960 <private>> sent handshake
default	11:28:26.367530-0500	Nexy	Requesting scene <FBSScene: 0x99134c6e0; com.apple.controlcenter:1A16AEFC-7117-4AA9-BC8E-CC1B780307AC> from com.apple.controlcenter.statusitems
default	11:28:26.367680-0500	Nexy	Request for <FBSScene: 0x99134c6e0; com.apple.controlcenter:1A16AEFC-7117-4AA9-BC8E-CC1B780307AC> complete!
default	11:28:26.367883-0500	Nexy	<FBSWorkspaceScenesClient:0x99134c960 <private>> was invalidated
default	11:28:26.367903-0500	Nexy	FBSWorkspace unregistering source: <private>
default	11:28:26.367938-0500	Nexy	FBSWorkspace registering source: <private>
default	11:28:26.367950-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	11:28:26.367989-0500	Nexy	<FBSWorkspaceScenesClient:0x99134ca00 <private>> attempting immediate handshake from activate
default	11:28:26.368004-0500	Nexy	<FBSWorkspaceScenesClient:0x99134ca00 <private>> sent handshake
error	11:28:26.368047-0500	Nexy	Error creating <FBSScene: 0x99134c6e0; com.apple.controlcenter:1A16AEFC-7117-4AA9-BC8E-CC1B780307AC>: <NSError: 0x9946008a0; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	11:28:26.368062-0500	Nexy	No scene exists for identity: com.apple.controlcenter:1A16AEFC-7117-4AA9-BC8E-CC1B780307AC
default	11:28:26.368112-0500	Nexy	Requesting scene <FBSScene: 0x99134cf00; com.apple.controlcenter:1A16AEFC-7117-4AA9-BC8E-CC1B780307AC-Aux[8]-NSStatusItemView> from com.apple.controlcenter.statusitems
default	11:28:26.368237-0500	Nexy	Request for <FBSScene: 0x99134cf00; com.apple.controlcenter:1A16AEFC-7117-4AA9-BC8E-CC1B780307AC-Aux[8]-NSStatusItemView> complete!
default	11:28:26.368351-0500	Nexy	<FBSWorkspaceScenesClient:0x99134ca00 <private>> was invalidated
default	11:28:26.368367-0500	Nexy	FBSWorkspace unregistering source: <private>
error	11:28:26.368407-0500	Nexy	Error creating <FBSScene: 0x99134cf00; com.apple.controlcenter:1A16AEFC-7117-4AA9-BC8E-CC1B780307AC-Aux[8]-NSStatusItemView>: <NSError: 0x9946008d0; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	11:28:26.368418-0500	Nexy	No scene exists for identity: com.apple.controlcenter:1A16AEFC-7117-4AA9-BC8E-CC1B780307AC-Aux[8]-NSStatusItemView
default	11:28:26.369745-0500	Nexy	[com.apple.controlcenter:1A16AEFC-7117-4AA9-BC8E-CC1B780307AC-Aux[8]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
error	11:28:26.369940-0500	Nexy	scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	11:28:26.369952-0500	Nexy	[com.apple.controlcenter:1A16AEFC-7117-4AA9-BC8E-CC1B780307AC] No matching scene to invalidate for this identity.
error	11:28:26.369976-0500	Nexy	auxiliary scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	11:28:26.369987-0500	Nexy	[com.apple.controlcenter:1A16AEFC-7117-4AA9-BC8E-CC1B780307AC-Aux[8]-NSStatusItemView] No matching scene to invalidate for this identity.
error	11:28:26.370238-0500	Nexy	Unhandled disconnected scene <private>
error	11:28:26.370306-0500	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
error	11:28:26.370347-0500	Nexy	Unhandled disconnected auxiliary scene <private>
error	11:28:26.370378-0500	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
