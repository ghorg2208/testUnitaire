def test_average():
    # liste d'entrée
    input1 = [11, -11, 10, 20]

    # Définit le résultat attendu
    expected_result = 7.5

    # Appeler la fonction average et stocker le résultat
    from lib import average
    actual_result = average(input1)

    # Vérifier que le résultat attendu est égal au résultat actuel
    assert expected_result == actual_result

# Appeler la fonction de test
test_average()