default	11:24:51.991815-0500	lsd	com.nexy.assistant/Unknown Persona:5:5:1:1:Building bundle record for app
default	11:24:51.991961-0500	lsd	com.nexy.assistant/Unknown Persona:5:5:2:1:Built bundle record for app
default	11:24:51.993308-0500	lsd	com.nexy.assistant/Unknown Persona:5:4:2:1:_LSServerRegisterItemInfo result = 0
default	11:24:51.996069-0500	dmd	Received xpc stream event (distributed notification matching) with name: com.apple.LaunchServices.applicationRegistered user info: {
    CFBundleDisplayName = Nexy;
    bundleIDs =     (
        "com.nexy.assistant"
    );
    isPlaceholder = 0;
}
default	11:24:52.999636-0500	runningboardd	Launch request for app<application.com.nexy.assistant.20318103.20318109(501)>[0] is using uid 501 (divined from auid 501 euid 501)
default	11:24:52.999708-0500	runningboardd	Acquiring assertion targeting app<application.com.nexy.assistant.20318103.20318109(501)> from originator [osservice<com.apple.coreservices.uiagent(501)>:46006] with description <RBSAssertionDescriptor| "LS launch com.nexy.assistant" ID:398-46006-1316593 target:app<application.com.nexy.assistant.20318103.20318109(501)> attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"LaunchRoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	11:24:52.999778-0500	runningboardd	Assertion 398-46006-1316593 (target:app<application.com.nexy.assistant.20318103.20318109(501)>) will be created as active
default	11:24:52.003709-0500	runningboardd	Checking PreventLaunch: global:0 exPath:/Applications/Nexy.app/Contents/MacOS/Nexy predicates:(null) allow:(null)
default	11:24:52.003737-0500	runningboardd	Creating and launching job for: app<application.com.nexy.assistant.20318103.20318109(501)>
default	11:24:52.003751-0500	runningboardd	_mutateContextIfNeeded called for com.nexy.assistant
default	11:24:52.003807-0500	runningboardd	app<application.com.nexy.assistant.20318103.20318109(501)>: -[RBPersonaManager personaForIdentity:context:personaUID:personaUniqueString:] required 0.000000 ms (wallclock); resolved to {4294967295, (null)}
default	11:24:52.036228-0500	runningboardd	[app<application.com.nexy.assistant.20318103.20318109(501)>:5436] is not RunningBoard jetsam managed.
default	11:24:52.036245-0500	runningboardd	[app<application.com.nexy.assistant.20318103.20318109(501)>:5436] This process will not be managed.
default	11:24:52.036256-0500	runningboardd	Now tracking process: [app<application.com.nexy.assistant.20318103.20318109(501)>:5436]
default	11:24:52.036415-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.20318103.20318109(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	11:24:52.037590-0500	gamepolicyd	Hit the server for a process handle 24a0cc00000153c that resolved to: [app<application.com.nexy.assistant.20318103.20318109(501)>:5436]
default	11:24:52.037626-0500	gamepolicyd	Received state update for 5436 (app<application.com.nexy.assistant.20318103.20318109(501)>, running-active-NotVisible
default	11:24:52.044845-0500	runningboardd	Using default underlying assertion for app: [app<application.com.nexy.assistant.20318103.20318109(501)>:5436]
default	11:24:52.044925-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.20318103.20318109(501)>:5436] from originator [app<application.com.nexy.assistant.20318103.20318109(501)>:5436] with description <RBSAssertionDescriptor| "RB Underlying Assertion" ID:398-398-1316594 target:5436 attributes:[
	<RBSDomainAttribute| domain:"com.apple.underlying" name:"defaultUnderlyingAppAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	11:24:52.045054-0500	runningboardd	Assertion 398-398-1316594 (target:[app<application.com.nexy.assistant.20318103.20318109(501)>:5436]) will be created as active
default	11:24:52.045253-0500	runningboardd	[app<application.com.nexy.assistant.20318103.20318109(501)>:5436] Ignoring jetsam update because this process is not memory-managed
default	11:24:52.045268-0500	runningboardd	[app<application.com.nexy.assistant.20318103.20318109(501)>:5436] Ignoring suspend because this process is not lifecycle managed
default	11:24:52.045284-0500	runningboardd	[app<application.com.nexy.assistant.20318103.20318109(501)>:5436] Set darwin role to: UserInteractive
default	11:24:52.045392-0500	runningboardd	[app<application.com.nexy.assistant.20318103.20318109(501)>:5436] Ignoring GPU update because this process is not GPU managed
default	11:24:52.045492-0500	runningboardd	[app<application.com.nexy.assistant.20318103.20318109(501)>:5436] Ignoring memory limit update because this process is not memory-managed
default	11:24:52.045437-0500	runningboardd	[app<application.com.nexy.assistant.20318103.20318109(501)>:5436] reported to RB as running
default	11:24:52.046925-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.20318103.20318109(501)>:5436] from originator [osservice<com.apple.coreservices.launchservicesd>:363] with description <RBSAssertionDescriptor| "uielement:5436" ID:398-363-1316595 target:5436 attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"RoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	11:24:52.046969-0500	CoreServicesUIAgent	LAUNCH: 0x0-0x13ff3fe com.nexy.assistant starting stopped process.
default	11:24:52.047130-0500	runningboardd	Assertion 398-363-1316595 (target:[app<application.com.nexy.assistant.20318103.20318109(501)>:5436]) will be created as active
default	11:24:52.048136-0500	loginwindow	-[Application updateInformation] | Got App URL: file:///Applications/Nexy.app/
default	11:24:52.048316-0500	loginwindow	-[ApplicationManager checkInAppContext:eventData:] | ApplicationManager: Checked in app : Nexy
default	11:24:52.050514-0500	runningboardd	[app<application.com.nexy.assistant.20318103.20318109(501)>:5436] Ignoring jetsam update because this process is not memory-managed
default	11:24:52.050555-0500	runningboardd	[app<application.com.nexy.assistant.20318103.20318109(501)>:5436] Ignoring suspend because this process is not lifecycle managed
default	11:24:52.050601-0500	runningboardd	[app<application.com.nexy.assistant.20318103.20318109(501)>:5436] Ignoring GPU update because this process is not GPU managed
default	11:24:52.050656-0500	runningboardd	[app<application.com.nexy.assistant.20318103.20318109(501)>:5436] Ignoring memory limit update because this process is not memory-managed
default	11:24:52.050749-0500	runningboardd	Successfully acquired underlying assertion for [app<application.com.nexy.assistant.20318103.20318109(501)>:5436]
default	11:24:52.053724-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.20318103.20318109(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	11:24:52.054017-0500	runningboardd	Invalidating assertion 398-46006-1316593 (target:app<application.com.nexy.assistant.20318103.20318109(501)>) from originator [osservice<com.apple.coreservices.uiagent(501)>:46006]
default	11:24:52.054135-0500	gamepolicyd	Received state update for 5436 (app<application.com.nexy.assistant.20318103.20318109(501)>, running-active-NotVisible
default	11:24:52.054059-0500	runningboardd	[app<application.com.nexy.assistant.20318103.20318109(501)>:5436] Ignoring jetsam update because this process is not memory-managed
default	11:24:52.054183-0500	runningboardd	[app<application.com.nexy.assistant.20318103.20318109(501)>:5436] Ignoring suspend because this process is not lifecycle managed
default	11:24:52.054207-0500	runningboardd	[app<application.com.nexy.assistant.20318103.20318109(501)>:5436] Ignoring GPU update because this process is not GPU managed
default	11:24:52.054322-0500	runningboardd	[app<application.com.nexy.assistant.20318103.20318109(501)>:5436] Ignoring memory limit update because this process is not memory-managed
default	11:24:52.058520-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.20318103.20318109(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	11:24:52.068304-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.20318103.20318109(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	11:24:52.160692-0500	gamepolicyd	Received state update for 5436 (app<application.com.nexy.assistant.20318103.20318109(501)>, running-active-NotVisible
default	11:24:52.175565-0500	syspolicyd	GK evaluateScanResult: 3, PST: (path: a2cffff67b96be6e), (team: 5NKLL2CLB9), (id: com.nexy.assistant), (bundle_id: (null)), 0, 0, 1, 0, 9, 4, 1
default	11:24:52.177109-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=511.132, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=5436, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.syspolicyd, pid=511, auid=0, euid=0, binary_path=/usr/libexec/syspolicyd}, },
default	11:24:52.183252-0500	tccd	AUTHREQ_SUBJECT: msgID=511.132, subject=com.nexy.assistant,
default	11:24:52.183943-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d116700 at /Applications/Nexy.app
default	11:24:52.568866-0500	Nexy	[0x105b49500] activating connection: mach=true listener=false peer=false name=com.apple.cfprefsd.daemon
default	11:24:52.568950-0500	Nexy	[0x105b49a70] activating connection: mach=true listener=false peer=false name=com.apple.cfprefsd.agent
error	11:24:52.709330-0500	Nexy	dlsym cannot find symbol NSMakeRect in CFBundle 0x105b39ef0 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	11:24:52.709562-0500	Nexy	dlsym cannot find symbol NSMakePoint in CFBundle 0x105b39ef0 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	11:24:52.709774-0500	Nexy	dlsym cannot find symbol NSMakeSize in CFBundle 0x105b39ef0 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	11:24:52.709980-0500	Nexy	dlsym cannot find symbol NSMakeRange in CFBundle 0x105b39ef0 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
default	11:24:52.804234-0500	Nexy	Registered notify signal com.apple.caulk.alloc.rtdump (0)
default	11:24:52.807354-0500	Nexy	System_Input_Processing_Notification_Handler.mm:456   System_Input_Processing_Notification_Handler::is_vi_available(): Voice isolation DSP is available for client with bundle id com.nexy.assistant (AVFoundation is available, application is not in client deny list, application is not FaceTime variant)
default	11:24:52.809323-0500	Nexy	[0x105b555c0] activating connection: mach=true listener=false peer=false name=com.apple.cmio.registerassistantservice.system-extensions
fault	11:24:52.813539-0500	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.20318103.20318109 AUID=501> and <type=Application identifier=application.com.nexy.assistant.20318103.20318109>
default	11:24:52.817874-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOInitializeListenersForBundleID: for <private> -> <private>
default	11:24:52.819771-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> vpio_preferenceChangedListener: new value ((null)) for key AUVoiceIOClients/com-nexy-assistant/AUVoiceIOChatFlavor, translatedBundleID com.nexy.assistant, bundleIDs {(
    "com.nexy.assistant"
)}
default	11:24:52.819941-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> vpio_preferenceChangedListener: new value ((null)) for key AUVoiceIOClients/com-nexy-assistant/AUVoiceIOIsAutoChatFlavorEnabled, translatedBundleID com.nexy.assistant, bundleIDs {(
    "com.nexy.assistant"
)}
default	11:24:52.820096-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetSupportedChatFlavorsForBundleID: <private>-><private> get supported chat flavors: <private>
default	11:24:52.820106-0500	Nexy	            HALSystem.cpp:134    Enabling HAL Voice Isolation support
default	11:24:52.820333-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetHiddenChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	11:24:52.820513-0500	Nexy	[0x71bbe0000] activating connection: mach=true listener=false peer=false name=com.apple.tccd
default	11:24:52.820668-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOHiddenChatFlavors newValue: (
    1
)
default	11:24:52.821043-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=5436.1, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=5436, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	11:24:52.827470-0500	tccd	AUTHREQ_SUBJECT: msgID=5436.1, subject=com.nexy.assistant,
default	11:24:52.828102-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa0b1a8c00 at /Applications/Nexy.app
default	11:24:52.839766-0500	Nexy	[0x71bbe0000] invalidated after the last release of the connection object
default	11:24:52.839807-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetSupportedChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	11:24:52.842271-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOSupportedChatFlavors newValue: (
)
default	11:24:52.843632-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.7067, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=5436, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	11:24:52.844368-0500	tccd	AUTHREQ_SUBJECT: msgID=401.7067, subject=com.nexy.assistant,
default	11:24:52.844887-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa0b1a8c00 at /Applications/Nexy.app
error	11:24:52.855561-0500	tccd	Request message contains a target_token to accessing_process (TCCDProcess: identifier=com.nexy.assistant, pid=5436, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy) but TCCDProcess: identifier=com.apple.audio.coreaudiod, pid=401, auid=202, euid=202, binary_path=/usr/sbin/coreaudiod is not a TCC manager for service: kTCCServiceScreenCapture.
default	11:24:52.856386-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.7069, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=5436, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	11:24:52.857070-0500	tccd	AUTHREQ_SUBJECT: msgID=401.7069, subject=com.nexy.assistant,
default	11:24:52.857558-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa0b1a8c00 at /Applications/Nexy.app
default	11:24:52.870874-0500	Nexy	  HALPlugInManagement.cpp:440    HALPlugInManagement::RegisterPlugIns: skipping in-process plug-ins
error	11:24:52.871054-0500	Nexy	AddInstanceForFactory: No factory registered for id <CFUUID 0x71ac08500> F8BB1C28-BAE8-11D6-9C31-00039315CD46
default	11:24:52.897716-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	11:24:52.897850-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	11:24:52.902650-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetPreferredChatFlavorForBundleID: <private>-><private> get value: 0
default	11:24:55.075495-0500	kernel	SK[7]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid F4943BE8-5F08-477F-AC60-445ABA4D2B29 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.64314,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0xeb6cf86f tp_proto=0x06"
default	11:24:55.075577-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:64314<-><IPv4-redacted>:53] interface: utun6 (skipped: 6743)
so_gencnt: 4930311 t_state: SYN_SENT process: Nexy:5436 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 1 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xb97bce1c
default	11:24:55.076201-0500	kernel	tcp connected: [<IPv4-redacted>:64314<-><IPv4-redacted>:53] interface: utun6 (skipped: 6743)
so_gencnt: 4930311 t_state: ESTABLISHED process: Nexy:5436 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 1 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xb97bce1c
default	11:24:55.076473-0500	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:64314<-><IPv4-redacted>:53] interface: utun6 (skipped: 6743)
so_gencnt: 4930311 t_state: FIN_WAIT_1 process: Nexy:5436 Duration: 0.001 sec Conn_Time: 0.001 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 1.000 ms rttvar: 0.500 ms base rtt: 1 ms so_error: 0 svc/tc: 0 flow: 0xb97bce1c
default	11:24:55.076483-0500	kernel	tcp_connection_summary [<IPv4-redacted>:64314<-><IPv4-redacted>:53] interface: utun6 (skipped: 6743)
so_gencnt: 4930311 t_state: FIN_WAIT_1 process: Nexy:5436 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	11:24:55.104495-0500	Nexy	[0x71bbe0000] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioComponentRegistrar
default	11:24:55.119560-0500	Nexy	                AUHAL.cpp:420   AUHAL: (0x71cd41540) Selecting device 85 from constructor
default	11:24:55.119570-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0x71cd41540)
default	11:24:55.119575-0500	Nexy	                AUHAL.cpp:676   SelectDevice: (0x71cd41540) not already running
default	11:24:55.119580-0500	Nexy	                AUHAL.cpp:752   SelectDevice: (0x71cd41540) nothing to teardown
default	11:24:55.119586-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0x71cd41540) connecting device 85
default	11:24:55.119685-0500	Nexy	                AUHAL.cpp:3413  IsDeviceUsable: (0x71cd41540) Device ID: 85 (Input:No | Output:Yes): true
default	11:24:55.120106-0500	Nexy	                AUHAL.cpp:769   SelectDevice: (0x71cd41540) created ioproc 0xa for device 85
default	11:24:55.120210-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x71cd41540) adding 7 device listeners to device 85
default	11:24:55.120383-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x71cd41540) adding 0 device delegate listeners to device 85
default	11:24:55.120392-0500	Nexy	                AUHAL.cpp:1581  UpdateStreamFormats: -> (0x71cd41540)
default	11:24:55.120459-0500	Nexy	                AUHAL.cpp:1677  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  48000 Hz, Float32, interleaved
default	11:24:55.120465-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 1 output streams; not all mono
default	11:24:55.120476-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	11:24:55.120486-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 0 input streams; not all mono
default	11:24:55.120493-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	11:24:55.120580-0500	Nexy	                AUHAL.cpp:1771  UpdateStreamFormats: AUHAL(0x71cd41540) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	11:24:55.120588-0500	Nexy	                AUHAL.cpp:1777  UpdateStreamFormats: AUHAL(0x71cd41540) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	11:24:55.120592-0500	Nexy	                AUHAL.cpp:1787  UpdateStreamFormats: <-
default	11:24:55.120595-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x71cd41540) removing 0 device listeners from device 0
default	11:24:55.120603-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x71cd41540) removing 0 device delegate listeners from device 0
default	11:24:55.120605-0500	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0x71cd41540)
default	11:24:55.120621-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Output stream enables: Stream 0 is DISABLED
default	11:24:55.120773-0500	Nexy	                AUHAL.cpp:2298  SetProperty: (0x71cd41540) caller requesting device change from 85 to 91
default	11:24:55.120784-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0x71cd41540)
default	11:24:55.120791-0500	Nexy	                AUHAL.cpp:676   SelectDevice: (0x71cd41540) not already running
default	11:24:55.120795-0500	Nexy	                AUHAL.cpp:682   SelectDevice: (0x71cd41540) disconnecting device 85
default	11:24:55.120800-0500	Nexy	                AUHAL.cpp:746   SelectDevice: (0x71cd41540) destroying ioproc 0xa for device 85
default	11:24:55.121407-0500	Nexy	  AVAudioSession_MacOS.mm:1021  initForMacOS
default	11:24:55.122457-0500	Nexy	[0x71bbe0280] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioSession
default	11:24:55.123858-0500	audiomxd	  ServerSessionManager.mm:315   { "action":"create_session", "session":{"ID":"0x1ef186","name":"Nexy(5436)"}, "details":{"PID":5436,"session_type":"Primary"} }
default	11:24:55.123949-0500	audiomxd	AudioApplicationInfoImpl.mm:250   Setting initial isRecording state: 0 for newly-created AudioApp
	app: {"name":"[implicit] Nexy","pid":5436}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1ef186, sessionType: 'prim', isRecording: false }, 
]
default	11:24:55.124654-0500	audiomxd	  ServerSessionManager.mm:1317  Start process monitoring, pid = 5436, name = Nexy
default	11:24:55.124901-0500	Nexy	    SessionCore_Create.mm:99    Created session 0x71aaf2680 with ID: 0x1ef186
default	11:24:55.126708-0500	Nexy	[0x71bbe03c0] activating connection: mach=true listener=false peer=false name=com.apple.audioanalyticsd
default	11:24:55.127118-0500	Nexy	No persisted cache on this platform.
error	11:24:55.127836-0500	Nexy	Reporter disconnected. { function=sendMessage, reporterID=23347442221057 }
default	11:24:55.127851-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped Unknown {1C-77-54-18-C8-A3:output, 0xa}
default	11:24:55.127907-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	11:24:55.128020-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0x71cd41540) connecting device 91
default	11:24:55.128103-0500	Nexy	                AUHAL.cpp:3413  IsDeviceUsable: (0x71cd41540) Device ID: 91 (Input:Yes | Output:No): true
default	11:24:55.129432-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.7070, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=5436, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	11:24:55.130537-0500	tccd	AUTHREQ_SUBJECT: msgID=401.7070, subject=com.nexy.assistant,
default	11:24:55.131198-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa0b1a8c00 at /Applications/Nexy.app
default	11:24:55.142755-0500	tccd	AUTHREQ_PROMPTING: msgID=401.7070, service=kTCCServiceMicrophone, subject=Sub:{com.nexy.assistant}Resp:{TCCDProcess: identifier=com.nexy.assistant, pid=5436, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy},
default	11:24:56.660002-0500	Nexy	                AUHAL.cpp:769   SelectDevice: (0x71cd41540) created ioproc 0xa for device 91
default	11:24:56.659189-0500	tccd	Publishing <TCCDEvent: type=Create, service=kTCCServiceMicrophone, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 3 subscribers: {
    471 = "<TCCDEventSubscriber: token=471, state=Passed, csid=com.apple.chronod>";
    37 = "<TCCDEventSubscriber: token=37, state=Initial, csid=(null)>";
    476 = "<TCCDEventSubscriber: token=476, state=Passed, csid=com.apple.photolibraryd>";
}
default	11:24:56.660265-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x71cd41540) adding 7 device listeners to device 91
default	11:24:56.660571-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x71cd41540) adding 0 device delegate listeners to device 91
default	11:24:56.660954-0500	chronod	[appAuth:com.nexy.assistant] tcc authorization(s) changed
default	11:24:56.660586-0500	Nexy	                AUHAL.cpp:1581  UpdateStreamFormats: -> (0x71cd41540)
default	11:24:56.660600-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 0 output streams; not all mono
default	11:24:56.660621-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Output render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	11:24:56.660825-0500	Nexy	                AUHAL.cpp:1677  UpdateStreamFormats: 
  input stream 0 [0x5c]:  1 ch,  24000 Hz, Float32
