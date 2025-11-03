default	17:17:25.438324-0500	lsd	com.nexy.assistant/Unknown Persona:5:5:1:1:Building bundle record for app
default	17:17:25.438446-0500	lsd	com.nexy.assistant/Unknown Persona:5:5:2:1:Built bundle record for app
default	17:17:25.439723-0500	lsd	com.nexy.assistant/Unknown Persona:5:4:2:1:_LSServerRegisterItemInfo result = 0
default	17:17:25.444989-0500	runningboardd	Launch request for app<application.com.nexy.assistant.20408399.20408405(501)>[0] is using uid 501 (divined from auid 501 euid 501)
default	17:17:25.445048-0500	runningboardd	Acquiring assertion targeting app<application.com.nexy.assistant.20408399.20408405(501)> from originator [osservice<com.apple.coreservices.uiagent(501)>:46006] with description <RBSAssertionDescriptor| "LS launch com.nexy.assistant" ID:398-46006-1382176 target:app<application.com.nexy.assistant.20408399.20408405(501)> attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"LaunchRoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	17:17:25.445111-0500	runningboardd	Assertion 398-46006-1382176 (target:app<application.com.nexy.assistant.20408399.20408405(501)>) will be created as active
default	17:17:25.444611-0500	dmd	Received xpc stream event (distributed notification matching) with name: com.apple.LaunchServices.applicationRegistered user info: {
    CFBundleDisplayName = Nexy;
    bundleIDs =     (
        "com.nexy.assistant"
    );
    isPlaceholder = 0;
}
default	17:17:25.448874-0500	runningboardd	Checking PreventLaunch: global:0 exPath:/Applications/Nexy.app/Contents/MacOS/Nexy predicates:(null) allow:(null)
default	17:17:25.448899-0500	runningboardd	Creating and launching job for: app<application.com.nexy.assistant.20408399.20408405(501)>
default	17:17:25.448910-0500	runningboardd	_mutateContextIfNeeded called for com.nexy.assistant
default	17:17:25.448951-0500	runningboardd	app<application.com.nexy.assistant.20408399.20408405(501)>: -[RBPersonaManager personaForIdentity:context:personaUID:personaUniqueString:] required 0.000000 ms (wallclock); resolved to {4294967295, (null)}
default	17:17:25.477834-0500	runningboardd	[app<application.com.nexy.assistant.20408399.20408405(501)>:98990] is not RunningBoard jetsam managed.
default	17:17:25.477845-0500	runningboardd	[app<application.com.nexy.assistant.20408399.20408405(501)>:98990] This process will not be managed.
default	17:17:25.477854-0500	runningboardd	Now tracking process: [app<application.com.nexy.assistant.20408399.20408405(501)>:98990]
default	17:17:25.477994-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.20408399.20408405(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	17:17:25.478566-0500	gamepolicyd	Hit the server for a process handle cdf981f000182ae that resolved to: [app<application.com.nexy.assistant.20408399.20408405(501)>:98990]
default	17:17:25.478591-0500	gamepolicyd	Received state update for 98990 (app<application.com.nexy.assistant.20408399.20408405(501)>, running-active-NotVisible
default	17:17:25.481272-0500	runningboardd	Using default underlying assertion for app: [app<application.com.nexy.assistant.20408399.20408405(501)>:98990]
default	17:17:25.481318-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.20408399.20408405(501)>:98990] from originator [app<application.com.nexy.assistant.20408399.20408405(501)>:98990] with description <RBSAssertionDescriptor| "RB Underlying Assertion" ID:398-398-1382177 target:98990 attributes:[
	<RBSDomainAttribute| domain:"com.apple.underlying" name:"defaultUnderlyingAppAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	17:17:25.481394-0500	runningboardd	Assertion 398-398-1382177 (target:[app<application.com.nexy.assistant.20408399.20408405(501)>:98990]) will be created as active
default	17:17:25.481517-0500	runningboardd	[app<application.com.nexy.assistant.20408399.20408405(501)>:98990] Ignoring jetsam update because this process is not memory-managed
default	17:17:25.481530-0500	runningboardd	[app<application.com.nexy.assistant.20408399.20408405(501)>:98990] Ignoring suspend because this process is not lifecycle managed
default	17:17:25.481547-0500	runningboardd	[app<application.com.nexy.assistant.20408399.20408405(501)>:98990] Set darwin role to: UserInteractive
default	17:17:25.481559-0500	runningboardd	[app<application.com.nexy.assistant.20408399.20408405(501)>:98990] Ignoring GPU update because this process is not GPU managed
default	17:17:25.481587-0500	runningboardd	[app<application.com.nexy.assistant.20408399.20408405(501)>:98990] Ignoring memory limit update because this process is not memory-managed
default	17:17:25.481601-0500	runningboardd	[app<application.com.nexy.assistant.20408399.20408405(501)>:98990] reported to RB as running
default	17:17:25.482497-0500	CoreServicesUIAgent	LAUNCH: 0x0-0x1482481 com.nexy.assistant starting stopped process.
default	17:17:25.482538-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.20408399.20408405(501)>:98990] from originator [osservice<com.apple.coreservices.launchservicesd>:363] with description <RBSAssertionDescriptor| "uielement:98990" ID:398-363-1382178 target:98990 attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"RoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	17:17:25.482630-0500	runningboardd	Assertion 398-363-1382178 (target:[app<application.com.nexy.assistant.20408399.20408405(501)>:98990]) will be created as active
default	17:17:25.483383-0500	loginwindow	-[Application updateInformation] | Got App URL: file:///Applications/Nexy.app/
default	17:17:25.483519-0500	loginwindow	-[ApplicationManager checkInAppContext:eventData:] | ApplicationManager: Checked in app : Nexy
default	17:17:25.485507-0500	runningboardd	[app<application.com.nexy.assistant.20408399.20408405(501)>:98990] Ignoring jetsam update because this process is not memory-managed
default	17:17:25.485531-0500	runningboardd	[app<application.com.nexy.assistant.20408399.20408405(501)>:98990] Ignoring suspend because this process is not lifecycle managed
default	17:17:25.485555-0500	runningboardd	[app<application.com.nexy.assistant.20408399.20408405(501)>:98990] Ignoring GPU update because this process is not GPU managed
default	17:17:25.485599-0500	runningboardd	[app<application.com.nexy.assistant.20408399.20408405(501)>:98990] Ignoring memory limit update because this process is not memory-managed
default	17:17:25.485661-0500	runningboardd	Successfully acquired underlying assertion for [app<application.com.nexy.assistant.20408399.20408405(501)>:98990]
default	17:17:25.486386-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.20408399.20408405(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	17:17:25.486558-0500	runningboardd	Invalidating assertion 398-46006-1382176 (target:app<application.com.nexy.assistant.20408399.20408405(501)>) from originator [osservice<com.apple.coreservices.uiagent(501)>:46006]
default	17:17:25.486639-0500	gamepolicyd	Received state update for 98990 (app<application.com.nexy.assistant.20408399.20408405(501)>, running-active-NotVisible
default	17:17:25.486584-0500	runningboardd	[app<application.com.nexy.assistant.20408399.20408405(501)>:98990] Ignoring jetsam update because this process is not memory-managed
default	17:17:25.486607-0500	runningboardd	[app<application.com.nexy.assistant.20408399.20408405(501)>:98990] Ignoring suspend because this process is not lifecycle managed
default	17:17:25.486649-0500	runningboardd	[app<application.com.nexy.assistant.20408399.20408405(501)>:98990] Ignoring GPU update because this process is not GPU managed
default	17:17:25.486732-0500	runningboardd	[app<application.com.nexy.assistant.20408399.20408405(501)>:98990] Ignoring memory limit update because this process is not memory-managed
default	17:17:25.489917-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.20408399.20408405(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	17:17:25.547146-0500	runningboardd	[app<application.com.nexy.assistant.20408399.20408405(501)>:98990] Ignoring jetsam update because this process is not memory-managed
default	17:17:25.547156-0500	runningboardd	[app<application.com.nexy.assistant.20408399.20408405(501)>:98990] Ignoring suspend because this process is not lifecycle managed
default	17:17:25.547167-0500	runningboardd	[app<application.com.nexy.assistant.20408399.20408405(501)>:98990] Ignoring GPU update because this process is not GPU managed
default	17:17:25.547183-0500	runningboardd	[app<application.com.nexy.assistant.20408399.20408405(501)>:98990] Ignoring memory limit update because this process is not memory-managed
default	17:17:25.550654-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.20408399.20408405(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	17:17:25.589323-0500	gamepolicyd	Received state update for 98990 (app<application.com.nexy.assistant.20408399.20408405(501)>, running-active-NotVisible
default	17:17:25.652273-0500	syspolicyd	GK evaluateScanResult: 3, PST: (path: a2cffff67b96be6e), (team: 5NKLL2CLB9), (id: com.nexy.assistant), (bundle_id: (null)), 0, 0, 1, 0, 9, 4, 1
default	17:17:25.653744-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=511.135, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=98990, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.syspolicyd, pid=511, auid=0, euid=0, binary_path=/usr/libexec/syspolicyd}, },
default	17:17:25.658904-0500	tccd	AUTHREQ_SUBJECT: msgID=511.135, subject=com.nexy.assistant,
default	17:17:25.659431-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d114900 at /Applications/Nexy.app
default	17:17:25.669857-0500	kernel	Nexy[98990] triggered unnest of range 0x1f6000000->0x1f8000000 of DYLD shared region in VM map 0x1647724d0562001. While not abnormal for debuggers, this increases system memory footprint until the target exits.
default	17:17:25.669873-0500	kernel	Nexy[98990] triggered unnest of range 0x1f8000000->0x1fa000000 of DYLD shared region in VM map 0x1647724d0562001. While not abnormal for debuggers, this increases system memory footprint until the target exits.
default	17:17:25.897041-0500	Nexy	[0x103bcf090] activating connection: mach=true listener=false peer=false name=com.apple.cfprefsd.daemon
default	17:17:25.897078-0500	Nexy	[0x103bcf1d0] activating connection: mach=true listener=false peer=false name=com.apple.cfprefsd.agent
error	17:17:25.973280-0500	Nexy	dlsym cannot find symbol NSMakeRect in CFBundle 0x9a17ac000 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	17:17:25.973403-0500	Nexy	dlsym cannot find symbol NSMakePoint in CFBundle 0x9a17ac000 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	17:17:25.973515-0500	Nexy	dlsym cannot find symbol NSMakeSize in CFBundle 0x9a17ac000 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	17:17:25.973623-0500	Nexy	dlsym cannot find symbol NSMakeRange in CFBundle 0x9a17ac000 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
default	17:17:26.022661-0500	Nexy	Registered notify signal com.apple.caulk.alloc.rtdump (0)
default	17:17:26.024163-0500	Nexy	System_Input_Processing_Notification_Handler.mm:456   System_Input_Processing_Notification_Handler::is_vi_available(): Voice isolation DSP is available for client with bundle id com.nexy.assistant (AVFoundation is available, application is not in client deny list, application is not FaceTime variant)
default	17:17:26.025182-0500	Nexy	[0x103bd38d0] activating connection: mach=true listener=false peer=false name=com.apple.cmio.registerassistantservice.system-extensions
fault	17:17:26.026895-0500	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.20408399.20408405 AUID=501> and <type=Application identifier=application.com.nexy.assistant.20408399.20408405>
default	17:17:26.029474-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOInitializeListenersForBundleID: for <private> -> <private>
default	17:17:26.030689-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> vpio_preferenceChangedListener: new value ((null)) for key AUVoiceIOClients/com-nexy-assistant/AUVoiceIOChatFlavor, translatedBundleID com.nexy.assistant, bundleIDs {(
    "com.nexy.assistant"
)}
default	17:17:26.030783-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> vpio_preferenceChangedListener: new value ((null)) for key AUVoiceIOClients/com-nexy-assistant/AUVoiceIOIsAutoChatFlavorEnabled, translatedBundleID com.nexy.assistant, bundleIDs {(
    "com.nexy.assistant"
)}
default	17:17:26.030857-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetSupportedChatFlavorsForBundleID: <private>-><private> get supported chat flavors: <private>
default	17:17:26.030863-0500	Nexy	            HALSystem.cpp:134    Enabling HAL Voice Isolation support
default	17:17:26.030987-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetHiddenChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	17:17:26.031086-0500	Nexy	[0x99fc08000] activating connection: mach=true listener=false peer=false name=com.apple.tccd
default	17:17:26.031174-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOHiddenChatFlavors newValue: (
    1
)
default	17:17:26.031704-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=98990.1, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=98990, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	17:17:26.035087-0500	tccd	AUTHREQ_SUBJECT: msgID=98990.1, subject=com.nexy.assistant,
default	17:17:26.035422-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa0b1a8600 at /Applications/Nexy.app
default	17:17:26.041565-0500	Nexy	[0x99fc08000] invalidated after the last release of the connection object
default	17:17:26.041595-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetSupportedChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	17:17:26.043301-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOSupportedChatFlavors newValue: (
)
default	17:17:26.044425-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.7501, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=98990, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	17:17:26.045084-0500	tccd	AUTHREQ_SUBJECT: msgID=401.7501, subject=com.nexy.assistant,
default	17:17:26.045659-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa0b1a8600 at /Applications/Nexy.app
error	17:17:26.052110-0500	tccd	Request message contains a target_token to accessing_process (TCCDProcess: identifier=com.nexy.assistant, pid=98990, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy) but TCCDProcess: identifier=com.apple.audio.coreaudiod, pid=401, auid=202, euid=202, binary_path=/usr/sbin/coreaudiod is not a TCC manager for service: kTCCServiceScreenCapture.
default	17:17:26.052561-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.7503, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=98990, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	17:17:26.052964-0500	tccd	AUTHREQ_SUBJECT: msgID=401.7503, subject=com.nexy.assistant,
default	17:17:26.053267-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa0b1a8600 at /Applications/Nexy.app
default	17:17:26.060662-0500	Nexy	  HALPlugInManagement.cpp:440    HALPlugInManagement::RegisterPlugIns: skipping in-process plug-ins
error	17:17:26.060784-0500	Nexy	AddInstanceForFactory: No factory registered for id <CFUUID 0x9a1024e60> F8BB1C28-BAE8-11D6-9C31-00039315CD46
default	17:17:26.076880-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	17:17:26.076965-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	17:17:26.079619-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetPreferredChatFlavorForBundleID: <private>-><private> get value: 0
default	17:17:27.326744-0500	kernel	SK[9]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid D51A9103-02C2-4FB6-95BF-84CC14A5F2FE flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.57410,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0x24b01f6c tp_proto=0x06"
default	17:17:27.326776-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:57410<-><IPv4-redacted>:53] interface: utun6 (skipped: 6843)
so_gencnt: 5135785 t_state: SYN_SENT process: Nexy:98990 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xa37aeb1d
default	17:17:27.327158-0500	kernel	tcp connected: [<IPv4-redacted>:57410<-><IPv4-redacted>:53] interface: utun6 (skipped: 6843)
so_gencnt: 5135785 t_state: ESTABLISHED process: Nexy:98990 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xa37aeb1d
default	17:17:27.327315-0500	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:57410<-><IPv4-redacted>:53] interface: utun6 (skipped: 6843)
so_gencnt: 5135785 t_state: FIN_WAIT_1 process: Nexy:98990 Duration: 0.001 sec Conn_Time: 0.001 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 1.000 ms rttvar: 0.500 ms base rtt: 1 ms so_error: 0 svc/tc: 0 flow: 0xa37aeb1d
default	17:17:27.327321-0500	kernel	tcp_connection_summary [<IPv4-redacted>:57410<-><IPv4-redacted>:53] interface: utun6 (skipped: 6843)
so_gencnt: 5135785 t_state: FIN_WAIT_1 process: Nexy:98990 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	17:17:27.345510-0500	Nexy	[0x99fc08000] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioComponentRegistrar
default	17:17:27.354581-0500	Nexy	                AUHAL.cpp:420   AUHAL: (0x9a18c8740) Selecting device 85 from constructor
default	17:17:27.354587-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0x9a18c8740)
default	17:17:27.354590-0500	Nexy	                AUHAL.cpp:676   SelectDevice: (0x9a18c8740) not already running
default	17:17:27.354593-0500	Nexy	                AUHAL.cpp:752   SelectDevice: (0x9a18c8740) nothing to teardown
default	17:17:27.354594-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0x9a18c8740) connecting device 85
default	17:17:27.354636-0500	Nexy	                AUHAL.cpp:3413  IsDeviceUsable: (0x9a18c8740) Device ID: 85 (Input:No | Output:Yes): true
default	17:17:27.354953-0500	Nexy	                AUHAL.cpp:769   SelectDevice: (0x9a18c8740) created ioproc 0xa for device 85
default	17:17:27.355036-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x9a18c8740) adding 7 device listeners to device 85
default	17:17:27.355122-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x9a18c8740) adding 0 device delegate listeners to device 85
default	17:17:27.355125-0500	Nexy	                AUHAL.cpp:1581  UpdateStreamFormats: -> (0x9a18c8740)
default	17:17:27.355161-0500	Nexy	                AUHAL.cpp:1677  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  48000 Hz, Float32, interleaved
default	17:17:27.355165-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 1 output streams; not all mono
default	17:17:27.355171-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	17:17:27.355175-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 0 input streams; not all mono
default	17:17:27.355180-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	17:17:27.355231-0500	Nexy	                AUHAL.cpp:1771  UpdateStreamFormats: AUHAL(0x9a18c8740) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	17:17:27.355236-0500	Nexy	                AUHAL.cpp:1777  UpdateStreamFormats: AUHAL(0x9a18c8740) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	17:17:27.355237-0500	Nexy	                AUHAL.cpp:1787  UpdateStreamFormats: <-
default	17:17:27.355240-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x9a18c8740) removing 0 device listeners from device 0
default	17:17:27.355242-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x9a18c8740) removing 0 device delegate listeners from device 0
default	17:17:27.355257-0500	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0x9a18c8740)
default	17:17:27.355303-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Output stream enables: Stream 0 is DISABLED
default	17:17:27.355393-0500	Nexy	                AUHAL.cpp:2298  SetProperty: (0x9a18c8740) caller requesting device change from 85 to 91
default	17:17:27.355397-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0x9a18c8740)
default	17:17:27.355400-0500	Nexy	                AUHAL.cpp:676   SelectDevice: (0x9a18c8740) not already running
default	17:17:27.355401-0500	Nexy	                AUHAL.cpp:682   SelectDevice: (0x9a18c8740) disconnecting device 85
default	17:17:27.355405-0500	Nexy	                AUHAL.cpp:746   SelectDevice: (0x9a18c8740) destroying ioproc 0xa for device 85
default	17:17:27.355428-0500	Nexy	  AVAudioSession_MacOS.mm:1021  initForMacOS
default	17:17:27.356105-0500	Nexy	[0x99fc08280] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioSession
default	17:17:27.356915-0500	audiomxd	  ServerSessionManager.mm:315   { "action":"create_session", "session":{"ID":"0x1ef195","name":"Nexy(98990)"}, "details":{"PID":98990,"session_type":"Primary"} }
default	17:17:27.356961-0500	audiomxd	AudioApplicationInfoImpl.mm:250   Setting initial isRecording state: 0 for newly-created AudioApp
	app: {"name":"[implicit] Nexy","pid":98990}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1ef195, sessionType: 'prim', isRecording: false }, 
]
default	17:17:27.357302-0500	audiomxd	  ServerSessionManager.mm:1317  Start process monitoring, pid = 98990, name = Nexy
default	17:17:27.357445-0500	Nexy	    SessionCore_Create.mm:99    Created session 0x9a06ce680 with ID: 0x1ef195
default	17:17:27.358305-0500	Nexy	[0x99fc083c0] activating connection: mach=true listener=false peer=false name=com.apple.audioanalyticsd
default	17:17:27.358376-0500	Nexy	No persisted cache on this platform.
error	17:17:27.358534-0500	Nexy	Reporter disconnected. { function=sendMessage, reporterID=425158812631041 }
default	17:17:27.358542-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped Unknown {1C-77-54-18-C8-A3:output, 0xa}
default	17:17:27.358570-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	17:17:27.358622-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0x9a18c8740) connecting device 91
default	17:17:27.358666-0500	Nexy	                AUHAL.cpp:3413  IsDeviceUsable: (0x9a18c8740) Device ID: 91 (Input:Yes | Output:No): true
default	17:17:27.359303-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.7504, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=98990, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	17:17:27.360034-0500	tccd	AUTHREQ_SUBJECT: msgID=401.7504, subject=com.nexy.assistant,
default	17:17:27.360723-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa0b1a8600 at /Applications/Nexy.app
default	17:17:27.366930-0500	tccd	AUTHREQ_PROMPTING: msgID=401.7504, service=kTCCServiceMicrophone, subject=Sub:{com.nexy.assistant}Resp:{TCCDProcess: identifier=com.nexy.assistant, pid=98990, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy},
default	17:17:28.858432-0500	Nexy	                AUHAL.cpp:769   SelectDevice: (0x9a18c8740) created ioproc 0xa for device 91
default	17:17:28.858773-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x9a18c8740) adding 7 device listeners to device 91
default	17:17:28.859195-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x9a18c8740) adding 0 device delegate listeners to device 91
default	17:17:28.859216-0500	Nexy	                AUHAL.cpp:1581  UpdateStreamFormats: -> (0x9a18c8740)
default	17:17:28.859236-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 0 output streams; not all mono
default	17:17:28.859260-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Output render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	17:17:28.859579-0500	Nexy	                AUHAL.cpp:1677  UpdateStreamFormats: 
  input stream 0 [0x5c]:  1 ch,  24000 Hz, Float32
