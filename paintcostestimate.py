import math


def showCostEstimate(gallonPaint, hourLabor, costPaint, costLabor):
    print(f"Gallons of paint: {gallonPaint}")
    print(f"Hours of labor: {hourLabor}")
    print(f"Paint Charges: ${costPaint:,.2f}")
    print(f"Labor Charges: ${costLabor:,.2f}")
    print(f"Total Cost: ${costPaint + costLabor:,.2f}")

def main():
    wallSpace = int(input("wall space "))
    paintPrice = int(input("paint price "))

    gallonPaint = math.ceil(wallSpace/112)
    hourLabor = (math.ceil(wallSpace/112))*8
    costPaint = gallonPaint * paintPrice
    costLabor = hourLabor * 35
    showCostEstimate(gallonPaint, hourLabor, costPaint, costLabor)

if __name__ == "__main__":
    main()