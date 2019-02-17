if __name__ == "__main__":
    team = 'Real Madrid'
    num = 7729
    # Length
    print('len:', len(team))
    print(len(str(num)))
    # Indexing
    print(team[1], team[-1], team[1:5], team[::2])

    # team[0] = 'P' ERROR!!!
    pteam = 'P' + team[1:]
    print(pteam)

    # String Format
    print('%s is a good team.' % (team))
    print('{} lost today : {} - {}'.format(team, 2, 1))
    
    # Multiline String:
    multi_line_string = """First line
Second line
Third line"""
    print(multi_line_string) 