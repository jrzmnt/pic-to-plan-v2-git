(define (problem cut-cucumber-1)
(:domain cut-cucumber)
(:objects
    <insert_objects>
);end objects
;TODO choose if insert most recent state in tree or just a basic hardcoded one
	;TODO How to handle that the hands must be active always?

	;TODO choose if insert most recent state in tree or just a basic hardcoded one
(:init
    ;hands always active and empty at start???
    (hand_empty r_hand)
    (hand_empty l_hand)
	(active r_hand)
	(active l_hand)
	;end hands active
    <insert_class_memberships>
    ;<insert_init>
);end init

(:goal (and (grasped cucumber1) (open drawer1))
);end goal

);end define