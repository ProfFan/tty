./twinpipec "unbuffer -p sh -c \"echo \$TERM;stty 300;stty echo;export TERM=dumb;export LC_ALL=en_US.UTF-8;stty cols 132;bash\" 2>&1" "python3 teletype.py"
