def stamina2tael(stamina: int) -> int:
    """计算用stamina体力打工能赚多少银两

    Args:
        stamina (int): 持有的体力

    Returns:
        str: 打工能赚到的银两
    """
    return round(stamina / 40 * 3000)


def stamina_given_tael(tael: int) -> int:
    """计算想打工赚tael银两需要消耗多少体力

    Args:
        tael (int): 想赚的银两

    Returns:
        str: 需要的体力
    """
    return round(tael / 3000 * 40)
