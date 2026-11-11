"""Stable domain enumerations used by future parser and conversion services."""

from enum import StrEnum


class DriverRole(StrEnum):
    MASTER = "MASTER"
    SLAVE = "SLAVE"
    UNKNOWN = "UNKNOWN"
    AMBIGUOUS = "AMBIGUOUS"


class IEC104Function(StrEnum):
    MONITORING = "MONITORING"
    COMMAND = "COMMAND"
    SETPOINT = "SETPOINT"
    SPECIAL = "SPECIAL"
    UNKNOWN = "UNKNOWN"


class Direction(StrEnum):
    RECEIVE = "RECEIVE"
    SEND = "SEND"
    BIDIRECTIONAL = "BIDIRECTIONAL"
    UNKNOWN = "UNKNOWN"


class DataFamily(StrEnum):
    SINGLE_POINT = "SINGLE_POINT"
    DOUBLE_POINT = "DOUBLE_POINT"
    FLOAT = "FLOAT"
    NORMALIZED_VALUE = "NORMALIZED_VALUE"
    SCALED_VALUE = "SCALED_VALUE"
    INTEGRATED_TOTAL = "INTEGRATED_TOTAL"
    STEP_POSITION = "STEP_POSITION"
    SINGLE_COMMAND = "SINGLE_COMMAND"
    DOUBLE_COMMAND = "DOUBLE_COMMAND"
    REGULATING_STEP_COMMAND = "REGULATING_STEP_COMMAND"
    SETPOINT_NORMALIZED = "SETPOINT_NORMALIZED"
    SETPOINT_SCALED = "SETPOINT_SCALED"
    SETPOINT_FLOAT = "SETPOINT_FLOAT"
    BITSTRING = "BITSTRING"
    UNKNOWN = "UNKNOWN"


# Compatibility alias for the foundation API; new domain code uses the
# explicit IEC104Function name.
Function = IEC104Function


class Priority(StrEnum):
    HIGH = "HIGH"
    LOW = "LOW"
    GI_ONLY = "GI_ONLY"
    NOT_APPLICABLE = "NOT_APPLICABLE"
    UNKNOWN = "UNKNOWN"


class CommandPhase(StrEnum):
    SELECT = "SELECT"
    EXECUTE = "EXECUTE"
    CANCEL = "CANCEL"
    NOT_APPLICABLE = "NOT_APPLICABLE"
    UNKNOWN = "UNKNOWN"


class TimestampFormat(StrEnum):
    NONE = "NONE"
    CP24 = "CP24"
    CP56 = "CP56"
    UNKNOWN = "UNKNOWN"