default	11:24:56.660835-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 1 input streams; all mono
default	11:24:56.660842-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Input render format:  1 ch,  24000 Hz, Float32
default	11:24:56.661145-0500	Nexy	                AUHAL.cpp:1771  UpdateStreamFormats: AUHAL(0x71cd41540) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	11:24:56.661298-0500	Nexy	                AUHAL.cpp:1777  UpdateStreamFormats: AUHAL(0x71cd41540) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	11:24:56.661504-0500	Nexy	                AUHAL.cpp:1787  UpdateStreamFormats: <-
default	11:24:56.661616-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x71cd41540) removing 7 device listeners from device 85
default	11:24:56.661933-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x71cd41540) removing 0 device delegate listeners from device 85
default	11:24:56.661946-0500	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0x71cd41540)
default	11:24:56.662998-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	11:24:56.665376-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.7071, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=5436, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	11:24:56.666932-0500	tccd	AUTHREQ_SUBJECT: msgID=401.7071, subject=com.nexy.assistant,
default	11:24:56.668370-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa0b1a8c00 at /Applications/Nexy.app
default	11:24:56.685962-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	11:24:56.687288-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.7072, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=5436, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	11:24:56.688328-0500	tccd	AUTHREQ_SUBJECT: msgID=401.7072, subject=com.nexy.assistant,
default	11:24:56.688941-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa0b1a8c00 at /Applications/Nexy.app
default	11:24:56.702200-0500	Nexy	Registered notify signal com.apple.caulk.alloc.audiodump (0)
default	11:24:56.703763-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.7073, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=5436, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	11:24:56.704674-0500	tccd	AUTHREQ_SUBJECT: msgID=401.7073, subject=com.nexy.assistant,
default	11:24:56.705235-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa0b1a8c00 at /Applications/Nexy.app
default	11:24:56.717947-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetPreferredChatFlavorForBundleID: <private>-><private> get value: 0
default	11:24:56.718281-0500	coreaudiod	>>> NEGOTIATE [com.nexy.assistant]
default	11:24:56.718410-0500	coreaudiod	<<< NEGOTIATE [com.nexy.assistant]
default	11:24:56.718547-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetSupportedChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	11:24:56.719748-0500	coreaudiod	>>> ADAPT [com.nexy.assistant]
default	11:24:56.720864-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOSupportedChatFlavors newValue: (
    0,
    2
)
default	11:24:56.721347-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xbf6fa0600] Created node ADM::com.nexy.assistant_49208.49141.0_airpods noise suppression studio::in-0 with nodeID 0 - reporting period = 10.000000, sample rate = 24000.000000
default	11:24:56.721424-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xbf6fa0600] Created node ADM::com.nexy.assistant_49208.49141.0_airpods noise suppression studio::out-0 with nodeID 1 - reporting period = 10.000000, sample rate = 24000.000000
default	11:24:56.797260-0500	coreaudiod	<<< ADAPT [com.nexy.assistant]
default	11:24:56.798686-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Input {1C-77-54-18-C8-A3:input, 0xa}
default	11:24:56.798650-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:49208 called from <private>
default	11:24:56.798754-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	11:24:56.799314-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(49207)
default	11:24:56.799345-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:49207 called from <private>
default	11:24:56.803009-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.20318103.20318109(501)>:5436] from originator [osservice<com.apple.powerd>:334] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:398-334-1316623 target:5436 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	11:24:56.803086-0500	runningboardd	Assertion 398-334-1316623 (target:[app<application.com.nexy.assistant.20318103.20318109(501)>:5436]) will be created as active
default	11:24:56.799350-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:49207 called from <private>
default	11:24:56.800426-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:49208 called from <private>
default	11:24:56.800563-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(49208)
default	11:24:56.800579-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:49208 called from <private>
default	11:24:56.800585-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:49208 called from <private>
default	11:24:56.804934-0500	runningboardd	[app<application.com.nexy.assistant.20318103.20318109(501)>:5436] Ignoring jetsam update because this process is not memory-managed
default	11:24:56.805519-0500	runningboardd	[app<application.com.nexy.assistant.20318103.20318109(501)>:5436] Ignoring suspend because this process is not lifecycle managed
default	11:24:56.805598-0500	runningboardd	[app<application.com.nexy.assistant.20318103.20318109(501)>:5436] Ignoring GPU update because this process is not GPU managed
default	11:24:56.805758-0500	runningboardd	[app<application.com.nexy.assistant.20318103.20318109(501)>:5436] Ignoring memory limit update because this process is not memory-managed
fault	11:24:56.808448-0500	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.20318103.20318109 AUID=501> and <type=Application identifier=application.com.nexy.assistant.20318103.20318109>
default	11:24:56.809746-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	11:24:56.810420-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	11:24:56.818627-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(49208)
default	11:24:56.818646-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(49208)
default	11:24:56.818651-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:49208 called from <private>
default	11:24:56.818659-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(49208)
default	11:24:56.818661-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:49208 called from <private>
default	11:24:56.818669-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:49208 called from <private>
default	11:24:56.818669-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(49208)
default	11:24:56.818675-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:49208 called from <private>
default	11:24:56.818748-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:49208 called from <private>
default	11:24:56.818788-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:49208 called from <private>
default	11:24:56.818842-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:49208 called from <private>
default	11:24:56.818870-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:49208 called from <private>
fault	11:24:56.824709-0500	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.20318103.20318109 AUID=501> and <type=Application identifier=application.com.nexy.assistant.20318103.20318109>
default	11:24:56.825787-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:49208 called from <private>
default	11:24:56.825798-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:49208 called from <private>
default	11:24:56.825980-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.20318103.20318109(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	11:24:56.826339-0500	runningboardd	Invalidating assertion 398-334-1316623 (target:[app<application.com.nexy.assistant.20318103.20318109(501)>:5436]) from originator [osservice<com.apple.powerd>:334]
default	11:24:56.826596-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(49208)
default	11:24:56.826622-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:49208 called from <private>
default	11:24:56.827904-0500	gamepolicyd	Received state update for 5436 (app<application.com.nexy.assistant.20318103.20318109(501)>, running-active-NotVisible
default	11:24:56.828175-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ef186","name":"Nexy(5436)"}, "details":{"deviceUIDs":["1C-77-54-18-C8-A3:input"],"implicit_category":"Record","input_running":true,"output_running":false} }
default	11:24:56.828255-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 391, PID = 5436, Name = sid:0x1ef186, Nexy(5436), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	11:24:56.828603-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 391, PID = 5436, Name = sid:0x1ef186, Nexy(5436), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	11:24:56.828803-0500	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1ef186, Nexy(5436), 'prim'', AudioCategory changed to 'Record_WithBluetooth'
default	11:24:56.829056-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	11:24:56.828888-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	11:24:56.828916-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 391, PID = 5436, Name = sid:0x1ef186, Nexy(5436), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	11:24:56.829011-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 391, PID = 5436, Name = sid:0x1ef186, Nexy(5436), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	11:24:56.829173-0500	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 391, PID = 5436, Name = sid:0x1ef186, Nexy(5436), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> is going active
default	11:24:56.829169-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	11:24:56.829200-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1ef186, Nexy(5436), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 391 starting recording
default	11:24:56.829659-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 391, PID = 5436, Name = sid:0x1ef186, Nexy(5436), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	11:24:56.829690-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 391, PID = 5436, Name = sid:0x1ef186, Nexy(5436), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	11:24:56.829281-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	11:24:56.829889-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1ef186, Nexy(5436), 'prim'', displayID:'com.nexy.assistant'}
default	11:24:56.829794-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(49207)
default	11:24:56.829912-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:49207 called from <private>
default	11:24:56.829890-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.7074, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=5436, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	11:24:56.829920-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:49207 called from <private>
default	11:24:56.830029-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	11:24:56.830017-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [1, 0]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:input"
)}
default	11:24:56.830027-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	11:24:56.831881-0500	tccd	AUTHREQ_SUBJECT: msgID=401.7074, subject=com.nexy.assistant,
default	11:24:56.832704-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa0b1a8c00 at /Applications/Nexy.app
default	11:24:56.842773-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:49207 called from <private>
default	11:24:56.842789-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:49207 called from <private>
default	11:24:56.842855-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(49207)
default	11:24:56.845871-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	11:24:56.846127-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	11:24:56.846925-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	11:24:56.847230-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	11:24:56.848582-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:24:56.848594-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:24:56.848608-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	11:24:56.848614-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:24:56.848620-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	11:24:56.848649-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	11:24:56.850857-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	11:24:56.863472-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	11:24:56.900639-0500	coreaudiod	>>> ADAPT [com.nexy.assistant]
default	11:24:56.902256-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xbf6fa0600] Created node ADM::com.nexy.assistant_49208.49141.0_airpods noise suppression studio::in-0 with nodeID 0 - reporting period = 10.000000, sample rate = 24000.000000
default	11:24:56.902318-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xbf6fa0600] Created node ADM::com.nexy.assistant_49208.49141.0_airpods noise suppression studio::out-0 with nodeID 1 - reporting period = 10.000000, sample rate = 24000.000000
default	11:24:56.917879-0500	audioaccessoryd	AudioStateSnapshot: Route:Bluetooth App com.nexy.assistant, Score 200, Remote 0NumofApp 1
default	11:24:56.927258-0500	runningboardd	[app<application.com.nexy.assistant.20318103.20318109(501)>:5436] Ignoring jetsam update because this process is not memory-managed
default	11:24:56.927269-0500	runningboardd	[app<application.com.nexy.assistant.20318103.20318109(501)>:5436] Ignoring suspend because this process is not lifecycle managed
default	11:24:56.927279-0500	runningboardd	[app<application.com.nexy.assistant.20318103.20318109(501)>:5436] Ignoring GPU update because this process is not GPU managed
default	11:24:56.927324-0500	runningboardd	[app<application.com.nexy.assistant.20318103.20318109(501)>:5436] Ignoring memory limit update because this process is not memory-managed
default	11:24:56.931674-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.20318103.20318109(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	11:24:56.932303-0500	gamepolicyd	Received state update for 5436 (app<application.com.nexy.assistant.20318103.20318109(501)>, running-active-NotVisible
default	11:24:56.937047-0500	coreaudiod	<<< ADAPT [com.nexy.assistant]
default	11:24:56.938174-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.20318103.20318109(501)>:5436] from originator [osservice<com.apple.powerd>:334] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:398-334-1316626 target:5436 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	11:24:56.938244-0500	runningboardd	Assertion 398-334-1316626 (target:[app<application.com.nexy.assistant.20318103.20318109(501)>:5436]) will be created as active
default	11:24:56.939363-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:49208 called from <private>
default	11:24:56.939385-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:49208 called from <private>
default	11:24:56.939728-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	11:24:56.938697-0500	runningboardd	[app<application.com.nexy.assistant.20318103.20318109(501)>:5436] Ignoring jetsam update because this process is not memory-managed
default	11:24:56.939002-0500	runningboardd	[app<application.com.nexy.assistant.20318103.20318109(501)>:5436] Ignoring suspend because this process is not lifecycle managed
default	11:24:56.942121-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:49208 called from <private>
default	11:24:56.943180-0500	runningboardd	[app<application.com.nexy.assistant.20318103.20318109(501)>:5436] Ignoring GPU update because this process is not GPU managed
default	11:24:56.942320-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(49208)
default	11:24:56.942337-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:49208 called from <private>
default	11:24:56.942343-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:49208 called from <private>
default	11:24:56.943376-0500	runningboardd	[app<application.com.nexy.assistant.20318103.20318109(501)>:5436] Ignoring memory limit update because this process is not memory-managed
default	11:24:56.944327-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	11:24:56.944456-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	11:24:56.944824-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(49208)
default	11:24:56.945203-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:49208 called from <private>
default	11:24:56.950020-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.20318103.20318109(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	11:24:56.950191-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	11:24:56.950184-0500	runningboardd	Invalidating assertion 398-334-1316626 (target:[app<application.com.nexy.assistant.20318103.20318109(501)>:5436]) from originator [osservice<com.apple.powerd>:334]
default	11:24:56.950258-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	11:24:56.950290-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	11:24:56.950722-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:24:56.950831-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:24:56.965156-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:49208 called from <private>
default	11:24:56.966813-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.20318103.20318109(501)>:5436] from originator [osservice<com.apple.powerd>:334] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:398-334-1316629 target:5436 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	11:24:56.966918-0500	runningboardd	Assertion 398-334-1316629 (target:[app<application.com.nexy.assistant.20318103.20318109(501)>:5436]) will be created as active
default	11:24:56.973659-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:24:56.973669-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:24:56.973680-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	11:24:56.973685-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:24:56.973694-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	11:24:56.973725-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	11:24:56.973766-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:24:56.973790-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:24:56.973808-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	11:24:56.973848-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:24:56.973896-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	11:24:56.973933-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	11:24:56.974113-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:24:56.974152-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	11:24:56.974159-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:24:56.974204-0500	ControlCenter	Navigating to new application [com.nexy.assistant]
default	11:24:56.974220-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	11:24:56.974277-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:24:56.974286-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	11:24:56.974302-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	11:24:57.029747-0500	runningboardd	Assertion did invalidate due to timeout: 398-398-1316594 (target:[app<application.com.nexy.assistant.20318103.20318109(501)>:5436])
default	11:24:57.035036-0500	gamepolicyd	Received state update for 5436 (app<application.com.nexy.assistant.20318103.20318109(501)>, running-active-NotVisible
default	11:24:57.052130-0500	runningboardd	[app<application.com.nexy.assistant.20318103.20318109(501)>:5436] Ignoring jetsam update because this process is not memory-managed
default	11:24:57.052150-0500	runningboardd	[app<application.com.nexy.assistant.20318103.20318109(501)>:5436] Ignoring suspend because this process is not lifecycle managed
default	11:24:57.052160-0500	runningboardd	[app<application.com.nexy.assistant.20318103.20318109(501)>:5436] Ignoring GPU update because this process is not GPU managed
default	11:24:57.052180-0500	runningboardd	[app<application.com.nexy.assistant.20318103.20318109(501)>:5436] Ignoring memory limit update because this process is not memory-managed
default	11:24:57.056329-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.20318103.20318109(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	11:24:57.059614-0500	gamepolicyd	Received state update for 5436 (app<application.com.nexy.assistant.20318103.20318109(501)>, running-active-NotVisible
default	11:24:57.994029-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xa}
default	11:24:57.994235-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ef186","name":"Nexy(5436)"}, "details":{"deviceUIDs":[],"implicit_category":"","input_running":false,"output_running":false} }
default	11:24:57.994323-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 391, PID = 5436, Name = sid:0x1ef186, Nexy(5436), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	11:24:57.994369-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 391, PID = 5436, Name = sid:0x1ef186, Nexy(5436), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	11:24:57.994394-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1ef186, Nexy(5436), 'prim'', displayID:'com.nexy.assistant'}
default	11:24:57.994441-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1ef186, Nexy(5436), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 391 stopping recording
default	11:24:57.994443-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	11:24:57.994463-0500	audiomxd	-MXCoreSession- -[MXCoreSession endInterruption:]: Session <ID: 391, PID = 5436, Name = sid:0x1ef186, Nexy(5436), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> is going inactive
default	11:24:57.994510-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 391, PID = 5436, Name = sid:0x1ef186, Nexy(5436), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	11:24:57.994647-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 200 flag 0x1 < Hijack > app com.nexy.assistant CID 0xD310001 category Not set
default	11:24:57.994554-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 391, PID = 5436, Name = sid:0x1ef186, Nexy(5436), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	11:24:57.994708-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 0]. BT device UIDS: {(
)}
default	11:24:57.994715-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	11:24:57.998296-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	11:24:57.997874-0500	runningboardd	Invalidating assertion 398-334-1316629 (target:[app<application.com.nexy.assistant.20318103.20318109(501)>:5436]) from originator [osservice<com.apple.powerd>:334]
default	11:24:57.998091-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	11:24:57.998358-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	11:24:57.998409-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	11:24:57.998450-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	11:24:57.998209-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	11:24:57.998572-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	11:24:57.998598-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	11:24:57.998771-0500	audioaccessoryd	AudioStateChanged: Removed audio session app com.nexy.assistant 201 count 0
default	11:24:58.000212-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	11:24:58.002217-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:24:58.002228-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:24:58.002238-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	11:24:58.002243-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:24:58.002250-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	11:24:58.002258-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	11:24:58.002356-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	11:24:58.095937-0500	Nexy	                AUHAL.cpp:473   ~AUHAL: (0x71cd41540) Selecting device 0 from destructor
default	11:24:58.095952-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0x71cd41540)
default	11:24:58.095959-0500	Nexy	                AUHAL.cpp:676   SelectDevice: (0x71cd41540) not already running
default	11:24:58.095966-0500	Nexy	                AUHAL.cpp:682   SelectDevice: (0x71cd41540) disconnecting device 91
default	11:24:58.095973-0500	Nexy	                AUHAL.cpp:746   SelectDevice: (0x71cd41540) destroying ioproc 0xa for device 91
default	11:24:58.095997-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xa}
default	11:24:58.096026-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	11:24:58.096190-0500	Nexy	                AUHAL.cpp:848   SelectDevice: (0x71cd41540) nothing to setup
default	11:24:58.096208-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x71cd41540) adding 0 device listeners to device 0
default	11:24:58.096216-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x71cd41540) adding 0 device delegate listeners to device 0
default	11:24:58.096225-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x71cd41540) removing 7 device listeners from device 91
default	11:24:58.096510-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x71cd41540) removing 0 device delegate listeners from device 91
default	11:24:58.096535-0500	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0x71cd41540)
default	11:24:58.101706-0500	runningboardd	[app<application.com.nexy.assistant.20318103.20318109(501)>:5436] Ignoring jetsam update because this process is not memory-managed
default	11:24:58.101722-0500	runningboardd	[app<application.com.nexy.assistant.20318103.20318109(501)>:5436] Ignoring suspend because this process is not lifecycle managed
default	11:24:58.101737-0500	runningboardd	[app<application.com.nexy.assistant.20318103.20318109(501)>:5436] Ignoring GPU update because this process is not GPU managed
default	11:24:58.101758-0500	runningboardd	[app<application.com.nexy.assistant.20318103.20318109(501)>:5436] Ignoring memory limit update because this process is not memory-managed
default	11:24:58.106483-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.20318103.20318109(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	11:24:58.106944-0500	gamepolicyd	Received state update for 5436 (app<application.com.nexy.assistant.20318103.20318109(501)>, running-active-NotVisible
default	11:24:58.353302-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=5441.1, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=5436, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.osascript, pid=5441, auid=501, euid=501, binary_path=/usr/bin/osascript}, },
default	11:24:58.354940-0500	tccd	AUTHREQ_SUBJECT: msgID=5441.1, subject=com.nexy.assistant,
default	11:24:58.355683-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d116700 at /Applications/Nexy.app
default	11:24:58.371944-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=393.13396, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=5436, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.osascript, pid=5441, auid=501, euid=501, binary_path=/usr/bin/osascript}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=393, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	11:24:58.373145-0500	tccd	AUTHREQ_SUBJECT: msgID=393.13396, subject=com.nexy.assistant,
default	11:24:58.373872-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d116700 at /Applications/Nexy.app
default	11:24:58.399610-0500	launchservicesd	CHECKIN:0x0-0x13ff3fe 5441 com.nexy.assistant
default	11:24:58.401983-0500	runningboardd	Invalidating assertion 398-363-1316595 (target:[app<application.com.nexy.assistant.20318103.20318109(501)>:5436]) from originator [osservice<com.apple.coreservices.launchservicesd>:363]
default	11:24:58.409358-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d116700 at /Applications/Nexy.app
default	11:24:58.411407-0500	runningboardd	[app<application.com.nexy.assistant.20318103.20318109(501)>:5436] Ignoring jetsam update because this process is not memory-managed
default	11:24:58.411434-0500	runningboardd	[app<application.com.nexy.assistant.20318103.20318109(501)>:5436] Ignoring suspend because this process is not lifecycle managed
default	11:24:58.411541-0500	runningboardd	[app<application.com.nexy.assistant.20318103.20318109(501)>:5436] Set darwin role to: None
default	11:24:58.411559-0500	runningboardd	[app<application.com.nexy.assistant.20318103.20318109(501)>:5436] Ignoring GPU update because this process is not GPU managed
default	11:24:58.411576-0500	runningboardd	[app<application.com.nexy.assistant.20318103.20318109(501)>:5436] Ignoring memory limit update because this process is not memory-managed
default	11:24:58.411503-0500	loginwindow	-[Application updateInformation] | Got App URL: file:///Applications/Nexy.app/
default	11:24:58.411653-0500	loginwindow	-[ApplicationManager checkInAppContext:eventData:] | ApplicationManager: Checked in app : Nexy
default	11:24:58.412431-0500	WindowServer	18a5fb[CreateApplication]: Process creation: 0x0-0x13ff3fe (Nexy) connectionID: 18A5FB pid: 5441 in session 0x101
default	11:24:58.415402-0500	loginwindow	-[Application updateInformation] | Got App URL: file:///Applications/Nexy.app/
default	11:24:58.419294-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.20318103.20318109(501)>: running-suspended (role: None) (endowments: (null))
default	11:24:58.419903-0500	gamepolicyd	Received state update for 5436 (app<application.com.nexy.assistant.20318103.20318109(501)>, running-suspended-NotVisible
default	11:24:58.574048-0500	System Events	TCCAccessRequestIndirect: TCCAccessRequestIndirect with pid 5442: target_identity: {
    kTCCCodeIdentityAuditToken = {length = 32, bytes = 0xf5010000 f5010000 14000000 f5010000 ... b7860100 742b1d00 };
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
default	11:24:58.585099-0500	tccd	target_executable_path_URL: file:///Applications/Nexy.app/Contents/MacOS/Nexy
default	11:24:58.636749-0500	WindowServer	0[outside of RPC]: Process death: 0x0-0x13ff3fe (Nexy) connectionID: 18A5FB pid: 5441 in session 0x101
default	11:24:58.636775-0500	WindowServer	<BSCompoundAssertion:0x7fb0154c0> ([FocusManager:257]-deferringPolicyEvaluationSuppression) acquire for reason:process death - 0x0-0x13ff3fe (Nexy) acq:0x8012ac0c0 count:1
default	11:24:58.637768-0500	loginwindow	-[ApplicationManager handleCASEvent:withData:] | CAS notification for appDeath for com.nexy.assistant with asn: LSASN:{hi=0x0;lo=0x13ff3fe} for bundle path: /Applications/Nexy.app with URL: file:///Applications/Nexy.app/
default	11:24:58.637798-0500	loginwindow	-[ApplicationManager(AppDeathHandler) appDeathCleanupHandler:forApp:] | Termination handler for: Nexy : 20968446
default	11:24:58.637857-0500	loginwindow	-[PersistentAppsSupport applicationQuit:] | for app:Nexy, _appTrackingState = 2
default	11:24:58.639183-0500	WindowServer	0[outside of RPC]: [FocusManager:257] update to deferring policy requested for reason: permitted list updated - 0x0-0x13ff3fe removed - but we are suppressing evaluation for reasons: {(
    "process death - 0x0-0x13ff3fe (Nexy)"
)}
default	11:24:58.639559-0500	WindowServer	0[outside of RPC]: [FocusManager:257] update to deferring policy requested for reason: permitted list updated - 0x1-0x1541 removed - but we are suppressing evaluation for reasons: {(
    "process death - 0x0-0x13ff3fe (Nexy)"
)}
default	11:24:58.801139-0500	Nexy	                AUHAL.cpp:420   AUHAL: (0x71cd42340) Selecting device 85 from constructor
default	11:24:58.801148-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0x71cd42340)
default	11:24:58.801153-0500	Nexy	                AUHAL.cpp:676   SelectDevice: (0x71cd42340) not already running
default	11:24:58.801157-0500	Nexy	                AUHAL.cpp:752   SelectDevice: (0x71cd42340) nothing to teardown
default	11:24:58.801162-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0x71cd42340) connecting device 85
default	11:24:58.801269-0500	Nexy	                AUHAL.cpp:3413  IsDeviceUsable: (0x71cd42340) Device ID: 85 (Input:No | Output:Yes): true
default	11:24:58.801389-0500	Nexy	                AUHAL.cpp:769   SelectDevice: (0x71cd42340) created ioproc 0xb for device 85
default	11:24:58.801522-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x71cd42340) adding 7 device listeners to device 85
default	11:24:58.801693-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x71cd42340) adding 0 device delegate listeners to device 85
default	11:24:58.801704-0500	Nexy	                AUHAL.cpp:1581  UpdateStreamFormats: -> (0x71cd42340)
default	11:24:58.801779-0500	Nexy	                AUHAL.cpp:1677  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  24000 Hz, Float32, interleaved
default	11:24:58.801786-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 1 output streams; not all mono
default	11:24:58.801791-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Output render format:  2 ch,  24000 Hz, Float32, interleaved
default	11:24:58.801798-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 0 input streams; not all mono
default	11:24:58.801805-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	11:24:58.801901-0500	Nexy	                AUHAL.cpp:1771  UpdateStreamFormats: AUHAL(0x71cd42340) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	11:24:58.801919-0500	Nexy	                AUHAL.cpp:1777  UpdateStreamFormats: AUHAL(0x71cd42340) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	11:24:58.801924-0500	Nexy	                AUHAL.cpp:1787  UpdateStreamFormats: <-
default	11:24:58.801928-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x71cd42340) removing 0 device listeners from device 0
default	11:24:58.801932-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x71cd42340) removing 0 device delegate listeners from device 0
default	11:24:58.801935-0500	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0x71cd42340)
default	11:24:58.801949-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Output stream enables: Stream 0 is DISABLED
default	11:24:58.802016-0500	Nexy	                AUHAL.cpp:2298  SetProperty: (0x71cd42340) caller requesting device change from 85 to 91
default	11:24:58.802026-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0x71cd42340)
default	11:24:58.802030-0500	Nexy	                AUHAL.cpp:676   SelectDevice: (0x71cd42340) not already running
default	11:24:58.802032-0500	Nexy	                AUHAL.cpp:682   SelectDevice: (0x71cd42340) disconnecting device 85
default	11:24:58.802037-0500	Nexy	                AUHAL.cpp:746   SelectDevice: (0x71cd42340) destroying ioproc 0xb for device 85
default	11:24:58.802052-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped Unknown {1C-77-54-18-C8-A3:output, 0xb}
default	11:24:58.802077-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	11:24:58.802160-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0x71cd42340) connecting device 91
default	11:24:58.802237-0500	Nexy	                AUHAL.cpp:3413  IsDeviceUsable: (0x71cd42340) Device ID: 91 (Input:Yes | Output:No): true
default	11:24:58.803395-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.7077, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=5436, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	11:24:58.804307-0500	tccd	AUTHREQ_SUBJECT: msgID=401.7077, subject=com.nexy.assistant,
default	11:24:58.804860-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa0b1a8c00 at /Applications/Nexy.app
default	11:24:58.816076-0500	Nexy	                AUHAL.cpp:769   SelectDevice: (0x71cd42340) created ioproc 0xb for device 91
default	11:24:58.816190-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x71cd42340) adding 7 device listeners to device 91
default	11:24:58.816364-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x71cd42340) adding 0 device delegate listeners to device 91
default	11:24:58.816373-0500	Nexy	                AUHAL.cpp:1581  UpdateStreamFormats: -> (0x71cd42340)
default	11:24:58.816379-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 0 output streams; not all mono
default	11:24:58.816387-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Output render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	11:24:58.816517-0500	Nexy	                AUHAL.cpp:1677  UpdateStreamFormats: 
  input stream 0 [0x5c]:  1 ch,  24000 Hz, Float32
