f = open('delete.sql', 'w')

for i in range(100):
    f.write('ALTER TABLE user_channel_tab_' + str(i).zfill(8) + ' DROP COLUMN tag_uniq;\n')

f.write('ALTER TABLE online_stream_tab DROP COLUMN tag_uniq;\n')
f.write('ALTER TABLE stream_log_tab DROP COLUMN tag_uniq;\n')
f.write('ALTER TABLE playback_log_tab DROP COLUMN tag_uniq;\n')

for i in range(100):
    f.write('ALTER TABLE channel_playback_tab_' + str(i).zfill(8) + ' DROP COLUMN tag_uniq;\n')

for i in range(100):
    f.write('ALTER TABLE playback_info_tab_' + str(i).zfill(8) + ' DROP COLUMN tag_uniq;\n')

f.write('ALTER TABLE stream_settings_tab DROP COLUMN tag_uniq;\n')

for i in range(100):
    f.write('ALTER TABLE clan_playback_tab_' + str(i).zfill(8) + ' DROP COLUMN tag_uniq;\n')