default	17:17:28.859592-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 1 input streams; all mono
default	17:17:28.857651-0500	tccd	Publishing <TCCDEvent: type=Create, service=kTCCServiceMicrophone, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 3 subscribers: {
    471 = "<TCCDEventSubscriber: token=471, state=Passed, csid=com.apple.chronod>";
    37 = "<TCCDEventSubscriber: token=37, state=Passed, csid=com.apple.cloudd>";
    476 = "<TCCDEventSubscriber: token=476, state=Passed, csid=com.apple.photolibraryd>";
}
default	17:17:28.859601-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Input render format:  1 ch,  24000 Hz, Float32
default	17:17:28.859819-0500	Nexy	                AUHAL.cpp:1771  UpdateStreamFormats: AUHAL(0x9a18c8740) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	17:17:28.859864-0500	Nexy	                AUHAL.cpp:1777  UpdateStreamFormats: AUHAL(0x9a18c8740) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	17:17:28.859875-0500	Nexy	                AUHAL.cpp:1787  UpdateStreamFormats: <-
default	17:17:28.859884-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x9a18c8740) removing 7 device listeners from device 85
default	17:17:28.860191-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x9a18c8740) removing 0 device delegate listeners from device 85
default	17:17:28.860204-0500	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0x9a18c8740)
default	17:17:28.860503-0500	chronod	[appAuth:com.nexy.assistant] tcc authorization(s) changed
default	17:17:28.861344-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	17:17:28.863315-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.7505, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=98990, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	17:17:28.864883-0500	tccd	AUTHREQ_SUBJECT: msgID=401.7505, subject=com.nexy.assistant,
default	17:17:28.866281-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa0b1a8600 at /Applications/Nexy.app
default	17:17:28.885401-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	17:17:28.886773-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.7506, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=98990, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	17:17:28.887931-0500	tccd	AUTHREQ_SUBJECT: msgID=401.7506, subject=com.nexy.assistant,
default	17:17:28.888493-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa0b1a8600 at /Applications/Nexy.app
default	17:17:28.900439-0500	Nexy	Registered notify signal com.apple.caulk.alloc.audiodump (0)
default	17:17:28.901700-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.7507, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=98990, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	17:17:28.902345-0500	tccd	AUTHREQ_SUBJECT: msgID=401.7507, subject=com.nexy.assistant,
default	17:17:28.902769-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa0b1a8600 at /Applications/Nexy.app
default	17:17:28.912596-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetPreferredChatFlavorForBundleID: <private>-><private> get value: 0
default	17:17:28.912828-0500	coreaudiod	>>> NEGOTIATE [com.nexy.assistant]
default	17:17:28.913026-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetSupportedChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	17:17:28.912925-0500	coreaudiod	<<< NEGOTIATE [com.nexy.assistant]
default	17:17:28.914372-0500	coreaudiod	>>> ADAPT [com.nexy.assistant]
default	17:17:28.914860-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOSupportedChatFlavors newValue: (
    0,
    2
)
default	17:17:28.915849-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xbf6d85200] Created node ADM::com.nexy.assistant_50308.50234.0_airpods noise suppression studio::in-0 with nodeID 0 - reporting period = 10.000000, sample rate = 24000.000000
default	17:17:28.915896-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xbf6d85200] Created node ADM::com.nexy.assistant_50308.50234.0_airpods noise suppression studio::out-0 with nodeID 1 - reporting period = 10.000000, sample rate = 24000.000000
default	17:17:28.974857-0500	coreaudiod	<<< ADAPT [com.nexy.assistant]
default	17:17:28.976083-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Input {1C-77-54-18-C8-A3:input, 0xa}
default	17:17:28.976061-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:50308 called from <private>
default	17:17:28.977945-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:50308 called from <private>
default	17:17:28.979341-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.20408399.20408405(501)>:98990] from originator [osservice<com.apple.powerd>:334] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:398-334-1382200 target:98990 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	17:17:28.980205-0500	runningboardd	Assertion 398-334-1382200 (target:[app<application.com.nexy.assistant.20408399.20408405(501)>:98990]) will be created as active
default	17:17:28.981436-0500	runningboardd	[app<application.com.nexy.assistant.20408399.20408405(501)>:98990] Ignoring jetsam update because this process is not memory-managed
default	17:17:28.981518-0500	runningboardd	[app<application.com.nexy.assistant.20408399.20408405(501)>:98990] Ignoring suspend because this process is not lifecycle managed
default	17:17:28.981671-0500	runningboardd	[app<application.com.nexy.assistant.20408399.20408405(501)>:98990] Ignoring GPU update because this process is not GPU managed
default	17:17:28.981678-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	17:17:28.981780-0500	runningboardd	[app<application.com.nexy.assistant.20408399.20408405(501)>:98990] Ignoring memory limit update because this process is not memory-managed
default	17:17:28.982299-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	17:17:28.978081-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(50308)
default	17:17:28.978091-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:50308 called from <private>
default	17:17:28.978096-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:50308 called from <private>
default	17:17:28.978219-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(50307)
default	17:17:28.978296-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:50307 called from <private>
default	17:17:28.978332-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:50307 called from <private>
default	17:17:28.985404-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(50308)
default	17:17:28.985419-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:50308 called from <private>
default	17:17:28.985424-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:50308 called from <private>
default	17:17:28.985433-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(50308)
default	17:17:28.985440-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(50308)
default	17:17:28.985445-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:50308 called from <private>
default	17:17:28.985449-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:50308 called from <private>
default	17:17:28.985466-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:50308 called from <private>
default	17:17:28.985476-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(50308)
default	17:17:28.996366-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ef195","name":"Nexy(98990)"}, "details":{"deviceUIDs":["1C-77-54-18-C8-A3:input"],"implicit_category":"Record","input_running":true,"output_running":false} }
default	17:17:28.997345-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 406, PID = 98990, Name = sid:0x1ef195, Nexy(98990), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	17:17:28.997782-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 406, PID = 98990, Name = sid:0x1ef195, Nexy(98990), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	17:17:28.998028-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 406, PID = 98990, Name = sid:0x1ef195, Nexy(98990), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	17:17:28.997957-0500	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1ef195, Nexy(98990), 'prim'', AudioCategory changed to 'Record_WithBluetooth'
default	17:17:28.998120-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 406, PID = 98990, Name = sid:0x1ef195, Nexy(98990), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	17:17:28.985513-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:50308 called from <private>
default	17:17:28.985590-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:50308 called from <private>
default	17:17:28.985631-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:50308 called from <private>
default	17:17:28.998307-0500	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 406, PID = 98990, Name = sid:0x1ef195, Nexy(98990), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> is going active
default	17:17:28.998354-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1ef195, Nexy(98990), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 406 starting recording
default	17:17:28.998070-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	17:17:28.998927-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 406, PID = 98990, Name = sid:0x1ef195, Nexy(98990), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	17:17:28.988807-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:50308 called from <private>
default	17:17:28.988812-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:50308 called from <private>
default	17:17:28.998914-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	17:17:28.996102-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(50308)
default	17:17:28.999075-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 406, PID = 98990, Name = sid:0x1ef195, Nexy(98990), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	17:17:28.996402-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:50308 called from <private>
default	17:17:28.998548-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	17:17:28.999142-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1ef195, Nexy(98990), 'prim'', displayID:'com.nexy.assistant'}
default	17:17:28.999130-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	17:17:28.999311-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [1, 0]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:input"
)}
default	17:17:29.999594-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	17:17:28.999349-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	17:17:29.000910-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:50307 called from <private>
default	17:17:29.001403-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.7508, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=98990, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	17:17:29.000951-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:50307 called from <private>
default	17:17:29.003138-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(50307)
fault	17:17:29.006514-0500	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.20408399.20408405 AUID=501> and <type=Application identifier=application.com.nexy.assistant.20408399.20408405>
default	17:17:29.007968-0500	tccd	AUTHREQ_SUBJECT: msgID=401.7508, subject=com.nexy.assistant,
default	17:17:29.008898-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa0b1a8600 at /Applications/Nexy.app
default	17:17:29.010596-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.20408399.20408405(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	17:17:29.011956-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:50307 called from <private>
default	17:17:29.011965-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:50307 called from <private>
default	17:17:29.012059-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(50307)
fault	17:17:29.009306-0500	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.20408399.20408405 AUID=501> and <type=Application identifier=application.com.nexy.assistant.20408399.20408405>
default	17:17:29.014893-0500	runningboardd	Invalidating assertion 398-334-1382200 (target:[app<application.com.nexy.assistant.20408399.20408405(501)>:98990]) from originator [osservice<com.apple.powerd>:334]
default	17:17:29.015880-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(50307)
default	17:17:29.016068-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:50307 called from <private>
default	17:17:29.016074-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:50307 called from <private>
default	17:17:29.016127-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(50307)
default	17:17:29.036405-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	17:17:29.043035-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.7509, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=98990, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	17:17:29.043618-0500	runningboardd	Invalidating assertion 398-334-1382201 (target:[app<application.com.nexy.assistant.20408399.20408405(501)>:98990]) from originator [osservice<com.apple.powerd>:334]
default	17:17:29.055978-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	17:17:29.056679-0500	coreaudiod	>>> ADAPT [com.nexy.assistant]
default	17:17:29.061197-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	17:17:29.061204-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	17:17:29.061208-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	17:17:29.061213-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	17:17:29.061217-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	17:17:29.061218-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	17:17:29.061291-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	17:17:29.061610-0500	ControlCenter	Navigating to new application [com.nexy.assistant]
default	17:17:29.079080-0500	coreaudiod	<<< ADAPT [com.nexy.assistant]
default	17:17:29.079775-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.20408399.20408405(501)>:98990] from originator [osservice<com.apple.powerd>:334] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:398-334-1382202 target:98990 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	17:17:29.079818-0500	runningboardd	Assertion 398-334-1382202 (target:[app<application.com.nexy.assistant.20408399.20408405(501)>:98990]) will be created as active
default	17:17:29.080801-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:50308 called from <private>
default	17:17:29.080823-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:50308 called from <private>
default	17:17:29.080981-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	17:17:29.083535-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:50308 called from <private>
default	17:17:29.083702-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(50308)
default	17:17:29.083713-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:50308 called from <private>
default	17:17:29.083715-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:50308 called from <private>
default	17:17:29.083803-0500	runningboardd	Invalidating assertion 398-334-1382202 (target:[app<application.com.nexy.assistant.20408399.20408405(501)>:98990]) from originator [osservice<com.apple.powerd>:334]
default	17:17:29.084264-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	17:17:29.084393-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	17:17:29.084922-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(50308)
default	17:17:29.085031-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:50308 called from <private>
default	17:17:29.085040-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:50308 called from <private>
default	17:17:29.085048-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:50308 called from <private>
default	17:17:29.086157-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.7510, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=98990, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	17:17:29.086899-0500	tccd	AUTHREQ_SUBJECT: msgID=401.7510, subject=com.nexy.assistant,
default	17:17:29.087577-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa0b1a8600 at /Applications/Nexy.app
default	17:17:29.087871-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	17:17:29.087902-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	17:17:29.087923-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	17:17:29.088066-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	17:17:29.088187-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	17:17:29.088192-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	17:17:29.088198-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	17:17:29.088201-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	17:17:29.088207-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	17:17:29.088210-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	17:17:29.088407-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	17:17:29.088479-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	17:17:29.088592-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	17:17:29.088689-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	17:17:29.088757-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	17:17:29.088879-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	17:17:29.088906-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	17:17:29.090056-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	17:17:29.097273-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.20408399.20408405(501)>:98990] from originator [osservice<com.apple.powerd>:334] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:398-334-1382203 target:98990 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	17:17:29.097313-0500	runningboardd	Assertion 398-334-1382203 (target:[app<application.com.nexy.assistant.20408399.20408405(501)>:98990]) will be created as active
default	17:17:29.098687-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:50308 called from <private>
default	17:17:29.103899-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	17:17:29.103921-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	17:17:29.103941-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	17:17:29.104156-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	17:17:29.104201-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	17:17:29.104300-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	17:17:29.104361-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	17:17:29.104407-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	17:17:29.104455-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	17:17:29.104553-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	17:17:29.104621-0500	ControlCenter	Navigating to new application [com.nexy.assistant]
default	17:17:29.104604-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	17:17:29.104695-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	17:17:29.104706-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	17:17:29.104825-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	17:17:29.104856-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	17:17:30.128649-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xa}
default	17:17:30.129046-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ef195","name":"Nexy(98990)"}, "details":{"deviceUIDs":[],"implicit_category":"","input_running":false,"output_running":false} }
default	17:17:30.129245-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 406, PID = 98990, Name = sid:0x1ef195, Nexy(98990), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	17:17:30.129355-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 406, PID = 98990, Name = sid:0x1ef195, Nexy(98990), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	17:17:30.129417-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1ef195, Nexy(98990), 'prim'', displayID:'com.nexy.assistant'}
default	17:17:30.129525-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	17:17:30.129528-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1ef195, Nexy(98990), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 406 stopping recording
default	17:17:30.129584-0500	audiomxd	-MXCoreSession- -[MXCoreSession endInterruption:]: Session <ID: 406, PID = 98990, Name = sid:0x1ef195, Nexy(98990), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> is going inactive
default	17:17:30.129657-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 406, PID = 98990, Name = sid:0x1ef195, Nexy(98990), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	17:17:30.129755-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 406, PID = 98990, Name = sid:0x1ef195, Nexy(98990), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	17:17:30.130014-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 0]. BT device UIDS: {(
)}
default	17:17:30.130038-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	17:17:30.130067-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 200 flag 0x1 < Hijack > app com.nexy.assistant CID 0xD310001 category Not set
default	17:17:30.136215-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	17:17:30.135852-0500	runningboardd	Invalidating assertion 398-334-1382203 (target:[app<application.com.nexy.assistant.20408399.20408405(501)>:98990]) from originator [osservice<com.apple.powerd>:334]
default	17:17:30.136259-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	17:17:30.136276-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	17:17:30.136295-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	17:17:30.136070-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	17:17:30.136141-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	17:17:30.136373-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	17:17:30.136385-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	17:17:30.136414-0500	audioaccessoryd	AudioStateChanged: Removed audio session app com.nexy.assistant 201 count 0
default	17:17:30.138381-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	17:17:30.144445-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	17:17:30.144464-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	17:17:30.144484-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	17:17:30.144493-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	17:17:30.144500-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	17:17:30.144510-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	17:17:30.144644-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	17:17:30.230583-0500	Nexy	                AUHAL.cpp:473   ~AUHAL: (0x9a18c8740) Selecting device 0 from destructor
default	17:17:30.230603-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0x9a18c8740)
default	17:17:30.230611-0500	Nexy	                AUHAL.cpp:676   SelectDevice: (0x9a18c8740) not already running
default	17:17:30.230616-0500	Nexy	                AUHAL.cpp:682   SelectDevice: (0x9a18c8740) disconnecting device 91
default	17:17:30.230623-0500	Nexy	                AUHAL.cpp:746   SelectDevice: (0x9a18c8740) destroying ioproc 0xa for device 91
default	17:17:30.230658-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xa}
default	17:17:30.230690-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	17:17:30.230850-0500	Nexy	                AUHAL.cpp:848   SelectDevice: (0x9a18c8740) nothing to setup
default	17:17:30.230864-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x9a18c8740) adding 0 device listeners to device 0
default	17:17:30.230870-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x9a18c8740) adding 0 device delegate listeners to device 0
default	17:17:30.230875-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x9a18c8740) removing 7 device listeners from device 91
default	17:17:30.231046-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x9a18c8740) removing 0 device delegate listeners from device 91
default	17:17:30.231057-0500	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0x9a18c8740)
default	17:17:30.241759-0500	runningboardd	[app<application.com.nexy.assistant.20408399.20408405(501)>:98990] Ignoring jetsam update because this process is not memory-managed
default	17:17:30.241779-0500	runningboardd	[app<application.com.nexy.assistant.20408399.20408405(501)>:98990] Ignoring suspend because this process is not lifecycle managed
default	17:17:30.241791-0500	runningboardd	[app<application.com.nexy.assistant.20408399.20408405(501)>:98990] Ignoring GPU update because this process is not GPU managed
default	17:17:30.241808-0500	runningboardd	[app<application.com.nexy.assistant.20408399.20408405(501)>:98990] Ignoring memory limit update because this process is not memory-managed
default	17:17:30.245760-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.20408399.20408405(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	17:17:30.251924-0500	gamepolicyd	Received state update for 98990 (app<application.com.nexy.assistant.20408399.20408405(501)>, running-active-NotVisible
default	17:17:30.435030-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=98993.1, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=98990, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.osascript, pid=98993, auid=501, euid=501, binary_path=/usr/bin/osascript}, },
default	17:17:30.437125-0500	tccd	AUTHREQ_SUBJECT: msgID=98993.1, subject=com.nexy.assistant,
default	17:17:30.438365-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d114900 at /Applications/Nexy.app
default	17:17:30.446043-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=393.13835, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=98990, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.osascript, pid=98993, auid=501, euid=501, binary_path=/usr/bin/osascript}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=393, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	17:17:30.446604-0500	tccd	AUTHREQ_SUBJECT: msgID=393.13835, subject=com.nexy.assistant,
default	17:17:30.446999-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d114900 at /Applications/Nexy.app
default	17:17:30.463933-0500	launchservicesd	CHECKIN:0x0-0x1482481 98993 com.nexy.assistant
default	17:17:30.464705-0500	loginwindow	-[Application updateInformation] | Got App URL: file:///Applications/Nexy.app/
default	17:17:30.464798-0500	loginwindow	-[ApplicationManager checkInAppContext:eventData:] | ApplicationManager: Checked in app : Nexy
default	17:17:30.465286-0500	runningboardd	Invalidating assertion 398-363-1382178 (target:[app<application.com.nexy.assistant.20408399.20408405(501)>:98990]) from originator [osservice<com.apple.coreservices.launchservicesd>:363]
default	17:17:30.465348-0500	runningboardd	Assertion did invalidate due to timeout: 398-398-1382177 (target:[app<application.com.nexy.assistant.20408399.20408405(501)>:98990])
default	17:17:30.465698-0500	WindowServer	cc173[CreateApplication]: Process creation: 0x0-0x1482481 (Nexy) connectionID: CC173 pid: 98993 in session 0x101
default	17:17:30.467863-0500	loginwindow	-[Application updateInformation] | Got App URL: file:///Applications/Nexy.app/
default	17:17:30.473069-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d114900 at /Applications/Nexy.app
default	17:17:30.500077-0500	runningboardd	[app<application.com.nexy.assistant.20408399.20408405(501)>:98990] Ignoring jetsam update because this process is not memory-managed
default	17:17:30.500087-0500	runningboardd	[app<application.com.nexy.assistant.20408399.20408405(501)>:98990] Ignoring suspend because this process is not lifecycle managed
default	17:17:30.500111-0500	runningboardd	[app<application.com.nexy.assistant.20408399.20408405(501)>:98990] Set darwin role to: None
default	17:17:30.500121-0500	runningboardd	[app<application.com.nexy.assistant.20408399.20408405(501)>:98990] Ignoring GPU update because this process is not GPU managed
default	17:17:30.500152-0500	runningboardd	[app<application.com.nexy.assistant.20408399.20408405(501)>:98990] Ignoring memory limit update because this process is not memory-managed
default	17:17:30.505280-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.20408399.20408405(501)>: running-suspended (role: None) (endowments: (null))
default	17:17:30.505908-0500	gamepolicyd	Received state update for 98990 (app<application.com.nexy.assistant.20408399.20408405(501)>, running-suspended-NotVisible
default	17:17:30.598515-0500	System Events	TCCAccessRequestIndirect: TCCAccessRequestIndirect with pid 98994: target_identity: {
    kTCCCodeIdentityAuditToken = {length = 32, bytes = 0xf5010000 f5010000 14000000 f5010000 ... b7860100 13551f00 };
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
default	17:17:30.605297-0500	tccd	target_executable_path_URL: file:///Applications/Nexy.app/Contents/MacOS/Nexy
default	17:17:30.667623-0500	WindowServer	0[outside of RPC]: Process death: 0x0-0x1482481 (Nexy) connectionID: CC173 pid: 98993 in session 0x101
default	17:17:30.667637-0500	WindowServer	<BSCompoundAssertion:0x7fb0154c0> ([FocusManager:257]-deferringPolicyEvaluationSuppression) acquire for reason:process death - 0x0-0x1482481 (Nexy) acq:0x7febb6280 count:1
default	17:17:30.668286-0500	WindowServer	0[outside of RPC]: [FocusManager:257] update to deferring policy requested for reason: permitted list updated - 0x0-0x1482481 removed - but we are suppressing evaluation for reasons: {(
    "process death - 0x0-0x1482481 (Nexy)"
)}
default	17:17:30.668418-0500	WindowServer	0[outside of RPC]: [FocusManager:257] update to deferring policy requested for reason: permitted list updated - 0x1-0x182b1 removed - but we are suppressing evaluation for reasons: {(
    "process death - 0x0-0x1482481 (Nexy)"
)}
default	17:17:30.670104-0500	loginwindow	-[ApplicationManager handleCASEvent:withData:] | CAS notification for appDeath for com.nexy.assistant with asn: LSASN:{hi=0x0;lo=0x1482481} for bundle path: /Applications/Nexy.app with URL: file:///Applications/Nexy.app/
default	17:17:30.670119-0500	loginwindow	-[ApplicationManager(AppDeathHandler) appDeathCleanupHandler:forApp:] | Termination handler for: Nexy : 21505153
default	17:17:30.670145-0500	loginwindow	-[PersistentAppsSupport applicationQuit:] | for app:Nexy, _appTrackingState = 2
default	17:17:30.787575-0500	Nexy	                AUHAL.cpp:420   AUHAL: (0x9a18c8740) Selecting device 85 from constructor
default	17:17:30.787580-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0x9a18c8740)
default	17:17:30.787581-0500	Nexy	                AUHAL.cpp:676   SelectDevice: (0x9a18c8740) not already running
default	17:17:30.787584-0500	Nexy	                AUHAL.cpp:752   SelectDevice: (0x9a18c8740) nothing to teardown
default	17:17:30.787585-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0x9a18c8740) connecting device 85
default	17:17:30.787636-0500	Nexy	                AUHAL.cpp:3413  IsDeviceUsable: (0x9a18c8740) Device ID: 85 (Input:No | Output:Yes): true
default	17:17:30.787700-0500	Nexy	                AUHAL.cpp:769   SelectDevice: (0x9a18c8740) created ioproc 0xb for device 85
default	17:17:30.787782-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x9a18c8740) adding 7 device listeners to device 85
default	17:17:30.787897-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x9a18c8740) adding 0 device delegate listeners to device 85
default	17:17:30.787904-0500	Nexy	                AUHAL.cpp:1581  UpdateStreamFormats: -> (0x9a18c8740)
default	17:17:30.787942-0500	Nexy	                AUHAL.cpp:1677  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  24000 Hz, Float32, interleaved
default	17:17:30.787947-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 1 output streams; not all mono
default	17:17:30.787950-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Output render format:  2 ch,  24000 Hz, Float32, interleaved
default	17:17:30.787955-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 0 input streams; not all mono
default	17:17:30.787960-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	17:17:30.788028-0500	Nexy	                AUHAL.cpp:1771  UpdateStreamFormats: AUHAL(0x9a18c8740) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	17:17:30.788036-0500	Nexy	                AUHAL.cpp:1777  UpdateStreamFormats: AUHAL(0x9a18c8740) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	17:17:30.788043-0500	Nexy	                AUHAL.cpp:1787  UpdateStreamFormats: <-
default	17:17:30.788045-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x9a18c8740) removing 0 device listeners from device 0
default	17:17:30.788048-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x9a18c8740) removing 0 device delegate listeners from device 0
default	17:17:30.788049-0500	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0x9a18c8740)
default	17:17:30.788058-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Output stream enables: Stream 0 is DISABLED
default	17:17:30.788099-0500	Nexy	                AUHAL.cpp:2298  SetProperty: (0x9a18c8740) caller requesting device change from 85 to 91
default	17:17:30.788103-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0x9a18c8740)
default	17:17:30.788105-0500	Nexy	                AUHAL.cpp:676   SelectDevice: (0x9a18c8740) not already running
default	17:17:30.788108-0500	Nexy	                AUHAL.cpp:682   SelectDevice: (0x9a18c8740) disconnecting device 85
default	17:17:30.788110-0500	Nexy	                AUHAL.cpp:746   SelectDevice: (0x9a18c8740) destroying ioproc 0xb for device 85
default	17:17:30.788120-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped Unknown {1C-77-54-18-C8-A3:output, 0xb}
default	17:17:30.788136-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	17:17:30.788181-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0x9a18c8740) connecting device 91
default	17:17:30.788233-0500	Nexy	                AUHAL.cpp:3413  IsDeviceUsable: (0x9a18c8740) Device ID: 91 (Input:Yes | Output:No): true
default	17:17:30.788919-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.7511, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=98990, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	17:17:30.789376-0500	tccd	AUTHREQ_SUBJECT: msgID=401.7511, subject=com.nexy.assistant,
default	17:17:30.789655-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa0b1a8600 at /Applications/Nexy.app
default	17:17:30.795624-0500	Nexy	                AUHAL.cpp:769   SelectDevice: (0x9a18c8740) created ioproc 0xb for device 91
default	17:17:30.795702-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x9a18c8740) adding 7 device listeners to device 91
default	17:17:30.795804-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x9a18c8740) adding 0 device delegate listeners to device 91
default	17:17:30.795809-0500	Nexy	                AUHAL.cpp:1581  UpdateStreamFormats: -> (0x9a18c8740)
default	17:17:30.795814-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 0 output streams; not all mono
default	17:17:30.795819-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Output render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	17:17:30.795905-0500	Nexy	                AUHAL.cpp:1677  UpdateStreamFormats: 
  input stream 0 [0x5c]:  1 ch,  24000 Hz, Float32