default	11:24:58.816524-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 1 input streams; all mono
default	11:24:58.816529-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Input render format:  1 ch,  24000 Hz, Float32
default	11:24:58.816629-0500	Nexy	                AUHAL.cpp:1771  UpdateStreamFormats: AUHAL(0x71cd42340) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	11:24:58.816642-0500	Nexy	                AUHAL.cpp:1777  UpdateStreamFormats: AUHAL(0x71cd42340) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	11:24:58.816647-0500	Nexy	                AUHAL.cpp:1787  UpdateStreamFormats: <-
default	11:24:58.816651-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x71cd42340) removing 7 device listeners from device 85
default	11:24:58.816823-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x71cd42340) removing 0 device delegate listeners from device 85
default	11:24:58.816832-0500	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0x71cd42340)
default	11:24:58.817487-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	11:24:58.818451-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.7078, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=5436, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	11:24:58.819261-0500	tccd	AUTHREQ_SUBJECT: msgID=401.7078, subject=com.nexy.assistant,
default	11:24:58.819827-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa0b1a8c00 at /Applications/Nexy.app
default	11:24:58.831001-0500	Nexy	       ACv2Workarounds.mm:51    com.nexy.assistant: fix84702776_86723525_86479548_89800354_SinglePacketDesc: false
default	11:24:58.831123-0500	Nexy	       AudioConverter.cpp:1042  Created a new in process converter -> 0x71aada520, from  1 ch,  24000 Hz, Float32 to  1 ch,  16000 Hz, Float32
default	11:24:58.831337-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	11:24:58.832317-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.7079, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=5436, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	11:24:58.833061-0500	tccd	AUTHREQ_SUBJECT: msgID=401.7079, subject=com.nexy.assistant,
default	11:24:58.833597-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa0b1a8c00 at /Applications/Nexy.app
default	11:24:58.845906-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.7080, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=5436, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	11:24:58.846687-0500	tccd	AUTHREQ_SUBJECT: msgID=401.7080, subject=com.nexy.assistant,
default	11:24:58.847245-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa0b1a8c00 at /Applications/Nexy.app
default	11:24:58.862234-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Input {1C-77-54-18-C8-A3:input, 0xb}
default	11:24:58.865425-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ef186","name":"Nexy(5436)"}, "details":{"deviceUIDs":["1C-77-54-18-C8-A3:input"],"implicit_category":"Record","input_running":true,"output_running":false} }
default	11:24:58.865524-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 391, PID = 5436, Name = sid:0x1ef186, Nexy(5436), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	11:24:58.865555-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Category/Mode changed -- The score for sid:0x1ef186, Nexy(5436), 'prim'/com.nexy.assistant was not correct. Old score = 201
default	11:24:58.865582-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 391, PID = 5436, Name = sid:0x1ef186, Nexy(5436), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	11:24:58.865731-0500	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1ef186, Nexy(5436), 'prim'', AudioCategory changed to 'Record_WithBluetooth'
default	11:24:58.865906-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 391, PID = 5436, Name = sid:0x1ef186, Nexy(5436), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	11:24:58.866018-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 391, PID = 5436, Name = sid:0x1ef186, Nexy(5436), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	11:24:58.866312-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	11:24:58.865784-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	11:24:58.866168-0500	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 391, PID = 5436, Name = sid:0x1ef186, Nexy(5436), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> is going active
default	11:24:58.866219-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1ef186, Nexy(5436), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 391 starting recording
default	11:24:58.866058-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.20318103.20318109(501)>:5436] from originator [osservice<com.apple.powerd>:334] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:398-334-1316639 target:5436 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	11:24:58.866136-0500	runningboardd	Assertion 398-334-1316639 (target:[app<application.com.nexy.assistant.20318103.20318109(501)>:5436]) will be created as active
default	11:24:58.866353-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	11:24:58.866286-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	11:24:58.866416-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 391, PID = 5436, Name = sid:0x1ef186, Nexy(5436), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	11:24:58.866473-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 391, PID = 5436, Name = sid:0x1ef186, Nexy(5436), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	11:24:58.866597-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1ef186, Nexy(5436), 'prim'', displayID:'com.nexy.assistant'}
default	11:24:58.866662-0500	runningboardd	[app<application.com.nexy.assistant.20318103.20318109(501)>:5436] Ignoring jetsam update because this process is not memory-managed
default	11:24:58.866744-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	11:24:58.866761-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [1, 0]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:input"
)}
default	11:24:58.866513-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	11:24:58.866772-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	11:24:58.866540-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	11:24:58.866738-0500	runningboardd	[app<application.com.nexy.assistant.20318103.20318109(501)>:5436] Ignoring suspend because this process is not lifecycle managed
default	11:24:58.866894-0500	runningboardd	[app<application.com.nexy.assistant.20318103.20318109(501)>:5436] Set darwin role to: Background
default	11:24:58.867005-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 200 flag 0x1 < Hijack > app com.nexy.assistant CID 0xD310001 category Not set
default	11:24:58.866964-0500	runningboardd	[app<application.com.nexy.assistant.20318103.20318109(501)>:5436] Ignoring GPU update because this process is not GPU managed
default	11:24:58.867208-0500	runningboardd	[app<application.com.nexy.assistant.20318103.20318109(501)>:5436] Ignoring memory limit update because this process is not memory-managed
default	11:24:58.868535-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	11:24:58.868561-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	11:24:58.868571-0500	audioaccessoryd	AudioStateChanged: Added audio session app com.nexy.assistant NULL -> 200 count 1
default	11:24:58.868578-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
error	11:24:58.868587-0500	audioaccessoryd	Updating local audio category 100 -> 200 app com.nexy.assistant
default	11:24:58.868453-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	11:24:58.868745-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	11:24:58.874262-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.20318103.20318109(501)>: running-active (role: Background) (endowments: (null))
default	11:24:58.874943-0500	gamepolicyd	Received state update for 5436 (app<application.com.nexy.assistant.20318103.20318109(501)>, running-active-NotVisible
default	11:24:58.876105-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	11:24:58.876182-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	11:24:58.876233-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	11:24:58.878367-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:24:58.878401-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:24:58.878454-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	11:24:58.878473-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:24:58.878513-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	11:24:58.878535-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	11:24:58.878572-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:24:58.878601-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:24:58.878626-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	11:24:58.878633-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:24:58.878659-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	11:24:58.878669-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	11:24:58.878802-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	11:24:58.879688-0500	ControlCenter	Navigating to new application [com.nexy.assistant]
default	11:24:58.879817-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:24:58.879841-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:24:58.879853-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	11:24:58.879862-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:24:58.879868-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	11:24:58.879874-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	11:24:59.921324-0500	audioaccessoryd	AudioStateSnapshot: Route:Bluetooth App com.nexy.assistant, Score 200, Remote 0NumofApp 1
default	11:25:02.917995-0500	audioaccessoryd	AudioStateSnapshot: Route:Bluetooth App com.nexy.assistant, Score 200, Remote 0NumofApp 1
error	11:25:02.986411-0500	Nexy	         HALC_ProxyIOContext.cpp:1623  HALC_ProxyIOContext::IOWorkLoop: skipping cycle due to overload
default	11:25:05.920785-0500	audioaccessoryd	AudioStateSnapshot: Route:Bluetooth App com.nexy.assistant, Score 200, Remote 0NumofApp 1
default	11:25:07.866483-0500	coreaudiod	IssueReporting.cpp:492   RTAID [ use_case=Generic report_type=RMS Generic Chain clientID=ADM node=ADM::com.nexy.assistant_49208.49141.0_airpods noise suppression studio::in-0 issue_detected_sample_time=0.000000 ] -- [ rms:[-32.720512], peaks:[-12.461781] ]
default	11:25:07.869906-0500	coreaudiod	IssueReporting.cpp:492   RTAID [ use_case=Generic report_type=RMS Generic Chain clientID=ADM node=ADM::com.nexy.assistant_49208.49141.0_airpods noise suppression studio::out-0 issue_detected_sample_time=240000.000000 ] -- [ rms:[-35.338573], peaks:[-14.087173] ]
default	11:25:08.882390-0500	audioaccessoryd	AudioStateSnapshot: Route:Bluetooth App com.nexy.assistant, Score 200, Remote 0NumofApp 1
default	11:25:11.882425-0500	audioaccessoryd	AudioStateSnapshot: Route:Bluetooth App com.nexy.assistant, Score 200, Remote 0NumofApp 1
default	11:25:11.982029-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xb}
default	11:25:11.982439-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ef186","name":"Nexy(5436)"}, "details":{"deviceUIDs":[],"implicit_category":"","input_running":false,"output_running":false} }
default	11:25:11.982567-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 391, PID = 5436, Name = sid:0x1ef186, Nexy(5436), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	11:25:11.982625-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 391, PID = 5436, Name = sid:0x1ef186, Nexy(5436), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	11:25:11.982659-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1ef186, Nexy(5436), 'prim'', displayID:'com.nexy.assistant'}
default	11:25:11.982709-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	11:25:11.982726-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1ef186, Nexy(5436), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 391 stopping recording
default	11:25:11.982753-0500	audiomxd	-MXCoreSession- -[MXCoreSession endInterruption:]: Session <ID: 391, PID = 5436, Name = sid:0x1ef186, Nexy(5436), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> is going inactive
default	11:25:11.982779-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 391, PID = 5436, Name = sid:0x1ef186, Nexy(5436), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	11:25:11.982826-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 391, PID = 5436, Name = sid:0x1ef186, Nexy(5436), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	11:25:11.983035-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 200 flag 0x1 < Hijack > app com.nexy.assistant CID 0xD310001 category Not set
default	11:25:11.983311-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 0]. BT device UIDS: {(
)}
default	11:25:11.984646-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	11:25:11.984811-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	11:25:11.984869-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	11:25:11.984945-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	11:25:11.984983-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	11:25:11.984999-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	11:25:11.985023-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	11:25:11.985093-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	11:25:11.985104-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	11:25:11.985115-0500	audioaccessoryd	AudioStateChanged: Removed audio session app com.nexy.assistant 201 count 0
default	11:25:11.988104-0500	runningboardd	Invalidating assertion 398-334-1316639 (target:[app<application.com.nexy.assistant.20318103.20318109(501)>:5436]) from originator [osservice<com.apple.powerd>:334]
default	11:25:11.990187-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	11:25:11.990433-0500	coreaudiod	Sending message. { reporterID=23347442221059, category=IO, type=error, message=["output_device_transport_list": Optional(), "other_page_faults": Optional(0), "input_device_source_list": Optional(Unknown), "overload_type": Optional(Overload), "smallest_buffer_frame_size": Optional(2147483647), "HostApplicationDisplayID": Optional(com.nexy.assistant), "careporting_timestamp": 1762187111.9894528, "start_time": Optional(10725854813961), "io_page_faults_duration": Optional(0), "cause": Optional(ClientHALIODurationExceededBudget), "output_device_uid_list": Optional(), "io_cycle_budget": Optional(22541666), "time_since_prev_overload": Optional(8996636958), "input_device_transport_list": Optional(Bluetooth), "safety_violation_sample_gap": Optional(0), "sample_rate": Optional(24000), "is_recovering": Optional(0), "io_page_faults": Optional(0), "wg_external_wakeups": Optional(5), "anchor_sample_time": Optional(98980), "safety_violation": Optional(0), "io_buffer_size": Optional(480), "issue_type": Optional(overload), "wg_system_time_mach": Optional(5896), "m<…> }
default	11:25:11.992314-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:25:11.992328-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:25:11.992342-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	11:25:11.992350-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:25:11.992357-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	11:25:11.992364-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	11:25:11.992466-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	11:25:12.061748-0500	runningboardd	[app<application.com.nexy.assistant.20318103.20318109(501)>:5436] Ignoring jetsam update because this process is not memory-managed
default	11:25:12.061778-0500	runningboardd	[app<application.com.nexy.assistant.20318103.20318109(501)>:5436] Ignoring suspend because this process is not lifecycle managed
default	11:25:12.061847-0500	runningboardd	[app<application.com.nexy.assistant.20318103.20318109(501)>:5436] Set darwin role to: None
default	11:25:12.061872-0500	runningboardd	[app<application.com.nexy.assistant.20318103.20318109(501)>:5436] Ignoring GPU update because this process is not GPU managed
default	11:25:12.061974-0500	runningboardd	[app<application.com.nexy.assistant.20318103.20318109(501)>:5436] Ignoring memory limit update because this process is not memory-managed
default	11:25:12.073246-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.20318103.20318109(501)>: running-suspended (role: None) (endowments: (null))
default	11:25:12.078335-0500	gamepolicyd	Received state update for 5436 (app<application.com.nexy.assistant.20318103.20318109(501)>, running-suspended-NotVisible
default	11:25:12.142664-0500	Nexy	                AUHAL.cpp:473   ~AUHAL: (0x71cd42340) Selecting device 0 from destructor
default	11:25:12.142689-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0x71cd42340)
default	11:25:12.142699-0500	Nexy	                AUHAL.cpp:676   SelectDevice: (0x71cd42340) not already running
default	11:25:12.142707-0500	Nexy	                AUHAL.cpp:682   SelectDevice: (0x71cd42340) disconnecting device 91
default	11:25:12.142715-0500	Nexy	                AUHAL.cpp:746   SelectDevice: (0x71cd42340) destroying ioproc 0xb for device 91
default	11:25:12.142760-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xb}
default	11:25:12.142802-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	11:25:12.143009-0500	Nexy	                AUHAL.cpp:848   SelectDevice: (0x71cd42340) nothing to setup
default	11:25:12.143028-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x71cd42340) adding 0 device listeners to device 0
default	11:25:12.143047-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x71cd42340) adding 0 device delegate listeners to device 0
default	11:25:12.143055-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x71cd42340) removing 7 device listeners from device 91
default	11:25:12.143368-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x71cd42340) removing 0 device delegate listeners from device 91
default	11:25:12.143392-0500	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0x71cd42340)
default	11:25:12.158317-0500	Nexy	[0x71bbe0640] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	11:25:12.159527-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=5436.2, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=5436, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	11:25:12.162082-0500	tccd	AUTHREQ_SUBJECT: msgID=5436.2, subject=com.nexy.assistant,
default	11:25:12.163166-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d116700 at /Applications/Nexy.app
default	11:25:12.179477-0500	Nexy	[0x71bbe0640] invalidated after the last release of the connection object
default	11:25:12.181062-0500	Nexy	[0x71bbe0640] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	11:25:12.181799-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=5436.3, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=5436, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	11:25:12.183044-0500	tccd	AUTHREQ_SUBJECT: msgID=5436.3, subject=com.nexy.assistant,
default	11:25:12.183722-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d116700 at /Applications/Nexy.app
default	11:25:12.195209-0500	Nexy	[0x71bbe0640] invalidated after the last release of the connection object
default	11:25:12.195414-0500	Nexy	[0x71bbe0640] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	11:25:12.195885-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=5436.4, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=5436, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	11:25:12.196739-0500	tccd	AUTHREQ_SUBJECT: msgID=5436.4, subject=com.nexy.assistant,
default	11:25:12.197333-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d116700 at /Applications/Nexy.app
default	11:25:12.209979-0500	tccd	Notifying for access  kTCCServiceScreenCapture for target PID[5436], responsiblePID[5436], responsiblePath: /Applications/Nexy.app to UID: 501
default	11:25:12.210220-0500	Nexy	[0x71bbe0640] invalidated after the last release of the connection object
default	11:25:12.282779-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d116d00 at /Applications/Nexy.app
default	11:25:12.303788-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d116700 at /Applications/Nexy.app
default	11:25:12.305898-0500	nehelper	Received an apps uninstalled notification with bundle IDs (
    "com.nexy.assistant"
)
default	11:25:12.306993-0500	nehelper	Received an apps uninstalled notification with bundle IDs (
    "com.nexy.assistant"
)
default	11:25:12.307765-0500	tccd	Publishing <TCCDEvent: type=Modify, service=kTCCServiceScreenCapture, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 0 subscribers: {
}
default	11:25:12.901381-0500	nehelper	Removing UUIDs for (
    "com.nexy.assistant"
)
default	11:25:12.907021-0500	nehelper	Handling an apps uninstalled notification with bundle IDs (
    "com.nexy.assistant"
)
default	11:25:12.926892-0500	nehelper	com.apple.preferences.networkprivacy-F67B3EA9-90A6-470B-B321-9BBD719C692B: Populating the cache with 1 UUID(s) for com.nexy.assistant
default	11:25:14.253164-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(49208)
default	11:25:14.254364-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:49208 called from <private>
default	11:25:14.254836-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:49208 called from <private>
default	11:25:14.255040-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:49208 called from <private>
default	11:25:14.255284-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:49208 called from <private>
default	11:25:14.255335-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(49207)
default	11:25:14.255362-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(49207)
default	11:25:14.255387-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:49207 called from <private>
default	11:25:14.255397-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:49207 called from <private>
default	11:25:14.255409-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:49207 called from <private>
default	11:25:14.255417-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:49207 called from <private>
default	11:25:14.286603-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:49207 called from <private>
default	11:25:14.334109-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:49207 called from <private>
default	11:25:14.334153-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:49207 called from <private>
default	11:25:21.245847-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d116400 at /Applications/Nexy.app
default	11:25:21.260272-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117000 at /Applications/Nexy.app
default	11:25:21.271101-0500	tccd	Publishing <TCCDEvent: type=Modify, service=kTCCServiceScreenCapture, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 0 subscribers: {
}
default	11:25:25.718394-0500	audiomxd	  ServerSessionManager.mm:472   { "action":"destroy_session", "session":{"ID":"0x1ef186","name":"Nexy(5436)"}, "details":null }
default	11:25:25.718461-0500	audiomxd	AudioApplicationInfoImpl.mm:690   Successfully removed session 0x1ef186 from AudioApp, recording state unchanged (app: {"name":"[implicit] Nexy","pid":5436})
default	11:25:25.718487-0500	audiomxd	  ServerSessionManager.mm:1081  destroy audio app instance since was created implicitly by session creation and all sessions now gone (audio app: {"name":"[implicit] Nexy","pid":5436})
default	11:25:25.720455-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 391, PID = 5436, Name = sid:0x1ef186, Nexy(5436), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	11:25:25.720830-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 391, PID = 5436, Name = sid:0x1ef186, Nexy(5436), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	11:25:25.722574-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	11:25:25.722683-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	11:25:25.722213-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	11:25:25.722441-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	11:25:25.730581-0500	coreaudiod	>>> NEGOTIATE [com.nexy.assistant]
default	11:25:25.730906-0500	coreaudiod	<<< NEGOTIATE [com.nexy.assistant]
default	11:25:25.733429-0500	coreaudiod	IssueReporting.cpp:492   RTAID [ use_case=Generic report_type=RMS Generic Chain clientID=ADM node=ADM::com.nexy.assistant_49208.49141.0_airpods noise suppression studio::out-0 issue_detected_sample_time=336480.000000 ] -- [ rms:[-37.510834], peaks:[-18.221321] ]
default	11:25:25.733462-0500	coreaudiod	IssueReporting.cpp:492   RTAID [ use_case=Generic report_type=RMS Generic Chain clientID=ADM node=ADM::com.nexy.assistant_49208.49141.0_airpods noise suppression studio::in-0 issue_detected_sample_time=0.000000 ] -- [ rms:[-34.699741], peaks:[-15.815254] ]
default	11:25:25.741534-0500	kernel	Nexy[5436] triggered unnest of range 0x1f6000000->0x1f8000000 of DYLD shared region in VM map 0x6b9ffd60633091f3. While not abnormal for debuggers, this increases system memory footprint until the target exits.
default	11:25:25.741559-0500	kernel	Nexy[5436] triggered unnest of range 0x1f8000000->0x1fa000000 of DYLD shared region in VM map 0x6b9ffd60633091f3. While not abnormal for debuggers, this increases system memory footprint until the target exits.
default	11:25:25.743474-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	11:25:25.743571-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	11:25:26.022129-0500	Nexy	[0x105cf5860] activating connection: mach=true listener=false peer=false name=com.apple.cfprefsd.daemon
default	11:25:26.022197-0500	Nexy	[0x105cf5da0] activating connection: mach=true listener=false peer=false name=com.apple.cfprefsd.agent
error	11:25:26.109996-0500	Nexy	dlsym cannot find symbol NSMakeRect in CFBundle 0x105cf7180 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	11:25:26.110239-0500	Nexy	dlsym cannot find symbol NSMakePoint in CFBundle 0x105cf7180 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	11:25:26.110665-0500	Nexy	dlsym cannot find symbol NSMakeSize in CFBundle 0x105cf7180 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
error	11:25:26.111159-0500	Nexy	dlsym cannot find symbol NSMakeRange in CFBundle 0x105cf7180 </System/Library/Frameworks/Foundation.framework> (framework, loaded): <private>
default	11:25:26.183469-0500	Nexy	Registered notify signal com.apple.caulk.alloc.rtdump (0)
default	11:25:26.186842-0500	Nexy	System_Input_Processing_Notification_Handler.mm:456   System_Input_Processing_Notification_Handler::is_vi_available(): Voice isolation DSP is available for client with bundle id com.nexy.assistant (AVFoundation is available, application is not in client deny list, application is not FaceTime variant)
default	11:25:26.188380-0500	Nexy	[0x105cfb2d0] activating connection: mach=true listener=false peer=false name=com.apple.cmio.registerassistantservice.system-extensions
default	11:25:26.190433-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOInitializeListenersForBundleID: for <private> -> <private>
default	11:25:26.192024-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> vpio_preferenceChangedListener: new value ((null)) for key AUVoiceIOClients/com-nexy-assistant/AUVoiceIOChatFlavor, translatedBundleID com.nexy.assistant, bundleIDs {(
    "com.nexy.assistant"
)}
default	11:25:26.192231-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> vpio_preferenceChangedListener: new value ((null)) for key AUVoiceIOClients/com-nexy-assistant/AUVoiceIOIsAutoChatFlavorEnabled, translatedBundleID com.nexy.assistant, bundleIDs {(
    "com.nexy.assistant"
)}
default	11:25:26.192375-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetSupportedChatFlavorsForBundleID: <private>-><private> get supported chat flavors: <private>
default	11:25:26.192389-0500	Nexy	            HALSystem.cpp:134    Enabling HAL Voice Isolation support
default	11:25:26.192416-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetHiddenChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	11:25:26.192612-0500	Nexy	[0x8ae118000] activating connection: mach=true listener=false peer=false name=com.apple.tccd
default	11:25:26.192684-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOHiddenChatFlavors newValue: (
    1
)
default	11:25:26.193236-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=5436.1, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=5436, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	11:25:26.200283-0500	tccd	AUTHREQ_SUBJECT: msgID=5436.1, subject=com.nexy.assistant,
default	11:25:26.200962-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa0b1a8c00 at /Applications/Nexy.app
default	11:25:26.212349-0500	Nexy	[0x8ae118000] invalidated after the last release of the connection object
default	11:25:26.212533-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetPreferredChatFlavorForBundleID: <private>-><private> get value: 0
default	11:25:26.212577-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOSetSupportedChatFlavorsForBundleID: <private>-><private> setting to: <private>
default	11:25:26.212884-0500	ControlCenter	<<<< AVControlCenterModules >>>> -[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]: com.nexy.assistant:AUVoiceIOClients/com-nexy-assistant/AUVoiceIOSupportedChatFlavors newValue: (
    0,
    2
)
default	11:25:26.214390-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.7081, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=5436, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	11:25:26.215359-0500	tccd	AUTHREQ_SUBJECT: msgID=401.7081, subject=com.nexy.assistant,
default	11:25:26.215967-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa0b1a8c00 at /Applications/Nexy.app
error	11:25:26.227273-0500	tccd	Request message contains a target_token to accessing_process (TCCDProcess: identifier=com.nexy.assistant, pid=5436, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy) but TCCDProcess: identifier=com.apple.audio.coreaudiod, pid=401, auid=202, euid=202, binary_path=/usr/sbin/coreaudiod is not a TCC manager for service: kTCCServiceScreenCapture.
default	11:25:26.228193-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.7083, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=5436, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	11:25:26.228974-0500	tccd	AUTHREQ_SUBJECT: msgID=401.7083, subject=com.nexy.assistant,
default	11:25:26.229494-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa0b1a8c00 at /Applications/Nexy.app
default	11:25:26.243330-0500	Nexy	  HALPlugInManagement.cpp:440    HALPlugInManagement::RegisterPlugIns: skipping in-process plug-ins
error	11:25:26.243350-0500	Nexy	AddInstanceForFactory: No factory registered for id <CFUUID 0x8aca504a0> F8BB1C28-BAE8-11D6-9C31-00039315CD46
error	11:25:26.266527-0500	Nexy	         HALC_ProxyObjectMap.cpp:174   HALC_ProxyObjectMap::_CopyObjectByObjectID: failed to create the local object
error	11:25:26.266540-0500	Nexy	            HALC_ShellDevice.cpp:2673  HALC_ShellDevice::RebuildControlList: couldn't find the control object
default	11:25:26.269731-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	11:25:26.269881-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	11:25:26.274862-0500	Nexy	<<<< AVAUVoiceIOChatFlavor >>>> AVAUVoiceIOGetPreferredChatFlavorForBundleID: <private>-><private> get value: 0
default	11:25:27.679379-0500	kernel	SK[6]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 65705080-B2F3-49AD-821F-8138C59B6C30 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.64326,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0x592c6c01 tp_proto=0x06"
default	11:25:27.679454-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:64326<-><IPv4-redacted>:53] interface: utun6 (skipped: 6743)
so_gencnt: 4930527 t_state: SYN_SENT process: Nexy:5436 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 1 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xb0031cc0
default	11:25:27.679960-0500	kernel	tcp connected: [<IPv4-redacted>:64326<-><IPv4-redacted>:53] interface: utun6 (skipped: 6743)
so_gencnt: 4930527 t_state: ESTABLISHED process: Nexy:5436 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 1 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xb0031cc0
default	11:25:27.680233-0500	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:64326<-><IPv4-redacted>:53] interface: utun6 (skipped: 6743)
so_gencnt: 4930527 t_state: FIN_WAIT_1 process: Nexy:5436 Duration: 0.001 sec Conn_Time: 0.000 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 1.000 ms rttvar: 0.500 ms base rtt: 1 ms so_error: 0 svc/tc: 0 flow: 0xb0031cc0
default	11:25:27.680243-0500	kernel	tcp_connection_summary [<IPv4-redacted>:64326<-><IPv4-redacted>:53] interface: utun6 (skipped: 6743)
so_gencnt: 4930527 t_state: FIN_WAIT_1 process: Nexy:5436 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	11:25:27.697210-0500	Nexy	[0x8ae118000] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioComponentRegistrar
default	11:25:27.709055-0500	Nexy	                AUHAL.cpp:420   AUHAL: (0x8ae093140) Selecting device 85 from constructor
default	11:25:27.709069-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0x8ae093140)
default	11:25:27.709075-0500	Nexy	                AUHAL.cpp:676   SelectDevice: (0x8ae093140) not already running
default	11:25:27.709079-0500	Nexy	                AUHAL.cpp:752   SelectDevice: (0x8ae093140) nothing to teardown
default	11:25:27.709084-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0x8ae093140) connecting device 85
default	11:25:27.709166-0500	Nexy	                AUHAL.cpp:3413  IsDeviceUsable: (0x8ae093140) Device ID: 85 (Input:No | Output:Yes): true
default	11:25:27.709263-0500	Nexy	                AUHAL.cpp:769   SelectDevice: (0x8ae093140) created ioproc 0xa for device 85
default	11:25:27.709376-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x8ae093140) adding 7 device listeners to device 85
default	11:25:27.709541-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x8ae093140) adding 0 device delegate listeners to device 85
default	11:25:27.709549-0500	Nexy	                AUHAL.cpp:1581  UpdateStreamFormats: -> (0x8ae093140)
default	11:25:27.709623-0500	Nexy	                AUHAL.cpp:1677  UpdateStreamFormats: 
  output stream 0 [0x56]:  2 ch,  48000 Hz, Float32, interleaved
default	11:25:27.709640-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 1 output streams; not all mono
default	11:25:27.709645-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Output render format:  2 ch,  48000 Hz, Float32, interleaved
default	11:25:27.709651-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 0 input streams; not all mono
default	11:25:27.709659-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Input render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	11:25:27.709757-0500	Nexy	                AUHAL.cpp:1771  UpdateStreamFormats: AUHAL(0x8ae093140) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	11:25:27.709770-0500	Nexy	                AUHAL.cpp:1777  UpdateStreamFormats: AUHAL(0x8ae093140) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	11:25:27.709775-0500	Nexy	                AUHAL.cpp:1787  UpdateStreamFormats: <-
default	11:25:27.709779-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x8ae093140) removing 0 device listeners from device 0
default	11:25:27.709784-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x8ae093140) removing 0 device delegate listeners from device 0
default	11:25:27.709788-0500	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0x8ae093140)
default	11:25:27.709805-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Output stream enables: Stream 0 is DISABLED
default	11:25:27.709906-0500	Nexy	                AUHAL.cpp:2298  SetProperty: (0x8ae093140) caller requesting device change from 85 to 91
default	11:25:27.709932-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0x8ae093140)
default	11:25:27.709942-0500	Nexy	                AUHAL.cpp:676   SelectDevice: (0x8ae093140) not already running
default	11:25:27.709947-0500	Nexy	                AUHAL.cpp:682   SelectDevice: (0x8ae093140) disconnecting device 85
default	11:25:27.709950-0500	Nexy	                AUHAL.cpp:746   SelectDevice: (0x8ae093140) destroying ioproc 0xa for device 85
default	11:25:27.709995-0500	Nexy	  AVAudioSession_MacOS.mm:1021  initForMacOS
default	11:25:27.710551-0500	Nexy	[0x8ae118280] activating connection: mach=true listener=false peer=false name=com.apple.audio.AudioSession
default	11:25:27.711503-0500	audiomxd	  ServerSessionManager.mm:315   { "action":"create_session", "session":{"ID":"0x1ef187","name":"Nexy(5436)"}, "details":{"PID":5436,"session_type":"Primary"} }
default	11:25:27.711585-0500	audiomxd	AudioApplicationInfoImpl.mm:250   Setting initial isRecording state: 0 for newly-created AudioApp
	app: {"name":"[implicit] Nexy","pid":5436}
	AudioApp.isRecording: false
