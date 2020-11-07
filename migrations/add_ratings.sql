alter table films
    add column win INTEGER DEFAULT 0;
alter table films
    add column lose INTEGER DEFAULT 0;
alter table films
    add column rating REAL NOT NULL DEFAULT 0;