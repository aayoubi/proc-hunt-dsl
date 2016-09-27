from process_utils import retrieve_jdk_jstat

# http://docs.oracle.com/javase/7/docs/technotes/tools/share/jstat.html

_JSTAT_GC_S0U_INDEX = 2
_JSTAT_GC_S1U_INDEX = 3
_JSTAT_GC_EU_INDEX = 5
_JSTAT_GC_OU_INDEX = 7
_JSTAT_GC_YGC_INDEX = 10
_JSTAT_GC_YGCT_INDEX = 11
_JSTAT_GC_FGC_INDEX = 12
_JSTAT_GC_FGCT_INDEX = 13
_JSTAT_GC_GCT_INDEX = 14


class YGC:
    """
    Number of Young generation GC Events
    """
    def __init__(self):
        pass

    def get(self, host, pid):
        return retrieve_jdk_jstat(pid, host, 'gc')[_JSTAT_GC_YGC_INDEX]


class YGCT:
    """
    Young generation garbage collection time.
    """
    def __init__(self):
        pass

    def get(self, host, pid):
        return retrieve_jdk_jstat(pid, host, 'gc')[_JSTAT_GC_YGCT_INDEX]


class FGC:
    """
    Number of Full GC Events.
    """
    def __init__(self):
        pass

    def get(self, host, pid):
        return retrieve_jdk_jstat(pid, host, 'gc')[_JSTAT_GC_FGC_INDEX]


class FGCT:
    """
    Full garbage collection time.
    """
    def __init__(self):
        pass

    def get(self, host, pid):
        return retrieve_jdk_jstat(pid, host, 'gc')[_JSTAT_GC_FGCT_INDEX]


class GCT:
    """
    Total garbage collection time.
    """
    def __init__(self):
        pass

    def get(self, host, pid):
        return retrieve_jdk_jstat(pid, host, 'gc')[_JSTAT_GC_GCT_INDEX]


class S0U:
    """
    Survivor space 0 utilization (KB).
    """
    def __init__(self):
        pass

    def get(self, host, pid):
        return retrieve_jdk_jstat(pid, host, 'gc')[_JSTAT_GC_S0U_INDEX]


class S1U:
    """
    Survivor space 1 utilization (KB).
    """
    def __init__(self):
        pass

    def get(self, host, pid):
        return retrieve_jdk_jstat(pid, host, 'gc')[_JSTAT_GC_S1U_INDEX]


class EU:
    """
    Eden space utilization (KB).
    """
    def __init__(self):
        pass

    def get(self, host, pid):
        return retrieve_jdk_jstat(pid, host, 'gc')[_JSTAT_GC_EU_INDEX]


class OU:
    """
    Old space utilization (KB).
    """
    def __init__(self):
        pass

    def get(self, host, pid):
        return retrieve_jdk_jstat(pid, host, 'gc')[_JSTAT_GC_OU_INDEX]

