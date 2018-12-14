#!/bin/bash
### BEGIN INIT INFO
# Provides: 	  nexus
# Required-Start: $all
# Required-Stop:
# Default-Start: 2 3 4 5
# Default-Stop: 0 1 2 6
# Short-Description: Nexus (https://www.sonatype.com/nexus-repository-sonatype)
# Description: Nexus (https://www.sonatype.com/nexus-repository-sonatype)
### END INIT INFO

/usr/bin/nexus $*