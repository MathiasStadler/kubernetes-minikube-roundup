#/bin/bash

set -e
##############################################
# NOT FOR PRODUCTION ONLY FOR TRAINING CASE
##############################################
# quick and dirty

# https://stackoverflow.com/questions/991758/how-to-get-pem-file-from-key-and-crt-files

CERT_KEY_PREFIX="kubernetes-dashboard"
TMP_CONFIG_FILE="/tmp/tmp_kez_config_file.conf"

KEZ_BACKUP_DIR="kez_backup_$(date +%Y%m%d%H%M%S)"

KEZ_BACKUP_LATEST="kez_backup_latest"

mkdir -p ./${KEZ_BACKUP_DIR}

rm -rf ${KEZ_BACKUP_LATEST}
ln -s ./${KEZ_BACKUP_DIR} ${KEZ_BACKUP_LATEST}

# clean old keys
if [[ -e ${CERT_KEY_PREFIX}.ca.key.pem ]]; then
	mv ${CERT_KEY_PREFIX}.ca.key.pem ./${KEZ_BACKUP_DIR}
fi

if [[ -e ${CERT_KEY_PREFIX}.ca.certificate.pem ]]; then
	mv ${CERT_KEY_PREFIX}.ca.certificate.pem ./${KEZ_BACKUP_DIR}
fi
if [[ -e ${CERT_KEY_PREFIX}.cert.pem ]]; then
	mv ${CERT_KEY_PREFIX}.cert.pem ./${KEZ_BACKUP_DIR}
fi
if [[ -e ${CERT_KEY_PREFIX}.ca.request ]]; then
	mv ${CERT_KEY_PREFIX}.ca.request ./${KEZ_BACKUP_DIR}
fi

##old  openssl genrsa -des3 -passout pass:x -out ${CERT_KEY_PREFIX}.pass.key 2048
##old openssl rsa -passin pass:x -in ${CERT_KEY_PREFIX}.pass.key -out ${CERT_KEY_PREFIX}.key
## old rm ${CERT_KEY_PREFIX}.pass.key

cat >${TMP_CONFIG_FILE} <<EOF
[req]
prompt = no
distinguished_name = req_distinguished_name
req_extensions = v3_req

[req_distinguished_name]
C = US
ST = California
L = Los Angeles
O = Our Company Llc
#OU = Org Unit Name
CN = Our Company Llc
#emailAddress = info@example.com

[v3_req]
basicConstraints = CA:FALSE
keyUsage = nonRepudiation, digitalSignature, keyEncipherment
subjectAltName = @alt_names

[alt_names]
DNS.1 = example.com
DNS.2 = www.example.com

EOF

## old openssl req -new -config ${TMP_CONFIG_FILE} -key ${CERT_KEY_PREFIX}.key -out ${CERT_KEY_PREFIX}.csr
# from here
# https://www.ibm.com/support/knowledgecenter/en/SSWHYP_4.0.0/com.ibm.apimgmt.cmc.doc/task_apionprem_gernerate_self_signed_openSSL.html
# or
# https://blogs.oracle.com/blogbypuneeth/steps-to-create-a-self-signed-certificate-using-openssl

# command to generate your private key and public certificate with data from config file
openssl req -newkey rsa:2048 -config ${TMP_CONFIG_FILE} -nodes -keyout ${CERT_KEY_PREFIX}.ca.key.pem -x509 -days 365 -out ${CERT_KEY_PREFIX}.ca.certificate.pem

# Review the created ca.certificate:
openssl x509 -text -noout -in ${CERT_KEY_PREFIX}.ca.certificate.pem

##old openssl x509 -req -sha256 -days 365 -in ${CERT_KEY_PREFIX}.csr -signkey ${CERT_KEY_PREFIX}.key -out ${CERT_KEY_PREFIX}.crt

# convert the x509 certificate to a certificate request:
# https://www.linuxquestions.org/questions/linux-networking-3/openssl-x509-expecting-certificate-request-290773/
openssl x509 -x509toreq -days 365 -in ${CERT_KEY_PREFIX}.ca.certificate.pem -signkey ${CERT_KEY_PREFIX}.ca.key.pem -out ${CERT_KEY_PREFIX}.ca.request

openssl x509 -req -sha256 -days 365 -in ${CERT_KEY_PREFIX}.ca.request -signkey ${CERT_KEY_PREFIX}.ca.key.pem -out ${CERT_KEY_PREFIX}.cert.pem

# Review the created certificate:
openssl x509 -text -noout -in ${CERT_KEY_PREFIX}.cert.pem

echo "Follow both md5 hash must be identical"
# check key and cert
openssl rsa -in ${CERT_KEY_PREFIX}.ca.key.pem -noout -modulus | openssl md5

openssl x509 -in ${CERT_KEY_PREFIX}.cert.pem -noout -modulus | openssl md5

# skip pkcs12 generte
exit 0
# Combine your key and certificate in a PKCS#12 (P12) bundle
openssl pkcs12 -inkey ${CERT_KEY_PREFIX}.ca.key.pem -in ${CERT_KEY_PREFIX}.ca.certificate.pem -export -out ${CERT_KEY_PREFIX}.certificate.p12
# Validate your P2 file
openssl pkcs12 -in ${CERT_KEY_PREFIX}.certificate.p12 -noout -info

# skip the copy part
exit 0

CERTS_DIR="$HOME/certs"

if [[ ! -e ${CERTS_DIR} ]]; then
	mkdir ${CERTS_DIR}
elif [[ ! -d ${CERTS_DIR} ]]; then
	echo "ERRROR ${CERTS_DIR} already exists BUT is not a directory" 1>&2
	exit 1
fi

cp ${CERT_KEY_PREFIX}.crt ${CERTS_DIR}

ls -l ${CERTS_DIR}
