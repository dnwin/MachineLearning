"""
Hot and Cold Learning
Adjusting our knob_weight either up or down so that our error reduces to 0.
"""
INPUT_VALUE = 0.4
GOAL_PREDICTION = 0.8

STEP_AMOUNT = 0.001

def main():
    """Loop and adjust knob weight."""
    knob_weight = 0.5

    for _ in range(10000):
        prediction = knob_weight * INPUT_VALUE

        error = (GOAL_PREDICTION - prediction) ** 2

        print("Error:" + str(error) + " Prediction:" + str(prediction))

        up_prediction = (knob_weight + STEP_AMOUNT) * INPUT_VALUE
        up_error = (GOAL_PREDICTION - up_prediction) ** 2

        down_prediction = (knob_weight - STEP_AMOUNT) * INPUT_VALUE
        down_error = (GOAL_PREDICTION - down_prediction) ** 2

        if down_error < up_error:
            knob_weight = knob_weight - STEP_AMOUNT

        if down_error > up_error:
            knob_weight = knob_weight + STEP_AMOUNT

if __name__ == "__main__":
    main()