[ 
	{ sessionID: 0x1ef187, sessionType: 'prim', isRecording: false }, 
]
default	11:25:27.711926-0500	Nexy	    SessionCore_Create.mm:99    Created session 0x8aca76680 with ID: 0x1ef187
default	11:25:27.712611-0500	Nexy	[0x8ae1183c0] activating connection: mach=true listener=false peer=false name=com.apple.audioanalyticsd
default	11:25:27.712752-0500	Nexy	No persisted cache on this platform.
error	11:25:27.713099-0500	Nexy	Reporter disconnected. { function=sendMessage, reporterID=23347442221057 }
default	11:25:27.713114-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped Unknown {1C-77-54-18-C8-A3:output, 0xa}
default	11:25:27.713170-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	11:25:27.713273-0500	Nexy	                AUHAL.cpp:757   SelectDevice: (0x8ae093140) connecting device 91
default	11:25:27.713361-0500	Nexy	                AUHAL.cpp:3413  IsDeviceUsable: (0x8ae093140) Device ID: 91 (Input:Yes | Output:No): true
default	11:25:27.714755-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.7084, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=5436, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	11:25:27.715951-0500	tccd	AUTHREQ_SUBJECT: msgID=401.7084, subject=com.nexy.assistant,
default	11:25:27.716574-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa0b1a8c00 at /Applications/Nexy.app
default	11:25:27.728816-0500	Nexy	                AUHAL.cpp:769   SelectDevice: (0x8ae093140) created ioproc 0xa for device 91
default	11:25:27.728945-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x8ae093140) adding 7 device listeners to device 91
default	11:25:27.729134-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x8ae093140) adding 0 device delegate listeners to device 91
default	11:25:27.729140-0500	Nexy	                AUHAL.cpp:1581  UpdateStreamFormats: -> (0x8ae093140)
default	11:25:27.729150-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 0 output streams; not all mono
default	11:25:27.729159-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Output render format:  0 ch,      0 Hz, lpcm (0x00000029) 32-bit little-endian float, deinterleaved
default	11:25:27.729278-0500	Nexy	                AUHAL.cpp:1677  UpdateStreamFormats: 
  input stream 0 [0x5c]:  1 ch,  24000 Hz, Float32
default	11:25:27.729286-0500	Nexy	                AUHAL.cpp:1689  UpdateStreamFormats: 1 input streams; all mono
default	11:25:27.729291-0500	Nexy	                AUHAL.cpp:1701  UpdateStreamFormats: 
  Input render format:  1 ch,  24000 Hz, Float32
default	11:25:27.729382-0500	Nexy	                AUHAL.cpp:1771  UpdateStreamFormats: AUHAL(0x8ae093140) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Output, Bus:Output
default	11:25:27.729398-0500	Nexy	                AUHAL.cpp:1777  UpdateStreamFormats: AUHAL(0x8ae093140) Calling PropertyChanged() for kAudioUnitProperty_StreamFormat, Scope:Input, Bus:Input
default	11:25:27.729406-0500	Nexy	                AUHAL.cpp:1787  UpdateStreamFormats: <-
default	11:25:27.729409-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x8ae093140) removing 7 device listeners from device 85
default	11:25:27.729585-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x8ae093140) removing 0 device delegate listeners from device 85
default	11:25:27.729593-0500	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0x8ae093140)
default	11:25:27.730214-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	11:25:27.731220-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.7085, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=5436, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	11:25:27.732007-0500	tccd	AUTHREQ_SUBJECT: msgID=401.7085, subject=com.nexy.assistant,
default	11:25:27.732553-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa0b1a8c00 at /Applications/Nexy.app
default	11:25:27.743407-0500	Nexy	                AUHAL.cpp:1893  SetStreamUsage: Input stream enables: Stream 0 is ENABLED
default	11:25:27.744330-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.7086, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=5436, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	11:25:27.745148-0500	tccd	AUTHREQ_SUBJECT: msgID=401.7086, subject=com.nexy.assistant,
default	11:25:27.745719-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa0b1a8c00 at /Applications/Nexy.app
default	11:25:27.757292-0500	Nexy	Registered notify signal com.apple.caulk.alloc.audiodump (0)
default	11:25:27.758740-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.7087, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=5436, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	11:25:27.759497-0500	tccd	AUTHREQ_SUBJECT: msgID=401.7087, subject=com.nexy.assistant,
default	11:25:27.760025-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa0b1a8c00 at /Applications/Nexy.app
default	11:25:27.771348-0500	coreaudiod	>>> NEGOTIATE [com.nexy.assistant]
default	11:25:27.771503-0500	coreaudiod	<<< NEGOTIATE [com.nexy.assistant]
default	11:25:27.772656-0500	coreaudiod	>>> ADAPT [com.nexy.assistant]
default	11:25:27.773015-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xbf6fa3600] Created node ADM::com.nexy.assistant_49221.49141.0_airpods noise suppression studio::in-0 with nodeID 0 - reporting period = 10.000000, sample rate = 24000.000000
default	11:25:27.773098-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xbf6fa3600] Created node ADM::com.nexy.assistant_49221.49141.0_airpods noise suppression studio::out-0 with nodeID 1 - reporting period = 10.000000, sample rate = 24000.000000
default	11:25:27.842299-0500	coreaudiod	<<< ADAPT [com.nexy.assistant]
default	11:25:27.849351-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.20318103.20318109(501)>:5436] from originator [osservice<com.apple.powerd>:334] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:398-334-1316815 target:5436 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	11:25:27.845197-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:49221 called from <private>
default	11:25:27.849453-0500	runningboardd	Assertion 398-334-1316815 (target:[app<application.com.nexy.assistant.20318103.20318109(501)>:5436]) will be created as active
default	11:25:27.845257-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	11:25:27.845263-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Started  Input {1C-77-54-18-C8-A3:input, 0xa}
default	11:25:27.846215-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:49221 called from <private>
default	11:25:27.846916-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(49221)
default	11:25:27.846944-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:49221 called from <private>
default	11:25:27.847398-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(49220)
default	11:25:27.849318-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:49221 called from <private>
default	11:25:27.850096-0500	runningboardd	[app<application.com.nexy.assistant.20318103.20318109(501)>:5436] Ignoring jetsam update because this process is not memory-managed
default	11:25:27.849806-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:49220 called from <private>
default	11:25:27.850300-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:49220 called from <private>
default	11:25:27.850469-0500	runningboardd	[app<application.com.nexy.assistant.20318103.20318109(501)>:5436] Ignoring suspend because this process is not lifecycle managed
default	11:25:27.851654-0500	runningboardd	[app<application.com.nexy.assistant.20318103.20318109(501)>:5436] Set darwin role to: Background
default	11:25:27.852138-0500	runningboardd	[app<application.com.nexy.assistant.20318103.20318109(501)>:5436] Ignoring GPU update because this process is not GPU managed
default	11:25:27.852273-0500	runningboardd	[app<application.com.nexy.assistant.20318103.20318109(501)>:5436] Ignoring memory limit update because this process is not memory-managed
default	11:25:27.855618-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
fault	11:25:27.855830-0500	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.20318103.20318109 AUID=501> and <type=Application identifier=application.com.nexy.assistant.20318103.20318109>
default	11:25:27.856234-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
fault	11:25:27.858582-0500	runningboardd	Two equal instances have unequal identities. <type=Application identifier=application.com.nexy.assistant.20318103.20318109 AUID=501> and <type=Application identifier=application.com.nexy.assistant.20318103.20318109>
default	11:25:27.862006-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(49221)
default	11:25:27.862514-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(49221)
default	11:25:27.862610-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(49221)
default	11:25:27.862761-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(49221)
default	11:25:27.862921-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:49221 called from <private>
default	11:25:27.862992-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:49221 called from <private>
default	11:25:27.863014-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:49221 called from <private>
default	11:25:27.863034-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:49221 called from <private>
default	11:25:27.863298-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.20318103.20318109(501)>: running-active (role: Background) (endowments: (null))
default	11:25:27.863742-0500	runningboardd	Invalidating assertion 398-334-1316815 (target:[app<application.com.nexy.assistant.20318103.20318109(501)>:5436]) from originator [osservice<com.apple.powerd>:334]
default	11:25:27.863883-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:49221 called from <private>
default	11:25:27.864294-0500	gamepolicyd	Received state update for 5436 (app<application.com.nexy.assistant.20318103.20318109(501)>, running-active-NotVisible
default	11:25:27.864340-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:49221 called from <private>
default	11:25:27.864490-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:49221 called from <private>
default	11:25:27.864548-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:49221 called from <private>
default	11:25:27.872819-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	11:25:27.872920-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	11:25:27.872981-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	11:25:27.875427-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:25:27.875439-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:25:27.875452-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	11:25:27.875459-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:25:27.875466-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	11:25:27.875473-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	11:25:27.875569-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	11:25:27.881792-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(49221)
default	11:25:27.885004-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(49220)
default	11:25:27.885164-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:49221 called from <private>
default	11:25:27.885179-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:49221 called from <private>
default	11:25:27.885226-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:49221 called from <private>
default	11:25:27.885540-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
error	11:25:27.885660-0500	Nexy	         HALC_ProxyIOContext.cpp:1042  HALC_ProxyIOContext::_StartIO(): Client running as an adaptive unboosted daemon
default	11:25:27.885691-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:25:27.885710-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:25:27.885732-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	11:25:27.885739-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:25:27.885746-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	11:25:27.885752-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	11:25:27.885874-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	11:25:27.886141-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ef187","name":"Nexy(5436)"}, "details":{"deviceUIDs":["1C-77-54-18-C8-A3:input"],"implicit_category":"Record","input_running":true,"output_running":false} }
default	11:25:27.886389-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 392, PID = 5436, Name = sid:0x1ef187, Nexy(5436), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = YES
default	11:25:27.886459-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 392, PID = 5436, Name = sid:0x1ef187, Nexy(5436), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	11:25:27.886533-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	11:25:27.886538-0500	audiomxd	-CMSMNotificationUtilities- CMSMNotificationUtility_PostSessionAudioCategoryDidChange_block_invoke: Posting AudioCategoryDidChange to session 'sid:0x1ef187, Nexy(5436), 'prim'', AudioCategory changed to 'Record_WithBluetooth'
default	11:25:27.886615-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 392, PID = 5436, Name = sid:0x1ef187, Nexy(5436), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	11:25:27.886687-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	11:25:27.886677-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 392, PID = 5436, Name = sid:0x1ef187, Nexy(5436), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	11:25:27.886796-0500	audiomxd	-MXCoreSession- -[MXCoreSession beginInterruption]: Session <ID: 392, PID = 5436, Name = sid:0x1ef187, Nexy(5436), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> is going active
default	11:25:27.886815-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1ef187, Nexy(5436), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 392 starting recording
default	11:25:27.886985-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 392, PID = 5436, Name = sid:0x1ef187, Nexy(5436), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	11:25:27.887464-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	11:25:27.887130-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 392, PID = 5436, Name = sid:0x1ef187, Nexy(5436), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	11:25:27.887217-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1ef187, Nexy(5436), 'prim'', displayID:'com.nexy.assistant'}
default	11:25:27.886853-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	11:25:27.887541-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	11:25:27.887939-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=401.7088, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=5436, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.tccd, pid=394, auid=0, euid=0, binary_path=/System/Library/PrivateFrameworks/TCC.framework/Support/tccd}, },
default	11:25:27.887942-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [1, 0]. BT device UIDS: {(
    "1C-77-54-18-C8-A3:input"
)}
default	11:25:27.888010-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	11:25:27.889532-0500	tccd	AUTHREQ_SUBJECT: msgID=401.7088, subject=com.nexy.assistant,
default	11:25:27.890830-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:25:27.890888-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:25:27.890997-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	11:25:27.891076-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:25:27.891127-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	11:25:27.891134-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	11:25:27.891938-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	11:25:27.890753-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa0b1a8c00 at /Applications/Nexy.app
default	11:25:27.898214-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:49220 called from <private>
default	11:25:27.898343-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:49220 called from <private>
default	11:25:27.899029-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(49220)
default	11:25:27.906903-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(49220)
default	11:25:27.907203-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:49220 called from <private>
default	11:25:27.907222-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:49220 called from <private>
default	11:25:27.908508-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:49220 called from <private>
default	11:25:27.908552-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:49220 called from <private>
default	11:25:27.908596-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:49220 called from <private>
default	11:25:27.908606-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:49220 called from <private>
default	11:25:27.908612-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:49220 called from <private>
default	11:25:27.908636-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:49220 called from <private>
default	11:25:27.913816-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	11:25:27.914184-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	11:25:27.914891-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 200 flag 0x1 < Hijack > app com.nexy.assistant CID 0xD310001 category Not set
default	11:25:27.930577-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:49221 called from <private>
default	11:25:27.931915-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:49220 called from <private>
default	11:25:27.943368-0500	tccd	AUTHREQ_SUBJECT: msgID=401.7089, subject=com.nexy.assistant,
default	11:25:27.944220-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa0b1a8c00 at /Applications/Nexy.app
default	11:25:27.959408-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xbf6fa3600] Created node ADM::com.nexy.assistant_49221.49141.0_airpods noise suppression studio::in-0 with nodeID 0 - reporting period = 10.000000, sample rate = 24000.000000
default	11:25:27.959469-0500	coreaudiod	[Detector.cpp:154   rtaid::Detector:0xbf6fa3600] Created node ADM::com.nexy.assistant_49221.49141.0_airpods noise suppression studio::out-0 with nodeID 1 - reporting period = 10.000000, sample rate = 24000.000000
default	11:25:27.968559-0500	runningboardd	[app<application.com.nexy.assistant.20318103.20318109(501)>:5436] Ignoring jetsam update because this process is not memory-managed
default	11:25:27.968570-0500	runningboardd	[app<application.com.nexy.assistant.20318103.20318109(501)>:5436] Ignoring suspend because this process is not lifecycle managed
default	11:25:27.968602-0500	runningboardd	[app<application.com.nexy.assistant.20318103.20318109(501)>:5436] Set darwin role to: None
default	11:25:27.968612-0500	runningboardd	[app<application.com.nexy.assistant.20318103.20318109(501)>:5436] Ignoring GPU update because this process is not GPU managed
default	11:25:27.968662-0500	runningboardd	[app<application.com.nexy.assistant.20318103.20318109(501)>:5436] Ignoring memory limit update because this process is not memory-managed
default	11:25:27.972732-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.20318103.20318109(501)>: running-suspended (role: None) (endowments: (null))
default	11:25:27.975775-0500	gamepolicyd	Received state update for 5436 (app<application.com.nexy.assistant.20318103.20318109(501)>, running-suspended-NotVisible
default	11:25:27.993918-0500	coreaudiod	<<< ADAPT [com.nexy.assistant]
default	11:25:27.995100-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.20318103.20318109(501)>:5436] from originator [osservice<com.apple.powerd>:334] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:398-334-1316820 target:5436 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	11:25:27.995165-0500	runningboardd	Assertion 398-334-1316820 (target:[app<application.com.nexy.assistant.20318103.20318109(501)>:5436]) will be created as active
default	11:25:27.997612-0500	runningboardd	[app<application.com.nexy.assistant.20318103.20318109(501)>:5436] Ignoring jetsam update because this process is not memory-managed
default	11:25:27.997744-0500	runningboardd	[app<application.com.nexy.assistant.20318103.20318109(501)>:5436] Ignoring suspend because this process is not lifecycle managed
default	11:25:27.997950-0500	runningboardd	[app<application.com.nexy.assistant.20318103.20318109(501)>:5436] Set darwin role to: Background
default	11:25:27.998089-0500	runningboardd	[app<application.com.nexy.assistant.20318103.20318109(501)>:5436] Ignoring GPU update because this process is not GPU managed
default	11:25:27.998820-0500	runningboardd	[app<application.com.nexy.assistant.20318103.20318109(501)>:5436] Ignoring memory limit update because this process is not memory-managed
default	11:25:27.999104-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:49221 called from <private>
default	11:25:27.999458-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 1 0 0, id:49221 called from <private>
default	11:25:28.999541-0500	Nexy	         HALC_ProxyIOContext.cpp:1594  HALC_ProxyIOContext::IOWorkLoop: ending the transport, stopping the io thread
default	11:25:28.001215-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:49221 called from <private>
default	11:25:28.001677-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(49221)
default	11:25:28.001730-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:49221 called from <private>
default	11:25:28.001912-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:49221 called from <private>
default	11:25:28.002228-0500	coreaudiod	>>> SIMULATE [com.nexy.assistant]
default	11:25:28.002355-0500	coreaudiod	<<< SIMULATE [com.nexy.assistant]
default	11:25:28.003295-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(49221)
default	11:25:28.003969-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:49221 called from <private>
default	11:25:28.004014-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:49221 called from <private>
default	11:25:28.004055-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:49221 called from <private>
error	11:25:28.004307-0500	Nexy	         HALC_ProxyIOContext.cpp:1042  HALC_ProxyIOContext::_StartIO(): Client running as an adaptive unboosted daemon
default	11:25:28.007805-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0xa0b1a8c00 at /Applications/Nexy.app
default	11:25:28.022840-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.20318103.20318109(501)>:5436] from originator [osservice<com.apple.powerd>:334] with description <RBSAssertionDescriptor| "App is holding power assertion" ID:398-334-1316821 target:5436 attributes:[
	<RBSDomainAttribute| domain:"com.apple.appnap" name:"PowerAssertion" sourceEnvironment:"(null)">,
	<RBSAcquisitionCompletionAttribute| policy:AfterApplication>
	]>
