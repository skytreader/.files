# vim: set ft=sh:
# For Kalibrr

checked_kubectl(){
    kubectl $@
    if [ "$1" == "config" ] && [ "$2" == "use-context" ]; then
        if [ "$2" == "use-context" ] || [ "$2" == "set-context" ]; then
            source ~/.work_customizations
        fi
    fi
}

alias kcl='checked_kubectl'
