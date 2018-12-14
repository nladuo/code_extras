# $PS1 for linux server
COLBROWN="\[\033[0;33m\]"
COLRED="\[\033[1;31m\]"
COLCLEAR="\[\033[0m\]"
COLGREEN="\[\033[1;32m\]"
COLBLUE="\[\033[1;34m\]"
COLYELLOW="\[\033[1;33m\]"
COLCYAN="\[\033[1;36m\]"

function we_are_in_git_work_tree {
    git rev-parse --is-inside-work-tree &> /dev/null
}

function parse_git_branch {
    if we_are_in_git_work_tree
    then
    local BR=$(git rev-parse --symbolic-full-name --abbrev-ref HEAD 2> /dev/null)
    if [ "$BR" == HEAD ]
    then
        local NM=$(git name-rev --name-only HEAD 2> /dev/null)
        if [ "$NM" != undefined ]
        then echo -n "@$NM"
        else git rev-parse --short HEAD 2> /dev/null
        fi
    else
        echo -n " git:($BR)"
    fi
    fi
}

function parse_git_status {
    if we_are_in_git_work_tree
    then
    local ST=$(git status --short 2> /dev/null)
    if [ -n "$ST" ]
    then echo -n "✗ "
    else echo -n "✗ "
    fi
    fi
}

function pwd_depth_limit_2 {
    if [ "$PWD" = "$HOME" ]
    then echo -n "~"
    else basename `pwd`
    fi
}

export -f parse_git_branch parse_git_status we_are_in_git_work_tree pwd_depth_limit_2
export PS1="$COLGREEN\u@localhost$COLCLEAR:$COLCYAN\$(pwd_depth_limit_2)$COLBLUE\$(parse_git_branch) $COLCLEAR\$ $COLYELLOW\$(parse_git_status)$COLCLEAR"