default	11:25:28.023566-0500	runningboardd	Assertion 398-334-1316821 (target:[app<application.com.nexy.assistant.20318103.20318109(501)>:5436]) will be created as active
default	11:25:28.023880-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 1 0 0 id:49221 called from <private>
default	11:25:28.030812-0500	ControlCenter	SystemStatus attributed attribution to com.nexy.assistant, displayName: <private>, bundlePath: <private>, executablePath: <private>, isSystemExecutable: false
default	11:25:28.030857-0500	ControlCenter	Sorted active attributions from SystemStatus update: [[mic] Nexy (com.nexy.assistant)]
default	11:25:28.030890-0500	ControlCenter	Active activity attributions changed to ["mic:com.nexy.assistant"]
default	11:25:28.031155-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:25:28.031167-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:25:28.031176-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	11:25:28.031182-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:25:28.031188-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	11:25:28.031213-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	11:25:28.031249-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:25:28.031297-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:25:28.031316-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	11:25:28.031322-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:25:28.031328-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	11:25:28.031351-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	11:25:28.031550-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	11:25:28.031641-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:25:28.031685-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:25:28.031743-0500	ControlCenter	Navigating to new application [com.nexy.assistant]
default	11:25:28.031732-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	11:25:28.031795-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:25:28.031860-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	11:25:28.031934-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	11:25:29.246645-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xa}
default	11:25:29.247066-0500	audiomxd	AVAudioSessionXPCServer.mm:2171  { "action":"update_running_state", "session":{"ID":"0x1ef187","name":"Nexy(5436)"}, "details":{"deviceUIDs":[],"implicit_category":"","input_running":false,"output_running":false} }
default	11:25:29.247237-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 392, PID = 5436, Name = sid:0x1ef187, Nexy(5436), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	11:25:29.247323-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 200 for session <ID: 392, PID = 5436, Name = sid:0x1ef187, Nexy(5436), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = YES, Playing = NO, Recording = YES>
default	11:25:29.247370-0500	audiomxd	-MXSessionManager- -[MXSessionManager shouldRequestForForceHijack]: Found only 1 session={clientName:'sid:0x1ef187, Nexy(5436), 'prim'', displayID:'com.nexy.assistant'}
default	11:25:29.247453-0500	audiomxd	-MXCoreSession- -[MXCoreSession updateIsRecording:]: MXCoreSession sid:0x1ef187, Nexy(5436), 'prim' with category(Record_WithBluetooth)/mode(Default) and coreSessionID = 392 stopping recording
default	11:25:29.247450-0500	audiomxd	-MXAudioAccessoryServices- -[MXAudioAccessoryServices requestForSharedRoute:audioScore:bundleID:startIO:forceHijack:]_block_invoke: Calling to request for ownership on shared route com.nexy.assistant, isDoingIO = YES, score = 200, deviceID = <private>
default	11:25:29.247502-0500	audiomxd	-MXCoreSession- -[MXCoreSession endInterruption:]: Session <ID: 392, PID = 5436, Name = sid:0x1ef187, Nexy(5436), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> is going inactive
default	11:25:29.247577-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Session <ID: 392, PID = 5436, Name = sid:0x1ef187, Nexy(5436), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO> requesting for shared ownership, didNowPlayingInfoChanged = NO, didCategoryOrModeChange = NO
default	11:25:29.247663-0500	audiomxd	-MXSessionManager- -[MXSessionManager requestForSharedOwnership:didNowPlayingInfoChange:didCategoryOrModeChange:]: Setting score as 201 for session <ID: 392, PID = 5436, Name = sid:0x1ef187, Nexy(5436), 'prim', BundleID = com.nexy.assistant, Category = Record_WithBluetooth, Mode = Default, Active = NO, Playing = NO, Recording = NO>
default	11:25:29.247880-0500	audioaccessoryd	Routing request Wx 1C:77:54:18:C8:A3 score 200 flag 0x1 < Hijack > app com.nexy.assistant CID 0xD310001 category Not set
default	11:25:29.247977-0500	Nexy	SessionCore_macOS_Legacy.mm:124   Sent updated IOState to server: [0, 0]. BT device UIDS: {(
)}
default	11:25:29.247996-0500	Nexy	SessionCore_macOS_Legacy.mm:167   <-- setPlayState Server update was required.
default	11:25:29.252502-0500	runningboardd	Invalidating assertion 398-334-1316821 (target:[app<application.com.nexy.assistant.20318103.20318109(501)>:5436]) from originator [osservice<com.apple.powerd>:334]
default	11:25:29.252934-0500	audioaccessoryd	Audio state update Start apps {
    "com.nexy.assistant" : 200,
}
default	11:25:29.252979-0500	audioaccessoryd	AudioStateChanged: Received audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	11:25:29.253002-0500	audioaccessoryd	Audio state update Stop apps {
    "com.nexy.assistant" : 201,
}
default	11:25:29.253032-0500	audioaccessoryd	AudioStateChanged: Updated audio session com.nexy.assistant 200
default	11:25:29.252765-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Start apps {
    "com.nexy.assistant" : 200,
}
default	11:25:29.253238-0500	audioaccessoryd	PredictiveRoute: Skip, Mac is not idle. LocalScore 200 App com.nexy.assistant
default	11:25:29.252852-0500	audiomxd	UpdateAudioState CID 0xD310001 audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	11:25:29.253300-0500	audioaccessoryd	AudioStateChanged: Received audioState Stop apps {
    "com.nexy.assistant" : 201,
}
default	11:25:29.253384-0500	audioaccessoryd	AudioStateChanged: Removed audio session app com.nexy.assistant 201 count 0
default	11:25:29.255583-0500	ControlCenter	Recent activity attributions changed to ["mic:com.nexy.assistant"]
default	11:25:29.258296-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:25:29.258310-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:25:29.258322-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterVideoEffectsModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	11:25:29.258330-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: called for bundleID: com.nexy.assistant
default	11:25:29.258336-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterMicrophoneModuleShouldBeShownForBundleID: com.nexy.assistant active:1
default	11:25:29.258342-0500	ControlCenter	<<<< AVControlCenterModules >>>> AVControlCenterModulesShouldBeShownForBundleID: com.nexy.assistant videoEffectsShouldBeShown:1 micModesShouldBeShown:1
default	11:25:29.258485-0500	ControlCenter	com.nexy.assistant supportedModes: [standard, voiceIsolation], unsupported: [], hidden: [wideSpectrum], enabled: true, _mode: standard
default	11:25:29.359905-0500	runningboardd	[app<application.com.nexy.assistant.20318103.20318109(501)>:5436] Ignoring jetsam update because this process is not memory-managed
default	11:25:29.359925-0500	runningboardd	[app<application.com.nexy.assistant.20318103.20318109(501)>:5436] Ignoring suspend because this process is not lifecycle managed
default	11:25:29.359982-0500	runningboardd	[app<application.com.nexy.assistant.20318103.20318109(501)>:5436] Set darwin role to: None
default	11:25:29.359997-0500	runningboardd	[app<application.com.nexy.assistant.20318103.20318109(501)>:5436] Ignoring GPU update because this process is not GPU managed
default	11:25:29.360024-0500	runningboardd	[app<application.com.nexy.assistant.20318103.20318109(501)>:5436] Ignoring memory limit update because this process is not memory-managed
default	11:25:29.364829-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.20318103.20318109(501)>: running-suspended (role: None) (endowments: (null))
default	11:25:29.365648-0500	gamepolicyd	Received state update for 5436 (app<application.com.nexy.assistant.20318103.20318109(501)>, running-suspended-NotVisible
default	11:25:29.405177-0500	Nexy	                AUHAL.cpp:473   ~AUHAL: (0x8ae093140) Selecting device 0 from destructor
default	11:25:29.405208-0500	Nexy	                AUHAL.cpp:624   SelectDevice: -> (0x8ae093140)
default	11:25:29.405224-0500	Nexy	                AUHAL.cpp:676   SelectDevice: (0x8ae093140) not already running
default	11:25:29.405236-0500	Nexy	                AUHAL.cpp:682   SelectDevice: (0x8ae093140) disconnecting device 91
default	11:25:29.405250-0500	Nexy	                AUHAL.cpp:746   SelectDevice: (0x8ae093140) destroying ioproc 0xa for device 91
default	11:25:29.405308-0500	Nexy	SessionCore_macOS_Legacy.mm:131   --> setPlayState Stopped  Input {1C-77-54-18-C8-A3:input, 0xa}
default	11:25:29.405374-0500	Nexy	SessionCore_macOS_Legacy.mm:162   <-- setPlayState IOState: [0, 0]. BT device UIDS: {(
)} Server update was not required.
default	11:25:29.405713-0500	Nexy	                AUHAL.cpp:848   SelectDevice: (0x8ae093140) nothing to setup
default	11:25:29.405738-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x8ae093140) adding 0 device listeners to device 0
default	11:25:29.405751-0500	Nexy	                AUHAL.cpp:858   SelectDevice: (0x8ae093140) adding 0 device delegate listeners to device 0
default	11:25:29.405769-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x8ae093140) removing 7 device listeners from device 91
default	11:25:29.406320-0500	Nexy	                AUHAL.cpp:895   SelectDevice: (0x8ae093140) removing 0 device delegate listeners from device 91
default	11:25:29.406352-0500	Nexy	                AUHAL.cpp:911   SelectDevice: <- (0x8ae093140)
default	11:25:29.548842-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=5476.1, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=5436, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.osascript, pid=5476, auid=501, euid=501, binary_path=/usr/bin/osascript}, },
default	11:25:29.550358-0500	tccd	AUTHREQ_SUBJECT: msgID=5476.1, subject=com.nexy.assistant,
default	11:25:29.551057-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d116400 at /Applications/Nexy.app
default	11:25:29.564496-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=393.13421, attribution={responsible={TCCDProcess: identifier=com.nexy.assistant, pid=5436, auid=501, euid=501, responsible_path=/Applications/Nexy.app/Contents/MacOS/Nexy, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, accessing={TCCDProcess: identifier=com.apple.osascript, pid=5476, auid=501, euid=501, binary_path=/usr/bin/osascript}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=393, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	11:25:29.565329-0500	tccd	AUTHREQ_SUBJECT: msgID=393.13421, subject=com.nexy.assistant,
default	11:25:29.565958-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d116400 at /Applications/Nexy.app
default	11:25:29.594445-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d116400 at /Applications/Nexy.app
default	11:25:29.611695-0500	System Events	TCCAccessRequestIndirect: TCCAccessRequestIndirect with pid 5442: target_identity: {
    kTCCCodeIdentityAuditToken = {length = 32, bytes = 0xf5010000 f5010000 14000000 f5010000 ... b7860100 dc2b1d00 };
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
default	11:25:29.625785-0500	tccd	target_executable_path_URL: file:///Applications/Nexy.app/Contents/MacOS/Nexy
default	11:25:30.486604-0500	Nexy	[0x8ae118640] activating connection: mach=true listener=false peer=false name=com.apple.distributed_notifications@Uv3
default	11:25:30.488018-0500	Nexy	[0x8ae1188c0] activating connection: mach=true listener=false peer=false name=com.apple.analyticsd
default	11:25:30.491492-0500	Nexy	Received configuration update from daemon (initial)
default	11:25:30.540406-0500	Nexy	[0x8ae118a00] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
error	11:25:30.541026-0500	tccd	TCCDProcess: identifier=com.nexy.assistant, pid=5436, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy attempted to call TCCAccessRequest for kTCCServiceAccessibility without the recommended com.apple.private.tcc.manager.check-by-audit-token entitlement
default	11:25:30.541202-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=5436.2, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=5436, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.nexy.assistant, pid=5436, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	11:25:30.542812-0500	tccd	AUTHREQ_SUBJECT: msgID=5436.2, subject=com.nexy.assistant,
default	11:25:30.543509-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d116400 at /Applications/Nexy.app
default	11:25:30.555336-0500	Nexy	[0x8ae118a00] invalidated after the last release of the connection object
default	11:25:30.556183-0500	Nexy	[0x8ae118a00] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
error	11:25:30.556616-0500	tccd	TCCDProcess: identifier=com.nexy.assistant, pid=5436, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy attempted to call TCCAccessRequest for kTCCServiceAccessibility without the recommended com.apple.private.tcc.manager.check-by-audit-token entitlement
default	11:25:30.556798-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=5436.3, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=5436, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.nexy.assistant, pid=5436, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	11:25:30.557723-0500	tccd	AUTHREQ_SUBJECT: msgID=5436.3, subject=com.nexy.assistant,
default	11:25:30.558393-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d116400 at /Applications/Nexy.app
default	11:25:30.569705-0500	Nexy	[0x8ae118a00] invalidated after the last release of the connection object
default	11:25:30.569760-0500	Nexy	[0x8ae118b40] activating connection: mach=true listener=false peer=false name=com.apple.universalaccessAuthWarn
default	11:25:30.569849-0500	Nexy	[0x8ae118b40] invalidated after the last release of the connection object
default	11:25:30.570157-0500	Nexy	[0x8ae118c80] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	11:25:30.570585-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=5436.4, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=5436, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	11:25:30.571465-0500	tccd	AUTHREQ_SUBJECT: msgID=5436.4, subject=com.nexy.assistant,
default	11:25:30.572150-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d116400 at /Applications/Nexy.app
default	11:25:30.583604-0500	tccd	Notifying for access  kTCCServiceListenEvent for target PID[5436], responsiblePID[5436], responsiblePath: /Applications/Nexy.app to UID: 501
default	11:25:30.583828-0500	Nexy	[0x8ae118c80] invalidated after the last release of the connection object
default	11:25:30.584152-0500	Nexy	server port 0x0000b90b, session port 0x0000b807
default	11:25:30.585078-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=393.13422, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=5436, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=393, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	11:25:30.585104-0500	tccd	requestor: TCCDProcess: identifier=com.apple.WindowServer, pid=393, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=5436, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	11:25:30.586262-0500	tccd	AUTHREQ_SUBJECT: msgID=393.13422, subject=com.nexy.assistant,
default	11:25:30.587253-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d116400 at /Applications/Nexy.app
default	11:25:30.590218-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d114300 at /Applications/Nexy.app
default	11:25:30.608289-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117000 at /Applications/Nexy.app
default	11:25:30.612314-0500	tccd	Publishing <TCCDEvent: type=Modify, service=kTCCServiceAccessibility, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 0 subscribers: {
}
default	11:25:30.627557-0500	kernel	SK[7]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 5EB7C41D-EF7E-4646-9E2F-7773DE00D413 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.64327,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0xd6caff2a tp_proto=0x06"
default	11:25:30.627641-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:64327<-><IPv4-redacted>:53] interface: utun6 (skipped: 6743)
so_gencnt: 4930529 t_state: SYN_SENT process: Nexy:5436 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 1 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xa8644fb3
default	11:25:30.628252-0500	kernel	tcp connected: [<IPv4-redacted>:64327<-><IPv4-redacted>:53] interface: utun6 (skipped: 6743)
so_gencnt: 4930529 t_state: ESTABLISHED process: Nexy:5436 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 1 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xa8644fb3
default	11:25:30.629050-0500	Nexy	networkd_settings_read_from_file initialized networkd settings by reading plist directly
default	11:25:30.629216-0500	Nexy	networkd_settings_read_from_file initialized networkd settings by reading plist directly
default	11:25:30.629403-0500	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:64327<-><IPv4-redacted>:53] interface: utun6 (skipped: 6743)
so_gencnt: 4930529 t_state: FIN_WAIT_1 process: Nexy:5436 Duration: 0.002 sec Conn_Time: 0.000 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 1.000 ms rttvar: 0.500 ms base rtt: 1 ms so_error: 0 svc/tc: 0 flow: 0xa8644fb3
default	11:25:30.629414-0500	kernel	tcp_connection_summary [<IPv4-redacted>:64327<-><IPv4-redacted>:53] interface: utun6 (skipped: 6743)
so_gencnt: 4930529 t_state: FIN_WAIT_1 process: Nexy:5436 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	11:25:30.629611-0500	kernel	SK[7]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid 51543484-6C2B-4A90-ACFB-3DB590E3E22C flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.64328,dst=<IPv4-redacted>.53,proto=0x06 mask=0x0000003f,hash=0xdb65d803 tp_proto=0x06"
default	11:25:30.629642-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:64328<-><IPv4-redacted>:53] interface: utun6 (skipped: 6743)
so_gencnt: 4930530 t_state: SYN_SENT process: Nexy:5436 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 1 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xb770ff8a
default	11:25:30.629786-0500	kernel	tcp connected: [<IPv4-redacted>:64328<-><IPv4-redacted>:53] interface: utun6 (skipped: 6743)
so_gencnt: 4930530 t_state: ESTABLISHED process: Nexy:5436 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 1 ms error: 0 so_error: 0 svc/tc: 0 flow: 0xb770ff8a
default	11:25:30.630006-0500	kernel	tcp_connection_summary (tcp_usrclosed:3210)[<IPv4-redacted>:64328<-><IPv4-redacted>:53] interface: utun6 (skipped: 6743)
so_gencnt: 4930530 t_state: FIN_WAIT_1 process: Nexy:5436 Duration: 0.000 sec Conn_Time: 0.000 sec bytes in/out: 0/0 pkts in/out: 0/0 pkt rxmit: 0 ooo pkts: 0 dup bytes in: 0 ACKs delayed: 0 delayed ACKs sent: 0
rtt: 1.000 ms rttvar: 0.500 ms base rtt: 1 ms so_error: 0 svc/tc: 0 flow: 0xb770ff8a
default	11:25:30.630017-0500	kernel	tcp_connection_summary [<IPv4-redacted>:64328<-><IPv4-redacted>:53] interface: utun6 (skipped: 6743)
so_gencnt: 4930530 t_state: FIN_WAIT_1 process: Nexy:5436 flowctl: 0us (0x) SYN in/out: 1/1 FIN in/out: 0/0 RST in/out: 0/0 AccECN (client/server): Disabled/Disabled
default	11:25:30.630361-0500	Nexy	nw_path_libinfo_path_check [26E2D554-627F-4AEE-A660-A54D1B955A3A IPv4#c9d96bf7:443 tcp, legacy-socket, attribution: developer]
	libinfo check path: <private>
default	11:25:30.631500-0500	kernel	SK[9]: flow_entry_alloc               fe "0 proc kernel_task(0)Nexy nx_port 1 flow_uuid DD880FC4-09FA-48A1-9011-289F0C62EC37 flags 0x14120<CONNECTED,QOS_MARKING,EXT_PORT,EXT_FLOWID> ipver=4,src=<IPv4-redacted>.64329,dst=<IPv4-redacted>.443,proto=0x06 mask=0x0000003f,hash=0xc78d458b tp_proto=0x06"
default	11:25:30.631531-0500	kernel	tcp connect outgoing: [<IPv4-redacted>:64329<-><IPv4-redacted>:443] interface: utun6 (skipped: 6743)
so_gencnt: 4930531 t_state: SYN_SENT process: Nexy:5436 SYN in/out: 0/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x8beabdba
default	11:25:30.631690-0500	Nexy	server port 0x0000b807, session port 0x0000b807
default	11:25:30.631794-0500	kernel	tcp connected: [<IPv4-redacted>:64329<-><IPv4-redacted>:443] interface: utun6 (skipped: 6743)
so_gencnt: 4930531 t_state: ESTABLISHED process: Nexy:5436 SYN in/out: 1/1 bytes in/out: 0/0 pkts in/out: 0/0 rtt: 0.0 ms rttvar: 250.0 ms base_rtt: 0 ms error: 0 so_error: 0 svc/tc: 0 flow: 0x8beabdba
default	11:25:30.632864-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=393.13423, attribution={accessing={TCCDProcess: identifier=com.nexy.assistant, pid=5436, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=393, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer}, },
default	11:25:30.632894-0500	tccd	requestor: TCCDProcess: identifier=com.apple.WindowServer, pid=393, auid=88, euid=88, binary_path=/System/Library/PrivateFrameworks/SkyLight.framework/Versions/A/Resources/WindowServer is checking access for accessor TCCDProcess: identifier=com.nexy.assistant, pid=5436, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy
default	11:25:30.634180-0500	tccd	AUTHREQ_SUBJECT: msgID=393.13423, subject=com.nexy.assistant,
default	11:25:30.634932-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117000 at /Applications/Nexy.app
default	11:25:30.648418-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d114300 at /Applications/Nexy.app
default	11:25:30.651906-0500	Nexy	[0x8ae118c80] activating connection: mach=true listener=false peer=false name=com.apple.coreservices.launchservicesd
default	11:25:30.654514-0500	Nexy	New connection 0x19a293 main
default	11:25:30.654685-0500	Nexy	[0x8ae118a00] activating connection: mach=true listener=false peer=false name=com.apple.pasteboard.1
default	11:25:30.657687-0500	Nexy	[0x8ae118f00] activating connection: mach=true listener=false peer=false name=com.apple.lsd.mapdb
default	11:25:30.661479-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117000 at /Applications/Nexy.app
default	11:25:30.665462-0500	tccd	Publishing <TCCDEvent: type=Modify, service=kTCCServiceListenEvent, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 0 subscribers: {
}
default	11:25:30.786565-0500	Nexy	[0x8ae118dc0] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
default	11:25:30.787250-0500	tccd	AUTHREQ_ATTRIBUTION: msgID=5436.5, attribution={requesting={TCCDProcess: identifier=com.nexy.assistant, pid=5436, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy}, },
default	11:25:30.788342-0500	Nexy	void _NSDisableAutomaticTerminationAndLog(NSString *) No windows open yet
default	11:25:30.790751-0500	Nexy	CHECKIN: pid=5436
default	11:25:30.794588-0500	tccd	AUTHREQ_SUBJECT: msgID=5436.5, subject=com.nexy.assistant,
default	11:25:30.795744-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117000 at /Applications/Nexy.app
default	11:25:30.798779-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.20318103.20318109(501)>:5436] from originator [osservice<com.apple.coreservices.launchservicesd>:363] with description <RBSAssertionDescriptor| "uielement:5436" ID:398-363-1316835 target:5436 attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"RoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	11:25:30.798877-0500	runningboardd	Assertion 398-363-1316835 (target:[app<application.com.nexy.assistant.20318103.20318109(501)>:5436]) will be created as active
default	11:25:30.799412-0500	runningboardd	[app<application.com.nexy.assistant.20318103.20318109(501)>:5436] Ignoring jetsam update because this process is not memory-managed
default	11:25:30.799439-0500	runningboardd	[app<application.com.nexy.assistant.20318103.20318109(501)>:5436] Ignoring suspend because this process is not lifecycle managed
default	11:25:30.799523-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.20318103.20318109(501)>:5436] from originator [osservice<com.apple.coreservices.launchservicesd>:363] with description <RBSAssertionDescriptor| "uielement:5436" ID:398-363-1316836 target:5436 attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"RoleUserInteractive" sourceEnvironment:"(null)">
	]>
default	11:25:30.799524-0500	runningboardd	[app<application.com.nexy.assistant.20318103.20318109(501)>:5436] Set darwin role to: UserInteractive
default	11:25:30.799576-0500	runningboardd	Assertion 398-363-1316836 (target:[app<application.com.nexy.assistant.20318103.20318109(501)>:5436]) will be created as active
default	11:25:30.799596-0500	runningboardd	[app<application.com.nexy.assistant.20318103.20318109(501)>:5436] Ignoring GPU update because this process is not GPU managed
default	11:25:30.799714-0500	runningboardd	[app<application.com.nexy.assistant.20318103.20318109(501)>:5436] Ignoring memory limit update because this process is not memory-managed
default	11:25:30.798907-0500	launchservicesd	CHECKIN:0x0-0x140c40b 5436 com.nexy.assistant
default	11:25:30.799593-0500	Nexy	CHECKEDIN: pid=5436 asn=0x0-0x140c40b foreground=0
default	11:25:30.800468-0500	loginwindow	-[Application updateInformation] | Got App URL: file:///Applications/Nexy.app/
default	11:25:30.800043-0500	Nexy	[0x8ae119040] activating connection: mach=true listener=false peer=false name=com.apple.lsd.modifydb
default	11:25:30.800573-0500	Nexy	[0x8ae119180] activating connection: mach=false listener=true peer=false name=(anonymous)
default	11:25:30.800580-0500	Nexy	[0x8ae119180] Connection returned listener port: 0x10303
default	11:25:30.801364-0500	Nexy	[0x8ad43c600] activating connection: mach=false listener=false peer=true name=com.apple.xpc.anonymous.0x8ae119180.peer[363].0x8ad43c600
default	11:25:30.803021-0500	loginwindow	-[ApplicationManager checkInAppContext:eventData:] | ApplicationManager: Checked in app : Nexy
default	11:25:30.803649-0500	Nexy	FRONTLOGGING: version 1
default	11:25:30.803924-0500	WindowServer	19a293[CreateApplication]: Process creation: 0x0-0x140c40b (Nexy) connectionID: 19A293 pid: 5436 in session 0x101
default	11:25:30.803699-0500	Nexy	Registered, pid=5436 ASN=0x0,0x140c40b
default	11:25:30.805393-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.20318103.20318109(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	11:25:30.805655-0500	runningboardd	Invalidating assertion 398-363-1316835 (target:[app<application.com.nexy.assistant.20318103.20318109(501)>:5436]) from originator [osservice<com.apple.coreservices.launchservicesd>:363]
default	11:25:30.805936-0500	gamepolicyd	Received state update for 5436 (app<application.com.nexy.assistant.20318103.20318109(501)>, running-active-NotVisible
default	11:25:30.806056-0500	Nexy	[0x8ae119180] Connection returned listener port: 0x10303
default	11:25:30.806402-0500	Nexy	BringForward: pid=5436 asn=0x0-0x140c40b bringForward=0 foreground=0 uiElement=1 launchedByLS=0 modifiersCount=0 allDisabled=0
default	11:25:30.806742-0500	Nexy	Current system appearance, (HLTB: 1), (SLS: 0)
default	11:25:30.808454-0500	Nexy	[0x8ae118dc0] invalidated after the last release of the connection object
default	11:25:30.808582-0500	Nexy	Current system appearance, (HLTB: 1), (SLS: 0)
default	11:25:30.809442-0500	Nexy	Post-registration system appearance: (HLTB: 1)
default	11:25:30.835220-0500	lsd	com.nexy.assistant/Unknown Persona:5:5:1:1:Building bundle record for app
default	11:25:30.835361-0500	lsd	com.nexy.assistant/Unknown Persona:5:5:2:1:Built bundle record for app
default	11:25:30.839924-0500	Nexy	FBSWorkspace: endpoint monitoring is disabled.
default	11:25:30.839932-0500	Nexy	FBSWorkspace: default shell endpoint is disabled.
default	11:25:30.839982-0500	Nexy	Initializing connection
default	11:25:30.840019-0500	Nexy	Removing all cached process handles
default	11:25:30.840045-0500	Nexy	Sending handshake request attempt #1 to server
default	11:25:30.840055-0500	Nexy	Creating connection to com.apple.runningboard
default	11:25:30.840063-0500	Nexy	[0x8ae1192c0] activating connection: mach=true listener=false peer=false name=com.apple.runningboard
default	11:25:30.840403-0500	Nexy	[0x8ae119180] Connection returned listener port: 0x10303
default	11:25:30.840445-0500	runningboardd	Setting client for [app<application.com.nexy.assistant.20318103.20318109(501)>:5436] as ready
default	11:25:30.841097-0500	Nexy	Handshake succeeded
default	11:25:30.841118-0500	Nexy	Identity resolved as app<application.com.nexy.assistant.20318103.20318109(501)>
default	11:25:30.841164-0500	distnoted	register name: com.apple.xctest.FakeForceTouchDevice object: com.nexy.assistant token: 2d00000024 pid: 5436
default	11:25:30.849817-0500	Nexy	[0x8ae119180] Connection returned listener port: 0x10303
default	11:25:30.851051-0500	Nexy	Created a new Process Instance Registry XPC connection (inactive)
default	11:25:30.851063-0500	Nexy	[0x8ae119400] activating connection: mach=true listener=false peer=false name=com.apple.linkd.autoShortcut
default	11:25:30.851130-0500	Nexy	Activated connection to com.apple.linkd.autoShortcut (ApplicationService)
default	11:25:30.851181-0500	Nexy	[0x8ae119680] activating connection: mach=false listener=true peer=false name=(anonymous)
default	11:25:30.853477-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.20318103.20318109(501)>:5436] from originator [osservice<com.apple.coreservices.launchservicesd>:363] with description <RBSAssertionDescriptor| "frontmost:5436" ID:398-363-1316837 target:5436 attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"RoleUserInteractiveFocal" sourceEnvironment:"(null)">
	]>
default	11:25:30.853552-0500	runningboardd	Assertion 398-363-1316837 (target:[app<application.com.nexy.assistant.20318103.20318109(501)>:5436]) will be created as active
default	11:25:30.853657-0500	WindowServer	19a293[SetFrontProcessWithInfo]: [DeferringManager] Updating policy {
    advicePolicy: .frontmost;
    frontmostProcess: 0x0-0x140c40b (Nexy) mainConnectionID: 19A293;
} for reason: updated frontmost process
default	11:25:30.853730-0500	WindowServer	19a293[SetFrontProcessWithInfo]: [DeferringManager] Deferring events from frontmost process PSN 0x0-0x140c40b (Nexy) -> <pid: 5436>
default	11:25:30.853868-0500	WindowServer	new deferring rules for pid:393: [
    [393-BC40]; <keyboardFocus; Nexy:0x0-0x140c40b>; () -> <pid: 5436>; reason: frontmost PSN --> outbound target,
    [393-BC3F]; <keyboardFocus; <frontmost>>; () -> <token: Nexy:0x0-0x140c40b; pid: 393>; reason: frontmost PSN,
    [393-BC3E]; <keyboardFocus>; () -> <token: <frontmost>; pid: 393>; reason: Deferring to <frontmost>
]
default	11:25:30.853909-0500	WindowServer	[keyboardFocus 0x7facf2b20] setRules:forPID(393): [
    [393-BC40]; <keyboardFocus; Nexy:0x0-0x140c40b>; () -> <pid: 5436>; reason: frontmost PSN --> outbound target,
    [393-BC3F]; <keyboardFocus; <frontmost>>; () -> <token: Nexy:0x0-0x140c40b; pid: 393>; reason: frontmost PSN,
    [393-BC3E]; <keyboardFocus>; () -> <token: <frontmost>; pid: 393>; reason: Deferring to <frontmost>
]
default	11:25:30.853944-0500	runningboardd	[app<application.com.nexy.assistant.20318103.20318109(501)>:5436] Ignoring jetsam update because this process is not memory-managed
default	11:25:30.853988-0500	runningboardd	[app<application.com.nexy.assistant.20318103.20318109(501)>:5436] Ignoring suspend because this process is not lifecycle managed
default	11:25:30.854063-0500	runningboardd	[app<application.com.nexy.assistant.20318103.20318109(501)>:5436] Set darwin role to: UserInteractiveFocal
default	11:25:30.854130-0500	runningboardd	[app<application.com.nexy.assistant.20318103.20318109(501)>:5436] Ignoring GPU update because this process is not GPU managed
default	11:25:30.854258-0500	runningboardd	[app<application.com.nexy.assistant.20318103.20318109(501)>:5436] Ignoring memory limit update because this process is not memory-managed
default	11:25:30.854820-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.20318103.20318109(501)>:5436] from originator [osservice<com.apple.coreservices.launchservicesd>:363] with description <RBSAssertionDescriptor| "notification:5436" ID:398-363-1316838 target:5436 attributes:[
	<RBSDomainAttribute| domain:"com.apple.launchservicesd" name:"LSNotification" sourceEnvironment:"(null)">
	]>
