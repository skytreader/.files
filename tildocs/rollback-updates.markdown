# For rolling back bulk updates that may have broken something

    grep -A 2 'Start-Date: 2016-08-26' /var/log/apt/history.log | tail -1 >/tmp/packages.txt
    tr ',' '\n' < /tmp/packages.txt | sed '/automatic)/d' | awk '{ print $1}' > /tmp/final.packages.txt

Then use the `rollback` script at the root of this repo.
