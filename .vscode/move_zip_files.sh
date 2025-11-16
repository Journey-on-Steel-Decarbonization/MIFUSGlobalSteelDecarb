#!/bin/bash
set -o xtrace
PS4='${LINENO}: '

pushd .
mkdir ZIPs
mv "C_ChinaSteelPolicyDeep01.zip" "ZIPs/C_ChinaSteelPolicyDeep01.zip"
mv "D_ClaudeIndia.zip" "ZIPs/D_ClaudeIndia.zip"
mv "E_ClaudeJapan.zip" "ZIPs/E_ClaudeJapan.zip"
mv "F_USASteelClaude.zip" "ZIPs/F_USASteelClaude.zip"
mv "I_Italy.zip" "ZIPs/I_Italy.zip"
mv "J_EuropeanUnion.zip" "ZIPs/J_EuropeanUnion.zip"
mv "L_Turkey.zip" "ZIPs/L_Turkey.zip"
mv "M_Brasil.zip" "ZIPs/M_Brasil.zip"
mv "N_Iran.zip" "ZIPs/N_Iran.zip"
mv "O_Vietnam.zip" "ZIPs/O_Vietnam.zip"

popd