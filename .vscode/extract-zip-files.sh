#!/bin/bash
set -o xtrace
PS4='${LINENO}: '

pushd .
7z e "./ZIPs/C_ChinaSteelPolicyDeep01.zip" -o./ZIPs/C_ChinaSteelPolicyDeep01
rm "./ZIPs/C_ChinaSteelPolicyDeep01.zip"

7z e "./ZIPs/D_ClaudeIndia.zip" -o./ZIPs/D_ClaudeIndia
rm "./ZIPs/D_ClaudeIndia.zip"

7z e "./ZIPs/E_ClaudeJapan.zip" -o./ZIPs/E_ClaudeJapan
rm "./ZIPs/E_ClaudeJapan.zip"

7z e "./ZIPs/F_USASteelClaude.zip" -o./ZIPs/F_USASteelClaude
rm "./ZIPs/F_USASteelClaude.zip"

7z e "./ZIPs/I_Italy.zip" -o./ZIPs/I_Italy
rm "./ZIPs/I_Italy.zip"

7z e "./ZIPs/J_EuropeanUnion.zip" -o./ZIPs/J_EuropeanUnion
rm "./ZIPs/J_EuropeanUnion.zip"

7z e "./ZIPs/L_Turkey.zip" -o./ZIPs/L_Turkey
rm "./ZIPs/L_Turkey.zip"

7z e "./ZIPs/M_Brasil.zip" -o./ZIPs/M_Brasil
rm "./ZIPs/M_Brasil.zip"

7z e "./ZIPs/N_Iran.zip" -o./ZIPs/N_Iran
rm "./ZIPs/N_Iran.zip"

7z e "./ZIPs/O_Vietnam.zip" -o./ZIPs/O_Vietnam
rm "./ZIPs/O_Vietnam.zip"


popd