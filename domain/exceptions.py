class InsufficientFundsError(Exception):
    """Lançado quando uma conta não tem saldo suficiente para uma operação."""


class AccountNotFoundError(Exception):
    """Lançado quando uma conta não é encontrada."""