default	17:17:30.795909-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 1 input streams; all mono
default	17:17:30.795912-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Input render format:  1 ch,  24000 Hz, Float32
default	17:17:30.795960-0500	Nexy	                AUHAL.cpp:1771  UpdateStreamFormats: AUHAL(0x9a18c8740) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	17:17:30.795967-0500	Nexy	                AUHAL.cpp:1777  UpdateStreamFormats: AUHAL(0x9a18c8740) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	17:17:30.795969-0500	Nexy	                AUHAL.cpp:1787  UpdateStreamFormats: <-
default	17:17:30.795973-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x9a18c8740) removing 7 device listeners from device 85
default	17:17:30.796068-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x9a18c8740) removing 0 device delegate listeners from device 85
default	17:17:30.796073-0500	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0x9a18c8740)
default	17:17:30.796401-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	17:17:30.796955-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.7512, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=98990, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	17:17:30.797363-0500	tccd	AUTHREQ_SUBJECT: msgID=401.7512, subject=com.nexy.assistant,
default	17:17:30.797652-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa0b1a8600 at /Applications/Nexy.app
default	17:17:30.803571-0500	Nexy	       ACv2Workarounds.mm:51    com.nexy.assistant: fix84702776_86723525_86479548_89800354_SinglePacketDesc: false
default	17:17:30.803626-0500	Nexy	       AudioConverter.cpp:1042  Created a new in process converter -> 0x99ec41320, from  1 ch,  24000 Hz, Float32 to  1 ch,  16000 Hz, Float32
default	17:17:30.803760-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	17:17:30.804337-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.7513, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=98990, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	17:17:30.804745-0500	tccd	AUTHREQ_SUBJECT: msgID=401.7513, subject=com.nexy.assistant,
default	17:17:30.805031-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa0b1a8600 at /Applications/Nexy.app
default	17:17:30.811625-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.7514, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=98990, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	17:17:30.812108-0500	tccd	AUTHREQ_SUBJECT: msgID=401.7514, subject=com.nexy.assistant,
default	17:17:30.812810-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa0b1a8600 at /Applications/Nexy.app
default	17:17:30.821002-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Input {1C-77-54-18-C8-A3:input, 0xb}
default	17:17:30.824804-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ef195","name":"Nexy(98990)"}, "details":{"deviceUIDs":["1C-77-54-18-C8-A3:input"],"implicit_category":"Record","input_running":true,"output_running":false} }
default	17:17:30.824850-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 406, PID = 98990, Name = sid:0x1ef195, Nexy(98990), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	17:17:30.824866-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Category/Mode changed -- The score for sid:0x1ef195, Nexy(98990), 'prim'/com.nexy.assistant was not correct. Old score = 201
default	17:17:30.824882-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 406, PID = 98990, Name = sid:0x1ef195, Nexy(98990), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	17:17:30.824955-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.20408399.20408405(501)>:98990] from originator [osservice<com.apple.powerd>:334] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:398-334-1382221 target:98990 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	17:17:30.825036-0500	runningboardd	Assertion 398-334-1382221 (target:[app<application.com.nexy.assistant.20408399.20408405(501)>:98990]) will be created as active
default	17:17:30.824917-0500	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1ef195, Nexy(98990), 'prim'', AudioCategory changed to 'Record_WithBluetooth'
default	17:17:30.825071-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 406, PID = 98990, Name = sid:0x1ef195, Nexy(98990), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	17:17:30.825148-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 406, PID = 98990, Name = sid:0x1ef195, Nexy(98990), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	17:17:30.825258-0500	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 406, PID = 98990, Name = sid:0x1ef195, Nexy(98990), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> is going active
default	17:17:30.825292-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1ef195, Nexy(98990), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 406 starting recording
default	17:17:30.825340-0500	runningboardd	[app<application.com.nexy.assistant.20408399.20408405(501)>:98990] Ignoring jetsam update because this process is not memory-managed
default	17:17:30.825381-0500	runningboardd	[app<application.com.nexy.assistant.20408399.20408405(501)>:98990] Ignoring suspend because this process is not lifecycle managed
default	17:17:30.825511-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 406, PID = 98990, Name = sid:0x1ef195, Nexy(98990), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	17:17:30.825483-0500	runningboardd	[app<application.com.nexy.assistant.20408399.20408405(501)>:98990] Set darwin role to: Background
default	17:17:30.825656-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 406, PID = 98990, Name = sid:0x1ef195, Nexy(98990), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	17:17:30.825622-0500	runningboardd	[app<application.com.nexy.assistant.20408399.20408405(501)>:98990] Ignoring GPU update because this process is not GPU managed
default	17:17:30.826010-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [1, 0]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:input"
)}
default	17:17:30.826060-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	17:17:30.825746-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1ef195, Nexy(98990), 'prim'', displayID:'com.nexy.assistant'}
default	17:17:30.825822-0500	runningboardd	[app<application.com.nexy.assistant.20408399.20408405(501)>:98990] Ignoring memory limit update because this process is not memory-managed
default	17:17:30.825936-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	17:17:30.826224-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 200 flag 0x1 < Hijack > app com.nexy.assistant CID 0xD310001 category Not set
default	17:17:30.826886-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	17:17:30.826839-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	17:17:30.826911-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	17:17:30.826865-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	17:17:30.826935-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	17:17:30.826880-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	17:17:30.826968-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	17:17:30.827033-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	17:17:30.827471-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	17:17:30.827541-0500	audioaccessoryd	AudioStateChanged: Added audio session app com.nexy.assistant NULL -> 200 count 1
default	17:17:30.827606-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
error	17:17:30.827649-0500	audioaccessoryd	Updating local audio category 100 -> 200 app com.nexy.assistant
default	17:17:30.827804-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	17:17:30.830521-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	17:17:30.830543-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	17:17:30.830560-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	17:17:30.830841-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	17:17:30.830997-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	17:17:30.831048-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	17:17:30.831101-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	17:17:30.831156-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	17:17:30.831280-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	17:17:30.831425-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	17:17:30.831454-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	17:17:30.831500-0500	ControlCenter	Navigating to new application [com.nexy.assistant]
default	17:17:30.831481-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	17:17:30.831602-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	17:17:30.832026-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	17:17:30.832117-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	17:17:30.832164-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	17:17:30.833358-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	17:17:30.833384-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	17:17:30.833451-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	17:17:30.833473-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	17:17:30.833579-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.20408399.20408405(501)>: running-active (role: Background) (endowments: (null))
default	17:17:30.833550-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	17:17:30.833584-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	17:17:30.833897-0500	gamepolicyd	Received state update for 98990 (app<application.com.nexy.assistant.20408399.20408405(501)>, running-active-NotVisible
default	17:17:30.908457-0500	audioaccessoryd	AudioStateSnapshot: Route:Bluetooth App com.nexy.assistant, Score 200, Remote 0NumofApp 1
default	17:17:33.851696-0500	audioaccessoryd	AudioStateSnapshot: Route:Bluetooth App com.nexy.assistant, Score 200, Remote 0NumofApp 1
default	17:17:36.863693-0500	audioaccessoryd	AudioStateSnapshot: Route:Bluetooth App com.nexy.assistant, Score 200, Remote 0NumofApp 1
default	17:17:39.801589-0500	coreaudiod	IssueReporting.cpp:492   RTAID [ use_case=Generic report_type=RMS Generic Chain clientID=ADM node=ADM::com.nexy.assistant_50308.50234.0_airpods noise suppression studio::in-0 issue_detected_sample_time=0.000000 ] -- [ rms:[-45.469383], peaks:[-26.179636] ]
default	17:17:39.804162-0500	coreaudiod	IssueReporting.cpp:492   RTAID [ use_case=Generic report_type=RMS Generic Chain clientID=ADM node=ADM::com.nexy.assistant_50308.50234.0_airpods noise suppression studio::out-0 issue_detected_sample_time=240000.000000 ] -- [ rms:[-49.334076], peaks:[-31.408642] ]
default	17:17:39.869663-0500	audioaccessoryd	AudioStateSnapshot: Route:Bluetooth App com.nexy.assistant, Score 200, Remote 0NumofApp 1
default	17:17:42.908000-0500	audioaccessoryd	AudioStateSnapshot: Route:Bluetooth App com.nexy.assistant, Score 200, Remote 0NumofApp 1
default	17:17:43.947644-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xb}
default	17:17:43.948225-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ef195","name":"Nexy(98990)"}, "details":{"deviceUIDs":[],"implicit_category":"","input_running":false,"output_running":false} }
default	17:17:43.948460-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 406, PID = 98990, Name = sid:0x1ef195, Nexy(98990), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	17:17:43.948580-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 406, PID = 98990, Name = sid:0x1ef195, Nexy(98990), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	17:17:43.948652-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1ef195, Nexy(98990), 'prim'', displayID:'com.nexy.assistant'}
default	17:17:43.948764-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	17:17:43.948781-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1ef195, Nexy(98990), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 406 stopping recording
default	17:17:43.948851-0500	audiomxd	-MXCoreSession- -[MXCoreSession endInterruption:]: Session <ID: 406, PID = 98990, Name = sid:0x1ef195, Nexy(98990), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> is going inactive
default	17:17:43.948915-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 406, PID = 98990, Name = sid:0x1ef195, Nexy(98990), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	17:17:43.948992-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 406, PID = 98990, Name = sid:0x1ef195, Nexy(98990), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	17:17:43.949229-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 0]. BT device UIDS: {(
)}
default	17:17:43.949278-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	17:17:43.949286-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 200 flag 0x1 < Hijack > app com.nexy.assistant CID 0xD310001 category Not set
default	17:17:43.953823-0500	runningboardd	Invalidating assertion 398-334-1382221 (target:[app<application.com.nexy.assistant.20408399.20408405(501)>:98990]) from originator [osservice<com.apple.powerd>:334]
default	17:17:43.955483-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	17:17:43.955564-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	17:17:43.955647-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	17:17:43.955693-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	17:17:43.955715-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	17:17:43.955743-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	17:17:43.955833-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	17:17:43.955852-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	17:17:43.955867-0500	audioaccessoryd	AudioStateChanged: Removed audio session app com.nexy.assistant 201 count 0
default	17:17:43.958031-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	17:17:43.962850-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	17:17:43.962866-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	17:17:43.962882-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	17:17:43.962892-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	17:17:43.962901-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	17:17:43.962908-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	17:17:43.963021-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	17:17:44.056224-0500	runningboardd	[app<application.com.nexy.assistant.20408399.20408405(501)>:98990] Ignoring jetsam update because this process is not memory-managed
default	17:17:44.056236-0500	runningboardd	[app<application.com.nexy.assistant.20408399.20408405(501)>:98990] Ignoring suspend because this process is not lifecycle managed
default	17:17:44.056266-0500	runningboardd	[app<application.com.nexy.assistant.20408399.20408405(501)>:98990] Set darwin role to: None
default	17:17:44.056276-0500	runningboardd	[app<application.com.nexy.assistant.20408399.20408405(501)>:98990] Ignoring GPU update because this process is not GPU managed
default	17:17:44.056338-0500	runningboardd	[app<application.com.nexy.assistant.20408399.20408405(501)>:98990] Ignoring memory limit update because this process is not memory-managed
default	17:17:44.060103-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.20408399.20408405(501)>: running-suspended (role: None) (endowments: (null))
default	17:17:44.060529-0500	gamepolicyd	Received state update for 98990 (app<application.com.nexy.assistant.20408399.20408405(501)>, running-suspended-NotVisible
default	17:17:44.112435-0500	Nexy	                AUHAL.cpp:473   ~AUHAL: (0x9a18c8740) Selecting device 0 from destructor
default	17:17:44.112447-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0x9a18c8740)
default	17:17:44.112454-0500	Nexy	                AUHAL.cpp:676   SelectDevice: (0x9a18c8740) not already running
default	17:17:44.112459-0500	Nexy	                AUHAL.cpp:682   SelectDevice: (0x9a18c8740) disconnecting device 91
default	17:17:44.112466-0500	Nexy	                AUHAL.cpp:746   SelectDevice: (0x9a18c8740) destroying ioproc 0xb for device 91
default	17:17:44.112485-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xb}
default	17:17:44.112509-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	17:17:44.112634-0500	Nexy	                AUHAL.cpp:848   SelectDevice: (0x9a18c8740) nothing to setup
default	17:17:44.112647-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x9a18c8740) adding 0 device listeners to device 0
default	17:17:44.112653-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x9a18c8740) adding 0 device delegate listeners to device 0
default	17:17:44.112659-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x9a18c8740) removing 7 device listeners from device 91
default	17:17:44.112875-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x9a18c8740) removing 0 device delegate listeners from device 91
default	17:17:44.112886-0500	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0x9a18c8740)
default	17:17:44.129017-0500	Nexy	[0x99fc08500] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	17:17:44.129815-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=98990.2, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=98990, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	17:17:44.131571-0500	tccd	AUTHREQ_SUBJECT: msgID=98990.2, subject=com.nexy.assistant,
default	17:17:44.132517-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d114900 at /Applications/Nexy.app
default	17:17:44.144550-0500	Nexy	[0x99fc08500] invalidated after the last release of the connection object
default	17:17:44.145348-0500	Nexy	[0x99fc08500] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	17:17:44.145698-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=98990.3, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=98990, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	17:17:44.146449-0500	tccd	AUTHREQ_SUBJECT: msgID=98990.3, subject=com.nexy.assistant,
default	17:17:44.147170-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d114900 at /Applications/Nexy.app
default	17:17:44.154386-0500	Nexy	[0x99fc08500] invalidated after the last release of the connection object
default	17:17:44.154566-0500	Nexy	[0x99fc08500] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	17:17:44.154863-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=98990.4, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=98990, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	17:17:44.155580-0500	tccd	AUTHREQ_SUBJECT: msgID=98990.4, subject=com.nexy.assistant,
default	17:17:44.156327-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d114900 at /Applications/Nexy.app
default	17:17:44.163737-0500	tccd	Notifying for access  kTCCServiceScreenCapture for target PID[98990], responsiblePID[98990], responsiblePath: /Applications/Nexy.app to UID: 501
default	17:17:44.163878-0500	Nexy	[0x99fc08500] invalidated after the last release of the connection object
default	17:17:44.228698-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117000 at /Applications/Nexy.app
default	17:17:44.244199-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d114900 at /Applications/Nexy.app
default	17:17:44.247045-0500	tccd	Publishing <TCCDEvent: type=Modify, service=kTCCServiceScreenCapture, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 0 subscribers: {
}
default	17:17:44.250111-0500	nehelper	Received an apps uninstalled notification with bundle IDs (
    "com.nexy.assistant"
)
default	17:17:44.250500-0500	nehelper	Received an apps uninstalled notification with bundle IDs (
    "com.nexy.assistant"
)
default	17:17:44.846600-0500	nehelper	Removing UUIDs for (
    "com.nexy.assistant"
)
default	17:17:44.850263-0500	nehelper	Handling an apps uninstalled notification with bundle IDs (
    "com.nexy.assistant"
)
default	17:17:44.868323-0500	nehelper	com.apple.preferences.networkprivacy-F67B3EA9-90A6-470B-B321-9BBD719C692B: Populating the cache with 1 UUID(s) for com.nexy.assistant
default	17:17:46.181035-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(50308)
default	17:17:46.182182-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(50307)
default	17:17:46.184585-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:50308 called from <private>
default	17:17:46.197099-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:50308 called from <private>
default	17:17:46.202491-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(50308)
default	17:17:46.203231-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:50308 called from <private>
default	17:17:46.203248-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:50308 called from <private>
default	17:17:46.203955-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(50307)
default	17:17:46.204122-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:50307 called from <private>
default	17:17:46.204137-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:50307 called from <private>
default	17:17:46.204150-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:50307 called from <private>
default	17:17:46.204158-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:50307 called from <private>
default	17:17:46.210664-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:50307 called from <private>
default	17:17:46.210926-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:50307 called from <private>
default	17:17:46.211081-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:50307 called from <private>
default	17:17:46.211529-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:50307 called from <private>
default	17:17:46.211585-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(50307)
default	17:17:46.231651-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(50307)
default	17:17:46.235069-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:50307 called from <private>
default	17:17:46.246860-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:50307 called from <private>
default	17:17:46.249108-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:50307 called from <private>
default	17:17:46.249214-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:50307 called from <private>
default	17:17:46.249275-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:50307 called from <private>
default	17:17:46.249285-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:50307 called from <private>
default	17:17:46.249320-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:50307 called from <private>
default	17:17:46.249325-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:50307 called from <private>
default	17:17:46.249339-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:50307 called from <private>
default	17:17:46.249350-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:50307 called from <private>
default	17:17:46.249356-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:50307 called from <private>
default	17:17:46.249363-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:50307 called from <private>
default	17:17:46.249381-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(50307)
default	17:17:46.249437-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:50307 called from <private>
default	17:17:46.249511-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:50307 called from <private>
default	17:17:46.249629-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(50307)
default	17:17:52.122205-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d114900 at /Applications/Nexy.app
default	17:17:52.134566-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117000 at /Applications/Nexy.app
default	17:17:52.140109-0500	tccd	Publishing <TCCDEvent: type=Modify, service=kTCCServiceScreenCapture, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 0 subscribers: {
}
default	17:17:57.673850-0500	audiomxd	  ServerSessionManager.mm:472   { "action":"destroy_session", "session":{"ID":"0x1ef195","name":"Nexy(98990)"}, "details":null }
default	17:17:57.673897-0500	audiomxd	AudioApplicationInfoImpl.mm:690   Successfully removed session 0x1ef195 from AudioApp, recording state unchanged (app: {"name":"[implicit] Nexy","pid":98990})
default	17:17:57.673913-0500	audiomxd	  ServerSessionManager.mm:1081  destroy audio app instance since was created implicitly by session creation and all sessions now gone (audio app: {"name":"[implicit] Nexy","pid":98990})
default	17:17:57.674210-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 406, PID = 98990, Name = sid:0x1ef195, Nexy(98990), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	17:17:57.674293-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 406, PID = 98990, Name = sid:0x1ef195, Nexy(98990), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	17:17:57.676192-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	17:17:57.676645-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	17:17:57.676683-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	17:17:57.675874-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	17:17:57.676069-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	17:17:57.683585-0500	coreaudiod	>>> NEGOTIATE [com.nexy.assistant]
default	17:17:57.683765-0500	coreaudiod	<<< NEGOTIATE [com.nexy.assistant]
default	17:17:57.685539-0500	coreaudiod	IssueReporting.cpp:492   RTAID [ use_case=Generic report_type=RMS Generic Chain clientID=ADM node=ADM::com.nexy.assistant_50308.50234.0_airpods noise suppression studio::out-0 issue_detected_sample_time=336960.000000 ] -- [ rms:[-50.538250], peaks:[-24.282898] ]
default	17:17:57.685580-0500	coreaudiod	IssueReporting.cpp:492   RTAID [ use_case=Generic report_type=RMS Generic Chain clientID=ADM node=ADM::com.nexy.assistant_50308.50234.0_airpods noise suppression studio::in-0 issue_detected_sample_time=0.000000 ] -- [ rms:[-51.152111], peaks:[-28.586380] ]
default	17:17:57.693438-0500	kernel	Nexy[98990] triggered unnest of range 0x1f6000000->0x1f8000000 of DYLD shared region in VM map 0xccfdbefbdd8e4f49. While not abnormal for debuggers, this increases system memory footprint until the target exits.
default	17:17:57.693458-0500	kernel	Nexy[98990] triggered unnest of range 0x1f8000000->0x1fa000000 of DYLD shared region in VM map 0xccfdbefbdd8e4f49. While not abnormal for debuggers, this increases system memory footprint until the target exits.
default	17:17:57.698278-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	17:17:57.803710-0500	Nexy	[0x1023690c0] activating connection: mach=true listener=false peer=false name=com.apple.cfprefsd.daemon
default	17:17:57.803756-0500	Nexy	[0x10236cdc0] activating connection: mach=true listener=false peer=false name=com.apple.cfprefsd.agent
error	17:17:57.844352-0500	Nexy	dlsym cannot find symbol NSMakeRect in CFBundle 0xc1770c000 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	17:17:57.844490-0500	Nexy	dlsym cannot find symbol NSMakePoint in CFBundle 0xc1770c000 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	17:17:57.844604-0500	Nexy	dlsym cannot find symbol NSMakeSize in CFBundle 0xc1770c000 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	17:17:57.844717-0500	Nexy	dlsym cannot find symbol NSMakeRange in CFBundle 0xc1770c000 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
default	17:17:57.879585-0500	Nexy	Registered notify signal com.apple.caulk.alloc.rtdump (0)
default	17:17:57.881175-0500	Nexy	System_Input_Processing_Notification_Handler.mm:456   System_Input_Processing_Notification_Handler::is_vi_available(): Voice isolation DSP is available for client with bundle id com.nexy.assistant (AVFoundation is available, application is not in client deny list, application is not FaceTime variant)
default	17:17:57.882061-0500	Nexy	[0x1023546e0] activating connection: mach=true listener=false peer=false name=com.apple.cmio.registerassistantservice.system-extensions
default	17:17:57.883109-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOInitializeListenersForBundleID: for <private> -> <private>
default	17:17:57.883917-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> vpio_preferenceChangedListener: new value ((null)) for key AUVoiceIOClients/com-nexy-assistant/AUVoiceIOChatFlavor, translatedBundleID com.nexy.assistant, bundleIDs {(
    "com.nexy.assistant"
)}
default	17:17:57.884037-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> vpio_preferenceChangedListener: new value ((null)) for key AUVoiceIOClients/com-nexy-assistant/AUVoiceIOIsAutoChatFlavorEnabled, translatedBundleID com.nexy.assistant, bundleIDs {(
    "com.nexy.assistant"
)}
default	17:17:57.884232-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetSupportedChatFlavorsForBundleID: <private>-><private> get supported chat flavors: <private>
default	17:17:57.884238-0500	Nexy	            HALSystem.cpp:134    Enabling HAL Voice Isolation support
default	17:17:57.884257-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetHiddenChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	17:17:57.884424-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOHiddenChatFlavors newValue: (
    1
)
default	17:17:57.884377-0500	Nexy	[0xc163cc000] activating connection: mach=true listener=false peer=false name=com.apple.tccd
default	17:17:57.884676-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=98990.1, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=98990, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	17:17:57.888308-0500	tccd	AUTHREQ_SUBJECT: msgID=98990.1, subject=com.nexy.assistant,
default	17:17:57.888860-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa0b1a9e00 at /Applications/Nexy.app
default	17:17:57.894655-0500	Nexy	[0xc163cc000] invalidated after the last release of the connection object
default	17:17:57.894752-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetPreferredChatFlavorForBundleID: <private>-><private> get value: 0
default	17:17:57.894771-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetSupportedChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	17:17:57.894952-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOSupportedChatFlavors newValue: (
    0,
    2
)
default	17:17:57.895639-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.7515, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=98990, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	17:17:57.896050-0500	tccd	AUTHREQ_SUBJECT: msgID=401.7515, subject=com.nexy.assistant,
default	17:17:57.896513-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa0b1a9e00 at /Applications/Nexy.app
error	17:17:57.902564-0500	tccd	Request message contains a target_token to accessing_process (TCCDProcess: identifier=com.nexy.assistant, pid=98990, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy) but TCCDProcess: identifier=com.apple.audio.coreaudiod, pid=401, auid=202, euid=202, binary_path=/usr/sbin/coreaudiod is not a TCC manager for service: kTCCServiceScreenCapture.
default	17:17:57.903114-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.7517, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=98990, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	17:17:57.903490-0500	tccd	AUTHREQ_SUBJECT: msgID=401.7517, subject=com.nexy.assistant,
default	17:17:57.903806-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa0b1a9e00 at /Applications/Nexy.app
default	17:17:57.911050-0500	Nexy	  HALPlugInManagement.cpp:440    HALPlugInManagement::RegisterPlugIns: skipping in-process plug-ins
error	17:17:57.911067-0500	Nexy	AddInstanceForFactory: No factory registered for id <CFUUID 0xc176fc440> F8BB1C28-BAE8-11D6-9C31-00039315CD46
error	17:17:57.924251-0500	Nexy	         HALC_ProxyObjectMap.cpp:174   HALC_ProxyObjectMap::_CopyObjectByObjectID: failed to create the local object
error	17:17:57.924262-0500	Nexy	            HALC_ShellDevice.cpp:2673  HALC_ShellDevice::RebuildControlList: couldn't find the control object
default	17:17:57.926672-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	17:17:57.926835-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	17:17:57.930155-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetPreferredChatFlavorForBundleID: <private>-><private> get value: 0
default	17:17:58.683383-0500	kernel	SK[8]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid D4C2D453-27B9-4A87-9CF8-BC9ED474DA8E flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.57416,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0x81a3034f tp_proto=0x06"
default	17:17:58.683414-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:57416<-><IPv4-redacted>:53] interface: utun6 (skipped: 6843)
so_gencnt: 5135900 t_state: SYN_SENT process: Nexy:98990 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 1 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xaa1ca991
default	17:17:58.683700-0500	kernel	tcp connected: [<IPv4-redacted>:57416<-><IPv4-redacted>:53] interface: utun6 (skipped: 6843)
so_gencnt: 5135900 t_state: ESTABLISHED process: Nexy:98990 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 1 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xaa1ca991
default	17:17:58.683842-0500	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:57416<-><IPv4-redacted>:53] interface: utun6 (skipped: 6843)
so_gencnt: 5135900 t_state: FIN_WAIT_1 process: Nexy:98990 Duration: 0.000 sec Conn_Time: 0.000 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 1.000 ms rttvar: 0.500 ms base rtt: 1 ms so_error: 0 svc/tc: 0 flow: 0xaa1ca991
default	17:17:58.683847-0500	kernel	tcp_connection_summary [<IPv4-redacted>:57416<-><IPv4-redacted>:53] interface: utun6 (skipped: 6843)
so_gencnt: 5135900 t_state: FIN_WAIT_1 process: Nexy:98990 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	17:17:58.692377-0500	Nexy	[0xc163cc000] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioComponentRegistrar
default	17:17:58.697328-0500	Nexy	                AUHAL.cpp:420   AUHAL: (0xc17428e40) Selecting device 85 from constructor
default	17:17:58.697334-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0xc17428e40)
default	17:17:58.697336-0500	Nexy	                AUHAL.cpp:676   SelectDevice: (0xc17428e40) not already running
default	17:17:58.697340-0500	Nexy	                AUHAL.cpp:752   SelectDevice: (0xc17428e40) nothing to teardown
default	17:17:58.697341-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0xc17428e40) connecting device 85
default	17:17:58.697391-0500	Nexy	                AUHAL.cpp:3413  IsDeviceUsable: (0xc17428e40) Device ID: 85 (Input:No | Output:Yes): true
default	17:17:58.697448-0500	Nexy	                AUHAL.cpp:769   SelectDevice: (0xc17428e40) created ioproc 0xa for device 85
default	17:17:58.697510-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0xc17428e40) adding 7 device listeners to device 85
default	17:17:58.697603-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0xc17428e40) adding 0 device delegate listeners to device 85
default	17:17:58.697608-0500	Nexy	                AUHAL.cpp:1581  UpdateStreamFormats: -> (0xc17428e40)
default	17:17:58.697652-0500	Nexy	                AUHAL.cpp:1677  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  48000 Hz, Float32, interleaved
default	17:17:58.697660-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 1 output streams; not all mono
default	17:17:58.697664-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	17:17:58.697668-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 0 input streams; not all mono
default	17:17:58.697674-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	17:17:58.697725-0500	Nexy	                AUHAL.cpp:1771  UpdateStreamFormats: AUHAL(0xc17428e40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	17:17:58.697731-0500	Nexy	                AUHAL.cpp:1777  UpdateStreamFormats: AUHAL(0xc17428e40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	17:17:58.697734-0500	Nexy	                AUHAL.cpp:1787  UpdateStreamFormats: <-
default	17:17:58.697736-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0xc17428e40) removing 0 device listeners from device 0
default	17:17:58.697738-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0xc17428e40) removing 0 device delegate listeners from device 0
default	17:17:58.697741-0500	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0xc17428e40)
default	17:17:58.697746-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Output stream enables: Stream 0 is DISABLED
default	17:17:58.697803-0500	Nexy	                AUHAL.cpp:2298  SetProperty: (0xc17428e40) caller requesting device change from 85 to 91
default	17:17:58.697812-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0xc17428e40)
default	17:17:58.697814-0500	Nexy	                AUHAL.cpp:676   SelectDevice: (0xc17428e40) not already running
default	17:17:58.697818-0500	Nexy	                AUHAL.cpp:682   SelectDevice: (0xc17428e40) disconnecting device 85
default	17:17:58.697822-0500	Nexy	                AUHAL.cpp:746   SelectDevice: (0xc17428e40) destroying ioproc 0xa for device 85
default	17:17:58.697845-0500	Nexy	  AVAudioSession_MacOS.mm:1021  initForMacOS
default	17:17:58.698062-0500	Nexy	[0xc163cc280] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioSession
default	17:17:58.698441-0500	audiomxd	  ServerSessionManager.mm:315   { "action":"create_session", "session":{"ID":"0x1ef196","name":"Nexy(98990)"}, "details":{"PID":98990,"session_type":"Primary"} }
default	17:17:58.698477-0500	audiomxd	AudioApplicationInfoImpl.mm:250   Setting initial isRecording state: 0 for newly-created AudioApp
	app: {"name":"[implicit] Nexy","pid":98990}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1ef196, sessionType: 'prim', isRecording: false }, 
]
default	17:17:58.698631-0500	Nexy	    SessionCore_Create.mm:99    Created session 0xc1626e680 with ID: 0x1ef196
default	17:17:58.698923-0500	Nexy	[0xc163cc3c0] activating connection: mach=true listener=false peer=false name=com.apple.audioanalyticsd
default	17:17:58.698997-0500	Nexy	No persisted cache on this platform.
error	17:17:58.699155-0500	Nexy	Reporter disconnected. { function=sendMessage, reporterID=425158812631041 }
default	17:17:58.699163-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped Unknown {1C-77-54-18-C8-A3:output, 0xa}
default	17:17:58.699192-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	17:17:58.699237-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0xc17428e40) connecting device 91
default	17:17:58.699290-0500	Nexy	                AUHAL.cpp:3413  IsDeviceUsable: (0xc17428e40) Device ID: 91 (Input:Yes | Output:No): true
default	17:17:58.699908-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.7518, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=98990, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	17:17:58.700417-0500	tccd	AUTHREQ_SUBJECT: msgID=401.7518, subject=com.nexy.assistant,
default	17:17:58.700804-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa0b1a9e00 at /Applications/Nexy.app
default	17:17:58.706403-0500	Nexy	                AUHAL.cpp:769   SelectDevice: (0xc17428e40) created ioproc 0xa for device 91
default	17:17:58.706473-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0xc17428e40) adding 7 device listeners to device 91
default	17:17:58.706566-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0xc17428e40) adding 0 device delegate listeners to device 91
default	17:17:58.706569-0500	Nexy	                AUHAL.cpp:1581  UpdateStreamFormats: -> (0xc17428e40)
default	17:17:58.706573-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 0 output streams; not all mono
default	17:17:58.706578-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Output render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	17:17:58.706645-0500	Nexy	                AUHAL.cpp:1677  UpdateStreamFormats: 
  input stream 0 [0x5c]:  1 ch,  24000 Hz, Float32
