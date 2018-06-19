#/bin/bash
##############################################
# NOT FOR PRODUCTION ONLY FOR TRAINING CASE
##############################################
# quick and dirty

CERT_KEY_PREFIX="kubernetes-dashboard"
TMP_CONFIG_FILE="/tmp/tmp_kez_config_file.conf"

KEZ_BACKUP_DIR="kez_backup_$(date +%Y%m%d%H%M%S)"

mkdir -p ./${KEZ_BACKUP_DIR}

ln -s ./${KEZ_BACKUP_DIR} latest_kez_backup

# clean old keys
mv ${CERT_KEY_PREFIX}.crt ./${KEZ_BACKUP_DIR}
mv ${CERT_KEY_PREFIX}.pass.key ./${KEZ_BACKUP_DIR}
mv ${CERT_KEY_PREFIX}.key ./${KEZ_BACKUP_DIR}
mv ${CERT_KEY_PREFIX}.csr ./${KEZ_BACKUP_DIR}

openssl genrsa -des3 -passout pass:x -out ${CERT_KEY_PREFIX}.pass.key 2048
openssl rsa -passin pass:x -in ${CERT_KEY_PREFIX}.pass.key -out ${CERT_KEY_PREFIX}.key
rm ${CERT_KEY_PREFIX}.pass.key

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

openssl req -new -config ${TMP_CONFIG_FILE} -key ${CERT_KEY_PREFIX}.key -out ${CERT_KEY_PREFIX}.csr
openssl x509 -req -sha256 -days 365 -in ${CERT_KEY_PREFIX}.csr -signkey ${CERT_KEY_PREFIX}.key -out ${CERT_KEY_PREFIX}.crt

CERTS_DIR="$HOME/certs"

if [[ ! -e ${CERTS_DIR} ]]; then
	mkdir ${CERTS_DIR}
elif [[ ! -d ${CERTS_DIR} ]]; then
	echo "ERRROR ${CERTS_DIR} already exists BUT is not a directory" 1>&2
	exit 1
fi

cp ${CERT_KEY_PREFIX}.crt ${CERTS_DIR}

ls -l ${CERTS_DIR}
