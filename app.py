from flask import Flask, render_template, request, session
import os
from yourappdb import query_db, get_db
from flask import g

app = Flask(__name__)
app.secret_key="any string"
def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()
init_db()

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route("/")
def hello_world():
    user = query_db('select * from contacts')
    the_username = "anonyme"
    one_user = query_db('select * from contacts where first_name = ?',
                [the_username], one=True)
    return render_template("hey.html", users=user, one_user=one_user, the_title="my title")
@app.route("/add_one_user", methods=["GET","POST"])
def add_one_user():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        touslescountry= query_db("select * from country")

        touslesjob= query_db("select * from job")

        one_user = query_db("insert into user (username,country_id,email,password,phone,job_id) values (:username,:country_id,:email,:password,:phone,:job_id)",hey)
        user = query_db('select * from user')

        last_user = query_db("select * from user where email = ? and password = ?",[hey["email"], hey["password"]], one=True)
        session["current_user_id"]=last_user["id"]
        for x in ['username','country_id','email','password','phone','job_id']:
            session[x]=hey[x]


        return render_template("userform.html", users=user, one_user=one_user, the_title="add new user", touslescountry=touslescountry, touslesjob=touslesjob)


    touslescountry= query_db("select * from country")

    touslesjob= query_db("select * from job")

    user = query_db('select * from user')
    one_user = query_db("select * from user limit 1", one=True)
    return render_template("userform.html", users=user, one_user=one_user, the_title="add new user", touslescountry=touslescountry, touslesjob=touslesjob)


@app.route("/user_sign_out", methods=["GET","POST"])
def user_sign_out():
    if request.method == 'POST':
        session["current_user_id"]=""
        for x in ['username','country_id','email','password','phone','job_id']:
            session[x]=""
        return redirect("/")


@app.route("/user_log_in", methods=["GET","POST"])
def user_login():
    if request.method == 'POST':
        hey=request.form
        last_user = query_db("select * from user where email = ? and password = ?",[hey["email"], hey["password"]], one=True)
        try:
            session["current_user_id"]=last_user["id"]
            for x in ['username','country_id','email','password','phone','job_id']:
                session[x]=hey[x]
        except:
            return render_template("userlogin.html")
    return render_template("userlogin.html")
@app.route("/add_one_commit_dating", methods=["GET","POST"])
def add_one_commit_dating():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        touslesuser= query_db("select * from user")

        one_user = query_db("insert into commit_dating (user_id,description) values (:user_id,:description)",hey)
        user = query_db('select * from commit_dating')

        return render_template("commit_datingform.html", commit_datings=user, one_user=one_user, the_title="add new commit_dating", touslesuser=touslesuser)


    touslesuser= query_db("select * from user")

    user = query_db('select * from commit_dating')
    one_user = query_db("select * from commit_dating limit 1", one=True)
    return render_template("commit_datingform.html", commit_datings=user, one_user=one_user, the_title="add new commit_dating", touslesuser=touslesuser)

@app.route("/add_one_country", methods=["GET","POST"])
def add_one_country():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        one_user = query_db("insert into country (name) values (:name)",hey)
        user = query_db('select * from country')

        return render_template("countryform.html", countrys=user, one_user=one_user, the_title="add new country")


    user = query_db('select * from country')
    one_user = query_db("select * from country limit 1", one=True)
    return render_template("countryform.html", countrys=user, one_user=one_user, the_title="add new country")

@app.route("/add_one_programminglanguage", methods=["GET","POST"])
def add_one_programminglanguage():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        one_user = query_db("insert into programminglanguage (name) values (:name)",hey)
        user = query_db('select * from programminglanguage')

        return render_template("programminglanguageform.html", programminglanguages=user, one_user=one_user, the_title="add new programminglanguage")


    user = query_db('select * from programminglanguage')
    one_user = query_db("select * from programminglanguage limit 1", one=True)
    return render_template("programminglanguageform.html", programminglanguages=user, one_user=one_user, the_title="add new programminglanguage")

@app.route("/add_one_job", methods=["GET","POST"])
def add_one_job():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        one_user = query_db("insert into job (name) values (:name)",hey)
        user = query_db('select * from job')

        return render_template("jobform.html", jobs=user, one_user=one_user, the_title="add new job")


    user = query_db('select * from job')
    one_user = query_db("select * from job limit 1", one=True)
    return render_template("jobform.html", jobs=user, one_user=one_user, the_title="add new job")

@app.route("/add_one_commit_coding", methods=["GET","POST"])
def add_one_commit_coding():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        touslesprogramminglanguage= query_db("select * from programminglanguage")

        touslesuser= query_db("select * from user")

        one_user = query_db("insert into commit_coding (programminglanguage_id,user_id,title,content) values (:programminglanguage_id,:user_id,:title,:content)",hey)
        user = query_db('select * from commit_coding')

        return render_template("commit_codingform.html", commit_codings=user, one_user=one_user, the_title="add new commit_coding", touslesprogramminglanguage=touslesprogramminglanguage, touslesuser=touslesuser)


    touslesprogramminglanguage= query_db("select * from programminglanguage")

    touslesuser= query_db("select * from user")

    user = query_db('select * from commit_coding')
    one_user = query_db("select * from commit_coding limit 1", one=True)
    return render_template("commit_codingform.html", commit_codings=user, one_user=one_user, the_title="add new commit_coding", touslesprogramminglanguage=touslesprogramminglanguage, touslesuser=touslesuser)

