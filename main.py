from statemachine import StateMachine, State


class Process(StateMachine):
    # ===============================================Stany=========================================================
    Wjazd_cz_w_strefe_robocza = State('Wjazd części w strefę roboczą', initial=True)
    Spowolnienie_tasmy = State('Spowolnienie taśmy')
    Za_tas_zam_zatrzaskow = State('Zatrzymanie tasmy i zamkniecie zatrzaskow')
    S1_S2_ON = State('Zezwolenie na prace')
    Spra_poz_robota = State('Sprawdzenie pozycji robota')
    S1_S2_OFF = State('Wylaczenie zezwolenian prace robota i zwolnienie zatrzaskow')
    Tas_wl = State('Wylaczenie tasmy')
    # =============================================Przejscia=======================================================
    cz1_ON = Wjazd_cz_w_strefe_robocza.to(Spowolnienie_tasmy)
    cz2_ON = Spowolnienie_tasmy.to(Za_tas_zam_zatrzaskow)
    cz3_ON = Za_tas_zam_zatrzaskow.to(S1_S2_ON)
    RnL_H = S1_S2_ON.to(Spra_poz_robota)
    RnL_End = Spra_poz_robota.to(S1_S2_OFF)
    cz3_OFF = S1_S2_OFF.to(Tas_wl)
    cz1_2__OFF = Tas_wl.to(Wjazd_cz_w_strefe_robocza)


class Robot(StateMachine):
    # ===============================================Stany=========================================================

    Home = State('Pozycja domowa', initial=True)
    Sek_1 = State('Sekwencja 1')
    Sek_2 = State('Sekwencja 2')
    Awaria = State('Przygotowanie do ponownego wykonania')
    # =============================================Przejscia=======================================================
    Cycle1_ON = Home.to(Sek_1)
    Cycle2_ON = Home.to(Sek_2)
    Zasilanie_OFF = Sek_2.to(Awaria) & Sek_1.to(Awaria)  ######################### nie wiem czy tak może być
    Cycle1_OFF_Start_Cycle2 = Sek_1.to(Sek_2)


class Bezpieczenstwo(StateMachine):
    # ===============================================Stany=========================================================
    Praca = State('Praca ukladu', initial=True)
    Przypal = State('Zadzialanie zabezpieczen')
    Powrot = State('Powrot do procesu')
    # =============================================Przejscia=======================================================
    Awaria=Praca.to(Przypal)
    Safety_OK=Przypal.to(Powrot)
    Praca_procesu=Powrot.to(Praca)