default	11:25:30.854922-0500	runningboardd	Assertion 398-363-1316838 (target:[app<application.com.nexy.assistant.20318103.20318109(501)>:5436]) will be created as active
default	11:25:30.855180-0500	WindowServer	chain did update (setDeferringRules) <keyboardFocus; display: null> containsEndOfChain: YES; [
    <token: <frontmost>; pid: 393>,
    <token: Nexy:0x0-0x140c40b; pid: 393>,
    <pid: 5436>
]
default	11:25:30.856278-0500	Nexy	[0x8ae119680] Connection returned listener port: 0x13f03
default	11:25:30.856903-0500	Nexy	Registered process with identifier 5436-1911770
default	11:25:30.858144-0500	Nexy	[0x8ae119900] activating connection: mach=true listener=false peer=false name=com.apple.usernoted.client
default	11:25:30.864171-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.20318103.20318109(501)>: running-active (role: UserInteractiveFocal) (endowments: <private>)
default	11:25:30.864520-0500	runningboardd	[app<application.com.nexy.assistant.20318103.20318109(501)>:5436] Ignoring jetsam update because this process is not memory-managed
default	11:25:30.864532-0500	runningboardd	[app<application.com.nexy.assistant.20318103.20318109(501)>:5436] Ignoring suspend because this process is not lifecycle managed
default	11:25:30.864547-0500	runningboardd	[app<application.com.nexy.assistant.20318103.20318109(501)>:5436] Ignoring GPU update because this process is not GPU managed
default	11:25:30.864648-0500	runningboardd	[app<application.com.nexy.assistant.20318103.20318109(501)>:5436] Ignoring memory limit update because this process is not memory-managed
default	11:25:30.869398-0500	usernoted	Connection com.nexy.assistant with path: /Applications/Nexy.app
default	11:25:30.871361-0500	distnoted	register name: com.apple.nsquiet_safe_quit_give_reason object: com.nexy.assistant token: 3100000032 pid: 5436
default	11:25:30.872570-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.20318103.20318109(501)>: running-active (role: UserInteractiveFocal) (endowments: <private>)
default	11:25:30.881337-0500	Nexy	NSApp cache appearance:
-NSRequiresAquaSystemAppearance: 0
-appearance: (null)
-effectiveAppearance: <NSCompositeAppearance: 0x8ad3894a0
 (
    "<NSAquaAppearance: 0x8ad3890e0>",
    "<NSSystemAppearance: 0x8ad389400>"
)>
default	11:25:30.887499-0500	Nexy	[0x8ae119f40] activating connection: mach=true listener=false peer=false name=com.apple.dock.fullscreen
default	11:25:30.887784-0500	Nexy	[0x8ae11a080] activating connection: mach=true listener=false peer=false name=com.apple.fonts
default	11:25:30.890182-0500	Nexy	(<private>) deleteSearchableItemsWithDomainIdentifiers, protectionClass:(null), domainIdentifiers number:1
default	11:25:30.890419-0500	Nexy	sConnectionName: com.apple.spotlight.IndexAgent
default	11:25:30.890427-0500	Nexy	Start service name com.apple.spotlight.IndexAgent
default	11:25:30.890464-0500	Nexy	[0x8ae119e00] activating connection: mach=true listener=false peer=false name=com.apple.spotlight.IndexAgent
default	11:25:30.890491-0500	Nexy	[C:1] Alloc com.apple.controlcenter.statusitems
default	11:25:30.890533-0500	Nexy	[0x8ae11a1c0] activating connection: mach=false listener=false peer=false name=(anonymous)
default	11:25:30.890594-0500	Nexy	FBSWorkspace registering source: <private>
default	11:25:30.891268-0500	suggestd	SGDSpotlightReceiver: deleting 1 domain identifiers (1 after removing overlaps) for com.nexy.assistant: <private>
default	11:25:30.891637-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	11:25:30.891702-0500	Nexy	<FBSWorkspaceScenesClient:0x8ad389fe0 <private>> attempting immediate handshake from activate
default	11:25:30.891746-0500	Nexy	<FBSWorkspaceScenesClient:0x8ad389fe0 <private>> sent handshake
default	11:25:30.891841-0500	Nexy	Realizing settings extension __NSStatusItemSceneHostSettings__ on FBSSceneSettings
default	11:25:30.894438-0500	Nexy	<FBSWorkspaceScenesClient:0x8ad389fe0 <private>> was invalidated
default	11:25:30.894458-0500	Nexy	FBSWorkspace unregistering source: <private>
default	11:25:30.894825-0500	Nexy	Realizing settings extension __NSStatusItemSceneClientSettings__ on FBSSceneClientSettings
default	11:25:30.896183-0500	Nexy	Realizing settings extension FBSSceneSettingsCore on FBSSceneSettings
default	11:25:30.897443-0500	Nexy	Realizing settings extension FBSSceneClientSettingsCore on FBSSceneClientSettings
default	11:25:30.898228-0500	Nexy	Requesting scene <FBSScene: 0x8ad38a300; com.apple.controlcenter:E8705660-4C84-4963-8B97-C4CE4274765E> from com.apple.controlcenter.statusitems
error	11:25:30.898432-0500	Nexy	Error creating <FBSScene: 0x8ad38a300; com.apple.controlcenter:E8705660-4C84-4963-8B97-C4CE4274765E>: <NSError: 0x8af3bde90; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
default	11:25:30.899657-0500	Nexy	Request for <FBSScene: 0x8ad38a300; com.apple.controlcenter:E8705660-4C84-4963-8B97-C4CE4274765E> complete!
default	11:25:30.905096-0500	Nexy	Warning: the app is using `-[NSStatusBarButton setHighlightsBy:]` to set the highlight behavior. Instead, consider removing that setting. That will enable macOS to highlight the status bar button as appropriate for all configurations (e.g., light, dark, and increased contrast modes).
default	11:25:30.915416-0500	gamepolicyd	Received state update for 5436 (app<application.com.nexy.assistant.20318103.20318109(501)>, running-active-NotVisible
default	11:25:30.921943-0500	Nexy	[0x8ae11a580] activating connection: mach=true listener=false peer=false name=com.apple.coreservices.appleevents
default	11:25:30.922415-0500	Nexy	[0x8ae119180] Connection returned listener port: 0x10303
default	11:25:30.922724-0500	Nexy	SignalReady: pid=5436 asn=0x0-0x140c40b
default	11:25:30.922983-0500	Nexy	SIGNAL: pid=5436 asn=0x0x-0x140c40b
default	11:25:30.923490-0500	loginwindow	-[Application updateInformation] | Got App URL: file:///Applications/Nexy.app/
default	11:25:30.926841-0500	Nexy	void _NSDisableAutomaticTerminationAndLog(NSString *) Restoring windows
default	11:25:30.926846-0500	Nexy	-[NSApplication _reopenWindowsAsNecessaryIncludingRestorableState:withFullFidelity:completionHandler:] shouldRestoreState=1 hasPersistentStateToRestore=0 shouldStillRestoreStateAfterPrompting=0
default	11:25:30.926860-0500	Nexy	[0x8ae118dc0] activating connection: mach=true listener=false peer=false name=com.apple.window_proxies
default	11:25:30.926919-0500	Nexy	[0x8ae118dc0] invalidated because the current process cancelled the connection by calling xpc_connection_cancel()
default	11:25:30.931751-0500	Nexy	void _NSEnableAutomaticTerminationAndLog(NSString *) Restoring windows
default	11:25:30.933670-0500	Nexy	[C:2] Alloc <private>
default	11:25:30.933712-0500	Nexy	[0x8ae118dc0] activating connection: mach=false listener=false peer=false name=(anonymous)
error	11:25:30.933871-0500	kernel	Sandbox: WindowManager(584) deny(1) mach-task-name others [Nexy(5436)]
default	11:25:30.934184-0500	Nexy	[0x8ae11a800] activating connection: mach=false listener=false peer=false name=com.apple.ViewBridgeAuxiliary
default	11:25:30.935311-0500	WindowManager	Connection activated | (5436) Nexy
default	11:25:30.942224-0500	Nexy	[0x8ae11a940] activating connection: mach=false listener=false peer=false name=(anonymous)
default	11:25:30.942673-0500	Nexy	[0x8ae11aa80] activating connection: mach=false listener=true peer=false name=(anonymous)
default	11:25:30.942687-0500	Nexy	[0x8ae11aa80] Connection returned listener port: 0x16103
default	11:25:30.947990-0500	Nexy	[0x8ae11a800] invalidated after the last release of the connection object
default	11:25:30.950126-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.20318103.20318109(501)>:5436] from originator [app<application.com.nexy.assistant.20318103.20318109(501)>:5436] with description <RBSAssertionDescriptor| "AudioHAL" ID:398-5436-1316839 target:5436 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	11:25:30.950184-0500	runningboardd	Assertion 398-5436-1316839 (target:[app<application.com.nexy.assistant.20318103.20318109(501)>:5436]) will be created as active
default	11:25:30.950505-0500	runningboardd	[app<application.com.nexy.assistant.20318103.20318109(501)>:5436] Ignoring jetsam update because this process is not memory-managed
default	11:25:30.950537-0500	runningboardd	[app<application.com.nexy.assistant.20318103.20318109(501)>:5436] Ignoring suspend because this process is not lifecycle managed
default	11:25:30.950582-0500	runningboardd	[app<application.com.nexy.assistant.20318103.20318109(501)>:5436] Ignoring GPU update because this process is not GPU managed
default	11:25:30.950683-0500	runningboardd	[app<application.com.nexy.assistant.20318103.20318109(501)>:5436] Ignoring memory limit update because this process is not memory-managed
default	11:25:30.950896-0500	runningboardd	Invalidating assertion 398-5436-1316839 (target:[app<application.com.nexy.assistant.20318103.20318109(501)>:5436]) from originator [app<application.com.nexy.assistant.20318103.20318109(501)>:5436]
default	11:25:30.951071-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.20318103.20318109(501)>:5436] from originator [app<application.com.nexy.assistant.20318103.20318109(501)>:5436] with description <RBSAssertionDescriptor| "AudioHAL" ID:398-5436-1316840 target:5436 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	11:25:30.951153-0500	runningboardd	Assertion 398-5436-1316840 (target:[app<application.com.nexy.assistant.20318103.20318109(501)>:5436]) will be created as active
default	11:25:30.954840-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.20318103.20318109(501)>: running-active (role: UserInteractiveFocal) (endowments: <private>)
default	11:25:30.955353-0500	gamepolicyd	Received state update for 5436 (app<application.com.nexy.assistant.20318103.20318109(501)>, running-active-NotVisible
default	11:25:30.955395-0500	runningboardd	Invalidating assertion 398-5436-1316840 (target:[app<application.com.nexy.assistant.20318103.20318109(501)>:5436]) from originator [app<application.com.nexy.assistant.20318103.20318109(501)>:5436]
default	11:25:30.955647-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.20318103.20318109(501)>:5436] from originator [app<application.com.nexy.assistant.20318103.20318109(501)>:5436] with description <RBSAssertionDescriptor| "AudioHAL" ID:398-5436-1316842 target:5436 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	11:25:30.955694-0500	runningboardd	Assertion 398-5436-1316842 (target:[app<application.com.nexy.assistant.20318103.20318109(501)>:5436]) will be created as active
default	11:25:30.955975-0500	runningboardd	Invalidating assertion 398-5436-1316842 (target:[app<application.com.nexy.assistant.20318103.20318109(501)>:5436]) from originator [app<application.com.nexy.assistant.20318103.20318109(501)>:5436]
default	11:25:30.956100-0500	runningboardd	Acquiring assertion targeting [app<application.com.nexy.assistant.20318103.20318109(501)>:5436] from originator [app<application.com.nexy.assistant.20318103.20318109(501)>:5436] with description <RBSAssertionDescriptor| "AudioHAL" ID:398-5436-1316843 target:5436 attributes:[
	<RBSDomainAttribute| domain:"com.apple.CoreAudio.HAL" name:"AudioHAL" sourceEnvironment:"(null)">
	]>
