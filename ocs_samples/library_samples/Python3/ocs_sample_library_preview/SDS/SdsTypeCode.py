# SdsTypeCode.py
#
# Copyright 2019 OSIsoft, LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# <http://www.apache.org/licenses/LICENSE-2.0>
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from enum import Enum

class SdsTypeCode(Enum):
    Empty = 0
    Object = 1
    DBNull = 2
    Boolean = 3
    Char = 4
    SByte = 5
    Byte = 6
    Int16 = 7
    UInt16 = 8
    Int32 = 9
    UInt32 = 10
    Int64 = 11
    UInt64 = 12
    Single = 13
    Double = 14
    Decimal = 15
    DateTime = 16
    String = 18
    Guid = 19
    DateTimeOffset = 20
    TimeSpan = 21
    Version = 22
    NullableBoolean = 103
    NullableChar = 104
    NullableSByte = 105
    NullableByte = 106
    NullableInt16 = 107
    NullableUInt16 = 108
    NullableInt32 = 109
    NullableUInt32 = 110
    NullableInt64 = 111
    NullableUInt64 = 112
    NullableSingle = 113
    NullableDouble = 114
    NullableDecimal = 115
    NullableDateTime = 116
    NullableGuid = 119
    NullableDateTimeOffset = 120
    NullableTimeSpan = 121
    BooleanArray = 203
    CharArray = 204
    SByteArray = 205
    ByteArray = 206
    Int16Array = 207
    UInt16Array = 208
    Int32Array = 209
    UInt32Array = 210
    Int64Array = 211
    UInt64Array = 212
    SingleArray = 213
    DoubleArray = 214
    DecimalArray = 215
    DateTimeArray = 216
    StringArray = 218
    GuidArray = 219
    DateTimeOffsetArray = 220
    TimeSpanArray = 221
    VersionArray = 222
    Array = 400
    IList = 401
    IDictionary = 402
    IEnumerable = 403
    SdsType = 501
    SdsTypeProperty = 502
    SByteEnum = 605
    ByteEnum = 606
    Int16Enum = 607
    UInt16Enum = 608
    Int32Enum = 609
    UInt32Enum = 610
    Int64Enum = 611
    UInt64Enum = 612
    NullableSByteEnum = 705
    NullableByteEnum = 706
    NullableInt16Enum = 707
    NullableUInt16Enum = 708
    NullableInt32Enum = 709
    NullableUInt32Enum = 710
    NullableInt64Enum = 711
    NullableUInt64Enum = 712
        
