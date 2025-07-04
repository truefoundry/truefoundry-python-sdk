# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class AwsRegion(str, enum.Enum):
    AF_SOUTH1 = "af-south-1"
    AP_EAST1 = "ap-east-1"
    AP_NORTHEAST1 = "ap-northeast-1"
    AP_NORTHEAST2 = "ap-northeast-2"
    AP_NORTHEAST3 = "ap-northeast-3"
    AP_SOUTH1 = "ap-south-1"
    AP_SOUTH2 = "ap-south-2"
    AP_SOUTHEAST1 = "ap-southeast-1"
    AP_SOUTHEAST2 = "ap-southeast-2"
    AP_SOUTHEAST3 = "ap-southeast-3"
    AP_SOUTHEAST4 = "ap-southeast-4"
    AP_SOUTHEAST5 = "ap-southeast-5"
    AP_SOUTHEAST7 = "ap-southeast-7"
    CA_CENTRAL1 = "ca-central-1"
    CA_WEST1 = "ca-west-1"
    CN_NORTH1 = "cn-north-1"
    CN_NORTHWEST1 = "cn-northwest-1"
    EU_CENTRAL1 = "eu-central-1"
    EU_CENTRAL2 = "eu-central-2"
    EU_NORTH1 = "eu-north-1"
    EU_SOUTH1 = "eu-south-1"
    EU_SOUTH2 = "eu-south-2"
    EU_WEST1 = "eu-west-1"
    EU_WEST2 = "eu-west-2"
    EU_WEST3 = "eu-west-3"
    IL_CENTRAL1 = "il-central-1"
    ME_CENTRAL1 = "me-central-1"
    ME_SOUTH1 = "me-south-1"
    MX_CENTRAL1 = "mx-central-1"
    SA_EAST1 = "sa-east-1"
    US_EAST1 = "us-east-1"
    US_EAST2 = "us-east-2"
    US_GOV_EAST1 = "us-gov-east-1"
    US_GOV_WEST1 = "us-gov-west-1"
    US_WEST1 = "us-west-1"
    US_WEST2 = "us-west-2"

    def visit(
        self,
        af_south1: typing.Callable[[], T_Result],
        ap_east1: typing.Callable[[], T_Result],
        ap_northeast1: typing.Callable[[], T_Result],
        ap_northeast2: typing.Callable[[], T_Result],
        ap_northeast3: typing.Callable[[], T_Result],
        ap_south1: typing.Callable[[], T_Result],
        ap_south2: typing.Callable[[], T_Result],
        ap_southeast1: typing.Callable[[], T_Result],
        ap_southeast2: typing.Callable[[], T_Result],
        ap_southeast3: typing.Callable[[], T_Result],
        ap_southeast4: typing.Callable[[], T_Result],
        ap_southeast5: typing.Callable[[], T_Result],
        ap_southeast7: typing.Callable[[], T_Result],
        ca_central1: typing.Callable[[], T_Result],
        ca_west1: typing.Callable[[], T_Result],
        cn_north1: typing.Callable[[], T_Result],
        cn_northwest1: typing.Callable[[], T_Result],
        eu_central1: typing.Callable[[], T_Result],
        eu_central2: typing.Callable[[], T_Result],
        eu_north1: typing.Callable[[], T_Result],
        eu_south1: typing.Callable[[], T_Result],
        eu_south2: typing.Callable[[], T_Result],
        eu_west1: typing.Callable[[], T_Result],
        eu_west2: typing.Callable[[], T_Result],
        eu_west3: typing.Callable[[], T_Result],
        il_central1: typing.Callable[[], T_Result],
        me_central1: typing.Callable[[], T_Result],
        me_south1: typing.Callable[[], T_Result],
        mx_central1: typing.Callable[[], T_Result],
        sa_east1: typing.Callable[[], T_Result],
        us_east1: typing.Callable[[], T_Result],
        us_east2: typing.Callable[[], T_Result],
        us_gov_east1: typing.Callable[[], T_Result],
        us_gov_west1: typing.Callable[[], T_Result],
        us_west1: typing.Callable[[], T_Result],
        us_west2: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AwsRegion.AF_SOUTH1:
            return af_south1()
        if self is AwsRegion.AP_EAST1:
            return ap_east1()
        if self is AwsRegion.AP_NORTHEAST1:
            return ap_northeast1()
        if self is AwsRegion.AP_NORTHEAST2:
            return ap_northeast2()
        if self is AwsRegion.AP_NORTHEAST3:
            return ap_northeast3()
        if self is AwsRegion.AP_SOUTH1:
            return ap_south1()
        if self is AwsRegion.AP_SOUTH2:
            return ap_south2()
        if self is AwsRegion.AP_SOUTHEAST1:
            return ap_southeast1()
        if self is AwsRegion.AP_SOUTHEAST2:
            return ap_southeast2()
        if self is AwsRegion.AP_SOUTHEAST3:
            return ap_southeast3()
        if self is AwsRegion.AP_SOUTHEAST4:
            return ap_southeast4()
        if self is AwsRegion.AP_SOUTHEAST5:
            return ap_southeast5()
        if self is AwsRegion.AP_SOUTHEAST7:
            return ap_southeast7()
        if self is AwsRegion.CA_CENTRAL1:
            return ca_central1()
        if self is AwsRegion.CA_WEST1:
            return ca_west1()
        if self is AwsRegion.CN_NORTH1:
            return cn_north1()
        if self is AwsRegion.CN_NORTHWEST1:
            return cn_northwest1()
        if self is AwsRegion.EU_CENTRAL1:
            return eu_central1()
        if self is AwsRegion.EU_CENTRAL2:
            return eu_central2()
        if self is AwsRegion.EU_NORTH1:
            return eu_north1()
        if self is AwsRegion.EU_SOUTH1:
            return eu_south1()
        if self is AwsRegion.EU_SOUTH2:
            return eu_south2()
        if self is AwsRegion.EU_WEST1:
            return eu_west1()
        if self is AwsRegion.EU_WEST2:
            return eu_west2()
        if self is AwsRegion.EU_WEST3:
            return eu_west3()
        if self is AwsRegion.IL_CENTRAL1:
            return il_central1()
        if self is AwsRegion.ME_CENTRAL1:
            return me_central1()
        if self is AwsRegion.ME_SOUTH1:
            return me_south1()
        if self is AwsRegion.MX_CENTRAL1:
            return mx_central1()
        if self is AwsRegion.SA_EAST1:
            return sa_east1()
        if self is AwsRegion.US_EAST1:
            return us_east1()
        if self is AwsRegion.US_EAST2:
            return us_east2()
        if self is AwsRegion.US_GOV_EAST1:
            return us_gov_east1()
        if self is AwsRegion.US_GOV_WEST1:
            return us_gov_west1()
        if self is AwsRegion.US_WEST1:
            return us_west1()
        if self is AwsRegion.US_WEST2:
            return us_west2()
