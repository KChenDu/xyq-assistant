from math import ceil


def tael_given_point(point: int, price: int) -> str:
    """计算买point点卡点数需要多少银两（额外消耗三界功绩）

    Args:
        point (int): 想买的点数
        price (int): 点卡价格（银两/点）

    Returns:
        str: 需要的银两与三界功绩
    """
    return f"{point * price}银两，额外消耗{ceil(.7 * point)}三界功绩"


def tael_given_yuan(yuan: int, rate: float) -> str:
    """计算获得yuan元需要出售多少万银两

    Args:
        yuan (int): 想要的元
        rate (float): 比例（元/万银两）

    Returns:
        str: 需出售的万银两与消耗的三界功绩
    """
    return f"{round(yuan / .95 / rate)}万银两，额外消耗{round(2 * yuan)}三界功绩"


def tael2yuan(tael: int, rate: float) -> str:
    """计算出售tael万银两可以获得多少元

    Args:
        tael (int): 出售的银两
        rate (float): 比例（元/万银两）

    Returns:
        str: 可获得的元
    """
    return f"{tael * rate * 0.95:.2f}元，额外消耗{round(2 * tael * rate)}三界功绩"


def yuan2tael(yuan: int, rate: float) -> str:
    """计算用yuan元能买多少万银两

    Args:
        yuan (int): 持有的元
        rate (float): 比例（元/万银两）

    Returns:
        str: 能买到的万银两
    """
    return f"{round(yuan / rate)}万银两"


def yuan_given_tael(tael: int, rate: float) -> str:
    """计算需要花多少元能买tael万银两

    Args:
        tael (int): 想买的万银两
        rate (float): 比例（元/万银两）

    Returns:
        str: 需要的元
    """
    return f"{tael * rate:.2f}元"


def yuan2point(yuan: int) -> int:
    """计算用yuan元能买多少点卡点数

    Args:
        yuan (int): 持有的元

    Returns:
        str: 能买到的点卡点数
    """
    return yuan * 10


def yuan_given_point(point: int) -> float:
    """计算需要多少元能买point点卡点数

    Args:
        point (int): 想买的点数

    Returns:
        str: 需要的元
    """
    return point / 10


def tael2reserve(tael: int) -> int:
    """计算tael银两等价于多少储备金

    Args:
        tael (int): 银两

    Returns:
        str: 储备金
    """
    return tael * 1.25
