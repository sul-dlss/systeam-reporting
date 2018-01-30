# Servers without a stack

This connects to puppetdb and gets a list of all hosts that don't have a stack
fact.

systeam-reporting/security/stacks-missing > /tmp/stacks.csv


# Servers with certain packages

Servers with Apache or Tomcat, and listing servers that have those but not
webauth or shibboleth.

ssh reporting@sulreports
cd server-reports/current/
RAILS_ENV=production rake report:alerts > /tmp/packages.csv


# Servers behind webauth/shibboleth

We have a script (server-webauth) that does a first pass at finding webservers
completely behind authentication (and thus less a worry).  But since most are
hard to figure by script, we use a worksheet in Google Drive.  It's available
as Security Mitigation, "Servers with websites fully behind Webauth/Shibboleth".

Download that file as CSV to /tmp/webauth.csv


# iptables

This reports on any iptables rules on our servers, via puppetdb.  The rules
are filtered to remove ranges that come from Stanford networks.

systeam-reporting/security/server-iptables > /tmp/iptables.csv


# Environments

This tries to determine server environment from first the stack fact, and
then the servername itself as a fallback.

systeam-reporting/security/server-environments > /tmp/environments.csv


# Load balanced servers

This can't be found by script, so is kept in a Google Drive document, under
Security Mitigation, "Servers in load-balanced pools".  Download it and save
to /tmp/lb.csv


# Non-Stanford accounts

Report on any server login accounts that aren't owned by a DLSS user.  This is
still in progress and needs more tweaking.

systeam-reporting/security/puppetdb-users > /tmp/users.csv


# SSH keypairs

Nothing for this yet.


# Combining reports and logic

This combines all our CSV reports into one.  The files fed it should be in the
order we want the columns to be in (with hostname automatically first).  It
also adds a field immediately after the hostname that determines the priority
of this server to be looked at.

systeam-reporting/security/csv-combine stacks.csv environment.csv \
  packages.csv webauth.csv iptables.csv lb.csv users.csv > all.csv
