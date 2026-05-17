import random

from PyQt6.QtCharts import QChart, QChartView, QLineSeries

from PyQt6.QtCore import QPointF


class EnergyChart(QChartView):
    def __init__(self):
        super().__init__()

        chart = QChart()

        series = QLineSeries()

        for i in range(30):
            series.append(QPointF(i, random.randint(0, 100)))

        chart.addSeries(series)
        chart.createDefaultAxes()

        self.setChart(chart)