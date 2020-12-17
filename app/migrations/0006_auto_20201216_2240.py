# Generated by Django 3.1.4 on 2020-12-16 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20201216_2237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='averages_behinds',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='player',
            name='averages_bounces',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='player',
            name='averages_centreClearances',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='player',
            name='averages_clangers',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='player',
            name='averages_contestDefLossPercentage',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='player',
            name='averages_contestDefLosses',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='player',
            name='averages_contestDefOneOnOnes',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='player',
            name='averages_contestOffOneOnOnes',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='player',
            name='averages_contestOffWins',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='player',
            name='averages_contestOffWinsPercentage',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='player',
            name='averages_contestedMarks',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='player',
            name='averages_contestedPossessionRate',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='player',
            name='averages_contestedPossessions',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='player',
            name='averages_defHalfPressureActs',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='player',
            name='averages_disposalEfficiency',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='player',
            name='averages_disposals',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='player',
            name='averages_dreamTeamPoints',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='player',
            name='averages_effectiveDisposals',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='player',
            name='averages_effectiveKicks',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='player',
            name='averages_f50GroundBallGets',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='player',
            name='averages_freesAgainst',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='player',
            name='averages_freesFor',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='player',
            name='averages_goalAccuracy',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='player',
            name='averages_goalAssists',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='player',
            name='averages_goals',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='player',
            name='averages_groundBallGets',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='player',
            name='averages_handballs',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='player',
            name='averages_hitoutToAdvantageRate',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='player',
            name='averages_hitoutWinPercentage',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='player',
            name='averages_hitouts',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='player',
            name='averages_hitoutsToAdvantage',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='player',
            name='averages_inside50s',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='player',
            name='averages_interceptMarks',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='player',
            name='averages_intercepts',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='player',
            name='averages_kickEfficiency',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='player',
            name='averages_kickToHandballRatio',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='player',
            name='averages_kicks',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='player',
            name='averages_marks',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='player',
            name='averages_marksInside50',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='player',
            name='averages_marksOnLead',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='player',
            name='averages_matchesPlayed',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='player',
            name='averages_metresGained',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='player',
            name='averages_onePercenters',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='player',
            name='averages_pressureActs',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='player',
            name='averages_ratingPoints',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='player',
            name='averages_rebound50s',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='player',
            name='averages_ruckContests',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='player',
            name='averages_scoreInvolvements',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='player',
            name='averages_scoreLaunches',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='player',
            name='averages_shotsAtGoal',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='player',
            name='averages_spoils',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='player',
            name='averages_stoppageClearances',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='player',
            name='averages_tackles',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='player',
            name='averages_tacklesInside50',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='player',
            name='averages_timeOnGroundPercentage',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='player',
            name='averages_totalClearances',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='player',
            name='averages_totalPossessions',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='player',
            name='averages_turnovers',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='player',
            name='averages_uncontestedPossessions',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='player',
            name='totals_behinds',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='player',
            name='totals_bounces',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='player',
            name='totals_centreClearances',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='player',
            name='totals_clangers',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='player',
            name='totals_contestDefLossPercentage',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='player',
            name='totals_contestDefLosses',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='player',
            name='totals_contestDefOneOnOnes',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='player',
            name='totals_contestOffOneOnOnes',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='player',
            name='totals_contestOffWins',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='player',
            name='totals_contestOffWinsPercentage',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='player',
            name='totals_contestedMarks',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='player',
            name='totals_contestedPossessionRate',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='player',
            name='totals_contestedPossessions',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='player',
            name='totals_defHalfPressureActs',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='player',
            name='totals_disposalEfficiency',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='player',
            name='totals_disposals',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='player',
            name='totals_dreamTeamPoints',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='player',
            name='totals_effectiveDisposals',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='player',
            name='totals_effectiveKicks',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='player',
            name='totals_f50GroundBallGets',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='player',
            name='totals_freesAgainst',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='player',
            name='totals_freesFor',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='player',
            name='totals_goalAccuracy',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='player',
            name='totals_goalAssists',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='player',
            name='totals_goals',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='player',
            name='totals_groundBallGets',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='player',
            name='totals_handballs',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='player',
            name='totals_hitoutToAdvantageRate',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='player',
            name='totals_hitoutWinPercentage',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='player',
            name='totals_hitouts',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='player',
            name='totals_hitoutsToAdvantage',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='player',
            name='totals_inside50s',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='player',
            name='totals_interceptMarks',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='player',
            name='totals_intercepts',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='player',
            name='totals_kickEfficiency',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='player',
            name='totals_kickToHandballRatio',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='player',
            name='totals_kicks',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='player',
            name='totals_marks',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='player',
            name='totals_marksInside50',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='player',
            name='totals_marksOnLead',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='player',
            name='totals_matchesPlayed',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='player',
            name='totals_metresGained',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='player',
            name='totals_onePercenters',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='player',
            name='totals_pressureActs',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='player',
            name='totals_ranking',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='player',
            name='totals_ratingPoints',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='player',
            name='totals_rebound50s',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='player',
            name='totals_ruckContests',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='player',
            name='totals_scoreInvolvements',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='player',
            name='totals_scoreLaunches',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='player',
            name='totals_shotsAtGoal',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='player',
            name='totals_spoils',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='player',
            name='totals_stoppageClearances',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='player',
            name='totals_tackles',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='player',
            name='totals_tacklesInside50',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='player',
            name='totals_timeOnGroundPercentage',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='player',
            name='totals_totalClearances',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='player',
            name='totals_totalPossessions',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='player',
            name='totals_turnovers',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='player',
            name='totals_uncontestedPossessions',
            field=models.FloatField(),
        ),
    ]