default	11:25:30.956144-0500	runningboardd	Assertion 398-5436-1316843 (target:[app<application.com.nexy.assistant.20318103.20318109(501)>:5436]) will be created as active
default	11:25:30.956346-0500	runningboardd	Invalidating assertion 398-5436-1316843 (target:[app<application.com.nexy.assistant.20318103.20318109(501)>:5436]) from originator [app<application.com.nexy.assistant.20318103.20318109(501)>:5436]
default	11:25:31.051667-0500	Nexy	*warn* MailCS ======%%% _setMailMessageAttributes skip:1
default	11:25:31.055928-0500	Nexy	Start service name com.apple.spotlightknowledged
default	11:25:31.056150-0500	runningboardd	[app<application.com.nexy.assistant.20318103.20318109(501)>:5436] Ignoring jetsam update because this process is not memory-managed
default	11:25:31.056169-0500	runningboardd	[app<application.com.nexy.assistant.20318103.20318109(501)>:5436] Ignoring suspend because this process is not lifecycle managed
default	11:25:31.056180-0500	runningboardd	[app<application.com.nexy.assistant.20318103.20318109(501)>:5436] Ignoring GPU update because this process is not GPU managed
default	11:25:31.056200-0500	runningboardd	[app<application.com.nexy.assistant.20318103.20318109(501)>:5436] Ignoring memory limit update because this process is not memory-managed
default	11:25:31.056700-0500	Nexy	[GMS] availability notification token 75
default	11:25:31.061039-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.20318103.20318109(501)>: running-active (role: UserInteractiveFocal) (endowments: <private>)
default	11:25:31.064625-0500	gamepolicyd	Received state update for 5436 (app<application.com.nexy.assistant.20318103.20318109(501)>, running-active-NotVisible
default	11:25:31.184756-0500	Nexy	[0x8ae118b40] activating connection: mach=false listener=false peer=false name=com.apple.hiservices-xpcservice
default	11:25:31.188493-0500	Nexy	+[IMKClient subclass]: chose IMKClient_Modern
default	11:25:31.188524-0500	Nexy	+[IMKInputSession subclass]: chose IMKInputSession_Modern
default	11:25:31.192172-0500	Nexy	[0x8ae11a6c0] activating connection: mach=true listener=false peer=false name=com.apple.inputmethodkit.getxpcendpoint
default	11:25:31.193875-0500	Nexy	[0x8ae11a800] activating connection: mach=true listener=false peer=false name=com.apple.inputmethodkit.getxpcendpoint
default	11:25:31.195050-0500	Nexy	[0x8ae11abc0] activating connection: mach=false listener=false peer=false name=(anonymous)
default	11:25:31.195355-0500	Nexy	[0x8ae11ae40] activating connection: mach=false listener=false peer=false name=(anonymous)
default	11:25:31.195971-0500	DictationIM	setting current input controller = com.nexy.assistant
default	11:25:31.198542-0500	Nexy	[0x8ae11ad00] activating connection: mach=true listener=false peer=false name=com.apple.tccd.system
error	11:25:31.200207-0500	tccd	TCCDProcess: identifier=com.nexy.assistant, pid=5436, auid=501, euid=501, binary_path=/Applications/Nexy.app/Contents/MacOS/Nexy attempted to call TCCAccessRequest for kTCCServiceAccessibility without the recommended com.apple.private.tcc.manager.check-by-audit-token entitlement
default	11:25:31.200333-0500	Nexy	[0x8ae11ad00] invalidated after the last release of the connection object
default	11:25:31.205600-0500	Nexy	void _NSDisableAutomaticTerminationAndLog(NSString *) NSAccessibility Request Received
default	11:25:31.471358-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(49220)
default	11:25:31.471426-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:49220 called from <private>
default	11:25:31.471436-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:49220 called from <private>
default	11:25:31.472685-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(49221)
default	11:25:31.472718-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:49221 called from <private>
default	11:25:31.472744-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:49221 called from <private>
default	11:25:31.495129-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:49220 called from <private>
default	11:25:31.495162-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:49220 called from <private>
default	11:25:31.496587-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(49220)
default	11:25:31.496619-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 2 2, id:49220 called from <private>
default	11:25:31.496629-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 3 3, id:49220 called from <private>
default	11:25:31.499495-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(49221)
default	11:25:31.499540-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:49221 called from <private>
default	11:25:31.499547-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:49221 called from <private>
default	11:25:31.499735-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(49220)
default	11:25:31.499754-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(49220)
default	11:25:31.499763-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 3 3 id:49220 called from <private>
default	11:25:31.499773-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 2 2 id:49220 called from <private>
default	11:25:31.499804-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:49220 called from <private>
default	11:25:31.499880-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:49220 called from <private>
default	11:25:31.501080-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:49220 called from <private>
default	11:25:31.501096-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:49220 called from <private>
default	11:25:31.501236-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(49220)
default	11:25:31.501729-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(49220)
default	11:25:31.519810-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:49220 called from <private>
default	11:25:31.519840-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:49220 called from <private>
default	11:25:31.521049-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 1 1, id:49220 called from <private>
default	11:25:31.521069-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 2 2, id:49220 called from <private>
default	11:25:31.521219-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(49220)
default	11:25:31.532855-0500	Nexy	  HALC_ProxyIOContext.cpp:3410   HALC_IOContext_ResumeIO(49220)
default	11:25:31.533093-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 2 2 id:49220 called from <private>
default	11:25:31.533107-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 1 1 id:49220 called from <private>
default	11:25:31.533217-0500	Nexy	  HALC_ProxyIOContext.cpp:3376   HALC_IOContext_PauseIO(49220)
default	11:25:31.541680-0500	Nexy	  HALC_ProxyIOContext.cpp:1146   HALC_ProxyIOContext::PauseIO: -> 0 0 0, id:49220 called from <private>
default	11:25:31.541729-0500	Nexy	  HALC_ProxyIOContext.cpp:1159   HALC_ProxyIOContext::PauseIO: <- 0 1 1, id:49220 called from <private>
default	11:25:31.541790-0500	Nexy	  HALC_ProxyIOContext.cpp:1193   HALC_ProxyIOContext::ResumeIO: -> 0 1 1 id:49220 called from <private>
default	11:25:31.541861-0500	Nexy	  HALC_ProxyIOContext.cpp:1210   HALC_ProxyIOContext::ResumeIO: <- 0 0 0 id:49220 called from <private>
default	11:25:31.926866-0500	Nexy	FBSWorkspace registering source: <private>
default	11:25:31.926917-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	11:25:31.927027-0500	Nexy	<FBSWorkspaceScenesClient:0x8ad38aee0 <private>> attempting immediate handshake from activate
default	11:25:31.927076-0500	Nexy	<FBSWorkspaceScenesClient:0x8ad38aee0 <private>> sent handshake
default	11:25:31.927552-0500	Nexy	Requesting scene <FBSScene: 0x8ad38af80; com.apple.controlcenter:D132A7FF-64C0-4D09-A104-BDC225EA3670> from com.apple.controlcenter.statusitems
default	11:25:31.927994-0500	Nexy	<FBSWorkspaceScenesClient:0x8ad38aee0 <private>> was invalidated
default	11:25:31.928047-0500	Nexy	FBSWorkspace unregistering source: <private>
error	11:25:31.928152-0500	Nexy	Error creating <FBSScene: 0x8ad38af80; com.apple.controlcenter:D132A7FF-64C0-4D09-A104-BDC225EA3670>: <NSError: 0x8af3c3b10; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	11:25:31.928200-0500	Nexy	No scene exists for identity: com.apple.controlcenter:D132A7FF-64C0-4D09-A104-BDC225EA3670
default	11:25:31.929115-0500	Nexy	Request for <FBSScene: 0x8ad38af80; com.apple.controlcenter:D132A7FF-64C0-4D09-A104-BDC225EA3670> complete!
default	11:25:31.929280-0500	Nexy	Realizing settings extension FBSSceneTransitionContextCore on FBSSceneTransitionContext
default	11:25:31.931538-0500	runningboardd	Invalidating assertion 398-363-1316837 (target:[app<application.com.nexy.assistant.20318103.20318109(501)>:5436]) from originator [osservice<com.apple.coreservices.launchservicesd>:363]
default	11:25:31.932528-0500	Nexy	FBSWorkspace registering source: <private>
default	11:25:31.932553-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	11:25:31.932615-0500	Nexy	<FBSWorkspaceScenesClient:0x8ad38b0c0 <private>> attempting immediate handshake from activate
default	11:25:31.932631-0500	Nexy	<FBSWorkspaceScenesClient:0x8ad38b0c0 <private>> sent handshake
default	11:25:31.932727-0500	Nexy	Realizing settings extension __NSHostedViewSceneSettings__ on FBSSceneSettings
default	11:25:31.933211-0500	Nexy	Realizing settings extension __NSClientHostedViewSceneSettings__ on FBSSceneClientSettings
default	11:25:31.933542-0500	Nexy	Realizing settings extension __NSStatusItemAuxiliaryViewSceneSettings__ on FBSSceneSettings
default	11:25:31.933604-0500	Nexy	Realizing settings extension __NSClientStatusItemAuxiliaryViewSceneSettings__ on FBSSceneClientSettings
default	11:25:31.933969-0500	Nexy	Requesting scene <FBSScene: 0x8ad38b160; com.apple.controlcenter:D132A7FF-64C0-4D09-A104-BDC225EA3670-Aux[1]-NSStatusItemView> from com.apple.controlcenter.statusitems
default	11:25:31.934261-0500	Nexy	Request for <FBSScene: 0x8ad38b160; com.apple.controlcenter:D132A7FF-64C0-4D09-A104-BDC225EA3670-Aux[1]-NSStatusItemView> complete!
default	11:25:31.934963-0500	Nexy	[com.apple.controlcenter:D132A7FF-64C0-4D09-A104-BDC225EA3670-Aux[1]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
default	11:25:31.934987-0500	Nexy	[com.apple.controlcenter:D132A7FF-64C0-4D09-A104-BDC225EA3670-Aux[1]-NSStatusItemView] Dropping transition context because the scene is reconnecting
error	11:25:31.935393-0500	Nexy	scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	11:25:31.935412-0500	Nexy	[com.apple.controlcenter:D132A7FF-64C0-4D09-A104-BDC225EA3670] No matching scene to invalidate for this identity.
error	11:25:31.935986-0500	Nexy	Unhandled disconnected scene <private>
error	11:25:31.936130-0500	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
default	11:25:31.938460-0500	Nexy	void _updateToReflectAutomaticTerminationState(void) Setting _kLSApplicationWouldBeTerminatedByTALKey=1
default	11:25:31.940509-0500	Nexy	<FBSWorkspaceScenesClient:0x8ad38b0c0 <private>> was invalidated
default	11:25:31.940541-0500	Nexy	FBSWorkspace unregistering source: <private>
error	11:25:31.940612-0500	Nexy	Error creating <FBSScene: 0x8ad38b160; com.apple.controlcenter:D132A7FF-64C0-4D09-A104-BDC225EA3670-Aux[1]-NSStatusItemView>: <NSError: 0x8af3bee80; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	11:25:31.940628-0500	Nexy	No scene exists for identity: com.apple.controlcenter:D132A7FF-64C0-4D09-A104-BDC225EA3670-Aux[1]-NSStatusItemView
error	11:25:31.940646-0500	Nexy	[com.apple.controlcenter:D132A7FF-64C0-4D09-A104-BDC225EA3670-Aux[1]-NSStatusItemView] No matching scene to invalidate for this identity.
error	11:25:31.940752-0500	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
error	11:25:31.940784-0500	Nexy	auxiliary scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
default	11:25:32.036592-0500	runningboardd	[app<application.com.nexy.assistant.20318103.20318109(501)>:5436] Ignoring jetsam update because this process is not memory-managed
default	11:25:32.036608-0500	runningboardd	[app<application.com.nexy.assistant.20318103.20318109(501)>:5436] Ignoring suspend because this process is not lifecycle managed
default	11:25:32.036638-0500	runningboardd	[app<application.com.nexy.assistant.20318103.20318109(501)>:5436] Set darwin role to: UserInteractive
default	11:25:32.036648-0500	runningboardd	[app<application.com.nexy.assistant.20318103.20318109(501)>:5436] Ignoring GPU update because this process is not GPU managed
default	11:25:32.036669-0500	runningboardd	[app<application.com.nexy.assistant.20318103.20318109(501)>:5436] Ignoring memory limit update because this process is not memory-managed
default	11:25:32.040736-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.20318103.20318109(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	11:25:32.042860-0500	gamepolicyd	Received state update for 5436 (app<application.com.nexy.assistant.20318103.20318109(501)>, running-active-NotVisible
default	11:25:32.396122-0500	DictationIM	setting current input controller = com.nexy.assistant
default	11:25:32.936651-0500	Nexy	FBSWorkspace registering source: <private>
default	11:25:32.936675-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	11:25:32.936728-0500	Nexy	<FBSWorkspaceScenesClient:0x8ad38b160 <private>> attempting immediate handshake from activate
default	11:25:32.936753-0500	Nexy	<FBSWorkspaceScenesClient:0x8ad38b160 <private>> sent handshake
default	11:25:32.936949-0500	Nexy	Requesting scene <FBSScene: 0x8ad38b2a0; com.apple.controlcenter:3E028D47-FD43-4949-B73F-0D306FEB700E> from com.apple.controlcenter.statusitems
default	11:25:32.937110-0500	Nexy	Request for <FBSScene: 0x8ad38b2a0; com.apple.controlcenter:3E028D47-FD43-4949-B73F-0D306FEB700E> complete!
default	11:25:32.937263-0500	Nexy	<FBSWorkspaceScenesClient:0x8ad38b160 <private>> was invalidated
default	11:25:32.937283-0500	Nexy	FBSWorkspace unregistering source: <private>
error	11:25:32.937326-0500	Nexy	Error creating <FBSScene: 0x8ad38b2a0; com.apple.controlcenter:3E028D47-FD43-4949-B73F-0D306FEB700E>: <NSError: 0x8af3c3ba0; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	11:25:32.937341-0500	Nexy	No scene exists for identity: com.apple.controlcenter:3E028D47-FD43-4949-B73F-0D306FEB700E
default	11:25:32.937369-0500	Nexy	FBSWorkspace registering source: <private>
default	11:25:32.937381-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	11:25:32.937417-0500	Nexy	<FBSWorkspaceScenesClient:0x8ad38b020 <private>> attempting immediate handshake from activate
default	11:25:32.937432-0500	Nexy	<FBSWorkspaceScenesClient:0x8ad38b020 <private>> sent handshake
default	11:25:32.937534-0500	Nexy	Requesting scene <FBSScene: 0x8ad38af80; com.apple.controlcenter:3E028D47-FD43-4949-B73F-0D306FEB700E-Aux[2]-NSStatusItemView> from com.apple.controlcenter.statusitems
default	11:25:32.937658-0500	Nexy	Request for <FBSScene: 0x8ad38af80; com.apple.controlcenter:3E028D47-FD43-4949-B73F-0D306FEB700E-Aux[2]-NSStatusItemView> complete!
default	11:25:32.937776-0500	Nexy	<FBSWorkspaceScenesClient:0x8ad38b020 <private>> was invalidated
default	11:25:32.937797-0500	Nexy	FBSWorkspace unregistering source: <private>
error	11:25:32.937836-0500	Nexy	Error creating <FBSScene: 0x8ad38af80; com.apple.controlcenter:3E028D47-FD43-4949-B73F-0D306FEB700E-Aux[2]-NSStatusItemView>: <NSError: 0x8af3c3870; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	11:25:32.937848-0500	Nexy	No scene exists for identity: com.apple.controlcenter:3E028D47-FD43-4949-B73F-0D306FEB700E-Aux[2]-NSStatusItemView
default	11:25:32.937972-0500	Nexy	[com.apple.controlcenter:3E028D47-FD43-4949-B73F-0D306FEB700E-Aux[2]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
error	11:25:32.938128-0500	Nexy	scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	11:25:32.938143-0500	Nexy	[com.apple.controlcenter:3E028D47-FD43-4949-B73F-0D306FEB700E] No matching scene to invalidate for this identity.
error	11:25:32.938163-0500	Nexy	auxiliary scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	11:25:32.938173-0500	Nexy	[com.apple.controlcenter:3E028D47-FD43-4949-B73F-0D306FEB700E-Aux[2]-NSStatusItemView] No matching scene to invalidate for this identity.
error	11:25:32.938395-0500	Nexy	Unhandled disconnected scene <private>
error	11:25:32.938447-0500	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
error	11:25:32.938496-0500	Nexy	Unhandled disconnected auxiliary scene <private>
error	11:25:32.938528-0500	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
default	11:25:33.939537-0500	Nexy	<FBSWorkspaceScenesClient:0x8ad38af80 <private>> sent handshake
default	11:25:33.939758-0500	Nexy	Requesting scene <FBSScene: 0x8ad38b2a0; com.apple.controlcenter:701B7C61-1102-4165-931E-8AF79DA023B2> from com.apple.controlcenter.statusitems
default	11:25:33.939995-0500	Nexy	Request for <FBSScene: 0x8ad38b2a0; com.apple.controlcenter:701B7C61-1102-4165-931E-8AF79DA023B2> complete!
default	11:25:33.940242-0500	Nexy	<FBSWorkspaceScenesClient:0x8ad38af80 <private>> was invalidated
default	11:25:33.940278-0500	Nexy	FBSWorkspace unregistering source: <private>
default	11:25:33.940326-0500	Nexy	FBSWorkspace registering source: <private>
default	11:25:33.940351-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	11:25:33.940402-0500	Nexy	<FBSWorkspaceScenesClient:0x8ad38aee0 <private>> attempting immediate handshake from activate
default	11:25:33.940423-0500	Nexy	<FBSWorkspaceScenesClient:0x8ad38aee0 <private>> sent handshake
error	11:25:33.940490-0500	Nexy	Error creating <FBSScene: 0x8ad38b2a0; com.apple.controlcenter:701B7C61-1102-4165-931E-8AF79DA023B2>: <NSError: 0x8af3c3b70; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	11:25:33.940510-0500	Nexy	No scene exists for identity: com.apple.controlcenter:701B7C61-1102-4165-931E-8AF79DA023B2
default	11:25:33.940562-0500	Nexy	Requesting scene <FBSScene: 0x8ad38b160; com.apple.controlcenter:701B7C61-1102-4165-931E-8AF79DA023B2-Aux[3]-NSStatusItemView> from com.apple.controlcenter.statusitems
default	11:25:33.940712-0500	Nexy	Request for <FBSScene: 0x8ad38b160; com.apple.controlcenter:701B7C61-1102-4165-931E-8AF79DA023B2-Aux[3]-NSStatusItemView> complete!
default	11:25:33.940927-0500	Nexy	<FBSWorkspaceScenesClient:0x8ad38aee0 <private>> was invalidated
default	11:25:33.940953-0500	Nexy	FBSWorkspace unregistering source: <private>
error	11:25:33.941009-0500	Nexy	Error creating <FBSScene: 0x8ad38b160; com.apple.controlcenter:701B7C61-1102-4165-931E-8AF79DA023B2-Aux[3]-NSStatusItemView>: <NSError: 0x8af3c3f60; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	11:25:33.941026-0500	Nexy	No scene exists for identity: com.apple.controlcenter:701B7C61-1102-4165-931E-8AF79DA023B2-Aux[3]-NSStatusItemView
default	11:25:33.941159-0500	Nexy	[com.apple.controlcenter:701B7C61-1102-4165-931E-8AF79DA023B2-Aux[3]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
error	11:25:33.941392-0500	Nexy	scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	11:25:33.941411-0500	Nexy	[com.apple.controlcenter:701B7C61-1102-4165-931E-8AF79DA023B2] No matching scene to invalidate for this identity.
error	11:25:33.941441-0500	Nexy	auxiliary scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	11:25:33.941456-0500	Nexy	[com.apple.controlcenter:701B7C61-1102-4165-931E-8AF79DA023B2-Aux[3]-NSStatusItemView] No matching scene to invalidate for this identity.
error	11:25:33.941812-0500	Nexy	Unhandled disconnected scene <private>
error	11:25:33.941884-0500	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
error	11:25:33.941939-0500	Nexy	Unhandled disconnected auxiliary scene <private>
error	11:25:33.941972-0500	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
default	11:25:34.942672-0500	Nexy	FBSWorkspace registering source: <private>
default	11:25:34.942696-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	11:25:34.942751-0500	Nexy	<FBSWorkspaceScenesClient:0x8ad38b160 <private>> attempting immediate handshake from activate
default	11:25:34.942774-0500	Nexy	<FBSWorkspaceScenesClient:0x8ad38b160 <private>> sent handshake
default	11:25:34.942956-0500	Nexy	Requesting scene <FBSScene: 0x8ad38b2a0; com.apple.controlcenter:771D3AF0-0F4E-4B12-A3EA-4F447A9C9ADF> from com.apple.controlcenter.statusitems
default	11:25:34.943121-0500	Nexy	Request for <FBSScene: 0x8ad38b2a0; com.apple.controlcenter:771D3AF0-0F4E-4B12-A3EA-4F447A9C9ADF> complete!
default	11:25:34.943397-0500	Nexy	<FBSWorkspaceScenesClient:0x8ad38b160 <private>> was invalidated
default	11:25:34.943420-0500	Nexy	FBSWorkspace unregistering source: <private>
error	11:25:34.943505-0500	Nexy	Error creating <FBSScene: 0x8ad38b2a0; com.apple.controlcenter:771D3AF0-0F4E-4B12-A3EA-4F447A9C9ADF>: <NSError: 0x8af3c3ea0; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	11:25:34.943521-0500	Nexy	No scene exists for identity: com.apple.controlcenter:771D3AF0-0F4E-4B12-A3EA-4F447A9C9ADF
default	11:25:34.943550-0500	Nexy	Requesting scene <FBSScene: 0x8ad38aee0; com.apple.controlcenter:771D3AF0-0F4E-4B12-A3EA-4F447A9C9ADF-Aux[4]-NSStatusItemView> from com.apple.controlcenter.statusitems
error	11:25:34.943645-0500	Nexy	Error creating <FBSScene: 0x8ad38aee0; com.apple.controlcenter:771D3AF0-0F4E-4B12-A3EA-4F447A9C9ADF-Aux[4]-NSStatusItemView>: <NSError: 0x8af3c3b40; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
default	11:25:34.943684-0500	Nexy	Request for <FBSScene: 0x8ad38aee0; com.apple.controlcenter:771D3AF0-0F4E-4B12-A3EA-4F447A9C9ADF-Aux[4]-NSStatusItemView> complete!
error	11:25:34.943823-0500	Nexy	scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	11:25:34.943841-0500	Nexy	[com.apple.controlcenter:771D3AF0-0F4E-4B12-A3EA-4F447A9C9ADF] No matching scene to invalidate for this identity.
error	11:25:34.943861-0500	Nexy	auxiliary scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	11:25:34.943888-0500	Nexy	Unhandled disconnected scene <private>
error	11:25:34.943929-0500	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
default	11:25:35.945338-0500	Nexy	FBSWorkspace registering source: <private>
default	11:25:35.945398-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	11:25:35.945530-0500	Nexy	<FBSWorkspaceScenesClient:0x8ad38aee0 <private>> attempting immediate handshake from activate
default	11:25:35.945580-0500	Nexy	<FBSWorkspaceScenesClient:0x8ad38aee0 <private>> sent handshake
default	11:25:35.946038-0500	Nexy	Requesting scene <FBSScene: 0x8ad38b2a0; com.apple.controlcenter:CCFCF0EF-181B-498C-9E51-B4A8CEEBB7EE> from com.apple.controlcenter.statusitems
default	11:25:35.946444-0500	Nexy	Request for <FBSScene: 0x8ad38b2a0; com.apple.controlcenter:CCFCF0EF-181B-498C-9E51-B4A8CEEBB7EE> complete!
default	11:25:35.947000-0500	Nexy	<FBSWorkspaceScenesClient:0x8ad38aee0 <private>> was invalidated
default	11:25:35.947057-0500	Nexy	FBSWorkspace unregistering source: <private>
default	11:25:35.947149-0500	Nexy	FBSWorkspace registering source: <private>
default	11:25:35.947185-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	11:25:35.947277-0500	Nexy	<FBSWorkspaceScenesClient:0x8ad38b160 <private>> attempting immediate handshake from activate
default	11:25:35.947316-0500	Nexy	<FBSWorkspaceScenesClient:0x8ad38b160 <private>> sent handshake
error	11:25:35.947437-0500	Nexy	Error creating <FBSScene: 0x8ad38b2a0; com.apple.controlcenter:CCFCF0EF-181B-498C-9E51-B4A8CEEBB7EE>: <NSError: 0x8af3c14a0; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	11:25:35.947478-0500	Nexy	No scene exists for identity: com.apple.controlcenter:CCFCF0EF-181B-498C-9E51-B4A8CEEBB7EE
default	11:25:35.947586-0500	Nexy	Requesting scene <FBSScene: 0x8ad38af80; com.apple.controlcenter:CCFCF0EF-181B-498C-9E51-B4A8CEEBB7EE-Aux[5]-NSStatusItemView> from com.apple.controlcenter.statusitems
default	11:25:35.947900-0500	Nexy	Request for <FBSScene: 0x8ad38af80; com.apple.controlcenter:CCFCF0EF-181B-498C-9E51-B4A8CEEBB7EE-Aux[5]-NSStatusItemView> complete!
default	11:25:35.948235-0500	Nexy	<FBSWorkspaceScenesClient:0x8ad38b160 <private>> was invalidated
default	11:25:35.948280-0500	Nexy	FBSWorkspace unregistering source: <private>
error	11:25:35.948378-0500	Nexy	Error creating <FBSScene: 0x8ad38af80; com.apple.controlcenter:CCFCF0EF-181B-498C-9E51-B4A8CEEBB7EE-Aux[5]-NSStatusItemView>: <NSError: 0x8af3c1680; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	11:25:35.948410-0500	Nexy	No scene exists for identity: com.apple.controlcenter:CCFCF0EF-181B-498C-9E51-B4A8CEEBB7EE-Aux[5]-NSStatusItemView
default	11:25:35.948630-0500	Nexy	[com.apple.controlcenter:CCFCF0EF-181B-498C-9E51-B4A8CEEBB7EE-Aux[5]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
error	11:25:35.949028-0500	Nexy	scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	11:25:35.949063-0500	Nexy	[com.apple.controlcenter:CCFCF0EF-181B-498C-9E51-B4A8CEEBB7EE] No matching scene to invalidate for this identity.
error	11:25:35.949119-0500	Nexy	auxiliary scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	11:25:35.949146-0500	Nexy	[com.apple.controlcenter:CCFCF0EF-181B-498C-9E51-B4A8CEEBB7EE-Aux[5]-NSStatusItemView] No matching scene to invalidate for this identity.
error	11:25:35.949700-0500	Nexy	Unhandled disconnected scene <private>
error	11:25:35.949841-0500	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
error	11:25:35.949930-0500	Nexy	Unhandled disconnected auxiliary scene <private>
error	11:25:35.949995-0500	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
default	11:25:36.067996-0500	runningboardd	Assertion did invalidate due to timeout: 398-363-1316838 (target:[app<application.com.nexy.assistant.20318103.20318109(501)>:5436])
default	11:25:36.264247-0500	runningboardd	[app<application.com.nexy.assistant.20318103.20318109(501)>:5436] Ignoring jetsam update because this process is not memory-managed
default	11:25:36.264271-0500	runningboardd	[app<application.com.nexy.assistant.20318103.20318109(501)>:5436] Ignoring suspend because this process is not lifecycle managed
default	11:25:36.264291-0500	runningboardd	[app<application.com.nexy.assistant.20318103.20318109(501)>:5436] Ignoring GPU update because this process is not GPU managed
default	11:25:36.264321-0500	runningboardd	[app<application.com.nexy.assistant.20318103.20318109(501)>:5436] Ignoring memory limit update because this process is not memory-managed
default	11:25:36.271631-0500	runningboardd	Calculated state for app<application.com.nexy.assistant.20318103.20318109(501)>: running-active (role: UserInteractive) (endowments: <private>)
default	11:25:36.272293-0500	gamepolicyd	Received state update for 5436 (app<application.com.nexy.assistant.20318103.20318109(501)>, running-active-NotVisible
default	11:25:36.950640-0500	Nexy	FBSWorkspace registering source: <private>
default	11:25:36.950699-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	11:25:36.950829-0500	Nexy	<FBSWorkspaceScenesClient:0x8ad38af80 <private>> attempting immediate handshake from activate
default	11:25:36.950877-0500	Nexy	<FBSWorkspaceScenesClient:0x8ad38af80 <private>> sent handshake
default	11:25:36.951309-0500	Nexy	Requesting scene <FBSScene: 0x8ad38b2a0; com.apple.controlcenter:D84AD3BC-77FF-489F-AD3B-F07CBEF7E036> from com.apple.controlcenter.statusitems
default	11:25:36.951709-0500	Nexy	Request for <FBSScene: 0x8ad38b2a0; com.apple.controlcenter:D84AD3BC-77FF-489F-AD3B-F07CBEF7E036> complete!
default	11:25:36.952167-0500	Nexy	<FBSWorkspaceScenesClient:0x8ad38af80 <private>> was invalidated
default	11:25:36.952218-0500	Nexy	FBSWorkspace unregistering source: <private>
default	11:25:36.952301-0500	Nexy	FBSWorkspace registering source: <private>
default	11:25:36.952336-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	11:25:36.952419-0500	Nexy	<FBSWorkspaceScenesClient:0x8ad38b160 <private>> attempting immediate handshake from activate
default	11:25:36.952455-0500	Nexy	<FBSWorkspaceScenesClient:0x8ad38b160 <private>> sent handshake
error	11:25:36.952564-0500	Nexy	Error creating <FBSScene: 0x8ad38b2a0; com.apple.controlcenter:D84AD3BC-77FF-489F-AD3B-F07CBEF7E036>: <NSError: 0x8af3c0f90; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	11:25:36.952595-0500	Nexy	No scene exists for identity: com.apple.controlcenter:D84AD3BC-77FF-489F-AD3B-F07CBEF7E036
default	11:25:36.952738-0500	Nexy	Requesting scene <FBSScene: 0x8ad38aee0; com.apple.controlcenter:D84AD3BC-77FF-489F-AD3B-F07CBEF7E036-Aux[6]-NSStatusItemView> from com.apple.controlcenter.statusitems
default	11:25:36.953087-0500	Nexy	Request for <FBSScene: 0x8ad38aee0; com.apple.controlcenter:D84AD3BC-77FF-489F-AD3B-F07CBEF7E036-Aux[6]-NSStatusItemView> complete!
default	11:25:36.953497-0500	Nexy	<FBSWorkspaceScenesClient:0x8ad38b160 <private>> was invalidated
default	11:25:36.953541-0500	Nexy	FBSWorkspace unregistering source: <private>
error	11:25:36.953634-0500	Nexy	Error creating <FBSScene: 0x8ad38aee0; com.apple.controlcenter:D84AD3BC-77FF-489F-AD3B-F07CBEF7E036-Aux[6]-NSStatusItemView>: <NSError: 0x8af3c3e40; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	11:25:36.953670-0500	Nexy	No scene exists for identity: com.apple.controlcenter:D84AD3BC-77FF-489F-AD3B-F07CBEF7E036-Aux[6]-NSStatusItemView
default	11:25:36.953802-0500	Nexy	[com.apple.controlcenter:D84AD3BC-77FF-489F-AD3B-F07CBEF7E036-Aux[6]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
error	11:25:36.954225-0500	Nexy	scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	11:25:36.954260-0500	Nexy	[com.apple.controlcenter:D84AD3BC-77FF-489F-AD3B-F07CBEF7E036] No matching scene to invalidate for this identity.
error	11:25:36.954334-0500	Nexy	auxiliary scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	11:25:36.954364-0500	Nexy	[com.apple.controlcenter:D84AD3BC-77FF-489F-AD3B-F07CBEF7E036-Aux[6]-NSStatusItemView] No matching scene to invalidate for this identity.
error	11:25:36.954898-0500	Nexy	Unhandled disconnected scene <private>
error	11:25:36.954984-0500	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
error	11:25:36.955039-0500	Nexy	Unhandled disconnected auxiliary scene <private>
error	11:25:36.955068-0500	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
default	11:25:37.049362-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d117000 at /Applications/Nexy.app
default	11:25:37.063088-0500	tccd	-[TCCDAccessIdentity staticCode]: static code for: identifier com.nexy.assistant, type: 0: 0x97d114000 at /Applications/Nexy.app
default	11:25:37.071753-0500	tccd	Publishing <TCCDEvent: type=Modify, service=kTCCServiceListenEvent, identifier_type=Bundle ID, identifier=com.nexy.assistant> to 0 subscribers: {
}
default	11:25:37.955879-0500	Nexy	FBSWorkspace registering source: <private>
default	11:25:37.955941-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	11:25:37.956084-0500	Nexy	<FBSWorkspaceScenesClient:0x8ad38aee0 <private>> attempting immediate handshake from activate
default	11:25:37.956134-0500	Nexy	<FBSWorkspaceScenesClient:0x8ad38aee0 <private>> sent handshake
default	11:25:37.956613-0500	Nexy	Requesting scene <FBSScene: 0x8ad38b2a0; com.apple.controlcenter:347E6D2A-C78B-4320-868E-A5A95FD2020E> from com.apple.controlcenter.statusitems
default	11:25:37.957022-0500	Nexy	Request for <FBSScene: 0x8ad38b2a0; com.apple.controlcenter:347E6D2A-C78B-4320-868E-A5A95FD2020E> complete!
default	11:25:37.957520-0500	Nexy	<FBSWorkspaceScenesClient:0x8ad38aee0 <private>> was invalidated
default	11:25:37.957580-0500	Nexy	FBSWorkspace unregistering source: <private>
default	11:25:37.957673-0500	Nexy	FBSWorkspace registering source: <private>
default	11:25:37.957710-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	11:25:37.957803-0500	Nexy	<FBSWorkspaceScenesClient:0x8ad38b200 <private>> attempting immediate handshake from activate
default	11:25:37.957844-0500	Nexy	<FBSWorkspaceScenesClient:0x8ad38b200 <private>> sent handshake
error	11:25:37.957966-0500	Nexy	Error creating <FBSScene: 0x8ad38b2a0; com.apple.controlcenter:347E6D2A-C78B-4320-868E-A5A95FD2020E>: <NSError: 0x8af3c1740; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	11:25:37.958003-0500	Nexy	No scene exists for identity: com.apple.controlcenter:347E6D2A-C78B-4320-868E-A5A95FD2020E
default	11:25:37.958116-0500	Nexy	Requesting scene <FBSScene: 0x8ad38af80; com.apple.controlcenter:347E6D2A-C78B-4320-868E-A5A95FD2020E-Aux[7]-NSStatusItemView> from com.apple.controlcenter.statusitems
default	11:25:37.958452-0500	Nexy	Request for <FBSScene: 0x8ad38af80; com.apple.controlcenter:347E6D2A-C78B-4320-868E-A5A95FD2020E-Aux[7]-NSStatusItemView> complete!
default	11:25:37.958739-0500	Nexy	<FBSWorkspaceScenesClient:0x8ad38b200 <private>> was invalidated
default	11:25:37.958786-0500	Nexy	FBSWorkspace unregistering source: <private>
error	11:25:37.958890-0500	Nexy	Error creating <FBSScene: 0x8ad38af80; com.apple.controlcenter:347E6D2A-C78B-4320-868E-A5A95FD2020E-Aux[7]-NSStatusItemView>: <NSError: 0x8af3c3810; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	11:25:37.958924-0500	Nexy	No scene exists for identity: com.apple.controlcenter:347E6D2A-C78B-4320-868E-A5A95FD2020E-Aux[7]-NSStatusItemView
default	11:25:37.959201-0500	Nexy	[com.apple.controlcenter:347E6D2A-C78B-4320-868E-A5A95FD2020E-Aux[7]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
error	11:25:37.959606-0500	Nexy	scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	11:25:37.959641-0500	Nexy	[com.apple.controlcenter:347E6D2A-C78B-4320-868E-A5A95FD2020E] No matching scene to invalidate for this identity.
error	11:25:37.959697-0500	Nexy	auxiliary scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	11:25:37.959727-0500	Nexy	[com.apple.controlcenter:347E6D2A-C78B-4320-868E-A5A95FD2020E-Aux[7]-NSStatusItemView] No matching scene to invalidate for this identity.
error	11:25:37.960289-0500	Nexy	Unhandled disconnected scene <private>
error	11:25:37.960408-0500	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
error	11:25:37.960498-0500	Nexy	Unhandled disconnected auxiliary scene <private>
error	11:25:37.960560-0500	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
default	11:25:38.960601-0500	Nexy	FBSWorkspace registering source: <private>
default	11:25:38.960663-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	11:25:38.960809-0500	Nexy	<FBSWorkspaceScenesClient:0x8ad38af80 <private>> attempting immediate handshake from activate
default	11:25:38.960864-0500	Nexy	<FBSWorkspaceScenesClient:0x8ad38af80 <private>> sent handshake
default	11:25:38.961338-0500	Nexy	Requesting scene <FBSScene: 0x8ad38b2a0; com.apple.controlcenter:434FB5C7-DB64-47E7-BF2C-22FC83F61AC6> from com.apple.controlcenter.statusitems
default	11:25:38.961740-0500	Nexy	Request for <FBSScene: 0x8ad38b2a0; com.apple.controlcenter:434FB5C7-DB64-47E7-BF2C-22FC83F61AC6> complete!
default	11:25:38.962266-0500	Nexy	<FBSWorkspaceScenesClient:0x8ad38af80 <private>> was invalidated
default	11:25:38.962327-0500	Nexy	FBSWorkspace unregistering source: <private>
default	11:25:38.962423-0500	Nexy	FBSWorkspace registering source: <private>
default	11:25:38.962457-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	11:25:38.962558-0500	Nexy	<FBSWorkspaceScenesClient:0x8ad38b0c0 <private>> attempting immediate handshake from activate
default	11:25:38.962625-0500	Nexy	<FBSWorkspaceScenesClient:0x8ad38b0c0 <private>> sent handshake
error	11:25:38.962748-0500	Nexy	Error creating <FBSScene: 0x8ad38b2a0; com.apple.controlcenter:434FB5C7-DB64-47E7-BF2C-22FC83F61AC6>: <NSError: 0x8af3c3000; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	11:25:38.962780-0500	Nexy	No scene exists for identity: com.apple.controlcenter:434FB5C7-DB64-47E7-BF2C-22FC83F61AC6
default	11:25:38.962913-0500	Nexy	Requesting scene <FBSScene: 0x8ad38aee0; com.apple.controlcenter:434FB5C7-DB64-47E7-BF2C-22FC83F61AC6-Aux[8]-NSStatusItemView> from com.apple.controlcenter.statusitems
default	11:25:38.963201-0500	Nexy	Request for <FBSScene: 0x8ad38aee0; com.apple.controlcenter:434FB5C7-DB64-47E7-BF2C-22FC83F61AC6-Aux[8]-NSStatusItemView> complete!
default	11:25:38.963488-0500	Nexy	<FBSWorkspaceScenesClient:0x8ad38b0c0 <private>> was invalidated
default	11:25:38.963514-0500	Nexy	FBSWorkspace unregistering source: <private>
error	11:25:38.963562-0500	Nexy	Error creating <FBSScene: 0x8ad38aee0; com.apple.controlcenter:434FB5C7-DB64-47E7-BF2C-22FC83F61AC6-Aux[8]-NSStatusItemView>: <NSError: 0x8af3c1590; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	11:25:38.963574-0500	Nexy	No scene exists for identity: com.apple.controlcenter:434FB5C7-DB64-47E7-BF2C-22FC83F61AC6-Aux[8]-NSStatusItemView
default	11:25:38.963737-0500	Nexy	[com.apple.controlcenter:434FB5C7-DB64-47E7-BF2C-22FC83F61AC6-Aux[8]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
error	11:25:38.963959-0500	Nexy	scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	11:25:38.963979-0500	Nexy	[com.apple.controlcenter:434FB5C7-DB64-47E7-BF2C-22FC83F61AC6] No matching scene to invalidate for this identity.
error	11:25:38.964005-0500	Nexy	auxiliary scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	11:25:38.964019-0500	Nexy	[com.apple.controlcenter:434FB5C7-DB64-47E7-BF2C-22FC83F61AC6-Aux[8]-NSStatusItemView] No matching scene to invalidate for this identity.
error	11:25:38.964365-0500	Nexy	Unhandled disconnected scene <private>
error	11:25:38.964432-0500	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
error	11:25:38.964479-0500	Nexy	Unhandled disconnected auxiliary scene <private>
error	11:25:38.964510-0500	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
default	11:25:39.965482-0500	Nexy	FBSWorkspace registering source: <private>
default	11:25:39.965524-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	11:25:39.965619-0500	Nexy	<FBSWorkspaceScenesClient:0x8ad38aee0 <private>> attempting immediate handshake from activate
default	11:25:39.965651-0500	Nexy	<FBSWorkspaceScenesClient:0x8ad38aee0 <private>> sent handshake
default	11:25:39.965974-0500	Nexy	Requesting scene <FBSScene: 0x8ad38b2a0; com.apple.controlcenter:0D24F8FF-D07C-49D5-978C-02DA1937C4E6> from com.apple.controlcenter.statusitems
default	11:25:39.966242-0500	Nexy	Request for <FBSScene: 0x8ad38b2a0; com.apple.controlcenter:0D24F8FF-D07C-49D5-978C-02DA1937C4E6> complete!
default	11:25:39.966551-0500	Nexy	<FBSWorkspaceScenesClient:0x8ad38aee0 <private>> was invalidated
default	11:25:39.966583-0500	Nexy	FBSWorkspace unregistering source: <private>
default	11:25:39.966634-0500	Nexy	FBSWorkspace registering source: <private>
default	11:25:39.966650-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	11:25:39.966698-0500	Nexy	<FBSWorkspaceScenesClient:0x8ad38b160 <private>> attempting immediate handshake from activate
default	11:25:39.966720-0500	Nexy	<FBSWorkspaceScenesClient:0x8ad38b160 <private>> sent handshake
error	11:25:39.966782-0500	Nexy	Error creating <FBSScene: 0x8ad38b2a0; com.apple.controlcenter:0D24F8FF-D07C-49D5-978C-02DA1937C4E6>: <NSError: 0x8af3c2fd0; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	11:25:39.966800-0500	Nexy	No scene exists for identity: com.apple.controlcenter:0D24F8FF-D07C-49D5-978C-02DA1937C4E6
default	11:25:39.966870-0500	Nexy	Requesting scene <FBSScene: 0x8ad38af80; com.apple.controlcenter:0D24F8FF-D07C-49D5-978C-02DA1937C4E6-Aux[9]-NSStatusItemView> from com.apple.controlcenter.statusitems
default	11:25:39.967056-0500	Nexy	Request for <FBSScene: 0x8ad38af80; com.apple.controlcenter:0D24F8FF-D07C-49D5-978C-02DA1937C4E6-Aux[9]-NSStatusItemView> complete!
default	11:25:39.967195-0500	Nexy	<FBSWorkspaceScenesClient:0x8ad38b160 <private>> was invalidated
default	11:25:39.967217-0500	Nexy	FBSWorkspace unregistering source: <private>
error	11:25:39.967262-0500	Nexy	Error creating <FBSScene: 0x8ad38af80; com.apple.controlcenter:0D24F8FF-D07C-49D5-978C-02DA1937C4E6-Aux[9]-NSStatusItemView>: <NSError: 0x8af3c3810; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	11:25:39.967279-0500	Nexy	No scene exists for identity: com.apple.controlcenter:0D24F8FF-D07C-49D5-978C-02DA1937C4E6-Aux[9]-NSStatusItemView
default	11:25:39.967571-0500	Nexy	[com.apple.controlcenter:0D24F8FF-D07C-49D5-978C-02DA1937C4E6-Aux[9]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
error	11:25:39.967801-0500	Nexy	scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	11:25:39.967818-0500	Nexy	[com.apple.controlcenter:0D24F8FF-D07C-49D5-978C-02DA1937C4E6] No matching scene to invalidate for this identity.
error	11:25:39.967854-0500	Nexy	auxiliary scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	11:25:39.967880-0500	Nexy	[com.apple.controlcenter:0D24F8FF-D07C-49D5-978C-02DA1937C4E6-Aux[9]-NSStatusItemView] No matching scene to invalidate for this identity.
error	11:25:39.968247-0500	Nexy	Unhandled disconnected scene <private>
error	11:25:39.968312-0500	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
error	11:25:39.968363-0500	Nexy	Unhandled disconnected auxiliary scene <private>
error	11:25:39.968394-0500	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
default	11:25:40.968362-0500	Nexy	FBSWorkspace registering source: <private>
default	11:25:40.968410-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	11:25:40.968509-0500	Nexy	<FBSWorkspaceScenesClient:0x8ad38af80 <private>> attempting immediate handshake from activate
default	11:25:40.968537-0500	Nexy	<FBSWorkspaceScenesClient:0x8ad38af80 <private>> sent handshake
default	11:25:40.968842-0500	Nexy	Requesting scene <FBSScene: 0x8ad38b2a0; com.apple.controlcenter:D8D68809-D327-42CE-AF0F-0AA7A3D39517> from com.apple.controlcenter.statusitems
default	11:25:40.969115-0500	Nexy	Request for <FBSScene: 0x8ad38b2a0; com.apple.controlcenter:D8D68809-D327-42CE-AF0F-0AA7A3D39517> complete!
default	11:25:40.969553-0500	Nexy	<FBSWorkspaceScenesClient:0x8ad38af80 <private>> was invalidated
default	11:25:40.969602-0500	Nexy	FBSWorkspace unregistering source: <private>
default	11:25:40.969690-0500	Nexy	LSExceptions shared instance invalidated for timeout.
error	11:25:40.969726-0500	Nexy	Error creating <FBSScene: 0x8ad38b2a0; com.apple.controlcenter:D8D68809-D327-42CE-AF0F-0AA7A3D39517>: <NSError: 0x8af3c3d80; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	11:25:40.969760-0500	Nexy	No scene exists for identity: com.apple.controlcenter:D8D68809-D327-42CE-AF0F-0AA7A3D39517
default	11:25:40.969806-0500	Nexy	Requesting scene <FBSScene: 0x8ad38b160; com.apple.controlcenter:D8D68809-D327-42CE-AF0F-0AA7A3D39517-Aux[10]-NSStatusItemView> from com.apple.controlcenter.statusitems
error	11:25:40.969963-0500	Nexy	Error creating <FBSScene: 0x8ad38b160; com.apple.controlcenter:D8D68809-D327-42CE-AF0F-0AA7A3D39517-Aux[10]-NSStatusItemView>: <NSError: 0x8af3c3930; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
default	11:25:40.969999-0500	Nexy	Request for <FBSScene: 0x8ad38b160; com.apple.controlcenter:D8D68809-D327-42CE-AF0F-0AA7A3D39517-Aux[10]-NSStatusItemView> complete!
error	11:25:40.970155-0500	Nexy	scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	11:25:40.970170-0500	Nexy	[com.apple.controlcenter:D8D68809-D327-42CE-AF0F-0AA7A3D39517] No matching scene to invalidate for this identity.
error	11:25:40.970196-0500	Nexy	auxiliary scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	11:25:40.970232-0500	Nexy	Unhandled disconnected scene <private>
error	11:25:40.970295-0500	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
default	11:25:41.069324-0500	Nexy	NSApplication._react(to:) dock
default	11:25:41.069333-0500	Nexy	NSApplication._react(to:) reactions=83
default	11:25:41.971612-0500	Nexy	FBSWorkspace registering source: <private>
default	11:25:41.971647-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	11:25:41.971721-0500	Nexy	<FBSWorkspaceScenesClient:0x8ad38b160 <private>> attempting immediate handshake from activate
default	11:25:41.971750-0500	Nexy	<FBSWorkspaceScenesClient:0x8ad38b160 <private>> sent handshake
default	11:25:41.972012-0500	Nexy	Requesting scene <FBSScene: 0x8ad38b2a0; com.apple.controlcenter:C078C1F3-BD72-4EC2-8780-A6951032B1CF> from com.apple.controlcenter.statusitems
default	11:25:41.972238-0500	Nexy	Request for <FBSScene: 0x8ad38b2a0; com.apple.controlcenter:C078C1F3-BD72-4EC2-8780-A6951032B1CF> complete!
default	11:25:41.972462-0500	Nexy	<FBSWorkspaceScenesClient:0x8ad38b160 <private>> was invalidated
default	11:25:41.972492-0500	Nexy	FBSWorkspace unregistering source: <private>
error	11:25:41.972567-0500	Nexy	Error creating <FBSScene: 0x8ad38b2a0; com.apple.controlcenter:C078C1F3-BD72-4EC2-8780-A6951032B1CF>: <NSError: 0x8af3c3f30; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	11:25:41.972592-0500	Nexy	No scene exists for identity: com.apple.controlcenter:C078C1F3-BD72-4EC2-8780-A6951032B1CF
default	11:25:41.972634-0500	Nexy	FBSWorkspace registering source: <private>
default	11:25:41.972651-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	11:25:41.972708-0500	Nexy	<FBSWorkspaceScenesClient:0x8ad38aee0 <private>> attempting immediate handshake from activate
default	11:25:41.972733-0500	Nexy	<FBSWorkspaceScenesClient:0x8ad38aee0 <private>> sent handshake
default	11:25:41.972903-0500	Nexy	Requesting scene <FBSScene: 0x8ad38af80; com.apple.controlcenter:C078C1F3-BD72-4EC2-8780-A6951032B1CF-Aux[11]-NSStatusItemView> from com.apple.controlcenter.statusitems
default	11:25:41.973092-0500	Nexy	Request for <FBSScene: 0x8ad38af80; com.apple.controlcenter:C078C1F3-BD72-4EC2-8780-A6951032B1CF-Aux[11]-NSStatusItemView> complete!
default	11:25:41.973294-0500	Nexy	<FBSWorkspaceScenesClient:0x8ad38aee0 <private>> was invalidated
default	11:25:41.973321-0500	Nexy	FBSWorkspace unregistering source: <private>
error	11:25:41.973386-0500	Nexy	Error creating <FBSScene: 0x8ad38af80; com.apple.controlcenter:C078C1F3-BD72-4EC2-8780-A6951032B1CF-Aux[11]-NSStatusItemView>: <NSError: 0x8af3c3bd0; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	11:25:41.973417-0500	Nexy	No scene exists for identity: com.apple.controlcenter:C078C1F3-BD72-4EC2-8780-A6951032B1CF-Aux[11]-NSStatusItemView
default	11:25:41.973500-0500	Nexy	[com.apple.controlcenter:C078C1F3-BD72-4EC2-8780-A6951032B1CF-Aux[11]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
error	11:25:41.973678-0500	Nexy	scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	11:25:41.973695-0500	Nexy	[com.apple.controlcenter:C078C1F3-BD72-4EC2-8780-A6951032B1CF] No matching scene to invalidate for this identity.
error	11:25:41.973720-0500	Nexy	auxiliary scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	11:25:41.973732-0500	Nexy	[com.apple.controlcenter:C078C1F3-BD72-4EC2-8780-A6951032B1CF-Aux[11]-NSStatusItemView] No matching scene to invalidate for this identity.
error	11:25:41.974020-0500	Nexy	Unhandled disconnected scene <private>
error	11:25:41.974073-0500	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
error	11:25:41.974118-0500	Nexy	Unhandled disconnected auxiliary scene <private>
error	11:25:41.974147-0500	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
default	11:25:42.975219-0500	Nexy	FBSWorkspace registering source: <private>
default	11:25:42.975260-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	11:25:42.975347-0500	Nexy	<FBSWorkspaceScenesClient:0x8ad38af80 <private>> attempting immediate handshake from activate
default	11:25:42.975380-0500	Nexy	<FBSWorkspaceScenesClient:0x8ad38af80 <private>> sent handshake
default	11:25:42.975704-0500	Nexy	Requesting scene <FBSScene: 0x8ad38b2a0; com.apple.controlcenter:3AE336A8-CE98-4C0E-BB8F-E5909FFFDA8B> from com.apple.controlcenter.statusitems
default	11:25:42.975982-0500	Nexy	Request for <FBSScene: 0x8ad38b2a0; com.apple.controlcenter:3AE336A8-CE98-4C0E-BB8F-E5909FFFDA8B> complete!
default	11:25:42.976197-0500	Nexy	<FBSWorkspaceScenesClient:0x8ad38af80 <private>> was invalidated
default	11:25:42.976228-0500	Nexy	FBSWorkspace unregistering source: <private>
error	11:25:42.976310-0500	Nexy	Error creating <FBSScene: 0x8ad38b2a0; com.apple.controlcenter:3AE336A8-CE98-4C0E-BB8F-E5909FFFDA8B>: <NSError: 0x8af3c1590; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	11:25:42.976329-0500	Nexy	No scene exists for identity: com.apple.controlcenter:3AE336A8-CE98-4C0E-BB8F-E5909FFFDA8B
default	11:25:42.976365-0500	Nexy	FBSWorkspace registering source: <private>
default	11:25:42.976381-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	11:25:42.976433-0500	Nexy	<FBSWorkspaceScenesClient:0x8ad38b160 <private>> attempting immediate handshake from activate
default	11:25:42.976455-0500	Nexy	<FBSWorkspaceScenesClient:0x8ad38b160 <private>> sent handshake
default	11:25:42.976623-0500	Nexy	Requesting scene <FBSScene: 0x8ad38aee0; com.apple.controlcenter:3AE336A8-CE98-4C0E-BB8F-E5909FFFDA8B-Aux[12]-NSStatusItemView> from com.apple.controlcenter.statusitems
default	11:25:42.976811-0500	Nexy	Request for <FBSScene: 0x8ad38aee0; com.apple.controlcenter:3AE336A8-CE98-4C0E-BB8F-E5909FFFDA8B-Aux[12]-NSStatusItemView> complete!
default	11:25:42.977041-0500	Nexy	<FBSWorkspaceScenesClient:0x8ad38b160 <private>> was invalidated
default	11:25:42.977066-0500	Nexy	FBSWorkspace unregistering source: <private>
error	11:25:42.977118-0500	Nexy	Error creating <FBSScene: 0x8ad38aee0; com.apple.controlcenter:3AE336A8-CE98-4C0E-BB8F-E5909FFFDA8B-Aux[12]-NSStatusItemView>: <NSError: 0x8af3c3e70; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	11:25:42.977133-0500	Nexy	No scene exists for identity: com.apple.controlcenter:3AE336A8-CE98-4C0E-BB8F-E5909FFFDA8B-Aux[12]-NSStatusItemView
default	11:25:42.977339-0500	Nexy	[com.apple.controlcenter:3AE336A8-CE98-4C0E-BB8F-E5909FFFDA8B-Aux[12]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
error	11:25:42.977533-0500	Nexy	scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	11:25:42.977549-0500	Nexy	[com.apple.controlcenter:3AE336A8-CE98-4C0E-BB8F-E5909FFFDA8B] No matching scene to invalidate for this identity.
error	11:25:42.977571-0500	Nexy	auxiliary scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	11:25:42.977592-0500	Nexy	[com.apple.controlcenter:3AE336A8-CE98-4C0E-BB8F-E5909FFFDA8B-Aux[12]-NSStatusItemView] No matching scene to invalidate for this identity.
error	11:25:42.977931-0500	Nexy	Unhandled disconnected scene <private>
error	11:25:42.978013-0500	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
error	11:25:42.978060-0500	Nexy	Unhandled disconnected auxiliary scene <private>
error	11:25:42.978094-0500	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
default	11:25:43.978809-0500	Nexy	FBSWorkspace registering source: <private>
default	11:25:43.978832-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	11:25:43.978890-0500	Nexy	<FBSWorkspaceScenesClient:0x8ad38aee0 <private>> attempting immediate handshake from activate
default	11:25:43.978910-0500	Nexy	<FBSWorkspaceScenesClient:0x8ad38aee0 <private>> sent handshake
default	11:25:43.979098-0500	Nexy	Requesting scene <FBSScene: 0x8ad38b2a0; com.apple.controlcenter:27C60660-C676-4319-9677-085E1D8AC99A> from com.apple.controlcenter.statusitems
default	11:25:43.979260-0500	Nexy	Request for <FBSScene: 0x8ad38b2a0; com.apple.controlcenter:27C60660-C676-4319-9677-085E1D8AC99A> complete!
default	11:25:43.979521-0500	Nexy	<FBSWorkspaceScenesClient:0x8ad38aee0 <private>> was invalidated
default	11:25:43.979546-0500	Nexy	FBSWorkspace unregistering source: <private>
error	11:25:43.979612-0500	Nexy	Error creating <FBSScene: 0x8ad38b2a0; com.apple.controlcenter:27C60660-C676-4319-9677-085E1D8AC99A>: <NSError: 0x8af3c3870; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	11:25:43.979629-0500	Nexy	No scene exists for identity: com.apple.controlcenter:27C60660-C676-4319-9677-085E1D8AC99A
default	11:25:43.979656-0500	Nexy	Requesting scene <FBSScene: 0x8ad38b160; com.apple.controlcenter:27C60660-C676-4319-9677-085E1D8AC99A-Aux[13]-NSStatusItemView> from com.apple.controlcenter.statusitems
error	11:25:43.979743-0500	Nexy	Error creating <FBSScene: 0x8ad38b160; com.apple.controlcenter:27C60660-C676-4319-9677-085E1D8AC99A-Aux[13]-NSStatusItemView>: <NSError: 0x8af3c3e10; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
default	11:25:43.979778-0500	Nexy	Request for <FBSScene: 0x8ad38b160; com.apple.controlcenter:27C60660-C676-4319-9677-085E1D8AC99A-Aux[13]-NSStatusItemView> complete!
error	11:25:43.979897-0500	Nexy	scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	11:25:43.979912-0500	Nexy	[com.apple.controlcenter:27C60660-C676-4319-9677-085E1D8AC99A] No matching scene to invalidate for this identity.
error	11:25:43.979933-0500	Nexy	auxiliary scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	11:25:43.979959-0500	Nexy	Unhandled disconnected scene <private>
error	11:25:43.980005-0500	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
default	11:25:44.981338-0500	Nexy	FBSWorkspace registering source: <private>
default	11:25:44.981396-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	11:25:44.981528-0500	Nexy	<FBSWorkspaceScenesClient:0x8ad38b160 <private>> attempting immediate handshake from activate
default	11:25:44.981576-0500	Nexy	<FBSWorkspaceScenesClient:0x8ad38b160 <private>> sent handshake
default	11:25:44.982029-0500	Nexy	Requesting scene <FBSScene: 0x8ad38b2a0; com.apple.controlcenter:697486FE-7E05-422D-AF40-9014FC521C05> from com.apple.controlcenter.statusitems
default	11:25:44.982431-0500	Nexy	Request for <FBSScene: 0x8ad38b2a0; com.apple.controlcenter:697486FE-7E05-422D-AF40-9014FC521C05> complete!
default	11:25:44.982836-0500	Nexy	<FBSWorkspaceScenesClient:0x8ad38b160 <private>> was invalidated
default	11:25:44.982883-0500	Nexy	FBSWorkspace unregistering source: <private>
error	11:25:44.983001-0500	Nexy	Error creating <FBSScene: 0x8ad38b2a0; com.apple.controlcenter:697486FE-7E05-422D-AF40-9014FC521C05>: <NSError: 0x8af3c3fc0; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	11:25:44.983030-0500	Nexy	No scene exists for identity: com.apple.controlcenter:697486FE-7E05-422D-AF40-9014FC521C05
default	11:25:44.983079-0500	Nexy	FBSWorkspace registering source: <private>
default	11:25:44.983102-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	11:25:44.983169-0500	Nexy	<FBSWorkspaceScenesClient:0x8ad38af80 <private>> attempting immediate handshake from activate
default	11:25:44.983197-0500	Nexy	<FBSWorkspaceScenesClient:0x8ad38af80 <private>> sent handshake
default	11:25:44.983406-0500	Nexy	Requesting scene <FBSScene: 0x8ad38b200; com.apple.controlcenter:697486FE-7E05-422D-AF40-9014FC521C05-Aux[14]-NSStatusItemView> from com.apple.controlcenter.statusitems
default	11:25:44.983680-0500	Nexy	Request for <FBSScene: 0x8ad38b200; com.apple.controlcenter:697486FE-7E05-422D-AF40-9014FC521C05-Aux[14]-NSStatusItemView> complete!
default	11:25:44.983879-0500	Nexy	<FBSWorkspaceScenesClient:0x8ad38af80 <private>> was invalidated
default	11:25:44.983916-0500	Nexy	FBSWorkspace unregistering source: <private>
error	11:25:44.983994-0500	Nexy	Error creating <FBSScene: 0x8ad38b200; com.apple.controlcenter:697486FE-7E05-422D-AF40-9014FC521C05-Aux[14]-NSStatusItemView>: <NSError: 0x8af3c3de0; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	11:25:44.984016-0500	Nexy	No scene exists for identity: com.apple.controlcenter:697486FE-7E05-422D-AF40-9014FC521C05-Aux[14]-NSStatusItemView
default	11:25:44.984262-0500	Nexy	[com.apple.controlcenter:697486FE-7E05-422D-AF40-9014FC521C05-Aux[14]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
error	11:25:44.984566-0500	Nexy	scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	11:25:44.984599-0500	Nexy	[com.apple.controlcenter:697486FE-7E05-422D-AF40-9014FC521C05] No matching scene to invalidate for this identity.
error	11:25:44.984639-0500	Nexy	auxiliary scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	11:25:44.984661-0500	Nexy	[com.apple.controlcenter:697486FE-7E05-422D-AF40-9014FC521C05-Aux[14]-NSStatusItemView] No matching scene to invalidate for this identity.
error	11:25:44.985033-0500	Nexy	Unhandled disconnected scene <private>
error	11:25:44.985105-0500	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
error	11:25:44.985148-0500	Nexy	Unhandled disconnected auxiliary scene <private>
error	11:25:44.985178-0500	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
default	11:25:45.985091-0500	Nexy	FBSWorkspace registering source: <private>
default	11:25:45.985129-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	11:25:45.985219-0500	Nexy	<FBSWorkspaceScenesClient:0x8ad38b200 <private>> attempting immediate handshake from activate
default	11:25:45.985249-0500	Nexy	<FBSWorkspaceScenesClient:0x8ad38b200 <private>> sent handshake
default	11:25:45.985570-0500	Nexy	Requesting scene <FBSScene: 0x8ad38b2a0; com.apple.controlcenter:72422E45-7A3B-42F6-85DD-B3F19FF8B947> from com.apple.controlcenter.statusitems
default	11:25:45.985831-0500	Nexy	Request for <FBSScene: 0x8ad38b2a0; com.apple.controlcenter:72422E45-7A3B-42F6-85DD-B3F19FF8B947> complete!
default	11:25:45.986200-0500	Nexy	<FBSWorkspaceScenesClient:0x8ad38b200 <private>> was invalidated
default	11:25:45.986232-0500	Nexy	FBSWorkspace unregistering source: <private>
error	11:25:45.986335-0500	Nexy	Error creating <FBSScene: 0x8ad38b2a0; com.apple.controlcenter:72422E45-7A3B-42F6-85DD-B3F19FF8B947>: <NSError: 0x8af3c1740; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	11:25:45.986357-0500	Nexy	No scene exists for identity: com.apple.controlcenter:72422E45-7A3B-42F6-85DD-B3F19FF8B947
default	11:25:45.986393-0500	Nexy	Requesting scene <FBSScene: 0x8ad38af80; com.apple.controlcenter:72422E45-7A3B-42F6-85DD-B3F19FF8B947-Aux[15]-NSStatusItemView> from com.apple.controlcenter.statusitems
error	11:25:45.986520-0500	Nexy	Error creating <FBSScene: 0x8ad38af80; com.apple.controlcenter:72422E45-7A3B-42F6-85DD-B3F19FF8B947-Aux[15]-NSStatusItemView>: <NSError: 0x8af3c3930; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
default	11:25:45.986567-0500	Nexy	Request for <FBSScene: 0x8ad38af80; com.apple.controlcenter:72422E45-7A3B-42F6-85DD-B3F19FF8B947-Aux[15]-NSStatusItemView> complete!
error	11:25:45.986732-0500	Nexy	scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	11:25:45.986751-0500	Nexy	[com.apple.controlcenter:72422E45-7A3B-42F6-85DD-B3F19FF8B947] No matching scene to invalidate for this identity.
error	11:25:45.986780-0500	Nexy	auxiliary scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	11:25:45.986821-0500	Nexy	Unhandled disconnected scene <private>
error	11:25:45.986886-0500	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
default	11:25:46.988300-0500	Nexy	FBSWorkspace registering source: <private>
default	11:25:46.988348-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	11:25:46.988451-0500	Nexy	<FBSWorkspaceScenesClient:0x8ad38af80 <private>> attempting immediate handshake from activate
default	11:25:46.988491-0500	Nexy	<FBSWorkspaceScenesClient:0x8ad38af80 <private>> sent handshake
default	11:25:46.988866-0500	Nexy	Requesting scene <FBSScene: 0x8ad38b2a0; com.apple.controlcenter:76BF6A8F-1E1E-47DA-BE51-2972ED1DB4AC> from com.apple.controlcenter.statusitems
default	11:25:46.989193-0500	Nexy	Request for <FBSScene: 0x8ad38b2a0; com.apple.controlcenter:76BF6A8F-1E1E-47DA-BE51-2972ED1DB4AC> complete!
default	11:25:46.989586-0500	Nexy	<FBSWorkspaceScenesClient:0x8ad38af80 <private>> was invalidated
default	11:25:46.989635-0500	Nexy	FBSWorkspace unregistering source: <private>
default	11:25:46.989729-0500	Nexy	FBSWorkspace registering source: <private>
default	11:25:46.989764-0500	Nexy	FBSWorkspace connected to endpoint : <private>
default	11:25:46.989855-0500	Nexy	<FBSWorkspaceScenesClient:0x8ad38b200 <private>> attempting immediate handshake from activate
default	11:25:46.989896-0500	Nexy	<FBSWorkspaceScenesClient:0x8ad38b200 <private>> sent handshake
error	11:25:46.990008-0500	Nexy	Error creating <FBSScene: 0x8ad38b2a0; com.apple.controlcenter:76BF6A8F-1E1E-47DA-BE51-2972ED1DB4AC>: <NSError: 0x8af3c0cf0; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	11:25:46.990046-0500	Nexy	No scene exists for identity: com.apple.controlcenter:76BF6A8F-1E1E-47DA-BE51-2972ED1DB4AC
default	11:25:46.990135-0500	Nexy	Requesting scene <FBSScene: 0x8ad38b160; com.apple.controlcenter:76BF6A8F-1E1E-47DA-BE51-2972ED1DB4AC-Aux[16]-NSStatusItemView> from com.apple.controlcenter.statusitems
default	11:25:46.990349-0500	Nexy	Request for <FBSScene: 0x8ad38b160; com.apple.controlcenter:76BF6A8F-1E1E-47DA-BE51-2972ED1DB4AC-Aux[16]-NSStatusItemView> complete!
default	11:25:46.990571-0500	Nexy	<FBSWorkspaceScenesClient:0x8ad38b200 <private>> was invalidated
default	11:25:46.990608-0500	Nexy	FBSWorkspace unregistering source: <private>
error	11:25:46.990688-0500	Nexy	Error creating <FBSScene: 0x8ad38b160; com.apple.controlcenter:76BF6A8F-1E1E-47DA-BE51-2972ED1DB4AC-Aux[16]-NSStatusItemView>: <NSError: 0x8af3c3d50; domain: BSServiceConnectionErrorDomain; code: 3 ("OperationFailed"); "XPC error received on message reply handler">
error	11:25:46.990714-0500	Nexy	No scene exists for identity: com.apple.controlcenter:76BF6A8F-1E1E-47DA-BE51-2972ED1DB4AC-Aux[16]-NSStatusItemView
default	11:25:46.990947-0500	Nexy	[com.apple.controlcenter:76BF6A8F-1E1E-47DA-BE51-2972ED1DB4AC-Aux[16]-NSStatusItemView] Sending action(s) in update: NSSceneFenceAction
error	11:25:46.991235-0500	Nexy	scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	11:25:46.991261-0500	Nexy	[com.apple.controlcenter:76BF6A8F-1E1E-47DA-BE51-2972ED1DB4AC] No matching scene to invalidate for this identity.
error	11:25:46.991301-0500	Nexy	auxiliary scene activation failed: Error Domain=BSServiceConnectionErrorDomain Code=3 "XPC error received on message reply handler" UserInfo={BSErrorCodeDescription=OperationFailed, NSLocalizedFailureReason=XPC error received on message reply handler}
error	11:25:46.991321-0500	Nexy	[com.apple.controlcenter:76BF6A8F-1E1E-47DA-BE51-2972ED1DB4AC-Aux[16]-NSStatusItemView] No matching scene to invalidate for this identity.
error	11:25:46.991775-0500	Nexy	Unhandled disconnected scene <private>
error	11:25:46.991857-0500	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
error	11:25:46.991928-0500	Nexy	Unhandled disconnected auxiliary scene <private>
error	11:25:46.991975-0500	Nexy	[BSBlockSentinel:FBSWorkspaceScenesClient] failed!