default	17:17:58.706650-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 1 input streams; all mono
default	17:17:58.706654-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Input render format:  1 ch,  24000 Hz, Float32
default	17:17:58.706706-0500	Nexy	                AUHAL.cpp:1771  UpdateStreamFormats: AUHAL(0xc17428e40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	17:17:58.706713-0500	Nexy	                AUHAL.cpp:1777  UpdateStreamFormats: AUHAL(0xc17428e40) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	17:17:58.706717-0500	Nexy	                AUHAL.cpp:1787  UpdateStreamFormats: <-
default	17:17:58.706721-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0xc17428e40) removing 7 device listeners from device 85
default	17:17:58.706809-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0xc17428e40) removing 0 device delegate listeners from device 85
default	17:17:58.706813-0500	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0xc17428e40)
default	17:17:58.707170-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	17:17:58.707725-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.7519, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=98990, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	17:17:58.708187-0500	tccd	AUTHREQ_SUBJECT: msgID=401.7519, subject=com.nexy.assistant,
default	17:17:58.708508-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa0b1a9e00 at /Applications/Nexy.app
default	17:17:58.714700-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	17:17:58.715291-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.7520, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=98990, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	17:17:58.715673-0500	tccd	AUTHREQ_SUBJECT: msgID=401.7520, subject=com.nexy.assistant,
default	17:17:58.715940-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa0b1a9e00 at /Applications/Nexy.app
default	17:17:58.721932-0500	Nexy	Registered notify signal com.apple.caulk.alloc.audiodump (0)
default	17:17:58.722744-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.7521, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=98990, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	17:17:58.723165-0500	tccd	AUTHREQ_SUBJECT: msgID=401.7521, subject=com.nexy.assistant,
default	17:17:58.723500-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa0b1a9e00 at /Applications/Nexy.app
default	17:17:58.729923-0500	coreaudiod	>>> NEGOTIATE [com.nexy.assistant]
default	17:17:58.730003-0500	coreaudiod	<<< NEGOTIATE [com.nexy.assistant]
default	17:17:58.730923-0500	coreaudiod	>>> ADAPT [com.nexy.assistant]
default	17:17:58.731197-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xbf6d86d00] Created node ADM::com.nexy.assistant_50321.50234.0_airpods noise suppression studio::in-0 with nodeID 0 - reporting period = 10.000000, sample rate = 24000.000000
default	17:17:58.731270-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xbf6d86d00] Created node ADM::com.nexy.assistant_50321.50234.0_airpods noise suppression studio::out-0 with nodeID 1 - reporting period = 10.000000, sample rate = 24000.000000
default	17:17:58.780975-0500	coreaudiod	<<< ADAPT [com.nexy.assistant]
default	17:17:58.782238-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:50321 called from <private>
default	17:17:58.782263-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Input {1C-77-54-18-C8-A3:input, 0xa}
default	17:17:58.782968-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:50321 called from <private>
default	17:17:58.783092-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(50321)
default	17:17:58.784789-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.20408399.20408405(501)>:98990] from originator [osservice<com.apple.powerd>:334] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:398-334-1382379 target:98990 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	17:17:58.785270-0500	runningboardd	Assertion 398-334-1382379 (target:[app<application.com.nexy.assistant.20408399.20408405(501)>:98990]) will be created as active
default	17:17:58.787111-0500	runningboardd	[app<application.com.nexy.assistant.20408399.20408405(501)>:98990] Ignoring jetsam update because this process is not memory-managed
default	17:17:58.787132-0500	runningboardd	[app<application.com.nexy.assistant.20408399.20408405(501)>:98990] Ignoring suspend because this process is not lifecycle managed
default	17:17:58.787381-0500	runningboardd	[app<application.com.nexy.assistant.20408399.20408405(501)>:98990] Set darwin role to: Background
default	17:17:58.787513-0500	runningboardd	[app<application.com.nexy.assistant.20408399.20408405(501)>:98990] Ignoring GPU update because this process is not GPU managed
default	17:17:58.787708-0500	runningboardd	[app<application.com.nexy.assistant.20408399.20408405(501)>:98990] Ignoring memory limit update because this process is not memory-managed
default	17:17:58.783106-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:50321 called from <private>
default	17:17:58.783109-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:50321 called from <private>
default	17:17:58.783379-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(50320)
default	17:17:58.783385-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:50320 called from <private>
default	17:17:58.783389-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:50320 called from <private>
fault	17:17:58.790380-0500	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.20408399.20408405 AUID=501> and <type=Application identifier=application.com.nexy.assistant.20408399.20408405>
default	17:17:58.791522-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	17:17:58.791944-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	17:17:58.794410-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(50321)
default	17:17:58.794559-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(50321)
default	17:17:58.794584-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(50321)
default	17:17:58.794663-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(50321)
fault	17:17:58.795520-0500	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.20408399.20408405 AUID=501> and <type=Application identifier=application.com.nexy.assistant.20408399.20408405>
default	17:17:58.800786-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.20408399.20408405(501)>: running-active (role: Background) (endowments: (null))
default	17:17:58.801295-0500	runningboardd	Invalidating assertion 398-334-1382379 (target:[app<application.com.nexy.assistant.20408399.20408405(501)>:98990]) from originator [osservice<com.apple.powerd>:334]
default	17:17:58.809186-0500	gamepolicyd	Received state update for 98990 (app<application.com.nexy.assistant.20408399.20408405(501)>, running-active-NotVisible
default	17:17:58.812369-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(50320)
default	17:17:58.812434-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(50321)
default	17:17:58.812490-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:50320 called from <private>
default	17:17:58.812522-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:50320 called from <private>
default	17:17:58.812639-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:50321 called from <private>
default	17:17:58.812652-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:50321 called from <private>
default	17:17:58.812752-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:50321 called from <private>
default	17:17:58.812782-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:50321 called from <private>
default	17:17:58.812789-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:50321 called from <private>
default	17:17:58.812892-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:50321 called from <private>
default	17:17:58.812906-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:50321 called from <private>
default	17:17:58.816462-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:50320 called from <private>
default	17:17:58.816482-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:50320 called from <private>
error	17:17:58.817991-0500	Nexy	         HALC_ProxyIOContext.cpp:1042  HALC_ProxyIOContext::_StartIO(): Client running as an adaptive unboosted daemon
default	17:17:58.818058-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(50320)
default	17:17:58.818572-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:50320 called from <private>
default	17:17:58.818639-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:50320 called from <private>
default	17:17:58.819535-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ef196","name":"Nexy(98990)"}, "details":{"deviceUIDs":["1C-77-54-18-C8-A3:input"],"implicit_category":"Record","input_running":true,"output_running":false} }
default	17:17:58.819753-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	17:17:58.819581-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 407, PID = 98990, Name = sid:0x1ef196, Nexy(98990), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	17:17:58.819825-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	17:17:58.819607-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 407, PID = 98990, Name = sid:0x1ef196, Nexy(98990), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	17:17:58.819891-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	17:17:58.819711-0500	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1ef196, Nexy(98990), 'prim'', AudioCategory changed to 'Record_WithBluetooth'
default	17:17:58.819845-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 407, PID = 98990, Name = sid:0x1ef196, Nexy(98990), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	17:17:58.819916-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 407, PID = 98990, Name = sid:0x1ef196, Nexy(98990), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	17:17:58.820118-0500	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 407, PID = 98990, Name = sid:0x1ef196, Nexy(98990), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> is going active
default	17:17:58.820152-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1ef196, Nexy(98990), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 407 starting recording
default	17:17:58.820046-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	17:17:58.820291-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	17:17:58.820416-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	17:17:58.820204-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.7522, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=98990, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	17:17:58.820312-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 407, PID = 98990, Name = sid:0x1ef196, Nexy(98990), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	17:17:58.820640-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	17:17:58.820424-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 407, PID = 98990, Name = sid:0x1ef196, Nexy(98990), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	17:17:58.820389-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	17:17:58.820476-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1ef196, Nexy(98990), 'prim'', displayID:'com.nexy.assistant'}
default	17:17:58.820725-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	17:17:58.820709-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	17:17:58.820873-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	17:17:58.820909-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	17:17:58.820952-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	17:17:58.821108-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	17:17:58.821217-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	17:17:58.821866-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [1, 0]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:input"
)}
default	17:17:58.821892-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	17:17:58.822534-0500	tccd	AUTHREQ_SUBJECT: msgID=401.7522, subject=com.nexy.assistant,
default	17:17:58.822848-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	17:17:58.823816-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa0b1a9e00 at /Applications/Nexy.app
default	17:17:58.826374-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(50320)
default	17:17:58.829278-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:50320 called from <private>
default	17:17:58.829297-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:50320 called from <private>
default	17:17:58.830172-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:50320 called from <private>
default	17:17:58.830187-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:50320 called from <private>
default	17:17:58.831907-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:50320 called from <private>
default	17:17:58.831924-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:50320 called from <private>
default	17:17:58.832107-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(50320)
default	17:17:58.832139-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:50320 called from <private>
default	17:17:58.832150-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:50320 called from <private>
default	17:17:58.837052-0500	coreaudiod	>>> NEGOTIATE [com.nexy.assistant]
default	17:17:58.837621-0500	coreaudiod	<<< NEGOTIATE [com.nexy.assistant]
default	17:17:58.841152-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	17:17:58.838392-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(50320)
default	17:17:58.846590-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	17:17:58.846271-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	17:17:58.847165-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	17:17:58.847306-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	17:17:58.846983-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	17:17:58.847033-0500	audioaccessoryd	AudioStateChanged: Added audio session app com.nexy.assistant NULL -> 200 count 1
default	17:17:58.846477-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	17:17:58.850172-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:50321 called from <private>
default	17:17:58.850286-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:50321 called from <private>
error	17:17:58.850718-0500	Nexy	         HALC_ProxyIOContext.cpp:1042  HALC_ProxyIOContext::_StartIO(): Client running as an adaptive unboosted daemon
default	17:17:58.847337-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	17:17:58.850476-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	17:17:58.850802-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:50321 called from <private>
default	17:17:58.850886-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	17:17:58.854944-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:50320 called from <private>
default	17:17:58.855119-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(50320)
default	17:17:58.855155-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.7523, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=98990, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	17:17:58.855192-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(50320)
default	17:17:58.855902-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:50320 called from <private>
default	17:17:58.856344-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:50320 called from <private>
default	17:17:58.862076-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	17:17:58.862081-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	17:17:58.862087-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	17:17:58.862090-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	17:17:58.862095-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	17:17:58.862097-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	17:17:58.866511-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xbf6d86d00] Created node ADM::com.nexy.assistant_50321.50234.0_airpods noise suppression studio::in-0 with nodeID 0 - reporting period = 10.000000, sample rate = 24000.000000
default	17:17:58.866550-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xbf6d86d00] Created node ADM::com.nexy.assistant_50321.50234.0_airpods noise suppression studio::out-0 with nodeID 1 - reporting period = 10.000000, sample rate = 24000.000000
default	17:17:58.888772-0500	coreaudiod	<<< ADAPT [com.nexy.assistant]
default	17:17:58.889434-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.20408399.20408405(501)>:98990] from originator [osservice<com.apple.powerd>:334] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:398-334-1382381 target:98990 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	17:17:58.889477-0500	runningboardd	Assertion 398-334-1382381 (target:[app<application.com.nexy.assistant.20408399.20408405(501)>:98990]) will be created as active
default	17:17:58.892170-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:50321 called from <private>
default	17:17:58.892671-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:50321 called from <private>
default	17:17:58.892715-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	17:17:58.893784-0500	runningboardd	Invalidating assertion 398-334-1382381 (target:[app<application.com.nexy.assistant.20408399.20408405(501)>:98990]) from originator [osservice<com.apple.powerd>:334]
default	17:17:58.894706-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:50321 called from <private>
default	17:17:58.895013-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(50321)
default	17:17:58.895273-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:50321 called from <private>
default	17:17:58.895308-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:50321 called from <private>
default	17:17:58.895349-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	17:17:58.895489-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	17:17:58.895843-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(50321)
default	17:17:58.895987-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:50321 called from <private>
default	17:17:58.895999-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:50321 called from <private>
default	17:17:58.896080-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:50321 called from <private>
error	17:17:58.896378-0500	Nexy	         HALC_ProxyIOContext.cpp:1042  HALC_ProxyIOContext::_StartIO(): Client running as an adaptive unboosted daemon
default	17:17:58.897355-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.7524, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=98990, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	17:17:58.897927-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	17:17:58.897950-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	17:17:58.897996-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	17:17:58.898102-0500	tccd	AUTHREQ_SUBJECT: msgID=401.7524, subject=com.nexy.assistant,
default	17:17:58.898153-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	17:17:58.898395-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	17:17:58.898400-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	17:17:58.898406-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	17:17:58.898462-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	17:17:58.898752-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa0b1a9e00 at /Applications/Nexy.app
default	17:17:58.898607-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	17:17:58.899612-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	17:17:58.901845-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	17:17:58.901932-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	17:17:58.901971-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	17:17:58.902000-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	17:17:58.902174-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	17:17:58.902256-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	17:17:58.902287-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	17:17:58.903965-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	17:17:58.906950-0500	runningboardd	[app<application.com.nexy.assistant.20408399.20408405(501)>:98990] Ignoring jetsam update because this process is not memory-managed
default	17:17:58.906965-0500	runningboardd	[app<application.com.nexy.assistant.20408399.20408405(501)>:98990] Ignoring suspend because this process is not lifecycle managed
default	17:17:58.906997-0500	runningboardd	[app<application.com.nexy.assistant.20408399.20408405(501)>:98990] Set darwin role to: None
default	17:17:58.907030-0500	runningboardd	[app<application.com.nexy.assistant.20408399.20408405(501)>:98990] Ignoring GPU update because this process is not GPU managed
default	17:17:58.907116-0500	runningboardd	[app<application.com.nexy.assistant.20408399.20408405(501)>:98990] Ignoring memory limit update because this process is not memory-managed
default	17:17:58.908426-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.20408399.20408405(501)>:98990] from originator [osservice<com.apple.powerd>:334] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:398-334-1382383 target:98990 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	17:17:58.908472-0500	runningboardd	Assertion 398-334-1382383 (target:[app<application.com.nexy.assistant.20408399.20408405(501)>:98990]) will be created as active
default	17:17:58.911087-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:50321 called from <private>
default	17:17:58.916744-0500	runningboardd	[app<application.com.nexy.assistant.20408399.20408405(501)>:98990] Set darwin role to: Background
default	17:17:58.916757-0500	runningboardd	[app<application.com.nexy.assistant.20408399.20408405(501)>:98990] Ignoring GPU update because this process is not GPU managed
default	17:17:58.916821-0500	runningboardd	[app<application.com.nexy.assistant.20408399.20408405(501)>:98990] Ignoring memory limit update because this process is not memory-managed
default	17:17:58.917007-0500	gamepolicyd	Received state update for 98990 (app<application.com.nexy.assistant.20408399.20408405(501)>, running-suspended-NotVisible
default	17:18:00.199963-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xa}
default	17:18:00.200226-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ef196","name":"Nexy(98990)"}, "details":{"deviceUIDs":[],"implicit_category":"","input_running":false,"output_running":false} }
default	17:18:00.200324-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 407, PID = 98990, Name = sid:0x1ef196, Nexy(98990), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	17:18:00.200376-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 407, PID = 98990, Name = sid:0x1ef196, Nexy(98990), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	17:18:00.200411-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1ef196, Nexy(98990), 'prim'', displayID:'com.nexy.assistant'}
default	17:18:00.200468-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	17:18:00.200470-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1ef196, Nexy(98990), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 407 stopping recording
default	17:18:00.200509-0500	audiomxd	-MXCoreSession- -[MXCoreSession endInterruption:]: Session <ID: 407, PID = 98990, Name = sid:0x1ef196, Nexy(98990), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> is going inactive
default	17:18:00.200541-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 407, PID = 98990, Name = sid:0x1ef196, Nexy(98990), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	17:18:00.200577-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 407, PID = 98990, Name = sid:0x1ef196, Nexy(98990), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	17:18:00.200720-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 200 flag 0x1 < Hijack > app com.nexy.assistant CID 0xD310001 category Not set
default	17:18:00.200704-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 0]. BT device UIDS: {(
)}
default	17:18:00.200726-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	17:18:00.203598-0500	runningboardd	Invalidating assertion 398-334-1382383 (target:[app<application.com.nexy.assistant.20408399.20408405(501)>:98990]) from originator [osservice<com.apple.powerd>:334]
default	17:18:00.205039-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	17:18:00.205068-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	17:18:00.205085-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	17:18:00.204937-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	17:18:00.205101-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	17:18:00.204989-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	17:18:00.205164-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	17:18:00.205178-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	17:18:00.205189-0500	audioaccessoryd	AudioStateChanged: Removed audio session app com.nexy.assistant 201 count 0
default	17:18:00.206708-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	17:18:00.207165-0500	coreaudiod	Sending message. { reporterID=425158812631042, category=IO, type=error, message=["cause": Optional(ClientHALIODurationExceededBudget), "safety_violation": Optional(0), "io_cycle_usage": Optional(1), "deadline": Optional(29348), "reporting_latency": Optional(72562875), "wg_external_wakeups": Optional(3), "HostApplicationDisplayID": Optional(com.nexy.assistant), "wg_user_time_mach": Optional(80083), "wg_instructions": Optional(7038134), "overload_type": Optional(Overload), "time_since_prev_overload": Optional(463018889901541), "is_recovering": Optional(0), "input_device_transport_list": Optional(Bluetooth), "num_continuous_silent_io_cycles": Optional(0), "wg_total_wakeups": Optional(5), "anchor_sample_time": Optional(8), "smallest_buffer_frame_size": Optional(2147483647), "sample_rate": Optional(24000), "io_page_faults_duration": Optional(0), "careporting_timestamp": 1762208280.2068691, "io_page_faults": Optional(0), "input_device_source_list": Optional(Unknown), "input_device_uid_list": Optional(3:input), "other_page_faults": Optional(0), "io_frame_<…> }
default	17:18:00.211930-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	17:18:00.211946-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	17:18:00.211957-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	17:18:00.211965-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	17:18:00.211972-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	17:18:00.211978-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	17:18:00.212068-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	17:18:00.287951-0500	runningboardd	[app<application.com.nexy.assistant.20408399.20408405(501)>:98990] Ignoring jetsam update because this process is not memory-managed
default	17:18:00.287971-0500	runningboardd	[app<application.com.nexy.assistant.20408399.20408405(501)>:98990] Ignoring suspend because this process is not lifecycle managed
default	17:18:00.288014-0500	runningboardd	[app<application.com.nexy.assistant.20408399.20408405(501)>:98990] Set darwin role to: None
default	17:18:00.288027-0500	runningboardd	[app<application.com.nexy.assistant.20408399.20408405(501)>:98990] Ignoring GPU update because this process is not GPU managed
default	17:18:00.288103-0500	runningboardd	[app<application.com.nexy.assistant.20408399.20408405(501)>:98990] Ignoring memory limit update because this process is not memory-managed
default	17:18:00.292228-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.20408399.20408405(501)>: running-suspended (role: None) (endowments: (null))
default	17:18:00.296798-0500	gamepolicyd	Received state update for 98990 (app<application.com.nexy.assistant.20408399.20408405(501)>, running-suspended-NotVisible
default	17:18:00.367424-0500	Nexy	                AUHAL.cpp:473   ~AUHAL: (0xc17428e40) Selecting device 0 from destructor
default	17:18:00.367443-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0xc17428e40)
default	17:18:00.367453-0500	Nexy	                AUHAL.cpp:676   SelectDevice: (0xc17428e40) not already running
default	17:18:00.367459-0500	Nexy	                AUHAL.cpp:682   SelectDevice: (0xc17428e40) disconnecting device 91
default	17:18:00.367466-0500	Nexy	                AUHAL.cpp:746   SelectDevice: (0xc17428e40) destroying ioproc 0xa for device 91
default	17:18:00.367501-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xa}
default	17:18:00.367536-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	17:18:00.367774-0500	Nexy	                AUHAL.cpp:848   SelectDevice: (0xc17428e40) nothing to setup
default	17:18:00.367793-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0xc17428e40) adding 0 device listeners to device 0
default	17:18:00.367800-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0xc17428e40) adding 0 device delegate listeners to device 0
default	17:18:00.367809-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0xc17428e40) removing 7 device listeners from device 91
default	17:18:00.368098-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0xc17428e40) removing 0 device delegate listeners from device 91
default	17:18:00.368113-0500	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0xc17428e40)
default	17:18:00.471662-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=99028.1, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=98990, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.osascript, pid=99028, auid=501, euid=501, binary_path=/usr/bin/osascript}, },
default	17:18:00.472352-0500	tccd	AUTHREQ_SUBJECT: msgID=99028.1, subject=com.nexy.assistant,
default	17:18:00.472686-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117000 at /Applications/Nexy.app
default	17:18:00.479861-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=393.13858, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=98990, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.osascript, pid=99028, auid=501, euid=501, binary_path=/usr/bin/osascript}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=393, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	17:18:00.480312-0500	tccd	AUTHREQ_SUBJECT: msgID=393.13858, subject=com.nexy.assistant,
default	17:18:00.480645-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117000 at /Applications/Nexy.app
default	17:18:00.502064-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117000 at /Applications/Nexy.app
default	17:18:00.517024-0500	System Events	TCCAccessRequestIndirect: TCCAccessRequestIndirect with pid 98994: target_identity: {
    kTCCCodeIdentityAuditToken = {length = 32, bytes = 0xf5010000 f5010000 14000000 f5010000 ... b7860100 7b551f00 };
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
default	17:18:00.527967-0500	tccd	target_executable_path_URL: file:///Applications/Nexy.app/Contents/MacOS/Nexy
default	17:18:01.391484-0500	Nexy	[0xc163cc640] activating connection: mach=true listener=false peer=false name=com.apple.distributed_notifications@Uv3
default	17:18:01.392396-0500	Nexy	[0xc163cc8c0] activating connection: mach=true listener=false peer=false name=com.apple.analyticsd
default	17:18:01.394082-0500	Nexy	Received configuration update from daemon (initial)
default	17:18:01.422900-0500	Nexy	[0xc163cca00] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
error	17:18:01.423234-0500	tccd	TCCDProcess: identifier=com.nexy.assistant, pid=98990, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy attempted to call TCCAccessRequest for kTCCServiceAccessibility without the recommended com.apple.private.tcc.manager.check-by-audit-token entitlement
default	17:18:01.423329-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=98990.2, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=98990, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.nexy.assistant, pid=98990, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	17:18:01.424145-0500	tccd	AUTHREQ_SUBJECT: msgID=98990.2, subject=com.nexy.assistant,
default	17:18:01.424509-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117000 at /Applications/Nexy.app
default	17:18:01.431020-0500	Nexy	[0xc163cca00] invalidated after the last release of the connection object
default	17:18:01.431454-0500	Nexy	[0xc163cca00] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
error	17:18:01.431669-0500	tccd	TCCDProcess: identifier=com.nexy.assistant, pid=98990, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy attempted to call TCCAccessRequest for kTCCServiceAccessibility without the recommended com.apple.private.tcc.manager.check-by-audit-token entitlement
default	17:18:01.431754-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=98990.3, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=98990, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.nexy.assistant, pid=98990, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	17:18:01.432216-0500	tccd	AUTHREQ_SUBJECT: msgID=98990.3, subject=com.nexy.assistant,
default	17:18:01.432544-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117000 at /Applications/Nexy.app
default	17:18:01.438374-0500	Nexy	[0xc163cca00] invalidated after the last release of the connection object
default	17:18:01.438405-0500	Nexy	[0xc163cca00] activating connection: mach=true listener=false peer=false name=com.apple.universalaccessAuthWarn
default	17:18:01.438460-0500	Nexy	[0xc163cca00] invalidated after the last release of the connection object
default	17:18:01.438642-0500	Nexy	[0xc163ccb40] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	17:18:01.438906-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=98990.4, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=98990, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	17:18:01.439342-0500	tccd	AUTHREQ_SUBJECT: msgID=98990.4, subject=com.nexy.assistant,
default	17:18:01.439666-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117000 at /Applications/Nexy.app
default	17:18:01.445250-0500	tccd	Notifying for access  kTCCServiceListenEvent for target PID[98990], responsiblePID[98990], responsiblePath: /Applications/Nexy.app to UID: 501
default	17:18:01.445369-0500	Nexy	[0xc163ccb40] invalidated after the last release of the connection object
default	17:18:01.445538-0500	Nexy	server port 0x0000f213, session port 0x0000c40f
default	17:18:01.446058-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=393.13859, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=98990, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=393, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	17:18:01.446069-0500	tccd	requestor: TCCDProcess: identifier=com.apple.WindowServer, pid=393, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=98990, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	17:18:01.446552-0500	tccd	AUTHREQ_SUBJECT: msgID=393.13859, subject=com.nexy.assistant,
default	17:18:01.447273-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117000 at /Applications/Nexy.app
default	17:18:01.455282-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d114900 at /Applications/Nexy.app
default	17:18:01.467768-0500	Nexy	server port 0x0000c40f, session port 0x0000c40f
default	17:18:01.467799-0500	kernel	SK[7]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid D4D3C993-B03A-49ED-AB97-B0DC464A06B6 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.57421,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0xd69121df tp_proto=0x06"
default	17:18:01.467825-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:57421<-><IPv4-redacted>:53] interface: utun6 (skipped: 6843)
so_gencnt: 5136013 t_state: SYN_SENT process: Nexy:98990 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 1 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xb95ee9b2
default	17:18:01.468086-0500	kernel	tcp connected: [<IPv4-redacted>:57421<-><IPv4-redacted>:53] interface: utun6 (skipped: 6843)
so_gencnt: 5136013 t_state: ESTABLISHED process: Nexy:98990 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 1 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xb95ee9b2
default	17:18:01.468096-0500	Nexy	[0xc163ccb40] activating connection: mach=true listener=false peer=false name=com.apple.coreservices.launchservicesd
default	17:18:01.468750-0500	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:57421<-><IPv4-redacted>:53] interface: utun6 (skipped: 6843)
so_gencnt: 5136013 t_state: FIN_WAIT_1 process: Nexy:98990 Duration: 0.001 sec Conn_Time: 0.001 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 1.000 ms rttvar: 0.500 ms base rtt: 1 ms so_error: 0 svc/tc: 0 flow: 0xb95ee9b2
default	17:18:01.468758-0500	kernel	tcp_connection_summary [<IPv4-redacted>:57421<-><IPv4-redacted>:53] interface: utun6 (skipped: 6843)
so_gencnt: 5136013 t_state: FIN_WAIT_1 process: Nexy:98990 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	17:18:01.468823-0500	Nexy	networkd_settings_read_from_file initialized networkd settings by reading plist directly
default	17:18:01.468908-0500	kernel	SK[9]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 099E19A4-3013-4DAA-B086-4C5AB9A21E8F flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.57422,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0xc6731f6a tp_proto=0x06"
default	17:18:01.468919-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:57422<-><IPv4-redacted>:53] interface: utun6 (skipped: 6843)
so_gencnt: 5136014 t_state: SYN_SENT process: Nexy:98990 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 1 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xabfd3393
default	17:18:01.468951-0500	Nexy	networkd_settings_read_from_file initialized networkd settings by reading plist directly
default	17:18:01.469024-0500	kernel	tcp connected: [<IPv4-redacted>:57422<-><IPv4-redacted>:53] interface: utun6 (skipped: 6843)
so_gencnt: 5136014 t_state: ESTABLISHED process: Nexy:98990 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 1 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xabfd3393
default	17:18:01.469139-0500	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:57422<-><IPv4-redacted>:53] interface: utun6 (skipped: 6843)
so_gencnt: 5136014 t_state: FIN_WAIT_1 process: Nexy:98990 Duration: 0.001 sec Conn_Time: 0.000 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 1.000 ms rttvar: 0.500 ms base rtt: 1 ms so_error: 0 svc/tc: 0 flow: 0xabfd3393
default	17:18:01.469144-0500	kernel	tcp_connection_summary [<IPv4-redacted>:57422<-><IPv4-redacted>:53] interface: utun6 (skipped: 6843)
so_gencnt: 5136014 t_state: FIN_WAIT_1 process: Nexy:98990 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	17:18:01.469512-0500	Nexy	nw_path_libinfo_path_check [EB4C9C14-BAF5-43EB-AA20-8E83F928D9A0 IPv4#82b3fe6f:443 tcp, legacy-socket, attribution: developer]
	libinfo check path: <private>
default	17:18:01.470024-0500	kernel	SK[7]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 0015CD5F-3FD5-4976-8325-ED70DFF93FA8 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.57423,dst=<IPv4-redacted>.443,proto=0x06 mask=0x0000003f,hash=0x75539e77 tp_proto=0x06"
default	17:18:01.470035-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:57423<-><IPv4-redacted>:443] interface: utun6 (skipped: 6843)
so_gencnt: 5136015 t_state: SYN_SENT process: Nexy:98990 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x950a9118
default	17:18:01.470045-0500	Nexy	New connection 0x129917 main
default	17:18:01.470215-0500	kernel	tcp connected: [<IPv4-redacted>:57423<-><IPv4-redacted>:443] interface: utun6 (skipped: 6843)
so_gencnt: 5136015 t_state: ESTABLISHED process: Nexy:98990 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x950a9118
default	17:18:01.470140-0500	Nexy	[0xc163ccc80] activating connection: mach=true listener=false peer=false name=com.apple.pasteboard.1
default	17:18:01.472048-0500	Nexy	[0xc163ccf00] activating connection: mach=true listener=false peer=false name=com.apple.lsd.mapdb
default	17:18:01.472996-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117000 at /Applications/Nexy.app
default	17:18:01.476996-0500	tccd	Publishing <TCCDEvent: type=Modify, service=kTCCServiceAccessibility, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 0 subscribers: {
}
default	17:18:01.506392-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d114900 at /Applications/Nexy.app
default	17:18:01.517926-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117000 at /Applications/Nexy.app
default	17:18:01.520896-0500	tccd	Publishing <TCCDEvent: type=Modify, service=kTCCServiceListenEvent, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 0 subscribers: {
}
default	17:18:01.627820-0500	Nexy	[0xc163ccdc0] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	17:18:01.628487-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=98990.5, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=98990, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	17:18:01.634687-0500	tccd	AUTHREQ_SUBJECT: msgID=98990.5, subject=com.nexy.assistant,
default	17:18:01.635241-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117000 at /Applications/Nexy.app
default	17:18:01.645467-0500	Nexy	[0xc163ccdc0] invalidated after the last release of the connection object
default	17:18:01.653124-0500	Nexy	void _NSDisableAutomaticTerminationAndLog(NSString *) No windows open yet
default	17:18:01.654721-0500	Nexy	CHECKIN: pid=98990
default	17:18:01.659595-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.20408399.20408405(501)>:98990] from originator [osservice<com.apple.coreservices.launchservicesd>:363] with description <RBSAssertionDescriptor| "uielement:98990" ID:398-363-1382395 target:98990 attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"RoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	17:18:01.659662-0500	runningboardd	Assertion 398-363-1382395 (target:[app<application.com.nexy.assistant.20408399.20408405(501)>:98990]) will be created as active
default	17:18:01.660032-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.20408399.20408405(501)>:98990] from originator [osservice<com.apple.coreservices.launchservicesd>:363] with description <RBSAssertionDescriptor| "uielement:98990" ID:398-363-1382396 target:98990 attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"RoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	17:18:01.660046-0500	runningboardd	[app<application.com.nexy.assistant.20408399.20408405(501)>:98990] Ignoring jetsam update because this process is not memory-managed
default	17:18:01.660149-0500	runningboardd	[app<application.com.nexy.assistant.20408399.20408405(501)>:98990] Ignoring suspend because this process is not lifecycle managed
default	17:18:01.660166-0500	runningboardd	Assertion 398-363-1382396 (target:[app<application.com.nexy.assistant.20408399.20408405(501)>:98990]) will be created as active
default	17:18:01.660218-0500	runningboardd	[app<application.com.nexy.assistant.20408399.20408405(501)>:98990] Set darwin role to: UserInteractive
default	17:18:01.659625-0500	launchservicesd	CHECKIN:0x0-0x148f48e 98990 com.nexy.assistant
default	17:18:01.660283-0500	runningboardd	[app<application.com.nexy.assistant.20408399.20408405(501)>:98990] Ignoring GPU update because this process is not GPU managed
default	17:18:01.660063-0500	Nexy	CHECKEDIN: pid=98990 asn=0x0-0x148f48e foreground=0
default	17:18:01.660482-0500	loginwindow	-[Application updateInformation] | Got App URL: file:///Applications/Nexy.app/
default	17:18:01.660322-0500	Nexy	[0xc163cd040] activating connection: mach=true listener=false peer=false name=com.apple.lsd.modifydb
default	17:18:01.660363-0500	runningboardd	[app<application.com.nexy.assistant.20408399.20408405(501)>:98990] Ignoring memory limit update because this process is not memory-managed
default	17:18:01.660640-0500	loginwindow	-[ApplicationManager checkInAppContext:eventData:] | ApplicationManager: Checked in app : Nexy
default	17:18:01.660629-0500	Nexy	[0xc163cd180] activating connection: mach=false listener=true peer=false name=(anonymous)
default	17:18:01.660634-0500	Nexy	[0xc163cd180] Connection returned listener port: 0x10303
default	17:18:01.660706-0500	Nexy	[0xc170e0600] activating connection: mach=false listener=false peer=true name=com.apple.xpc.anonymous.0xc163cd180.peer[363].0xc170e0600
default	17:18:01.661813-0500	Nexy	FRONTLOGGING: version 1
default	17:18:01.661822-0500	Nexy	Registered, pid=98990 ASN=0x0,0x148f48e
default	17:18:01.662003-0500	WindowServer	129917[CreateApplication]: Process creation: 0x0-0x148f48e (Nexy) connectionID: 129917 pid: 98990 in session 0x101
default	17:18:01.665106-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.20408399.20408405(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	17:18:01.665313-0500	runningboardd	Invalidating assertion 398-363-1382395 (target:[app<application.com.nexy.assistant.20408399.20408405(501)>:98990]) from originator [osservice<com.apple.coreservices.launchservicesd>:363]
default	17:18:01.665602-0500	gamepolicyd	Received state update for 98990 (app<application.com.nexy.assistant.20408399.20408405(501)>, running-active-NotVisible
default	17:18:01.665633-0500	Nexy	[0xc163cd180] Connection returned listener port: 0x10303
default	17:18:01.665993-0500	Nexy	BringForward: pid=98990 asn=0x0-0x148f48e bringForward=0 foreground=0 uiElement=1 launchedByLS=0 modifiersCount=0 allDisabled=0
default	17:18:01.666232-0500	Nexy	Current system appearance, (HLTB: 1), (SLS: 0)
default	17:18:01.667090-0500	Nexy	Current system appearance, (HLTB: 1), (SLS: 0)
default	17:18:01.667412-0500	Nexy	Post-registration system appearance: (HLTB: 1)
default	17:18:01.684614-0500	lsd	com.nexy.assistant/Unknown Persona:5:5:1:1:Building bundle record for app
default	17:18:01.684696-0500	lsd	com.nexy.assistant/Unknown Persona:5:5:2:1:Built bundle record for app
default	17:18:01.688360-0500	Nexy	FBSWorkspace: endpoint monitoring is disabled.
default	17:18:01.688366-0500	Nexy	FBSWorkspace: default shell endpoint is disabled.
default	17:18:01.688402-0500	Nexy	Initializing connection
default	17:18:01.688429-0500	Nexy	Removing all cached process handles
default	17:18:01.688441-0500	Nexy	Sending handshake request attempt #1 to server
default	17:18:01.688446-0500	Nexy	Creating connection to com.apple.runningboard
default	17:18:01.688452-0500	Nexy	[0xc163cd2c0] activating connection: mach=true listener=false peer=false name=com.apple.runningboard
default	17:18:01.688699-0500	runningboardd	Setting client for [app<application.com.nexy.assistant.20408399.20408405(501)>:98990] as ready
default	17:18:01.689066-0500	Nexy	Handshake succeeded
default	17:18:01.689075-0500	Nexy	Identity resolved as app<application.com.nexy.assistant.20408399.20408405(501)>
default	17:18:01.692003-0500	Nexy	[0xc163cd180] Connection returned listener port: 0x10303
default	17:18:01.692627-0500	distnoted	register name: com.apple.xctest.FakeForceTouchDevice object: com.nexy.assistant token: 2d00000024 pid: 98990
default	17:18:01.693753-0500	Nexy	[0xc163cd180] Connection returned listener port: 0x10303
default	17:18:01.694576-0500	Nexy	Created a new Process Instance Registry XPC connection (inactive)
default	17:18:01.694588-0500	Nexy	[0xc163cd400] activating connection: mach=true listener=false peer=false name=com.apple.linkd.autoShortcut
default	17:18:01.694642-0500	Nexy	Activated connection to com.apple.linkd.autoShortcut (ApplicationService)
default	17:18:01.694775-0500	Nexy	[0xc163cd680] activating connection: mach=false listener=true peer=false name=(anonymous)
default	17:18:01.696979-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.20408399.20408405(501)>:98990] from originator [osservice<com.apple.coreservices.launchservicesd>:363] with description <RBSAssertionDescriptor| "frontmost:98990" ID:398-363-1382397 target:98990 attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"RoleUserInteractiveFocal" sourceEnvironment:"(null)">
	]>
