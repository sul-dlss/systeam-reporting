# systeam-reporting

This contains various scripts used by Operations for reports, meant to be a
default location for one-offs.  Most are meant to be run on
sulreports.stanford.edu.  In some cases these wrapper other software to gather
data from several sources and clean it up into a format we like.

These are currently written in multiple languages, though Ruby is preferred.  
We may also use Python for anything that relies on Python libraries, or Perl
for LDAP functions so that we can use Stanford::Directory.

## Requirements

https://github.com/tskirvin/cms-puppetdb-tools
