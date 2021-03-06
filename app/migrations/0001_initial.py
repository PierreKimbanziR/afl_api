# Generated by Django 3.1.4 on 2020-12-16 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('playerId', models.IntegerField(primary_key=True, serialize=False)),
                ('gamesPlayed', models.IntegerField()),
                ('players_details_givenName', models.CharField(max_length=200)),
                ('players_details_surname', models.CharField(max_length=200)),
                ('players_details_heightCm', models.IntegerField()),
                ('players_details_weightKg', models.IntegerField()),
                ('players_details_jumperNumber', models.IntegerField()),
                ('players_details_kickingFoot', models.CharField(max_length=200)),
                ('players_details_stateOfOrigin', models.CharField(max_length=200)),
                ('players_details_position', models.CharField(max_length=200)),
                ('players_details_photoURL', models.URLField()),
                ('team_teamName', models.CharField(max_length=200)),
                ('team_teamAbbr', models.CharField(max_length=200)),
                ('team_teamNickname', models.CharField(max_length=200)),
                ('team_teamId', models.IntegerField()),
                ('totals_matchesPlayed', models.IntegerField()),
                ('totals_timeOnGroundPercentage', models.IntegerField()),
                ('totals_behinds', models.IntegerField()),
                ('totals_bounces', models.IntegerField()),
                ('totals_centreClearances', models.IntegerField()),
                ('totals_clangers', models.IntegerField()),
                ('totals_contestDefLosses', models.IntegerField()),
                ('totals_contestDefLossPercentage', models.IntegerField()),
                ('totals_contestDefOneOnOnes', models.IntegerField()),
                ('totals_contestedMarks', models.IntegerField()),
                ('totals_contestedPossessionRate', models.IntegerField()),
                ('totals_contestedPossessions', models.IntegerField()),
                ('totals_contestOffOneOnOnes', models.IntegerField()),
                ('totals_contestOffWins', models.IntegerField()),
                ('totals_contestOffWinsPercentage', models.IntegerField()),
                ('totals_defHalfPressureActs', models.IntegerField()),
                ('totals_disposalEfficiency', models.IntegerField()),
                ('totals_disposals', models.IntegerField()),
                ('totals_dreamTeamPoints', models.IntegerField()),
                ('totals_effectiveDisposals', models.IntegerField()),
                ('totals_effectiveKicks', models.IntegerField()),
                ('totals_f50GroundBallGets', models.IntegerField()),
                ('totals_freesAgainst', models.IntegerField()),
                ('totals_freesFor', models.IntegerField()),
                ('totals_goalAccuracy', models.IntegerField()),
                ('totals_goalAssists', models.IntegerField()),
                ('totals_goals', models.IntegerField()),
                ('totals_groundBallGets', models.IntegerField()),
                ('totals_handballs', models.IntegerField()),
                ('totals_hitouts', models.IntegerField()),
                ('totals_hitoutsToAdvantage', models.IntegerField()),
                ('totals_hitoutToAdvantageRate', models.IntegerField()),
                ('totals_hitoutWinPercentage', models.IntegerField()),
                ('totals_inside50s', models.IntegerField()),
                ('totals_interceptMarks', models.IntegerField()),
                ('totals_intercepts', models.IntegerField()),
                ('totals_kickEfficiency', models.IntegerField()),
                ('totals_kicks', models.IntegerField()),
                ('totals_kickToHandballRatio', models.IntegerField()),
                ('totals_marks', models.IntegerField()),
                ('totals_marksInside50', models.IntegerField()),
                ('totals_marksOnLead', models.IntegerField()),
                ('totals_metresGained', models.IntegerField()),
                ('totals_onePercenters', models.IntegerField()),
                ('totals_pressureActs', models.IntegerField()),
                ('totals_ranking', models.IntegerField()),
                ('totals_ratingPoints', models.IntegerField()),
                ('totals_rebound50s', models.IntegerField()),
                ('totals_ruckContests', models.IntegerField()),
                ('totals_scoreInvolvements', models.IntegerField()),
                ('totals_scoreLaunches', models.IntegerField()),
                ('totals_shotsAtGoal', models.IntegerField()),
                ('totals_spoils', models.IntegerField()),
                ('totals_stoppageClearances', models.IntegerField()),
                ('totals_tackles', models.IntegerField()),
                ('totals_tacklesInside50', models.IntegerField()),
                ('totals_totalClearances', models.IntegerField()),
                ('totals_totalPossessions', models.IntegerField()),
                ('totals_turnovers', models.IntegerField()),
                ('totals_uncontestedPossessions', models.IntegerField()),
                ('averages_matchesPlayed', models.IntegerField()),
                ('averages_timeOnGroundPercentage', models.IntegerField()),
                ('averages_behinds', models.IntegerField()),
                ('averages_bounces', models.IntegerField()),
                ('averages_centreClearances', models.IntegerField()),
                ('averages_clangers', models.IntegerField()),
                ('averages_contestDefLosses', models.IntegerField()),
                ('averages_contestDefLossPercentage', models.IntegerField()),
                ('averages_contestDefOneOnOnes', models.IntegerField()),
                ('averages_contestedMarks', models.IntegerField()),
                ('averages_contestedPossessionRate', models.IntegerField()),
                ('averages_contestedPossessions', models.IntegerField()),
                ('averages_contestOffOneOnOnes', models.IntegerField()),
                ('averages_contestOffWins', models.IntegerField()),
                ('averages_contestOffWinsPercentage', models.IntegerField()),
                ('averages_defHalfPressureActs', models.IntegerField()),
                ('averages_disposalEfficiency', models.IntegerField()),
                ('averages_disposals', models.IntegerField()),
                ('averages_dreamTeamPoints', models.IntegerField()),
                ('averages_effectiveDisposals', models.IntegerField()),
                ('averages_effectiveKicks', models.IntegerField()),
                ('averages_f50GroundBallGets', models.IntegerField()),
                ('averages_freesAgainst', models.IntegerField()),
                ('averages_freesFor', models.IntegerField()),
                ('averages_goalAccuracy', models.IntegerField()),
                ('averages_goalAssists', models.IntegerField()),
                ('averages_goals', models.IntegerField()),
                ('averages_groundBallGets', models.IntegerField()),
                ('averages_handballs', models.IntegerField()),
                ('averages_hitouts', models.IntegerField()),
                ('averages_hitoutsToAdvantage', models.IntegerField()),
                ('averages_hitoutToAdvantageRate', models.IntegerField()),
                ('averages_hitoutWinPercentage', models.IntegerField()),
                ('averages_inside50s', models.IntegerField()),
                ('averages_interceptMarks', models.IntegerField()),
                ('averages_intercepts', models.IntegerField()),
                ('averages_kickEfficiency', models.IntegerField()),
                ('averages_kicks', models.IntegerField()),
                ('averages_kickToHandballRatio', models.IntegerField()),
                ('averages_marks', models.IntegerField()),
                ('averages_marksInside50', models.IntegerField()),
                ('averages_marksOnLead', models.IntegerField()),
                ('averages_metresGained', models.IntegerField()),
                ('averages_onePercenters', models.IntegerField()),
                ('averages_pressureActs', models.IntegerField()),
                ('averages_ratingPoints', models.IntegerField()),
                ('averages_rebound50s', models.IntegerField()),
                ('averages_ruckContests', models.IntegerField()),
                ('averages_scoreInvolvements', models.IntegerField()),
                ('averages_scoreLaunches', models.IntegerField()),
                ('averages_shotsAtGoal', models.IntegerField()),
                ('averages_spoils', models.IntegerField()),
                ('averages_stoppageClearances', models.IntegerField()),
                ('averages_tackles', models.IntegerField()),
                ('averages_tacklesInside50', models.IntegerField()),
                ('averages_totalClearances', models.IntegerField()),
                ('averages_totalPossessions', models.IntegerField()),
                ('averages_turnovers', models.IntegerField()),
                ('averages_uncontestedPossessions', models.IntegerField()),
            ],
        ),
    ]