default	17:18:01.697027-0500	runningboardd	Assertion 398-363-1382397 (target:[app<application.com.nexy.assistant.20408399.20408405(501)>:98990]) will be created as active
default	17:18:01.697385-0500	WindowServer	129917[SetFrontProcessWithInfo]: [DeferringManager] Updating policy {
    advicePolicy: .frontmost;
    frontmostProcess: 0x0-0x148f48e (Nexy) mainConnectionID: 129917;
} for reason: updated frontmost process
default	17:18:01.697429-0500	WindowServer	129917[SetFrontProcessWithInfo]: [DeferringManager] Deferring events from frontmost process PSN 0x0-0x148f48e (Nexy) -> <pid: 98990>
default	17:18:01.697510-0500	WindowServer	new deferring rules for pid:393: [
    [393-C051]; <keyboardFocus; Nexy:0x0-0x148f48e>; () -> <pid: 98990>; reason: frontmost PSN --> outbound target,
    [393-C050]; <keyboardFocus; <frontmost>>; () -> <token: Nexy:0x0-0x148f48e; pid: 393>; reason: frontmost PSN,
    [393-C04F]; <keyboardFocus>; () -> <token: <frontmost>; pid: 393>; reason: Deferring to <frontmost>
]
default	17:18:01.697566-0500	WindowServer	[keyboardFocus 0x7facf2b20] setRules:forPID(393): [
    [393-C051]; <keyboardFocus; Nexy:0x0-0x148f48e>; () -> <pid: 98990>; reason: frontmost PSN --> outbound target,
    [393-C050]; <keyboardFocus; <frontmost>>; () -> <token: Nexy:0x0-0x148f48e; pid: 393>; reason: frontmost PSN,
    [393-C04F]; <keyboardFocus>; () -> <token: <frontmost>; pid: 393>; reason: Deferring to <frontmost>
]
default	17:18:01.697851-0500	runningboardd	[app<application.com.nexy.assistant.20408399.20408405(501)>:98990] Ignoring jetsam update because this process is not memory-managed
default	17:18:01.697930-0500	Nexy	[0xc163cd680] Connection returned listener port: 0x13c03
default	17:18:01.697916-0500	runningboardd	[app<application.com.nexy.assistant.20408399.20408405(501)>:98990] Ignoring suspend because this process is not lifecycle managed
default	17:18:01.697989-0500	runningboardd	[app<application.com.nexy.assistant.20408399.20408405(501)>:98990] Set darwin role to: UserInteractiveFocal
default	17:18:01.698020-0500	runningboardd	[app<application.com.nexy.assistant.20408399.20408405(501)>:98990] Ignoring GPU update because this process is not GPU managed
default	17:18:01.698120-0500	runningboardd	[app<application.com.nexy.assistant.20408399.20408405(501)>:98990] Ignoring memory limit update because this process is not memory-managed
default	17:18:01.698333-0500	Nexy	Registered process with identifier 98990-2053488
default	17:18:01.698481-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.20408399.20408405(501)>:98990] from originator [osservice<com.apple.coreservices.launchservicesd>:363] with description <RBSAssertionDescriptor| "notification:98990" ID:398-363-1382398 target:98990 attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"LSNotification" sourceEnvironment:"(null)">
	]>
