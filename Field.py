import random


class FieldClass:
    def __init__(self):
        self.list_field = ['fire_area', 'water_area', 'forest_area', 'snow_area']
        # self.field_monster_population()
        # self.field_hp_monster()
        monster_cnt, hp_monster_ = self.field_monster_population()
        self.dict_user_gard = dict()

        # 지역 몬스터 리스트
        self.dict_field_monster = {'fire_area': {'survival': True, 'int_cnt': monster_cnt, 'hp': hp_monster_,
                                                 'attack': ['fire_attack', 0.05], 'skill': ['fire_ball', 0.10]},
                                   'water_area': {'survival': True, 'int_cnt': monster_cnt, 'hp': hp_monster_,
                                                  'attack': ['aqua_attack', 0.05], 'skill': ['aqua_ball', 0.10]},
                                   'forest_area': {'survival': True, 'int_cnt': monster_cnt, 'hp': hp_monster_,
                                                   'attack': ['air_attack', 0.05], 'skill': ['air_ball', 0.10]},
                                   'snow_area': {'survival': True, 'int_cnt': monster_cnt, 'hp': hp_monster_,
                                                 'attack': ['snow_attack', 0.05], 'skill': ['snow_ball', 0.10]}}
        # 이동 중 아이템 드랍 리스트
        self.list_move_drop = ['hp_potion_high', 'hp_potion_middle', 'hp_potion_low', 'mp_potion_high',
                               'mp_potion_middle', 'mp_potion_low', 'all_potion_high', 'all_potion_middle',
                               'all_potion_low']

        # 획득한 장비 리스트

        self.move_meet_equipment = ['black_armor', 'black_cape', 'black_glove', 'black_pants', 'blue_armor', 'blue_cape',
                               'blue_glove','blue_hood', 'blue_pants', 'bronze_armor', 'bronze_bow', 'bronze_pants',
                               'bronze_shield', 'bronze_staff', 'bronze_sword', 'bronze_wand', 'chain_armor',
                               'chain_pants', 'chain_shield', 'cow_armor', 'cow_cape', 'cow_glove', 'cow_helmet',
                               'cow_pants', 'croc_cape', 'croc_glove', 'diamond_gem', 'gold_armor', 'gold_bow',
                               'gold_helmet', 'gold_pants', 'gold_staff', 'gold_sword', 'gold_wand', 'high_chain_glove',
                               'horse_armor', 'horse_cape', 'horse_glove', 'horse_helmet', 'horse_pants', 'iron_armor',
                               'iron_pants', 'iron_shield', 'leather_shield', 'low_chain_glove', 'middle_chain_glove',
                               'red_armor', 'red_cape', 'red_glove', 'red_hood', 'red_pants', 'ruby_gem', 'silver_armor',
                               'silver_bow', 'silver_helmet', 'silver_pants', 'silver_staff', 'silver_sword',
                               'silver_wand', 'stone_gem']


        # 턴수 11번째에 던전입구 재생성
        self.trun = 0

    def field_monster_population(self):  # 1~10 마리 뽑기
        rand_monster_population_ = random.randint(1, 10)
        monster_population_hp = random.sample(range(200, 1000), k=rand_monster_population_)
        return rand_monster_population_, monster_population_hp

    def field_hp_monster(self):  # 몬스터 랜덤 체력
        rand_hp_monster = random.randint(200, 1000)
        print(f"일반 몬스터의 체력 {rand_hp_monster}")
        return rand_hp_monster

    def field_move_random_drop(self):  # 필드 이동 중 랜덤 드랍
        list_move_drop = []
        list_drop = random.choice(self.list_move_drop)
        list_move_drop.append(list_drop)
        print(f"이동중 포션 획득 {list_move_drop} 획득")
        return list_move_drop

    def field_meet_ally_gard(self):  # 아군 수호대 조우
        rand_num = random.randint(1, 3)
        list_drop_ = []
        drop_item = random.choices(self.list_move_drop, k= rand_num)
        list_eq_drop = random.choices(self.move_meet_equipment,k= rand_num)
        print(f"아군 수호대 조우 {drop_item} 포션 획득")
        print(f"아군 수호대 조우 {list_eq_drop} 장비 획득")

        list_drop_ += drop_item
        list_drop_ += list_eq_drop
        print(list_drop_)
        return list_drop_

    # if self.turn <= 10: # 10 턴 마다 던전입구 재생성
    def random_maze_door(self):  # 랜덤한 위치에 던전 입구 생성
        rand_maze_door = random.randint(1, 20)
        rand_maze_door_ = random.randint(1, 20)
        print(f"랜덤 던전 좌표 X {rand_maze_door} Y {rand_maze_door_}")

        return rand_maze_door, rand_maze_door_

    def field_meet_enemy_gard(self, str_my_gard):
        self.int_hp_up = 1.2
        self.list_enemy_lvs = [15, 16, 17, 18, 19, 20]
        self.list_enemy_lvs_ = random.choice(self.list_enemy_lvs)

        if str_my_gard == 'light_gard':
            str_enemy_gard = random.choice(['moon_gard', 'star_gard', 'forest_gard'])
        elif str_my_gard == 'moon_gard':
            str_enemy_gard = random.choice(['light_gard', 'star_gard', 'forest_gard'])
        elif str_my_gard == 'star_gard':
            str_enemy_gard = random.choice(['light_gard', 'moon_gard', 'forest_gard'])
        elif str_my_gard == 'forest_gard':
            str_enemy_gard = random.choice(['light_gard', 'star_gard', 'moon_gard'])

        self.dict_user_gard = {'gard': str_my_gard,
                               'warrior': {'lv': 1, 'hp': 300, 'mp': 0, 'power': 200,
                                           'skill': {10: 'slice_chop'}},
                               'archer': {'lv': 1, 'hp': 300, 'mp': 0, 'power': 300,
                                          'skill': {10: 'target_shot',
                                                    15: 'dual_shot',
                                                    20: 'master_shot'}},
                               'swordman': {'lv': 1, 'hp': 300, 'mp': 0, 'power': 250,
                                            'skill': {10: 'slice_chop'}},
                               'wizard_red': {'lv': 1, 'hp': 300, 'mp': 0, 'power': 150,
                                              'skill': {1: ['heal_normal', 'fire_ball'],
                                                        15: ['heal_greater', 'fire_wall'],
                                                        20: 'thunder_breaker',
                                                        25: 'bilzzard',
                                                        30: 'heal_all'}},
                               'wizard_black': {'lv': 1, 'hp': 300, 'mp': 0, 'power': 200,
                                                'skill': {1: 'fire_ball',
                                                          15: 'fire_wall',
                                                          20: 'thunder_breaker',
                                                          25: 'bilzzard'}},
                               'wizard_white': {'lv': 1, 'hp': 300, 'mp': 0, 'power': 100,
                                                'skill': {1: 'heal_normal',
                                                          15: 'heal_greater',
                                                          30: 'heal_all'}}}

        self.dict_enemy_gard = {'gard': str_enemy_gard,
                                'warrior': {'lv': self.list_enemy_lvs_, 'hp': 300 * self.int_hp_up, 'mp': 0,
                                            'skill': {10: 'slice_chop'}, 'power': 200},
                                'archer': {'lv': self.list_enemy_lvs_, 'hp': 150 * self.int_hp_up, 'mp': 150 * self.int_hp_up,
                                           'power': 300,
                                           'skill': {10: 'target_shot',
                                                     15: 'dual_shot',
                                                     20: 'master_shot'}},
                                'swordman': {'lv': self.list_enemy_lvs_, 'hp': 150 * self.int_hp_up, 'mp': 150 * self.int_hp_up,
                                             'power': 250,
                                             'skill': {10: 'slice_chop'}},
                                'wizard_red': {'lv': self.list_enemy_lvs_, 'hp': 150 * self.int_hp_up, 'mp': 100 * self.int_hp_up,
                                               'power': 150,
                                               'skill': {1: ['heal_normal', 'fire_ball'],
                                                         15: ['heal_greater', 'fire_wall'],
                                                         20: 'thunder_breaker',
                                                         25: 'bilzzard',
                                                         30: 'heal_all'}},
                                'wizard_black': {'lv': self.list_enemy_lvs_, 'hp': 200 * self.int_hp_up, 'mp': 150 * self.int_hp_up,
                                                 'power': 200,
                                                 'skill': {1: 'fire_ball',
                                                           15: 'fire_wall',
                                                           20: 'thunder_breaker',
                                                           25: 'bilzzard'}},
                                'wizard_white': {'lv': self.list_enemy_lvs_, 'hp': 200 * self.int_hp_up, 'mp': 150 * self.int_hp_up,
                                                 'power': 100,
                                                 'skill': {1: 'heal_normal',
                                                           15: 'heal_greater',
                                                           30: 'heal_all'}}}

        return self.dict_enemy_gard, self.dict_user_gard

    def field_move_event(self):  # 이동 중 이벤트 발생
        ratio = random.randint(1, 100)
        if ratio <= 10:
            print('Tent 획득')
            return '텐트', ['tent']

        elif 10 < ratio <= 20:
            print('아군수호대 조우')
            return '아군수호대', self.field_meet_ally_gard()

        elif 20 < ratio <= 30:
            print('적군수호대 조우')
            self.trun += 1
            self.bool_meet_gard = True
            return '적군수호대', self.field_meet_enemy_gard('moon_gard'), self.bool_meet_gard

        elif 30 < ratio <= 50:
            print('아이템')
            return '아이템', self.field_move_random_drop()

        elif 50 < ratio <= 80:
            print('몬스터 출현')
            self.bool_meet_monster = True
            self.trun += 1
            return '일반몬스터', self.bool_meet_monster
            # 전투전 좌표 저장
        elif 80 < ratio <= 100:
            print('이동')

    # def back_position(self): # 도망 , 전투 후 전투전 위치로
    # 몬스터 출현 했을때 좌표 저장했을때의 위치로 돌아가기

    # def fire_monster_match(self):
    #     print(self.dict_field_monster['fire_area'])

    # def water_monster_match(self):
    #     self.dict_field_monster['water_area']
    #     print(self.dict_field_monster['water_area'])
    #
    # def forest_monster_match(self):
    #     self.dict_field_monster['forest_area']
    #     print(self.dict_field_monster['forest_area'])
    #
    # def snow_monster_match(self):
    #     self.dict_field_monster['snow_area']
    #     print(self.dict_field_monster['snow_area'])


# def random_maze_door(self): # 랜덤한 위치에 던전 입구 생성
#     # if self.turn <= 10: # 10 턴 마다 던전입구 재생성
#     rand_maze_door = random.randint(0, 20)
#     rand_maze_door_ = random.randint(0, 20)
#     print(f"랜덤 던전 좌표 X {rand_maze_door} Y {rand_maze_door_}")


a = FieldClass()
f=a.field_move_event()
print(f)
# a.field_monster_population()
# a.field_hp_monster()
# a.field_move_random_drop()
# a.field_meet_ally_gard
# a.field_monster_population()
# a.random_maze_door()
#
