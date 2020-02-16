def heart_rate_outlier_detection(age,heart_rate):
    #dictionary format={age:[min_target_heart_rate,max_target_heart_rate,ultimate_max],...}
    outlier_dictionary={20:[100,170,200],
                        30:[95,162,90],
                        35:[93,157,185],
                        40:[90,153,180],
                        45:[88,149,175],
                        50:[85,145,170],
                        60:[80,136,160]}

    traditional_output=0.85*outlier_dictionary[age][2]
    traditional_minimum=outlier_dictionary[age][1]
    if heart_rate>traditional_output:
        return 2
    elif heart_rate<traditional_output and heart_rate>traditional_minimum:
        return 1
    else:
        return 0
    #Output Format: 2 for OverWorked, 1 for Decent Work, 0 for Underworked
    