default	17:18:01.698550-0500	runningboardd	Assertion 398-363-1382398 (target:[app<application.com.nexy.assistant.20408399.20408405(501)>:98990]) will be created as active
default	17:18:01.698662-0500	WindowServer	chain did update (setDeferringRules) <keyboardFocus; display: null> containsEndOfChain: YES; [
    <token: <frontmost>; pid: 393>,
    <token: Nexy:0x0-0x148f48e; pid: 393>,
    <pid: 98990>
]
default	17:18:01.700539-0500	Nexy	[0xc163cd900] activating connection: mach=true listener=false peer=false name=com.apple.usernoted.client
default	17:18:01.704125-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.20408399.20408405(501)>: running-active (role: UserInteractiveFocal) (endowments: <private>)
default	17:18:01.704396-0500	runningboardd	[app<application.com.nexy.assistant.20408399.20408405(501)>:98990] Ignoring jetsam update because this process is not memory-managed
default	17:18:01.704422-0500	runningboardd	[app<application.com.nexy.assistant.20408399.20408405(501)>:98990] Ignoring suspend because this process is not lifecycle managed
default	17:18:01.704442-0500	runningboardd	[app<application.com.nexy.assistant.20408399.20408405(501)>:98990] Ignoring GPU update because this process is not GPU managed
default	17:18:01.704513-0500	runningboardd	[app<application.com.nexy.assistant.20408399.20408405(501)>:98990] Ignoring memory limit update because this process is not memory-managed
default	17:18:01.708812-0500	usernoted	Connection com.nexy.assistant with path: /Applications/Nexy.app
default	17:18:01.708807-0500	distnoted	register name: com.apple.nsquiet_safe_quit_give_reason object: com.nexy.assistant token: 3100000032 pid: 98990
default	17:18:01.710299-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.20408399.20408405(501)>: running-active (role: UserInteractiveFocal) (endowments: <private>)
default	17:18:01.715174-0500	Nexy	NSApp cache appearance:
-NSRequiresAquaSystemAppearance: 0
-appearance: (null)
-effectiveAppearance: <NSCompositeAppearance: 0xc17709360
 (
    "<NSAquaAppearance: 0xc17709400>",
    "<NSSystemAppearance: 0xc17708fa0>"
)>
default	17:18:01.719105-0500	Nexy	[0xc163cde00] activating connection: mach=true listener=false peer=false name=com.apple.dock.fullscreen
default	17:18:01.719177-0500	Nexy	[0xc163cdf40] activating connection: mach=true listener=false peer=false name=com.apple.fonts
default	17:18:01.720747-0500	Nexy	(<private>) deleteSearchableItemsWithDomainIdentifiers, protectionClass:(null), domainIdentifiers number:1
default	17:18:01.720947-0500	Nexy	sConnectionName: com.apple.spotlight.IndexAgent
default	17:18:01.720952-0500	Nexy	Start service name com.apple.spotlight.IndexAgent
default	17:18:01.720952-0500	Nexy	[C:1] Alloc com.apple.controlcenter.statusitems
default	17:18:01.720969-0500	Nexy	[0xc163ce080] activating connection: mach=true listener=false peer=false name=com.apple.spotlight.IndexAgent
default	17:18:01.720983-0500	Nexy	[0xc163ce1c0] activating connection: mach=false listener=false peer=false name=(anonymous)
default	17:18:01.721028-0500	Nexy	FBSWorkspace registering source: <private>
default	17:18:01.721707-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	17:18:01.722027-0500	Nexy	<FBSWorkspaceScenesClient:0xc17709fe0 <private>> attempting immediate handshake from activate
default	17:18:01.722124-0500	Nexy	<FBSWorkspaceScenesClient:0xc17709fe0 <private>> sent handshake
default	17:18:01.722275-0500	Nexy	Realizing settings extension __NSStatusItemSceneHostSettings__ on FBSSceneSettings
default	17:18:01.725857-0500	Nexy	<FBSWorkspaceScenesClient:0xc17709fe0 <private>> was invalidated
default	17:18:01.725874-0500	Nexy	FBSWorkspace unregistering source: <private>
default	17:18:01.726074-0500	suggestd	SGDSpotlightReceiver: deleting 1 domain identifiers (1 after removing overlaps) for com.nexy.assistant: <private>
default	17:18:01.726403-0500	Nexy	Realizing settings extension __NSStatusItemSceneClientSettings__ on FBSSceneClientSettings
default	17:18:01.727760-0500	Nexy	Realizing settings extension FBSSceneSettingsCore on FBSSceneSettings
default	17:18:01.728920-0500	Nexy	Realizing settings extension FBSSceneClientSettingsCore on FBSSceneClientSettings
default	17:18:01.729270-0500	Nexy	Requesting scene <FBSScene: 0xc1770a300; com.apple.controlcenter:720CB185-E04A-442C-AE9F-38A96A09C220> from com.apple.controlcenter.statusitems
error	17:18:01.729391-0500	Nexy	Error creating <FBSScene: 0xc1770a300; com.apple.controlcenter:720CB185-E04A-442C-AE9F-38A96A09C220>: <NSError: 0xc189eba50; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
default	17:18:01.730492-0500	Nexy	Request for <FBSScene: 0xc1770a300; com.apple.controlcenter:720CB185-E04A-442C-AE9F-38A96A09C220> complete!
default	17:18:01.734369-0500	Nexy	Warning: the app is using `-[NSStatusBarButton setHighlightsBy:]` to set the highlight behavior. Instead, consider removing that setting. That will enable macOS to highlight the status bar button as appropriate for all configurations (e.g., light, dark, and increased contrast modes).
default	17:18:01.745215-0500	Nexy	Registering for test daemon availability notify post.
default	17:18:01.745348-0500	Nexy	notify_get_state check indicated test daemon not ready.
default	17:18:01.745415-0500	Nexy	notify_get_state check indicated test daemon not ready.
default	17:18:01.745479-0500	Nexy	notify_get_state check indicated test daemon not ready.
default	17:18:01.746470-0500	Nexy	[0xc163ce580] activating connection: mach=true listener=false peer=false name=com.apple.coreservices.appleevents
default	17:18:01.746848-0500	Nexy	[0xc163cd180] Connection returned listener port: 0x10303
default	17:18:01.747065-0500	Nexy	SignalReady: pid=98990 asn=0x0-0x148f48e
default	17:18:01.747245-0500	Nexy	SIGNAL: pid=98990 asn=0x0x-0x148f48e
default	17:18:01.747765-0500	loginwindow	-[Application updateInformation] | Got App URL: file:///Applications/Nexy.app/
error	17:18:01.748909-0500	Nexy	scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
default	17:18:01.750298-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117000 at /Applications/Nexy.app
default	17:18:01.751059-0500	Nexy	void _NSDisableAutomaticTerminationAndLog(NSString *) Restoring windows
default	17:18:01.751072-0500	Nexy	-[NSApplication _reopenWindowsAsNecessaryIncludingRestorableState:withFullFidelity:completionHandler:] shouldRestoreState=1 hasPersistentStateToRestore=0 shouldStillRestoreStateAfterPrompting=0
default	17:18:01.751121-0500	Nexy	[0xc163ccdc0] activating connection: mach=true listener=false peer=false name=com.apple.window_proxies
default	17:18:01.751192-0500	Nexy	[0xc163ccdc0] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	17:18:01.752093-0500	Nexy	void _NSEnableAutomaticTerminationAndLog(NSString *) Restoring windows
default	17:18:01.754013-0500	Nexy	[0xc163ccdc0] activating connection: mach=false listener=false peer=false name=com.apple.ViewBridgeAuxiliary
default	17:18:01.759778-0500	Nexy	[0xc163ce800] activating connection: mach=false listener=false peer=false name=(anonymous)
default	17:18:01.760206-0500	Nexy	[0xc163ce940] activating connection: mach=false listener=true peer=false name=(anonymous)
default	17:18:01.760212-0500	Nexy	[0xc163ce940] Connection returned listener port: 0x15e03
error	17:18:01.761193-0500	kernel	Sandbox: WindowManager(584) deny(1) mach-task-name others [Nexy(98990)]
default	17:18:01.761082-0500	Nexy	[C:2] Alloc <private>
default	17:18:01.761107-0500	Nexy	[0xc163cea80] activating connection: mach=false listener=false peer=false name=(anonymous)
default	17:18:01.761620-0500	Nexy	[0xc163ccdc0] invalidated after the last release of the connection object
default	17:18:01.762495-0500	WindowManager	Connection activated | (98990) Nexy
default	17:18:01.762774-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.20408399.20408405(501)>:98990] from originator [app<application.com.nexy.assistant.20408399.20408405(501)>:98990] with description <RBSAssertionDescriptor| "AudioHAL" ID:398-98990-1382399 target:98990 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	17:18:01.762813-0500	runningboardd	Assertion 398-98990-1382399 (target:[app<application.com.nexy.assistant.20408399.20408405(501)>:98990]) will be created as active
default	17:18:01.763020-0500	runningboardd	Invalidating assertion 398-98990-1382399 (target:[app<application.com.nexy.assistant.20408399.20408405(501)>:98990]) from originator [app<application.com.nexy.assistant.20408399.20408405(501)>:98990]
default	17:18:01.763051-0500	runningboardd	[app<application.com.nexy.assistant.20408399.20408405(501)>:98990] Ignoring jetsam update because this process is not memory-managed
default	17:18:01.763097-0500	runningboardd	[app<application.com.nexy.assistant.20408399.20408405(501)>:98990] Ignoring suspend because this process is not lifecycle managed
default	17:18:01.763132-0500	runningboardd	[app<application.com.nexy.assistant.20408399.20408405(501)>:98990] Ignoring GPU update because this process is not GPU managed
default	17:18:01.763159-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.20408399.20408405(501)>:98990] from originator [app<application.com.nexy.assistant.20408399.20408405(501)>:98990] with description <RBSAssertionDescriptor| "AudioHAL" ID:398-98990-1382400 target:98990 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	17:18:01.763220-0500	runningboardd	Assertion 398-98990-1382400 (target:[app<application.com.nexy.assistant.20408399.20408405(501)>:98990]) will be created as active
default	17:18:01.763207-0500	runningboardd	[app<application.com.nexy.assistant.20408399.20408405(501)>:98990] Ignoring memory limit update because this process is not memory-managed
default	17:18:01.767534-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.20408399.20408405(501)>: running-active (role: UserInteractiveFocal) (endowments: <private>)
default	17:18:01.767693-0500	runningboardd	Invalidating assertion 398-98990-1382400 (target:[app<application.com.nexy.assistant.20408399.20408405(501)>:98990]) from originator [app<application.com.nexy.assistant.20408399.20408405(501)>:98990]
default	17:18:01.767811-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.20408399.20408405(501)>:98990] from originator [app<application.com.nexy.assistant.20408399.20408405(501)>:98990] with description <RBSAssertionDescriptor| "AudioHAL" ID:398-98990-1382401 target:98990 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	17:18:01.767864-0500	runningboardd	Assertion 398-98990-1382401 (target:[app<application.com.nexy.assistant.20408399.20408405(501)>:98990]) will be created as active
default	17:18:01.768030-0500	runningboardd	Invalidating assertion 398-98990-1382401 (target:[app<application.com.nexy.assistant.20408399.20408405(501)>:98990]) from originator [app<application.com.nexy.assistant.20408399.20408405(501)>:98990]
default	17:18:01.768167-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.20408399.20408405(501)>:98990] from originator [app<application.com.nexy.assistant.20408399.20408405(501)>:98990] with description <RBSAssertionDescriptor| "AudioHAL" ID:398-98990-1382402 target:98990 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	17:18:01.768210-0500	runningboardd	Assertion 398-98990-1382402 (target:[app<application.com.nexy.assistant.20408399.20408405(501)>:98990]) will be created as active
default	17:18:01.768366-0500	runningboardd	Invalidating assertion 398-98990-1382402 (target:[app<application.com.nexy.assistant.20408399.20408405(501)>:98990]) from originator [app<application.com.nexy.assistant.20408399.20408405(501)>:98990]
default	17:18:01.768479-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.20408399.20408405(501)>:98990] from originator [app<application.com.nexy.assistant.20408399.20408405(501)>:98990] with description <RBSAssertionDescriptor| "AudioHAL" ID:398-98990-1382403 target:98990 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	17:18:01.768527-0500	runningboardd	Assertion 398-98990-1382403 (target:[app<application.com.nexy.assistant.20408399.20408405(501)>:98990]) will be created as active
default	17:18:01.768709-0500	runningboardd	Invalidating assertion 398-98990-1382403 (target:[app<application.com.nexy.assistant.20408399.20408405(501)>:98990]) from originator [app<application.com.nexy.assistant.20408399.20408405(501)>:98990]
default	17:18:01.768767-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.20408399.20408405(501)>:98990] from originator [app<application.com.nexy.assistant.20408399.20408405(501)>:98990] with description <RBSAssertionDescriptor| "AudioHAL" ID:398-98990-1382404 target:98990 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	17:18:01.768789-0500	runningboardd	Assertion 398-98990-1382404 (target:[app<application.com.nexy.assistant.20408399.20408405(501)>:98990]) will be created as active
default	17:18:01.768924-0500	runningboardd	Invalidating assertion 398-98990-1382404 (target:[app<application.com.nexy.assistant.20408399.20408405(501)>:98990]) from originator [app<application.com.nexy.assistant.20408399.20408405(501)>:98990]
default	17:18:01.771774-0500	gamepolicyd	Received state update for 98990 (app<application.com.nexy.assistant.20408399.20408405(501)>, running-active-NotVisible
default	17:18:01.865611-0500	runningboardd	[app<application.com.nexy.assistant.20408399.20408405(501)>:98990] Ignoring jetsam update because this process is not memory-managed
default	17:18:01.865626-0500	runningboardd	[app<application.com.nexy.assistant.20408399.20408405(501)>:98990] Ignoring suspend because this process is not lifecycle managed
default	17:18:01.865637-0500	runningboardd	[app<application.com.nexy.assistant.20408399.20408405(501)>:98990] Ignoring GPU update because this process is not GPU managed
default	17:18:01.865654-0500	runningboardd	[app<application.com.nexy.assistant.20408399.20408405(501)>:98990] Ignoring memory limit update because this process is not memory-managed
default	17:18:01.869090-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.20408399.20408405(501)>: running-active (role: UserInteractiveFocal) (endowments: <private>)
default	17:18:01.869426-0500	gamepolicyd	Received state update for 98990 (app<application.com.nexy.assistant.20408399.20408405(501)>, running-active-NotVisible
default	17:18:02.005008-0500	Nexy	[0xc163cca00] activating connection: mach=false listener=false peer=false name=com.apple.hiservices-xpcservice
default	17:18:02.009794-0500	Nexy	+[IMKClient subclass]: chose IMKClient_Modern
default	17:18:02.009819-0500	Nexy	+[IMKInputSession subclass]: chose IMKInputSession_Modern
default	17:18:02.014491-0500	Nexy	[0xc163ce6c0] activating connection: mach=true listener=false peer=false name=com.apple.inputmethodkit.getxpcendpoint
default	17:18:02.015547-0500	Nexy	[0xc163ccdc0] activating connection: mach=true listener=false peer=false name=com.apple.inputmethodkit.getxpcendpoint
default	17:18:02.016124-0500	Nexy	[0xc163cebc0] activating connection: mach=false listener=false peer=false name=(anonymous)
default	17:18:02.016278-0500	Nexy	[0xc163cee40] activating connection: mach=false listener=false peer=false name=(anonymous)
default	17:18:02.016613-0500	DictationIM	setting current input controller = com.nexy.assistant
default	17:18:02.017282-0500	Nexy	[0xc163ced00] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
error	17:18:02.017997-0500	tccd	TCCDProcess: identifier=com.nexy.assistant, pid=98990, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy attempted to call TCCAccessRequest for kTCCServiceAccessibility without the recommended com.apple.private.tcc.manager.check-by-audit-token entitlement
default	17:18:02.018076-0500	Nexy	[0xc163ced00] invalidated after the last release of the connection object
default	17:18:02.023469-0500	Nexy	void _NSDisableAutomaticTerminationAndLog(NSString *) NSAccessibility Request Received
default	17:18:02.222837-0500	Nexy	*warn* MailCS ======%%% _setMailMessageAttributes skip:1
default	17:18:02.229520-0500	Nexy	Start service name com.apple.spotlightknowledged
default	17:18:02.231136-0500	Nexy	[GMS] availability notification token 75
default	17:18:02.429271-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(50321)
default	17:18:02.429342-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:50321 called from <private>
default	17:18:02.429357-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:50321 called from <private>
default	17:18:02.429946-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(50320)
default	17:18:02.429991-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:50320 called from <private>
default	17:18:02.430002-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:50320 called from <private>
default	17:18:02.452883-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:50320 called from <private>
default	17:18:02.452915-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:50320 called from <private>
default	17:18:02.454011-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(50320)
default	17:18:02.454041-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:50320 called from <private>
default	17:18:02.454049-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:50320 called from <private>
default	17:18:02.457714-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(50320)
default	17:18:02.457745-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(50320)
default	17:18:02.457757-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(50320)
default	17:18:02.457982-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(50320)
default	17:18:02.458818-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:50320 called from <private>
default	17:18:02.458832-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:50320 called from <private>
default	17:18:02.459245-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(50321)
default	17:18:02.459275-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:50321 called from <private>
default	17:18:02.459283-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:50321 called from <private>
default	17:18:02.475284-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:50320 called from <private>
default	17:18:02.475316-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:50320 called from <private>
default	17:18:02.476327-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 3 3, id:50320 called from <private>
default	17:18:02.476346-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 4 4, id:50320 called from <private>
default	17:18:02.476526-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(50320)
default	17:18:02.493858-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(50320)
default	17:18:02.494267-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 4 4 id:50320 called from <private>
default	17:18:02.494278-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 3 3 id:50320 called from <private>
default	17:18:02.494375-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(50320)
default	17:18:02.497529-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(50320)
default	17:18:02.497857-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:50320 called from <private>
default	17:18:02.497865-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:50320 called from <private>
default	17:18:02.497884-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:50320 called from <private>
default	17:18:02.497893-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:50320 called from <private>
default	17:18:02.497899-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:50320 called from <private>
default	17:18:02.497905-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:50320 called from <private>
default	17:18:02.497940-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:50320 called from <private>
default	17:18:02.498018-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:50320 called from <private>
default	17:18:02.498089-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:50320 called from <private>
default	17:18:02.498135-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:50320 called from <private>
default	17:18:02.498181-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:50320 called from <private>
default	17:18:02.498224-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:50320 called from <private>
default	17:18:02.498267-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:50320 called from <private>
default	17:18:02.498317-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:50320 called from <private>
default	17:18:02.498346-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:50320 called from <private>
default	17:18:02.498394-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:50320 called from <private>
default	17:18:02.498451-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:50320 called from <private>
default	17:18:02.498522-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:50320 called from <private>
default	17:18:02.750375-0500	Nexy	FBSWorkspace registering source: <private>
default	17:18:02.750422-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	17:18:02.750513-0500	Nexy	<FBSWorkspaceScenesClient:0xc1770af80 <private>> attempting immediate handshake from activate
default	17:18:02.750555-0500	Nexy	<FBSWorkspaceScenesClient:0xc1770af80 <private>> sent handshake
default	17:18:02.750901-0500	Nexy	Requesting scene <FBSScene: 0xc1770b020; com.apple.controlcenter:D75C5E1F-C5E5-4DF0-A79A-D5F3E4FBC337> from com.apple.controlcenter.statusitems
default	17:18:02.751080-0500	Nexy	<FBSWorkspaceScenesClient:0xc1770af80 <private>> was invalidated
default	17:18:02.751132-0500	Nexy	FBSWorkspace unregistering source: <private>
default	17:18:02.751192-0500	Nexy	Request for <FBSScene: 0xc1770b020; com.apple.controlcenter:D75C5E1F-C5E5-4DF0-A79A-D5F3E4FBC337> complete!
error	17:18:02.751225-0500	Nexy	Error creating <FBSScene: 0xc1770b020; com.apple.controlcenter:D75C5E1F-C5E5-4DF0-A79A-D5F3E4FBC337>: <NSError: 0xc170fc030; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	17:18:02.751257-0500	Nexy	No scene exists for identity: com.apple.controlcenter:D75C5E1F-C5E5-4DF0-A79A-D5F3E4FBC337
error	17:18:02.751293-0500	Nexy	scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
default	17:18:03.010327-0500	runningboardd	Invalidating assertion 398-363-1382397 (target:[app<application.com.nexy.assistant.20408399.20408405(501)>:98990]) from originator [osservice<com.apple.coreservices.launchservicesd>:363]
default	17:18:03.016849-0500	Nexy	void _updateToReflectAutomaticTerminationState(void) Setting _kLSApplicationWouldBeTerminatedByTALKey=1
default	17:18:03.118895-0500	runningboardd	[app<application.com.nexy.assistant.20408399.20408405(501)>:98990] Ignoring jetsam update because this process is not memory-managed
default	17:18:03.118911-0500	runningboardd	[app<application.com.nexy.assistant.20408399.20408405(501)>:98990] Ignoring suspend because this process is not lifecycle managed
default	17:18:03.118942-0500	runningboardd	[app<application.com.nexy.assistant.20408399.20408405(501)>:98990] Set darwin role to: UserInteractive
default	17:18:03.118957-0500	runningboardd	[app<application.com.nexy.assistant.20408399.20408405(501)>:98990] Ignoring GPU update because this process is not GPU managed
default	17:18:03.118982-0500	runningboardd	[app<application.com.nexy.assistant.20408399.20408405(501)>:98990] Ignoring memory limit update because this process is not memory-managed
default	17:18:03.122978-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.20408399.20408405(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	17:18:03.123404-0500	gamepolicyd	Received state update for 98990 (app<application.com.nexy.assistant.20408399.20408405(501)>, running-active-NotVisible
default	17:18:03.752516-0500	Nexy	FBSWorkspace registering source: <private>
default	17:18:03.752536-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	17:18:03.752584-0500	Nexy	<FBSWorkspaceScenesClient:0xc1770b020 <private>> attempting immediate handshake from activate
default	17:18:03.752608-0500	Nexy	<FBSWorkspaceScenesClient:0xc1770b020 <private>> sent handshake
default	17:18:03.752803-0500	Nexy	Requesting scene <FBSScene: 0xc1770af80; com.apple.controlcenter:A83DFAEE-519F-4932-8CD9-4A5E7A008F13> from com.apple.controlcenter.statusitems
default	17:18:03.753071-0500	Nexy	Request for <FBSScene: 0xc1770af80; com.apple.controlcenter:A83DFAEE-519F-4932-8CD9-4A5E7A008F13> complete!
default	17:18:03.753096-0500	Nexy	<FBSWorkspaceScenesClient:0xc1770b020 <private>> was invalidated
default	17:18:03.753117-0500	Nexy	FBSWorkspace unregistering source: <private>
default	17:18:03.753161-0500	Nexy	Realizing settings extension FBSSceneTransitionContextCore on FBSSceneTransitionContext
default	17:18:03.755489-0500	Nexy	<FBSWorkspaceScenesClient:0xc1770ae40 <private>> attempting immediate handshake from activate
default	17:18:03.755508-0500	Nexy	<FBSWorkspaceScenesClient:0xc1770ae40 <private>> sent handshake
default	17:18:03.755580-0500	Nexy	Realizing settings extension __NSHostedViewSceneSettings__ on FBSSceneSettings
default	17:18:03.756014-0500	Nexy	<FBSWorkspaceScenesClient:0xc1770ae40 <private>> was invalidated
default	17:18:03.756016-0500	Nexy	Realizing settings extension __NSClientHostedViewSceneSettings__ on FBSSceneClientSettings
default	17:18:03.756042-0500	Nexy	FBSWorkspace unregistering source: <private>
default	17:18:03.756366-0500	Nexy	Realizing settings extension __NSStatusItemAuxiliaryViewSceneSettings__ on FBSSceneSettings
default	17:18:03.756408-0500	Nexy	Realizing settings extension __NSClientStatusItemAuxiliaryViewSceneSettings__ on FBSSceneClientSettings
default	17:18:03.756762-0500	Nexy	Requesting scene <FBSScene: 0xc1770b0c0; com.apple.controlcenter:A83DFAEE-519F-4932-8CD9-4A5E7A008F13-Aux[1]-NSStatusItemView> from com.apple.controlcenter.statusitems
error	17:18:03.756916-0500	Nexy	Error creating <FBSScene: 0xc1770b0c0; com.apple.controlcenter:A83DFAEE-519F-4932-8CD9-4A5E7A008F13-Aux[1]-NSStatusItemView>: <NSError: 0xc170fc060; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
default	17:18:03.756953-0500	Nexy	Request for <FBSScene: 0xc1770b0c0; com.apple.controlcenter:A83DFAEE-519F-4932-8CD9-4A5E7A008F13-Aux[1]-NSStatusItemView> complete!
error	17:18:03.757244-0500	Nexy	scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	17:18:03.757260-0500	Nexy	[com.apple.controlcenter:A83DFAEE-519F-4932-8CD9-4A5E7A008F13] No matching scene to invalidate for this identity.
error	17:18:03.757283-0500	Nexy	auxiliary scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	17:18:03.757324-0500	Nexy	Unhandled disconnected scene <private>
default	17:18:04.758603-0500	Nexy	FBSWorkspace registering source: <private>
default	17:18:04.758625-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	17:18:04.758740-0500	Nexy	<FBSWorkspaceScenesClient:0xc1770b0c0 <private>> attempting immediate handshake from activate
default	17:18:04.758765-0500	Nexy	<FBSWorkspaceScenesClient:0xc1770b0c0 <private>> sent handshake
default	17:18:04.758974-0500	Nexy	Requesting scene <FBSScene: 0xc1770af80; com.apple.controlcenter:A039FC8D-98B0-4575-901B-74256BBBBEEA> from com.apple.controlcenter.statusitems
default	17:18:04.759160-0500	Nexy	Request for <FBSScene: 0xc1770af80; com.apple.controlcenter:A039FC8D-98B0-4575-901B-74256BBBBEEA> complete!
default	17:18:04.759483-0500	Nexy	Requesting scene <FBSScene: 0xc1770b200; com.apple.controlcenter:A039FC8D-98B0-4575-901B-74256BBBBEEA-Aux[2]-NSStatusItemView> from com.apple.controlcenter.statusitems
default	17:18:04.759526-0500	Nexy	<FBSWorkspaceScenesClient:0xc1770b0c0 <private>> was invalidated
default	17:18:04.759551-0500	Nexy	FBSWorkspace unregistering source: <private>
error	17:18:04.759598-0500	Nexy	Error creating <FBSScene: 0xc1770af80; com.apple.controlcenter:A039FC8D-98B0-4575-901B-74256BBBBEEA>: <NSError: 0xc170fc1b0; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	17:18:04.759613-0500	Nexy	No scene exists for identity: com.apple.controlcenter:A039FC8D-98B0-4575-901B-74256BBBBEEA
error	17:18:04.759644-0500	Nexy	Error creating <FBSScene: 0xc1770b200; com.apple.controlcenter:A039FC8D-98B0-4575-901B-74256BBBBEEA-Aux[2]-NSStatusItemView>: <NSError: 0xc170fc000; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
default	17:18:04.759646-0500	Nexy	Request for <FBSScene: 0xc1770b200; com.apple.controlcenter:A039FC8D-98B0-4575-901B-74256BBBBEEA-Aux[2]-NSStatusItemView> complete!
error	17:18:04.759654-0500	Nexy	No scene exists for identity: com.apple.controlcenter:A039FC8D-98B0-4575-901B-74256BBBBEEA-Aux[2]-NSStatusItemView
error	17:18:04.759798-0500	Nexy	scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	17:18:04.759813-0500	Nexy	[com.apple.controlcenter:A039FC8D-98B0-4575-901B-74256BBBBEEA] No matching scene to invalidate for this identity.
error	17:18:04.759838-0500	Nexy	auxiliary scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	17:18:04.759901-0500	Nexy	Unhandled disconnected scene <private>
error	17:18:04.759947-0500	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
default	17:18:05.761369-0500	Nexy	FBSWorkspace registering source: <private>
default	17:18:05.761410-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	17:18:05.761504-0500	Nexy	<FBSWorkspaceScenesClient:0xc1770af80 <private>> attempting immediate handshake from activate
default	17:18:05.761544-0500	Nexy	<FBSWorkspaceScenesClient:0xc1770af80 <private>> sent handshake
default	17:18:05.761914-0500	Nexy	Requesting scene <FBSScene: 0xc1770b200; com.apple.controlcenter:6B2292EB-43BF-4345-B742-7A4258D4A3F1> from com.apple.controlcenter.statusitems
default	17:18:05.762249-0500	Nexy	Request for <FBSScene: 0xc1770b200; com.apple.controlcenter:6B2292EB-43BF-4345-B742-7A4258D4A3F1> complete!
default	17:18:05.762718-0500	Nexy	<FBSWorkspaceScenesClient:0xc1770af80 <private>> was invalidated
default	17:18:05.762753-0500	Nexy	FBSWorkspace unregistering source: <private>
error	17:18:05.762850-0500	Nexy	Error creating <FBSScene: 0xc1770b200; com.apple.controlcenter:6B2292EB-43BF-4345-B742-7A4258D4A3F1>: <NSError: 0xc170139f0; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	17:18:05.762880-0500	Nexy	No scene exists for identity: com.apple.controlcenter:6B2292EB-43BF-4345-B742-7A4258D4A3F1
default	17:18:05.762928-0500	Nexy	Requesting scene <FBSScene: 0xc1770b0c0; com.apple.controlcenter:6B2292EB-43BF-4345-B742-7A4258D4A3F1-Aux[3]-NSStatusItemView> from com.apple.controlcenter.statusitems
error	17:18:05.763088-0500	Nexy	Error creating <FBSScene: 0xc1770b0c0; com.apple.controlcenter:6B2292EB-43BF-4345-B742-7A4258D4A3F1-Aux[3]-NSStatusItemView>: <NSError: 0xc189eae50; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
default	17:18:05.763129-0500	Nexy	Request for <FBSScene: 0xc1770b0c0; com.apple.controlcenter:6B2292EB-43BF-4345-B742-7A4258D4A3F1-Aux[3]-NSStatusItemView> complete!
error	17:18:05.763322-0500	Nexy	scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	17:18:05.763339-0500	Nexy	[com.apple.controlcenter:6B2292EB-43BF-4345-B742-7A4258D4A3F1] No matching scene to invalidate for this identity.
error	17:18:05.763372-0500	Nexy	auxiliary scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	17:18:05.763415-0500	Nexy	Unhandled disconnected scene <private>
error	17:18:05.763484-0500	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
default	17:18:06.746778-0500	runningboardd	Assertion did invalidate due to timeout: 398-363-1382398 (target:[app<application.com.nexy.assistant.20408399.20408405(501)>:98990])
default	17:18:06.764914-0500	Nexy	FBSWorkspace registering source: <private>
default	17:18:06.764955-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	17:18:06.765059-0500	Nexy	<FBSWorkspaceScenesClient:0xc1770b0c0 <private>> attempting immediate handshake from activate
default	17:18:06.765094-0500	Nexy	<FBSWorkspaceScenesClient:0xc1770b0c0 <private>> sent handshake
default	17:18:06.765419-0500	Nexy	Requesting scene <FBSScene: 0xc1770b200; com.apple.controlcenter:D87CF442-1C58-48A3-894D-F425B8D7AFFD> from com.apple.controlcenter.statusitems
default	17:18:06.765702-0500	Nexy	Request for <FBSScene: 0xc1770b200; com.apple.controlcenter:D87CF442-1C58-48A3-894D-F425B8D7AFFD> complete!
default	17:18:06.766129-0500	Nexy	<FBSWorkspaceScenesClient:0xc1770b0c0 <private>> was invalidated
default	17:18:06.766164-0500	Nexy	FBSWorkspace unregistering source: <private>
error	17:18:06.766256-0500	Nexy	Error creating <FBSScene: 0xc1770b200; com.apple.controlcenter:D87CF442-1C58-48A3-894D-F425B8D7AFFD>: <NSError: 0xc17013900; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	17:18:06.766278-0500	Nexy	No scene exists for identity: com.apple.controlcenter:D87CF442-1C58-48A3-894D-F425B8D7AFFD
default	17:18:06.766318-0500	Nexy	Requesting scene <FBSScene: 0xc1770af80; com.apple.controlcenter:D87CF442-1C58-48A3-894D-F425B8D7AFFD-Aux[4]-NSStatusItemView> from com.apple.controlcenter.statusitems
error	17:18:06.766448-0500	Nexy	Error creating <FBSScene: 0xc1770af80; com.apple.controlcenter:D87CF442-1C58-48A3-894D-F425B8D7AFFD-Aux[4]-NSStatusItemView>: <NSError: 0xc189ebf90; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
default	17:18:06.766494-0500	Nexy	Request for <FBSScene: 0xc1770af80; com.apple.controlcenter:D87CF442-1C58-48A3-894D-F425B8D7AFFD-Aux[4]-NSStatusItemView> complete!
error	17:18:06.766661-0500	Nexy	scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	17:18:06.766680-0500	Nexy	[com.apple.controlcenter:D87CF442-1C58-48A3-894D-F425B8D7AFFD] No matching scene to invalidate for this identity.
error	17:18:06.766719-0500	Nexy	auxiliary scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	17:18:06.766753-0500	Nexy	Unhandled disconnected scene <private>
error	17:18:06.766823-0500	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
default	17:18:06.852900-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d116100 at /Applications/Nexy.app
default	17:18:06.865623-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d114900 at /Applications/Nexy.app
default	17:18:06.872594-0500	tccd	Publishing <TCCDEvent: type=Modify, service=kTCCServiceListenEvent, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 0 subscribers: {
}
default	17:18:06.949120-0500	runningboardd	[app<application.com.nexy.assistant.20408399.20408405(501)>:98990] Ignoring jetsam update because this process is not memory-managed
default	17:18:06.949131-0500	runningboardd	[app<application.com.nexy.assistant.20408399.20408405(501)>:98990] Ignoring suspend because this process is not lifecycle managed
default	17:18:06.949137-0500	runningboardd	[app<application.com.nexy.assistant.20408399.20408405(501)>:98990] Ignoring GPU update because this process is not GPU managed
default	17:18:06.949151-0500	runningboardd	[app<application.com.nexy.assistant.20408399.20408405(501)>:98990] Ignoring memory limit update because this process is not memory-managed
default	17:18:06.952908-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.20408399.20408405(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	17:18:06.953257-0500	gamepolicyd	Received state update for 98990 (app<application.com.nexy.assistant.20408399.20408405(501)>, running-active-NotVisible
default	17:18:07.768156-0500	Nexy	FBSWorkspace registering source: <private>
default	17:18:07.768193-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	17:18:07.768281-0500	Nexy	<FBSWorkspaceScenesClient:0xc1770af80 <private>> attempting immediate handshake from activate
default	17:18:07.768313-0500	Nexy	<FBSWorkspaceScenesClient:0xc1770af80 <private>> sent handshake
default	17:18:07.768630-0500	Nexy	Requesting scene <FBSScene: 0xc1770b200; com.apple.controlcenter:67E89FC6-F5DD-467F-B01A-0E82A3775B7B> from com.apple.controlcenter.statusitems
default	17:18:07.768907-0500	Nexy	Request for <FBSScene: 0xc1770b200; com.apple.controlcenter:67E89FC6-F5DD-467F-B01A-0E82A3775B7B> complete!
default	17:18:07.769145-0500	Nexy	<FBSWorkspaceScenesClient:0xc1770af80 <private>> was invalidated
default	17:18:07.769175-0500	Nexy	FBSWorkspace unregistering source: <private>
error	17:18:07.769241-0500	Nexy	Error creating <FBSScene: 0xc1770b200; com.apple.controlcenter:67E89FC6-F5DD-467F-B01A-0E82A3775B7B>: <NSError: 0xc170138a0; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	17:18:07.769259-0500	Nexy	No scene exists for identity: com.apple.controlcenter:67E89FC6-F5DD-467F-B01A-0E82A3775B7B
default	17:18:07.769296-0500	Nexy	FBSWorkspace registering source: <private>
default	17:18:07.769314-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	17:18:07.769361-0500	Nexy	<FBSWorkspaceScenesClient:0xc1770b340 <private>> attempting immediate handshake from activate
default	17:18:07.769381-0500	Nexy	<FBSWorkspaceScenesClient:0xc1770b340 <private>> sent handshake
default	17:18:07.769530-0500	Nexy	Requesting scene <FBSScene: 0xc1770b020; com.apple.controlcenter:67E89FC6-F5DD-467F-B01A-0E82A3775B7B-Aux[5]-NSStatusItemView> from com.apple.controlcenter.statusitems
default	17:18:07.769833-0500	Nexy	Request for <FBSScene: 0xc1770b020; com.apple.controlcenter:67E89FC6-F5DD-467F-B01A-0E82A3775B7B-Aux[5]-NSStatusItemView> complete!
default	17:18:07.769855-0500	Nexy	<FBSWorkspaceScenesClient:0xc1770b340 <private>> was invalidated
default	17:18:07.769881-0500	Nexy	FBSWorkspace unregistering source: <private>
error	17:18:07.769947-0500	Nexy	Error creating <FBSScene: 0xc1770b020; com.apple.controlcenter:67E89FC6-F5DD-467F-B01A-0E82A3775B7B-Aux[5]-NSStatusItemView>: <NSError: 0xc170131e0; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	17:18:07.769967-0500	Nexy	No scene exists for identity: com.apple.controlcenter:67E89FC6-F5DD-467F-B01A-0E82A3775B7B-Aux[5]-NSStatusItemView
default	17:18:07.770824-0500	Nexy	[com.apple.controlcenter:67E89FC6-F5DD-467F-B01A-0E82A3775B7B-Aux[5]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
error	17:18:07.771147-0500	Nexy	scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	17:18:07.771163-0500	Nexy	[com.apple.controlcenter:67E89FC6-F5DD-467F-B01A-0E82A3775B7B] No matching scene to invalidate for this identity.
error	17:18:07.771189-0500	Nexy	auxiliary scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	17:18:07.771205-0500	Nexy	[com.apple.controlcenter:67E89FC6-F5DD-467F-B01A-0E82A3775B7B-Aux[5]-NSStatusItemView] No matching scene to invalidate for this identity.
error	17:18:07.771747-0500	Nexy	Unhandled disconnected scene <private>
error	17:18:07.771822-0500	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
error	17:18:07.771879-0500	Nexy	Unhandled disconnected auxiliary scene <private>
error	17:18:07.771914-0500	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
default	17:18:08.772326-0500	Nexy	FBSWorkspace registering source: <private>
default	17:18:08.772360-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	17:18:08.772443-0500	Nexy	<FBSWorkspaceScenesClient:0xc1770b020 <private>> attempting immediate handshake from activate
default	17:18:08.772469-0500	Nexy	<FBSWorkspaceScenesClient:0xc1770b020 <private>> sent handshake
default	17:18:08.772744-0500	Nexy	Requesting scene <FBSScene: 0xc1770b200; com.apple.controlcenter:DABBBEE3-EC16-41EE-AFAF-E11B1FE094F1> from com.apple.controlcenter.statusitems
default	17:18:08.772978-0500	Nexy	Request for <FBSScene: 0xc1770b200; com.apple.controlcenter:DABBBEE3-EC16-41EE-AFAF-E11B1FE094F1> complete!
default	17:18:08.773232-0500	Nexy	<FBSWorkspaceScenesClient:0xc1770b020 <private>> was invalidated
default	17:18:08.773258-0500	Nexy	FBSWorkspace unregistering source: <private>
default	17:18:08.773303-0500	Nexy	FBSWorkspace registering source: <private>
default	17:18:08.773319-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	17:18:08.773365-0500	Nexy	<FBSWorkspaceScenesClient:0xc1770b2a0 <private>> attempting immediate handshake from activate
default	17:18:08.773386-0500	Nexy	<FBSWorkspaceScenesClient:0xc1770b2a0 <private>> sent handshake
error	17:18:08.773441-0500	Nexy	Error creating <FBSScene: 0xc1770b200; com.apple.controlcenter:DABBBEE3-EC16-41EE-AFAF-E11B1FE094F1>: <NSError: 0xc17013f60; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	17:18:08.773457-0500	Nexy	No scene exists for identity: com.apple.controlcenter:DABBBEE3-EC16-41EE-AFAF-E11B1FE094F1
default	17:18:08.773519-0500	Nexy	Requesting scene <FBSScene: 0xc1770af80; com.apple.controlcenter:DABBBEE3-EC16-41EE-AFAF-E11B1FE094F1-Aux[6]-NSStatusItemView> from com.apple.controlcenter.statusitems
default	17:18:08.773685-0500	Nexy	Request for <FBSScene: 0xc1770af80; com.apple.controlcenter:DABBBEE3-EC16-41EE-AFAF-E11B1FE094F1-Aux[6]-NSStatusItemView> complete!
default	17:18:08.773802-0500	Nexy	<FBSWorkspaceScenesClient:0xc1770b2a0 <private>> was invalidated
default	17:18:08.773824-0500	Nexy	FBSWorkspace unregistering source: <private>
error	17:18:08.773866-0500	Nexy	Error creating <FBSScene: 0xc1770af80; com.apple.controlcenter:DABBBEE3-EC16-41EE-AFAF-E11B1FE094F1-Aux[6]-NSStatusItemView>: <NSError: 0xc170fc000; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	17:18:08.773881-0500	Nexy	No scene exists for identity: com.apple.controlcenter:DABBBEE3-EC16-41EE-AFAF-E11B1FE094F1-Aux[6]-NSStatusItemView
default	17:18:08.774171-0500	Nexy	[com.apple.controlcenter:DABBBEE3-EC16-41EE-AFAF-E11B1FE094F1-Aux[6]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
error	17:18:08.774370-0500	Nexy	scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	17:18:08.774385-0500	Nexy	[com.apple.controlcenter:DABBBEE3-EC16-41EE-AFAF-E11B1FE094F1] No matching scene to invalidate for this identity.
error	17:18:08.774410-0500	Nexy	auxiliary scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	17:18:08.774425-0500	Nexy	[com.apple.controlcenter:DABBBEE3-EC16-41EE-AFAF-E11B1FE094F1-Aux[6]-NSStatusItemView] No matching scene to invalidate for this identity.
error	17:18:08.774769-0500	Nexy	Unhandled disconnected scene <private>
error	17:18:08.774838-0500	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
error	17:18:08.774900-0500	Nexy	Unhandled disconnected auxiliary scene <private>
error	17:18:08.774933-0500	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
default	17:18:09.776060-0500	Nexy	FBSWorkspace registering source: <private>
default	17:18:09.776102-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	17:18:09.776189-0500	Nexy	<FBSWorkspaceScenesClient:0xc1770af80 <private>> attempting immediate handshake from activate
default	17:18:09.776223-0500	Nexy	<FBSWorkspaceScenesClient:0xc1770af80 <private>> sent handshake
default	17:18:09.776520-0500	Nexy	Requesting scene <FBSScene: 0xc1770b200; com.apple.controlcenter:38CF1875-B12B-4D11-966D-269C7D3FE376> from com.apple.controlcenter.statusitems
default	17:18:09.776793-0500	Nexy	Request for <FBSScene: 0xc1770b200; com.apple.controlcenter:38CF1875-B12B-4D11-966D-269C7D3FE376> complete!
default	17:18:09.777240-0500	Nexy	<FBSWorkspaceScenesClient:0xc1770af80 <private>> was invalidated
default	17:18:09.777271-0500	Nexy	FBSWorkspace unregistering source: <private>
error	17:18:09.777328-0500	Nexy	Error creating <FBSScene: 0xc1770b200; com.apple.controlcenter:38CF1875-B12B-4D11-966D-269C7D3FE376>: <NSError: 0xc17013f00; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	17:18:09.777347-0500	Nexy	No scene exists for identity: com.apple.controlcenter:38CF1875-B12B-4D11-966D-269C7D3FE376
error	17:18:09.777399-0500	Nexy	Error creating <FBSScene: 0xc1770ae40; com.apple.controlcenter:38CF1875-B12B-4D11-966D-269C7D3FE376-Aux[7]-NSStatusItemView>: <NSError: 0xc17013630; domain: FBSWorkspaceErrorDomain; code: 1 ("InvalidScene"); "scene <FBSScene: 0xc1770ae40; com.apple.controlcenter:38CF1875-B12B-4D11-966D-269C7D3FE376-Aux[7]-NSStatusItemView> was invalidated before activation com.apple.controlcenter.statusitems">
error	17:18:09.777420-0500	Nexy	No scene exists for identity: com.apple.controlcenter:38CF1875-B12B-4D11-966D-269C7D3FE376-Aux[7]-NSStatusItemView
error	17:18:09.777570-0500	Nexy	scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	17:18:09.777592-0500	Nexy	[com.apple.controlcenter:38CF1875-B12B-4D11-966D-269C7D3FE376] No matching scene to invalidate for this identity.
error	17:18:09.777621-0500	Nexy	auxiliary scene activation failed: Error Domain=FBSWorkspaceErrorDomain Code=1 UserInfo={BSErrorCodeDescription=InvalidScene, NSLocalizedFailureReason=<private>}
error	17:18:09.777698-0500	Nexy	Unhandled disconnected scene <private>
error	17:18:09.777754-0500	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
default	17:18:10.779002-0500	Nexy	FBSWorkspace registering source: <private>
default	17:18:10.779037-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	17:18:10.779110-0500	Nexy	<FBSWorkspaceScenesClient:0xc1770b200 <private>> attempting immediate handshake from activate
default	17:18:10.779141-0500	Nexy	<FBSWorkspaceScenesClient:0xc1770b200 <private>> sent handshake
default	17:18:10.779417-0500	Nexy	Requesting scene <FBSScene: 0xc1770ae40; com.apple.controlcenter:A781F5FE-E7E5-4B73-867F-DAC7D6733C6F> from com.apple.controlcenter.statusitems
default	17:18:10.779692-0500	Nexy	Request for <FBSScene: 0xc1770ae40; com.apple.controlcenter:A781F5FE-E7E5-4B73-867F-DAC7D6733C6F> complete!
default	17:18:10.780086-0500	Nexy	<FBSWorkspaceScenesClient:0xc1770b200 <private>> was invalidated
default	17:18:10.780117-0500	Nexy	FBSWorkspace unregistering source: <private>
error	17:18:10.780200-0500	Nexy	Error creating <FBSScene: 0xc1770ae40; com.apple.controlcenter:A781F5FE-E7E5-4B73-867F-DAC7D6733C6F>: <NSError: 0xc170137e0; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	17:18:10.780217-0500	Nexy	No scene exists for identity: com.apple.controlcenter:A781F5FE-E7E5-4B73-867F-DAC7D6733C6F
default	17:18:10.780249-0500	Nexy	Requesting scene <FBSScene: 0xc1770af80; com.apple.controlcenter:A781F5FE-E7E5-4B73-867F-DAC7D6733C6F-Aux[8]-NSStatusItemView> from com.apple.controlcenter.statusitems
error	17:18:10.780539-0500	Nexy	Error creating <FBSScene: 0xc1770af80; com.apple.controlcenter:A781F5FE-E7E5-4B73-867F-DAC7D6733C6F-Aux[8]-NSStatusItemView>: <NSError: 0xc189eafa0; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
default	17:18:10.780625-0500	Nexy	Request for <FBSScene: 0xc1770af80; com.apple.controlcenter:A781F5FE-E7E5-4B73-867F-DAC7D6733C6F-Aux[8]-NSStatusItemView> complete!
error	17:18:10.780905-0500	Nexy	scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	17:18:10.780942-0500	Nexy	[com.apple.controlcenter:A781F5FE-E7E5-4B73-867F-DAC7D6733C6F] No matching scene to invalidate for this identity.
error	17:18:10.780996-0500	Nexy	auxiliary scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	17:18:10.781047-0500	Nexy	Unhandled disconnected scene <private>
error	17:18:10.781141-0500	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
default	17:18:11.782397-0500	Nexy	FBSWorkspace registering source: <private>
default	17:18:11.782438-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	17:18:11.782529-0500	Nexy	<FBSWorkspaceScenesClient:0xc1770af80 <private>> attempting immediate handshake from activate
default	17:18:11.782561-0500	Nexy	<FBSWorkspaceScenesClient:0xc1770af80 <private>> sent handshake
default	17:18:11.782872-0500	Nexy	Requesting scene <FBSScene: 0xc1770ae40; com.apple.controlcenter:FECC2087-39A7-4240-B81A-3E0B37BC7506> from com.apple.controlcenter.statusitems
default	17:18:11.783133-0500	Nexy	Request for <FBSScene: 0xc1770ae40; com.apple.controlcenter:FECC2087-39A7-4240-B81A-3E0B37BC7506> complete!
default	17:18:11.783555-0500	Nexy	<FBSWorkspaceScenesClient:0xc1770af80 <private>> was invalidated
default	17:18:11.783587-0500	Nexy	FBSWorkspace unregistering source: <private>
default	17:18:11.783667-0500	Nexy	LSExceptions shared instance invalidated for timeout.
error	17:18:11.783684-0500	Nexy	Error creating <FBSScene: 0xc1770ae40; com.apple.controlcenter:FECC2087-39A7-4240-B81A-3E0B37BC7506>: <NSError: 0xc17013a20; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	17:18:11.783704-0500	Nexy	No scene exists for identity: com.apple.controlcenter:FECC2087-39A7-4240-B81A-3E0B37BC7506
default	17:18:11.783737-0500	Nexy	Requesting scene <FBSScene: 0xc1770b200; com.apple.controlcenter:FECC2087-39A7-4240-B81A-3E0B37BC7506-Aux[9]-NSStatusItemView> from com.apple.controlcenter.statusitems
error	17:18:11.783866-0500	Nexy	Error creating <FBSScene: 0xc1770b200; com.apple.controlcenter:FECC2087-39A7-4240-B81A-3E0B37BC7506-Aux[9]-NSStatusItemView>: <NSError: 0xc189e9ec0; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
default	17:18:11.783915-0500	Nexy	Request for <FBSScene: 0xc1770b200; com.apple.controlcenter:FECC2087-39A7-4240-B81A-3E0B37BC7506-Aux[9]-NSStatusItemView> complete!
error	17:18:11.784071-0500	Nexy	scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	17:18:11.784090-0500	Nexy	[com.apple.controlcenter:FECC2087-39A7-4240-B81A-3E0B37BC7506] No matching scene to invalidate for this identity.
error	17:18:11.784116-0500	Nexy	auxiliary scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	17:18:11.784145-0500	Nexy	Unhandled disconnected scene <private>
error	17:18:11.784214-0500	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
default	17:18:12.785680-0500	Nexy	FBSWorkspace registering source: <private>
default	17:18:12.785741-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	17:18:12.785886-0500	Nexy	<FBSWorkspaceScenesClient:0xc1770b200 <private>> attempting immediate handshake from activate
default	17:18:12.785938-0500	Nexy	<FBSWorkspaceScenesClient:0xc1770b200 <private>> sent handshake
default	17:18:12.786406-0500	Nexy	Requesting scene <FBSScene: 0xc1770ae40; com.apple.controlcenter:AC0CD3C5-8017-48CC-BE64-AD963B6086BF> from com.apple.controlcenter.statusitems
default	17:18:12.786829-0500	Nexy	Request for <FBSScene: 0xc1770ae40; com.apple.controlcenter:AC0CD3C5-8017-48CC-BE64-AD963B6086BF> complete!
default	17:18:12.787441-0500	Nexy	<FBSWorkspaceScenesClient:0xc1770b200 <private>> was invalidated
default	17:18:12.787491-0500	Nexy	FBSWorkspace unregistering source: <private>
error	17:18:12.787643-0500	Nexy	Error creating <FBSScene: 0xc1770ae40; com.apple.controlcenter:AC0CD3C5-8017-48CC-BE64-AD963B6086BF>: <NSError: 0xc17013600; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	17:18:12.787686-0500	Nexy	No scene exists for identity: com.apple.controlcenter:AC0CD3C5-8017-48CC-BE64-AD963B6086BF
default	17:18:12.787753-0500	Nexy	Requesting scene <FBSScene: 0xc1770af80; com.apple.controlcenter:AC0CD3C5-8017-48CC-BE64-AD963B6086BF-Aux[10]-NSStatusItemView> from com.apple.controlcenter.statusitems
error	17:18:12.787962-0500	Nexy	Error creating <FBSScene: 0xc1770af80; com.apple.controlcenter:AC0CD3C5-8017-48CC-BE64-AD963B6086BF-Aux[10]-NSStatusItemView>: <NSError: 0xc17013c60; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
default	17:18:12.788058-0500	Nexy	Request for <FBSScene: 0xc1770af80; com.apple.controlcenter:AC0CD3C5-8017-48CC-BE64-AD963B6086BF-Aux[10]-NSStatusItemView> complete!
error	17:18:12.788259-0500	Nexy	scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	17:18:12.788280-0500	Nexy	[com.apple.controlcenter:AC0CD3C5-8017-48CC-BE64-AD963B6086BF] No matching scene to invalidate for this identity.
error	17:18:12.788309-0500	Nexy	auxiliary scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	17:18:12.788336-0500	Nexy	Unhandled disconnected scene <private>
error	17:18:12.788403-0500	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
default	17:18:13.789431-0500	Nexy	FBSWorkspace registering source: <private>
default	17:18:13.789463-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	17:18:13.789535-0500	Nexy	<FBSWorkspaceScenesClient:0xc1770af80 <private>> attempting immediate handshake from activate
default	17:18:13.789563-0500	Nexy	<FBSWorkspaceScenesClient:0xc1770af80 <private>> sent handshake
default	17:18:13.789807-0500	Nexy	Requesting scene <FBSScene: 0xc1770ae40; com.apple.controlcenter:7307F095-23A5-476D-A567-6F32F2342CA3> from com.apple.controlcenter.statusitems
default	17:18:13.790025-0500	Nexy	Request for <FBSScene: 0xc1770ae40; com.apple.controlcenter:7307F095-23A5-476D-A567-6F32F2342CA3> complete!
default	17:18:13.790330-0500	Nexy	<FBSWorkspaceScenesClient:0xc1770af80 <private>> was invalidated
default	17:18:13.790355-0500	Nexy	FBSWorkspace unregistering source: <private>
error	17:18:13.790406-0500	Nexy	Error creating <FBSScene: 0xc1770ae40; com.apple.controlcenter:7307F095-23A5-476D-A567-6F32F2342CA3>: <NSError: 0xc17013ed0; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	17:18:13.790432-0500	Nexy	No scene exists for identity: com.apple.controlcenter:7307F095-23A5-476D-A567-6F32F2342CA3
default	17:18:13.790482-0500	Nexy	Requesting scene <FBSScene: 0xc1770b020; com.apple.controlcenter:7307F095-23A5-476D-A567-6F32F2342CA3-Aux[11]-NSStatusItemView> from com.apple.controlcenter.statusitems
error	17:18:13.790585-0500	Nexy	Error creating <FBSScene: 0xc1770b020; com.apple.controlcenter:7307F095-23A5-476D-A567-6F32F2342CA3-Aux[11]-NSStatusItemView>: <NSError: 0xc17013c60; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
default	17:18:13.790623-0500	Nexy	Request for <FBSScene: 0xc1770b020; com.apple.controlcenter:7307F095-23A5-476D-A567-6F32F2342CA3-Aux[11]-NSStatusItemView> complete!
error	17:18:13.790759-0500	Nexy	scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	17:18:13.790774-0500	Nexy	[com.apple.controlcenter:7307F095-23A5-476D-A567-6F32F2342CA3] No matching scene to invalidate for this identity.
error	17:18:13.790796-0500	Nexy	auxiliary scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	17:18:13.790821-0500	Nexy	Unhandled disconnected scene <private>
error	17:18:13.790879-0500	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
default	17:18:14.792006-0500	Nexy	FBSWorkspace registering source: <private>
default	17:18:14.792049-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	17:18:14.792151-0500	Nexy	<FBSWorkspaceScenesClient:0xc1770b020 <private>> attempting immediate handshake from activate
default	17:18:14.792187-0500	Nexy	<FBSWorkspaceScenesClient:0xc1770b020 <private>> sent handshake
default	17:18:14.792535-0500	Nexy	Requesting scene <FBSScene: 0xc1770ae40; com.apple.controlcenter:63074A41-4325-4437-892D-8E301E6C31C9> from com.apple.controlcenter.statusitems
default	17:18:14.792833-0500	Nexy	Request for <FBSScene: 0xc1770ae40; com.apple.controlcenter:63074A41-4325-4437-892D-8E301E6C31C9> complete!
default	17:18:14.793328-0500	Nexy	<FBSWorkspaceScenesClient:0xc1770b020 <private>> was invalidated
default	17:18:14.793370-0500	Nexy	FBSWorkspace unregistering source: <private>
error	17:18:14.793487-0500	Nexy	Error creating <FBSScene: 0xc1770ae40; com.apple.controlcenter:63074A41-4325-4437-892D-8E301E6C31C9>: <NSError: 0xc17013930; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	17:18:14.793515-0500	Nexy	No scene exists for identity: com.apple.controlcenter:63074A41-4325-4437-892D-8E301E6C31C9
default	17:18:14.793561-0500	Nexy	Requesting scene <FBSScene: 0xc1770af80; com.apple.controlcenter:63074A41-4325-4437-892D-8E301E6C31C9-Aux[12]-NSStatusItemView> from com.apple.controlcenter.statusitems
error	17:18:14.793723-0500	Nexy	Error creating <FBSScene: 0xc1770af80; com.apple.controlcenter:63074A41-4325-4437-892D-8E301E6C31C9-Aux[12]-NSStatusItemView>: <NSError: 0xc17013600; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
default	17:18:14.793777-0500	Nexy	Request for <FBSScene: 0xc1770af80; com.apple.controlcenter:63074A41-4325-4437-892D-8E301E6C31C9-Aux[12]-NSStatusItemView> complete!
error	17:18:14.794001-0500	Nexy	scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	17:18:14.794024-0500	Nexy	[com.apple.controlcenter:63074A41-4325-4437-892D-8E301E6C31C9] No matching scene to invalidate for this identity.
error	17:18:14.794058-0500	Nexy	auxiliary scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	17:18:14.794095-0500	Nexy	Unhandled disconnected scene <private>
error	17:18:14.794173-0500	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
default	17:18:15.795556-0500	Nexy	FBSWorkspace registering source: <private>
default	17:18:15.795603-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	17:18:15.795703-0500	Nexy	<FBSWorkspaceScenesClient:0xc1770af80 <private>> attempting immediate handshake from activate
default	17:18:15.795736-0500	Nexy	<FBSWorkspaceScenesClient:0xc1770af80 <private>> sent handshake
default	17:18:15.796046-0500	Nexy	Requesting scene <FBSScene: 0xc1770ae40; com.apple.controlcenter:CCA9643F-9308-418F-8658-E8587AA3D7C5> from com.apple.controlcenter.statusitems
default	17:18:15.796308-0500	Nexy	Request for <FBSScene: 0xc1770ae40; com.apple.controlcenter:CCA9643F-9308-418F-8658-E8587AA3D7C5> complete!
default	17:18:15.796768-0500	Nexy	<FBSWorkspaceScenesClient:0xc1770af80 <private>> was invalidated
default	17:18:15.796802-0500	Nexy	FBSWorkspace unregistering source: <private>
error	17:18:15.796866-0500	Nexy	Error creating <FBSScene: 0xc1770ae40; com.apple.controlcenter:CCA9643F-9308-418F-8658-E8587AA3D7C5>: <NSError: 0xc17013c60; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	17:18:15.796869-0500	Nexy	Error creating <FBSScene: 0xc1770b340; com.apple.controlcenter:CCA9643F-9308-418F-8658-E8587AA3D7C5-Aux[13]-NSStatusItemView>: <NSError: 0xc17013930; domain: FBSWorkspaceErrorDomain; code: 1 ("InvalidScene"); "scene <FBSScene: 0xc1770b340; com.apple.controlcenter:CCA9643F-9308-418F-8658-E8587AA3D7C5-Aux[13]-NSStatusItemView> was invalidated before activation com.apple.controlcenter.statusitems">
error	17:18:15.796885-0500	Nexy	No scene exists for identity: com.apple.controlcenter:CCA9643F-9308-418F-8658-E8587AA3D7C5
error	17:18:15.796889-0500	Nexy	No scene exists for identity: com.apple.controlcenter:CCA9643F-9308-418F-8658-E8587AA3D7C5-Aux[13]-NSStatusItemView
error	17:18:15.797051-0500	Nexy	scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	17:18:15.797066-0500	Nexy	[com.apple.controlcenter:CCA9643F-9308-418F-8658-E8587AA3D7C5] No matching scene to invalidate for this identity.
error	17:18:15.797091-0500	Nexy	auxiliary scene activation failed: Error Domain=FBSWorkspaceErrorDomain Code=1 UserInfo={BSErrorCodeDescription=InvalidScene, NSLocalizedFailureReason=<private>}
error	17:18:15.797118-0500	Nexy	Unhandled disconnected scene <private>
error	17:18:15.797179-0500	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
default	17:18:16.798141-0500	Nexy	FBSWorkspace registering source: <private>
default	17:18:16.798180-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	17:18:16.798274-0500	Nexy	<FBSWorkspaceScenesClient:0xc1770b340 <private>> attempting immediate handshake from activate
default	17:18:16.798309-0500	Nexy	<FBSWorkspaceScenesClient:0xc1770b340 <private>> sent handshake
default	17:18:16.798640-0500	Nexy	Requesting scene <FBSScene: 0xc1770ae40; com.apple.controlcenter:265850DC-ED69-40FC-B90E-3F8BBA3CDE40> from com.apple.controlcenter.statusitems
default	17:18:16.798921-0500	Nexy	Request for <FBSScene: 0xc1770ae40; com.apple.controlcenter:265850DC-ED69-40FC-B90E-3F8BBA3CDE40> complete!
default	17:18:16.799309-0500	Nexy	<FBSWorkspaceScenesClient:0xc1770b340 <private>> was invalidated
default	17:18:16.799340-0500	Nexy	FBSWorkspace unregistering source: <private>
error	17:18:16.799443-0500	Nexy	Error creating <FBSScene: 0xc1770ae40; com.apple.controlcenter:265850DC-ED69-40FC-B90E-3F8BBA3CDE40>: <NSError: 0xc17013a80; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	17:18:16.799463-0500	Nexy	No scene exists for identity: com.apple.controlcenter:265850DC-ED69-40FC-B90E-3F8BBA3CDE40
default	17:18:16.799500-0500	Nexy	Requesting scene <FBSScene: 0xc1770af80; com.apple.controlcenter:265850DC-ED69-40FC-B90E-3F8BBA3CDE40-Aux[14]-NSStatusItemView> from com.apple.controlcenter.statusitems
error	17:18:16.799623-0500	Nexy	Error creating <FBSScene: 0xc1770af80; com.apple.controlcenter:265850DC-ED69-40FC-B90E-3F8BBA3CDE40-Aux[14]-NSStatusItemView>: <NSError: 0xc17013c90; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
default	17:18:16.799671-0500	Nexy	Request for <FBSScene: 0xc1770af80; com.apple.controlcenter:265850DC-ED69-40FC-B90E-3F8BBA3CDE40-Aux[14]-NSStatusItemView> complete!
error	17:18:16.799841-0500	Nexy	scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	17:18:16.799860-0500	Nexy	[com.apple.controlcenter:265850DC-ED69-40FC-B90E-3F8BBA3CDE40] No matching scene to invalidate for this identity.
error	17:18:16.799886-0500	Nexy	auxiliary scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	17:18:16.799932-0500	Nexy	Unhandled disconnected scene <private>
error	17:18:16.799998-0500	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
