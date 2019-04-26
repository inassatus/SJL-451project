CREATE OR REPLACE FUNCTION reviewed() RETURNS trigger AS '
BEGIN

	UPDATE businessTable
	SET reviewcount = businessTable.reviewcount+1
	where businessTable.business_id=NEW.business_id;
	UPDATE userTable
	SET reviewcount = userTable.reviewcount+1
	where userTable.user_id=NEW.user_id;

	return NEW;
END
' LANGUAGE plpgsql;

CREATE TRIGGER reviewing
AFTER INSERT ON review
FOR EACH ROW
EXECUTE PROCEDURE reviewed();

CREATE OR REPLACE FUNCTION checked() RETURNS trigger AS '
BEGIN
	UPDATE businessTable
	SET numCheckins = businessTable.numCheckins+NEW.count
	where businessTable.business_id = NEW.business_id;

	return NEW;
END
' LANGUAGE plpgsql;

CREATE TRIGGER checking
AFTER INSERT ON checkins
FOR EACH ROW
EXECUTE PROCEDURE checked();