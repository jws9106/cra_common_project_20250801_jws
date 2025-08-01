from mission2.src.point_calculator.point_strategy.interface_point_strategy import IPointStrategy

class PointCalculator:
    @staticmethod
    def execute():
        for strategy_key in sorted(IPointStrategy.registry.keys()):
            cls = IPointStrategy.registry[strategy_key]
            cls().execute()