def expected_orbs(suit_type: str, current_count: int = 0) -> float:
    """计算点到目标套装效果所需的附魔宝珠期望数量。

    Args:
        suit_type (str): 套装类型，可选“变身术”“法术追加”“附加状态”“变化咒”
        current_count (int, optional): 当前已失败点化次数，范围 0-30

    Returns:
        float: 还需要消耗的附魔宝珠期望数量
    """
    assert -1 < current_count < 31
    
    if suit_type == "变身术":
        total: int = 80
    elif suit_type == "变化咒":
        total: int = 40
    elif suit_type == "法术追加":
        total: int = 56
    elif suit_type == "附加状态":
        total: int = 19
    else:
        raise ValueError

    p: float = 1 / total
    remaining_attempts: int = 31 - current_count

    return (1 - (1 - p) ** remaining_attempts) / p


def expected_price(suit_type: str, orb_price: int, current_count: int = 0) -> float:
    """计算点到目标套装效果所需的附魔宝珠期望价格。

    Args:
        suit_type (str): 套装类型，可选“变身术”“法术追加”“附加状态”“变化咒”
        orb_price (int): 单颗附魔宝珠价格
        current_count (int, optional): 当前已失败点化次数，范围 0-30

    Returns:
        float: 期望价格
    """
    return expected_orbs(suit_type, current_count) * orb_price