@app.route("/add_one_migration_trip", methods=["GET","POST"])
def add_one_migration_trip():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        touslesuser= query_db("select * from user")

        one_user = query_db("insert into migration_trip (destination,user_id) values (:destination,:user_id)",hey)
        user = query_db('select * from migration_trip')

        return render_template("migration_tripform.html", migration_trips=user, one_user=one_user, the_title="add new migration_trip", touslesuser=touslesuser)


    touslesuser= query_db("select * from user")

    user = query_db('select * from migration_trip')
    one_user = query_db("select * from migration_trip limit 1", one=True)
    return render_template("migration_tripform.html", migration_trips=user, one_user=one_user, the_title="add new migration_trip", touslesuser=touslesuser)

@app.route("/add_one_migration_database", methods=["GET","POST"])
def add_one_migration_database():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        touslesuser= query_db("select * from user")

        touslesmigration_trip= query_db("select * from migration_trip")

        one_user = query_db("insert into migration_database (user_id,content,migration_trip_id) values (:user_id,:content,:migration_trip_id)",hey)
        user = query_db('select * from migration_database')

        return render_template("migration_databaseform.html", migration_databases=user, one_user=one_user, the_title="add new migration_database", touslesuser=touslesuser, touslesmigration_trip=touslesmigration_trip)


    touslesuser= query_db("select * from user")

    touslesmigration_trip= query_db("select * from migration_trip")

    user = query_db('select * from migration_database')
    one_user = query_db("select * from migration_database limit 1", one=True)
    return render_template("migration_databaseform.html", migration_databases=user, one_user=one_user, the_title="add new migration_database", touslesuser=touslesuser, touslesmigration_trip=touslesmigration_trip)

@app.route("/add_one_artist", methods=["GET","POST"])
def add_one_artist():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        one_user = query_db("insert into artist (name) values (:name)",hey)
        user = query_db('select * from artist')

        return render_template("artistform.html", artists=user, one_user=one_user, the_title="add new artist")


    user = query_db('select * from artist')
    one_user = query_db("select * from artist limit 1", one=True)
    return render_template("artistform.html", artists=user, one_user=one_user, the_title="add new artist")

@app.route("/add_one_musicvideo", methods=["GET","POST"])
def add_one_musicvideo():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        one_user = query_db("insert into musicvideo (artist_composer,title) values (:artist_composer,:title)",hey)
        user = query_db('select * from musicvideo')

        return render_template("musicvideoform.html", musicvideos=user, one_user=one_user, the_title="add new musicvideo")


    user = query_db('select * from musicvideo')
    one_user = query_db("select * from musicvideo limit 1", one=True)
    return render_template("musicvideoform.html", musicvideos=user, one_user=one_user, the_title="add new musicvideo")

@app.route("/add_one_artisthasmusicvideo", methods=["GET","POST"])
def add_one_artisthasmusicvideo():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        touslesmusicvideo= query_db("select * from musicvideo")

        touslesartist= query_db("select * from artist")

        one_user = query_db("insert into artisthasmusicvideo (musicvideo_id,artist_id) values (:musicvideo_id,:artist_id)",hey)
        user = query_db('select * from artisthasmusicvideo')

        return render_template("artisthasmusicvideoform.html", artisthasmusicvideos=user, one_user=one_user, the_title="add new artisthasmusicvideo", touslesmusicvideo=touslesmusicvideo, touslesartist=touslesartist)


    touslesmusicvideo= query_db("select * from musicvideo")

    touslesartist= query_db("select * from artist")

    user = query_db('select * from artisthasmusicvideo')
    one_user = query_db("select * from artisthasmusicvideo limit 1", one=True)
    return render_template("artisthasmusicvideoform.html", artisthasmusicvideos=user, one_user=one_user, the_title="add new artisthasmusicvideo", touslesmusicvideo=touslesmusicvideo, touslesartist=touslesartist)

@app.route("/add_one_gossip", methods=["GET","POST"])
def add_one_gossip():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        touslesuser= query_db("select * from user")

        one_user = query_db("insert into gossip (content,user_id) values (:content,:user_id)",hey)
        user = query_db('select * from gossip')

        return render_template("gossipform.html", gossips=user, one_user=one_user, the_title="add new gossip", touslesuser=touslesuser)


    touslesuser= query_db("select * from user")

    user = query_db('select * from gossip')
    one_user = query_db("select * from gossip limit 1", one=True)
    return render_template("gossipform.html", gossips=user, one_user=one_user, the_title="add new gossip", touslesuser=touslesuser)

@app.route("/add_one_artisthasgossip", methods=["GET","POST"])
def add_one_artisthasgossip():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        touslesgossip= query_db("select * from gossip")

        touslesartist= query_db("select * from artist")

        one_user = query_db("insert into artisthasgossip (gossip_id,artist_id) values (:gossip_id,:artist_id)",hey)
        user = query_db('select * from artisthasgossip')

        return render_template("artisthasgossipform.html", artisthasgossips=user, one_user=one_user, the_title="add new artisthasgossip", touslesgossip=touslesgossip, touslesartist=touslesartist)


    touslesgossip= query_db("select * from gossip")

    touslesartist= query_db("select * from artist")

    user = query_db('select * from artisthasgossip')
    one_user = query_db("select * from artisthasgossip limit 1", one=True)
    return render_template("artisthasgossipform.html", artisthasgossips=user, one_user=one_user, the_title="add new artisthasgossip", touslesgossip=touslesgossip, touslesartist=touslesartist)

